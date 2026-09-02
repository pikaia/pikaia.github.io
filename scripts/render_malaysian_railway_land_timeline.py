"""Render assets/images/malaysian-railway-land-timeline.png - the static
PNG of the 1903-to-present timeline for the video / Watch "chart" slide.

Mirrors the post's inline .rail-timeline SVG: eight point-events on a
year-linear axis, labels alternating above and below the line, in
watch_video_lib's dark chart palette. Rendered once, near-full-frame
(compose_chart_frame() only animates a data line - see
docs/production-pipeline.md and CLAUDE.md Charts).

Committed binary, same documented exception as the OSM maps / other
chart PNGs.

    python scripts/render_malaysian_railway_land_timeline.py
"""
import sys
from pathlib import Path

from PIL import Image, ImageDraw

sys.path.insert(0, str(Path(__file__).resolve().parent))
from watch_video_lib import (  # noqa: E402
    CHART_BG, CHART_GRID, CHART_LINE, CHART_MUTED, CHART_SECONDARY, CHART_TEXT, load_font,
)

OUT = Path(__file__).resolve().parent.parent / "assets" / "images" / "malaysian-railway-land-timeline.png"
W, H = 1280, 720
SS = 2

TITLE = "A line of ground through Singapore, 1903 to the present"
FOOT = ("Sources as for the video. The axis is linear in years; \"2010-11\" and \"2021-27\" each cover a "
        "pair of closely spaced events.")

X_MIN, X_MAX = 1900, 2032

# pos, year label, description, side ("above"/"below"), level (0 = near axis, 1 = far)
EVENTS = [
    (1903, "1903", "Railway reaches Singapore", "above", 1),
    (1918, "1918", "999-year lease to the FMSR", "below", 1),
    (1932, "1932", "Tanjong Pagar terminus opens", "above", 0),
    (1965, "1965", "Separation; the land stays with KTM", "below", 0),
    (1990, "1990", "Points of Agreement signed", "above", 1),
    (1998, "1998", "Checkpoints split at Woodlands", "below", 1),
    (2010.5, "2010-11", "Land swap; the last train", "above", 0),
    (2024, "2021-27", "HSR scrapped; RTS Link due", "below", 0),
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

    left, right = 90 * SS, (W - 60) * SS
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
        anchor = "ls" if pos < 1912 else ("rs" if pos > 2022 else "ms")
        d.text((x, y_year), ytext, font=year_font, fill=CHART_TEXT, anchor=anchor)
        d.text((x, y_label), label, font=label_font, fill=CHART_SECONDARY, anchor=anchor)

    d.text((margin, 686 * SS), FOOT, font=foot_font, fill=CHART_MUTED)

    img = img.resize((W, H), Image.LANCZOS)
    OUT.parent.mkdir(parents=True, exist_ok=True)
    img.save(OUT)
    print(f"wrote {OUT}  ({W}x{H})")


if __name__ == "__main__":
    render()
