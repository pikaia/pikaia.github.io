"""Render the stage-by-stage reclamation maps for the shoreline post:

  assets/images/reclamation-map-0.png ... reclamation-map-5.png

Each is today's OpenStreetMap map of the downtown waterfront (muted), with the
land reclaimed up to that stage shaded, oldest darkest:

  0  today's map only (the old beach along Telok Ayer Street marked)
  1  + 1822: the south bank of the river filled for Boat Quay and Commercial Square
  2  + 1864: Collyer Quay's seawall and the strip behind it
  3  + 1879-97: the Telok Ayer reclamation (Cecil Street, Robinson Road, Raffles Quay)
  4  + 1932: the Telok Ayer Basin reclamation (the land Shenton Way was built on)
  5  + after 1965: Marina Bay and the rest of the modern waterfront

The areas are hand-set approximations, anchored on today's street geometry from
OpenStreetMap (Telok Ayer Street as the old beach, Raffles Quay and Collyer Quay
as the 19th-century seafront, Shenton Way for the 1930s land) and checked by eye
against Jackson's 1822 plan, the 1893 Constable city plan and a 1951 town map.
They show roughly where the shoreline moved, not surveyed boundaries.

"Map data (c) OpenStreetMap contributors" is burned in and belongs in the post's
Sources list. Tiles are cached in scratch/rc/ after the first run.

    python scripts/render_reclamation_map.py
"""
import io
import json
import math
import time
import urllib.parse
import urllib.request
from pathlib import Path

import numpy as np
from PIL import Image, ImageDraw, ImageEnhance, ImageFont

ROOT = Path(__file__).resolve().parent.parent
CACHE = ROOT / "scratch" / "rc"
OUT = ROOT / "assets" / "images"
UA = "LesserKnownSingapore-map-render/1.0 (one-off static map for a blog post)"

Z = 16
LAT_N, LAT_S = 1.2935, 1.2665
LON_W, LON_E = 103.834, 103.872
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


def streets():
    p = CACHE / "streets.json"
    if not p.exists():
        names = ["Telok Ayer Street", "Robinson Road", "Raffles Quay", "Shenton Way"]
        q = "[out:json][timeout:60];(" + "".join(
            f'way["name"="{n}"]({LAT_S},{LON_W},{LAT_N},{LON_E});' for n in names) + ");out geom;"
        req = urllib.request.Request("https://overpass-api.de/api/interpreter",
                                     data=urllib.parse.urlencode({"data": q}).encode(), headers={"User-Agent": UA})
        p.write_text(urllib.request.urlopen(req, timeout=90).read().decode())
    d = json.loads(p.read_text())
    out = {}
    for e in d["elements"]:
        if "highway" not in e["tags"]:
            continue
        out.setdefault(e["tags"]["name"], []).extend(px(g["lat"], g["lon"]) for g in e["geometry"])
    return out


def line_along(pts, y_from, y_to, step=12):
    """Resample a street's points into an ordered line (by y), x = mean x of nearby points."""
    a = np.array(pts)
    ys = np.arange(y_from, y_to + 1, step)
    line = []
    for y in ys:
        near = a[np.abs(a[:, 1] - y) < step * 1.5]
        if len(near):
            line.append((float(near[:, 0].mean()), float(y)))
    return line


def font(size, bold=False):
    for nm in (["arialbd.ttf"] if bold else ["arial.ttf"]) + ["DejaVuSans-Bold.ttf" if bold else "DejaVuSans.ttf"]:
        try:
            return ImageFont.truetype(nm, size)
        except OSError:
            continue
    return ImageFont.load_default()


# Oldest darkest (a single-hue sequential ramp: time order, not categories).
COLS = [(140, 45, 4), (204, 76, 2), (236, 112, 20), (254, 153, 41), (254, 217, 142)]
LABELS = ["1822", "1864", "1879-97", "1893-1932", "after 1965"]
NAMES = ["Boat Quay and Commercial Square filled", "Collyer Quay seawall", "Telok Ayer reclamation",
         "Telok Ayer Basin reclamation", "Marina Bay and the modern waterfront"]


def polygons(st):
    """Hand-set stage polygons in pixel space, anchored on street lines."""
    telok = sorted(line_along(st["Telok Ayer Street"], 450, 720), key=lambda p: p[1])
    shenton = sorted(line_along(st["Shenton Way"], 640, 930), key=lambda p: p[1])
    robinson = st["Robinson Road"]
    # 1897 seafront south of today's Raffles Quay: a block seaward of Robinson Road,
    # just inland of Shenton Way (which was built on the 1930s land).
    rob = np.array(robinson)

    def toward_rob(p, f):
        near = rob[np.argmin(np.abs(rob[:, 1] - p[1]))]
        return (p[0] * (1 - f) + near[0] * f, p[1])
    rq1897 = [(835, 505), (805, 565), (782, 612)] + [toward_rob(p, 0.3) for p in shenton]
    # 1932 seafront: just seaward of Shenton Way.
    sh1932 = [(835, 505), (812, 560)] + [(p[0] + 45, p[1] + 10) for p in shenton]
    old_beach_south = telok + [(595, 800), (575, 900)]

    p1822 = [(690, 250), (712, 300), (735, 345), (760, 372), (815, 382), (830, 400), (822, 470),
             (800, 505), (760, 500), (740, 455), (705, 425), (690, 380), (682, 310)]
    p1864 = [(912, 368), (890, 430), (855, 505), (835, 505), (822, 470), (832, 400), (870, 372)]
    p1897 = [(740, 455), (760, 500), (800, 505), (835, 505)] + rq1897 + list(reversed(old_beach_south))
    p1932 = [(835, 505)] + sh1932 + list(reversed(rq1897))
    # Everything land-side seaward of the 1960 waterfront (water masked out later).
    coast1960 = [(1000, 0), (960, 180), (925, 250), (905, 330), (915, 360), (890, 430), (855, 505)] + sh1932[1:] + [(560, 1000), (480, 1005), (0, 1010)]
    pmod = coast1960 + [(0, 1259), (1771, 1259), (1771, 0)]
    return [p1822, p1864, p1897, p1932, pmod], old_beach_south, telok


def main():
    base = base_tile()
    W, H = base.size
    arr = np.asarray(base).astype(int)
    water = (np.abs(arr[:, :, 0] - 170) < 14) & (np.abs(arr[:, :, 1] - 211) < 14) & (np.abs(arr[:, :, 2] - 223) < 14)
    land = Image.fromarray((~water * 255).astype(np.uint8))

    muted = ImageEnhance.Color(base).enhance(0.25)
    muted = Image.blend(muted, Image.new("RGB", base.size, "white"), 0.35)
    st = streets()
    polys, beach, telok = polygons(st)

    lab_pos = [(700, 330), (905, 440), (700, 640), (760, 820), (1250, 800)]
    for stage in range(6):
        img = muted.copy().convert("RGBA")
        for k in range(min(stage, 5)):
            mask = Image.new("L", (W, H), 0)
            ImageDraw.Draw(mask).polygon(polys[k], fill=190)
            if k == 4:
                mask = Image.fromarray(np.minimum(np.asarray(mask), np.asarray(land)))
            layer = Image.new("RGBA", (W, H), COLS[k] + (255,))
            img.paste(layer, (0, 0), mask)
        d = ImageDraw.Draw(img)
        # the old beach, always shown
        d.line(beach, fill=(30, 60, 140, 255), width=5)
        bf = font(24, bold=True)
        tx, ty = beach[len(beach) // 2]
        d.text((tx - 250, ty - 14), "the beach until 1879:", font=font(20), fill=(30, 60, 140, 255))
        d.text((tx - 250, ty + 10), "Telok Ayer Street", font=bf, fill=(30, 60, 140, 255))
        for k in range(min(stage, 5)):
            x, y = lab_pos[k]
            t = LABELS[k]
            tb = d.textbbox((0, 0), t, font=font(30, bold=True))
            d.rectangle([x - 8, y - 6, x + tb[2] + 8, y + tb[3] + 6], fill=(255, 255, 255, 225))
            d.text((x, y), t, font=font(30, bold=True), fill=COLS[k] if k < 4 else (150, 95, 0))
        # title and legend
        d.rectangle([0, 0, W, 70], fill=(255, 255, 255, 235))
        d.text((28, 16), "How Singapore's downtown shoreline moved", font=font(34, bold=True), fill=(28, 28, 26, 255))
        ly = 90
        for k in range(min(stage, 5)):
            d.rectangle([28, ly, 60, ly + 26], fill=COLS[k] + (255,))
            d.text((72, ly - 1), f"{LABELS[k]}  {NAMES[k]}", font=font(22), fill=(28, 28, 26, 255))
            ly += 38
        foot = "Approximate areas, drawn on today's map."
        fb = d.textbbox((0, 0), foot, font=font(22))
        d.rectangle([0, H - 44, fb[2] + 36, H], fill=(255, 255, 255, 225))
        d.text((18, H - 36), foot, font=font(22), fill=(70, 70, 68, 255))
        cred = "Map data (c) OpenStreetMap contributors"
        cb = d.textbbox((0, 0), cred, font=font(20))
        d.rectangle([W - cb[2] - 36, H - 44, W, H], fill=(255, 255, 255, 225))
        d.text((W - cb[2] - 18, H - 36), cred, font=font(20), fill=(70, 70, 68, 255))
        out = OUT / f"reclamation-map-{stage}.png"
        img.convert("RGB").resize((1600, round(1600 * H / W)), Image.LANCZOS).save(out, optimize=True)
        print("wrote", out)


if __name__ == "__main__":
    main()
