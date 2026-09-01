"""Render assets/images/aw-brothers-hq-park-map.png for the Aw brothers post.

Stitches OpenStreetMap raster tiles for the southern strip of Singapore,
mutes them, and marks the two ends of the Tiger Balm story: the Eng Aun
Tong factory / headquarters at 89 Neil Road in Chinatown, and Haw Par
Villa on Pasir Panjang Road about 7 km west along the coast. A dashed
line joins them with the straight-line distance.

Markers are placed from real coordinates through the Web Mercator
projection the tiles use. "Map data (c) OpenStreetMap contributors" is
burned in and also belongs in the post's Sources list. Committed binary,
same documented exception as the other OSM maps / chart PNGs.

    python scripts/render_aw_brothers_hq_park_map.py
"""
import io
import math
import os
import time
import urllib.request

from PIL import Image, ImageDraw, ImageEnhance, ImageFont

ZOOM = 14
LAT_N, LAT_S = 1.302, 1.255
LON_W, LON_E = 103.752, 103.872

OUT = os.path.join(os.path.dirname(__file__), "..", "assets", "images", "aw-brothers-hq-park-map.png")
TILE_URL = "https://tile.openstreetmap.org/{z}/{x}/{y}.png"
UA = "LesserKnownSingapore-map-render/1.0 (one-off static map for a blog post)"

HQ_C = (37, 99, 197, 255)
PARK_C = (196, 76, 40, 255)

# label, colour, lat, lon, label anchor side ("l" = text to the right, "r" = to the left)
PINS = [
    ("Eng Aun Tong / Tiger Balm factory\n89 Neil Road, Chinatown", HQ_C, 1.27856, 103.84168, "l"),
    ("Haw Par Villa (Tiger Balm Garden)\nPasir Panjang Road", PARK_C, 1.28268, 103.78176, "r"),
]


def deg2px(lat, lon, z):
    n = 2.0 ** z
    x = (lon + 180.0) / 360.0 * n * 256.0
    y = (1.0 - math.asinh(math.tan(math.radians(lat))) / math.pi) / 2.0 * n * 256.0
    return x, y


def fetch_tile(z, x, y):
    req = urllib.request.Request(TILE_URL.format(z=z, x=x, y=y), headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=30) as r:
        return Image.open(io.BytesIO(r.read())).convert("RGB")


def load_font(size, bold=False):
    names = (["arialbd.ttf"] if bold else ["arial.ttf"]) + \
            ["DejaVuSans-Bold.ttf" if bold else "DejaVuSans.ttf"]
    for nm in names:
        try:
            return ImageFont.truetype(nm, size)
        except OSError:
            continue
    return ImageFont.load_default()


def haversine_km(a, b):
    r = 6371.0
    lat1, lon1, lat2, lon2 = map(math.radians, (a[0], a[1], b[0], b[1]))
    h = math.sin((lat2 - lat1) / 2) ** 2 + math.cos(lat1) * math.cos(lat2) * math.sin((lon2 - lon1) / 2) ** 2
    return 2 * r * math.asin(math.sqrt(h))


def main():
    n = 2.0 ** ZOOM
    tx0 = int((LON_W + 180.0) / 360.0 * n)
    tx1 = int((LON_E + 180.0) / 360.0 * n)
    ty0 = int((1.0 - math.asinh(math.tan(math.radians(LAT_N))) / math.pi) / 2.0 * n)
    ty1 = int((1.0 - math.asinh(math.tan(math.radians(LAT_S))) / math.pi) / 2.0 * n)

    tw = (tx1 - tx0 + 1) * 256
    th = (ty1 - ty0 + 1) * 256
    tiles = Image.new("RGB", (tw, th), "#dddddd")
    print(f"stitching {tx1 - tx0 + 1}x{ty1 - ty0 + 1} tiles at z{ZOOM} ({tw}x{th}px)")
    for tx in range(tx0, tx1 + 1):
        for ty in range(ty0, ty1 + 1):
            try:
                tiles.paste(fetch_tile(ZOOM, tx, ty), ((tx - tx0) * 256, (ty - ty0) * 256))
            except Exception as e:  # noqa: BLE001
                print(f"  tile {tx},{ty} failed: {e}")
            time.sleep(0.1)

    tiles = ImageEnhance.Color(tiles).enhance(0.4)
    tiles = ImageEnhance.Brightness(tiles).enhance(1.12)
    tiles = Image.blend(tiles, Image.new("RGB", tiles.size, "#ffffff"), 0.34)

    canvas = tiles.convert("RGB")
    draw = ImageDraw.Draw(canvas, "RGBA")
    ox, oy = tx0 * 256, ty0 * 256
    label_font = load_font(21, bold=True)
    sub_font = load_font(19)
    dist_font = load_font(20, bold=True)

    pts = []
    for _lab, _col, lat, lon, _side in PINS:
        px, py = deg2px(lat, lon, ZOOM)
        pts.append((px - ox, py - oy))

    # connector
    draw.line([pts[0], pts[1]], fill=(60, 60, 58, 200), width=3)
    for frac in [i / 24 for i in range(25)]:
        mx = pts[0][0] + (pts[1][0] - pts[0][0]) * frac
        my = pts[0][1] + (pts[1][1] - pts[0][1]) * frac
        if int(frac * 24) % 2 == 0:
            draw.ellipse([mx - 2, my - 2, mx + 2, my + 2], fill=(255, 255, 255, 230))
    midx, midy = (pts[0][0] + pts[1][0]) / 2, (pts[0][1] + pts[1][1]) / 2
    km = haversine_km((PINS[0][2], PINS[0][3]), (PINS[1][2], PINS[1][3]))
    dtxt = f"about {km:.0f} km apart"
    tb = draw.textbbox((0, 0), dtxt, font=dist_font)
    dw, dh = tb[2] - tb[0], tb[3] - tb[1]
    draw.rectangle([midx - dw / 2 - 8, midy - dh - 22, midx + dw / 2 + 8, midy - 6], fill=(255, 255, 255, 235))
    draw.text((midx, midy - 14), dtxt, font=dist_font, fill=(40, 40, 38, 255), anchor="mm")

    for (lab, col, _lat, _lon, side), (cx, cy) in zip(PINS, pts):
        draw.ellipse([cx - 15, cy - 15, cx + 15, cy + 15], fill=(255, 255, 255, 245))
        draw.ellipse([cx - 11, cy - 11, cx + 11, cy + 11], fill=col)
        lines = lab.split("\n")
        widths = [draw.textbbox((0, 0), ln, font=(label_font if i == 0 else sub_font))[2] for i, ln in enumerate(lines)]
        boxw = max(widths) + 20
        boxh = 30 * len(lines) + 12
        if side == "l":
            bx = cx + 22
        else:
            bx = cx - 22 - boxw
        by = cy - boxh / 2
        draw.rectangle([bx, by, bx + boxw, by + boxh], fill=(255, 255, 255, 235))
        for i, ln in enumerate(lines):
            draw.text((bx + 10, by + 8 + i * 30), ln, font=(label_font if i == 0 else sub_font),
                      fill=(30, 30, 28, 255))

    cred_font = load_font(18)
    txt = "Map data (c) OpenStreetMap contributors"
    tb = draw.textbbox((0, 0), txt, font=cred_font)
    cw, ch = tb[2] - tb[0], tb[3] - tb[1]
    W, H = canvas.size
    draw.rectangle([W - cw - 22, H - ch - 18, W, H], fill=(255, 255, 255, 215))
    draw.text((W - cw - 12, H - ch - 12), txt, font=cred_font, fill=(70, 70, 68, 255))

    target_w = 1600
    scale = target_w / canvas.width
    canvas = canvas.resize((target_w, int(canvas.height * scale)), Image.LANCZOS)

    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    canvas.save(OUT, optimize=True)
    print(f"wrote {OUT}  ({canvas.size[0]}x{canvas.size[1]})")


if __name__ == "__main__":
    main()
