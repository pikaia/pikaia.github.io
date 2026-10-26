"""Timeline of Singapore's gas supply, for the gas pipelines post's video/Watch slide.

One axis (1960-2030) with the PUB years shaded, and dated events as dots
with labels staggered on four levels (two above the axis, two below) so
neighbours never overlap. The post has no HTML timeline; this script only
writes the dark-theme 1280x720 PNG:

  python scripts/render_gas_pipelines_timeline.py   # assets/images/gas-pipelines-timeline-chart.png

Dates are from the National Archives of Singapore and NLB Infopedia (PUB),
the New Straits Times (1992), the Oil & Gas Journal (West Natuna), the Prime
Minister's speech of 4 August 2003 (Grissik), the 2013 government release
(the LNG terminal), the Ministry of Energy, Trade and Industry (nuclear) and
Bloomberg (2026). Layout and drawing follow render_alsagoff_timeline.py.
"""
import sys
from pathlib import Path

from PIL import Image, ImageDraw

sys.path.insert(0, str(Path(__file__).resolve().parent))
from watch_video_lib import (  # noqa: E402
    CHART_BG, CHART_LINE, CHART_MUTED, CHART_SECONDARY, CHART_TEXT, load_font,
)

OUT = Path(__file__).resolve().parent.parent / "assets" / "images" / "gas-pipelines-timeline-chart.png"
TITLE = "Singapore's gas, 1963 to today"
SUB = "From oil-fired power stations to three pipelines, a terminal for LNG ships, and a look at nuclear"
FOOT = "Sources: National Archives of Singapore; NLB Infopedia; New Straits Times; Oil & Gas Journal; Singapore Government; METI; Bloomberg."
Y0, Y1 = 1960, 2030
TICK = 10

# (position, date label, label line 1, label line 2, level, anchor). Levels: -2, -1 above the axis, 1, 2 below.
EVENTS = [
    (1963.33, "May 1963", "The PUB takes over", "power, gas and water", -1, "start"),
    (1992.08, "Jan 1992", "Malaysian gas", "reaches Senoko", -2, "start"),
    (1995.75, "Oct 1995", "Singapore Power takes", "over power and gas", 2, "start"),
    (2001, "2001", "West Natuna gas flows;", "EMA set up", -1, "start"),
    (2003.6, "Aug 2003", "The Grissik pipeline", "opens", 1, "start"),
    (2013.35, "May 2013", "The LNG terminal", "takes its first cargo", -2, "start"),
    (2014, "2014", "A nuclear research", "programme begins", 1, "start"),
    (2026.8, "Oct 2026", "Indonesia trims", "pipeline exports", -1, "end"),
]
BANDS = [  # (from, to, label, kind)
    (1963.33, 1995.75, "The PUB runs electricity and gas, 1963-1995", "bank"),
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
