"""Render the POSB post's deposits chart to a static PNG for use as a
video / Watch-widget slide.

The post's inline chart is a single-series time-series on a *logarithmic*
y-axis (deposits span six orders of magnitude, 1877 to 1998).
compose_chart_frame() in watch_video_lib.py animates a linear line only,
so this renders the same series once, in the pipeline's dark chart
theme, to assets/images/posb-deposits.png (1280x720, drawn 2x and
downscaled for crisp text).

Captions are no longer burned into the main video (see
docs/production-pipeline.md section 6), so the plot uses close to the
full frame - a normal ~40-60px video margin all round, plus a little
extra at the bottom (content ends ~y=680 of 720) so YouTube's own
caption overlay, when a viewer toggles it on, doesn't bury the x-axis.

Re-run if the figures change; the output is a committed binary (same
documented exception as the other chart PNGs and the OSM map tiles).

    python scripts/render_posb_deposits_chart.py
"""
import math
import sys
from pathlib import Path

from PIL import Image, ImageDraw

sys.path.insert(0, str(Path(__file__).resolve().parent))
from watch_video_lib import (  # noqa: E402
    CHART_BG, CHART_GRID, CHART_LINE, CHART_MUTED, CHART_SECONDARY, CHART_TEXT, load_font,
)

OUT = Path(__file__).resolve().parent.parent / "assets" / "images" / "posb-deposits.png"
W, H = 1280, 720
SS = 2

TITLE = "A savings habit, compounded"
SUBTITLE = "Post Office Savings Bank of Singapore — total deposits, 1877–1998 (logarithmic scale)"
FOOT = ("Deposits in current dollars; Straits, Malayan and Singapore dollars were issued at par. "
        "Series ends at the 1998 transfer to DBS Bank.")

# (year, deposits in dollars)
DATA = [
    (1877, 19865), (1940, 14_300_000), (1948, 18_632_519), (1949, 27_400_000),
    (1955, 57_600_000), (1966, 37_400_000), (1969, 57_700_000),
    (1976, 1_000_000_000), (1986, 10_000_000_000), (1998, 25_500_000_000),
]
YEAR_MIN, YEAR_MAX = 1877, 1998
LOG_MIN, LOG_MAX = 4.0, 10.5
GRID = {4: "$10K", 5: "$100K", 6: "$1M", 7: "$10M", 8: "$100M", 9: "$1B", 10: "$10B"}


def render():
    w, h = W * SS, H * SS
    img = Image.new("RGB", (w, h), CHART_BG)
    d = ImageDraw.Draw(img)

    title_font = load_font(int(36 * SS), bold=True)
    sub_font = load_font(int(20 * SS), bold=False)
    tick_font = load_font(int(18 * SS), bold=False)
    anno_font = load_font(int(19 * SS), bold=False)
    anno_strong = load_font(int(21 * SS), bold=True)
    foot_font = load_font(int(16 * SS), bold=False)

    margin = 70 * SS
    d.text((margin, 40 * SS), TITLE, font=title_font, fill=CHART_TEXT)
    d.text((margin, 84 * SS), SUBTITLE, font=sub_font, fill=CHART_SECONDARY)

    plot_l, plot_r = 150 * SS, 1150 * SS
    plot_t, plot_b = 130 * SS, 590 * SS

    def x_of(year):
        return plot_l + (year - YEAR_MIN) / (YEAR_MAX - YEAR_MIN) * (plot_r - plot_l)

    def y_of(val):
        lg = math.log10(val)
        return plot_t + (LOG_MAX - lg) / (LOG_MAX - LOG_MIN) * (plot_b - plot_t)

    for p, lab in GRID.items():
        gy = y_of(10 ** p)
        d.line([(plot_l, gy), (plot_r, gy)], fill=CHART_GRID, width=max(1, SS))
        d.text((plot_l - 14 * SS, gy), lab, font=tick_font, fill=CHART_MUTED, anchor="rm")

    for yr in range(1880, 1991, 20):
        gx = x_of(yr)
        d.text((gx, plot_b + 22 * SS), str(yr), font=tick_font, fill=CHART_MUTED, anchor="mm")

    pts = [(x_of(y), y_of(v)) for y, v in DATA]
    d.line(pts, fill=CHART_LINE, width=max(2, 4 * SS), joint="curve")

    def dot(year, val, r=6):
        cx, cy = x_of(year), y_of(val)
        d.ellipse([cx - r * SS, cy - r * SS, cx + r * SS, cy + r * SS],
                  fill=CHART_LINE, outline=CHART_BG, width=max(1, 2 * SS))

    # start
    dot(1877, 19865, 5)
    d.text((x_of(1877) + 12 * SS, y_of(19865) - 16 * SS),
           "1877: 211 depositors, $19,900", font=anno_font, fill=CHART_SECONDARY, anchor="ls")
    # the mid-century drift
    dot(1966, 37_400_000, 5)
    d.text((x_of(1966), y_of(37_400_000) + 30 * SS),
           "1957–66: a decade of drift", font=anno_font, fill=CHART_SECONDARY, anchor="mm")
    # the 1969 turn
    d.text((x_of(1969) - 12 * SS, y_of(57_700_000) - 14 * SS),
           "1969: schools campaign, tax-free interest", font=anno_font, fill=CHART_SECONDARY,
           anchor="rm")
    # end marker
    ex, ey = x_of(1998), y_of(25_500_000_000)
    d.line([(ex, ey), (ex, plot_b)], fill=CHART_MUTED, width=max(1, SS))
    dot(1998, 25_500_000_000, 7)
    d.text((ex - 12 * SS, ey - 30 * SS), "Transferred to DBS, 1998",
           font=anno_strong, fill=CHART_TEXT, anchor="rm")
    d.text((ex - 12 * SS, ey - 7 * SS), "$25.5 billion in deposits",
           font=anno_font, fill=CHART_SECONDARY, anchor="rm")

    d.text((margin, 680 * SS), FOOT, font=foot_font, fill=CHART_MUTED)

    img = img.resize((W, H), Image.LANCZOS)
    OUT.parent.mkdir(parents=True, exist_ok=True)
    img.save(OUT)
    print(f"wrote {OUT}  ({W}x{H})")


if __name__ == "__main__":
    render()
