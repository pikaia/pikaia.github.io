"""Render the fine-city post's rule-timeline chart to a static PNG for use
as a video / Watch-widget slide.

The post's chart is a horizontal timeline (five rules, each a bar from
its start year to where it stands today, colour-coded by outcome).
compose_chart_frame() in watch_video_lib.py only animates a time-series
line, so this renders the timeline once, in the pipeline's dark chart
theme, to assets/images/fine-city-timeline.png (1280x720, drawn 2x and
downscaled for crisp text).

Re-run this if the rules / years / statuses change; the output is a
committed binary (same documented exception as the route-walk OSM tiles
and the ageism-gap bar chart).

    python scripts/render_fine_city_timeline.py
"""
import sys
from pathlib import Path

from PIL import Image, ImageDraw

sys.path.insert(0, str(Path(__file__).resolve().parent))
from watch_video_lib import (  # noqa: E402
    CHART_BG, CHART_TEXT, CHART_SECONDARY, CHART_MUTED, CHART_GRID, load_font,
)

OUT = Path(__file__).resolve().parent.parent / "assets" / "images" / "fine-city-timeline.png"
W, H = 1280, 720
SS = 2

TITLE = "Some rules died quietly. Others are still landing fines."
SUBTITLE = "Five Singapore rules, from when each began to where it stands today"
FOOT = ("Two of the five stopped mattering years before they were formally undone. "
        "The two “boring” rules never eased at all.")

ENFORCED = (57, 135, 229)    # blue  - still enforced
EASED = (46, 160, 67)        # green - eased (brightened from the post's
                             # #008300 for contrast against the dark slide bg)
REPEALED = (213, 81, 129)    # pink  - repealed / lapsed

YEAR_MIN, YEAR_MAX = 1934, 2027
TODAY = 2026

# (label, start, end, colour, status, optional marker (year, text))
ROWS = [
    ("Gay sex ban (377A)",     1938, 2022, REPEALED, "Repealed 2022", None),
    ("Littering fines",        1968, TODAY, ENFORCED, "Still enforced", None),
    ("Flush-the-toilet rule",  1968, TODAY, ENFORCED, "Still enforced", None),
    ("Long hair ban (men)",    1970, 1990, REPEALED, "Gone by ~1990", None),
    ("Chewing gum ban",        1992, TODAY, EASED,    "Sale still banned", (2004, "Eased 2004")),
]


def render():
    w, h = W * SS, H * SS
    img = Image.new("RGB", (w, h), CHART_BG)
    d = ImageDraw.Draw(img)

    title_font = load_font(int(34 * SS), bold=True)
    sub_font = load_font(int(20 * SS), bold=False)
    legend_font = load_font(int(19 * SS), bold=False)
    row_font = load_font(int(25 * SS), bold=False)
    status_font = load_font(int(21 * SS), bold=True)
    tick_font = load_font(int(19 * SS), bold=False)
    foot_font = load_font(int(18 * SS), bold=False)

    margin = 68 * SS
    d.text((margin, 40 * SS), TITLE, font=title_font, fill=CHART_TEXT)
    d.text((margin, 82 * SS), SUBTITLE, font=sub_font, fill=CHART_SECONDARY)

    # legend
    lx, ly = margin, 128 * SS
    for colour, lab in ((ENFORCED, "Still enforced"), (EASED, "Eased"), (REPEALED, "Repealed / lapsed")):
        d.ellipse([lx, ly, lx + 15 * SS, ly + 15 * SS], fill=colour)
        d.text((lx + 22 * SS, ly + 7 * SS), lab, font=legend_font, fill=CHART_SECONDARY, anchor="lm")
        lx += (28 + len(lab) * 11) * SS

    plot_left = 372 * SS
    plot_right = 1000 * SS
    px_per_year = (plot_right - plot_left) / (YEAR_MAX - YEAR_MIN)

    def x_of(year):
        return plot_left + (year - YEAR_MIN) * px_per_year

    top = 194 * SS
    bar_h = 42 * SS
    row_gap = 48 * SS
    centres = [top + bar_h / 2 + i * (bar_h + row_gap) for i in range(len(ROWS))]

    # x gridlines + tick labels
    for yr in (1940, 1960, 1980, 2000, 2020):
        gx = x_of(yr)
        d.line([(gx, top - 18 * SS), (gx, centres[-1] + bar_h / 2 + 16 * SS)], fill=CHART_GRID, width=max(1, SS))
        d.text((gx, centres[-1] + bar_h / 2 + 34 * SS), str(yr), font=tick_font, fill=CHART_MUTED, anchor="mm")
    tx = x_of(TODAY)
    for dash_y in range(int(top - 18 * SS), int(centres[-1] + bar_h / 2 + 16 * SS), int(10 * SS)):
        d.line([(tx, dash_y), (tx, dash_y + 5 * SS)], fill=CHART_MUTED, width=max(1, SS))
    d.text((tx, top - 34 * SS), "Today", font=tick_font, fill=CHART_SECONDARY, anchor="mm")

    for (label, start, end, colour, status, marker), cy in zip(ROWS, centres):
        x0, x1 = x_of(start), x_of(end)
        d.rounded_rectangle([x0, cy - bar_h / 2, x1, cy + bar_h / 2], radius=7 * SS, fill=colour)
        d.text((plot_left - 22 * SS, cy), label, font=row_font, fill=CHART_SECONDARY, anchor="rm")
        d.text((x1 + 16 * SS, cy), status, font=status_font, fill=CHART_TEXT, anchor="lm")
        if marker:
            myr, mtext = marker
            mx = x_of(myr)
            d.ellipse([mx - 5 * SS, cy - 5 * SS, mx + 5 * SS, cy + 5 * SS],
                      fill=CHART_BG, outline=CHART_TEXT, width=max(1, SS))
            d.text((mx, cy - bar_h / 2 - 8 * SS), mtext, font=tick_font, fill=CHART_SECONDARY, anchor="mb")

    d.text((margin, (H - 44) * SS), FOOT, font=foot_font, fill=CHART_MUTED)

    img = img.resize((W, H), Image.LANCZOS)
    OUT.parent.mkdir(parents=True, exist_ok=True)
    img.save(OUT)
    print(f"wrote {OUT}  ({W}x{H})")


if __name__ == "__main__":
    render()
