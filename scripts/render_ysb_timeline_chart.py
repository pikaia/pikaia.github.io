"""Render assets/images/yokohama-specie-bank-timeline-chart.png - the static PNG
of the Yokohama Specie Bank post's timeline of its Singapore offices, for the
video/Watch "chart" slide.

Mirrors the post's inline .ys-card SVG: one bar per Singapore office, from
when the bank moved in to when it left (Yokohama Specie Bank in series-1, its
successor the Bank of Tokyo in series-2). Laid out in 1280x720 frame
coordinates directly, on the post's year scale (1910-1960). compose_chart_frame() only animates a single calendar-year line,
so this is rendered once, near-full-frame.

    python scripts/render_ysb_timeline_chart.py
"""
import sys
from pathlib import Path

from PIL import Image, ImageDraw

sys.path.insert(0, str(Path(__file__).resolve().parent))
from watch_video_lib import (  # noqa: E402
    CHART_BG, CHART_LINE, CHART_MUTED, CHART_SECONDARY, CHART_TEXT, load_font,
)

OUT = Path(__file__).resolve().parent.parent / "assets" / "images" / "yokohama-specie-bank-timeline-chart.png"
W, H = 1280, 720
SS = 2

SERIES_2 = (31, 166, 31)  # #1fa61f, the inline chart's dark-mode --series-2
GRID = (44, 44, 42)       # #2c2c2a, dark-mode --grid

TITLE = "Where the bank was in Singapore, 1916 to 1957"
SUB = "The Yokohama Specie Bank's Singapore office in each period, and its successor's return"
FOOT = ("Sources: The Straits Times, 1916 and 1957; Singapore Free Press, 1933; "
        "The Syonan Shimbun, 1942 and 1943.")

# Plot area: years 1910-1960 across x = 470..1220.
X0, X1, Y0, Y1 = 1910, 1960, 470, 1220

# (office, from, to, colour, label)
ROWS = [
    ("Bonham Building", 1916.68, 1933.25, CHART_LINE, "1916-1933"),
    ("Meyer Chambers", 1933.25, 1941.93, CHART_LINE, "1933-1941"),
    ("21 Collyer Quay (Occupation)", 1942.21, 1945.67, CHART_LINE, "1942-1945"),
    ("Bank of Tokyo, Phillip Street", 1957.05, 1960, SERIES_2, "from 1957"),
]


def xy(year):
    return (Y0 + (year - X0) * (Y1 - Y0) / (X1 - X0)) * SS


def render():
    img = Image.new("RGB", (W * SS, H * SS), CHART_BG)
    d = ImageDraw.Draw(img)

    title_font = load_font(int(34 * SS))
    sub_font = load_font(int(19 * SS), bold=False)
    legend_font = load_font(int(17 * SS), bold=False)
    row_font = load_font(int(19 * SS))
    fate_font = load_font(int(16 * SS), bold=False)
    axis_font = load_font(int(16 * SS), bold=False)
    foot_font = load_font(int(14 * SS), bold=False)

    margin = 60 * SS
    d.text((margin, 40 * SS), TITLE, font=title_font, fill=CHART_TEXT)
    d.text((margin, 84 * SS), SUB, font=sub_font, fill=CHART_SECONDARY)

    ly = 124 * SS
    for lx, colour, label in [(margin, CHART_LINE, "Yokohama Specie Bank"), (margin + 300 * SS, SERIES_2, "Bank of Tokyo")]:
        d.rectangle([lx, ly, lx + 22 * SS, ly + 12 * SS], fill=colour)
        d.text((lx + 30 * SS, ly + 6 * SS), label, font=legend_font, fill=CHART_SECONDARY, anchor="lm")

    top, bottom = 170 * SS, 590 * SS
    for yr in range(1910, 1961, 10):
        x = xy(yr)
        d.line([(x, top), (x, bottom)], fill=GRID, width=max(1, SS))
        d.text((x, 612 * SS), str(yr), font=axis_font, fill=CHART_MUTED, anchor="mm")

    row_h = (bottom - top) / len(ROWS)
    bar_h = 22 * SS
    r = 6 * SS
    for i, (name, opened, end, colour, fate) in enumerate(ROWS):
        cy = top + row_h * (i + 0.5)
        d.text((Y0 * SS - 20 * SS, cy), name, font=row_font, fill=CHART_TEXT, anchor="rm")
        d.rounded_rectangle([xy(opened), cy - bar_h / 2, xy(end), cy + bar_h / 2], radius=r, fill=colour)
        if colour == SERIES_2:  # runs to the chart's edge: label to its left
            d.text((xy(opened) - 14 * SS, cy), fate, font=fate_font, fill=CHART_SECONDARY, anchor="rm")
        else:
            d.text((xy(end) + 14 * SS, cy), fate, font=fate_font, fill=CHART_SECONDARY, anchor="lm")

    d.text((margin, 680 * SS), FOOT, font=foot_font, fill=CHART_MUTED)

    img = img.resize((W, H), Image.LANCZOS)
    OUT.parent.mkdir(parents=True, exist_ok=True)
    img.save(OUT)
    print(f"wrote {OUT}  ({W}x{H})")


if __name__ == "__main__":
    render()
