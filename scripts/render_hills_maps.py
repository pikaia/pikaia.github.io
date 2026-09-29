"""Render the terrain maps for the vanished-hills post:

  assets/images/hills-island.png    - shaded relief of the whole island today,
      from real elevation data, with the downtown area boxed.
  assets/images/hills-downtown-0.png ... -3.png
      0  the 1880s: Mount Wallich, Mount Erskine and Mount Palmer drawn back in
         (reconstructed), with the shoreline of the time
      1  Mount Wallich blasted and carted away (from 1884)
      2  Mount Palmer cut down for the Telok Ayer Basin (1905-1932)
      3  today: Mount Erskine gone too; Ann Siang Hill and the Habib Noh knoll remain

Elevation: the free "Terrain Tiles" dataset on AWS (elevation-tiles-prod,
terrarium encoding), derived mainly from NASA's SRTM survey. It shows today's
terrain (c.2000), buildings and trees included, so it is smoothed here. The
vanished hills are RECONSTRUCTIONS: placed from the streets named after them
(Wallich Street, Erskine Road, Palmer and Parsi Roads) and checked against the
1893 city plan; only Mount Palmer's height (about 119 ft, Infopedia) is
documented, so the others are drawn smaller and labelled approximate.

The downtown base map reuses the reclamation map's OpenStreetMap tile.
"Map data (c) OpenStreetMap contributors" and the elevation credit are burned in.

    python scripts/render_hills_maps.py
"""
import io
import math
import time
import urllib.request
from pathlib import Path

import sys

import numpy as np
from PIL import Image, ImageDraw, ImageEnhance, ImageFont

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))
CACHE = ROOT / "scratch" / "hl"
OUT = ROOT / "assets" / "images"
TERR = "https://s3.amazonaws.com/elevation-tiles-prod/terrarium/{z}/{x}/{y}.png"


def tx(lon, n):
    return (lon + 180) / 360 * n


def ty(lat, n):
    return (1 - math.asinh(math.tan(math.radians(lat))) / math.pi) / 2 * n


def dem(z, lat_n, lat_s, lon_w, lon_e, name):
    p = CACHE / f"{name}.npy"
    if p.exists():
        return np.load(p)
    n = 2.0 ** z
    x0, x1, y0, y1 = int(tx(lon_w, n)), int(tx(lon_e, n)), int(ty(lat_n, n)), int(ty(lat_s, n))
    img = Image.new("RGB", ((x1 - x0 + 1) * 256, (y1 - y0 + 1) * 256))
    for x in range(x0, x1 + 1):
        for y in range(y0, y1 + 1):
            b = urllib.request.urlopen(TERR.format(z=z, x=x, y=y), timeout=30).read()
            img.paste(Image.open(io.BytesIO(b)).convert("RGB"), ((x - x0) * 256, (y - y0) * 256))
            time.sleep(0.05)
    L, R = (tx(lon_w, n) - x0) * 256, (tx(lon_e, n) - x0) * 256
    T, B = (ty(lat_n, n) - y0) * 256, (ty(lat_s, n) - y0) * 256
    img = img.crop((int(L), int(T), int(R), int(B)))
    a = np.asarray(img).astype(float)
    h = a[:, :, 0] * 256 + a[:, :, 1] + a[:, :, 2] / 256 - 32768
    CACHE.mkdir(parents=True, exist_ok=True)
    np.save(p, h)
    return h


def blur(h, r):
    """Separable Gaussian blur (sigma r px), edge-padded."""
    k = int(3 * r) + 1
    x = np.arange(-k, k + 1)
    g = np.exp(-x ** 2 / (2 * r * r))
    g /= g.sum()
    a = np.pad(h.astype(float), k, mode="edge")
    a = np.apply_along_axis(lambda v: np.convolve(v, g, "valid"), 0, a)
    return np.apply_along_axis(lambda v: np.convolve(v, g, "valid"), 1, a)


def hillshade(h, m_per_px, az=315, alt=40, exag=2.5):
    gy, gx = np.gradient(h * exag, m_per_px)
    slope = np.arctan(np.hypot(gx, gy))
    aspect = np.arctan2(-gx, gy)
    a, e = math.radians(az), math.radians(alt)
    return np.clip(np.sin(e) * np.cos(slope) + np.cos(e) * np.sin(slope) * np.cos(a - aspect), 0, 1)


# hypsometric ramp: metres -> colour (low green-cream to high brown)
RAMP = [(0, (214, 226, 196)), (15, (226, 230, 190)), (40, (232, 214, 160)), (80, (214, 176, 120)),
        (120, (182, 136, 92)), (170, (140, 100, 70))]


def tint(h):
    xs = [r[0] for r in RAMP]
    out = np.zeros(h.shape + (3,))
    for c in range(3):
        out[..., c] = np.interp(h, xs, [r[1][c] for r in RAMP])
    return out


def font(size, bold=False):
    for nm in (["arialbd.ttf"] if bold else ["arial.ttf"]) + ["DejaVuSans-Bold.ttf" if bold else "DejaVuSans.ttf"]:
        try:
            return ImageFont.truetype(nm, size)
        except OSError:
            continue
    return ImageFont.load_default()


def tag(d, x, y, text, f, col=(28, 28, 26), anchor="la"):
    tb = d.textbbox((x, y), text, font=f, anchor=anchor)
    d.rectangle([tb[0] - 6, tb[1] - 4, tb[2] + 6, tb[3] + 4], fill=(255, 255, 255, 225))
    d.text((x, y), text, font=f, fill=col, anchor=anchor)


SEA = np.array([176, 206, 224])
DOWN = (1.2935, 1.2665, 103.834, 103.872)  # the reclamation map's bbox


def island():
    lat_n, lat_s, lon_w, lon_e = 1.475, 1.21, 103.60, 104.05
    z = 12
    h = dem(z, lat_n, lat_s, lon_w, lon_e, "dem_island_z12")
    m = 156543.03 * math.cos(math.radians(1.35)) / 2 ** z
    land = blur((h > 1).astype(float), 1.2) > 0.5
    hs = blur(h, 2.2)
    shade = hillshade(hs, m, exag=3.0)
    rgb = tint(np.clip(hs, 0, 200)) * (0.62 + 0.38 * shade[..., None])
    rgb[~land] = SEA
    img = Image.fromarray(rgb.astype(np.uint8)).resize((h.shape[1] * 2, h.shape[0] * 2), Image.LANCZOS).convert("RGBA")
    W, H = img.size
    n = 2.0 ** z
    ox, oy = tx(lon_w, n) * 256, ty(lat_n, n) * 256

    def P(lat, lon):
        return ((tx(lon, n) * 256 - ox) * 2, (ty(lat, n) * 256 - oy) * 2)
    d = ImageDraw.Draw(img, "RGBA")
    x0, y0 = P(DOWN[0], DOWN[2])
    x1, y1 = P(DOWN[1], DOWN[3])
    d.rectangle([x0, y0, x1, y1], outline=(180, 40, 30, 255), width=5)
    f, fb = font(26), font(28, bold=True)
    tag(d, x1 + 12, y1 - 8, "the city centre (next map)", f, (150, 30, 20))
    for name, lat, lon, dx, dy in [("Bukit Timah Hill, 164 m", 1.3546, 103.7764, 30, -70),
                                   ("Mount Faber, about 105 m", 1.2736, 103.8190, -330, 50),
                                   ("Fort Canning Hill", 1.2946, 103.8455, -120, -90)]:
        px, py = P(lat, lon)
        tb = d.textbbox((px + dx, py + dy), name, font=f)
        ex = tb[0] - 6 if tb[0] > px else (tb[2] + 6 if tb[2] < px else px)
        ey = tb[3] + 4 if tb[3] < py else (tb[1] - 4 if tb[1] > py else py)
        d.line([(px, py), (ex, ey)], fill=(40, 40, 40, 200), width=2)
        d.ellipse([px - 8, py - 8, px + 8, py + 8], fill=(255, 255, 255, 255), outline=(40, 40, 40, 255), width=3)
        tag(d, px + dx, py + dy, name, f)
    d.rectangle([0, 0, W, 80], fill=(255, 255, 255, 235))
    d.text((30, 18), "Singapore's hills today", font=font(40, bold=True), fill=(28, 28, 26))
    tag(d, 24, H - 50, "Shaded relief, heights exaggerated for effect; browner is higher. Coastline c. 2000.", font(22), (70, 70, 68))
    cred = "Elevation: Terrain Tiles (AWS), from NASA SRTM"
    tb = d.textbbox((0, 0), cred, font=font(20))
    tag(d, W - tb[2] - 30, H - 48, cred, font(20), (70, 70, 68))
    img.convert("RGB").save(OUT / "hills-island.png", optimize=True)
    print("wrote hills-island.png", img.size, "max elev", round(float(h.max())))
    del fb


# Reconstructed hills in the downtown base's pixel space (z16 OSM tile, 1771x1259):
# (name, x, y, radius px, height m, label offset)
HILLS = [
    ("Mount Wallich", 535, 765, 58, 25, (-330, -20)),
    ("Mount Erskine", 530, 625, 55, 20, (-330, -30)),
    ("Mount Palmer", 585, 905, 85, 36, (-360, 60)),
]
ANN_SIANG = ("Ann Siang Hill", 580, 590, 26)
STAGES = [
    ("The 1880s: three hills on the waterfront", [0, 1, 2]),
    ("Mount Wallich blasted away, from 1884", [1, 2]),
    ("Mount Palmer cut down, 1905-1932", [1]),
    ("Today", []),
]
CROP = (140, 340, 1090, 1050)  # x0, y0, x1, y1 in the base tile
STREETS = {"Wallich Street": (551, 750), "Erskine Road": (521, 584), "Palmer Road": (561, 934)}


def downtown():
    lat_n, lat_s, lon_w, lon_e = DOWN
    base = Image.open(ROOT / "scratch" / "rc" / "base_raw.png").convert("RGB")
    W, H = base.size
    # No elevation data here: it is a surface model, and the CBD's towers read as
    # false "hills". Only the reconstructed hills (and Ann Siang Hill) get relief.
    m = 2.387
    yy, xx = np.mgrid[0:H, 0:W]
    muted = ImageEnhance.Color(base).enhance(0.18)
    muted = np.asarray(Image.blend(muted, Image.new("RGB", base.size, "white"), 0.25)).astype(float)
    arr = np.asarray(base).astype(int)
    water = (np.abs(arr[:, :, 0] - 170) < 14) & (np.abs(arr[:, :, 1] - 211) < 14) & (np.abs(arr[:, :, 2] - 223) < 14)
    # Coastline of each stage, from the reclamation map's hand-set areas:
    # the 1880s stages show the sea up to the pre-1879 shore, 1932 up to the basin.
    import render_reclamation_map as rc
    polys, _, _ = rc.polygons(rc.streets())

    def mask(ps):
        mk = Image.new("L", (W, H), 0)
        dd = ImageDraw.Draw(mk)
        for pp in ps:
            dd.polygon(pp, fill=255)
        return np.asarray(mk) > 0
    sea_by_stage = [mask(polys[2:]), mask(polys[2:]), mask(polys[4:]), np.zeros((H, W), bool)]
    for k, (title, keep) in enumerate(STAGES):
        hh = np.zeros((H, W))
        for i in keep:
            _, cx, cy, r, ht, _ = HILLS[i]
            hh = hh + ht * np.exp(-(((xx - cx) ** 2 + (yy - cy) ** 2) / (2 * (r / 1.6) ** 2)))
        _, ax, ay, ar = ANN_SIANG
        hh = hh + 12 * np.exp(-(((xx - ax) ** 2 + (yy - ay) ** 2) / (2 * (ar / 1.4) ** 2)))
        shade = hillshade(hh, m, exag=9.0)
        relief = np.clip(hh / 14, 0, 1)[..., None]
        col = tint(np.clip(hh, 0, 60) * 2.2)
        rgb = muted * (1 - 0.92 * relief) + col * (0.92 * relief)
        rgb = rgb * (0.5 + 0.5 * shade[..., None])
        sea = (water | sea_by_stage[k]) & (hh < 8)
        rgb[sea] = muted[sea] * 0.35 + SEA * 0.65
        img = Image.fromarray(np.clip(rgb, 0, 255).astype(np.uint8)).convert("RGBA")
        d = ImageDraw.Draw(img, "RGBA")
        f, fb, fs = font(22), font(24, bold=True), font(19)
        for i in keep:
            name, cx, cy, r, ht, (dx, dy) = HILLS[i]
            for rr in (r * 0.45, r * 0.8, r * 1.1):
                d.ellipse([cx - rr, cy - rr, cx + rr, cy + rr], outline=(120, 70, 30, 170), width=2)
            label = name + (", about 36 m (119 ft)" if name == "Mount Palmer" else " (approximate)")
            tag(d, cx + dx, cy + dy, label, fb if name == "Mount Palmer" else f, (110, 55, 15))
        if k == 3:
            _, ax, ay, ar = ANN_SIANG
            tag(d, ax + 30, ay - 40, "Ann Siang Hill (still there)", f, (40, 90, 40))
            tag(d, 600, 955, "Keramat Habib Noh, on the last knoll of Mount Palmer", fs, (40, 90, 40))
        for st, (sx, sy) in STREETS.items():
            d.ellipse([sx - 6, sy - 6, sx + 6, sy + 6], fill=(30, 60, 140, 255))
            tag(d, sx + 14, sy - 12, st, fs, (30, 60, 140))
        # crop to the waterfront hills so the labels read at page width
        img = img.crop(CROP)
        img = img.resize((round(img.width * 1.45), round(img.height * 1.45)), Image.LANCZOS)
        cw, ch = img.size
        d = ImageDraw.Draw(img, "RGBA")
        d.rectangle([0, 0, cw, 62], fill=(255, 255, 255, 235))
        d.text((24, 14), title, font=font(32, bold=True), fill=(28, 28, 26))
        fsm = font(20)
        tag(d, 16, ch - 36, "Old hills and coastlines reconstructed and approximate.", fsm, (70, 70, 68))
        cred = "Map data (c) OpenStreetMap contributors"
        tb = d.textbbox((0, 0), cred, font=fsm)
        tag(d, cw - tb[2] - 22, ch - 36, cred, fsm, (70, 70, 68))
        img.convert("RGB").save(OUT / f"hills-downtown-{k}.png", optimize=True)
        print("wrote", f"hills-downtown-{k}.png")


if __name__ == "__main__":
    island()
    downtown()
