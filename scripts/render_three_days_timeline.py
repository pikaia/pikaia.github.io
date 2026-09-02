"""Render assets/images/three-days-stock-exchange-shut-1985-timeline.png -
the static PNG of the Pan-Electric timeline for the video / Watch slide.

Mirrors the post's inline .pe-timeline SVG: five point-events on a
year-linear axis (1984-2001), labels alternating above and below the
line, in watch_video_lib's dark chart palette. Rendered once,
near-full-frame (compose_chart_frame() only animates a data line - see
docs/production-pipeline.md and CLAUDE.md Charts).

Committed binary, same documented exception as the OSM maps / other
chart PNGs.

    python scripts/render_three_days_timeline.py
"""
import sys
from pathlib import Path

from PIL import Image, ImageDraw

sys.path.insert(0, str(Path(__file__).resolve().parent))
from watch_video_lib import (  # noqa: E402
    CHART_BG, CHART_GRID, CHART_LINE, CHART_MUTED, CHART_SECONDARY, CHART_TEXT, load_font,
)

OUT = (Path(__file__).resolve().parent.parent / "assets" / "images"
       / "three-days-stock-exchange-shut-1985-timeline.png")
W, H = 1280, 720
SS = 2

TITLE = "From the shutdown to the CLOB freeze"
FOOT = ("Sources as for the video. The axis is linear in years; the December 1985 shutdown "
        "lasted three trading days.")

X_MIN, X_MAX = 1984, 2001

# pos, year label, description, side ("above"/"below"), level (0 = near axis, 1 = far)
EVENTS = [
    (1985.9, "Dec 1985", "Both exchanges shut for three days", "above", 1),
    (1986.4, "1986", "Tan Koon Swan jailed; Securities Industry Act", "below", 1),
    (1990.0, "Jan 1990", "CLOB opens for Malaysian shares", "above", 0),
    (1998.7, "Sep 1998", "Malaysia freezes CLOB (~172,000 investors)", "below", 0),
    (2000.1, "Feb 2000", "Frozen shares released in stages", "above", 1),
]


def render():
    w, h = W * SS, H * SS
    img = Image.new("RGB", (w, h), CHART_BG)
    d = ImageDraw.Draw(img)

    title_font = load_font(int(34 * SS), bold=True)
    year_font = load_font(int(23 * SS), bold=True)
    label_font = load_font(int(19 * SS), bold=False)
    foot_font = load_font(int(15 * SS), bold=False)

    margin = 60 * SS
    d.text((margin, 44 * SS), TITLE, font=title_font, fill=CHART_TEXT)

    left, right = 110 * SS, (W - 80) * SS
    axis_y = 360 * SS
    d.line([(left, axis_y), (right, axis_y)], fill=CHART_MUTED, width=max(2, 2 * SS))

    def x_of(yr):
        return left + (yr - X_MIN) / (X_MAX - X_MIN) * (right - left)

    for pos, ytext, label, side, lvl in EVENTS:
        x = x_of(pos)
        if side == "above":
            conn_end = axis_y - (150 if lvl else 80) * SS
            y_year = conn_end - 40 * SS
            y_label = conn_end - 12 * SS
        else:
            conn_end = axis_y + (150 if lvl else 80) * SS
            y_year = conn_end + 8 * SS
            y_label = conn_end + 38 * SS
        d.line([(x, axis_y), (x, conn_end)], fill=CHART_GRID, width=max(1, SS))
        d.ellipse([x - 8 * SS, axis_y - 8 * SS, x + 8 * SS, axis_y + 8 * SS],
                  fill=CHART_LINE, outline=CHART_BG, width=max(1, 2 * SS))
        anchor = "ls" if pos < 1987 else ("rs" if pos > 1999 else "ms")
        d.text((x, y_year), ytext, font=year_font, fill=CHART_TEXT, anchor=anchor)
        d.text((x, y_label), label, font=label_font, fill=CHART_SECONDARY, anchor=anchor)

    d.text((margin, 686 * SS), FOOT, font=foot_font, fill=CHART_MUTED)

    img = img.resize((W, H), Image.LANCZOS)
    OUT.parent.mkdir(parents=True, exist_ok=True)
    img.save(OUT)
    print(f"wrote {OUT}  ({W}x{H})")


if __name__ == "__main__":
    render()
