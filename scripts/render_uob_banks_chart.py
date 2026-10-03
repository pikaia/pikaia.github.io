"""Render assets/images/uob-banks-timeline-chart.png - the static PNG of the
UOB post's "banks that became part of UOB" timeline for the video/Watch
"chart" slide.

Mirrors the post's inline .om-card SVG: one bar per bank from the year it
opened to the year UOB took control of it (United Chinese Bank / UOB in
series-2, running on to today, with its 1965 rename marked). Laid out in
1280x720 frame coordinates directly, using the same year scale as the post
(1915-2030). compose_chart_frame() only animates a single calendar-year line,
so this is rendered once, near-full-frame.

    python scripts/render_uob_banks_chart.py
"""
import sys
from pathlib import Path

from PIL import Image, ImageDraw

sys.path.insert(0, str(Path(__file__).resolve().parent))
from watch_video_lib import (  # noqa: E402
    CHART_BG, CHART_LINE, CHART_MUTED, CHART_SECONDARY, CHART_TEXT, load_font,
)

OUT = Path(__file__).resolve().parent.parent / "assets" / "images" / "uob-banks-timeline-chart.png"
W, H = 1280, 720
SS = 2

SERIES_2 = (31, 166, 31)  # #1fa61f, the inline chart's dark-mode --series-2
GRID = (44, 44, 42)       # #2c2c2a, dark-mode --grid

TITLE = "The banks that became part of UOB"
SUB = "From the year each bank opened to the year UOB took control of it"
FOOT = ("Sources: UOB corporate milestones; National Library Board; Wikipedia; "
        "Remember Singapore (Lee Wah, Far Eastern, Industrial & Commercial founding years).")

# Plot area: years 1915-2030 across x = 420..1220.
X0, X1, Y0, Y1 = 1915, 2030, 420, 1220
TODAY = 2026

# (name, opened, end, colour, fate label)
ROWS = [
    ("Lee Wah Bank", 1920, 1973, CHART_LINE, "UOB, 1973"),
    ("United Chinese Bank", 1935, TODAY, SERIES_2, "renamed UOB, 1965"),
    ("Overseas Union Bank", 1949, 2001, CHART_LINE, "UOB, 2001"),
    ("Chung Khiaw Bank", 1950, 1971, CHART_LINE, "UOB, 1971"),
    ("Industrial & Commercial Bank", 1953, 1987, CHART_LINE, "UOB, 1987"),
    ("Far Eastern Bank", 1958, 1984, CHART_LINE, "UOB, 1984"),
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
    d.rectangle([margin, ly, margin + 22 * SS, ly + 12 * SS], fill=SERIES_2)
    d.text((margin + 30 * SS, ly + 6 * SS), "United Chinese Bank / UOB", font=legend_font,
           fill=CHART_SECONDARY, anchor="lm")
    lx2 = margin + 300 * SS
    d.rectangle([lx2, ly, lx2 + 22 * SS, ly + 12 * SS], fill=CHART_LINE)
    d.text((lx2 + 30 * SS, ly + 6 * SS), "Banks UOB acquired", font=legend_font,
           fill=CHART_SECONDARY, anchor="lm")

    top, bottom = 170 * SS, 590 * SS
    for yr in range(1920, 2030, 20):
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
        if colour == SERIES_2:
            mx = xy(1965)
            d.ellipse([mx - r, cy - r, mx + r, cy + r], fill=CHART_BG, outline=CHART_TEXT, width=2 * SS)
            d.text((mx, cy + bar_h / 2 + 16 * SS), fate, font=fate_font, fill=CHART_SECONDARY, anchor="mm")
        else:
            ex = xy(end)
            d.ellipse([ex - r, cy - r, ex + r, cy + r], fill=CHART_BG, outline=CHART_TEXT, width=2 * SS)
            d.text((ex + 14 * SS, cy), fate, font=fate_font, fill=CHART_SECONDARY, anchor="lm")

    d.text((margin, 680 * SS), FOOT, font=foot_font, fill=CHART_MUTED)

    img = img.resize((W, H), Image.LANCZOS)
    OUT.parent.mkdir(parents=True, exist_ok=True)
    img.save(OUT)
    print(f"wrote {OUT}  ({W}x{H})")


if __name__ == "__main__":
    render()
