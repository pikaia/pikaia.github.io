"""Render assets/images/opium-timeline-chart.png - the static PNG of the
opium-trade start-to-end timeline for the video/Watch "chart" slide.

Mirrors the post's inline .om-card timeline SVG exactly: era bands (blue =
privately farmed, green = government monopoly, hatched = banned/
criminalised) plus milestone ticks above/below the axis. compose_chart_frame()
only animates a single calendar-year line, so this Gantt-like timeline is
rendered once, near-full-frame (see docs/production-pipeline.md and
CLAUDE.md Charts). Coordinates are the inline SVG's own viewBox values
shifted by a fixed (60, 150) offset into the 1280x720 frame - deliberately
not re-derived, to avoid a fresh set of pixel-math mistakes.

    python scripts/render_opium_timeline_chart.py
"""
import sys
from pathlib import Path

from PIL import Image, ImageDraw

sys.path.insert(0, str(Path(__file__).resolve().parent))
from watch_video_lib import (  # noqa: E402
    CHART_BG, CHART_GRID, CHART_LINE, CHART_MUTED, CHART_SECONDARY, CHART_TEXT, load_font,
)

OUT = Path(__file__).resolve().parent.parent / "assets" / "images" / "opium-timeline-chart.png"
W, H = 1280, 720
SS = 2

SERIES_2 = (31, 166, 31)  # #1fa61f, the inline chart's dark-mode --series-2

TITLE = "Singapore's opium trade, start to end"
SUB = "1820 to 1951 – from a private tax farm to a state monopoly to a crime"
FOOT = "Dates from the sources cited below the post."

OX, OY = 60, 140  # offset from the inline SVG's own viewBox coordinates
VSCALE = 1.6  # stretches the inline chart's vertical spacing to fill more
              # of the 1280x720 frame (the raw SVG offset alone left too
              # much empty space below the timeline)


def p(x, y):
    return (OX + x) * SS, (OY + y * VSCALE) * SS


def render():
    w, h = W * SS, H * SS
    img = Image.new("RGB", (w, h), CHART_BG)
    d = ImageDraw.Draw(img)

    title_font = load_font(int(34 * SS))
    sub_font = load_font(int(19 * SS), bold=False)
    legend_font = load_font(int(17 * SS), bold=False)
    year_font = load_font(int(16 * SS))
    label_font = load_font(int(15 * SS), bold=False)
    axis_font = load_font(int(15 * SS), bold=False)
    foot_font = load_font(int(15 * SS), bold=False)

    margin = 60 * SS
    d.text((margin, 40 * SS), TITLE, font=title_font, fill=CHART_TEXT)
    d.text((margin, 84 * SS), SUB, font=sub_font, fill=CHART_SECONDARY)

    # legend
    ly = 118 * SS
    d.rectangle([margin, ly, margin + 22 * SS, ly + 10 * SS], fill=CHART_LINE)
    d.text((margin + 30 * SS, ly + 5 * SS), "Privately farmed (auctioned to the highest bidder)",
            font=legend_font, fill=CHART_SECONDARY, anchor="lm")
    lx2 = margin + 470 * SS
    d.rectangle([lx2, ly, lx2 + 22 * SS, ly + 10 * SS], fill=SERIES_2)
    d.text((lx2 + 30 * SS, ly + 5 * SS), "Government monopoly",
            font=legend_font, fill=CHART_SECONDARY, anchor="lm")
    lx3 = lx2 + 260 * SS
    hatch_box = [lx3, ly, lx3 + 22 * SS, ly + 10 * SS]
    d.rectangle(hatch_box, fill=CHART_GRID)
    for i in range(-10, 22, 4):
        d.line([(lx3 + i * SS, ly + 10 * SS), (lx3 + (i + 10) * SS, ly)], fill=CHART_MUTED, width=max(1, SS))
    d.rectangle(hatch_box, outline=CHART_MUTED, width=max(1, SS))
    d.text((lx3 + 30 * SS, ly + 5 * SS), "Banned / criminalised",
            font=legend_font, fill=CHART_SECONDARY, anchor="lm")

    # axis baseline
    d.line([p(60, 163), p(1100, 163)], fill=CHART_MUTED, width=max(1, SS))
    d.line([p(60, 177), p(1100, 177)], fill=CHART_MUTED, width=max(1, SS))
    for yr, x in [("1820", 97), ("1860", 320), ("1900", 617), ("1940", 915), ("1951", 1071)]:
        d.text(p(x, 200), yr, font=axis_font, fill=CHART_MUTED, anchor="mm")

    # era bands
    d.rectangle([p(97, 163), p(97 + 662, 177)], fill=CHART_LINE)
    d.rectangle([p(759, 163), p(759 + 275, 177)], fill=SERIES_2)
    hx0, hy0 = p(1034, 163)
    hx1, hy1 = p(1034 + 66, 177)
    d.rectangle([hx0, hy0, hx1, hy1], fill=CHART_GRID)
    step = 7 * SS
    xx = hx0 - (hy1 - hy0)
    while xx < hx1:
        d.line([(xx, hy1), (xx + (hy1 - hy0), hy0)], fill=CHART_MUTED, width=max(1, SS))
        xx += step

    # Great Syndicate range bracket, below baseline
    d.line([p(476, 177), p(476, 206), p(536, 206), p(536, 177)], fill=CHART_SECONDARY, width=max(1, SS))
    d.text(p(506, 222), "1871–79", font=year_font, fill=CHART_TEXT, anchor="mm")
    d.text(p(506, 237), "The Great Syndicate holds the", font=label_font, fill=CHART_SECONDARY, anchor="mm")
    d.text(p(506, 251), "Singapore, Johor, Melaka & Riau farms", font=label_font, fill=CHART_SECONDARY, anchor="mm")

    def milestone_above(x, year, line1, line2, dot_fill):
        d.line([p(x, 163), p(x, 140)], fill=CHART_SECONDARY, width=max(1, SS))
        cx, cy = p(x, 140)
        d.ellipse([cx - 4 * SS, cy - 4 * SS, cx + 4 * SS, cy + 4 * SS], fill=dot_fill)
        d.text(p(x, 130), year, font=year_font, fill=CHART_TEXT, anchor="mm")
        d.text(p(x, 116), line1, font=label_font, fill=CHART_SECONDARY, anchor="mm")
        d.text(p(x, 102), line2, font=label_font, fill=CHART_SECONDARY, anchor="mm")

    def milestone_below(x, year, line1, line2, dot_fill):
        d.line([p(x, 177), p(x, 255)], fill=CHART_SECONDARY, width=max(1, SS))
        cx, cy = p(x, 255)
        d.ellipse([cx - 4 * SS, cy - 4 * SS, cx + 4 * SS, cy + 4 * SS], fill=dot_fill)
        d.text(p(x, 271), year, font=year_font, fill=CHART_TEXT, anchor="mm")
        d.text(p(x, 286), line1, font=label_font, fill=CHART_SECONDARY, anchor="mm")
        d.text(p(x, 300), line2, font=label_font, fill=CHART_SECONDARY, anchor="mm")

    milestone_above(97, "1820", "Farm system", "introduced", CHART_LINE)
    milestone_above(751, "1907–09", "Commission; farm", "system ends", CHART_LINE)
    milestone_below(766, "1910", "Monopolies", "Dept formed", SERIES_2)
    milestone_above(877, "1925", "Reserve Fund", "begins wind-down", SERIES_2)
    milestone_below(915, "1930", "Pasir Panjang", "packing factory", SERIES_2)
    milestone_above(1023, "1943–46", "Banned, first by", "occupier then coloniser", CHART_SECONDARY)
    milestone_below(1071, "1951", "Consumption made", "a criminal offence", CHART_SECONDARY)

    d.text((margin, 680 * SS), FOOT, font=foot_font, fill=CHART_MUTED)

    img = img.resize((W, H), Image.LANCZOS)
    OUT.parent.mkdir(parents=True, exist_ok=True)
    img.save(OUT)
    print(f"wrote {OUT}  ({W}x{H})")


if __name__ == "__main__":
    render()
