"""Render the Turf Club post's Gold Cup prize-money chart to a static PNG
for use as a video / Watch-widget slide.

The post's inline chart is a single-series time-series on a *logarithmic*
y-axis (the purse runs from $1,600 in 1924 to $1.5 million in 2003).
compose_chart_frame() in watch_video_lib.py animates a linear line only,
so this renders the same series once, in the pipeline's dark chart
theme, to assets/images/turf-club-gold-cup-prize.png (1280x720, drawn 2x
and downscaled for crisp text). Layout follows
render_posb_deposits_chart.py.

    python scripts/render_turf_club_gold_cup_chart.py
"""
import math
import sys
from pathlib import Path

from PIL import Image, ImageDraw

sys.path.insert(0, str(Path(__file__).resolve().parent))
from watch_video_lib import (  # noqa: E402
    CHART_BG, CHART_GRID, CHART_LINE, CHART_MUTED, CHART_SECONDARY, CHART_TEXT, load_font,
)

OUT = Path(__file__).resolve().parent.parent / "assets" / "images" / "turf-club-gold-cup-prize.png"
W, H = 1280, 720
SS = 2

TITLE = "A century of Gold Cup prize money"
SUBTITLE = "Singapore Gold Cup, total prize money, 1924–2024 (logarithmic scale)"
FOOT = ("Current dollars, not adjusted for inflation. Each dot is a year with a published figure; "
        "racing stopped from 1942 until November 1947.")

# (year, prize money in dollars) - the same series as the post's inline chart
DATA = [
    (1924, 1600), (1936, 5000), (1949, 14000), (1953, 17054), (1957, 35000),
    (1961, 50000), (1971, 60000), (1977, 100000), (1984, 220500), (1985, 300000),
    (1986, 330000), (1988, 400000), (1990, 500000), (1996, 650000), (1998, 750000),
    (1999, 1000000), (2003, 1500000), (2005, 1250000), (2007, 1350000), (2017, 1350000),
    (2019, 1000000), (2021, 1000000), (2024, 1380000),
]
YEAR_MIN, YEAR_MAX = 1920, 2026
LOG_MIN, LOG_MAX = 3.0, 6.5
GRID = {3: "$1K", 4: "$10K", 5: "$100K", 6: "$1M"}


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

    for yr in range(1930, 2021, 15):
        gx = x_of(yr)
        d.text((gx, plot_b + 22 * SS), str(yr), font=tick_font, fill=CHART_MUTED, anchor="mm")

    pts = [(x_of(y), y_of(v)) for y, v in DATA]
    d.line(pts, fill=CHART_LINE, width=max(2, 4 * SS), joint="curve")

    def dot(year, val, r=6):
        cx, cy = x_of(year), y_of(val)
        d.ellipse([cx - r * SS, cy - r * SS, cx + r * SS, cy + r * SS],
                  fill=CHART_LINE, outline=CHART_BG, width=max(1, 2 * SS))

    # every reported year gets a small dot, so the gaps between reports read as gaps
    for yr, val in DATA:
        dot(yr, val, 3)

    # the first Gold Cup, Farrer Park
    dot(1924, 1600, 5)
    d.text((x_of(1924) + 12 * SS, y_of(1600) + 6 * SS),
           "1924, Farrer Park: $1,600", font=anno_font, fill=CHART_SECONDARY, anchor="lm")
    # the post-war meeting
    dot(1949, 14000, 5)
    d.text((x_of(1949) + 12 * SS, y_of(14000) + 14 * SS),
           "1949: $14,000", font=anno_font, fill=CHART_SECONDARY, anchor="lm")
    # Kranji
    dot(1999, 1000000, 5)
    d.text((x_of(1999) - 12 * SS, y_of(1000000) + 22 * SS),
           "1999, Kranji: $1 million", font=anno_font, fill=CHART_SECONDARY, anchor="rm")
    # the peak
    dot(2003, 1500000, 5)
    d.text((x_of(2003) - 12 * SS, y_of(1500000) - 16 * SS),
           "2003: $1.5 million", font=anno_font, fill=CHART_SECONDARY, anchor="rm")
    # the last Gold Cup
    ex, ey = x_of(2024), y_of(1380000)
    d.line([(ex, ey), (ex, plot_b)], fill=CHART_MUTED, width=max(1, SS))
    dot(2024, 1380000, 7)
    d.text((ex - 12 * SS, ey + 40 * SS), "Last Gold Cup, 2024",
           font=anno_strong, fill=CHART_TEXT, anchor="rm")
    d.text((ex - 12 * SS, ey + 64 * SS), "$1.38 million",
           font=anno_font, fill=CHART_SECONDARY, anchor="rm")

    d.text((margin, 680 * SS), FOOT, font=foot_font, fill=CHART_MUTED)

    img = img.resize((W, H), Image.LANCZOS)
    OUT.parent.mkdir(parents=True, exist_ok=True)
    img.save(OUT)
    print(f"wrote {OUT}  ({W}x{H})")


if __name__ == "__main__":
    render()
