"""Render the stage-by-stage fort maps for the forts post:

  assets/images/fort-map-0.png ... fort-map-3.png

Each is today's OpenStreetMap map of the southern waterfront (muted), with the
forts that stood at that stage marked; forts already removed by then are shown
hollow and grey:

  0  1820s-1850s: Fort Fullerton at the river mouth, Fort Palmer at Tanjong Pagar
  1  1859-1877: + Fort Canning on Government Hill; Fort Fullerton gone by 1873
  2  1878-1905: + Fort Pasir Panjang (Labrador), Fort Siloso and Fort Serapong
     guarding New Harbour; Fort Palmer rearmed with 10-inch guns in 1891
  3  after 1907: Fort Palmer (1905) and Fort Canning (1907) removed; what
     still stands today

Positions are today's sites (the Fullerton Hotel, Palmer Road, the Fort
Canning gate, Labrador Nature Reserve, Fort Siloso, the Fort Serapong ruins)
from OpenStreetMap, so the coastline is today's, much of it reclaimed since.

"Map data (c) OpenStreetMap contributors" is burned in and belongs in the post's
Sources list. Tiles are cached in scratch/fm/ after the first run.

    python scripts/render_fort_map.py
"""
import io
import math
import time
import urllib.request
from pathlib import Path

from PIL import Image, ImageDraw, ImageEnhance, ImageFont

ROOT = Path(__file__).resolve().parent.parent
CACHE = ROOT / "scratch" / "fm"
OUT = ROOT / "assets" / "images"
UA = "LesserKnownSingapore-map-render/1.0 (one-off static map for a blog post)"

Z = 15
LAT_N, LAT_S = 1.3015, 1.2435
LON_W, LON_E = 103.789, 103.874
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


# name, built, removed (None = still there), (lat, lon), label offset (dx, dy), label anchor
FORTS = [
    ("Fort Fullerton", "c. 1829", 1873, (1.2862, 103.8531), (22, -4), "lm"),
    ("Fort Palmer", "1850s", 1905, (1.2738, 103.8456), (22, 6), "lm"),
    ("Fort Canning", "1859", 1907, (1.2950, 103.8459), (-22, -4), "rm"),
    ("Fort Pasir Panjang (Labrador)", "1878", None, (1.2660, 103.8024), (0, -30), "ms"),
    ("Fort Siloso", "1878", None, (1.2588, 103.8088), (22, 8), "lm"),
    ("Fort Serapong", "1878-1880s", None, (1.2501, 103.8334), (22, 4), "lm"),
]
# which stage each fort first appears in
FIRST = {"Fort Fullerton": 0, "Fort Palmer": 0, "Fort Canning": 1,
         "Fort Pasir Panjang (Labrador)": 2, "Fort Siloso": 2, "Fort Serapong": 2}
STAGE_END = [1858, 1877, 1904, 2100]  # Palmer (removed 1905) still stands in stage 2
TITLES = ["The forts, 1820s to 1850s", "The forts, 1859 to 1877", "The forts, 1878 to 1905",
          "The forts after 1907, and what is left"]
ACTIVE = (176, 38, 30)      # red: standing at this stage
GONE = (150, 148, 142)      # grey: removed by this stage
TODAY = (24, 112, 60)       # green: still there today (last stage)
NOTE = {2: {"Fort Palmer": "10-inch guns, 1891"},
        3: {"Fort Canning": "gate and walls survive", "Fort Pasir Panjang (Labrador)": "ruins, Labrador Park",
            "Fort Siloso": "museum"}}


def main():
    base = base_tile()
    W, H = base.size
    muted = ImageEnhance.Color(base).enhance(0.3)
    muted = Image.blend(muted, Image.new("RGB", base.size, "white"), 0.35)
    for stage in range(4):
        img = muted.copy().convert("RGBA")
        d = ImageDraw.Draw(img)
        for name, built, removed, (lat, lon), (dx, dy), anchor in FORTS:
            if FIRST[name] > stage:
                continue
            x, y = px(lat, lon)
            gone = removed is not None and removed <= STAGE_END[stage]
            col = GONE if gone else (TODAY if stage == 3 else ACTIVE)
            r = 13
            if gone:
                d.ellipse([x - r, y - r, x + r, y + r], fill=(255, 255, 255, 230), outline=col + (255,), width=4)
                d.line([x - 7, y - 7, x + 7, y + 7], fill=col + (255,), width=4)
                d.line([x - 7, y + 7, x + 7, y - 7], fill=col + (255,), width=4)
            else:
                d.ellipse([x - r, y - r, x + r, y + r], fill=col + (255,), outline=(255, 255, 255, 255), width=3)
            note = NOTE.get(stage, {}).get(name)
            if gone:
                sub = f"{built}, removed {removed}"
            else:
                sub = f"from {built}" + (f"; {note}" if note else "")
            if stage == 3 and gone and name == "Fort Canning":
                sub += "; gate and walls survive"  # the one removed fort with visible remains
            f1, f2 = font(26, bold=True), font(21)
            lx, ly = x + dx, y + dy
            if anchor == "ms":
                tb1 = d.textbbox((lx, ly - 26), name, font=f1, anchor="ms")
                tb2 = d.textbbox((lx, ly), sub, font=f2, anchor="ms")
                pos1, pos2, a1, a2 = (lx, ly - 26), (lx, ly), "ms", "ms"
            else:
                a1 = a2 = "ls" if anchor[0] == "l" else "rs"
                pos1, pos2 = (lx, ly - 2), (lx, ly + 24)
                tb1 = d.textbbox(pos1, name, font=f1, anchor=a1)
                tb2 = d.textbbox(pos2, sub, font=f2, anchor=a2)
            bx0, by0 = min(tb1[0], tb2[0]) - 8, tb1[1] - 6
            bx1, by1 = max(tb1[2], tb2[2]) + 8, tb2[3] + 6
            d.rounded_rectangle([bx0, by0, bx1, by1], radius=6, fill=(255, 255, 255, 225))
            d.text(pos1, name, font=f1, fill=(GONE if gone else (28, 28, 26)) + (255,), anchor=a1)
            d.text(pos2, sub, font=f2, fill=(110, 108, 102, 255) if gone else (70, 70, 68, 255), anchor=a2)
        # title and legend
        d.rectangle([0, 0, W, 70], fill=(255, 255, 255, 235))
        d.text((28, 16), TITLES[stage], font=font(34, bold=True), fill=(28, 28, 26, 255))
        ly = 92
        legend = [(TODAY if stage == 3 else ACTIVE, "still there today" if stage == 3 else "standing", False)]
        if any(r is not None and r <= STAGE_END[stage] and FIRST[n] <= stage for n, _, r, *_ in FORTS):
            legend.append((GONE, "removed", True))
        for col, lab, hollow in legend:
            cx, cy = 44, ly + 13
            if hollow:
                d.ellipse([cx - 12, cy - 12, cx + 12, cy + 12], fill=(255, 255, 255, 255), outline=col + (255,), width=4)
                d.line([cx - 6, cy - 6, cx + 6, cy + 6], fill=col + (255,), width=4)
                d.line([cx - 6, cy + 6, cx + 6, cy - 6], fill=col + (255,), width=4)
            else:
                d.ellipse([cx - 12, cy - 12, cx + 12, cy + 12], fill=col + (255,), outline=(255, 255, 255, 255), width=3)
            tb = d.textbbox((68, ly), lab, font=font(22))
            d.rectangle([tb[0] - 4, tb[1] - 3, tb[2] + 6, tb[3] + 4], fill=(255, 255, 255, 215))
            d.text((68, ly), lab, font=font(22), fill=(28, 28, 26, 255))
            ly += 38
        foot = "Sites marked on today's map; much of the coast shown has been reclaimed since."
        fb = d.textbbox((0, 0), foot, font=font(22))
        d.rectangle([0, H - 44, fb[2] + 36, H], fill=(255, 255, 255, 225))
        d.text((18, H - 36), foot, font=font(22), fill=(70, 70, 68, 255))
        cred = "Map data (c) OpenStreetMap contributors"
        cb = d.textbbox((0, 0), cred, font=font(20))
        d.rectangle([W - cb[2] - 36, H - 44, W, H], fill=(255, 255, 255, 225))
        d.text((W - cb[2] - 18, H - 36), cred, font=font(20), fill=(70, 70, 68, 255))
        out = OUT / f"fort-map-{stage}.png"
        img.convert("RGB").resize((1600, round(1600 * H / W)), Image.LANCZOS).save(out, optimize=True)
        print("wrote", out, img.size)


if __name__ == "__main__":
    main()
