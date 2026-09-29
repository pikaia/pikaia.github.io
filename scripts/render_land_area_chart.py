"""Render the static PNG for the shoreline post's video/Watch "chart" slide:

  assets/images/singapore-land-area-chart.png  - Singapore's total land area,
      1960-2025, from the Singapore Land Authority's "Total Land Area of
      Singapore" dataset on data.gov.sg (end-of-year figures, km2, offshore
      islands included). Same series as the post's inline line chart. The
      y-axis starts at 550 km2, noted on the chart. Dark theme matching
      watch_video_lib's chart palette.

    python scripts/render_land_area_chart.py
"""
import json
import sys
import urllib.request
from pathlib import Path

from PIL import Image, ImageDraw

sys.path.insert(0, str(Path(__file__).resolve().parent))
from watch_video_lib import (  # noqa: E402
    CHART_BG, CHART_LINE, CHART_MUTED, CHART_SECONDARY, CHART_TEXT, load_font,
)

ROOT = Path(__file__).resolve().parent.parent
IMG = ROOT / "assets" / "images"
CACHE = ROOT / "scratch" / "rc" / "d_f74e5ee9575e98ba439bee67e8f9b097.json"
URL = "https://data.gov.sg/api/action/datastore_search?resource_id=d_f74e5ee9575e98ba439bee67e8f9b097&limit=200"
W, H = 1280, 720
SS = 2
X0, X1, Y0, Y1 = 150, 1130, 150, 580
YMIN, YMAX = 550, 760


def data():
    if CACHE.exists():
        d = json.loads(CACHE.read_text())
    else:
        d = json.loads(urllib.request.urlopen(URL, timeout=60).read())
    return [(int(r["year"]), float(r["total_land_area"])) for r in d["result"]["records"]]


def main():
    rows = data()
    y_first, y_last = rows[0][0], rows[-1][0]
    img = Image.new("RGB", (W * SS, H * SS), CHART_BG)
    d = ImageDraw.Draw(img)
    d.text((60 * SS, 40 * SS), "Singapore's land area, 1960-2025", font=load_font(34 * SS), fill=CHART_TEXT)
    d.text((60 * SS, 86 * SS), "Square kilometres, end of each year; the axis starts at 550 km²",
           font=load_font(19 * SS, bold=False), fill=CHART_SECONDARY)

    def x(yr):
        return (X0 + (yr - y_first) * (X1 - X0) / (y_last - y_first)) * SS

    def y(v):
        return (Y1 - (v - YMIN) * (Y1 - Y0) / (YMAX - YMIN)) * SS

    tick = load_font(17 * SS, bold=False)
    for v in range(550, 761, 50):
        d.line([(X0 * SS, y(v)), (X1 * SS, y(v))], fill=(60, 60, 58), width=SS)
        d.text(((X0 - 14) * SS, y(v)), f"{v}", font=tick, fill=CHART_MUTED, anchor="rm")
    for yr in (1960, 1970, 1980, 1990, 2000, 2010, 2020):
        d.text((x(yr), (Y1 + 26) * SS), str(yr), font=tick, fill=CHART_MUTED, anchor="mm")
    d.line([(X0 * SS, Y1 * SS), (X1 * SS, Y1 * SS)], fill=CHART_MUTED, width=SS)
    d.line([(x(a), y(v)) for a, v in rows], fill=CHART_LINE, width=5 * SS, joint="curve")
    lab, val = load_font(18 * SS, bold=False), load_font(24 * SS)
    for yr, v, dx, anchor in [(rows[0][0], rows[0][1], 0, "lm"), (rows[-1][0], rows[-1][1], 0, "rm")]:
        cx, cy = x(yr), y(v)
        d.ellipse([cx - 8 * SS, cy - 8 * SS, cx + 8 * SS, cy + 8 * SS], fill=CHART_LINE, outline=CHART_BG, width=2 * SS)
        tx = cx + (16 * SS if anchor == "lm" else -16 * SS)
        d.text((tx, cy - 34 * SS), f"{v:.1f} km²", font=val, fill=CHART_TEXT, anchor=anchor)
        d.text((tx, cy + 30 * SS), str(yr), font=lab, fill=CHART_SECONDARY, anchor=anchor)
    d.text((60 * SS, 680 * SS), "Source: Singapore Land Authority, Total Land Area of Singapore (data.gov.sg). Offshore islands included.",
           font=load_font(15 * SS, bold=False), fill=CHART_MUTED)
    out = IMG / "singapore-land-area-chart.png"
    img.resize((W, H), Image.LANCZOS).save(out)
    print(f"wrote {out}  ({W}x{H})")


if __name__ == "__main__":
    main()
