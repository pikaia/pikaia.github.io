"""Render assets/images/gas-pipelines-map.png.

A locator for the gas pipelines post: the three pipelines that bring natural
gas to Singapore - from Malaysia (1992, gas from the fields off Terengganu,
carried down the peninsula and under the Johor Strait to Senoko), from West
Natuna (2001, under the South China Sea to Jurong Island) and from Grissik
in South Sumatra (2003, by way of Batam). Routes and pins are approximate,
drawn by hand to show direction and distance, not the surveyed lines. "Map
data (c) OpenStreetMap contributors" is burned in and also belongs in the
post's Sources list.

    python scripts/render_gas_pipelines_map.py
"""
import io
import math
import os
import time
import urllib.request

from PIL import Image, ImageDraw, ImageEnhance, ImageFont

ZOOM = 8
LAT_N, LAT_S = 5.7000, -2.8000
LON_W, LON_E = 101.6000, 106.6000

OUT = os.path.join(os.path.dirname(__file__), "..", "assets", "images",
                   "gas-pipelines-map.png")
TILE_URL = "https://tile.openstreetmap.org/{z}/{x}/{y}.png"
UA = "LesserKnownSingapore-map-render/1.0 (one-off static map for a blog post)"

MY_C = (176, 58, 46, 255)          # Malaysia, 1992
NATUNA_C = (46, 98, 150, 255)      # West Natuna, 2001
SUMATRA_C = (64, 120, 64, 255)     # Grissik, 2003
SG_C = (60, 60, 60, 255)           # the Singapore end

# (legend label, colour, [(lat, lon), ...]) - hand-drawn, approximate
ROUTES = [
    ("From Malaysia, 1992", MY_C, [(4.51, 103.45), (3.80, 103.30), (2.50, 102.85), (1.95, 103.30), (1.47, 103.90), (1.46, 103.80)]),
    ("From West Natuna, 2001", NATUNA_C, [(5.00, 105.70), (3.60, 105.20), (2.20, 104.70), (1.40, 104.30), (1.15, 103.95), (1.22, 103.72)]),
    ("From Grissik, South Sumatra, 2003", SUMATRA_C, [(-2.27, 103.79), (-1.30, 103.95), (-0.20, 104.15), (0.70, 104.10), (1.05, 104.02), (1.20, 103.80), (1.24, 103.70)]),
]

# label, colour, lat, lon, anchor side ("l" = box to the right, "r" = box to the left),
# vertical box offset (px), horizontal gap from marker to box (px, default 22)
PINS = [
    ("Kertih, Terengganu\nMalaysian gas", MY_C, 4.51, 103.45, "r", 0, 30),
    ("West Natuna\ngas fields", NATUNA_C, 5.00, 105.70, "r", 40, 30),
    ("Grissik\nSouth Sumatra", SUMATRA_C, -2.27, 103.79, "l", 0, 30),
    ("Batam", SUMATRA_C, 1.05, 104.02, "l", 40, 40),
    ("Senoko\npower station", SG_C, 1.46, 103.80, "r", -70, 40),
    ("Jurong Island", SG_C, 1.24, 103.70, "r", 60, 40),
]

TITLE = "The pipelines that feed Singapore"
FOOT = "Routes and pins are approximate."


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
    names = (["arialbd.ttf", "Arial Bold.ttf"] if bold else ["arial.ttf", "Arial.ttf"]) + \
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

    tiles = ImageEnhance.Color(tiles).enhance(0.32)
    tiles = ImageEnhance.Brightness(tiles).enhance(1.13)
    tiles = ImageEnhance.Contrast(tiles).enhance(0.92)
    tiles = Image.blend(tiles, Image.new("RGB", tiles.size, "#ffffff"), 0.32)

    canvas = tiles.convert("RGB")
    draw = ImageDraw.Draw(canvas, "RGBA")
    ox, oy = tx0 * 256, ty0 * 256
    label_font = load_font(22, bold=True)
    sub_font = load_font(19)
    title_font = load_font(24, bold=True)
    cred_font = load_font(18)

    for _, col, pts in ROUTES:
        xy = []
        for lat, lon in pts:
            px, py = deg2px(lat, lon, ZOOM)
            xy.append((px - ox, py - oy))
        draw.line(xy, fill=(255, 255, 255, 230), width=11, joint="curve")
        draw.line(xy, fill=col, width=6, joint="curve")

    for lab, col, lat, lon, side, voffset, gap in PINS:
        px, py = deg2px(lat, lon, ZOOM)
        cx, cy = px - ox, py - oy

        lines = lab.split("\n")
        fonts = [label_font] + [sub_font] * (len(lines) - 1)
        widths = [draw.textbbox((0, 0), ln, font=fonts[i])[2] for i, ln in enumerate(lines)]
        boxw = max(widths) + 20
        boxh = 26 * len(lines) + 12
        bx2 = cx + gap if side == "l" else cx - gap - boxw
        by2 = cy - boxh / 2 + voffset

        if abs(voffset) > 15 or gap > 22:
            near_x = bx2 if side == "l" else bx2 + boxw
            near_y = by2 + boxh / 2
            draw.line([(cx, cy), (near_x, near_y)], fill=(*col[:3], 160), width=2)

        draw.rectangle([bx2, by2, bx2 + boxw, by2 + boxh], fill=(255, 255, 255, 234))
        for i, ln in enumerate(lines):
            draw.text((bx2 + 10, by2 + 8 + i * 26), ln, font=fonts[i], fill=(28, 28, 26, 255))

        r = 11
        draw.ellipse([cx - r - 4, cy - r - 4, cx + r + 4, cy + r + 4], fill=(255, 255, 255, 245))
        draw.ellipse([cx - r, cy - r, cx + r, cy + r], fill=col)

    W, H = canvas.size
    ly = 76
    lw = max(draw.textbbox((0, 0), lab, font=sub_font)[2] for lab, _, _ in ROUTES) + 70
    draw.rectangle([16, ly - 10, 16 + lw, ly + 34 * len(ROUTES)], fill=(255, 255, 255, 234))
    for i, (lab, col, _) in enumerate(ROUTES):
        yy = ly + 34 * i + 12
        draw.line([(28, yy), (64, yy)], fill=col, width=6)
        draw.text((74, yy - 12), lab, font=sub_font, fill=(28, 28, 26, 255))
    draw.rectangle([0, 0, W, 56], fill=(255, 255, 255, 234))
    draw.text((24, 14), TITLE, font=title_font, fill=(28, 28, 26, 255))

    fb = draw.textbbox((0, 0), FOOT, font=sub_font)
    draw.rectangle([0, H - (fb[3] - fb[1]) - 20, (fb[2] - fb[0]) + 30, H], fill=(255, 255, 255, 210))
    draw.text((14, H - (fb[3] - fb[1]) - 12), FOOT, font=sub_font, fill=(80, 80, 78, 255))

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
