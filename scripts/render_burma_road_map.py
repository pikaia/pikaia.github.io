"""Render assets/images/burma-road-map.png for the Nanyang volunteers post.

Today's OpenStreetMap map of northern Burma and Yunnan (muted), with the
supply route the volunteers drove drawn on: by rail from Rangoon, where the
supplies were landed (off the map's southern edge), through Mandalay to the
railhead at Lashio, then the Burma Road through
Wanding on the border, Baoshan, Xiaguan and Chuxiong to Kunming. The road line
is hand-plotted through towns on the old route, an approximate stand-in for
the 1,146-km road, not a survey of it.

"Map data (c) OpenStreetMap contributors" is burned in and belongs in the
post's Sources list. Tiles are cached in scratch/brm/ after the first run.

    python scripts/render_burma_road_map.py
"""
import io
import math
import time
import urllib.request
from pathlib import Path

from PIL import Image, ImageDraw, ImageEnhance, ImageFont

ROOT = Path(__file__).resolve().parent.parent
CACHE = ROOT / "scratch" / "brm"
OUT = ROOT / "assets" / "images" / "burma-road-map.png"
UA = "LesserKnownSingapore-map-render/1.0 (one-off static map for a blog post)"

Z = 8
LAT_N, LAT_S = 26.4, 20.6
LON_W, LON_E = 94.6, 105.4
N = 2.0 ** Z


def _tx(lon):
    return (lon + 180) / 360 * N * 256


def _ty(lat):
    return (1 - math.asinh(math.tan(math.radians(lat))) / math.pi) / 2 * N * 256


X0, Y0 = _tx(LON_W), _ty(LAT_N)


def px(lat, lon):
    return (_tx(lon) - X0, _ty(lat) - Y0)


def base_tile():
    p = CACHE / "base_raw.png"
    if p.exists():
        return Image.open(p).convert("RGB")
    CACHE.mkdir(parents=True, exist_ok=True)
    x0, x1 = int(_tx(LON_W) / 256), int(_tx(LON_E) / 256)
    y0, y1 = int(_ty(LAT_N) / 256), int(_ty(LAT_S) / 256)
    img = Image.new("RGB", ((x1 - x0 + 1) * 256, (y1 - y0 + 1) * 256))
    for x in range(x0, x1 + 1):
        for y in range(y0, y1 + 1):
            req = urllib.request.Request(f"https://tile.openstreetmap.org/{Z}/{x}/{y}.png", headers={"User-Agent": UA})
            img.paste(Image.open(io.BytesIO(urllib.request.urlopen(req, timeout=30).read())).convert("RGB"),
                      ((x - x0) * 256, (y - y0) * 256))
            time.sleep(0.2)
    img = img.crop((int(X0 - x0 * 256), int(Y0 - y0 * 256), int(_tx(LON_E) - x0 * 256), int(_ty(LAT_S) - y0 * 256)))
    img.save(p)
    return img


def font(size, bold=False):
    for nm in (["arialbd.ttf"] if bold else ["arial.ttf"]) + ["DejaVuSans-Bold.ttf" if bold else "DejaVuSans.ttf"]:
        try:
            return ImageFont.truetype(nm, size)
        except OSError:
            continue
    return ImageFont.load_default()


# The railway north from Rangoon, entering from the map's southern edge.
RAIL = [(20.6, 96.05), (21.98, 96.08), (22.08, 96.47), (22.62, 97.30), (22.94, 97.75)]
# The Burma Road, through towns on the old route.
ROAD = [(22.94, 97.75), (23.30, 97.96), (23.45, 97.94), (23.98, 97.90), (24.08, 98.07),
        (24.43, 98.58), (24.59, 98.69), (24.90, 98.95), (25.12, 99.17), (25.40, 99.40),
        (25.60, 99.95), (25.59, 100.23), (25.48, 100.55), (25.03, 101.54), (25.15, 102.08),
        (25.04, 102.71)]
# name, (lat, lon), label offset (dx, dy), anchor, bold
PLACES = [
    ("Mandalay", (21.98, 96.08), (-16, 0), "rm", False),
    ("Lashio", (22.94, 97.75), (-16, 10), "rm", True),
    ("Wanding (border)", (24.08, 98.07), (-16, 2), "rm", False),
    ("Baoshan", (25.12, 99.17), (-14, -16), "rm", False),
    ("Xiaguan", (25.59, 100.23), (0, -22), "ms", False),
    ("Chuxiong", (25.03, 101.54), (0, 30), "mt", False),
    ("Kunming", (25.04, 102.71), (16, 0), "lm", True),
]
ROAD_COL = (176, 38, 30)
RAIL_COL = (60, 60, 58)


def main():
    base = base_tile()
    W, H = base.size
    muted = ImageEnhance.Color(base).enhance(0.35)
    img = Image.blend(muted, Image.new("RGB", base.size, "white"), 0.3).convert("RGBA")
    d = ImageDraw.Draw(img)
    rail = [px(*p) for p in RAIL]
    for a, b in zip(rail, rail[1:]):  # dashed railway
        n = int(math.dist(a, b) // 14) + 1
        for i in range(0, n, 2):
            p0 = (a[0] + (b[0] - a[0]) * i / n, a[1] + (b[1] - a[1]) * i / n)
            p1 = (a[0] + (b[0] - a[0]) * min(i + 1, n) / n, a[1] + (b[1] - a[1]) * min(i + 1, n) / n)
            d.line([p0, p1], fill=RAIL_COL + (255,), width=5)
    road = [px(*p) for p in ROAD]
    d.line(road, fill=(255, 255, 255, 255), width=13, joint="curve")
    d.line(road, fill=ROAD_COL + (255,), width=8, joint="curve")
    for name, (lat, lon), (dx, dy), anchor, bold in PLACES:
        x, y = px(lat, lon)
        r = 10 if bold else 7
        d.ellipse([x - r, y - r, x + r, y + r], fill=(28, 28, 26, 255), outline=(255, 255, 255, 255), width=3)
        f = font(30 if bold else 24, bold=bold)
        tb = d.textbbox((x + dx, y + dy), name, font=f, anchor=anchor)
        d.rounded_rectangle([tb[0] - 7, tb[1] - 5, tb[2] + 7, tb[3] + 5], radius=6, fill=(255, 255, 255, 225))
        d.text((x + dx, y + dy), name, font=f, fill=(28, 28, 26, 255), anchor=anchor)
    # arrow note at the southern edge: the rail line runs on to Rangoon
    rx, ry = px(21.15, 96.06)
    note = "rail from Rangoon"
    tb = d.textbbox((rx + 18, ry), note, font=font(22), anchor="lm")
    d.rounded_rectangle([tb[0] - 6, tb[1] - 4, tb[2] + 6, tb[3] + 4], radius=6, fill=(255, 255, 255, 225))
    d.text((rx + 18, ry), note, font=font(22), fill=(70, 70, 68, 255), anchor="lm")
    # title and legend
    d.rectangle([0, 0, W, 74], fill=(255, 255, 255, 235))
    d.text((28, 18), "The Burma Road, 1939", font=font(36, bold=True), fill=(28, 28, 26, 255))
    ly = 96
    for col, lab, dashed in [(ROAD_COL, "the Burma Road, Lashio to Kunming (about 1,146 km)", False),
                             (RAIL_COL, "railway from Rangoon, where the supplies were landed", True)]:
        if dashed:
            for x in range(30, 74, 16):
                d.line([(x, ly + 13), (x + 8, ly + 13)], fill=col + (255,), width=5)
        else:
            d.line([(30, ly + 13), (74, ly + 13)], fill=col + (255,), width=8)
        tb = d.textbbox((86, ly), lab, font=font(23))
        d.rectangle([tb[0] - 4, tb[1] - 3, tb[2] + 6, tb[3] + 4], fill=(255, 255, 255, 215))
        d.text((86, ly), lab, font=font(23), fill=(28, 28, 26, 255))
        ly += 40
    foot = "Approximate route, drawn through towns on the old road over today's map."
    fb = d.textbbox((0, 0), foot, font=font(22))
    d.rectangle([0, H - 44, fb[2] + 36, H], fill=(255, 255, 255, 225))
    d.text((18, H - 36), foot, font=font(22), fill=(70, 70, 68, 255))
    cred = "Map data (c) OpenStreetMap contributors"
    cb = d.textbbox((0, 0), cred, font=font(20))
    d.rectangle([W - cb[2] - 36, H - 44, W, H], fill=(255, 255, 255, 225))
    d.text((W - cb[2] - 18, H - 36), cred, font=font(20), fill=(70, 70, 68, 255))
    img.convert("RGB").resize((1600, round(1600 * H / W)), Image.LANCZOS).save(OUT, optimize=True)
    print("wrote", OUT, img.size)


if __name__ == "__main__":
    main()
