"""Render assets/images/kallang-airport-map.png for the Kallang Airport post.

A locator over today's OpenStreetMap tiles: the surviving terminal
building on the north edge of the Kallang Basin, the line the 1937 grass
field / wartime concrete runway ran along (roughly - a hand-plotted
approximation, not a survey), the flying-boat basin, and the present-day
landmarks people know the area by - the Singapore Sports Hub on what was
the airfield, and Stadium and Dakota MRT stations. "Map data (c)
OpenStreetMap contributors" is burned in and belongs in the post's
Sources list too.

    python scripts/render_kallang_airport_finest_in_the_british_empire_map.py
"""
import io
import math
import os
import time
import urllib.request

from PIL import Image, ImageDraw, ImageEnhance, ImageFont

ZOOM = 16
LAT_N, LAT_S = 1.3120, 1.2980
LON_W, LON_E = 103.8640, 103.8930

OUT = os.path.join(os.path.dirname(__file__), "..", "assets", "images", "kallang-airport-map.png")
TILE_URL = "https://tile.openstreetmap.org/{z}/{x}/{y}.png"
UA = "LesserKnownSingapore-map-render/1.0 (one-off static map for a blog post)"

THEN_C = (198, 118, 36, 255)   # the airport, 1937-1955
NOW_C = (36, 110, 122, 255)    # what the area is known by today

# label, colour, lat, lon, anchor side ("l"/"r"), vertical box offset (px), gap
PINS = [
    ("Former Kallang Airport terminal\n(the curved building with the\nround control tower)", THEN_C, 1.30768, 103.87355, "l", -66, 30),
    ("National Stadium &\nSingapore Sports Hub\n(built over the airfield)", NOW_C, 1.30410, 103.87440, "r", 4, 30),
    ("Stadium MRT", NOW_C, 1.30330, 103.87560, "l", 44, 26),
    ("Dakota MRT\n(named after the DC-3 airliner)", NOW_C, 1.30820, 103.88860, "r", 0, 26),
]

# the runway/landing-ground ran roughly along this line (approximate)
RUNWAY = [(1.30600, 103.87150), (1.30380, 103.88120)]

BASIN_LABEL = ("Kallang Basin\nthe flying-boat water aerodrome", 1.30550, 103.87050)

TITLE = "Kallang: the airport, and what's there now"
FOOT = "The runway line and positions are hand-plotted approximations, shown against today's map."


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

    def to_xy(lat, lon):
        px, py = deg2px(lat, lon, ZOOM)
        return px - ox, py - oy

    # runway line - dashed
    (r0, r1) = [to_xy(*p) for p in RUNWAY]
    seg = 16
    dx, dy = r1[0] - r0[0], r1[1] - r0[1]
    dist = math.hypot(dx, dy)
    steps = int(dist / seg)
    for i in range(0, steps, 2):
        a = (r0[0] + dx * i / steps, r0[1] + dy * i / steps)
        b = (r0[0] + dx * (i + 1) / steps, r0[1] + dy * (i + 1) / steps)
        draw.line([a, b], fill=(*THEN_C[:3], 235), width=6)
    rl_font = load_font(18, bold=True)
    mid = ((r0[0] + r1[0]) / 2, (r0[1] + r1[1]) / 2)
    rt = "the runway ran roughly along here"
    tb = draw.textbbox((0, 0), rt, font=rl_font)
    draw.rectangle([mid[0] - 6, mid[1] + 10, mid[0] + (tb[2] - tb[0]) + 12, mid[1] + 10 + (tb[3] - tb[1]) + 12],
                    fill=(255, 255, 255, 232))
    draw.text((mid[0] + 3, mid[1] + 16), rt, font=rl_font, fill=(120, 72, 20, 255))

    # basin label
    blab, blat, blon = BASIN_LABEL
    bx, by = to_xy(blat, blon)
    blines = blab.split("\n")
    bfonts = [label_font] + [sub_font] * (len(blines) - 1)
    bw = max(draw.textbbox((0, 0), ln, font=bfonts[i])[2] for i, ln in enumerate(blines)) + 20
    bh = 26 * len(blines) + 12
    draw.rectangle([bx - bw - 30, by - bh / 2, bx - 30, by + bh / 2], fill=(255, 255, 255, 224))
    for i, ln in enumerate(blines):
        draw.text((bx - bw - 20, by - bh / 2 + 8 + i * 26), ln, font=bfonts[i], fill=(28, 28, 26, 255))

    for lab, col, lat, lon, side, voffset, gap in PINS:
        cx, cy = to_xy(lat, lon)
        lines = lab.split("\n")
        fonts = [label_font] + [sub_font] * (len(lines) - 1)
        boxw = max(draw.textbbox((0, 0), ln, font=fonts[i])[2] for i, ln in enumerate(lines)) + 20
        boxh = 26 * len(lines) + 12
        bx2 = cx + gap if side == "l" else cx - gap - boxw
        by2 = cy - boxh / 2 + voffset
        if abs(voffset) > 15 or gap > 22:
            near_x = bx2 + boxw if side == "l" else bx2
            draw.line([(cx, cy), (near_x, by2 + boxh / 2)], fill=(*col[:3], 160), width=2)
        draw.rectangle([bx2, by2, bx2 + boxw, by2 + boxh], fill=(255, 255, 255, 236))
        for i, ln in enumerate(lines):
            draw.text((bx2 + 10, by2 + 8 + i * 26), ln, font=fonts[i], fill=(28, 28, 26, 255))
        r = 12 if col == THEN_C else 11
        draw.ellipse([cx - r - 4, cy - r - 4, cx + r + 4, cy + r + 4], fill=(255, 255, 255, 245))
        draw.ellipse([cx - r, cy - r, cx + r, cy + r], fill=col)

    W, H = canvas.size
    draw.rectangle([0, 0, W, 56], fill=(255, 255, 255, 234))
    draw.text((24, 14), TITLE, font=title_font, fill=(28, 28, 26, 255))

    fb = draw.textbbox((0, 0), FOOT, font=sub_font)
    draw.rectangle([0, H - (fb[3] - fb[1]) - 20, (fb[2] - fb[0]) + 30, H], fill=(255, 255, 255, 210))
    draw.text((14, H - (fb[3] - fb[1]) - 12), FOOT, font=sub_font, fill=(80, 80, 78, 255))

    legend_font = load_font(19)
    legend = [("Kallang Airport, 1937-1955", THEN_C), ("what the area is known by now", NOW_C)]
    lx, ly = 24, H - 150
    lw = 320
    draw.rectangle([lx, ly, lx + lw, ly + 30 * len(legend) + 16], fill=(255, 255, 255, 234))
    for i, (lab, col) in enumerate(legend):
        ry = ly + 14 + i * 30
        draw.ellipse([lx + 14, ry - 8, lx + 30, ry + 8], fill=col)
        draw.text((lx + 42, ry - 11), lab, font=legend_font, fill=(28, 28, 26, 255))

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
