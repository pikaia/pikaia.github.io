"""Render the rickshaw-men post's "rickshaws registered" chart to a static
PNG for use as a video / Watch-widget slide.

The post's inline chart is a single-series line over a year-linear x-axis
(six years for which a count survives, 1883 to 1947). This renders the
same series once, in the pipeline's dark chart theme, to
assets/images/rickshaw-registered.png (1280x720, drawn 2x and downscaled
for crisp text).

Captions are no longer burned into the main video (see
docs/production-pipeline.md section 6), so the plot uses close to the
full frame - a normal ~40-60px video margin all round, plus a little
extra at the bottom (content ends ~y=680 of 720) so YouTube's own
caption overlay, when a viewer toggles it on, doesn't bury the x-axis.

Re-run if the figures change; the output is a committed binary (same
documented exception as the other chart PNGs and the OSM map tiles).

    python scripts/render_the_rickshaw_men_and_the_jinricksha_station_chart.py
"""
import sys
from pathlib import Path

from PIL import Image, ImageDraw

sys.path.insert(0, str(Path(__file__).resolve().parent))
from watch_video_lib import (  # noqa: E402
    CHART_BG, CHART_GRID, CHART_LINE, CHART_MUTED, CHART_SECONDARY, CHART_TEXT, load_font,
)

OUT = Path(__file__).resolve().parent.parent / "assets" / "images" / "rickshaw-registered.png"
W, H = 1280, 720
SS = 2

TITLE = "Rickshaws registered in Singapore, 1883–1947"
SUBTITLE = "Points mark the years for which a count survives; the early-1920s peak is an estimate."
FOOT = ("Sources: Singapore municipal administration reports; James Francis Warren, "
        "Rickshaw Coolie: A People's History of Singapore, 1880–1940.")

# (year, rickshaws registered, label or None)
DATA = [
    (1883, 2000, "2,000"),
    (1893, 13000, None),
    (1902, 22629, "22,629"),
    (1920, 29500, "≈ 30,000  (early 1920s)"),
    (1940, 3693, "3,693"),
    (1947, 0, "0 — banned"),
]
YEAR_MIN, YEAR_MAX = 1879, 1951
Y_MAX = 32000
GRID = [0, 10000, 20000, 30000]


def render():
    w, h = W * SS, H * SS
    img = Image.new("RGB", (w, h), CHART_BG)
    d = ImageDraw.Draw(img)

    title_font = load_font(int(36 * SS), bold=True)
    sub_font = load_font(int(20 * SS), bold=False)
    tick_font = load_font(int(18 * SS), bold=False)
    anno_font = load_font(int(20 * SS), bold=False)
    anno_strong = load_font(int(22 * SS), bold=True)
    foot_font = load_font(int(16 * SS), bold=False)

    margin = 70 * SS
    d.text((margin, 40 * SS), TITLE, font=title_font, fill=CHART_TEXT)
    d.text((margin, 88 * SS), SUBTITLE, font=sub_font, fill=CHART_SECONDARY)

    plot_l, plot_r = 150 * SS, 1180 * SS
    plot_t, plot_b = 150 * SS, 600 * SS

    def x_of(year):
        return plot_l + (year - YEAR_MIN) / (YEAR_MAX - YEAR_MIN) * (plot_r - plot_l)

    def y_of(val):
        return plot_t + (Y_MAX - val) / Y_MAX * (plot_b - plot_t)

    for g in GRID:
        gy = y_of(g)
        d.line([(plot_l, gy), (plot_r, gy)], fill=CHART_GRID, width=max(1, SS))
        d.text((plot_l - 14 * SS, gy), f"{g:,}", font=tick_font, fill=CHART_MUTED, anchor="rm")

    for yr in (1880, 1900, 1920, 1940):
        gx = x_of(yr)
        d.text((gx, plot_b + 24 * SS), str(yr), font=tick_font, fill=CHART_MUTED, anchor="mm")

    pts = [(x_of(y), y_of(v)) for y, v, _ in DATA]
    d.line(pts, fill=CHART_LINE, width=max(2, 4 * SS), joint="curve")

    for (yr, val, lab), (px, py) in zip(DATA, pts):
        r = 8 * SS if yr == 1920 else 6 * SS
        d.ellipse([px - r, py - r, px + r, py + r], fill=CHART_LINE)
        d.ellipse([px - r, py - r, px + r, py + r], outline=CHART_BG, width=max(1, 2 * SS))
        if not lab:
            continue
        strong = yr in (1920, 1947)
        font = anno_strong if strong else anno_font
        fill = CHART_TEXT if strong else CHART_SECONDARY
        if yr == 1883:
            d.text((px + 14 * SS, py + 4 * SS), lab, font=font, fill=fill, anchor="lm")
        elif yr == 1902:
            d.text((px, py - 20 * SS), lab, font=font, fill=fill, anchor="mb")
        elif yr == 1920:
            d.text((px, py - 22 * SS), lab, font=font, fill=fill, anchor="mb")
        elif yr == 1940:
            d.text((px - 14 * SS, py - 10 * SS), lab, font=font, fill=fill, anchor="rb")
        elif yr == 1947:
            d.text((px - 14 * SS, py - 14 * SS), lab, font=font, fill=fill, anchor="rb")

    fb = d.textbbox((0, 0), FOOT, font=foot_font)
    d.text((margin, 680 * SS - (fb[3] - fb[1])), FOOT, font=foot_font, fill=CHART_MUTED)

    img = img.resize((W, H), Image.LANCZOS)
    OUT.parent.mkdir(parents=True, exist_ok=True)
    img.save(OUT, optimize=True)
    print(f"wrote {OUT}  ({W}x{H})")


if __name__ == "__main__":
    render()
