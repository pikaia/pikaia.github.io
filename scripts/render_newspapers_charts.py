"""Render the two static PNGs for the newspapers post's video/Watch "chart" slides:

  assets/images/newspapers-1824-1846-chart.png  - the Chronicle's subsidy and the
      arrival of competition (the post's upper inline panel)
  assets/images/newspapers-2005-2025-chart.png  - public money returns (the post's
      lower inline panel)

Both panels are drawn on real linear year scales (as in the inline SVG) but split
across two full frames so each is legible at video size. Dark theme matching
watch_video_lib's chart palette.

    python scripts/render_newspapers_charts.py
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
X0, X1 = 150, 1130


def canvas():
    img = Image.new("RGB", (W * SS, H * SS), CHART_BG)
    return img, ImageDraw.Draw(img)


def save(img, name):
    out = IMG / name
    img.resize((W, H), Image.LANCZOS).save(out)
    print(f"wrote {out}  ({W}x{H})")


def timeline(name, title, sub, y0, y1, ticks, bars, marks, by):
    img, d = canvas()
    d.text((60 * SS, 40 * SS), title, font=load_font(34 * SS), fill=CHART_TEXT)
    d.text((60 * SS, 86 * SS), sub, font=load_font(19 * SS, bold=False), fill=CHART_SECONDARY)

    def x(yr):
        return (X0 + (yr - y0) * (X1 - X0) / (y1 - y0)) * SS

    leg = load_font(17 * SS, bold=False)
    ly = 122 * SS
    d.rectangle([60 * SS, ly, 82 * SS, ly + 10 * SS], fill=CHART_LINE)
    d.text((90 * SS, ly + 5 * SS), "Government subsidy or funding", font=leg, fill=CHART_SECONDARY, anchor="lm")
    d.rectangle([380 * SS, ly, 402 * SS, ly + 10 * SS], fill=SERIES_2)
    d.text((410 * SS, ly + 5 * SS), "Paid for by readers, advertisers and owners", font=leg, fill=CHART_SECONDARY, anchor="lm")

    by *= SS
    bh = 24 * SS
    for a, b, col in bars:
        d.rectangle([x(a), by, x(b), by + bh], fill=col)
    d.line([(X0 * SS, by - 4 * SS), (X1 * SS, by - 4 * SS)], fill=CHART_MUTED, width=SS)
    tick = load_font(16 * SS, bold=False)
    for yr in ticks:
        d.text((x(yr), by + bh + 20 * SS), str(yr), font=tick, fill=CHART_MUTED, anchor="mm")

    yf, lf = load_font(20 * SS), load_font(18 * SS, bold=False)
    for m in marks:
        yr, year, l1, l2, where = m[:5]
        lift = 60 * SS if len(m) > 5 and m[5] else 0
        # optional 7th field: shift the text block left so it clears a neighbouring stem
        tx = x(yr) - (75 * SS if len(m) > 6 and m[6] == "left" else 0)
        px = x(yr)
        if where == "up":
            d.line([(px, by), (px, by - 70 * SS - lift)], fill=CHART_SECONDARY, width=SS)
            d.ellipse([px - 5 * SS, by - 75 * SS - lift, px + 5 * SS, by - 65 * SS - lift], fill=CHART_SECONDARY)
            d.text((tx, by - 92 * SS - lift), year, font=yf, fill=CHART_TEXT, anchor="mm")
            d.text((tx, by - 118 * SS - lift), l2, font=lf, fill=CHART_SECONDARY, anchor="mm")
            d.text((tx, by - 142 * SS - lift), l1, font=lf, fill=CHART_SECONDARY, anchor="mm")
        else:
            top = by + bh
            d.line([(px, top + 6 * SS), (px, top + 60 * SS)], fill=CHART_SECONDARY, width=SS)
            d.ellipse([px - 5 * SS, top + 55 * SS, px + 5 * SS, top + 65 * SS], fill=CHART_SECONDARY)
            d.text((tx, top + 86 * SS), year, font=yf, fill=CHART_TEXT, anchor="mm")
            d.text((tx, top + 112 * SS), l1, font=lf, fill=CHART_SECONDARY, anchor="mm")
            d.text((tx, top + 136 * SS), l2, font=lf, fill=CHART_SECONDARY, anchor="mm")

    d.text((60 * SS, 686 * SS), "Dates and figures from the sources cited below the post.",
           font=load_font(15 * SS, bold=False), fill=CHART_MUTED)
    save(img, name)


def early_chart():
    timeline(
        "newspapers-1824-1846-chart.png",
        "1824–1846: from subsidy to open market",
        "Linear scale, 1820–1850",
        1820, 1850, (1820, 1830, 1840, 1850),
        [(1824, 1829, CHART_LINE), (1829, 1846, SERIES_2)],
        [(1824, "1824", "Chronicle launches,", "18 Spanish dollars a year", "up"),
         (1829, "1829", "Government subsidy", "withdrawn", "down"),
         (1835, "1835", "Press restrictions lifted;", "Free Press founded", "up"),
         (1837, "1837", "Chronicle ceases", "publication", "down"),
         (1845, "1845", "Straits Times, half", "a Spanish dollar", "up"),
         (1846, "1846", "Owner tries to sell,", "finds no buyer", "down")],
        by=370,
    )


def modern_chart():
    timeline(
        "newspapers-2005-2025-chart.png",
        "2005–2025: public money returns",
        "Linear scale, 2000–2030",
        2000, 2030, (2000, 2010, 2020, 2030),
        [(2000, 2022, SERIES_2), (2022, 2027, CHART_LINE)],
        [(2005, "2005", "Straits Times", "introduces a paywall", "up"),
         (2022, "2021–22", "SPH Media Trust set up;", "up to S$900m announced", "up", False, "left"),
         (2023, "2023", "Circulation found", "overstated by 10–12%", "down"),
         (2025, "2025", "Mediacorp: about", "S$380m a year", "up", True)],
        by=420,
    )


if __name__ == "__main__":
    early_chart()
    modern_chart()
