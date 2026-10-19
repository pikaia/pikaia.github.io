"""Render the three-stage map of Blakang Mati for the Blakang Mati post:

  assets/images/blakang-mati-map-0.png  the fortress island, around 1900
  assets/images/blakang-mati-map-1.png  the kampongs and the garrison, 1950s-60s
  assets/images/blakang-mati-map-2.png  the same sites on Sentosa today

Each is today's OpenStreetMap map of Sentosa (muted). The island has been
reclaimed and reshaped since the 1970s, so the markers are placed on the
present-day buildings that occupy the sites and show only roughly where each
place stood. The kampong positions follow the NHB Sentosa Heritage Trail guide
(the Hokkien village by the jetty, where Universal Studios now stands, and the
Malay village further west, facing Pulau Selegu) and are approximate.

"Map data (c) OpenStreetMap contributors" is burned in and belongs in the post's
Sources list. Tiles are cached in scratch/bmm/.

    python scripts/render_blakang_mati_map.py
"""
import io
import math
import time
import urllib.request
from pathlib import Path

from PIL import Image, ImageDraw, ImageEnhance, ImageFont

ROOT = Path(__file__).resolve().parent.parent
CACHE = ROOT / "scratch" / "bmm"
OUT = ROOT / "assets" / "images"
UA = "LesserKnownSingapore-map-render/1.0 (one-off static map for a blog post)"

Z = 16
LAT_N, LAT_S = 1.2672, 1.2395
LON_W, LON_E = 103.8040, 103.8430
N = 2.0 ** Z
SCALE = 0.62  # the Z16 render is ~1800px wide; shrink to ~1100px for the post


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


SILOSO = (1.25877, 103.80880)
IMBIAH = (1.25693, 103.81471)
SERAPONG = (1.25009, 103.83340)
CONNAUGHT = (1.24420, 103.83640)   # inside today's golf course; approximate
BARRACKS = (1.25199, 103.82100)    # parade ground, now the Barracks Lawn
MESS = (1.24970, 103.82443)        # Officers' Mess, now Capella Singapore
HOSPITAL = (1.25410, 103.81777)    # "Sick Quarters", now Madame Tussauds
JETTY_KG = (1.25420, 103.82267)    # Hokkien kampong by the jetty, now Universal Studios
MALAY_KG = (1.25660, 103.81620)    # Malay kampong facing Pulau Selegu; approximate
JARDINE = (1.26415, 103.82024)     # Jardine Steps, now HarbourFront

# Per stage: (label, (lat, lon), colour key, label offset (dx, dy) in full-res px)
STAGES = [
    ("The fortress island, around 1900", [
        ("Fort Siloso (1878)", SILOSO, "red", (26, -50)),
        ("Mount Imbiah battery", IMBIAH, "red", (26, -64)),
        ("Military hospital", HOSPITAL, "red", (26, 10)),
        ("Barracks and parade ground", BARRACKS, "red", (26, -22)),
        ("Officers' Mess", MESS, "red", (26, -6)),
        ("Fort Serapong", SERAPONG, "red", (26, -22)),
        ("Fort Connaught (1878)", CONNAUGHT, "red", (-26, -22)),
    ], []),
    ("The kampongs and the garrison, 1950s-60s", [
        ("Malay kampong", MALAY_KG, "blue", (-26, -60)),
        ("Hokkien kampong by the jetty", JETTY_KG, "blue", (26, -22)),
        ("Gurkha battalions in the barracks", BARRACKS, "red", (26, 6)),
        ("Army ferry from Jardine Steps", JARDINE, "red", (26, -22)),
    ], [(JARDINE, JETTY_KG)]),
    ("The same places on Sentosa today", [
        ("Fort Siloso: museum and monument", SILOSO, "green", (26, -50)),
        ("Old hospital: Madame Tussauds", HOSPITAL, "green", (26, 10)),
        ("Hokkien kampong: Universal Studios", JETTY_KG, "grey", (26, -40)),
        ("Malay kampong: gone", MALAY_KG, "grey", (-26, -60)),
        ("Barracks: hotels and restaurants", BARRACKS, "green", (26, -6)),
        ("Officers' Mess: Capella hotel", MESS, "green", (26, 12)),
        ("Fort Connaught: remains in a golf course", CONNAUGHT, "grey", (-26, -22)),
    ], []),
]
COLS = {"red": (200, 40, 40), "blue": (40, 90, 190), "green": (30, 130, 70), "grey": (130, 130, 128)}
INK = (28, 28, 26, 255)


def label(dr, x, y, text, off, f):
    ox, oy = off
    tb = dr.textbbox((0, 0), text, font=f)
    tx = x + ox if ox >= 0 else x + ox - tb[2]
    dr.rectangle([tx - 8, y + oy - 6, tx + tb[2] + 8, y + oy + tb[3] + 6], fill=(255, 255, 255, 235))
    dr.text((tx, y + oy), text, font=f, fill=INK)


def main():
    base = base_tile()
    W, H = base.size
    muted = ImageEnhance.Color(base).enhance(0.25)
    muted = Image.blend(muted, Image.new("RGB", base.size, "white"), 0.35)
    for i, (title, places, lines) in enumerate(STAGES):
        img = muted.copy().convert("RGBA")
        dr = ImageDraw.Draw(img)
        for a, b in lines:
            (x1, y1), (x2, y2) = px(*a), px(*b)
            steps = int(math.hypot(x2 - x1, y2 - y1) / 22)
            for s in range(0, steps, 2):
                t0, t1 = s / steps, (s + 1) / steps
                dr.line([x1 + (x2 - x1) * t0, y1 + (y2 - y1) * t0, x1 + (x2 - x1) * t1, y1 + (y2 - y1) * t1],
                        fill=COLS["red"] + (255,), width=7)
        f = font(34, bold=True)
        for name, (lat, lon), ck, off in places:
            x, y = px(lat, lon)
            dr.ellipse([x - 16, y - 16, x + 16, y + 16], fill=COLS[ck] + (255,), outline=(255, 255, 255, 255), width=5)
            label(dr, x, y, name, off, f)
        if i == 1:
            note = "Off the map, north across the harbour: Telok Blangah, where the villagers were rehoused in the 1970s"
            nf = font(28, bold=True)
            tb = dr.textbbox((0, 0), note, font=nf)
            ny = H - 128
            dr.rectangle([24, ny - 8, 40 + tb[2] + 16, ny + tb[3] + 10], fill=(255, 255, 255, 235))
            dr.text((40, ny), note, font=nf, fill=(60, 60, 58, 255))
        dr.rectangle([0, 0, W, 100], fill=(255, 255, 255, 235))
        dr.text((40, 24), title, font=font(50, bold=True), fill=INK)
        legend = {0: [("forts and barracks", "red")],
                  1: [("military", "red"), ("kampongs", "blue")],
                  2: [("gone", "grey"), ("still standing", "green")]}[i]
        lx = W - 40
        for lab, ck in legend:
            tb = dr.textbbox((0, 0), lab, font=font(32))
            lx -= tb[2]
            dr.text((lx, 34), lab, font=font(32), fill=(60, 60, 58, 255))
            dr.ellipse([lx - 42, 36, lx - 12, 66], fill=COLS[ck] + (255,))
            lx -= 76
        foot = "Places marked on today's map, which reclamation has reshaped; approximate."
        fb = dr.textbbox((0, 0), foot, font=font(30))
        dr.rectangle([0, H - 64, fb[2] + 56, H], fill=(255, 255, 255, 225))
        dr.text((26, H - 52), foot, font=font(30), fill=(70, 70, 68, 255))
        cred = "Map data (c) OpenStreetMap contributors"
        cb = dr.textbbox((0, 0), cred, font=font(29))
        dr.rectangle([W - cb[2] - 56, H - 64, W, H], fill=(255, 255, 255, 225))
        dr.text((W - cb[2] - 26, H - 52), cred, font=font(29), fill=(70, 70, 68, 255))
        out = OUT / f"blakang-mati-map-{i}.png"
        img = img.convert("RGB").resize((round(W * SCALE), round(H * SCALE)), Image.LANCZOS)
        img.save(out, optimize=True)
        print("wrote", out, img.size)


if __name__ == "__main__":
    main()
