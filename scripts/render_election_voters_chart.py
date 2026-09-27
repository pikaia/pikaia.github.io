"""Render the static PNG for the 1948 election post's video/Watch "chart" slide:

  assets/images/election-1948-registered-voters-chart.png  - registered voters at
      the 1948, 1951, 1955 and 1959 elections (the post's inline bar chart), bar
      lengths on a linear 0-600,000 scale, with the elected seats beside each
      bar. Dark theme matching watch_video_lib's chart palette.

    python scripts/render_election_voters_chart.py
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
X0, X1, VMAX = 330, 1080, 600000

ROWS = [
    ("1948", "Legislative Council", 22334, "22,334", "6 of 22 seats elected"),
    ("1951", "Legislative Council", 48155, "48,155", "9 of 25 seats elected"),
    ("1955", "Legislative Assembly", 300199, "300,199", "25 of 32 seats elected"),
    ("1959", "Legislative Assembly", 586098, "586,098", "all 51 seats elected"),
]


def main():
    img = Image.new("RGB", (W * SS, H * SS), CHART_BG)
    d = ImageDraw.Draw(img)
    d.text((60 * SS, 40 * SS), "Registered voters at Singapore's first four elections", font=load_font(34 * SS), fill=CHART_TEXT)
    d.text((60 * SS, 86 * SS), "Linear scale; beside each bar, how many seats were elected",
           font=load_font(19 * SS, bold=False), fill=CHART_SECONDARY)

    def x(v):
        return (X0 + v * (X1 - X0) / VMAX) * SS

    yr_f, lab, val, sub = load_font(26 * SS), load_font(17 * SS, bold=False), load_font(23 * SS), load_font(17 * SS, bold=False)
    top, step, bh = 160, 100, 56
    for i, (yr, body, v, vl, seats) in enumerate(ROWS):
        y = (top + i * step) * SS
        d.text(((X0 - 20) * SS, y + 18 * SS), yr, font=yr_f, fill=CHART_TEXT, anchor="rm")
        d.text(((X0 - 20) * SS, y + 44 * SS), body, font=lab, fill=CHART_SECONDARY, anchor="rm")
        d.rounded_rectangle([X0 * SS, y, max(x(v), (X0 + 4) * SS), y + bh * SS], radius=5 * SS, fill=CHART_LINE)
        vx = max(x(v), (X0 + 4) * SS) + 14 * SS
        if x(v) > (X1 - 190) * SS:
            vx = x(v) - 14 * SS
            d.text((vx, y + 18 * SS), vl, font=val, fill=CHART_BG, anchor="rm")
            d.text((vx, y + 42 * SS), seats, font=sub, fill=CHART_BG, anchor="rm")
        else:
            d.text((vx, y + 18 * SS), vl, font=val, fill=CHART_TEXT, anchor="lm")
            d.text((vx, y + 42 * SS), seats, font=sub, fill=CHART_SECONDARY, anchor="lm")

    base = (top + len(ROWS) * step - 20) * SS
    d.line([(X0 * SS, (top - 12) * SS), (X0 * SS, base)], fill=CHART_MUTED, width=SS)
    tick = load_font(17 * SS, bold=False)
    for t in (0, 200000, 400000, 600000):
        d.text((x(t), base + 24 * SS), f"{t:,}", font=tick, fill=CHART_MUTED, anchor="mm")

    d.text((60 * SS, 686 * SS), "Sources: The Sunday Times, 21 March 1948; election records for 1951-1959 cited below the post.",
           font=load_font(15 * SS, bold=False), fill=CHART_MUTED)
    out = IMG / "election-1948-registered-voters-chart.png"
    img.resize((W, H), Image.LANCZOS).save(out)
    print(f"wrote {out}  ({W}x{H})")


if __name__ == "__main__":
    main()
