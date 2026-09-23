"""Render assets/images/opium-local-map.png - the static PNG of the local
Singapore-places map for the video/Watch "chart" slide.

Mirrors the post's inline .om-card map SVG: the real OpenStreetMap extract
already saved at assets/images/osm-opium-network-singapore.jpg, with the
same five place pins as scratch/opium/gen_map_singapore.py (not re-derived,
to avoid a fresh set of pixel-math mistakes).

    python scripts/render_opium_local_map.py
"""
import sys
from pathlib import Path

from PIL import Image, ImageDraw

sys.path.insert(0, str(Path(__file__).resolve().parent))
from watch_video_lib import CHART_BG, CHART_MUTED, CHART_SECONDARY, CHART_TEXT, load_font  # noqa: E402

BASE = Path(__file__).resolve().parent.parent
SRC = BASE / "assets" / "images" / "osm-opium-network-singapore.jpg"
OUT = BASE / "assets" / "images" / "opium-local-map.png"
W, H = 1280, 720
SS = 2

SERIES_1 = (57, 135, 229)  # #3987e5, dark-mode --series-1

TITLE = "Places in the story, on the ground"
SUB = "Locations are approximate; the map beneath them is a real OpenStreetMap extract of Singapore"
FOOT = "Map data © OpenStreetMap contributors."

# Node coordinates in the source image's own 1221x571 pixel space
# (scratch/opium/gen_map_singapore.py).
CHINATOWN = (762, 305)
HONG_LIM_PARK = (728, 258)
HAVELOCK_RD = (652, 243)
QUEEN_ST = (792, 198)
PASIR_PANJANG = (418, 350)

MAP_X, MAP_Y, MAP_W, MAP_H = 40, 140, 1200, 540


def render():
    src = Image.open(SRC).convert("RGB")
    sw, sh = src.size
    scale_final = max(MAP_W / sw, MAP_H / sh)
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

    px, py = mp(PASIR_PANJANG)
    cx, cy = mp(CHINATOWN)
    dash_len, gap_len = 8 * SS, 6 * SS
    length = ((cx - px) ** 2 + (cy - py) ** 2) ** 0.5
    n = max(1, int(length / (dash_len + gap_len)))
    for i in range(n):
        t0 = i / n
        t1 = min(1, t0 + dash_len / length)
        d.line([(px + (cx - px) * t0, py + (cy - py) * t0),
                (px + (cx - px) * t1, py + (cy - py) * t1)], fill=(*SERIES_1, 90), width=max(1, SS))

    for pt in (CHINATOWN, HONG_LIM_PARK, HAVELOCK_RD, QUEEN_ST, PASIR_PANJANG):
        x, y = mp(pt)
        d.ellipse([x - 6 * SS, y - 6 * SS, x + 6 * SS, y + 6 * SS], fill=SERIES_1, outline=CHART_BG, width=SS)

    node_font = load_font(int(19 * SS))

    def label(pt, text, dx, dy, anchor):
        x, y = mp(pt)
        d.text((x + dx * SS, y + dy * SS), text, font=node_font, fill=CHART_TEXT, anchor=anchor,
               stroke_width=max(2, 3 * SS), stroke_fill=CHART_BG)

    label(CHINATOWN, "Chinatown / South Bridge Rd", 12, 5, "lm")
    label(HONG_LIM_PARK, "Hong Lim Park", 12, -10, "lm")
    label(HAVELOCK_RD, "Havelock Road", -12, 5, "rm")
    label(QUEEN_ST, "Queen Street", 0, -18, "mm")
    label(PASIR_PANJANG, "Pasir Panjang", 0, 24, "mm")

    title_font = load_font(int(34 * SS))
    sub_font = load_font(int(19 * SS), bold=False)
    foot_font = load_font(int(15 * SS), bold=False)

    margin = 40 * SS
    d.text((margin, 40 * SS), TITLE, font=title_font, fill=CHART_TEXT)
    d.text((margin, 84 * SS), SUB, font=sub_font, fill=CHART_SECONDARY)
    d.text((margin, 690 * SS), FOOT, font=foot_font, fill=CHART_MUTED)

    canvas = canvas.resize((W, H), Image.LANCZOS)
    OUT.parent.mkdir(parents=True, exist_ok=True)
    canvas.save(OUT)
    print(f"wrote {OUT}  ({W}x{H})")


if __name__ == "__main__":
    render()
