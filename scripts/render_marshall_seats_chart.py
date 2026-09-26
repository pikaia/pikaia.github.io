"""Render the static PNG for the David Marshall post's video/Watch "chart" slide:

  assets/images/marshall-1955-seats-chart.png  - seats won at the 2 April 1955
      Legislative Assembly election (the post's inline bar chart), bar lengths on
      a linear 0-10 scale. Dark theme matching watch_video_lib's chart palette.

    python scripts/render_marshall_seats_chart.py
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
X0, X1, VMAX = 470, 1150, 10

ROWS = [
    ("Labour Front", "", 10, SERIES_2, "10"),
    ("Progressive Party", "", 4, CHART_LINE, "4"),
    ("People's Action Party", "", 3, CHART_LINE, "3"),
    ("Alliance", "(UMNO, MCA, Malay Union)", 3, CHART_LINE, "3"),
    ("Independents", "", 3, CHART_LINE, "3"),
    ("Democratic Party", "", 2, CHART_LINE, "2"),
]


def main():
    img = Image.new("RGB", (W * SS, H * SS), CHART_BG)
    d = ImageDraw.Draw(img)
    d.text((60 * SS, 40 * SS), "Seats won, 2 April 1955", font=load_font(34 * SS), fill=CHART_TEXT)
    d.text((60 * SS, 86 * SS), "The 25 elected seats of the 32-member Legislative Assembly",
           font=load_font(19 * SS, bold=False), fill=CHART_SECONDARY)

    leg = load_font(17 * SS, bold=False)
    ly = 122 * SS
    d.rectangle([60 * SS, ly, 82 * SS, ly + 10 * SS], fill=SERIES_2)
    d.text((90 * SS, ly + 5 * SS), "Party asked to form the government", font=leg, fill=CHART_SECONDARY, anchor="lm")
    d.rectangle([400 * SS, ly, 422 * SS, ly + 10 * SS], fill=CHART_LINE)
    d.text((430 * SS, ly + 5 * SS), "Other parties", font=leg, fill=CHART_SECONDARY, anchor="lm")

    def x(v):
        return (X0 + v * (X1 - X0) / VMAX) * SS

    lab, sub, val = load_font(21 * SS, bold=False), load_font(16 * SS, bold=False), load_font(23 * SS)
    top, step, bh = 172, 68, 42
    for i, (l1, l2, v, col, vl) in enumerate(ROWS):
        y = (top + i * step) * SS
        if l2:
            d.text(((X0 - 20) * SS, y + 12 * SS), l1, font=lab, fill=CHART_SECONDARY, anchor="rm")
            d.text(((X0 - 20) * SS, y + 33 * SS), l2, font=sub, fill=CHART_MUTED, anchor="rm")
        else:
            d.text(((X0 - 20) * SS, y + 21 * SS), l1, font=lab, fill=CHART_SECONDARY, anchor="rm")
        d.rounded_rectangle([X0 * SS, y, x(v), y + bh * SS], radius=5 * SS, fill=col)
        d.text((x(v) + 14 * SS, y + 21 * SS), vl, font=val, fill=CHART_TEXT, anchor="lm")

    base = (top + len(ROWS) * step - 14) * SS
    d.line([(X0 * SS, (top - 12) * SS), (X0 * SS, base)], fill=CHART_MUTED, width=SS)
    tick = load_font(17 * SS, bold=False)
    for t in (0, 2, 4, 6, 8, 10):
        d.text((x(t), base + 24 * SS), str(t), font=tick, fill=CHART_MUTED, anchor="mm")

    d.text((60 * SS, 686 * SS), "Source: The Sunday Times (Singapore), 3 April 1955, front page. The Alliance is counted as one group.",
           font=load_font(15 * SS, bold=False), fill=CHART_MUTED)
    out = IMG / "marshall-1955-seats-chart.png"
    img.resize((W, H), Image.LANCZOS).save(out)
    print(f"wrote {out}  ({W}x{H})")


if __name__ == "__main__":
    main()
