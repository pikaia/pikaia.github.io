"""Render assets/images/opium-regional-map.png - the static PNG of the
Singapore-centred regional opium network map for the video/Watch "chart"
slide.

Mirrors the post's inline .om-card map SVG: the real OpenStreetMap extract
already saved at assets/images/osm-opium-network-asia.jpg, with the same
long-haul supply routes (Bombay/Calcutta -> Singapore -> South China coast)
and Great Syndicate farm territories (Melaka/Johor/Riau) drawn on top, using
the same node coordinates as scratch/opium/gen_map.py (not re-derived, to
avoid a fresh set of pixel-math mistakes).

    python scripts/render_opium_regional_map.py
"""
import sys
from pathlib import Path

from PIL import Image, ImageDraw

sys.path.insert(0, str(Path(__file__).resolve().parent))
from watch_video_lib import CHART_BG, CHART_MUTED, CHART_SECONDARY, CHART_TEXT, load_font  # noqa: E402

BASE = Path(__file__).resolve().parent.parent
SRC = BASE / "assets" / "images" / "osm-opium-network-asia.jpg"
OUT = BASE / "assets" / "images" / "opium-regional-map.png"
W, H = 1280, 720
SS = 2

SERIES_1 = (57, 135, 229)   # #3987e5, dark-mode --series-1
SERIES_2 = (31, 166, 31)    # #1fa61f, dark-mode --series-2

TITLE = "Singapore, the hub of two opium networks"
SUB = "Routes are approximate and not to scale; the map beneath them is a real OpenStreetMap extract"
FOOT = "Map data © OpenStreetMap contributors. Routes and farm territories are schematic."

# Node coordinates in the source image's own 1140x550 pixel space
# (scratch/opium/gen_map.py).
BOMBAY = (370, 210)
CALCUTTA = (490, 165)
CHINA = (895, 151)
SINGAPORE = (737, 385)
MELAKA = (650, 340)
JOHOR = (733, 345)
RIAU = (765, 435)

MAP_X, MAP_Y, MAP_W, MAP_H = 40, 140, 1200, 540  # placement of the map inside the frame


def cubic(a, b, t):
    mx, my = (a[0] + b[0]) / 2, a[1] + (b[1] - a[1]) * 0.35
    ex, ey = b[0] - (b[0] - a[0]) * 0.25, (a[1] + b[1]) / 2
    p0, p1, p2, p3 = a, (mx, my), (ex, ey), b
    u = 1 - t
    x = u**3 * p0[0] + 3 * u**2 * t * p1[0] + 3 * u * t**2 * p2[0] + t**3 * p3[0]
    y = u**3 * p0[1] + 3 * u**2 * t * p1[1] + 3 * u * t**2 * p2[1] + t**3 * p3[1]
    return x, y


def render():
    src = Image.open(SRC).convert("RGB")
    sw, sh = src.size
    scale_final = max(MAP_W / sw, MAP_H / sh)  # cover-crop into the MAP_W x MAP_H box
    resized = src.resize((round(sw * scale_final), round(sh * scale_final)), Image.LANCZOS)
    left = (resized.width - MAP_W) // 2
    top = (resized.height - MAP_H) // 2
    resized = resized.crop((left, top, left + MAP_W, top + MAP_H))

    canvas = Image.new("RGB", (W * SS, H * SS), CHART_BG)
    map_ss = resized.resize((resized.width * SS, resized.height * SS), Image.LANCZOS)
    canvas.paste(map_ss, (MAP_X * SS, MAP_Y * SS))

    d = ImageDraw.Draw(canvas, "RGBA")

    def mp(pt):
        return ((MAP_X + pt[0] * scale_final - left) * SS,
                (MAP_Y + pt[1] * scale_final - top) * SS)

    for a, b in [(CALCUTTA, SINGAPORE), (BOMBAY, SINGAPORE), (SINGAPORE, CHINA)]:
        pts = [mp(cubic(a, b, t / 24)) for t in range(25)]
        d.line(pts, fill=SERIES_1, width=max(2, 3 * SS), joint="curve")
    for pt in (BOMBAY, CALCUTTA, CHINA):
        x, y = mp(pt)
        d.ellipse([x - 6 * SS, y - 6 * SS, x + 6 * SS, y + 6 * SS], fill=SERIES_1, outline=CHART_BG, width=SS)

    for dest in (MELAKA, JOHOR, RIAU):
        x0, y0 = mp(SINGAPORE)
        x1, y1 = mp(dest)
        length = ((x1 - x0) ** 2 + (y1 - y0) ** 2) ** 0.5
        n = max(2, int(length / (10 * SS)))
        for i in range(n):
            if i % 2:
                continue
            t0, t1 = i / n, min(1, (i + 0.6) / n)
            d.line([(x0 + (x1 - x0) * t0, y0 + (y1 - y0) * t0),
                    (x0 + (x1 - x0) * t1, y0 + (y1 - y0) * t1)], fill=SERIES_2, width=max(2, 3 * SS))
    for pt in (MELAKA, JOHOR, RIAU):
        x, y = mp(pt)
        d.ellipse([x - 5 * SS, y - 5 * SS, x + 5 * SS, y + 5 * SS], fill=SERIES_2, outline=CHART_BG, width=SS)

    sx, sy = mp(SINGAPORE)
    d.ellipse([sx - 7 * SS, sy - 7 * SS, sx + 7 * SS, sy + 7 * SS], fill=CHART_TEXT, outline=CHART_BG, width=SS)

    node_font = load_font(int(20 * SS))
    node_sub_font = load_font(int(15 * SS), bold=False)
    sing_font = load_font(int(23 * SS))

    def label(pt, text, dx, dy, anchor, font=node_font, fill=CHART_TEXT):
        x, y = mp(pt)
        d.text((x + dx * SS, y + dy * SS), text, font=font, fill=fill, anchor=anchor,
               stroke_width=max(2, 3 * SS), stroke_fill=CHART_BG)

    label(BOMBAY, "Bombay", 12, -10, "lm")
    label(BOMBAY, "Malwa opium auctions", 12, 12, "lm", font=node_sub_font, fill=CHART_SECONDARY)
    label(CALCUTTA, "Calcutta", 12, -10, "lm")
    label(CALCUTTA, "Bengal opium auctions", 12, 12, "lm", font=node_sub_font, fill=CHART_SECONDARY)
    label(CHINA, "South China coast", 12, 5, "lm")
    label(MELAKA, "Melaka", -12, -10, "rm")
    label(JOHOR, "Johor", 0, -18, "mm")
    label(RIAU, "Riau", 12, 20, "lm")
    label(SINGAPORE, "Singapore", 16, 6, "lm", font=sing_font)

    title_font = load_font(int(34 * SS))
    sub_font = load_font(int(19 * SS), bold=False)
    legend_font = load_font(int(17 * SS), bold=False)
    foot_font = load_font(int(15 * SS), bold=False)

    margin = 40 * SS
    d.text((margin, 34 * SS), TITLE, font=title_font, fill=CHART_TEXT)
    d.text((margin, 78 * SS), SUB, font=sub_font, fill=CHART_SECONDARY)
    ly = 108 * SS
    d.line([(margin, ly + 5 * SS), (margin + 26 * SS, ly + 5 * SS)], fill=SERIES_1, width=max(2, 3 * SS))
    d.text((margin + 34 * SS, ly + 5 * SS), "Long-haul supply route, India to China",
            font=legend_font, fill=CHART_SECONDARY, anchor="lm")
    lx2 = margin + 470 * SS
    for i in range(0, 26, 8):
        d.line([(lx2 + i * SS, ly + 5 * SS), (lx2 + (i + 4) * SS, ly + 5 * SS)], fill=SERIES_2, width=max(2, 3 * SS))
    d.text((lx2 + 34 * SS, ly + 5 * SS), "The Great Syndicate's regional farm territories, 1871–79",
            font=legend_font, fill=CHART_SECONDARY, anchor="lm")

    d.text((margin, 690 * SS), FOOT, font=foot_font, fill=CHART_MUTED)

    canvas = canvas.resize((W, H), Image.LANCZOS)
    OUT.parent.mkdir(parents=True, exist_ok=True)
    canvas.save(OUT)
    print(f"wrote {OUT}  ({W}x{H})")


if __name__ == "__main__":
    render()
