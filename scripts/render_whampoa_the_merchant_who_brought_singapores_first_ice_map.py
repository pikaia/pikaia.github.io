"""Render assets/images/whampoa-the-merchant-who-brought-singapores-first-ice-map.png
for the Whampoa post.

Stitches OpenStreetMap raster tiles covering central Singapore into a
muted base image, then marks the four places that actually anchor
Hoo Ah Kay's story: his failed ice house at Boat Quay, his garden
estate (later Bendemeer) on Serangoon Road, the Tanglin plot his own
former nutmeg plantation became - the Botanic Gardens - and Keppel
Harbour, named for the Royal Navy admiral he provisioned and
befriended. Same convention as the other OSM maps on this blog:
present-day roads/coastline, a sense of geographic spread rather than
a period map.

"Map data (c) OpenStreetMap contributors" is burned in and also
belongs in the post's Sources list.

    python scripts/render_whampoa_the_merchant_who_brought_singapores_first_ice_map.py
"""
import io
import math
import os
import time
import urllib.request

from PIL import Image, ImageDraw, ImageEnhance, ImageFont

ZOOM = 14
LAT_N, LAT_S = 1.335, 1.255
LON_W, LON_E = 103.805, 103.905

OUT = os.path.join(os.path.dirname(__file__), "..", "assets", "images",
                    "whampoa-the-merchant-who-brought-singapores-first-ice-map.png")
TILE_URL = "https://tile.openstreetmap.org/{z}/{x}/{y}.png"
UA = "LesserKnownSingapore-map-render/1.0 (one-off static map for a blog post)"

ICE_C = (44, 106, 196, 255)     # ice house / business
GARDEN_C = (196, 106, 30, 255)  # Whampoa's own garden estate
BOTANIC_C = (52, 129, 79, 255)  # Botanic Gardens (his old plantation land)
KEPPEL_C = (100, 98, 96, 255)   # Keppel Harbour / the Navy friendship

# label, colour, lat, lon, anchor side ("l"/"r"), vertical box offset (px),
# horizontal gap from marker to box (px, default 22)
PINS = [
    ("Boat Quay\nWhampoa's Ice House, 1854 -\nfailed within three years", ICE_C, 1.2884, 103.8460, "l", -10, 22),
    ("Serangoon Road\nWhampoa's Garden, later\nBendemeer House; demolished 1964", GARDEN_C, 1.3160, 103.8620, "l", -20, 22),
    ("Tanglin\nHis own former nutmeg land -\nbecame the Botanic Gardens, 1859", BOTANIC_C, 1.3138, 103.8159, "l", 40, 22),
    ("Keppel Harbour\nnamed for Admiral Henry Keppel,\nWhampoa's friend and customer", KEPPEL_C, 1.2650, 103.8210, "l", 0, 22),
]

TITLE = "The places behind the name"
FOOT = "Neighbourhood-level approximations, shown on today's map."


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
            near_x = bx2 + boxw if side == "l" else bx2
            near_y = by2 + boxh / 2
            draw.line([(cx, cy), (near_x, near_y)], fill=(*col[:3], 160), width=2)

        draw.rectangle([bx2, by2, bx2 + boxw, by2 + boxh], fill=(255, 255, 255, 234))
        for i, ln in enumerate(lines):
            draw.text((bx2 + 10, by2 + 8 + i * 26), ln, font=fonts[i], fill=(28, 28, 26, 255))

        draw.ellipse([cx - 15, cy - 15, cx + 15, cy + 15], fill=(255, 255, 255, 245))
        draw.ellipse([cx - 11, cy - 11, cx + 11, cy + 11], fill=col)

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
