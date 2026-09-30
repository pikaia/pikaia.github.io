"""Render the static PNG for the Chinese banks post's video/Watch "chart" slide:

  assets/images/chinese-banks-chart.png  - Singapore's first Chinese banks by
      community, 1900-1975 (the post's inline lifespan chart): one row per
      community (Cantonese, Teochew, Hokkien), a bar per bank's life under its
      own name, the three Hokkien banks merging into OCBC in 1932. Colours are
      the dataviz reference palette's first three categorical slots (dark mode).

    python scripts/render_chinese_banks_chart.py
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
X0, X1, Y0, Y1 = 230, 1200, 1900, 1975
LANES = [("Cantonese", (57, 135, 229), 170), ("Teochew", (217, 89, 38), 300), ("Hokkien", (25, 158, 112), 430)]
BARS = [  # lane, row, start, end, label
    (0, 0, 1903, 1913, "Kwong Yik"),
    (0, 0, 1920, 1973, "Lee Wah"),
    (1, 0, 1907, 1972, "Sze Hai Tong"),
    (2, 0, 1912, 1932, "Chinese Commercial"),
    (2, 1, 1917, 1932, "Ho Hong"),
    (2, 2, 1919, 1932, "Oversea-Chinese"),
    (2, 1, 1932, 1975, "OCBC"),
]


def main():
    img = Image.new("RGB", (W * SS, H * SS), CHART_BG)
    d = ImageDraw.Draw(img)
    d.text((60 * SS, 40 * SS), "Singapore's first Chinese banks, by community", font=load_font(34 * SS), fill=CHART_TEXT)
    d.text((60 * SS, 86 * SS), "Each bar is a bank's life under its own name; the three Hokkien banks merged into OCBC in 1932",
           font=load_font(19 * SS, bold=False), fill=CHART_SECONDARY)

    def x(yr):
        return (X0 + (yr - Y0) * (X1 - X0) / (Y1 - Y0)) * SS

    lane_f, bar_f = load_font(26 * SS), load_font(20 * SS)
    for name, col, y in LANES:
        d.text(((X0 - 20) * SS, (y + 20) * SS), name, font=lane_f, fill=CHART_TEXT, anchor="rm")
    for lane, row, a, b, lab in BARS:
        name, col, y = LANES[lane]
        by = (y + row * 40) * SS
        d.rounded_rectangle([x(a), by, x(b), by + 32 * SS], radius=6 * SS, fill=col)
        w = x(b) - x(a)
        tw = d.textlength(lab, font=bar_f)
        if tw + 20 * SS < w:
            d.text((x(a) + 10 * SS, by + 16 * SS), lab, font=bar_f, fill=(255, 255, 255), anchor="lm")
        else:
            d.text((x(b) + 10 * SS, by + 16 * SS), lab, font=bar_f, fill=CHART_TEXT, anchor="lm")
    base = 600 * SS
    d.line([(X0 * SS, base), (X1 * SS, base)], fill=CHART_MUTED, width=SS)
    tick = load_font(17 * SS, bold=False)
    for t in range(1900, 1976, 10):
        d.text((x(t), base + 24 * SS), str(t), font=tick, fill=CHART_MUTED, anchor="mm")
    d.text((60 * SS, 682 * SS), "Dates from the Infopedia articles cited below the post.", font=load_font(15 * SS, bold=False), fill=CHART_MUTED)
    out = IMG / "chinese-banks-chart.png"
    img.resize((W, H), Image.LANCZOS).save(out)
    print(f"wrote {out}  ({W}x{H})")


if __name__ == "__main__":
    main()
