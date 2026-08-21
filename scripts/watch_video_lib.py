"""Shared engine for rendering a post's Watch-widget slideshow to video.

Local dev tool only - not part of the deployed Jekyll site. Renders a Ken
Burns slideshow (pan/zoom over images, narration audio, burned-in captions)
frame-by-frame with PIL, piped to ffmpeg - the same technique used for
scripts/render_route_clip.py, chosen over ffmpeg's own zoompan filter
because zoompan's internal integer-position panning produced a "hold a few
frames then jump" jerky artifact that was hard to debug from the outside
(see docs/superpowers/ history / project memory for the original diagnosis).

This module used to be copy-pasted fresh into a scratch directory for each
post (lks-video/build_video.py, syonan-video/build_video.py, ...). That's
exactly how a real jerky-panning regression slipped back in on 2026-08-21:
a fix landed in one copy and not the others. This is now the single copy -
per-post data lives in scripts/video-configs/<slug>.py instead, imported by
this module's CLI, so every post automatically gets the current engine.

Usage:
    python scripts/watch_video_lib.py --config scripts/video-configs/<slug>.py --out OUT.mp4
    python scripts/watch_video_lib.py --config scripts/video-configs/<slug>.py --check-only

Config module contract (see scripts/video-configs/ for real examples):
    IMAGES: dict[str, str]      - key -> Commons/https URL, or a site-root
                                   path starting with "/" (resolved against
                                   the repo root), or a path relative to the
                                   config file's own directory.
    SLIDES: list[dict]          - {"img": key, "type": "cover"|"letterbox",
                                    "zoom": [z0,z1,z2], "pan": [(x,y)x3]}
                                   ("ease" may be present for parity with the
                                   live widget's slides array; unused here -
                                   see the docstring above cover_crop.)
    SCHEDULE: list[(t, slide_index)]
    TOTAL_DURATION: float
    TIMING_JSON: str             - path to the post's <slug>.timing.json,
                                    relative to the repo root.
    WIDTH, HEIGHT, FPS: int      - optional, default 1280x720x25.
    CAPTION_FONT_RATIO, CAPTION_MAX_WIDTH_FRAC, CAPTION_Y_FRAC: float
                                  - optional caption-box sizing overrides,
                                    e.g. a vertical Shorts config wants a
                                    smaller font ratio / higher box position
                                    than the default landscape values.
"""
import argparse
import functools
import hashlib
import importlib.util
import io
import json
import re
import subprocess
import sys
import urllib.request
from pathlib import Path

from PIL import Image, ImageDraw, ImageEnhance, ImageFilter, ImageFont

REPO_ROOT = Path(__file__).resolve().parent.parent
CACHE_DIR = REPO_ROOT / ".video-cache"
WORK_SCALE = 4
USER_AGENT = "pikaia-blog-tool/1.0 (https://pikaia.github.io; chriskslee@gmail.com)"

DEFAULT_CAPTION_FONT_RATIO = 0.045
DEFAULT_CAPTION_MAX_WIDTH_FRAC = 0.82
DEFAULT_CAPTION_Y_FRAC = 0.82


def load_config(config_path):
    config_path = Path(config_path).resolve()
    spec = importlib.util.spec_from_file_location(config_path.stem, config_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    module._config_dir = config_path.parent
    return module


@functools.lru_cache(maxsize=None)
def load_source(img_ref, config_dir):
    if img_ref.startswith("http://") or img_ref.startswith("https://"):
        CACHE_DIR.mkdir(exist_ok=True)
        digest = hashlib.sha256(img_ref.encode("utf-8")).hexdigest()[:16]
        suffix = Path(img_ref.split("?")[0]).suffix or ".img"
        cache_path = CACHE_DIR / f"{digest}{suffix}"
        if not cache_path.exists():
            req = urllib.request.Request(img_ref, headers={"User-Agent": USER_AGENT})
            with urllib.request.urlopen(req, timeout=30) as resp:
                data = resp.read()
            cache_path.write_bytes(data)
        path = cache_path
    elif img_ref.startswith("/"):
        path = REPO_ROOT / img_ref.lstrip("/")
    else:
        path = Path(config_dir) / img_ref
    return Image.open(path).convert("RGB")


@functools.lru_cache(maxsize=None)
def load_font(size, bold=True):
    candidates = ("arialbd.ttf", "Arial Bold.ttf") if bold else ("arial.ttf", "Arial.ttf")
    for candidate in candidates:
        try:
            return ImageFont.truetype(candidate, size)
        except OSError:
            continue
    return ImageFont.load_default()


def interp3(v0, v1, v2, t):
    if t <= 0.5:
        return v0 + (v1 - v0) * (t / 0.5)
    return v1 + (v2 - v1) * ((t - 0.5) / 0.5)


def prepare_source(img, out_w, out_h, max_zoom, work_scale=WORK_SCALE):
    # Pre-scale into a work_scale-multiplied coordinate space sized for this
    # slide's largest zoom. A low-res source (e.g. a 490x341 archival scan)
    # cover-scaled straight to the output size leaves very little pan slack
    # (sometimes under 200px total) - a 5-15% pan of that over hundreds of
    # frames is well under 1px/frame, so naive per-frame cropping holds the
    # same integer pixel for many consecutive frames then jumps: the exact
    # same "jerky panning" failure mode as ffmpeg zoompan's historical bug,
    # just reached through fresh-per-frame PIL resizes instead of zoompan's
    # internal state. Supersampling first (same fix as that bug) gives many
    # more distinct integer positions to move through. Diagnosed and fixed
    # 2026-08-21 on the Syonan Jinja post; see project memory for the full
    # writeup and the pixel-slack math.
    work_w, work_h = out_w * work_scale, out_h * work_scale
    scale = max(work_w / img.width, work_h / img.height) * max_zoom
    new_w, new_h = int(img.width * scale) + 1, int(img.height * scale) + 1
    resized = img.resize((new_w, new_h), Image.LANCZOS)
    return resized, work_w, work_h


def crop_from_prepared(prepared, work_w, work_h, out_w, out_h, zoom, max_zoom, pan_x, pan_y):
    win_w = int(work_w * max_zoom / zoom)
    win_h = int(work_h * max_zoom / zoom)
    max_x = max(0, prepared.width - win_w)
    max_y = max(0, prepared.height - win_h)
    left = max(0, min(int(max_x * pan_x), max_x))
    top = max(0, min(int(max_y * pan_y), max_y))
    cropped = prepared.crop((left, top, left + win_w, top + win_h))
    return cropped.resize((out_w, out_h), Image.LANCZOS)


def cover_crop(img, out_w, out_h, zoom, pan_x, pan_y, work_scale=WORK_SCALE):
    # Single-shot convenience wrapper (prepare+crop at exactly this zoom) -
    # fine for one-off calls (letterbox background, standalone tests). For
    # per-frame animated panning across many frames, prepare once per slide
    # via prepare_source()/crop_from_prepared() instead - see render().
    prepared, work_w, work_h = prepare_source(img, out_w, out_h, zoom, work_scale)
    return crop_from_prepared(prepared, work_w, work_h, out_w, out_h, zoom, zoom, pan_x, pan_y)


def compose_letterbox_frame(img, out_w, out_h, zoom, pan_x, pan_y):
    # Mirrors the live widget exactly: only the blurred cover background is
    # Ken-Burns animated (pan/zoom); the contained foreground stays sharp
    # and static (inset 6%, background-size:contain, no animation target).
    bg = cover_crop(img, out_w, out_h, zoom, pan_x, pan_y)
    bg = bg.filter(ImageFilter.GaussianBlur(30))
    bg = ImageEnhance.Brightness(bg).enhance(0.55)
    fw, fh = out_w * 0.88, out_h * 0.88
    scale_fg = min(fw / img.width, fh / img.height)
    fg = img.resize((int(img.width * scale_fg), int(img.height * scale_fg)), Image.LANCZOS)
    fx, fy = (out_w - fg.width) // 2, (out_h - fg.height) // 2
    bg.paste(fg, (fx, fy))
    return bg


def wrap_text(text, font, draw, max_width):
    words = text.split(" ")
    lines, cur = [], ""
    for w in words:
        trial = (cur + " " + w).strip()
        if not cur or draw.textlength(trial, font=font) <= max_width:
            cur = trial
        else:
            lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines


def draw_caption(frame, text, out_w, out_h, font_ratio, max_width_frac, y_frac):
    draw = ImageDraw.Draw(frame, "RGBA")
    font = load_font(int(out_h * font_ratio))
    max_width = out_w * max_width_frac
    lines = wrap_text(text, font, draw, max_width)
    line_height = font.size * 1.3
    pad_x, pad_y = 16, 12
    widths = [draw.textlength(l, font=font) for l in lines]
    box_w = max(widths) + pad_x * 2
    box_h = line_height * len(lines) + pad_y * 2
    box_x = (out_w - box_w) / 2
    box_y = out_h * y_frac - box_h / 2
    draw.rounded_rectangle([box_x, box_y, box_x + box_w, box_y + box_h], radius=5, fill=(0, 0, 0, 140))
    for i, line in enumerate(lines):
        tx = box_x + (box_w - widths[i]) / 2
        ty = box_y + pad_y + i * line_height
        draw.text((tx, ty), line, font=font, fill=(255, 255, 255, 255))
    return frame


def load_captions(timing_path, max_chars=100):
    with open(timing_path, encoding="utf-8") as f:
        sentences = json.load(f)

    def split_long(text, offset, duration):
        if len(text) <= max_chars:
            return [{"text": text, "offset_s": offset, "duration_s": duration}]
        parts = re.split(r"(?<=[:;])\s+", text)
        chunks = []
        for p in parts:
            if len(p) <= max_chars:
                chunks.append(p)
                continue
            words = p.split(" ")
            cur = ""
            for w in words:
                if len((cur + " " + w).strip()) > max_chars:
                    chunks.append(cur.strip())
                    cur = w
                else:
                    cur = (cur + " " + w).strip()
            if cur:
                chunks.append(cur.strip())
        total_chars = sum(len(c) for c in chunks)
        result = []
        t = offset
        for c in chunks:
            share = duration * (len(c) / total_chars)
            result.append({"text": c, "offset_s": t, "duration_s": share})
            t += share
        return result

    chunks = []
    for s in sentences:
        chunks.extend(split_long(s["text"], s["offset_s"], s["duration_s"]))
    return chunks


def slide_for_time(t, schedule, total_duration):
    idx = schedule[0][1]
    start = schedule[0][0]
    for st, si in schedule:
        if st <= t:
            idx, start = si, st
        else:
            break
    end = total_duration
    for st, si in schedule:
        if st > start:
            end = st
            break
    return idx, start, end


def build_prepared_cache(cfg, out_w, out_h):
    # One supersampled prepare per slide (not per frame) - see
    # prepare_source()'s docstring for why. Skipped for letterbox slides,
    # which prepare fresh per frame inside compose_letterbox_frame (only
    # matters if a letterbox slide also pans - none observed so far; the
    # foreground is always static so a letterbox slide's motion budget is
    # small regardless).
    cache = {}
    for i, slide in enumerate(cfg.SLIDES):
        if slide["type"] == "letterbox":
            continue
        src = load_source(cfg.IMAGES[slide["img"]], cfg._config_dir)
        max_zoom = max(slide["zoom"])
        cache[i] = (max_zoom,) + prepare_source(src, out_w, out_h, max_zoom)
    return cache


def compose_frame_at(t, out_w, out_h, cfg, captions, prepared_cache):
    slide_idx, seg_start, seg_end = slide_for_time(t, cfg.SCHEDULE, cfg.TOTAL_DURATION)
    slide = cfg.SLIDES[slide_idx]
    progress = min(1.0, max(0.0, (t - seg_start) / max(0.001, seg_end - seg_start)))
    zoom = interp3(*slide["zoom"], progress)
    pan_x = interp3(slide["pan"][0][0], slide["pan"][1][0], slide["pan"][2][0], progress)
    pan_y = interp3(slide["pan"][0][1], slide["pan"][1][1], slide["pan"][2][1], progress)
    if slide["type"] == "letterbox":
        src = load_source(cfg.IMAGES[slide["img"]], cfg._config_dir)
        frame = compose_letterbox_frame(src, out_w, out_h, zoom, pan_x, pan_y)
    else:
        max_zoom, prepared, work_w, work_h = prepared_cache[slide_idx]
        frame = crop_from_prepared(prepared, work_w, work_h, out_w, out_h, zoom, max_zoom, pan_x, pan_y)

    cap_text = None
    for c in captions:
        if c["offset_s"] <= t < c["offset_s"] + c["duration_s"]:
            cap_text = c["text"]
            break
    if cap_text:
        font_ratio = getattr(cfg, "CAPTION_FONT_RATIO", DEFAULT_CAPTION_FONT_RATIO)
        max_width_frac = getattr(cfg, "CAPTION_MAX_WIDTH_FRAC", DEFAULT_CAPTION_MAX_WIDTH_FRAC)
        y_frac = getattr(cfg, "CAPTION_Y_FRAC", DEFAULT_CAPTION_Y_FRAC)
        frame = draw_caption(frame, cap_text, out_w, out_h, font_ratio, max_width_frac, y_frac)
    return frame, slide_idx


def check_smoothness(cfg, duration=4.0, sample_slides=None):
    # Render a short slice of every requested slide through the exact same
    # compose_frame_at() code path the real render uses (critical - a
    # separate/simplified test path wouldn't actually validate the real
    # render), then flag any slide where consecutive frames go near-
    # identical for 2+ frames in a row as JERKY. Costs well under a minute;
    # run this before every full render, not just when something looks off.
    #
    # Caveat: a letterbox slide with zero pan (foreground pinned, matching
    # the live widget's design) will always read as JERKY here even when
    # genuinely fine - a static foreground dominates the pixel count and
    # suppresses the whole-frame diff regardless of how smoothly the
    # blurred background is actually zooming underneath it. Real jerkiness
    # only shows up on `cover` slides or any slide with actual pan
    # movement; treat a letterbox-with-zero-pan JERKY flag as expected, not
    # a signal to block the render on.
    import numpy as np

    out_w, out_h = getattr(cfg, "WIDTH", 1280), getattr(cfg, "HEIGHT", 720)
    fps = getattr(cfg, "FPS", 25)
    captions = load_captions(str(REPO_ROOT / cfg.TIMING_JSON))
    prepared_cache = build_prepared_cache(cfg, out_w, out_h)
    slide_starts = {s: t for t, s in cfg.SCHEDULE}
    targets = sample_slides if sample_slides is not None else range(len(cfg.SLIDES))

    any_bad = False
    for slide_idx in targets:
        start_t = slide_starts[slide_idx]
        n = int(duration * fps)
        frames = []
        for i in range(n):
            t = start_t + i / fps
            frame, actual_idx = compose_frame_at(t, out_w, out_h, cfg, captions, prepared_cache)
            if actual_idx != slide_idx:
                break  # slide shorter than `duration`
            arr = np.asarray(frame.convert("L"), dtype=np.int16)
            frames.append(arr)
        max_held_streak, streak = 0, 0
        held = 0
        for i in range(1, len(frames)):
            diff = np.abs(frames[i] - frames[i - 1]).mean()
            if diff < 0.05:
                held += 1
                streak += 1
                max_held_streak = max(max_held_streak, streak)
            else:
                streak = 0
        status = "JERKY" if max_held_streak >= 2 else "smooth"
        if max_held_streak >= 2:
            any_bad = True
        slide = cfg.SLIDES[slide_idx]
        print(f"slide {slide_idx} ({slide['img']}, {slide['type']}): "
              f"{held}/{max(1, len(frames)-1)} held-frame gaps, max consecutive streak {max_held_streak} -> {status}",
              file=sys.stderr)
    return not any_bad


def render(cfg, out_path):
    out_w, out_h = getattr(cfg, "WIDTH", 1280), getattr(cfg, "HEIGHT", 720)
    fps = getattr(cfg, "FPS", 25)
    captions = load_captions(str(REPO_ROOT / cfg.TIMING_JSON))
    total_frames = int(cfg.TOTAL_DURATION * fps)
    prepared_cache = build_prepared_cache(cfg, out_w, out_h)

    proc = subprocess.Popen(
        ["ffmpeg", "-y", "-f", "image2pipe", "-vcodec", "png", "-r", str(fps), "-i", "-",
         "-vcodec", "libx264", "-pix_fmt", "yuv420p", "-r", str(fps), "-preset", "medium",
         "-crf", "20", out_path],
        stdin=subprocess.PIPE,
    )

    for frame_i in range(total_frames):
        t = frame_i / fps
        frame, _ = compose_frame_at(t, out_w, out_h, cfg, captions, prepared_cache)

        buf = io.BytesIO()
        frame.save(buf, format="PNG")
        proc.stdin.write(buf.getvalue())

        if frame_i % 250 == 0:
            print(f"frame {frame_i}/{total_frames} t={t:.1f}s", file=sys.stderr)

    proc.stdin.close()
    proc.wait()
    if proc.returncode != 0:
        print(f"ffmpeg exited {proc.returncode}", file=sys.stderr)
        sys.exit(1)
    print(f"Wrote {out_path}", file=sys.stderr)


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--config", required=True, help="Path to a video config module (see scripts/video-configs/)")
    ap.add_argument("--out", help="Output .mp4 path (required unless --check-only)")
    ap.add_argument("--check-only", action="store_true", help="Run the smoothness pre-check and exit, no render")
    ap.add_argument("--check-duration", type=float, default=4.0, help="Seconds of test frames per slide for --check-only")
    args = ap.parse_args()

    cfg = load_config(args.config)

    if args.check_only:
        ok = check_smoothness(cfg, duration=args.check_duration)
        print("ALL SMOOTH" if ok else "SOME JERKY (see per-slide detail above; letterbox+zero-pan false positives are expected)", file=sys.stderr)
        sys.exit(0 if ok else 1)

    if not args.out:
        ap.error("--out is required unless --check-only is passed")
    render(cfg, args.out)


if __name__ == "__main__":
    main()
