"""Timeline of the exchange banks of Raffles Place, for the exchange banks post's video/Watch slide.

One axis (1850-2010) with the Japanese Occupation shaded, and dated events
as dots with labels staggered on four levels (two above the axis, two below)
so neighbours never overlap. The post has no HTML timeline; this script only
writes the dark-theme 1280x720 PNG:

  python scripts/render_exchange_banks_timeline.py   # assets/images/exchange-banks-timeline-chart.png

Dates are from Wikipedia, HSBC, Roots.gov.sg, The Straits Times of 1953,
1961 and 1977 and The Business Times of 1983. Layout and drawing follow
render_alsagoff_timeline.py.
"""
import sys
from pathlib import Path

from PIL import Image, ImageDraw

sys.path.insert(0, str(Path(__file__).resolve().parent))
from watch_video_lib import (  # noqa: E402
    CHART_BG, CHART_LINE, CHART_MUTED, CHART_SECONDARY, CHART_TEXT, load_font,
)

OUT = Path(__file__).resolve().parent.parent / "assets" / "images" / "exchange-banks-timeline-chart.png"
TITLE = "The exchange banks of Raffles Place, 1850s to today"
SUB = "Three British banks, their buildings on the square, and the towers that replaced them"
FOOT = "Sources: Wikipedia; HSBC; Roots.gov.sg; The Straits Times, 1953, 1961 and 1977; The Business Times, 1983."
Y0, Y1 = 1850, 2010
TICK = 20

# (position, date label, label line 1, label line 2, level, anchor). Levels: -2, -1 above the axis, 1, 2 below.
EVENTS = [
    (1855.5, "Mid-1850s", "The Mercantile Bank", "comes to Singapore", -1, "start"),
    (1859.1, "Feb 1859", "The Chartered Bank's", "first branch opens", 2, "start"),
    (1877.9, "Dec 1877", "The Hongkong and Shanghai", "Bank's own office opens", -2, "start"),
    (1894.8, "1894", "HSBC's first building", "on Collyer Quay", 1, "start"),
    (1895.1, "1895", "Chartered Bank's palazzo,", "Battery Road", -1, "start"),
    (1899, "1899", "Government currency", "notes begin", 2, "start"),
    (1916.35, "1916", "Chartered Bank's domed", "building on the square", -2, "start"),
    (1925, "Mid-1920s", "Hongkong Bank", "Chambers finished", 1, "start"),
    (1942.1, "1941-42", "Raffles Place bombed;", "British banks closed", -1, "start"),
    (1953.6, "Jul 1953", "Foundation stone of a new", "Chartered Bank building", 2, "start"),
    (1959, "1959", "HSBC buys the", "Mercantile Bank", -2, "start"),
    (1969, "1969", "Standard Chartered", "is formed", 1, "start"),
    (1983.1, "Jan 1983", "The new HSBC", "Building opens", -1, "start"),
    (1984.8, "Oct 1984", "Six Battery Road", "opens", 2, "start"),
]
BANDS = [  # (from, to, label, kind)
    (1942.1, 1945.7, "Japanese Occupation", "war"),
]


def _ticks():
    """(year, side) for every tick label. A label next to a below-axis stem is
    nudged to the far side of it (side -1/+1) instead of being dropped, which
    left gaps in the axis on the Ya'acob timeline."""
    below = [e[0] for e in EVENTS if e[4] > 0]
    out = []
    for y in range(Y0, Y1 + 1, TICK):
        near = [b for b in below if abs(y - b) <= (Y1 - Y0) * 0.016]
        out.append((y, 0 if not near else (-1 if near[0] > y else 1)))
    return out


def _layout(x0, x1):
    sx = lambda y: x0 + (y - Y0) / (Y1 - Y0) * (x1 - x0)  # noqa: E731
    return sx


def render_png():
    W, H, SS = 1280, 720, 2
    img = Image.new("RGB", (W * SS, H * SS), CHART_BG)
    d = ImageDraw.Draw(img)
    d.text((60 * SS, 40 * SS), TITLE, font=load_font(34 * SS), fill=CHART_TEXT)
    d.text((60 * SS, 84 * SS), SUB, font=load_font(19 * SS, bold=False), fill=CHART_SECONDARY)
    d.text((60 * SS, 680 * SS), FOOT, font=load_font(14 * SS, bold=False), fill=CHART_MUTED)
    sx = _layout(90, 1190)
    ax = 395
    lev = {-2: 175, -1: 270, 1: 520, 2: 615}
    colours = {"bank": (28, 52, 82), "war": (60, 72, 60)}
    for a, b, _, kind in BANDS:
        d.rectangle([sx(a) * SS, (ax - 30) * SS, sx(b) * SS, (ax + 30) * SS], fill=colours[kind])
    # Band legend, under the subtitle.
    lx, ly0 = 60, 128
    for _, _, lab, kind in BANDS:
        d.rectangle([lx * SS, (ly0 - 8) * SS, (lx + 16) * SS, (ly0 + 8) * SS], fill=colours[kind])
        d.text(((lx + 24) * SS, ly0 * SS), lab, font=load_font(15 * SS, bold=False), fill=CHART_SECONDARY, anchor="lm")
        lx += 24 + d.textlength(lab, font=load_font(15 * SS, bold=False)) / SS + 36
    d.line([(sx(Y0) * SS, ax * SS), (sx(Y1) * SS, ax * SS)], fill=CHART_MUTED, width=2 * SS)
    for y in range(Y0, Y1 + 1, TICK):
        d.line([(sx(y) * SS, (ax - 5) * SS), (sx(y) * SS, (ax + 5) * SS)], fill=CHART_MUTED, width=SS)
    for y, side in _ticks():
        d.text(((sx(y) + side * 22) * SS, (ax + 58) * SS), str(y), font=load_font(14 * SS, bold=False), fill=CHART_MUTED, anchor="mm")
    fy, fl = load_font(20 * SS), load_font(16 * SS, bold=False)
    for yr, dl, l1, l2, lv, an in EVENTS:
        x, ly = sx(yr), lev[lv]
        d.line([(x * SS, ax * SS), (x * SS, (ly + (34 if lv < 0 else -26)) * SS)], fill=CHART_MUTED, width=SS)
        d.ellipse([(x - 7) * SS, (ax - 7) * SS, (x + 7) * SS, (ax + 7) * SS], fill=CHART_BG, outline=CHART_LINE, width=3 * SS)
        anc = {"start": "l", "end": "r", "middle": "m"}[an]
        tx = x - 4 if anc == "l" else (x + 4 if anc == "r" else x)
        d.text((tx * SS, (ly - 22) * SS), dl, font=fy, fill=CHART_TEXT, anchor=anc + "m")
        d.text((tx * SS, ly * SS), l1, font=fl, fill=CHART_SECONDARY, anchor=anc + "m")
        d.text((tx * SS, (ly + 20) * SS), l2, font=fl, fill=CHART_SECONDARY, anchor=anc + "m")
    img.resize((W, H), Image.LANCZOS).save(OUT)
    print("wrote", OUT)




if __name__ == "__main__":
    render_png()
