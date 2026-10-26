"""Timeline of the Chinese sub-post office and the 1876 riot, for the Post Office riot post's video/Watch slide.

One axis (1840-1895) with dated events as dots and labels staggered on four
levels (two above the axis, two below) so neighbours never overlap. The post
has no HTML timeline; this script only writes the dark-theme 1280x720 PNG:

  python scripts/render_post_office_riot_timeline.py   # assets/images/post-office-riot-timeline-chart.png

Dates are from T. A. Melville in Makepeace et al., One Hundred Years of
Singapore (1921), vol. 2; Song Ong Siang, One Hundred Years' History of the
Chinese in Singapore (1923); the Straits Times Overland Journal of 27
December 1876; and NLB Infopedia. Layout and drawing follow
render_alsagoff_timeline.py.
"""
import sys
from pathlib import Path

from PIL import Image, ImageDraw

sys.path.insert(0, str(Path(__file__).resolve().parent))
from watch_video_lib import (  # noqa: E402
    CHART_BG, CHART_LINE, CHART_MUTED, CHART_SECONDARY, CHART_TEXT, load_font,
)

OUT = Path(__file__).resolve().parent.parent / "assets" / "images" / "post-office-riot-timeline-chart.png"
TITLE = "The Chinese sub-post office, 1847 to 1889"
SUB = "From the street letter-writers to a riot, and a post office the Chinese came to use"
FOOT = "Sources: Makepeace et al. (1921); Song Ong Siang (1923); Straits Times Overland Journal, 27 Dec 1876; NLB Infopedia."
Y0, Y1 = 1840, 1895
TICK = 10

# (position, date label, label line 1, label line 2, level, anchor). Levels: -2, -1 above the axis, 1, 2 below.
EVENTS = [
    (1847, "1847", "Letter-writers' stalls", "line the streets", -1, "start"),
    (1873, "1873", "Officials look into a", "post office for coolies", 2, "start"),
    (1876.95, "15 Dec 1876", "Sub-post office", "opens; the riot", -2, "start"),
    (1877.33, "May 1877", "Pickering becomes", "Protector of Chinese", 1, "start"),
    (1880, "1880", "About 80,000 letters", "go through the post", -1, "start"),
    (1887, "1887", "49 Chinese letter", "offices in Singapore", 1, "start"),
    (1889, "1889", "About 280,000", "letters a year", -2, "end"),
]
BANDS = []


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
