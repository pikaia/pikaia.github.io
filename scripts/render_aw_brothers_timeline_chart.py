"""Render assets/images/aw-brothers-timeline-chart.png - the static PNG of
the Aw-fortune timeline for the video / Watch "chart" slide.

Mirrors the post's inline .aw-timeline SVG: five parts of the empire as
horizontal bars, blue while run by the Aw family / still trading under
its own name, grey after each passed to others, with a marker and a
one-line fate at each hand-over. Dark theme matching watch_video_lib's
chart palette. compose_chart_frame() only animates a single calendar-year
line, so a Gantt like this is rendered once, near-full-frame (see
docs/production-pipeline.md and CLAUDE.md Charts).

Committed binary, same documented exception as the OSM maps / other
chart PNGs.

    python scripts/render_aw_brothers_timeline_chart.py
"""
import sys
from pathlib import Path

from PIL import Image, ImageDraw

sys.path.insert(0, str(Path(__file__).resolve().parent))
from watch_video_lib import (  # noqa: E402
    CHART_BG, CHART_GRID, CHART_LINE, CHART_MUTED, CHART_SECONDARY, CHART_TEXT, load_font,
)

OUT = Path(__file__).resolve().parent.parent / "assets" / "images" / "aw-brothers-timeline-chart.png"
W, H = 1280, 720
SS = 2

SERIES_PAST = (116, 115, 108)  # #74736c, the inline chart's --series-past

TITLE = "The Aw fortune's main parts, and what became of each"
SUB = "Blue: run by the Aw family, or still trading under its own name.  Grey: after it passed to others."
FOOT = ("Sources: Wikipedia; Singapore Chinese Cultural Centre; reporting on the Slater Walker affair. "
        "Hand-over dates approximate.")

X_MIN, X_MAX = 1905, 2030
TODAY = 2026

# label, live-span, past-span (or None), marker year (or None), fate text
ROWS = [
    ("Tiger Balm", (1908, TODAY), None, None, "still sold worldwide"),
    ("Sin Chew Jit Poh", (1929, 1983), None, 1983, "→ merged into Lianhe Zaobao"),
    ("Haw Par Villa", (1937, 1985), (1985, TODAY), 1985, "→ taken over by the state; still open"),
    ("Chung Khiaw Bank", (1950, 1972), (1972, 1999), 1972, "→ absorbed by UOB"),
    ("The listed company", (1969, 1971), (1971, TODAY), 1971, "→ Slater Walker, then the Wee family"),
]


def render():
    w, h = W * SS, H * SS
    img = Image.new("RGB", (w, h), CHART_BG)
    d = ImageDraw.Draw(img)

    title_font = load_font(int(34 * SS), bold=True)
    sub_font = load_font(int(19 * SS), bold=False)
    row_font = load_font(int(21 * SS), bold=True)
    fate_font = load_font(int(18 * SS), bold=False)
    tick_font = load_font(int(18 * SS), bold=False)
    legend_font = load_font(int(18 * SS), bold=False)
    foot_font = load_font(int(15 * SS), bold=False)

    margin = 60 * SS
    d.text((margin, 40 * SS), TITLE, font=title_font, fill=CHART_TEXT)
    d.text((margin, 86 * SS), SUB, font=sub_font, fill=CHART_SECONDARY)

    plot_l = 300 * SS
    plot_r = (W - 40) * SS
    top = 150 * SS
    row_pitch = 92 * SS
    bar_h = 34 * SS

    def x_of(year):
        return plot_l + (year - X_MIN) / (X_MAX - X_MIN) * (plot_r - plot_l)

    # vertical year gridlines + labels
    axis_y = top + len(ROWS) * row_pitch - 30 * SS
    for yr in range(1920, 2021, 20):
        gx = x_of(yr)
        d.line([(gx, top - 14 * SS), (gx, axis_y)], fill=CHART_GRID, width=max(1, SS))
        d.text((gx, axis_y + 12 * SS), str(yr), font=tick_font, fill=CHART_MUTED, anchor="mm")

    for i, (label, live, past, mark, fate) in enumerate(ROWS):
        y0 = top + i * row_pitch
        cy = y0 + bar_h / 2
        d.text((margin, cy), label, font=row_font, fill=CHART_TEXT, anchor="lm")
        if past:
            d.rounded_rectangle([x_of(past[0]), y0, x_of(past[1]), y0 + bar_h],
                                radius=6 * SS, fill=SERIES_PAST)
        d.rounded_rectangle([x_of(live[0]), y0, max(x_of(live[1]), x_of(live[0]) + 4 * SS), y0 + bar_h],
                            radius=6 * SS, fill=CHART_LINE)
        if mark:
            mx = x_of(mark)
            d.ellipse([mx - 6 * SS, cy - 6 * SS, mx + 6 * SS, cy + 6 * SS],
                      fill=CHART_BG, outline=CHART_TEXT, width=max(1, 2 * SS))
        fx = x_of(TODAY) if fate == "still sold worldwide" else x_of(mark) + 10 * SS
        anchor = "rs" if fate == "still sold worldwide" else "ls"
        d.text((fx, y0 + bar_h + 26 * SS), fate, font=fate_font, fill=CHART_SECONDARY, anchor=anchor)

    # legend
    ly = axis_y + 44 * SS
    d.rounded_rectangle([plot_l, ly - 11 * SS, plot_l + 26 * SS, ly + 3 * SS], radius=4 * SS, fill=CHART_LINE)
    d.text((plot_l + 38 * SS, ly - 4 * SS), "Aw family / still itself", font=legend_font,
           fill=CHART_SECONDARY, anchor="lm")
    x2 = plot_l + 290 * SS
    d.rounded_rectangle([x2, ly - 11 * SS, x2 + 26 * SS, ly + 3 * SS], radius=4 * SS, fill=SERIES_PAST)
    d.text((x2 + 38 * SS, ly - 4 * SS), "after it passed to others", font=legend_font,
           fill=CHART_SECONDARY, anchor="lm")

    d.text((margin, 686 * SS), FOOT, font=foot_font, fill=CHART_MUTED)

    img = img.resize((W, H), Image.LANCZOS)
    OUT.parent.mkdir(parents=True, exist_ok=True)
    img.save(OUT)
    print(f"wrote {OUT}  ({W}x{H})")


if __name__ == "__main__":
    render()
