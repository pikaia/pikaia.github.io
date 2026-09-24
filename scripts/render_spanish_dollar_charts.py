"""Render the two static PNGs for the Spanish dollar post's video/Watch "chart" slides:

  assets/images/spanish-dollar-reserve-currencies-chart.png  - who held the world's
      reserve-currency role (the post's upper inline panel)
  assets/images/spanish-dollar-singapore-money-chart.png     - Singapore's own money,
      1815-1945 (the post's lower inline panel)

Both panels are drawn on real linear year scales (as in the inline SVG) but split
across two full frames so each is legible at video size. Dark theme matching
watch_video_lib's chart palette.

    python scripts/render_spanish_dollar_charts.py
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
GREY = (137, 135, 129)


def canvas():
    img = Image.new("RGB", (W * SS, H * SS), CHART_BG)
    return img, ImageDraw.Draw(img)


def header(d, title, sub):
    d.text((60 * SS, 40 * SS), title, font=load_font(34 * SS), fill=CHART_TEXT)
    d.text((60 * SS, 86 * SS), sub, font=load_font(19 * SS, bold=False), fill=CHART_SECONDARY)


def save(img, name):
    out = IMG / name
    img.resize((W, H), Image.LANCZOS).save(out)
    print(f"wrote {out}  ({W}x{H})")


def reserve_chart():
    img, d = canvas()
    header(d, "Who held the world's reserve-currency role",
           "Approximate periods; the handover years are contested")
    X0, X1, Y0, Y1 = 100, 1120, 1500, 2000

    def x(yr):
        return (X0 + (yr - Y0) * (X1 - X0) / (Y1 - Y0)) * SS

    rows = [
        ("Spanish dollar, 16th–19th centuries", 1500, 1900, CHART_LINE),
        ("Dutch guilder, 17th–18th centuries (the Dutch empire's trade)", 1600, 1800, GREY),
        ("Pound sterling, 19th to early 20th century", 1800, 1950, GREY),
        ("US dollar, from 1944", 1944, 2026, GREY),
    ]
    lab = load_font(21 * SS, bold=False)
    for i, (label, s, e, col) in enumerate(rows):
        y = (200 + i * 100) * SS
        d.text((x(s), y - 12 * SS), label, font=lab, fill=CHART_TEXT if i == 0 else CHART_SECONDARY, anchor="ls")
        d.rounded_rectangle([x(s), y, x(e), y + 36 * SS], radius=6 * SS, fill=col)
    ay = 600 * SS
    d.line([(X0 * SS, ay), (x(2030), ay)], fill=CHART_MUTED, width=SS)
    tick = load_font(17 * SS, bold=False)
    for yr in range(1500, 2001, 100):
        d.line([(x(yr), ay), (x(yr), ay + 8 * SS)], fill=CHART_MUTED, width=SS)
        d.text((x(yr), ay + 28 * SS), str(yr), font=tick, fill=CHART_MUTED, anchor="mm")
    d.text((60 * SS, 686 * SS), "Sources: Wikipedia (Reserve currency, Spanish dollar); cited below the post.",
           font=load_font(15 * SS, bold=False), fill=CHART_MUTED)
    save(img, "spanish-dollar-reserve-currencies-chart.png")


def singapore_chart():
    img, d = canvas()
    header(d, "Singapore's own money, 1815–1945",
           "From the Spanish dollar to the Straits dollar and the Malayan dollar")
    X0, X1, Y0, Y1 = 150, 1130, 1815, 1945

    def x(yr):
        return (X0 + (yr - Y0) * (X1 - X0) / (Y1 - Y0)) * SS

    ly = 122 * SS
    leg = load_font(17 * SS, bold=False)
    d.rectangle([60 * SS, ly, 82 * SS, ly + 10 * SS], fill=CHART_LINE)
    d.text((90 * SS, ly + 5 * SS), "Silver-dollar era", font=leg, fill=CHART_SECONDARY, anchor="lm")
    d.rectangle([300 * SS, ly, 322 * SS, ly + 10 * SS], fill=SERIES_2)
    d.text((330 * SS, ly + 5 * SS), "Straits dollar era", font=leg, fill=CHART_SECONDARY, anchor="lm")

    by = 380 * SS
    bh = 24 * SS
    d.rectangle([x(1819), by, x(1903), by + bh], fill=CHART_LINE)
    d.rectangle([x(1903), by, x(1939), by + bh], fill=SERIES_2)
    d.line([(X0 * SS, by - 4 * SS), (X1 * SS, by - 4 * SS)], fill=CHART_MUTED, width=SS)
    tick = load_font(16 * SS, bold=False)
    for yr in (1820, 1860, 1900, 1940):
        d.text((x(yr), by + bh + 20 * SS), str(yr), font=tick, fill=CHART_MUTED, anchor="mm")

    yf, lf = load_font(20 * SS), load_font(18 * SS, bold=False)

    def above(yr, year, l1, l2):
        px = x(yr)
        d.line([(px, by), (px, by - 70 * SS)], fill=CHART_SECONDARY, width=SS)
        d.ellipse([px - 5 * SS, by - 75 * SS, px + 5 * SS, by - 65 * SS], fill=CHART_SECONDARY)
        d.text((px, by - 92 * SS), year, font=yf, fill=CHART_TEXT, anchor="mm")
        d.text((px, by - 118 * SS), l2, font=lf, fill=CHART_SECONDARY, anchor="mm")
        d.text((px, by - 142 * SS), l1, font=lf, fill=CHART_SECONDARY, anchor="mm")

    above(1824, "1824", "Treaty paid in", "Spanish dollars")
    above(1867, "1867", "Crown colony: five", "silver dollars legal tender")
    above(1897, "1895–99", "Trade dollar, Currency", "Board, first notes")
    above(1939, "1939", "Malayan dollar", "replaces Straits dollar")

    # bracket 1826-67, below
    b0, b1 = x(1826), x(1867)
    yb = by + bh + 60 * SS
    d.line([(b0, by + bh + 6 * SS), (b0, yb), (b1, yb), (b1, by + bh + 6 * SS)], fill=CHART_SECONDARY, width=SS)
    mid = (b0 + b1) / 2
    d.text((mid, yb + 26 * SS), "1826–67", font=yf, fill=CHART_TEXT, anchor="mm")
    d.text((mid, yb + 54 * SS), "Rupee for the accounts,", font=lf, fill=CHART_SECONDARY, anchor="mm")
    d.text((mid, yb + 78 * SS), "dollar for the trade", font=lf, fill=CHART_SECONDARY, anchor="mm")

    # 1903-06 below
    cx = (x(1903) + x(1906)) / 2
    d.line([(cx, by + bh + 6 * SS), (cx, yb)], fill=CHART_SECONDARY, width=SS)
    d.ellipse([cx - 5 * SS, yb - 5 * SS, cx + 5 * SS, yb + 5 * SS], fill=SERIES_2)
    d.text((cx, yb + 26 * SS), "1903–06", font=yf, fill=CHART_TEXT, anchor="mm")
    d.text((cx, yb + 54 * SS), "Straits dollar,", font=lf, fill=CHART_SECONDARY, anchor="mm")
    d.text((cx, yb + 78 * SS), "pegged at 2s 4d", font=lf, fill=CHART_SECONDARY, anchor="mm")

    d.text((60 * SS, 686 * SS), "Dates from the sources cited below the post.",
           font=load_font(15 * SS, bold=False), fill=CHART_MUTED)
    save(img, "spanish-dollar-singapore-money-chart.png")


if __name__ == "__main__":
    reserve_chart()
    singapore_chart()
