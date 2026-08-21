"""Render a route-walk slide's animated map segment to an .mp4 clip.

Local dev tool only - not part of the deployed Jekyll site. Draws the
same route-walk data (map tile, path, nodes, labels) used by the live
Watch widget onto video frames with PIL, then encodes them with ffmpeg.
Mirrors the CSS/SVG live renderer's math independently rather than
sharing code - see the design spec's "Architecture" section for why
(same duality already used for the existing pan/zoom slides).

IMPORTANT: node/path coordinates below must be kept in sync by hand with
the matching post's inline <script> if either one changes - see
docs/superpowers/specs/2026-08-20-route-walk-animation-design.md.

Requires: pip install pillow
ffmpeg must be on PATH.

Usage:
    python scripts/render_route_clip.py \
        --tile assets/images/jalan-payoh-lai-route-map.png \
        --out preview-motion/jalan-payoh-lai-route-walk.mp4 \
        --duration 25.05
"""
import argparse
import io
import subprocess
import sys

from PIL import Image, ImageDraw, ImageEnhance, ImageFilter, ImageFont

# Route data - must match the "route-walk" slide entry in
# _posts/2026-08-16-jalan-payoh-lai-kangkar-montfort-nativity-church.md
NODES = [
    {"x": 72, "y": 560, "label": "Jalan Payoh Lai", "delay_s": 0.1},
    {"x": 145, "y": 548, "label": "Upper Serangoon Rd Junction", "delay_s": 1.5},
    {"x": 210, "y": 460, "label": "Holy Innocents' Lane", "delay_s": 4.0},
    {"x": 272, "y": 385, "label": "Montfort School", "delay_s": 6.5},
]
# Cubic Bezier control points (start, c1, c2, end) per segment - same
# curve as the "d" attribute on the live SVG path.
PATH_SEGMENTS = [
    ((72, 560), (95, 555), (120, 552), (145, 548)),
    ((145, 548), (175, 543), (190, 510), (210, 460)),
    ((210, 460), (230, 410), (250, 400), (272, 385)),
]
ROUTE_COLOR = (226, 87, 46)      # #e2572e
HALO_COLOR = (253, 246, 232)     # #fdf6e8
CREDIT_TEXT = "Map data © OpenStreetMap contributors"


def cubic_bezier_points(p0, p1, p2, p3, n=40):
    points = []
    for i in range(n + 1):
        t = i / n
        mt = 1 - t
        x = (mt ** 3) * p0[0] + 3 * (mt ** 2) * t * p1[0] + 3 * mt * (t ** 2) * p2[0] + (t ** 3) * p3[0]
        y = (mt ** 3) * p0[1] + 3 * (mt ** 2) * t * p1[1] + 3 * mt * (t ** 2) * p2[1] + (t ** 3) * p3[1]
        points.append((x, y))
    return points


def full_path_points():
    points = [PATH_SEGMENTS[0][0]]
    for p0, p1, p2, p3 in PATH_SEGMENTS:
        points.extend(cubic_bezier_points(p0, p1, p2, p3)[1:])
    return points


def resize_cover(img, canvas_w, canvas_h):
    """Resize+crop to fill canvas_w x canvas_h without distortion - the
    PIL equivalent of CSS background-size:cover, matching the live
    letterbox background layer's behavior."""
    scale = max(canvas_w / img.width, canvas_h / img.height)
    new_w, new_h = int(img.width * scale) + 1, int(img.height * scale) + 1
    resized = img.resize((new_w, new_h))
    left, top = (new_w - canvas_w) // 2, (new_h - canvas_h) // 2
    return resized.crop((left, top, left + canvas_w, top + canvas_h))


def load_font(size):
    for candidate in ("arialbd.ttf", "Arial Bold.ttf", "DejaVuSans-Bold.ttf"):
        try:
            return ImageFont.truetype(candidate, size)
        except OSError:
            continue
    return ImageFont.load_default()


def compose_frame(tile, canvas_w, canvas_h, elapsed_s, anim_s):
    progress = min(1.0, elapsed_s / anim_s) if anim_s > 0 else 1.0
    scale = min(canvas_w / tile.width, canvas_h / tile.height)
    disp_w, disp_h = int(tile.width * scale), int(tile.height * scale)
    off_x, off_y = (canvas_w - disp_w) // 2, (canvas_h - disp_h) // 2

    bg = resize_cover(tile, canvas_w, canvas_h)
    bg = bg.filter(ImageFilter.GaussianBlur(18))
    bg = ImageEnhance.Brightness(bg).enhance(0.42)

    frame = bg.convert("RGB")
    frame.paste(tile.resize((disp_w, disp_h)), (off_x, off_y))
    frame = frame.convert("RGBA")

    draw = ImageDraw.Draw(frame)

    def to_canvas(pt):
        return (off_x + pt[0] * scale, off_y + pt[1] * scale)

    pts = [to_canvas(p) for p in full_path_points()]
    n_shown = max(2, int(len(pts) * progress))
    shown = pts[:n_shown]

    draw.line(shown, fill=HALO_COLOR + (217,), width=max(1, int(4 * scale)), joint="curve")
    draw.line(shown, fill=ROUTE_COLOR + (255,), width=max(1, int(2 * scale)), joint="curve")

    for node in NODES:
        cx, cy = to_canvas((node["x"], node["y"]))
        r = 3.5 * scale
        draw.ellipse([cx - r, cy - r, cx + r, cy + r], fill=ROUTE_COLOR + (255,), outline=HALO_COLOR + (255,), width=2)

    if shown:
        mx, my = shown[-1]
        r = 3.5 * scale
        draw.ellipse([mx - r * 2, my - r * 2, mx + r * 2, my + r * 2], fill=ROUTE_COLOR + (77,))
        draw.ellipse([mx - r, my - r, mx + r, my + r], fill=ROUTE_COLOR + (255,))

    font = load_font(max(12, int(16 * scale)))
    for node in NODES:
        if elapsed_s < node["delay_s"]:
            continue
        cx, cy = to_canvas((node["x"], node["y"]))
        label = node["label"]
        bbox = draw.textbbox((0, 0), label, font=font)
        pad = 6
        w, h = bbox[2] - bbox[0] + pad * 2, bbox[3] - bbox[1] + pad * 2
        lx, ly = cx - w / 2, cy - h - 14
        draw.rounded_rectangle([lx, ly, lx + w, ly + h], radius=4, fill=(0, 0, 0, 153))
        draw.text((lx + pad, ly + pad), label, font=font, fill=(255, 255, 255, 255))

    credit_font = load_font(max(10, int(11 * scale)))
    credit_w = draw.textlength(CREDIT_TEXT, font=credit_font)
    draw.rectangle([8, 8, 8 + credit_w + 12, 30], fill=(0, 0, 0, 115))
    draw.text((14, 12), CREDIT_TEXT, font=credit_font, fill=(255, 255, 255, 166))

    return frame.convert("RGB")


def render(tile_path, out_path, duration_s, anim_s, width, height, fps):
    tile = Image.open(tile_path).convert("RGB")
    total_frames = int(duration_s * fps)

    proc = subprocess.Popen(
        ["ffmpeg", "-y", "-f", "image2pipe", "-vcodec", "png", "-r", str(fps), "-i", "-",
         "-vcodec", "libx264", "-pix_fmt", "yuv420p", "-r", str(fps), out_path],
        stdin=subprocess.PIPE,
    )

    for frame_i in range(total_frames):
        t = frame_i / fps
        frame = compose_frame(tile, width, height, t, anim_s)
        buf = io.BytesIO()
        frame.save(buf, format="PNG")
        proc.stdin.write(buf.getvalue())

    proc.stdin.close()
    proc.wait()
    if proc.returncode != 0:
        print(f"ffmpeg exited with code {proc.returncode}", file=sys.stderr)
        sys.exit(1)
    print(f"Wrote {out_path}: {total_frames} frames @ {fps}fps, {duration_s}s")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--tile", required=True, help="path to the OSM tile image")
    parser.add_argument("--out", required=True, help="output .mp4 path")
    parser.add_argument("--duration", type=float, required=True, help="total clip length in seconds")
    parser.add_argument("--anim-seconds", type=float, default=7.0, help="how long the route takes to draw before holding static")
    parser.add_argument("--width", type=int, default=1920)
    parser.add_argument("--height", type=int, default=1080)
    parser.add_argument("--fps", type=int, default=30)
    args = parser.parse_args()
    render(args.tile, args.out, args.duration, args.anim_seconds, args.width, args.height, args.fps)


if __name__ == "__main__":
    main()
