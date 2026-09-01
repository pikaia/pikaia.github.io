"""Render assets/images/aw-brothers-money-chart.png - the static PNG of
Haw Par Corporation's two income streams for the video / Watch "chart"
slide.

Mirrors the post's inline .aw-money SVG: two horizontal bars, the entire
worldwide Tiger Balm business against the dividends from a decades-old
UOB shareholding. Dark theme matching watch_video_lib's chart palette,
rendered once, near-full-frame (compose_chart_frame() can't animate a
bar chart - see docs/production-pipeline.md and CLAUDE.md Charts).

Committed binary, same documented exception as the OSM maps / other
chart PNGs.

    python scripts/render_aw_brothers_money_chart.py
"""
import sys
from pathlib import Path

from PIL import Image, ImageDraw

sys.path.insert(0, str(Path(__file__).resolve().parent))
from watch_video_lib import (  # noqa: E402
    CHART_BG, CHART_GRID, CHART_LINE, CHART_MUTED, CHART_SECONDARY, CHART_TEXT, load_font,
)

OUT = Path(__file__).resolve().parent.parent / "assets" / "images" / "aw-brothers-money-chart.png"
W, H = 1280, 720
SS = 2

TITLE = "Haw Par Corporation's two income streams, FY2025"
SUB = "The entire worldwide balm business, next to the dividends from a bank shareholding held for decades."
FOOT = ("Healthcare revenue S$240.5m (about a third outside Asia); UOB dividends S$169.9m. "
        "FY2025 net profit S$266m exceeded group revenue S$230m. Figures: Haw Par FY2025 results.")

X_MAX = 260  # S$ million
BARS = [
    ("Tiger Balm & medicated-oil sales worldwide", 240, "S$240m"),
    ("Dividends from its decades-old UOB shareholding", 170, "S$170m"),
]


def render():
    w, h = W * SS, H * SS
    img = Image.new("RGB", (w, h), CHART_BG)
    d = ImageDraw.Draw(img)

    title_font = load_font(int(34 * SS), bold=True)
    sub_font = load_font(int(19 * SS), bold=False)
    label_font = load_font(int(23 * SS), bold=False)
    value_font = load_font(int(26 * SS), bold=True)
    tick_font = load_font(int(18 * SS), bold=False)
    foot_font = load_font(int(15 * SS), bold=False)

    margin = 60 * SS
    d.text((margin, 44 * SS), TITLE, font=title_font, fill=CHART_TEXT)
    d.text((margin, 92 * SS), SUB, font=sub_font, fill=CHART_SECONDARY)

    plot_l = margin
    plot_r = (W - 160) * SS
    plot_t = 190 * SS
    plot_b = 560 * SS

    def x_of(v):
        return plot_l + v / X_MAX * (plot_r - plot_l)

    for gv in range(0, X_MAX + 1, 50):
        gx = x_of(gv)
        d.line([(gx, plot_t), (gx, plot_b)], fill=CHART_GRID, width=max(1, SS))
        d.text((gx, plot_b + 20 * SS), str(gv), font=tick_font, fill=CHART_MUTED, anchor="mm")
    d.text((x_of(X_MAX / 2), plot_b + 46 * SS), "S$ million", font=tick_font, fill=CHART_MUTED, anchor="mm")

    slot = (plot_b - plot_t) / len(BARS)
    bar_h = 60 * SS
    for i, (label, val, vtext) in enumerate(BARS):
        cy = plot_t + slot * (i + 0.5)
        d.text((plot_l, cy - bar_h / 2 - 12 * SS), label, font=label_font, fill=CHART_TEXT, anchor="ls")
        d.rounded_rectangle([plot_l, cy - bar_h / 2, x_of(val), cy + bar_h / 2],
                            radius=8 * SS, fill=CHART_LINE)
        d.text((x_of(val) + 16 * SS, cy), vtext, font=value_font, fill=CHART_TEXT, anchor="lm")

    d.text((margin, 640 * SS), FOOT, font=foot_font, fill=CHART_MUTED)

    img = img.resize((W, H), Image.LANCZOS)
    OUT.parent.mkdir(parents=True, exist_ok=True)
    img.save(OUT)
    print(f"wrote {OUT}  ({W}x{H})")


if __name__ == "__main__":
    render()
