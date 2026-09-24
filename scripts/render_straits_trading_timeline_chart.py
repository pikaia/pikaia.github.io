"""Render assets/images/straits-trading-timeline-chart.png - the static PNG of
the Straits Trading Company timeline for the video/Watch "chart" slide.

Mirrors the post's inline .om-card timeline SVG (two era bands - tin
smelting, then diversified conglomerate - plus nine milestone ticks). Same
approach as render_opium_timeline_chart.py: the inline SVG's own viewBox
coordinates, shifted/stretched into the 1280x720 frame rather than
re-derived. compose_chart_frame() only animates a single calendar-year line,
so this is rendered once, near-full-frame.

    python scripts/render_straits_trading_timeline_chart.py
"""
import sys
from pathlib import Path

from PIL import Image, ImageDraw

sys.path.insert(0, str(Path(__file__).resolve().parent))
from watch_video_lib import (  # noqa: E402
    CHART_BG, CHART_LINE, CHART_MUTED, CHART_SECONDARY, CHART_TEXT, load_font,
)

OUT = Path(__file__).resolve().parent.parent / "assets" / "images" / "straits-trading-timeline-chart.png"
W, H = 1280, 720
SS = 2

SERIES_2 = (31, 166, 31)  # #1fa61f, the inline chart's dark-mode --series-2

TITLE = "From Pulau Brani to a listed conglomerate"
SUB = "1887 to today – a tin smelter that became something else entirely"
FOOT = "Dates from the sources cited below the post."

OX, OY = 60, -60
VSCALE = 2.0


def p(x, y):
    return (OX + x) * SS, (OY + y * VSCALE) * SS


def render():
    img = Image.new("RGB", (W * SS, H * SS), CHART_BG)
    d = ImageDraw.Draw(img)

    title_font = load_font(int(34 * SS))
    sub_font = load_font(int(19 * SS), bold=False)
    legend_font = load_font(int(17 * SS), bold=False)
    year_font = load_font(int(17 * SS))
    label_font = load_font(int(16 * SS), bold=False)
    axis_font = load_font(int(15 * SS), bold=False)
    foot_font = load_font(int(15 * SS), bold=False)

    margin = 60 * SS
    d.text((margin, 40 * SS), TITLE, font=title_font, fill=CHART_TEXT)
    d.text((margin, 84 * SS), SUB, font=sub_font, fill=CHART_SECONDARY)

    ly = 118 * SS
    d.rectangle([margin, ly, margin + 22 * SS, ly + 10 * SS], fill=CHART_LINE)
    d.text((margin + 30 * SS, ly + 5 * SS), "Tin smelting era", font=legend_font, fill=CHART_SECONDARY, anchor="lm")
    lx2 = margin + 240 * SS
    d.rectangle([lx2, ly, lx2 + 22 * SS, ly + 10 * SS], fill=SERIES_2)
    d.text((lx2 + 30 * SS, ly + 5 * SS), "Diversified conglomerate era", font=legend_font,
           fill=CHART_SECONDARY, anchor="lm")

    d.line([p(60, 200), p(1100, 200)], fill=CHART_MUTED, width=max(1, SS))
    d.line([p(60, 214), p(1100, 214)], fill=CHART_MUTED, width=max(1, SS))
    for yr, x in [("1887", 97), ("1920", 328), ("1955", 573), ("1990", 819), ("Today", 1071)]:
        d.text(p(x, 237), yr, font=axis_font, fill=CHART_MUTED, anchor="mm")

    d.rectangle([p(97, 200), p(97 + 666, 214)], fill=CHART_LINE)
    d.rectangle([p(763, 200), p(763 + 337, 214)], fill=SERIES_2)

    def above(x, year, top, mid, dot):
        d.line([p(x, 200), p(x, 170)], fill=CHART_SECONDARY, width=max(1, SS))
        cx, cy = p(x, 170)
        d.ellipse([cx - 4 * SS, cy - 4 * SS, cx + 4 * SS, cy + 4 * SS], fill=dot)
        d.text(p(x, 160), year, font=year_font, fill=CHART_TEXT, anchor="mm")
        d.text(p(x, 146), mid, font=label_font, fill=CHART_SECONDARY, anchor="mm")
        d.text(p(x, 132), top, font=label_font, fill=CHART_SECONDARY, anchor="mm")

    def below(x, year, l1, l2, dot):
        d.line([p(x, 214), p(x, 255)], fill=CHART_SECONDARY, width=max(1, SS))
        cx, cy = p(x, 255)
        d.ellipse([cx - 4 * SS, cy - 4 * SS, cx + 4 * SS, cy + 4 * SS], fill=dot)
        d.text(p(x, 271), year, font=year_font, fill=CHART_TEXT, anchor="mm")
        d.text(p(x, 286), l1, font=label_font, fill=CHART_SECONDARY, anchor="mm")
        d.text(p(x, 300), l2, font=label_font, fill=CHART_SECONDARY, anchor="mm")

    above(97, "1887", "Company", "incorporated", CHART_LINE)
    below(118, "1890", "Pulau Brani", "smelter opens", CHART_LINE)
    above(272, "1912", "Two-thirds of Malaya's", "world's tin", CHART_LINE)
    below(489, "1941–46", "Destroyed, then", "rebuilt after", CHART_LINE)
    above(665, "late 1960s", "Leaves Pulau Brani", "for naval base", CHART_LINE)
    below(763, "1982", "Spun into Malaysia", "Smelting Corp", SERIES_2)
    above(868, "1997", "Rendezvous", "hotels launch", SERIES_2)
    below(945, "2008", "Tecity Group takes", "majority stake", SERIES_2)
    above(1071, "Today", "Three-division", "conglomerate", SERIES_2)

    d.text((margin, 680 * SS), FOOT, font=foot_font, fill=CHART_MUTED)

    img = img.resize((W, H), Image.LANCZOS)
    OUT.parent.mkdir(parents=True, exist_ok=True)
    img.save(OUT)
    print(f"wrote {OUT}  ({W}x{H})")


if __name__ == "__main__":
    render()
