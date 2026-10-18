"""Render the two-stage map of Sir Manasseh Meyer's town properties for the
Manasseh Meyer post:

  assets/images/meyer-map-0.png  his main buildings in town around 1930
  assets/images/meyer-map-1.png  the same sites today: what still stands, what replaced the rest

Each is today's OpenStreetMap map of the city centre (muted). The markers are
placed on the present-day buildings or streets that occupy the sites, so they
show roughly where each property stood, not surveyed plot boundaries. His
seaside properties at Katong and his gift to Raffles College lie off the map and
are noted at its edges.

"Map data (c) OpenStreetMap contributors" is burned in and belongs in the post's
Sources list. Tiles are cached in scratch/mm/.

    python scripts/render_meyer_map.py
"""
import io
import math
import time
import urllib.request
from pathlib import Path

from PIL import Image, ImageDraw, ImageEnhance, ImageFont

ROOT = Path(__file__).resolve().parent.parent
CACHE = ROOT / "scratch" / "mm"
OUT = ROOT / "assets" / "images"
UA = "LesserKnownSingapore-map-render/1.0 (one-off static map for a blog post)"

Z = 16
LAT_N, LAT_S = 1.3036, 1.2812
LON_W, LON_E = 103.8375, 103.8590
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
            time.sleep(0.15)
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


# (1930 label, today label, still standing?, (lat, lon) from OSM, label offset)
PLACES = [
    ("Belle Vue, his home, and Chesed-El (1905)", "Chesed-El still stands; Belle Vue is gone",
     True, (1.29725, 103.84262), (16, -14)),
    ("Maghain Aboth synagogue (1878)", "Maghain Aboth still stands",
     True, (1.29823, 103.85070), (16, -14)),
    ("Meyer Mansions", "Meyer Mansions: now Peninsula Plaza",
     False, (1.29233, 103.85083), (-16, -14)),
    ("Adelphi Hotel", "Adelphi Hotel: demolished 1980",
     False, (1.29115, 103.85116), (16, 12)),
    ("Raffles Place: shops and offices, Meyer Chambers", "Raffles Place: all rebuilt as office towers",
     False, (1.28430, 103.85130), (-16, -14)),
]
GREEN, GREY, RED = (30, 130, 70), (130, 130, 128), (200, 40, 40)


def main():
    base = base_tile()
    W, H = base.size
    muted = ImageEnhance.Color(base).enhance(0.25)
    muted = Image.blend(muted, Image.new("RGB", base.size, "white"), 0.35)
    titles = ["Sir Manasseh Meyer's buildings in town, around 1930", "The same sites today"]
    for stage in range(2):
        img = muted.copy().convert("RGBA")
        dr = ImageDraw.Draw(img)
        for lab0, lab1, stands, (lat, lon), (ox, oy) in PLACES:
            x, y = px(lat, lon)
            col = RED if stage == 0 else (GREEN if stands else GREY)
            name = lab0 if stage == 0 else lab1
            dr.ellipse([x - 10, y - 10, x + 10, y + 10], fill=col + (255,), outline=(255, 255, 255, 255), width=3)
            f = font(21, bold=True)
            tb = dr.textbbox((0, 0), name, font=f)
            tx = x + ox if ox >= 0 else x + ox - tb[2]
            dr.rectangle([tx - 6, y + oy - 4, tx + tb[2] + 6, y + oy + tb[3] + 4], fill=(255, 255, 255, 235))
            dr.text((tx, y + oy), name, font=f, fill=(28, 28, 26, 255))
        # Off-map notes, stacked above the footer.
        notes = (["Off the map, east at Katong: Crescent Flats and the Sea View Hotel",
                  "Off the map, on Bukit Timah Road: his gift to Raffles College"] if stage == 0 else
                 ["Off the map, east at Katong: Crescent Flats and the Sea View Hotel are gone",
                  "Off the map, on Bukit Timah Road: the Manasseh Meyer Building still stands"])
        f = font(19, bold=True)
        for i, t in enumerate(notes):
            ny = H - 118 + i * 34
            tb = dr.textbbox((0, 0), t, font=f)
            dr.rectangle([16, ny - 5, 24 + tb[2] + 8, ny + tb[3] + 5], fill=(255, 255, 255, 235))
            dr.text((24, ny), t, font=f, fill=(60, 60, 58, 255))
        dr.rectangle([0, 0, W, 62], fill=(255, 255, 255, 235))
        dr.text((24, 14), titles[stage], font=font(30, bold=True), fill=(28, 28, 26, 255))
        if stage == 1:
            lx = W - 24
            for lab, col in (("gone", GREY), ("still standing", GREEN)):
                tb = dr.textbbox((0, 0), lab, font=font(19))
                lx -= tb[2]
                dr.text((lx, 22), lab, font=font(19), fill=(60, 60, 58, 255))
                dr.ellipse([lx - 26, 22, lx - 8, 40], fill=col + (255,))
                lx -= 46
        foot = "Sites marked on today's map; approximate."
        fb = dr.textbbox((0, 0), foot, font=font(19))
        dr.rectangle([0, H - 40, fb[2] + 34, H], fill=(255, 255, 255, 225))
        dr.text((16, H - 32), foot, font=font(19), fill=(70, 70, 68, 255))
        cred = "Map data (c) OpenStreetMap contributors"
        cb = dr.textbbox((0, 0), cred, font=font(18))
        dr.rectangle([W - cb[2] - 34, H - 40, W, H], fill=(255, 255, 255, 225))
        dr.text((W - cb[2] - 16, H - 32), cred, font=font(18), fill=(70, 70, 68, 255))
        out = OUT / f"meyer-map-{stage}.png"
        img.convert("RGB").save(out, optimize=True)
        print("wrote", out, img.size)


if __name__ == "__main__":
    main()
