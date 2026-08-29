"""Render the SkillsFuture post's credit-uptake chart to a static PNG for
use as a video / Watch-widget slide.

The post's chart is a two-series line comparison (the 2015 Opening
Credit vs the 2020 top-up) on a "years since the scheme began" x-axis.
compose_chart_frame() animates a single calendar-year line and can't
overlay two lines, so this renders it once, in the pipeline's dark
chart theme, to assets/images/skillsfuture-uptake.png (1280x720, drawn
2x and downscaled for crisp text).

Re-run if the figures change; the output is a committed binary (same
documented exception as the route-walk OSM tiles and the other two
chart PNGs).

    python scripts/render_skillsfuture_uptake_chart.py
"""
import sys
from pathlib import Path

from PIL import Image, ImageDraw

sys.path.insert(0, str(Path(__file__).resolve().parent))
from watch_video_lib import (  # noqa: E402
    CHART_BG, CHART_TEXT, CHART_SECONDARY, CHART_MUTED, CHART_GRID, load_font,
)

OUT = Path(__file__).resolve().parent.parent / "assets" / "images" / "skillsfuture-uptake.png"
W, H = 1280, 720
SS = 2

TITLE = "Patience compounds. A deadline caps."
SUBTITLE = ("Share of eligible Singaporeans who have used their SkillsFuture Credit, "
            "by years since each scheme began")
FOOT = ("The top-up was slightly ahead until it expired at year 5. The open-ended "
        "Opening Credit just kept adding users.")

OPENING_COL = (57, 135, 229)   # blue
TOPUP_COL = (46, 160, 67)      # green

# (years since introduction, % of eligible who have used the credit)
OPENING = [(0, 0), (4, 20), (7, 29), (10, 52)]
TOPUP = [(0, 0), (4, 26), (5, 30)]        # last point = expired end-2025

X_MAX, Y_MAX = 10, 60
Y_STEP = 15


def render():
    w, h = W * SS, H * SS
    img = Image.new("RGB", (w, h), CHART_BG)
    d = ImageDraw.Draw(img)

    title_font = load_font(int(35 * SS), bold=True)
    sub_font = load_font(int(19 * SS), bold=False)
    legend_font = load_font(int(19 * SS), bold=False)
    tick_font = load_font(int(19 * SS), bold=False)
    end_font = load_font(int(22 * SS), bold=True)
    foot_font = load_font(int(18 * SS), bold=False)

    margin = 70 * SS
    d.text((margin, 40 * SS), TITLE, font=title_font, fill=CHART_TEXT)
    d.text((margin, 84 * SS), SUBTITLE, font=sub_font, fill=CHART_SECONDARY)

    # legend
    lx, ly = margin, 128 * SS
    for col, lab in ((OPENING_COL, "Opening Credit (2015, no expiry)"),
                     (TOPUP_COL, "2020 top-up ($500, expired end-2025)")):
        d.line([(lx, ly + 8 * SS), (lx + 26 * SS, ly + 8 * SS)], fill=col, width=max(2, 3 * SS))
        d.text((lx + 34 * SS, ly + 8 * SS), lab, font=legend_font, fill=CHART_SECONDARY, anchor="lm")
        lx += (46 + len(lab) * 10) * SS

    left, right = 120 * SS, 1130 * SS
    top, bot = 180 * SS, 590 * SS

    def sx(yr):
        return left + yr / X_MAX * (right - left)

    def sy(pct):
        return bot - pct / Y_MAX * (bot - top)

    # y gridlines + ticks
    v = 0
    while v <= Y_MAX:
        y = sy(v)
        d.line([(left, y), (right, y)], fill=CHART_GRID, width=max(1, SS))
        d.text((left - 14 * SS, y), f"{v}%", font=tick_font, fill=CHART_MUTED, anchor="rm")
        v += Y_STEP

    # x ticks at the years the data actually marks
    for yr in (0, 4, 7, 10):
        d.text((sx(yr), bot + 26 * SS), f"Year {yr}", font=tick_font, fill=CHART_MUTED, anchor="mm")

    # lines
    d.line([(sx(x), sy(y)) for x, y in OPENING], fill=OPENING_COL, width=max(2, 3 * SS), joint="curve")
    d.line([(sx(x), sy(y)) for x, y in TOPUP], fill=TOPUP_COL, width=max(2, 3 * SS), joint="curve")

    for x, y in OPENING:
        d.ellipse([sx(x) - 5 * SS, sy(y) - 5 * SS, sx(x) + 5 * SS, sy(y) + 5 * SS],
                  fill=OPENING_COL, outline=CHART_BG, width=max(1, SS))
    for x, y in TOPUP[:-1]:
        d.ellipse([sx(x) - 5 * SS, sy(y) - 5 * SS, sx(x) + 5 * SS, sy(y) + 5 * SS],
                  fill=TOPUP_COL, outline=CHART_BG, width=max(1, SS))
    # the expiry point: hollow marker
    ex, ey = sx(TOPUP[-1][0]), sy(TOPUP[-1][1])
    d.ellipse([ex - 7 * SS, ey - 7 * SS, ex + 7 * SS, ey + 7 * SS],
              fill=CHART_BG, outline=TOPUP_COL, width=max(2, 2 * SS))

    # end labels
    ox, oy = sx(OPENING[-1][0]), sy(OPENING[-1][1])
    d.text((ox - 10 * SS, oy - 22 * SS), "52%+ (2025)", font=end_font, fill=CHART_TEXT, anchor="rb")
    d.text((ex, ey + 30 * SS), "30%, expired", font=end_font, fill=CHART_TEXT, anchor="mm")

    d.text((margin, (H - 44) * SS), FOOT, font=foot_font, fill=CHART_MUTED)

    img = img.resize((W, H), Image.LANCZOS)
    OUT.parent.mkdir(parents=True, exist_ok=True)
    img.save(OUT)
    print(f"wrote {OUT}  ({W}x{H})")


if __name__ == "__main__":
    render()
