"""Render the "Long Island" illustration for the shoreline post:

  assets/images/long-island-map-0.png  - the East Coast today
  assets/images/long-island-map-1.png  - with the planned Long Island drawn in

An ILLUSTRATION, not an official plan. It follows the published descriptions
of the concept announced in November 2023: three elongated tracts of reclaimed
land from Marina East to Tanah Merah (the westernmost extending Marina East, the
easternmost starting from Tanah Merah), a new reservoir between them and East
Coast Park, and a tidal gate and pumping station between each pair of tracts,
about 800 hectares in all. The tract shapes, widths and offsets are hand-set
approximations sized to roughly 800 ha; URA says the design is still being
studied. Official URA/CNA graphics are copyrighted and are not used.

"Map data (c) OpenStreetMap contributors" is burned in and belongs in the post's
Sources list. The base tile is cached in scratch/li/.

    python scripts/render_long_island_map.py
"""
import io
import math
import time
import urllib.request
from pathlib import Path

import numpy as np
from PIL import Image, ImageDraw, ImageEnhance, ImageFont

ROOT = Path(__file__).resolve().parent.parent
CACHE = ROOT / "scratch" / "li" / "base_raw.png"
OUT = ROOT / "assets" / "images"
UA = "LesserKnownSingapore-map-render/1.0 (one-off static map for a blog post)"
Z = 14
LAT_N, LAT_S = 1.330, 1.262
LON_W, LON_E = 103.855, 103.990
M_PER_PX = 156543.03 * math.cos(math.radians(1.3)) / 2 ** Z

# East Coast shoreline (pixel space of the cached base), Marina East -> Tanah Merah.
COAST = [(360, 505), (420, 452), (480, 425), (560, 392), (650, 362), (760, 327), (870, 300),
         (990, 266), (1100, 236), (1200, 206), (1300, 182), (1420, 166), (1512, 166)]
RES = 62    # reservoir width, px (seaward edge of the coast to the tracts)
WIDTH = 83  # tract width, px
# Tracts as fractions along the coastline; the ends join Marina East / Tanah Merah.
TRACTS = [(0.0, 0.30), (0.335, 0.66), (0.695, 1.0)]


def base():
    if CACHE.exists():
        return Image.open(CACHE).convert("RGB")
    n = 2.0 ** Z
    tx = lambda lon: (lon + 180) / 360 * n  # noqa: E731
    ty = lambda lat: (1 - math.asinh(math.tan(math.radians(lat))) / math.pi) / 2 * n  # noqa: E731
    x0, x1, y0, y1 = int(tx(LON_W)), int(tx(LON_E)), int(ty(LAT_N)), int(ty(LAT_S))
    img = Image.new("RGB", ((x1 - x0 + 1) * 256, (y1 - y0 + 1) * 256))
    for x in range(x0, x1 + 1):
        for y in range(y0, y1 + 1):
            req = urllib.request.Request(f"https://tile.openstreetmap.org/{Z}/{x}/{y}.png", headers={"User-Agent": UA})
            img.paste(Image.open(io.BytesIO(urllib.request.urlopen(req, timeout=30).read())).convert("RGB"),
                      ((x - x0) * 256, (y - y0) * 256))
            time.sleep(0.15)
    img = img.crop((int((tx(LON_W) - x0) * 256), int((ty(LAT_N) - y0) * 256),
                    int((tx(LON_E) - x0) * 256), int((ty(LAT_S) - y0) * 256)))
    CACHE.parent.mkdir(parents=True, exist_ok=True)
    img.save(CACHE)
    return img


def along(pts, n=400):
    """Resample the coast polyline evenly; return points and seaward unit normals."""
    p = np.array(pts, float)
    seg = np.hypot(*np.diff(p, axis=0).T)
    s = np.concatenate([[0], np.cumsum(seg)])
    t = np.linspace(0, s[-1], n)
    xy = np.column_stack([np.interp(t, s, p[:, 0]), np.interp(t, s, p[:, 1])])
    d = np.gradient(xy, axis=0)
    d /= np.hypot(d[:, 0], d[:, 1])[:, None]
    normal = np.column_stack([-d[:, 1], d[:, 0]])  # rotate +90deg: points out to sea here
    if normal[:, 1].mean() < 0:
        normal = -normal
    return xy, normal


def font(size, bold=False):
    for nm in (["arialbd.ttf"] if bold else ["arial.ttf"]) + ["DejaVuSans-Bold.ttf" if bold else "DejaVuSans.ttf"]:
        try:
            return ImageFont.truetype(nm, size)
        except OSError:
            continue
    return ImageFont.load_default()


def main():
    b = base()
    W, H = b.size
    muted = ImageEnhance.Color(b).enhance(0.3)
    muted = Image.blend(muted, Image.new("RGB", b.size, "white"), 0.3)
    xy, nrm = along(COAST)
    N = len(xy)
    tracts, area_px = [], 0.0
    for a, z in TRACTS:
        i0, i1 = int(a * (N - 1)), int(z * (N - 1))
        inner = [tuple(xy[i] + nrm[i] * (RES if 0 < i < N - 1 else 0)) for i in range(i0, i1 + 1)]
        # the two end tracts close onto the existing coast (Marina East / Tanah Merah)
        if a == 0.0:
            inner = [tuple(xy[i0])] + inner[1:]
        if z == 1.0:
            inner = inner[:-1] + [tuple(xy[i1])]
        outer = [tuple(xy[i] + nrm[i] * (RES + WIDTH)) for i in range(i0, i1 + 1)]
        poly = inner + outer[::-1]
        tracts.append(poly)
        q = np.array(poly)
        area_px += 0.5 * abs(np.dot(q[:, 0], np.roll(q[:, 1], 1)) - np.dot(q[:, 1], np.roll(q[:, 0], 1)))
    ha = area_px * M_PER_PX ** 2 / 1e4
    print(f"tract area ~{ha:.0f} ha")
    reservoir = [tuple(p) for p in xy] + [tuple(xy[i] + nrm[i] * RES) for i in range(N - 1, -1, -1)]
    gates = [tuple(xy[int(g * (N - 1))] + nrm[int(g * (N - 1))] * (RES + WIDTH / 2)) for g in (0.3175, 0.6775)]

    for stage in (0, 1):
        img = muted.copy().convert("RGBA")
        ov = Image.new("RGBA", img.size, (0, 0, 0, 0))
        d = ImageDraw.Draw(ov)
        if stage == 1:
            d.polygon(reservoir, fill=(40, 110, 190, 150))
            for poly in tracts:
                d.polygon(poly, fill=(233, 138, 43, 235), outline=(160, 80, 10, 255))
        img = Image.alpha_composite(img, ov)
        d = ImageDraw.Draw(img)
        lab = font(22, bold=True)
        small = font(19)

        def tag(x, y, text, f=lab, col=(28, 28, 26, 255)):
            tb = d.textbbox((0, 0), text, font=f)
            d.rectangle([x - 6, y - 4, x + tb[2] + 6, y + tb[3] + 4], fill=(255, 255, 255, 225))
            d.text((x, y), text, font=f, fill=col)

        tag(250, 540, "Marina East")
        tag(560, 300, "East Coast Park", f=small)
        tag(1380, 110, "Tanah Merah")
        if stage == 1:
            for gx, gy in gates:
                d.ellipse([gx - 11, gy - 11, gx + 11, gy + 11], fill=(255, 255, 255, 255), outline=(20, 60, 120, 255), width=4)
            tag(gates[0][0] - 60, gates[0][1] + 24, "tidal gate and pumping station", f=small)
            tag(gates[1][0] - 60, gates[1][1] + 24, "tidal gate and pumping station", f=small)
            tag(700, 500, "Planned \"Long Island\": three tracts, about 800 hectares", f=font(24, bold=True), col=(150, 70, 0, 255))
            tag(820, 312, "new reservoir", f=small, col=(20, 60, 120, 255))
        d.rectangle([0, 0, W, 62], fill=(255, 255, 255, 235))
        title = "The East Coast today" if stage == 0 else "\"Long Island\": the East Coast reclamation being planned"
        d.text((24, 14), title, font=font(30, bold=True), fill=(28, 28, 26, 255))
        foot = ("Illustration only. Approximate layout from published descriptions; the design is still being studied."
                if stage == 1 else "")
        if foot:
            fb = d.textbbox((0, 0), foot, font=font(18))
            d.rectangle([0, H - 40, fb[2] + 30, H], fill=(255, 255, 255, 225))
            d.text((14, H - 32), foot, font=font(18), fill=(70, 70, 68, 255))
        cred = "Map data (c) OpenStreetMap contributors"
        cb = d.textbbox((0, 0), cred, font=font(17))
        d.rectangle([W - cb[2] - 30, H - 40, W, H], fill=(255, 255, 255, 225))
        d.text((W - cb[2] - 15, H - 32), cred, font=font(17), fill=(70, 70, 68, 255))
        out = OUT / f"long-island-map-{stage}.png"
        img.convert("RGB").save(out, optimize=True)
        print("wrote", out, img.size)


if __name__ == "__main__":
    main()
