"""Render the ageism-gap post's employer-hiring bar chart to a static PNG
for use as a video / Watch-widget slide.

The post's chart is a 3-category horizontal bar comparison (52% overall,
65% among employers who already have older staff, 22% among those who
don't). compose_chart_frame() in watch_video_lib.py only animates a
time-series line, so a bar chart can't be a live "chart" slide - this
renders it once, matching the post SVG's dark theme and the pipeline's
own chart colours, to assets/images/the-ageism-gap-hire-chart.png
(1280x720, drawn 2x and downscaled for crisp text).

Re-run this if the survey numbers or labels ever change; the output is a
committed binary (same documented exception as the route-walk OSM tiles
in assets/images/).

    python scripts/render_ageism_hire_chart.py
"""
import sys
from pathlib import Path

from PIL import Image, ImageDraw

sys.path.insert(0, str(Path(__file__).resolve().parent))
from watch_video_lib import (  # noqa: E402
    CHART_BG, CHART_LINE, CHART_TEXT, CHART_SECONDARY, CHART_MUTED, CHART_BASELINE,
    load_font,
)

OUT = Path(__file__).resolve().parent.parent / "assets" / "images" / "the-ageism-gap-hire-chart.png"
W, H = 1280, 720
SS = 2  # supersample

TITLE = "Employers who say they'd likely hire a worker aged 55 or older"
SOURCE = ("Source: NTUC, Singapore University of Social Sciences & Tsao Foundation, "
          "2023 employer survey")
# (label, percent)
ROWS = [
    ("All employers surveyed", 52),
    ("Already employ workers 55+", 65),
    ("No workers 55+ on staff", 22),
]
AXIS_MAX = 72  # % at the right edge of the plotting area


def render():
    w, h = W * SS, H * SS
    img = Image.new("RGB", (w, h), CHART_BG)
    d = ImageDraw.Draw(img)

    title_font = load_font(int(36 * SS), bold=True)
    label_font = load_font(int(29 * SS), bold=False)
    value_font = load_font(int(38 * SS), bold=True)
    source_font = load_font(int(21 * SS), bold=False)

    margin = 70 * SS
    d.text((margin, 54 * SS), TITLE, font=title_font, fill=CHART_TEXT)

    baseline_x = 560 * SS
    plot_right = (W - 88) * SS
    px_per_pct = (plot_right - baseline_x) / AXIS_MAX

    bar_h = 74 * SS
    row_gap = 82 * SS
    top = 210 * SS
    row_centres = [top + bar_h / 2 + i * (bar_h + row_gap) for i in range(len(ROWS))]

    d.line([(baseline_x, top - 14 * SS),
            (baseline_x, row_centres[-1] + bar_h / 2 + 14 * SS)],
           fill=CHART_BASELINE, width=max(1, SS))

    for (label, pct), cy in zip(ROWS, row_centres):
        bar_w = pct * px_per_pct
        d.rounded_rectangle(
            [baseline_x, cy - bar_h / 2, baseline_x + bar_w, cy + bar_h / 2],
            radius=8 * SS, fill=CHART_LINE,
        )
        d.text((baseline_x - 24 * SS, cy), label, font=label_font,
               fill=CHART_SECONDARY, anchor="rm")
        d.text((baseline_x + bar_w + 22 * SS, cy), f"{pct}%", font=value_font,
               fill=CHART_TEXT, anchor="lm")

    d.text((margin, (H - 46) * SS), SOURCE, font=source_font, fill=CHART_MUTED)

    img = img.resize((W, H), Image.LANCZOS)
    OUT.parent.mkdir(parents=True, exist_ok=True)
    img.save(OUT)
    print(f"wrote {OUT}  ({W}x{H})")


if __name__ == "__main__":
    render()
