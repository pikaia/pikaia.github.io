"""Render assets/images/three-days-stock-exchange-shut-1985-money.png - the
static PNG of the Pan-Electric crisis money figures for the video / Watch
slide.

Mirrors the post's inline .pe-money SVG: four horizontal bars putting the
market-wide broker exposure, Pan-Electric's bank debt, the four-bank
rescue line and Tan Koon Swan's own position on one scale. Dark theme
matching watch_video_lib's chart palette, rendered once, near-full-frame
(compose_chart_frame() can't animate a bar chart - see
docs/production-pipeline.md and CLAUDE.md Charts).

Committed binary, same documented exception as the OSM maps / other
chart PNGs.

    python scripts/render_three_days_money_chart.py
"""
import sys
from pathlib import Path

from PIL import Image, ImageDraw

sys.path.insert(0, str(Path(__file__).resolve().parent))
from watch_video_lib import (  # noqa: E402
    CHART_BG, CHART_GRID, CHART_LINE, CHART_MUTED, CHART_SECONDARY, CHART_TEXT, load_font,
)

OUT = (Path(__file__).resolve().parent.parent / "assets" / "images"
       / "three-days-stock-exchange-shut-1985-money.png")
W, H = 1280, 720
SS = 2

TITLE = "The 1985 crisis, by the scale of the money"
SUB = ("Broker exposure to Pan-Electric stock, the company's bank debt, the rescue line, "
       "and Tan Koon Swan's own position.")
FOOT = ("Figures approximate, from contemporary reports and later reviews. "
        "Sources: MAS Staff Paper No. 32 (2004); SAL (2022); NLB.")

X_MAX = 640  # S$ million
BARS = [
    ("Brokers' forward exposure to Pan-Electric and related stocks", 600, "~S$600m"),
    ("Pan-Electric's disclosed borrowings from 35 banks", 453, "S$453m"),
    ("The four banks' rescue credit line", 180, "S$180m"),
    ("Tan Koon Swan's own forward commitments", 140, "~S$140m"),
]


def render():
    w, h = W * SS, H * SS
    img = Image.new("RGB", (w, h), CHART_BG)
    d = ImageDraw.Draw(img)

    title_font = load_font(int(34 * SS), bold=True)
    sub_font = load_font(int(19 * SS), bold=False)
    label_font = load_font(int(21 * SS), bold=False)
    value_font = load_font(int(25 * SS), bold=True)
    tick_font = load_font(int(17 * SS), bold=False)
    foot_font = load_font(int(15 * SS), bold=False)

    margin = 60 * SS
    d.text((margin, 42 * SS), TITLE, font=title_font, fill=CHART_TEXT)
    d.text((margin, 88 * SS), SUB, font=sub_font, fill=CHART_SECONDARY)

    plot_l = margin
    plot_r = (W - 190) * SS
    plot_t = 170 * SS
    plot_b = 590 * SS

    def x_of(v):
        return plot_l + v / X_MAX * (plot_r - plot_l)

    for gv in range(0, X_MAX + 1, 100):
        gx = x_of(gv)
        d.line([(gx, plot_t), (gx, plot_b)], fill=CHART_GRID, width=max(1, SS))
        d.text((gx, plot_b + 20 * SS), str(gv), font=tick_font, fill=CHART_MUTED, anchor="mm")
    d.text((x_of(X_MAX / 2), plot_b + 46 * SS), "S$ million", font=tick_font, fill=CHART_MUTED, anchor="mm")

    slot = (plot_b - plot_t) / len(BARS)
    bar_h = 52 * SS
    for i, (label, val, vtext) in enumerate(BARS):
        cy = plot_t + slot * (i + 0.5)
        d.text((plot_l, cy - bar_h / 2 - 12 * SS), label, font=label_font, fill=CHART_TEXT, anchor="ls")
        d.rounded_rectangle([plot_l, cy - bar_h / 2, x_of(val), cy + bar_h / 2],
                            radius=8 * SS, fill=CHART_LINE)
        d.text((x_of(val) + 16 * SS, cy), vtext, font=value_font, fill=CHART_TEXT, anchor="lm")

    d.text((margin, 668 * SS), FOOT, font=foot_font, fill=CHART_MUTED)

    img = img.resize((W, H), Image.LANCZOS)
    OUT.parent.mkdir(parents=True, exist_ok=True)
    img.save(OUT)
    print(f"wrote {OUT}  ({W}x{H})")


if __name__ == "__main__":
    render()
