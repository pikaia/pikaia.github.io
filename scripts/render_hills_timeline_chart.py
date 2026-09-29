"""Render the static PNG for the vanished-hills post's video/Watch "chart" slide:

  assets/images/hills-timeline-chart.png  - how the waterfront hills disappeared,
      1822-1932 (the post's inline timeline), on a linear 1815-1940 axis, with
      bars for the Telok Ayer reclamation (1879-1897) and the cutting of Mount
      Palmer for the Telok Ayer Basin (1905-1932). Dark theme matching
      watch_video_lib's chart palette.

    python scripts/render_hills_timeline_chart.py
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
X0, X1, Y0, Y1 = 80, 1200, 1815, 1940
BY = 380
BAR2 = (230, 150, 60)

MARKS = [  # year, label, line 1, line 2, up?, lift
    (1822, "1822", "Wallich stays", "on the hill", True, 0),
    (1828, "1828", "Parsi burial ground", "on Mount Palmer", False, 0),
    (1879, "1879", "Telok Ayer", "reclamation begins", False, 0),
    (1884.9, "1884", "50,000-ton blast", "on Mount Wallich", True, 0),
    (1899, "1899", "Wallich Street", "named", True, 110),
    (1905, "1905", "Fort Palmer demolished;", "the hill is cut", False, 0),
    (1913.6, "1913", "Government acquires", "Mount Erskine", True, 0),
    (1932, "1932", "Basin finished; a knoll", "of Mount Palmer left", False, 0),
]


def main():
    img = Image.new("RGB", (W * SS, H * SS), CHART_BG)
    d = ImageDraw.Draw(img)
    d.text((60 * SS, 40 * SS), "How the waterfront hills disappeared, 1822-1932", font=load_font(34 * SS), fill=CHART_TEXT)
    d.text((60 * SS, 86 * SS), "Linear scale, 1815-1940", font=load_font(19 * SS, bold=False), fill=CHART_SECONDARY)

    def x(yr):
        return (X0 + (yr - Y0) * (X1 - X0) / (Y1 - Y0)) * SS

    d.line([(X0 * SS, (BY - 3) * SS), (X1 * SS, (BY - 3) * SS)], fill=CHART_MUTED, width=SS)
    d.rounded_rectangle([x(1879), BY * SS, x(1897), (BY + 16) * SS], radius=4 * SS, fill=CHART_LINE)
    d.rounded_rectangle([x(1905), BY * SS, x(1932), (BY + 16) * SS], radius=4 * SS, fill=BAR2)
    tick = load_font(17 * SS, bold=False)
    for t in (1820, 1860, 1900, 1940):
        d.text((x(t), (BY + 44) * SS), str(t), font=tick, fill=CHART_MUTED, anchor="mm")
    yf, lf = load_font(20 * SS), load_font(17 * SS, bold=False)
    for yr, year, l1, l2, up, lift in MARKS:
        cx = x(yr)
        if up:
            top = (BY - 40 - lift) * SS
            d.line([(cx, BY * SS), (cx, top)], fill=CHART_SECONDARY, width=2 * SS)
            d.ellipse([cx - 5 * SS, top - 5 * SS, cx + 5 * SS, top + 5 * SS], fill=CHART_SECONDARY)
            d.text((cx, top - 16 * SS), year, font=yf, fill=CHART_TEXT, anchor="mm")
            d.text((cx, top - 40 * SS), l2, font=lf, fill=CHART_SECONDARY, anchor="mm")
            d.text((cx, top - 62 * SS), l1, font=lf, fill=CHART_SECONDARY, anchor="mm")
        else:
            bot = (BY + 70 + lift) * SS
            d.line([(cx, (BY + 16) * SS), (cx, bot)], fill=CHART_SECONDARY, width=2 * SS)
            d.ellipse([cx - 5 * SS, bot - 5 * SS, cx + 5 * SS, bot + 5 * SS], fill=CHART_SECONDARY)
            d.text((cx, bot + 22 * SS), year, font=yf, fill=CHART_TEXT, anchor="mm")
            d.text((cx, bot + 46 * SS), l1, font=lf, fill=CHART_SECONDARY, anchor="mm")
            d.text((cx, bot + 68 * SS), l2, font=lf, fill=CHART_SECONDARY, anchor="mm")
    lg = load_font(16 * SS, bold=False)
    d.rounded_rectangle([60 * SS, 640 * SS, 80 * SS, 652 * SS], radius=3 * SS, fill=CHART_LINE)
    d.text((88 * SS, 646 * SS), "Telok Ayer reclamation, 1879-1897", font=lg, fill=CHART_SECONDARY, anchor="lm")
    d.rounded_rectangle([420 * SS, 640 * SS, 440 * SS, 652 * SS], radius=3 * SS, fill=BAR2)
    d.text((448 * SS, 646 * SS), "Mount Palmer cut for the Telok Ayer Basin, 1905-1932", font=lg, fill=CHART_SECONDARY, anchor="lm")
    d.text((60 * SS, 682 * SS), "Dates from the sources cited below the post.", font=load_font(15 * SS, bold=False), fill=CHART_MUTED)
    out = IMG / "hills-timeline-chart.png"
    img.resize((W, H), Image.LANCZOS).save(out)
    print(f"wrote {out}  ({W}x{H})")


if __name__ == "__main__":
    main()
