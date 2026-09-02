"""Render assets/images/malaysian-railway-land-map.png for the Malaysian
railway-land post.

Stitches OpenStreetMap tiles for the whole of Singapore, mutes them, and
traces (hand-plotted, approximate) the former KTM rail line from the
Woodlands Causeway down to the Tanjong Pagar terminus - the strip of
land that stayed under Malaysian administration until 2011. Also marks
the six parcels Malaysia received in the 2010 swap (Marina South,
Ophir-Rochor) and the new RTS Link point at Woodlands North.

The route line is a rough stand-in plotted against the tile, not a
precise survey of the historical alignment (same convention as the
route-walk slides). "Map data (c) OpenStreetMap contributors" is burned
in and belongs in the post's Sources list. Committed binary, same
documented exception as the other OSM maps / chart PNGs.

    python scripts/render_malaysian_railway_land_map.py
"""
import io
import math
import os
import time
import urllib.request

from PIL import Image, ImageDraw, ImageEnhance, ImageFont

ZOOM = 13
LAT_N, LAT_S = 1.475, 1.235
LON_W, LON_E = 103.685, 103.895

OUT = os.path.join(os.path.dirname(__file__), "..", "assets", "images", "malaysian-railway-land-map.png")
TILE_URL = "https://tile.openstreetmap.org/{z}/{x}/{y}.png"
UA = "LesserKnownSingapore-map-render/1.0 (one-off static map for a blog post)"

RAIL_C = (196, 76, 40, 255)     # the KTM line
PARCEL_C = (37, 99, 197, 255)   # land Malaysia received in the swap
RTS_C = (60, 130, 70, 255)      # the new RTS Link

# Hand-plotted nodes tracing the former line, Woodlands -> Tanjong Pagar,
# following the corridor still faintly visible on the tile.
ROUTE = [
    (1.4470, 103.7690),  # Woodlands, near the Causeway
    (1.4380, 103.7560),
    (1.4180, 103.7480),  # Kranji / Sungei Kadut
    (1.3950, 103.7500),
    (1.3720, 103.7625),  # Hillview / Bukit Panjang
    (1.3540, 103.7705),
    (1.33896, 103.77693),  # Bukit Timah Railway Station
    (1.3230, 103.7835),
    (1.3140, 103.7875),  # Clementi / Ulu Pandan
    (1.3055, 103.7915),  # Buona Vista bend
    (1.2960, 103.7995),  # Tanglin Halt / Commonwealth
    (1.2875, 103.8115),  # Queensway
    (1.2800, 103.8255),  # Alexandra
    (1.2745, 103.8360),
    (1.27295, 103.83847),  # Tanjong Pagar Railway Station
]

# label, colour, lat, lon, text-side ("l" = right of dot, "r" = left)
PINS = [
    ("Woodlands\n(Causeway)", RAIL_C, 1.4470, 103.7690, "r"),
    ("Bukit Timah\nstation", RAIL_C, 1.33896, 103.77693, "l"),
    ("Tanjong Pagar\nterminus", RAIL_C, 1.27295, 103.83847, "r"),
    ("Woodlands North\n(RTS Link, ~2027)", RTS_C, 1.4498, 103.7862, "l"),
    ("Ophir-Rochor\nparcels", PARCEL_C, 1.3010, 103.8595, "l"),
    ("Marina South\nparcels", PARCEL_C, 1.2755, 103.8645, "l"),
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

    canvas = tiles.convert("RGB")
    draw = ImageDraw.Draw(canvas, "RGBA")
    ox, oy = tx0 * 256, ty0 * 256
    label_font = load_font(20, bold=True)
    sub_font = load_font(18)

    pts = [(deg2px(lat, lon, ZOOM)[0] - ox, deg2px(lat, lon, ZOOM)[1] - oy) for lat, lon in ROUTE]
    draw.line(pts, fill=(196, 76, 40, 235), width=6, joint="curve")
    draw.line(pts, fill=(255, 255, 255, 130), width=2, joint="curve")

    for lab, col, lat, lon, side in PINS:
        px, py = deg2px(lat, lon, ZOOM)
        cx, cy = px - ox, py - oy
        draw.ellipse([cx - 13, cy - 13, cx + 13, cy + 13], fill=(255, 255, 255, 245))
        draw.ellipse([cx - 9, cy - 9, cx + 9, cy + 9], fill=col)
        lines = lab.split("\n")
        widths = [draw.textbbox((0, 0), ln, font=(label_font if i == 0 else sub_font))[2]
                  for i, ln in enumerate(lines)]
        boxw = max(widths) + 18
        boxh = 27 * len(lines) + 10
        bx = cx + 20 if side == "l" else cx - 20 - boxw
        by = cy - boxh / 2
        draw.rectangle([bx, by, bx + boxw, by + boxh], fill=(255, 255, 255, 232))
        for i, ln in enumerate(lines):
            draw.text((bx + 9, by + 6 + i * 27), ln,
                      font=(label_font if i == 0 else sub_font), fill=(30, 30, 28, 255))

    cred_font = load_font(18)
    txt = "Map data (c) OpenStreetMap contributors"
    tb = draw.textbbox((0, 0), txt, font=cred_font)
    cw, ch = tb[2] - tb[0], tb[3] - tb[1]
    W, H = canvas.size
    draw.rectangle([W - cw - 22, H - ch - 18, W, H], fill=(255, 255, 255, 215))
    draw.text((W - cw - 12, H - ch - 12), txt, font=cred_font, fill=(70, 70, 68, 255))

    target_w = 1500
    scale = target_w / canvas.width
    canvas = canvas.resize((target_w, int(canvas.height * scale)), Image.LANCZOS)

    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    canvas.save(OUT, optimize=True)
    print(f"wrote {OUT}  ({canvas.size[0]}x{canvas.size[1]})")


if __name__ == "__main__":
    main()
