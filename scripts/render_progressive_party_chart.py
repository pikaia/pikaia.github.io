"""Render the static PNG for the Progressive Party post's video/Watch "chart" slide:

  assets/images/progressive-party-vote-seat-share-chart.png  - the party's share
      of the vote and of the elected seats at the 1948, 1951, 1955 and 1959
      elections (the post's inline grouped bar chart; 1959 is the Liberal
      Socialist Party it merged into). Linear 0-70% scale, dark theme matching
      watch_video_lib's chart palette.

    python scripts/render_progressive_party_chart.py
"""
import sys
from pathlib import Path

from PIL import Image, ImageDraw

sys.path.insert(0, str(Path(__file__).resolve().parent))
from watch_video_lib import (  # noqa: E402
    CHART_BG, CHART_GRID, CHART_LINE, CHART_MUTED, CHART_SECONDARY, CHART_TEXT, load_font,
)

IMG = Path(__file__).resolve().parent.parent / "assets" / "images"
W, H = 1280, 720
SS = 2
SERIES_2 = (31, 166, 31)  # #1fa61f, dark-mode --series-2
BASE, TOP, VMAX = 560, 170, 70
BAR_W, GAP = 92, 8

# (year, voters label, vote share %, seat share %, seat label)
ROWS = [
    ("1948", "22,334 voters", 49.5, 50.0, "3 of 6"),
    ("1951", "48,155 voters", 45.4, 66.7, "6 of 9"),
    ("1955", "about 300,000 voters", 24.8, 16.0, "4 of 25"),
    ("1959", "over 580,000 voters", 8.2, 0.0, "0 of 51"),
]
CENTRES = [290, 560, 830, 1100]


def y(v):
    return (BASE - v * (BASE - TOP) / VMAX) * SS


def main():
    img = Image.new("RGB", (W * SS, H * SS), CHART_BG)
    d = ImageDraw.Draw(img)
    d.text((60 * SS, 40 * SS), "The Progressive Party's share of the vote and of the seats",
           font=load_font(32 * SS), fill=CHART_TEXT)
    d.text((60 * SS, 84 * SS), "Each election, 1948-1959; 1959 is the Liberal Socialist Party it merged into",
           font=load_font(19 * SS, bold=False), fill=CHART_SECONDARY)

    leg = load_font(17 * SS, bold=False)
    ly = 122 * SS
    d.rectangle([60 * SS, ly, 82 * SS, ly + 12 * SS], fill=CHART_LINE)
    d.text((90 * SS, ly + 6 * SS), "Share of the vote", font=leg, fill=CHART_SECONDARY, anchor="lm")
    d.rectangle([300 * SS, ly, 322 * SS, ly + 12 * SS], fill=SERIES_2)
    d.text((330 * SS, ly + 6 * SS), "Share of elected seats", font=leg, fill=CHART_SECONDARY, anchor="lm")

    tick = load_font(16 * SS, bold=False)
    for t in (0, 20, 40, 60):
        d.line([(110 * SS, y(t)), (1220 * SS, y(t))], fill=CHART_GRID if t else CHART_MUTED, width=SS)
        d.text((100 * SS, y(t)), f"{t}%", font=tick, fill=CHART_MUTED, anchor="rm")

    val, small = load_font(20 * SS), load_font(15 * SS, bold=False)
    yr, sub = load_font(22 * SS), load_font(16 * SS, bold=False)
    for (year, voters, vote, seat, seats), c in zip(ROWS, CENTRES):
        vx0, sx0 = c - GAP // 2 - BAR_W, c + GAP // 2
        d.rounded_rectangle([vx0 * SS, y(vote), (vx0 + BAR_W) * SS, y(0)], radius=5 * SS, fill=CHART_LINE)
        d.text(((vx0 + BAR_W / 2) * SS, y(vote) - 14 * SS), f"{vote:.1f}%", font=val, fill=CHART_TEXT, anchor="mm")
        if seat > 0:
            d.rounded_rectangle([sx0 * SS, y(seat), (sx0 + BAR_W) * SS, y(0)], radius=5 * SS, fill=SERIES_2)
        d.text(((sx0 + BAR_W / 2) * SS, y(seat) - 14 * SS), f"{seat:.0f}%", font=val, fill=CHART_TEXT, anchor="mm")
        d.text(((sx0 + BAR_W / 2) * SS, y(seat) - 36 * SS), seats, font=small, fill=CHART_SECONDARY, anchor="mm")
        d.text((c * SS, 588 * SS), year, font=yr, fill=CHART_TEXT, anchor="mm")
        d.text((c * SS, 614 * SS), voters, font=sub, fill=CHART_MUTED, anchor="mm")

    d.text((60 * SS, 680 * SS),
           "Sources: The Straits Times, 11 April 1951; Elections Department Singapore results (1955, 1959); "
           "1948 election records.", font=load_font(15 * SS, bold=False), fill=CHART_MUTED, anchor="lm")
    out = IMG / "progressive-party-vote-seat-share-chart.png"
    img.resize((W, H), Image.LANCZOS).save(out)
    print(f"wrote {out}  ({W}x{H})")


if __name__ == "__main__":
    main()
