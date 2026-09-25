"""Render the static PNG for the Tanjong Pagar post's video/Watch "chart" slide:

  assets/images/tanjong-pagar-share-price-chart.png  - five per-$100-share figures
      around the 1905 takeover (the post's inline bar chart), bar lengths on a
      linear $0-800 scale, ordered by amount (not a timeline). Dark theme
      matching watch_video_lib's chart palette.

    python scripts/render_tanjong_pagar_bar_chart.py
"""
import sys
from pathlib import Path

from PIL import Image, ImageDraw

sys.path.insert(0, str(Path(__file__).resolve().parent))
from watch_video_lib import (  # noqa: E402
    CHART_BG, CHART_LINE, CHART_MUTED, CHART_SECONDARY, CHART_TEXT, load_font,
)

IMG = Path(__file__).resolve().parent.parent / "assets" / "images"
W, H = 1280, 720
SS = 2
SERIES_2 = (31, 166, 31)  # #1fa61f, dark-mode --series-2
X0, X1, VMAX = 470, 1150, 800

ROWS = [
    ("Par value of a share", "", 100, CHART_LINE, "$100"),
    ("Quoted price when", "expropriation was decided", 240, CHART_LINE, "about $240"),
    ("Highest market price", "reached by the share", 600, CHART_LINE, "$600"),
    ("Figure the directors", "mentioned to the Governor", 700, CHART_LINE, "$700"),
    ("Arbitration award", "(declared 14 July 1906)", 755, SERIES_2, "about $755"),
]


def main():
    img = Image.new("RGB", (W * SS, H * SS), CHART_BG)
    d = ImageDraw.Draw(img)
    d.text((60 * SS, 40 * SS), "What a $100 share was worth in 1905–06", font=load_font(34 * SS), fill=CHART_TEXT)
    d.text((60 * SS, 86 * SS), "Five figures from the takeover, ordered by amount (not a timeline)",
           font=load_font(19 * SS, bold=False), fill=CHART_SECONDARY)

    leg = load_font(17 * SS, bold=False)
    ly = 122 * SS
    d.rectangle([60 * SS, ly, 82 * SS, ly + 10 * SS], fill=CHART_LINE)
    d.text((90 * SS, ly + 5 * SS), "Reference and market figures", font=leg, fill=CHART_SECONDARY, anchor="lm")
    d.rectangle([380 * SS, ly, 402 * SS, ly + 10 * SS], fill=SERIES_2)
    d.text((410 * SS, ly + 5 * SS), "Price the government paid", font=leg, fill=CHART_SECONDARY, anchor="lm")

    def x(v):
        return (X0 + v * (X1 - X0) / VMAX) * SS

    lab, val = load_font(21 * SS, bold=False), load_font(23 * SS)
    top, step, bh = 175, 82, 46
    for i, (l1, l2, v, col, vl) in enumerate(ROWS):
        y = (top + i * step) * SS
        if l2:
            d.text(((X0 - 20) * SS, y + 4 * SS), l1, font=lab, fill=CHART_SECONDARY, anchor="rm")
            d.text(((X0 - 20) * SS, y + 32 * SS), l2, font=lab, fill=CHART_SECONDARY, anchor="rm")
        else:
            d.text(((X0 - 20) * SS, y + 23 * SS), l1, font=lab, fill=CHART_SECONDARY, anchor="rm")
        d.rounded_rectangle([X0 * SS, y, x(v), y + bh * SS], radius=5 * SS, fill=col)
        d.text((x(v) + 14 * SS, y + 23 * SS), vl, font=val, fill=CHART_TEXT, anchor="lm")

    base = (top + len(ROWS) * step - 12) * SS
    d.line([(X0 * SS, (top - 12) * SS), (X0 * SS, base)], fill=CHART_MUTED, width=SS)
    tick = load_font(17 * SS, bold=False)
    for t in (0, 200, 400, 600, 800):
        d.text((x(t), base + 24 * SS), f"${t}", font=tick, fill=CHART_MUTED, anchor="mm")

    d.text((60 * SS, 686 * SS), "Sources: House of Commons Hansard, 28 November 1906; BiblioAsia (National Library Board), 2019.",
           font=load_font(15 * SS, bold=False), fill=CHART_MUTED)
    out = IMG / "tanjong-pagar-share-price-chart.png"
    img.resize((W, H), Image.LANCZOS).save(out)
    print(f"wrote {out}  ({W}x{H})")


if __name__ == "__main__":
    main()
