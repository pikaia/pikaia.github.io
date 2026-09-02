"""Render assets/images/three-days-stock-exchange-shut-1985-map.png for the
Pan-Electric post.

Stitches OpenStreetMap raster tiles for Raffles Place, mutes them, and
marks how tightly the 1985 crisis was packed into one district: the
Stock Exchange of Singapore's trading floor at Clifford Centre, and the
head-office towers of three of the four banks that put up the rescue
credit line (OCBC, UOB, OUB) - all within about 250 metres. DBS, the
fourth, was a short way south on Shenton Way.

Building names and positions are shown as they stand today; this is a
sense of the geography, not a precise 1985 street plan. Markers are
placed from real coordinates through the Web Mercator projection the
tiles use. "Map data (c) OpenStreetMap contributors" is burned in and
also belongs in the post's Sources list. Committed binary, same
documented exception as the other OSM maps / chart PNGs.

    python scripts/render_three_days_map.py
"""
import io
import math
import os
import time
import urllib.request

from PIL import Image, ImageDraw, ImageEnhance, ImageFont

ZOOM = 17
LAT_N, LAT_S = 1.2874, 1.2820
LON_W, LON_E = 103.8485, 103.8539

OUT = os.path.join(os.path.dirname(__file__), "..", "assets", "images",
                   "three-days-stock-exchange-shut-1985-map.png")
TILE_URL = "https://tile.openstreetmap.org/{z}/{x}/{y}.png"
UA = "LesserKnownSingapore-map-render/1.0 (one-off static map for a blog post)"

SES_C = (57, 135, 229, 255)     # the exchange
BANK_C = (196, 76, 40, 255)     # rescue banks

# label, colour, lat, lon, anchor side ("l" = text to the right, "r" = to the left)
PINS = [
    ("OCBC Centre", BANK_C, 1.28565, 103.84945, "l"),
    ("UOB Plaza", BANK_C, 1.28470, 103.85030, "r"),
    ("Clifford Centre\nStock Exchange of Singapore\ntrading floor, 1980s", SES_C, 1.28390, 103.85175, "l"),
]

TITLE = "1985: the crisis, inside a few blocks of Raffles Place"
FOOT = "OUB and DBS, the other two rescue banks, were a short walk away."


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

    tiles = ImageEnhance.Color(tiles).enhance(0.28)
    tiles = ImageEnhance.Brightness(tiles).enhance(1.14)
    tiles = Image.blend(tiles, Image.new("RGB", tiles.size, "#ffffff"), 0.45)

    canvas = tiles.convert("RGB")
    draw = ImageDraw.Draw(canvas, "RGBA")
    ox, oy = tx0 * 256, ty0 * 256
    label_font = load_font(21, bold=True)
    sub_font = load_font(18)
    title_font = load_font(20, bold=True)
    cred_font = load_font(17)

    pts = [(px - ox, py - oy) for px, py in (deg2px(lat, lon, ZOOM) for _l, _c, lat, lon, _s in PINS)]

    # scale bar: 100 m at this latitude
    m_per_px = math.cos(math.radians(1.2845)) * 2 * math.pi * 6378137 / (256 * 2 ** ZOOM)
    bar_px = 100 / m_per_px
    W, H = canvas.size
    bx, by = 40, H - 60
    draw.line([(bx, by), (bx + bar_px, by)], fill=(30, 30, 28, 255), width=4)
    for ex in (bx, bx + bar_px):
        draw.line([(ex, by - 7), (ex, by + 7)], fill=(30, 30, 28, 255), width=4)
    draw.text((bx + bar_px / 2, by - 12), "100 m", font=sub_font, fill=(30, 30, 28, 255), anchor="ms")

    for (lab, col, _lat, _lon, side), (cx, cy) in zip(PINS, pts):
        draw.ellipse([cx - 15, cy - 15, cx + 15, cy + 15], fill=(255, 255, 255, 245))
        draw.ellipse([cx - 11, cy - 11, cx + 11, cy + 11], fill=col)
        lines = lab.split("\n")
        fonts = [label_font] + [sub_font] * (len(lines) - 1)
        widths = [draw.textbbox((0, 0), ln, font=fonts[i])[2] for i, ln in enumerate(lines)]
        boxw = max(widths) + 20
        boxh = 27 * len(lines) + 12
        bx2 = cx + 22 if side == "l" else cx - 22 - boxw
        by2 = cy - boxh / 2
        draw.rectangle([bx2, by2, bx2 + boxw, by2 + boxh], fill=(255, 255, 255, 236))
        for i, ln in enumerate(lines):
            draw.text((bx2 + 10, by2 + 8 + i * 27), ln, font=fonts[i], fill=(28, 28, 26, 255))

    # title strip (title + a note on the two banks not shown)
    draw.rectangle([0, 0, W, 82], fill=(255, 255, 255, 234))
    draw.text((24, 12), TITLE, font=title_font, fill=(28, 28, 26, 255))
    draw.text((24, 46), FOOT, font=sub_font, fill=(80, 80, 78, 255))

    txt = "Map data (c) OpenStreetMap contributors"
    tb = draw.textbbox((0, 0), txt, font=cred_font)
    cw, ch = tb[2] - tb[0], tb[3] - tb[1]
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
