"""Render assets/images/yaohan-store-map.png for the Yaohan post.

Stitches OpenStreetMap raster tiles for the built-up belt of Singapore,
mutes them, and marks each Japanese department store at the mall it
occupied - numbered dots, blue for still-open and grey for closed, with
a numbered key panel down the left because the Orchard-Road stores sit
too close together for inline labels.

Markers are placed from real coordinates through the Web Mercator
projection the tiles use. "Map data (c) OpenStreetMap contributors" is
burned in and also belongs in the post's Sources list. Committed binary,
same documented exception as the other OSM maps / chart PNGs.

    python scripts/render_yaohan_store_map.py
"""
import io
import math
import os
import time
import urllib.request

from PIL import Image, ImageDraw, ImageEnhance, ImageFont

ZOOM = 13
LAT_N, LAT_S = 1.398, 1.242
LON_W, LON_E = 103.700, 103.958

OUT = os.path.join(os.path.dirname(__file__), "..", "assets", "images", "yaohan-store-map.png")
TILE_URL = "https://tile.openstreetmap.org/{z}/{x}/{y}.png"
UA = "LesserKnownSingapore-map-render/1.0 (one-off static map for a blog post)"

OPEN_C = (37, 99, 197, 255)
SHUT_C = (122, 126, 132, 255)
PANEL_W = 430

# number, store, mall, years, lat, lon, open?
STORES = [
    (1, "Isetan", "Havelock Road (first store)", "1972", 1.2903, 103.8356, False),
    (2, "Yaohan", "Plaza Singapura", "1974–97", 1.3007, 103.8452, False),
    (3, "Yaohan", "Katong / Parkway Parade", "1977–97", 1.3020, 103.9048, False),
    (4, "Yaohan", "Thomson Plaza", "1979–98", 1.3545, 103.8319, False),
    (5, "Yaohan", "Bukit Timah Plaza", "1981–96", 1.3392, 103.7767, False),
    (6, "Yaohan", "Jurong East", "1983–97", 1.3339, 103.7423, False),
    (7, "Daimaru", "Liang Court", "1983–2003", 1.2903, 103.8466, False),
    (8, "Sogo", "Raffles City", "1986–2000", 1.2933, 103.8536, False),
    (9, "Isetan", "Wisma Atria", "1986 – now", 1.3049, 103.8324, True),
    (10, "Isetan", "Scotts Road (Shaw House)", "still open", 1.3070, 103.8312, True),
    (11, "Takashimaya", "Ngee Ann City", "1993 – now", 1.3028, 103.8352, True),
    (12, "Isetan", "NEX, Serangoon", "2010–24", 1.3506, 103.8719, False),
    (13, "Isetan", "Tampines Mall", "1995–2025", 1.3527, 103.9451, False),
    (14, "Don Don Donki", "Orchard Central (first store)", "2017 – now", 1.3007, 103.8396, True),
    (15, "Don Don Donki", "Suntec City", "open", 1.2954, 103.8592, True),
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

    canvas = Image.new("RGB", (tw + PANEL_W, th), "#ffffff")
    canvas.paste(tiles, (PANEL_W, 0))
    draw = ImageDraw.Draw(canvas, "RGBA")

    num_font = load_font(17, bold=True)
    store_font = load_font(20, bold=True)
    mall_font = load_font(18)
    head_font = load_font(23, bold=True)
    ox, oy = tx0 * 256, ty0 * 256

    for num, store, _mall, _yrs, lat, lon, is_open in STORES:
        px, py = deg2px(lat, lon, ZOOM)
        cx, cy = px - ox + PANEL_W, py - oy
        col = OPEN_C if is_open else SHUT_C
        draw.ellipse([cx - 15, cy - 15, cx + 15, cy + 15], fill=(255, 255, 255, 240))
        draw.ellipse([cx - 12, cy - 12, cx + 12, cy + 12], fill=col)
        draw.text((cx, cy), str(num), font=num_font, fill=(255, 255, 255, 255), anchor="mm")

    # key panel
    draw.rectangle([0, 0, PANEL_W, th], fill=(255, 255, 255, 255))
    draw.line([(PANEL_W, 0), (PANEL_W, th)], fill=(210, 210, 208, 255), width=2)
    y = 34
    draw.text((28, y), "Japanese department stores", font=head_font, fill=(30, 30, 28, 255))
    y += 34
    draw.text((28, y), "on and off Orchard Road", font=head_font, fill=(30, 30, 28, 255))
    y += 52
    for num, store, mall, yrs, _lat, _lon, is_open in STORES:
        col = OPEN_C if is_open else SHUT_C
        draw.ellipse([28, y - 1, 54, y + 25], fill=col)
        draw.text((41, y + 12), str(num), font=num_font, fill=(255, 255, 255, 255), anchor="mm")
        draw.text((70, y - 2), f"{store} · {mall}", font=store_font, fill=(30, 30, 28, 255))
        draw.text((70, y + 22), yrs, font=mall_font, fill=(120, 120, 118, 255))
        y += 56
    y += 6
    for lab, col in (("still open", OPEN_C), ("closed", SHUT_C)):
        draw.ellipse([28, y, 48, y + 20], fill=col)
        draw.text((60, y + 10), lab, font=mall_font, fill=(70, 70, 68, 255), anchor="lm")
        y += 30

    cred_font = load_font(18)
    txt = "Map data (c) OpenStreetMap contributors"
    tb = draw.textbbox((0, 0), txt, font=cred_font)
    cw = tb[2] - tb[0]
    ch = tb[3] - tb[1]
    W = canvas.width
    draw.rectangle([W - cw - 22, th - ch - 18, W, th], fill=(255, 255, 255, 215))
    draw.text((W - cw - 12, th - ch - 12), txt, font=cred_font, fill=(70, 70, 68, 255))

    target_w = 1700
    scale = target_w / canvas.width
    canvas = canvas.resize((target_w, int(canvas.height * scale)), Image.LANCZOS)

    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    canvas.save(OUT, optimize=True)
    print(f"wrote {OUT}  ({canvas.size[0]}x{canvas.size[1]})")


if __name__ == "__main__":
    main()
