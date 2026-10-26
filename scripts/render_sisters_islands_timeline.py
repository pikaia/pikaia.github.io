"""Timeline of the Sisters' Islands, for the Sisters' Islands post's video/Watch slide.

One axis (1870-2030) with the Sentosa Development Corporation's years in
charge of the islands shaded, and dated events as dots with labels staggered
on four levels (two above the axis, two below) so neighbours never overlap.
The post has no HTML timeline; this script only writes the dark-theme
1280x720 PNG:

  python scripts/render_sisters_islands_timeline.py   # assets/images/sisters-islands-timeline-chart.png

Dates are from the Wellcome Collection, The Straits Times of 1905 and 1975,
wildsingapore, Ng, Toh and Chou (2013), NParks and Mothership. Layout and
drawing follow render_alsagoff_timeline.py.
"""
import sys
from pathlib import Path

from PIL import Image, ImageDraw

sys.path.insert(0, str(Path(__file__).resolve().parent))
from watch_video_lib import (  # noqa: E402
    CHART_BG, CHART_LINE, CHART_MUTED, CHART_SECONDARY, CHART_TEXT, load_font,
)

OUT = Path(__file__).resolve().parent.parent / "assets" / "images" / "sisters-islands-timeline-chart.png"
TITLE = "The Sisters' Islands, 1879 to today"
SUB = "From a target range and picnic islands to Singapore's first marine park"
FOOT = "Sources: Wellcome Collection; The Straits Times, 1905 and 1975; wildsingapore; Ng, Toh and Chou (2013); NParks."
Y0, Y1 = 1870, 2030
TICK = 20

# (position, date label, label line 1, label line 2, level, anchor). Levels: -2, -1 above the axis, 1, 2 below.
EVENTS = [
    (1879.35, "1879", "A watercolour of", "\"the Sisters\"", -1, "start"),
    (1905.25, "1905", "Howitzer practice at", "targets on the islands", 1, "start"),
    (1953, "1953", "Singapore's reefs cover", "about 39.85 sq km", -2, "start"),
    (1974.5, "1974-75", "Reclamation builds", "the lagoons", 2, "start"),
    (2012, "2012", "Reef area down to", "about 13.25 sq km", 1, "end"),
    (2014.5, "Jul 2014", "Singapore's first marine", "park announced", -1, "end"),
    (2018, "2018", "Turtle hatchery on", "Small Sister's Island", 2, "end"),
    (2024.8, "Oct 2024", "Big Sister's Island", "reopens", -2, "end"),
]
BANDS = [  # (from, to, label, kind)
    (1976, 2017.2, "Looked after by the Sentosa Development Corporation, 1976-2017", "bank"),
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
