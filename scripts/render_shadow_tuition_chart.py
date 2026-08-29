"""Render the shadow-tuition post's spending chart to a static PNG for use
as a video / Watch-widget slide.

The post's chart is a 4-bar series - total household spending on private
tuition and enrichment at S$680M (2008), S$1.1B (2013), S$1.4B (2018),
and S$1.8B (2023). compose_chart_frame() only animates a time-series
line, so this renders it once, in the pipeline's dark chart theme, to
assets/images/shadow-tuition-spend.png (1280x720, drawn 2x and
downscaled for crisp text).

Re-run if the figures change; the output is a committed binary (same
documented exception as the route-walk OSM tiles and the other chart
PNGs).

    python scripts/render_shadow_tuition_chart.py
"""
import sys
from pathlib import Path

from PIL import Image, ImageDraw

sys.path.insert(0, str(Path(__file__).resolve().parent))
from watch_video_lib import (  # noqa: E402
    CHART_BG, CHART_LINE, CHART_TEXT, CHART_SECONDARY, CHART_MUTED, CHART_GRID, load_font,
)

OUT = Path(__file__).resolve().parent.parent / "assets" / "images" / "shadow-tuition-spend.png"
W, H = 1280, 720
SS = 2

TITLE = "A $680M industry became a $1.8B one"
SUBTITLE = "Total household spending on private tuition and enrichment, Singapore"
FOOT = ("More than doubled in 15 years, outpacing the economy around it. "
        "Source: Singapore's Household Expenditure Survey.")

# (year label, value in S$ billions, value label)
BARS = [
    ("2008", 0.68, "$680M"),
    ("2013", 1.1, "$1.1B"),
    ("2018", 1.4, "$1.4B"),
    ("2023", 1.8, "$1.8B"),
]
Y_MAX, Y_STEP = 2.0, 0.5


def render():
    w, h = W * SS, H * SS
    img = Image.new("RGB", (w, h), CHART_BG)
    d = ImageDraw.Draw(img)

    title_font = load_font(int(36 * SS), bold=True)
    sub_font = load_font(int(20 * SS), bold=False)
    tick_font = load_font(int(19 * SS), bold=False)
    cat_font = load_font(int(23 * SS), bold=True)
    val_font = load_font(int(30 * SS), bold=True)
    foot_font = load_font(int(18 * SS), bold=False)

    margin = 70 * SS
    d.text((margin, 44 * SS), TITLE, font=title_font, fill=CHART_TEXT)
    d.text((margin, 90 * SS), SUBTITLE, font=sub_font, fill=CHART_SECONDARY)

    left, right = 170 * SS, 1150 * SS
    top, bot = 180 * SS, 570 * SS

    def sy(v):
        return bot - v / Y_MAX * (bot - top)

    v = 0.0
    while v <= Y_MAX + 1e-9:
        y = sy(v)
        d.line([(left, y), (right, y)], fill=CHART_GRID, width=max(1, SS))
        label = "$0" if v == 0 else f"${v:g}B"
        d.text((left - 16 * SS, y), label, font=tick_font, fill=CHART_MUTED, anchor="rm")
        v += Y_STEP

    slot = (right - left) / len(BARS)
    bar_w = 110 * SS
    for i, (year, val, vlabel) in enumerate(BARS):
        cx = left + slot * (i + 0.5)
        y = sy(val)
        d.rounded_rectangle([cx - bar_w / 2, y, cx + bar_w / 2, bot], radius=8 * SS, fill=CHART_LINE)
        d.text((cx, y - 14 * SS), vlabel, font=val_font, fill=CHART_TEXT, anchor="mb")
        d.text((cx, bot + 22 * SS), year, font=cat_font, fill=CHART_SECONDARY, anchor="mt")

    d.text((margin, (H - 44) * SS), FOOT, font=foot_font, fill=CHART_MUTED)

    img = img.resize((W, H), Image.LANCZOS)
    OUT.parent.mkdir(parents=True, exist_ok=True)
    img.save(OUT)
    print(f"wrote {OUT}  ({W}x{H})")


if __name__ == "__main__":
    render()
