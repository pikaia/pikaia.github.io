"""Render the Tekong post's population chart to a static PNG for use as a
video / Watch-widget slide.

The post's chart is a 3-point line (4,169 in 1957 -> ~8,000 in the 1980s
-> 0 by the late 1980s) on a non-numeric x-axis ("1957" / "1980s (peak)"
/ "Late 1980s"). It's rendered once here, in the pipeline's dark chart
theme, to assets/images/tekong-population.png (1280x720, drawn 2x and
downscaled for crisp text).

Re-run if the figures change; the output is a committed binary (same
documented exception as the route-walk OSM tiles and the other chart
PNGs).

    python scripts/render_tekong_population_chart.py
"""
import sys
from pathlib import Path

from PIL import Image, ImageDraw

sys.path.insert(0, str(Path(__file__).resolve().parent))
from watch_video_lib import (  # noqa: E402
    CHART_BG, CHART_LINE, CHART_TEXT, CHART_SECONDARY, CHART_MUTED, CHART_GRID, load_font,
)

OUT = Path(__file__).resolve().parent.parent / "assets" / "images" / "tekong-population.png"
W, H = 1280, 720
SS = 2

TITLE = "From 8,000 residents to zero"
SUBTITLE = "Pulau Tekong's population, before it became a military training island"
FOOT = ("In roughly three decades, Tekong went from a growing multi-ethnic settlement "
        "to militarised land with no civilian residents at all.")

# (x-label, population, data-label)
POINTS = [
    ("1957", 4169, "4,169"),
    ("1980s (peak)", 8000, "~8,000"),
    ("Late 1980s", 0, "0"),
]
Y_MAX, Y_STEP = 8000, 2000


def render():
    w, h = W * SS, H * SS
    img = Image.new("RGB", (w, h), CHART_BG)
    d = ImageDraw.Draw(img, "RGBA")

    title_font = load_font(int(36 * SS), bold=True)
    sub_font = load_font(int(20 * SS), bold=False)
    tick_font = load_font(int(19 * SS), bold=False)
    dot_font = load_font(int(23 * SS), bold=True)
    foot_font = load_font(int(18 * SS), bold=False)

    margin = 70 * SS
    d.text((margin, 44 * SS), TITLE, font=title_font, fill=CHART_TEXT)
    d.text((margin, 90 * SS), SUBTITLE, font=sub_font, fill=CHART_SECONDARY)

    left, right = 150 * SS, 1130 * SS
    top, bot = 190 * SS, 580 * SS

    def sx(i):
        return left + i / (len(POINTS) - 1) * (right - left)

    def sy(v):
        return bot - v / Y_MAX * (bot - top)

    v = 0
    while v <= Y_MAX:
        y = sy(v)
        d.line([(left, y), (right, y)], fill=CHART_GRID, width=max(1, SS))
        d.text((left - 16 * SS, y), f"{v:,}", font=tick_font, fill=CHART_MUTED, anchor="rm")
        v += Y_STEP

    for i, (lab, _, _) in enumerate(POINTS):
        d.text((sx(i), bot + 28 * SS), lab, font=tick_font, fill=CHART_MUTED, anchor="mm")

    pts = [(sx(i), sy(p)) for i, (_, p, _) in enumerate(POINTS)]
    # area fill under the line
    d.polygon(pts + [(pts[-1][0], sy(0)), (pts[0][0], sy(0))], fill=CHART_LINE[:3] + (28,))
    d.line(pts, fill=CHART_LINE, width=max(2, 3 * SS), joint="curve")

    for (px, py), (_, _, dl) in zip(pts, POINTS):
        d.ellipse([px - 6 * SS, py - 6 * SS, px + 6 * SS, py + 6 * SS],
                  fill=CHART_LINE, outline=CHART_BG, width=max(1, 2 * SS))
        above = py > top + 40 * SS
        d.text((px, py - 18 * SS if above else py + 18 * SS), dl, font=dot_font,
               fill=CHART_TEXT, anchor="mb" if above else "mt")

    d.text((margin, (H - 44) * SS), FOOT, font=foot_font, fill=CHART_MUTED)

    img = img.resize((W, H), Image.LANCZOS)
    OUT.parent.mkdir(parents=True, exist_ok=True)
    img.save(OUT)
    print(f"wrote {OUT}  ({W}x{H})")


if __name__ == "__main__":
    render()
