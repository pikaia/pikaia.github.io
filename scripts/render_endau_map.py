"""Render assets/images/endau-bahau-map.png for the Endau settlement post.

Today's OpenStreetMap map of southern Malaya (muted), with the two wartime
farm settlements marked against Syonan (Singapore): New Syonan at Endau, on
Johor's east coast, and Fuji-go at Bahau, in Negri Sembilan. No route line is
drawn, since how each party travelled is not recorded in the sources used;
the markers show only where the settlements lay. Distances are straight-line.

"Map data (c) OpenStreetMap contributors" is burned in and belongs in the
post's Sources list. Tiles are cached in scratch/endau-map/ after the first run.

    python scripts/render_endau_map.py
"""
import io
import math
import time
import urllib.request
from pathlib import Path

from PIL import Image, ImageDraw, ImageEnhance, ImageFont

ROOT = Path(__file__).resolve().parent.parent
CACHE = ROOT / "scratch" / "endau-map"
OUT = ROOT / "assets" / "images" / "endau-bahau-map.png"
UA = "LesserKnownSingapore-map-render/1.0 (one-off static map for a blog post)"

Z = 9
LAT_N, LAT_S = 3.35, 1.05
LON_W, LON_E = 101.75, 104.55
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
            time.sleep(0.2)
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


SYONAN = (1.29, 103.85)
# name, second line, (lat, lon), label offset (dx, dy), anchor, kind
PLACES = [
    ("Syonan (Singapore)", "", SYONAN, (-18, 4), "rm", "city"),
    ("New Syonan, Endau", "Chinese settlers, from Feb 1944", (2.65, 103.62), (20, -2), "lm", "settlement"),
    ("Fuji-go, Bahau", "Catholic settlers, from Dec 1943", (2.81, 102.40), (20, -30), "lm", "settlement"),
    ("Mersing", "", (2.43, 103.84), (16, 0), "lm", "town"),
    ("Kota Tinggi", "", (1.73, 103.90), (16, 0), "lm", "town"),
    ("Johore Bahru", "", (1.46, 103.76), (-16, -4), "rm", "town"),
    ("Gemas", "", (2.58, 102.61), (14, 12), "lm", "town"),
]
SETTLE_COL = (176, 38, 30)


def km(a, b):
    la1, lo1, la2, lo2 = map(math.radians, (*a, *b))
    h = math.sin((la2 - la1) / 2) ** 2 + math.cos(la1) * math.cos(la2) * math.sin((lo2 - lo1) / 2) ** 2
    return 2 * 6371 * math.asin(math.sqrt(h))


def main():
    base = base_tile()
    W, H = base.size
    muted = ImageEnhance.Color(base).enhance(0.35)
    img = Image.blend(muted, Image.new("RGB", base.size, "white"), 0.3).convert("RGBA")
    d = ImageDraw.Draw(img)
    # dashed straight-line distance guides from Syonan to each settlement
    sx, sy = px(*SYONAN)
    for name, _sub, ll, *_rest in PLACES:
        if _rest[-1] != "settlement":
            continue
        ex, ey = px(*ll)
        n = int(math.dist((sx, sy), (ex, ey)) // 12) + 1
        for i in range(0, n, 2):
            p0 = (sx + (ex - sx) * i / n, sy + (ey - sy) * i / n)
            p1 = (sx + (ex - sx) * min(i + 1, n) / n, sy + (ey - sy) * min(i + 1, n) / n)
            d.line([p0, p1], fill=(90, 90, 86, 255), width=3)
        mx, my = (sx + ex) / 2, (sy + ey) / 2
        lab = f"about {round(km(SYONAN, ll), -1):.0f} km"
        tb = d.textbbox((mx, my), lab, font=font(20), anchor="mm")
        d.rounded_rectangle([tb[0] - 6, tb[1] - 4, tb[2] + 6, tb[3] + 4], radius=6, fill=(255, 255, 255, 230))
        d.text((mx, my), lab, font=font(20), fill=(70, 70, 68, 255), anchor="mm")
    for name, sub, (lat, lon), (dx, dy), anchor, kind in PLACES:
        x, y = px(lat, lon)
        r = {"settlement": 11, "city": 10, "town": 6}[kind]
        fill = SETTLE_COL if kind == "settlement" else (28, 28, 26)
        d.ellipse([x - r, y - r, x + r, y + r], fill=fill + (255,), outline=(255, 255, 255, 255), width=3)
        f = font({"settlement": 26, "city": 26, "town": 20}[kind], bold=kind != "town")
        tb = d.textbbox((x + dx, y + dy), name, font=f, anchor=anchor)
        box = list(tb)
        if sub:
            sb = d.textbbox((tb[0], tb[3] + 8), sub, font=font(20), anchor="lt")
            box = [min(tb[0], sb[0]), tb[1], max(tb[2], sb[2]), sb[3]]
        d.rounded_rectangle([box[0] - 7, box[1] - 5, box[2] + 7, box[3] + 5], radius=6, fill=(255, 255, 255, 228))
        d.text((x + dx, y + dy), name, font=f, fill=(28, 28, 26, 255), anchor=anchor)
        if sub:
            d.text((tb[0], tb[3] + 8), sub, font=font(20), fill=(70, 70, 68, 255), anchor="lt")
    d.rectangle([0, 0, W, 64], fill=(255, 255, 255, 235))
    d.text((24, 14), "The wartime farm settlements, 1943-45", font=font(32, bold=True), fill=(28, 28, 26, 255))
    foot = "Settlement markers are approximate; dashed lines show straight-line distance, not a route."
    fb = d.textbbox((0, 0), foot, font=font(18))
    d.rectangle([0, H - 64, fb[2] + 30, H - 32], fill=(255, 255, 255, 225))
    d.text((14, H - 58), foot, font=font(18), fill=(70, 70, 68, 255))
    cred = "Map data (c) OpenStreetMap contributors"
    cb = d.textbbox((0, 0), cred, font=font(18))
    d.rectangle([0, H - 32, cb[2] + 30, H], fill=(255, 255, 255, 225))
    d.text((14, H - 27), cred, font=font(18), fill=(70, 70, 68, 255))
    img.convert("RGB").resize((1600, round(1600 * H / W)), Image.LANCZOS).save(OUT, optimize=True)
    print("wrote", OUT, img.size)


if __name__ == "__main__":
    main()
