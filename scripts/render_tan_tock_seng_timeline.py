"""Render the Tan Tock Seng post's relocation timeline to a static PNG for
use as a video / Watch-widget slide.

The post's chart is a single horizontal timeline - four sites the
hospital has occupied (Pearl's Hill 1844, Serangoon Road / Balestier
1861, Moulmein Road 1909, Novena 2000) with a dashed tail to "today".
compose_chart_frame() in watch_video_lib.py only animates a time-series
line, so this renders the timeline once, in the pipeline's dark chart
theme, to assets/images/tan-tock-seng-timeline.png (1280x720, drawn 2x
and downscaled for crisp text).

Re-run if the sites / years change; the output is a committed binary
(same documented exception as the route-walk OSM tiles and the other
chart PNGs).

    python scripts/render_tan_tock_seng_timeline.py
"""
import sys
from pathlib import Path

from PIL import Image, ImageDraw

sys.path.insert(0, str(Path(__file__).resolve().parent))
from watch_video_lib import (  # noqa: E402
    CHART_BG, CHART_LINE, CHART_TEXT, CHART_SECONDARY, CHART_MUTED, CHART_GRID, load_font,
)

OUT = Path(__file__).resolve().parent.parent / "assets" / "images" / "tan-tock-seng-timeline.png"
W, H = 1280, 720
SS = 2

TITLE = "One hospital, four addresses"
SUBTITLE = "Tan Tock Seng Hospital's relocations, 1844 to today"
FOOT = ("156 years and three moves on, the hospital still carries the name of the man "
        "who funded it before the colonial government would.")

YEAR_MIN, YEAR_MAX = 1836, 2026
TODAY = 2026

# (year, line 1, line 2, place above the axis?)
STOPS = [
    (1844, "Pearl's Hill", "foundation stone, 25 May 1844", True),
    (1861, "Serangoon Road", "near Balestier Plain", False),
    (1909, "Moulmein Road", "", True),
    (2000, "Novena", "current site", False),
]


def render():
    w, h = W * SS, H * SS
    img = Image.new("RGB", (w, h), CHART_BG)
    d = ImageDraw.Draw(img)

    title_font = load_font(int(36 * SS), bold=True)
    sub_font = load_font(int(20 * SS), bold=False)
    year_font = load_font(int(26 * SS), bold=True)
    place_font = load_font(int(21 * SS), bold=True)
    placesub_font = load_font(int(17 * SS), bold=False)
    tick_font = load_font(int(18 * SS), bold=False)
    foot_font = load_font(int(18 * SS), bold=False)

    margin = 70 * SS
    d.text((margin, 46 * SS), TITLE, font=title_font, fill=CHART_TEXT)
    d.text((margin, 92 * SS), SUBTITLE, font=sub_font, fill=CHART_SECONDARY)

    axis_left, axis_right = 120 * SS, 1120 * SS
    axis_y = 360 * SS
    px_per_year = (axis_right - axis_left) / (YEAR_MAX - YEAR_MIN)

    def x_of(year):
        return axis_left + (year - YEAR_MIN) * px_per_year

    # decade gridlines + tick labels
    for yr in range(1840, 2021, 20):
        gx = x_of(yr)
        d.line([(gx, axis_y - 150 * SS), (gx, axis_y + 150 * SS)], fill=CHART_GRID, width=max(1, SS))
        d.text((gx, axis_y + 168 * SS), str(yr), font=tick_font, fill=CHART_MUTED, anchor="mm")

    # the timeline: solid to the last move, dashed on to "today"
    d.line([(axis_left, axis_y), (x_of(2000), axis_y)], fill=CHART_LINE, width=max(2, 4 * SS))
    dash = 12 * SS
    x = x_of(2000)
    while x < axis_right:
        d.line([(x, axis_y), (min(x + dash, axis_right), axis_y)], fill=CHART_LINE, width=max(2, 4 * SS))
        x += dash * 2
    d.text((axis_right + 8 * SS, axis_y), "today", font=tick_font, fill=CHART_SECONDARY, anchor="lm")

    for year, l1, l2, above in STOPS:
        cx = x_of(year)
        d.ellipse([cx - 9 * SS, axis_y - 9 * SS, cx + 9 * SS, axis_y + 9 * SS],
                  fill=CHART_LINE, outline=CHART_BG, width=max(1, 3 * SS))
        if above:
            d.text((cx, axis_y - 34 * SS), str(year), font=year_font, fill=CHART_TEXT, anchor="mb")
            d.text((cx, axis_y - 74 * SS), l1, font=place_font, fill=CHART_SECONDARY, anchor="mb")
            if l2:
                d.text((cx, axis_y - 100 * SS), l2, font=placesub_font, fill=CHART_MUTED, anchor="mb")
        else:
            d.text((cx, axis_y + 34 * SS), str(year), font=year_font, fill=CHART_TEXT, anchor="mt")
            d.text((cx, axis_y + 68 * SS), l1, font=place_font, fill=CHART_SECONDARY, anchor="mt")
            if l2:
                d.text((cx, axis_y + 94 * SS), l2, font=placesub_font, fill=CHART_MUTED, anchor="mt")

    d.text((margin, (H - 44) * SS), FOOT, font=foot_font, fill=CHART_MUTED)

    img = img.resize((W, H), Image.LANCZOS)
    OUT.parent.mkdir(parents=True, exist_ok=True)
    img.save(OUT)
    print(f"wrote {OUT}  ({W}x{H})")


if __name__ == "__main__":
    render()
