"""Render assets/images/posb-branch-map.png for the POSB post.

Stitches OpenStreetMap raster tiles for the Singapore bounding box into a
single base image, lightly desaturates and lightens it so the markers
read, then plots one marker per neighbourhood that has a POSB branch.
Marker positions are converted from real latitude/longitude through the
Web Mercator (slippy-map) projection the tiles use, so they land in the
right place to the neighbourhood - not at an exact street address.

OSM tile usage: a one-off fetch of ~30 tiles with a descriptive
User-Agent, well within the tile-usage policy. "Map data (c) OpenStreetMap
contributors" is burned into the image and also belongs in the post's
Sources list.

Run: python scripts/render_posb_branch_map.py
"""
import io
import math
import os
import time
import urllib.request

from PIL import Image, ImageDraw, ImageEnhance, ImageFont

ZOOM = 12
# Singapore main island, a little padding on each side.
LAT_N, LAT_S = 1.478, 1.205
LON_W, LON_E = 103.585, 104.075

OUT = os.path.join(os.path.dirname(__file__), "..", "assets", "images", "posb-branch-map.png")
TILE_URL = "https://tile.openstreetmap.org/{z}/{x}/{y}.png"
UA = "LesserKnownSingapore-map-render/1.0 (one-off static map for a blog post)"

# One entry per neighbourhood with a POSB branch (approximate centres).
BRANCHES = [
    ("Woodlands", 1.4360, 103.7865), ("Marsiling", 1.4327, 103.7740),
    ("Admiralty", 1.4406, 103.8009), ("Sembawang", 1.4491, 103.8200),
    ("Yishun", 1.4294, 103.8350), ("Khatib", 1.4173, 103.8329),
    ("Sengkang", 1.3924, 103.8949), ("Buangkok", 1.3830, 103.8934),
    ("Punggol", 1.4074, 103.9020), ("Hougang", 1.3720, 103.8935),
    ("Kovan", 1.3601, 103.8850), ("Serangoon", 1.3506, 103.8720),
    ("Ang Mo Kio", 1.3690, 103.8480), ("Bishan", 1.3506, 103.8486),
    ("Toa Payoh", 1.3324, 103.8470), ("Novena", 1.3202, 103.8438),
    ("Newton", 1.3130, 103.8390), ("Orchard", 1.3040, 103.8320),
    ("Somerset", 1.3010, 103.8386), ("Dhoby Ghaut", 1.2996, 103.8455),
    ("City Hall", 1.2933, 103.8520), ("Raffles Place", 1.2839, 103.8515),
    ("Chinatown", 1.2847, 103.8430), ("Tanjong Pagar", 1.2765, 103.8457),
    ("Bugis", 1.2996, 103.8556), ("Jalan Besar", 1.3070, 103.8560),
    ("Kallang", 1.3025, 103.8710), ("Geylang", 1.3180, 103.8930),
    ("Paya Lebar", 1.3340, 103.8930), ("MacPherson", 1.3267, 103.8900),
    ("Eunos", 1.3197, 103.9030), ("Marine Parade", 1.3010, 103.9050),
    ("Mountbatten", 1.3020, 103.8830), ("Bedok", 1.3250, 103.9300),
    ("Tampines", 1.3530, 103.9450), ("Tampines East", 1.3560, 103.9560),
    ("Simei", 1.3430, 103.9530), ("Pasir Ris", 1.3730, 103.9490),
    ("Loyang", 1.3660, 103.9660), ("Changi Village", 1.3890, 103.9880),
    ("Queenstown", 1.2900, 103.8050), ("Commonwealth", 1.3010, 103.7980),
    ("Buona Vista", 1.3070, 103.7880), ("Holland Village", 1.3115, 103.7960),
    ("Clementi", 1.3150, 103.7640), ("Dover", 1.3110, 103.7790),
    ("West Coast", 1.3060, 103.7650), ("Jurong East", 1.3330, 103.7420),
    ("Jurong West", 1.3400, 103.7060), ("Boon Lay", 1.3390, 103.7020),
    ("Pioneer", 1.3375, 103.6970), ("Taman Jurong", 1.3340, 103.7200),
    ("Bukit Batok", 1.3500, 103.7490), ("Bukit Gombak", 1.3590, 103.7520),
    ("Choa Chu Kang", 1.3850, 103.7450), ("Yew Tee", 1.3970, 103.7470),
    ("Bukit Panjang", 1.3790, 103.7620), ("Beauty World", 1.3410, 103.7760),
    ("Bukit Timah", 1.3300, 103.8020),
]

LABELS = [
    ("WOODLANDS", 1.446, 103.787), ("PUNGGOL", 1.417, 103.905),
    ("JURONG", 1.335, 103.702), ("TAMPINES", 1.362, 103.945),
    ("CHANGI", 1.373, 103.988), ("CITY", 1.279, 103.848),
]


def deg2px(lat, lon, z):
    n = 2.0 ** z
    x = (lon + 180.0) / 360.0 * n * 256.0
    lat_r = math.radians(lat)
    y = (1.0 - math.asinh(math.tan(lat_r)) / math.pi) / 2.0 * n * 256.0
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

    w = (tx1 - tx0 + 1) * 256
    h = (ty1 - ty0 + 1) * 256
    base = Image.new("RGB", (w, h), "#dddddd")
    print(f"stitching {tx1 - tx0 + 1}x{ty1 - ty0 + 1} tiles at z{ZOOM} ({w}x{h}px)")
    for tx in range(tx0, tx1 + 1):
        for ty in range(ty0, ty1 + 1):
            try:
                tile = fetch_tile(ZOOM, tx, ty)
                base.paste(tile, ((tx - tx0) * 256, (ty - ty0) * 256))
            except Exception as e:  # noqa: BLE001 - one missing tile shouldn't abort
                print(f"  tile {tx},{ty} failed: {e}")
            time.sleep(0.1)

    # Mute the basemap so the markers dominate.
    base = ImageEnhance.Color(base).enhance(0.45)
    base = ImageEnhance.Brightness(base).enhance(1.12)
    base = ImageEnhance.Contrast(base).enhance(0.92)
    base = Image.blend(base, Image.new("RGB", base.size, "#ffffff"), 0.28)

    ox, oy = tx0 * 256, ty0 * 256
    draw = ImageDraw.Draw(base, "RGBA")

    lab_font = load_font(30, bold=True)
    for name, lat, lon in LABELS:
        px, py = deg2px(lat, lon, ZOOM)
        draw.text((px - ox, py - oy), name, font=lab_font, fill=(60, 60, 58, 235),
                  anchor="mm", stroke_width=4, stroke_fill=(255, 255, 255, 220))

    for _name, lat, lon in BRANCHES:
        px, py = deg2px(lat, lon, ZOOM)
        cx, cy = px - ox, py - oy
        draw.ellipse([cx - 11, cy - 11, cx + 11, cy + 11], fill=(255, 255, 255, 235))
        draw.ellipse([cx - 8, cy - 8, cx + 8, cy + 8], fill=(41, 108, 214, 255))

    # Crop to the island with a small margin.
    cx0, _ = deg2px(LAT_N, LON_W - 0.008, ZOOM)
    cx1, _ = deg2px(LAT_N, LON_E + 0.008, ZOOM)
    _, cy0 = deg2px(LAT_N + 0.006, LON_W, ZOOM)
    _, cy1 = deg2px(LAT_S - 0.006, LON_W, ZOOM)
    crop = base.crop((int(cx0 - ox), int(cy0 - oy), int(cx1 - ox), int(cy1 - oy)))

    cd = ImageDraw.Draw(crop, "RGBA")
    cred_font = load_font(20)
    txt = "Map data (c) OpenStreetMap contributors"
    tb = cd.textbbox((0, 0), txt, font=cred_font)
    tw, th = tb[2] - tb[0], tb[3] - tb[1]
    cw, ch = crop.size
    cd.rectangle([cw - tw - 22, ch - th - 18, cw, ch], fill=(255, 255, 255, 205))
    cd.text((cw - tw - 12, ch - th - 12), txt, font=cred_font, fill=(70, 70, 68, 255))

    # Downscale for the web (2x for crispness).
    target_w = 1600
    scale = target_w / crop.width
    crop = crop.resize((target_w, int(crop.height * scale)), Image.LANCZOS)

    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    crop.save(OUT, optimize=True)
    print(f"wrote {OUT}  ({crop.size[0]}x{crop.size[1]})")


if __name__ == "__main__":
    main()
