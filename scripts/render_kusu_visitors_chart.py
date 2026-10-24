"""Render the static PNG for the Kusu Island post's video/Watch "chart" slide:

  assets/images/kusu-pilgrimage-visitors-chart.png  - visitors per pilgrimage
      season, 2019-2025, from the Singapore Land Authority's figures as
      reported by CNA in 2026 (the post's inline column chart). The two
      COVID-limited seasons are drawn lighter. Dark theme matching
      watch_video_lib's chart palette.

    python scripts/render_kusu_visitors_chart.py
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
COVID = tuple(int(c * 0.45 + b * 0.55) for c, b in zip(CHART_LINE[:3], CHART_BG[:3]))
X0, X1 = 110, 1220
Y0, Y1, VMAX = 150, 590, 34000

SEASONS = [
    (2019, 30000, False),
    (2020, 11200, True),
    (2021, 9400, True),
    (2022, 20000, False),
    (2023, 22500, False),
    (2024, 18500, False),
    (2025, 15500, False),
]


def main():
    img = Image.new("RGB", (W * SS, H * SS), CHART_BG)
    d = ImageDraw.Draw(img)
    d.text((60 * SS, 40 * SS), "Visitors to Kusu Island in the pilgrimage season", font=load_font(34 * SS), fill=CHART_TEXT)
    d.text((60 * SS, 86 * SS), "About half as many in 2025 as in 2019",
           font=load_font(19 * SS, bold=False), fill=CHART_SECONDARY)

    leg = load_font(17 * SS, bold=False)
    ly = 122 * SS
    d.rectangle([60 * SS, ly, 82 * SS, ly + 10 * SS], fill=CHART_LINE)
    d.text((90 * SS, ly + 5 * SS), "Visitors in the season", font=leg, fill=CHART_SECONDARY, anchor="lm")
    d.rectangle([300 * SS, ly, 322 * SS, ly + 10 * SS], fill=COVID)
    d.text((330 * SS, ly + 5 * SS), "Seasons with COVID-19 limits", font=leg, fill=CHART_SECONDARY, anchor="lm")

    def y(v):
        return (Y1 - v * (Y1 - Y0 - 20) / VMAX) * SS

    tick = load_font(16 * SS, bold=False)
    for t in (0, 10000, 20000, 30000):
        d.line([(X0 * SS, y(t)), (X1 * SS, y(t))], fill=CHART_MUTED if t == 0 else (60, 60, 58), width=SS)
        d.text(((X0 - 12) * SS, y(t)), f"{t:,}", font=tick, fill=CHART_MUTED, anchor="rm")

    slot = (X1 - X0) / len(SEASONS)
    bw = slot * 0.56
    val, yr = load_font(21 * SS), load_font(19 * SS, bold=False)
    for i, (year, v, covid) in enumerate(SEASONS):
        cx = X0 + slot * (i + 0.5)
        d.rounded_rectangle([(cx - bw / 2) * SS, y(v), (cx + bw / 2) * SS, Y1 * SS], radius=5 * SS,
                            fill=COVID if covid else CHART_LINE)
        d.rectangle([(cx - bw / 2) * SS, Y1 * SS - 5 * SS, (cx + bw / 2) * SS, Y1 * SS], fill=COVID if covid else CHART_LINE)
        d.text((cx * SS, y(v) - 14 * SS), f"about {v:,}", font=val, fill=CHART_TEXT, anchor="mb")
        d.text((cx * SS, (Y1 + 24) * SS), str(year), font=yr, fill=CHART_SECONDARY, anchor="mm")

    d.text((60 * SS, 680 * SS), "Source: Singapore Land Authority figures, reported by CNA, 2026.",
           font=load_font(15 * SS, bold=False), fill=CHART_MUTED)
    out = IMG / "kusu-pilgrimage-visitors-chart.png"
    img.resize((W, H), Image.LANCZOS).save(out)
    print(f"wrote {out}  ({W}x{H})")


if __name__ == "__main__":
    main()
