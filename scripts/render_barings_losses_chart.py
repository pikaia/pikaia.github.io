"""Render the static PNG for the Barings 1995 post's video/Watch "chart" slide:

  assets/images/barings-losses-chart.png  - the losses hidden in account 88888,
      1992-1995 (the post's inline bar chart), in Singapore dollars, from the
      Singapore inspectors' report as summarised by NLB Infopedia. Colours are
      the dataviz reference palette's first two categorical slots (dark mode).

    python scripts/render_barings_losses_chart.py
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
X0, X1, VMAX = 400, 1080, 2500
BLUE, ORANGE = (57, 135, 229), (217, 89, 38)
ROWS = [  # label, sublabel, value (S$ million), colour, shown value
    ("Sep 1992", "three months after it opened", 8.8, BLUE, "S$8.8 million"),
    ("Dec 1994", "after the internal audit", 373.9, BLUE, "S$373.9 million"),
    ("23 Feb 1995", "the day Leeson left", 1400, BLUE, "S$1.4 billion"),
    ("26 Feb 1995", "Barings' total losses", 2200, ORANGE, "S$2.2 billion"),
]


def main():
    img = Image.new("RGB", (W * SS, H * SS), CHART_BG)
    d = ImageDraw.Draw(img)
    d.text((60 * SS, 40 * SS), "The losses hidden in account 88888", font=load_font(34 * SS), fill=CHART_TEXT)
    d.text((60 * SS, 86 * SS), "Singapore dollars, 1992-1995",
           font=load_font(19 * SS, bold=False), fill=CHART_SECONDARY)

    def x(v):
        return (X0 + v * (X1 - X0) / VMAX) * SS

    lab_f, sub_f, val_f = load_font(26 * SS), load_font(18 * SS, bold=False), load_font(24 * SS)
    for i, (lab, sub, v, col, shown) in enumerate(ROWS):
        y = 150 + i * 105
        d.text(((X0 - 24) * SS, (y + 12) * SS), lab, font=lab_f, fill=CHART_TEXT, anchor="rm")
        d.text(((X0 - 24) * SS, (y + 44) * SS), sub, font=sub_f, fill=CHART_SECONDARY, anchor="rm")
        d.rounded_rectangle([X0 * SS, y * SS, max(x(v), (X0 + 4) * SS), (y + 56) * SS], radius=4 * SS, fill=col)
        d.text((max(x(v), (X0 + 4) * SS) + 14 * SS, (y + 28) * SS), shown, font=val_f, fill=CHART_TEXT, anchor="lm")
    base = 580 * SS
    d.line([(X0 * SS, 140 * SS), (X0 * SS, base)], fill=CHART_MUTED, width=SS)
    tick = load_font(17 * SS, bold=False)
    for t, lab in ((0, "S$0"), (1000, "S$1 billion"), (2000, "S$2 billion")):
        d.text((x(t), base + 24 * SS), lab, font=tick, fill=CHART_MUTED, anchor="mm")
    d.text((60 * SS, 680 * SS), "Source: Singapore inspectors' report (1995), via NLB Infopedia, \"Collapse of Barings\".",
           font=load_font(15 * SS, bold=False), fill=CHART_MUTED)
    out = IMG / "barings-losses-chart.png"
    img.resize((W, H), Image.LANCZOS).save(out)
    print(f"wrote {out}  ({W}x{H})")


if __name__ == "__main__":
    main()
