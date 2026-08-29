"""Render the Christmas Island post's payout chart to a static PNG for use
as a video / Watch-widget slide.

The post's chart is a 2-bar comparison - the ~M$48 million of phosphate
income Singapore signed away (32 remaining lease years at ~M$1.5M/yr) vs
the ~M$20 million lump sum it actually received in 1958.
compose_chart_frame() only animates a time-series line, so this renders
it once, in the pipeline's dark chart theme, to
assets/images/christmas-island-payout.png (1280x720, drawn 2x and
downscaled for crisp text).

Re-run if the figures change; the output is a committed binary (same
documented exception as the route-walk OSM tiles and the other chart
PNGs).

    python scripts/render_christmas_island_payout_chart.py
"""
import sys
from pathlib import Path

from PIL import Image, ImageDraw

sys.path.insert(0, str(Path(__file__).resolve().parent))
from watch_video_lib import (  # noqa: E402
    CHART_BG, CHART_LINE, CHART_TEXT, CHART_SECONDARY, CHART_MUTED, CHART_GRID, load_font,
)

OUT = Path(__file__).resolve().parent.parent / "assets" / "images" / "christmas-island-payout.png"
W, H = 1280, 720
SS = 2

TITLE = "M$20 million in, roughly M$48 million left on the table"
SUBTITLE = ("What Singapore received for Christmas Island's phosphate income "
            "vs. what the remaining lease was worth")
FOOT = ("Compensation for lost phosphate income, not a sale price — and still under half of "
        "what that income was projected to be worth.")

# (line 1, line 2, value in M$ millions, value label)
BARS = [
    ("Foregone", "32 remaining lease years", 48, "M$48M"),
    ("Received", "lump sum, 1958", 20, "M$20M"),
]
Y_MAX, Y_STEP = 50, 12.5


def render():
    w, h = W * SS, H * SS
    img = Image.new("RGB", (w, h), CHART_BG)
    d = ImageDraw.Draw(img)

    title_font = load_font(int(33 * SS), bold=True)
    sub_font = load_font(int(19 * SS), bold=False)
    tick_font = load_font(int(19 * SS), bold=False)
    cat_font = load_font(int(24 * SS), bold=True)
    catsub_font = load_font(int(18 * SS), bold=False)
    val_font = load_font(int(34 * SS), bold=True)
    foot_font = load_font(int(18 * SS), bold=False)

    margin = 70 * SS
    d.text((margin, 42 * SS), TITLE, font=title_font, fill=CHART_TEXT)
    d.text((margin, 86 * SS), SUBTITLE, font=sub_font, fill=CHART_SECONDARY)

    left, right = 200 * SS, 1160 * SS
    top, bot = 170 * SS, 560 * SS

    def sy(v):
        return bot - v / Y_MAX * (bot - top)

    v = 0
    while v <= Y_MAX:
        y = sy(v)
        d.line([(left, y), (right, y)], fill=CHART_GRID, width=max(1, SS))
        d.text((left - 16 * SS, y), f"M${v:g}M", font=tick_font, fill=CHART_MUTED, anchor="rm")
        v += Y_STEP

    slot = (right - left) / len(BARS)
    bar_w = 150 * SS
    for i, (l1, l2, val, vlabel) in enumerate(BARS):
        cx = left + slot * (i + 0.5)
        y = sy(val)
        d.rounded_rectangle([cx - bar_w / 2, y, cx + bar_w / 2, bot], radius=8 * SS, fill=CHART_LINE)
        d.text((cx, y - 16 * SS), vlabel, font=val_font, fill=CHART_TEXT, anchor="mb")
        d.text((cx, bot + 22 * SS), l1, font=cat_font, fill=CHART_SECONDARY, anchor="mt")
        d.text((cx, bot + 52 * SS), l2, font=catsub_font, fill=CHART_MUTED, anchor="mt")

    d.text((margin, (H - 44) * SS), FOOT, font=foot_font, fill=CHART_MUTED)

    img = img.resize((W, H), Image.LANCZOS)
    OUT.parent.mkdir(parents=True, exist_ok=True)
    img.save(OUT)
    print(f"wrote {OUT}  ({W}x{H})")


if __name__ == "__main__":
    render()
