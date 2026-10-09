"""Render the avatar bubble as a transparent video track (pipeline step 6a).

    python scripts/render_avatar_track.py --config scripts/video-configs/<slug>.py

Reads the config's AVATAR settings, audio/<slug>.avatar.json (step 1.5)
and the PNG layers for the AVATAR style (assets/avatar/png/ for the
cartoon, assets/avatar/photo/png/ for the photo version), and writes
preview-motion/<slug>-avatar.mov: a bubble-sized qtrle ARGB video the full
length of the main video, transparent outside AVATAR's ranges and faded
at their edges, so step 6b can lay it over <slug>.mp4 frame for frame.
A config without AVATAR is skipped (exit 0). Single process; the work per
frame is stacking three small images, so memory stays tiny.
"""

import argparse
import json
import subprocess
import sys
from pathlib import Path

import numpy as np
from PIL import Image

sys.path.insert(0, str(Path(__file__).resolve().parent))
from avatar_lib import (  # noqa: E402
    BLINK_FRAMES, LAYER_NAMES, MOTION_LAYER_NAMES, PNG_DIR, REPO_ROOT, STYLE_DIRS, alpha_at,
    avatar_settings, bubble_geometry, load_mouth_file, mouth_path_for_config, video_dims,
)
from avatar_motion import BREATH_SCALE, motion_curves, sentence_start_frames  # noqa: E402
from watch_video_lib import load_config  # noqa: E402


def load_layers(diameter, png_dir=PNG_DIR, names=LAYER_NAMES):
    png_dir = Path(png_dir)
    layers = {}
    for name in names:
        path = png_dir / f"{name}.png"
        if not path.exists():
            raise FileNotFoundError(f"missing avatar layer {path} - run python scripts/build_avatar.py")
        layers[name] = Image.open(path).convert("RGBA").resize((diameter, diameter), Image.LANCZOS)
    return layers


def mouth_layer_for(level, shape):
    """A shaped mouth (M F U E) wins, even on a frame the loudness meter
    calls silent: shapes only exist inside spoken sounds, and the sounds
    they mark are the quiet ones (the hiss of an f, the closure of m/b -
    on Barings 55% of f/v frames measured as silent). With no shape, the
    loudness level picks the opening, and level 0 (a pause) closes."""
    if shape in ("M", "F", "U", "E"):
        return f"mouth-{shape}"
    return f"mouth-{level}"


def compose_avatar(layers, mouth, eyes_closed):
    """mouth: a loudness level (0-3) or a layer name such as 'mouth-F'."""
    img = layers["body"].copy()
    img.alpha_composite(layers["eyes-closed" if eyes_closed else "eyes-open"])
    img.alpha_composite(layers[mouth if isinstance(mouth, str) else f"mouth-{mouth}"])
    return img


def with_alpha(img, a):
    if a >= 1.0:
        return img
    r, g, b, alpha = img.split()
    return Image.merge("RGBA", (r, g, b, alpha.point(lambda v: int(v * a))))


def hold_keys(keys, hold):
    """Per-frame layer keys with short runs absorbed: the bubble switches to
    a new key only when that key's run lasts at least `hold` frames (or it
    is the first frame); otherwise the current key carries on. hold=1 keeps
    every frame as it was."""
    if hold <= 1 or not keys:
        return list(keys)
    out, cur, i = [], keys[0], 0
    while i < len(keys):
        j = i
        while j < len(keys) and keys[j] == keys[i]:
            j += 1
        if j - i >= hold:
            cur = keys[i]
        out.extend([cur] * (j - i))
        i = j
    return out


# Motion frames are drawn at twice the bubble size and scaled down, so the
# sub-pixel sway and tilt stay smooth instead of stepping a pixel at a time.
MOTION_SS = 2
# The head tilts about the base of the neck (512-canvas coordinates).
HEAD_PIVOT = (256, 400)


def _shift(img, dx, dy):
    if not dx and not dy:
        return img
    return img.transform(img.size, Image.AFFINE, (1, 0, -dx, 0, 1, -dy), resample=Image.BILINEAR)


def compose_moving(layers, mouth, eyes_closed, p, size):
    """One motion frame at `size` px (the layers' size): shoulders breathe,
    the head (with brows, eyes, glasses and mouth) sways and tilts about the
    neck, the pupils glance and the brows lift. p holds this frame's curve
    values in 512-canvas units (avatar_motion.motion_curves)."""
    k = size / 512
    back = layers["back"]
    stretch = 1 + BREATH_SCALE * p["breath"]
    h = int(round(size * stretch))
    frame = Image.new("RGBA", (size, size), (0, 0, 0, 0))
    frame.alpha_composite(back if h == size else back.resize((size, h), Image.BILINEAR), (0, size - h))
    head = layers["head"].copy()
    head.alpha_composite(_shift(layers["brows"], 0, p["brow_dy"] * k))
    if eyes_closed:
        head.alpha_composite(layers["lids"])
    else:
        head.alpha_composite(_shift(layers["pupils"], p["pupil_dx"] * k, 0))
    head.alpha_composite(layers["glasses"])
    head.alpha_composite(layers[mouth if isinstance(mouth, str) else f"mouth-{mouth}"])
    if p["tilt"] or p["head_dx"] or p["head_dy"]:
        head = head.rotate(p["tilt"], resample=Image.BICUBIC, center=(HEAD_PIVOT[0] * k, HEAD_PIVOT[1] * k),
                           translate=(p["head_dx"] * k, p["head_dy"] * k))
    frame.alpha_composite(head)
    frame.alpha_composite(layers["rim"])
    # keep everything inside the bubble: the unstretched background is the
    # circle, and the rim's outer half sits just beyond it
    r, g, b, a = frame.split()
    bubble = np.maximum(np.asarray(back.getchannel("A")), np.asarray(layers["rim"].getchannel("A")))
    a = Image.fromarray(np.minimum(np.asarray(a), bubble))
    return Image.merge("RGBA", (r, g, b, a))


def blink_frame_set(blinks):
    return {f for b in blinks for f in range(b, b + BLINK_FRAMES)}


def default_track_path(config_path):
    return REPO_ROOT / "preview-motion" / f"{Path(config_path).stem}-avatar.mov"


def render_track(cfg, out_path, png_dir=None):
    settings = avatar_settings(cfg)
    if settings is None:
        print("No AVATAR in this config - step 6a skipped.")
        return False
    out_w, out_h, fps = video_dims(cfg)
    track = load_mouth_file(mouth_path_for_config(cfg), fps, cfg.TOTAL_DURATION)
    d, _, _ = bubble_geometry(settings, out_w, out_h)
    png_dir = png_dir or STYLE_DIRS[settings["style"]]
    motion = settings["motion"]
    if motion:
        layers = load_layers(d * MOTION_SS, png_dir, LAYER_NAMES + MOTION_LAYER_NAMES)
        timing_path = REPO_ROOT / cfg.TIMING_JSON
        timing = json.loads(timing_path.read_text(encoding="utf-8")) if timing_path.exists() else []
        curves = motion_curves(track["mouth"] if isinstance(track["mouth"], list) else [int(c) for c in track["mouth"]],
                               sentence_start_frames(timing, fps), fps, seed=Path(cfg.TIMING_JSON).stem)
    else:
        layers = load_layers(d, png_dir)
    blinking = blink_frame_set(track["blinks"])
    mouth = track["mouth"]
    shape = track.get("shape")
    total_frames = int(cfg.TOTAL_DURATION * fps)  # same count watch_video_lib.render() uses
    keys = hold_keys([mouth_layer_for(int(mouth[min(i, len(mouth) - 1)]),
                                      shape[min(i, len(mouth) - 1)] if shape else ".")
                      for i in range(total_frames)], settings["hold"])
    ease = settings["ease"]
    blank = bytes(d * d * 4)
    cache = {}
    eased = None  # float image the bubble is easing toward its target from

    out_path = Path(out_path)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    proc = subprocess.Popen(
        ["ffmpeg", "-y", "-v", "error", "-f", "rawvideo", "-pix_fmt", "rgba", "-s", f"{d}x{d}",
         "-r", str(fps), "-i", "-", "-c:v", "qtrle", "-pix_fmt", "argb", str(out_path)],
        stdin=subprocess.PIPE)
    try:
        for i in range(total_frames):
            a = alpha_at(i / fps, settings["ranges"], settings["fade"])
            if a <= 0.0:
                proc.stdin.write(blank)
                eased = None
                continue
            key = (keys[i], i in blinking)
            if motion:
                j = min(i, len(curves["tilt"]) - 1)
                p = {name: float(c[j]) for name, c in curves.items()}
                img = compose_moving(layers, *key, p, d * MOTION_SS).resize((d, d), Image.LANCZOS)
            else:
                if key not in cache:
                    cache[key] = compose_avatar(layers, *key)
                img = cache[key]
            if ease < 1.0:
                target = np.asarray(img, dtype=np.float32)
                eased = target if eased is None else eased + (target - eased) * ease
                img = Image.fromarray(np.rint(eased).astype(np.uint8), "RGBA")
            proc.stdin.write(with_alpha(img, a).tobytes())
            if i % (fps * 60) == 0:
                print(f"frame {i}/{total_frames} t={i / fps:.0f}s", file=sys.stderr)
    finally:
        proc.stdin.close()
        proc.wait()
    if proc.returncode != 0:
        raise RuntimeError(f"ffmpeg exited {proc.returncode} writing {out_path}")
    print(f"Wrote {out_path} - {total_frames} frames, {d}x{d}, {settings['style']}"
          f"{' + motion' if motion else ''}, ranges {settings['ranges']}")
    return True


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--config", required=True)
    ap.add_argument("--out", help="default: preview-motion/<config-stem>-avatar.mov")
    args = ap.parse_args()
    cfg = load_config(args.config)
    render_track(cfg, Path(args.out) if args.out else default_track_path(args.config))


if __name__ == "__main__":
    main()
