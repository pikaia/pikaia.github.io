"""Render the static PNG for the 1914 bank-run post's video/Watch "chart" slide:

  assets/images/bank-run-1914-chart.png  - the Chinese Commercial Bank's cash,
      August-October 1914 (the post's inline bar chart): paid out on 4 and 5
      August, cash left at the close on 5 August, and the net intake by noon on
      reopening day. Colours are the dataviz reference palette's first two
      categorical slots plus the secondary text ink (dark mode).

    python scripts/render_bank_run_1914_chart.py
"""
import sys
from pathlib import Path

from PIL import Image, ImageDraw

sys.path.insert(0, str(Path(__file__).resolve().parent))
from watch_video_lib import (  # noqa: E402
    CHART_BG, CHART_MUTED, CHART_SECONDARY, CHART_TEXT, load_font,
)

IMG = Path(__file__).resolve().parent.parent / "assets" / "images"
W, H = 1280, 720
SS = 2
X0, X1, VMAX = 400, 1120, 300000
BLUE, ORANGE = (57, 135, 229), (217, 89, 38)
ROWS = [  # label, sublabel, value, colour, shown value
    ("Tue 4 Aug", "paid over the counter", 257667, BLUE, "$257,667"),
    ("Wed 5 Aug", "paid out, despite delays", 50000, BLUE, "$50,000"),
    ("Close, 5 Aug", "cash left in hand", 167268, CHART_SECONDARY, "$167,268"),
    ("Thu 1 Oct, noon", "taken in more than paid out", 27552, ORANGE, "+$27,552"),
]


def main():
    img = Image.new("RGB", (W * SS, H * SS), CHART_BG)
    d = ImageDraw.Draw(img)
    d.text((60 * SS, 40 * SS), "The Chinese Commercial Bank's cash, 1914", font=load_font(34 * SS), fill=CHART_TEXT)
    d.text((60 * SS, 86 * SS), "Straits dollars. The run of 4-5 August, and reopening day on 1 October",
           font=load_font(19 * SS, bold=False), fill=CHART_SECONDARY)

    def x(v):
        return (X0 + v * (X1 - X0) / VMAX) * SS

    lab_f, sub_f, val_f = load_font(26 * SS), load_font(18 * SS, bold=False), load_font(24 * SS)
    for i, (lab, sub, v, col, shown) in enumerate(ROWS):
        y = 150 + i * 105
        d.text(((X0 - 24) * SS, (y + 12) * SS), lab, font=lab_f, fill=CHART_TEXT, anchor="rm")
        d.text(((X0 - 24) * SS, (y + 44) * SS), sub, font=sub_f, fill=CHART_SECONDARY, anchor="rm")
        d.rounded_rectangle([X0 * SS, y * SS, x(v), (y + 56) * SS], radius=6 * SS, fill=col)
        d.text((x(v) + 14 * SS, (y + 28) * SS), shown, font=val_f, fill=CHART_TEXT, anchor="lm")
    base = 580 * SS
    d.line([(X0 * SS, 140 * SS), (X0 * SS, base)], fill=CHART_MUTED, width=SS)
    tick = load_font(17 * SS, bold=False)
    for t in range(0, VMAX + 1, 100000):
        d.text((x(t), base + 24 * SS), "$0" if t == 0 else f"${t:,}", font=tick, fill=CHART_MUTED, anchor="mm")
    d.text((60 * SS, 680 * SS), "Sources: Straits Times, 24 September 1914; Straits Echo, 5 October 1914.",
           font=load_font(15 * SS, bold=False), fill=CHART_MUTED)
    out = IMG / "bank-run-1914-chart.png"
    img.resize((W, H), Image.LANCZOS).save(out)
    print(f"wrote {out}  ({W}x{H})")


if __name__ == "__main__":
    main()
