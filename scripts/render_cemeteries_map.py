"""Render assets/images/singapore-former-cemeteries-map.png.

A locator for the cemeteries post: former burial grounds in central
Singapore and what replaced them, with Choa Chu Kang Cemetery (the only one
still open for burials) and the Mandai crematorium. Positions are
approximate, plotted by hand against today's OpenStreetMap tiles. "Map data
(c) OpenStreetMap contributors" is burned in and also belongs in the post's
Sources list.

    python scripts/render_cemeteries_map.py
"""
import io
import math
import os
import time
import urllib.request

from PIL import Image, ImageDraw, ImageEnhance, ImageFont

ZOOM = 13
LAT_N, LAT_S = 1.4250, 1.2700
LON_W, LON_E = 103.6800, 103.8950

OUT = os.path.join(os.path.dirname(__file__), "..", "assets", "images",
                   "singapore-former-cemeteries-map.png")
TILE_URL = "https://tile.openstreetmap.org/{z}/{x}/{y}.png"
UA = "LesserKnownSingapore-map-render/1.0 (one-off static map for a blog post)"

THEN_C = (176, 58, 46, 255)        # former cemeteries
TODAY_C = (46, 98, 150, 255)       # still in use today

# label, colour, lat, lon, anchor side ("l"/"r"), vertical box offset (px),
# horizontal gap from marker to box (px, default 22)
PINS = [
    ("Fort Canning\nChristian cemetery 1823-65, now a park", THEN_C, 1.295, 103.846, "l", 140, 40),
    ("Tiong Bahru\nflats built on old grave yards", THEN_C, 1.2855, 103.831, "r", 150, 30),
    ("Bukit Timah Road\nChristian cemetery 1865-1907", THEN_C, 1.3105, 103.844, "r", 30, 220),
    ("Thomson Road\nJewish cemetery, cleared 1985 for Novena MRT", THEN_C, 1.3204, 103.8438, "r", -45, 220),
    ("Bukit Brown\nChinese cemetery 1922-1973, still standing", THEN_C, 1.3335, 103.8185, "r", -120, 120),
    ("Peck San Theng\nexhumed 1982-84, now Bishan", THEN_C, 1.351, 103.848, "l", -80, 150),
    ("Bidadari\n1908-72, exhumed 2001-06", THEN_C, 1.337, 103.872, "l", 110, 25),
    ("Mandai\ncrematorium and columbaria", TODAY_C, 1.412, 103.8, "l", 0, 30),
    ("Choa Chu Kang Cemetery\nthe only cemetery open for burials,\nand the Garden of Peace", TODAY_C, 1.372, 103.695, "l", -110, 40),
]

TITLE = "Singapore's former cemeteries, and where the dead go today"
FOOT = "Positions are approximate, shown against today's map."


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
