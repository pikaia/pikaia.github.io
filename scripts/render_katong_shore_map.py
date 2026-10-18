"""Render the stage-by-stage shoreline maps for the Tanjong Katong post:

  assets/images/katong-shore-map-0.png  today's map, with the places in the post marked
  assets/images/katong-shore-map-1.png  + the shoreline before reclamation began in 1966
  assets/images/katong-shore-map-2.png  + the land added by the East Coast reclamation

Each is today's OpenStreetMap map of Tanjong Katong and Marine Parade (muted).
The pre-1966 shoreline is a hand-set approximation: it follows the seaward side
of the old seafront roads (Meyer Road, Marine Parade Road and East Coast Road
east of Marine Parade Road), whose seaward plots ran down to the beach, and was
checked by eye against a 1942 map of Singapore's defences. It shows roughly
where the beach was, not a surveyed line.

"Map data (c) OpenStreetMap contributors" is burned in and belongs in the post's
Sources list. Tiles and street geometry are cached in scratch/kt/.

    python scripts/render_katong_shore_map.py
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
CACHE = ROOT / "scratch" / "kt"
OUT = ROOT / "assets" / "images"
UA = "LesserKnownSingapore-map-render/1.0 (one-off static map for a blog post)"

Z = 15
LAT_N, LAT_S = 1.3165, 1.2905
LON_W, LON_E = 103.880, 103.934
N = 2.0 ** Z
M_PER_PX = 156543.03 * math.cos(math.radians(1.3)) / N


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


def osm():
    p = CACHE / "osm.json"
    if not p.exists():
        bb = f"{LAT_S},{LON_W},{LAT_N},{LON_E}"
        q = (f'[out:json][timeout:90];(way["highway"]["name"~"^(Meyer Road|Marine Parade Road|East Coast Road|Amber Road|Fort Road)$"]({bb});'
             f'nwr["name"~"Katong Park|Chinese Swimming Club|Sea Breeze"]({bb}););out center geom;')
        req = urllib.request.Request("https://overpass.kumi.systems/api/interpreter",
                                     data=urllib.parse.urlencode({"data": q}).encode(), headers={"User-Agent": UA})
        p.write_bytes(urllib.request.urlopen(req, timeout=150).read())
    return json.loads(p.read_text(encoding="utf-8"))


def road_points(d, name, lon_min=-1e9, lon_max=1e9):
    pts = []
    for e in d["elements"]:
        if e["tags"].get("name") == name and "highway" in e["tags"]:
            pts += [px(g["lat"], g["lon"]) for g in e["geometry"] if lon_min <= g["lon"] <= lon_max]
    return pts


def centroid(d, name, key, val):
    for e in d["elements"]:
        t = e["tags"]
        if t.get("name") == name and t.get(key) == val:
            g = e.get("geometry") or []
            if g:
                return px(sum(p["lat"] for p in g) / len(g), sum(p["lon"] for p in g) / len(g))
            return px(e["lat"], e["lon"])
    raise KeyError(name)


def font(size, bold=False):
    for nm in (["arialbd.ttf"] if bold else ["arial.ttf"]) + ["DejaVuSans-Bold.ttf" if bold else "DejaVuSans.ttf"]:
        try:
            return ImageFont.truetype(nm, size)
        except OSError:
            continue
    return ImageFont.load_default()


# Marine Parade Road meets East Coast Road here; east of it, East Coast Road was the seafront road.
MPR_EAST_LON = 103.9135
SHORE_OFFSET_M = 70   # seaward plots between the road and the beach


def old_shore(d, W):
    """Southmost seafront-road point per x bin, pushed seaward by the plot depth."""
    off = SHORE_OFFSET_M / M_PER_PX
    pts = [(x, y + off) for x, y in road_points(d, "Meyer Road") + road_points(d, "Marine Parade Road")
           + road_points(d, "East Coast Road", lon_min=MPR_EAST_LON)]
    # Katong Park was laid out on the seafront in front of Meyer Road, so the beach
    # ran along its far edge, not 70 m from the road.
    for e in d["elements"]:
        if e["tags"].get("name") == "Katong Park" and e["tags"].get("leisure") == "park":
            pts += [(x, y + 3) for x, y in (px(g["lat"], g["lon"]) for g in e["geometry"])]
    a = np.array(pts)
    step = 14
    off = 0
    line = []
    for x in range(0, W + step, step):
        near = a[np.abs(a[:, 0] - x) < step]
        if len(near):
            line.append((float(x), float(near[:, 1].max() + off)))
    # light smoothing so the beach doesn't follow every kerb
    ys = np.array([p[1] for p in line])
    k = np.ones(5) / 5
    sm = np.convolve(np.pad(ys, 2, mode="edge"), k, mode="valid")
    return [(p[0], float(y)) for p, y in zip(line, sm)]


SAND = (237, 177, 68)
SHORE = (30, 60, 140)


def main():
    base = base_tile()
    W, H = base.size
    d = osm()
    arr = np.asarray(base).astype(int)
    water = (np.abs(arr[:, :, 0] - 170) < 14) & (np.abs(arr[:, :, 1] - 211) < 14) & (np.abs(arr[:, :, 2] - 223) < 14)
    land = Image.fromarray((~water * 255).astype(np.uint8))
    muted = ImageEnhance.Color(base).enhance(0.25)
    muted = Image.blend(muted, Image.new("RGB", base.size, "white"), 0.35)

    shore = old_shore(d, W)
    added = shore + [(shore[-1][0], H), (shore[0][0], H)]

    places = [
        ("Katong Park (the old fort)", centroid(d, "Katong Park", "leisure", "park"), (16, 2)),
        ("Katong Park MRT", centroid(d, "Katong Park", "railway", "station"), (-14, -44)),
        ("Chinese Swimming Club", centroid(d, "Chinese Swimming Club", "leisure", "sports_centre")
         if any(e["tags"].get("leisure") == "sports_centre" and e["tags"].get("name") == "Chinese Swimming Club" for e in d["elements"])
         else centroid(d, "Chinese Swimming Club", "name", "Chinese Swimming Club"), (14, -48)),
        ("Sea Breeze Lodge (1898)", px(1.30250, 103.90389), (14, -48)),
    ]

    titles = ["Tanjong Katong today", "The shore before 1966", "The land added from 1966"]
    for stage in range(3):
        img = muted.copy().convert("RGBA")
        dr = ImageDraw.Draw(img)
        if stage >= 2:
            mask = Image.new("L", (W, H), 0)
            ImageDraw.Draw(mask).polygon(added, fill=170)
            mask = Image.fromarray(np.minimum(np.asarray(mask), np.asarray(land)))
            img.paste(Image.new("RGBA", (W, H), SAND + (255,)), (0, 0), mask)
            dr = ImageDraw.Draw(img)
        if stage >= 1:
            dr.line(shore, fill=SHORE + (255,), width=5, joint="curve")
            lx, ly = shore[len(shore) * 2 // 3]
            t = "the beach before 1966"
            tb = dr.textbbox((0, 0), t, font=font(22, bold=True))
            dr.rectangle([lx - 8, ly + 12, lx + tb[2] + 8, ly + tb[3] + 22], fill=(255, 255, 255, 225))
            dr.text((lx, ly + 16), t, font=font(22, bold=True), fill=SHORE + (255,))
        if stage >= 2:
            t = "reclaimed 1966 onwards: East Coast Park, the ECP and new housing"
            x, y = 470, H - 120
            tb = dr.textbbox((0, 0), t, font=font(22, bold=True))
            dr.rectangle([x - 8, y - 6, x + tb[2] + 8, y + tb[3] + 6], fill=(255, 255, 255, 225))
            dr.text((x, y), t, font=font(22, bold=True), fill=(150, 95, 0, 255))
        for name, (x, y), (ox, oy) in places:
            dr.ellipse([x - 8, y - 8, x + 8, y + 8], fill=(200, 40, 40, 255), outline=(255, 255, 255, 255), width=3)
            tb = dr.textbbox((0, 0), name, font=font(20, bold=True))
            dr.rectangle([x + ox - 6, y + oy - 4, x + ox + tb[2] + 6, y + oy + tb[3] + 4], fill=(255, 255, 255, 230))
            dr.text((x + ox, y + oy), name, font=font(20, bold=True), fill=(28, 28, 26, 255))
        dr.rectangle([0, 0, W, 62], fill=(255, 255, 255, 235))
        dr.text((24, 14), titles[stage], font=font(32, bold=True), fill=(28, 28, 26, 255))
        foot = "Approximate shoreline, drawn on today's map."
        fb = dr.textbbox((0, 0), foot, font=font(20))
        dr.rectangle([0, H - 40, fb[2] + 34, H], fill=(255, 255, 255, 225))
        dr.text((16, H - 32), foot, font=font(20), fill=(70, 70, 68, 255))
        cred = "Map data (c) OpenStreetMap contributors"
        cb = dr.textbbox((0, 0), cred, font=font(18))
        dr.rectangle([W - cb[2] - 34, H - 40, W, H], fill=(255, 255, 255, 225))
        dr.text((W - cb[2] - 16, H - 32), cred, font=font(18), fill=(70, 70, 68, 255))
        out = OUT / f"katong-shore-map-{stage}.png"
        img.convert("RGB").save(out, optimize=True)
        print("wrote", out, img.size)


if __name__ == "__main__":
    main()
