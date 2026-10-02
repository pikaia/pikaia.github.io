"""Render the avatar bubble as a transparent video track (pipeline step 6a).

    python scripts/render_avatar_track.py --config scripts/video-configs/<slug>.py

Reads the config's AVATAR settings, audio/<slug>.avatar.json (step 1.5)
and the PNG layers in assets/avatar/png/, and writes
preview-motion/<slug>-avatar.mov: a bubble-sized qtrle ARGB video the full
length of the main video, transparent outside AVATAR's ranges and faded
at their edges, so step 6b can lay it over <slug>.mp4 frame for frame.
A config without AVATAR is skipped (exit 0). Single process; the work per
frame is stacking three small images, so memory stays tiny.
"""

import argparse
import subprocess
import sys
from pathlib import Path

from PIL import Image

sys.path.insert(0, str(Path(__file__).resolve().parent))
from avatar_lib import (  # noqa: E402
    BLINK_FRAMES, LAYER_NAMES, PNG_DIR, REPO_ROOT, alpha_at, avatar_settings,
    bubble_geometry, load_mouth_file, mouth_path_for_config, video_dims,
)
from watch_video_lib import load_config  # noqa: E402


def load_layers(diameter, png_dir=PNG_DIR):
    png_dir = Path(png_dir)
    layers = {}
    for name in LAYER_NAMES:
        path = png_dir / f"{name}.png"
        if not path.exists():
            raise FileNotFoundError(f"missing avatar layer {path} - run python scripts/build_avatar.py")
        layers[name] = Image.open(path).convert("RGBA").resize((diameter, diameter), Image.LANCZOS)
    return layers


def mouth_layer_for(level, shape):
    """Silence always closes the mouth; otherwise a shaped mouth (M F U E)
    beats the loudness level; otherwise the level picks the opening."""
    if level == 0:
        return "mouth-0"
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


def blink_frame_set(blinks):
    return {f for b in blinks for f in range(b, b + BLINK_FRAMES)}


def default_track_path(config_path):
    return REPO_ROOT / "preview-motion" / f"{Path(config_path).stem}-avatar.mov"


def render_track(cfg, out_path, png_dir=PNG_DIR):
    settings = avatar_settings(cfg)
    if settings is None:
        print("No AVATAR in this config - step 6a skipped.")
        return False
    out_w, out_h, fps = video_dims(cfg)
    track = load_mouth_file(mouth_path_for_config(cfg), fps, cfg.TOTAL_DURATION)
    d, _, _ = bubble_geometry(settings, out_w, out_h)
    layers = load_layers(d, png_dir)
    blinking = blink_frame_set(track["blinks"])
    mouth = track["mouth"]
    shape = track.get("shape")
    total_frames = int(cfg.TOTAL_DURATION * fps)  # same count watch_video_lib.render() uses
    blank = bytes(d * d * 4)
    cache = {}

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
                continue
            j = min(i, len(mouth) - 1)
            key = (mouth_layer_for(int(mouth[j]), shape[j] if shape else "."), i in blinking)
            if key not in cache:
                cache[key] = compose_avatar(layers, *key)
            proc.stdin.write(with_alpha(cache[key], a).tobytes())
            if i % (fps * 60) == 0:
                print(f"frame {i}/{total_frames} t={i / fps:.0f}s", file=sys.stderr)
    finally:
        proc.stdin.close()
        proc.wait()
    if proc.returncode != 0:
        raise RuntimeError(f"ffmpeg exited {proc.returncode} writing {out_path}")
    print(f"Wrote {out_path} - {total_frames} frames, {d}x{d}, ranges {settings['ranges']}")
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
