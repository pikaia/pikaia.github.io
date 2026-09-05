"""Render assets/images/when-singapore-had-wild-tigers-timeline.png - the
static PNG of the tiger-encounters timeline for the video / Watch slide.

Mirrors the post's inline SVG: eight point-events on a year-linear axis
(1831-1930), labels alternating above and below the line, in
watch_video_lib's dark chart palette. The two documented hunts (1928,
1930) are marked in a second colour. Rendered once, near-full-frame
(compose_chart_frame() only animates a data line - see
docs/production-pipeline.md and CLAUDE.md Charts).

Committed binary, same documented exception as the OSM maps / other
chart PNGs.

    python scripts/render_when_singapore_had_wild_tigers_timeline.py
"""
import sys
from pathlib import Path

from PIL import Image, ImageDraw

sys.path.insert(0, str(Path(__file__).resolve().parent))
from watch_video_lib import (  # noqa: E402
    CHART_BG, CHART_GRID, CHART_MUTED, CHART_SECONDARY, CHART_TEXT, load_font,
)

OUT = (Path(__file__).resolve().parent.parent / "assets" / "images"
       / "when-singapore-had-wild-tigers-timeline.png")
W, H = 1280, 720
SS = 2

TITLE = "A century of tigers, 1831–1930"
FOOT = ("Sources as for the video. The axis is linear in years; the two blue markers are the "
        "documented hunts. Not every recorded encounter is shown.")

X_MIN, X_MAX = 1826, 1940
HUNT_C = (109, 168, 224)     # the 1928 and 1930 hunts
TOLL_C = (214, 140, 66)      # the running toll over the decades

# pos, year label, description, side ("above"/"below"), level (0 = near axis, 1 = far)
EVENTS = [
    (1831, "1831", "First recorded tiger attack", "below", 0),
    (1839, "1839", "Two labourers taken near Rangong Road", "above", 0),
    (1857, "1857", "~300 deaths believed; 7 reported", "below", 1),
    (1859, "1859", "Village near Bukit Timah abandoned; patrols begin", "above", 1),
    (1890, "1890", "A man killed on Thomson Road", "below", 0),
    (1902, "1902", "Escaped circus tiger shot at Raffles Hotel", "above", 0),
    (1928, "1928", "Hunting party shoots a tiger, Pasir Panjang", "below", 1),
    (1930, "1930", "The last wild tiger, Choa Chu Kang", "above", 1),
]


def render():
    w, h = W * SS, H * SS
    img = Image.new("RGB", (w, h), CHART_BG)
    d = ImageDraw.Draw(img)

    title_font = load_font(int(34 * SS), bold=True)
    year_font = load_font(int(23 * SS), bold=True)
    label_font = load_font(int(18 * SS), bold=False)
    foot_font = load_font(int(15 * SS), bold=False)

    margin = 60 * SS
    d.text((margin, 44 * SS), TITLE, font=title_font, fill=CHART_TEXT)

    left, right = 90 * SS, (W - 70) * SS
    axis_y = 360 * SS
    d.line([(left, axis_y), (right, axis_y)], fill=CHART_MUTED, width=max(2, 2 * SS))

    def x_of(yr):
        return left + (yr - X_MIN) / (X_MAX - X_MIN) * (right - left)

    for pos, ytext, label, side, lvl in EVENTS:
        x = x_of(pos)
        dot_c = HUNT_C if pos in (1928, 1930) else TOLL_C
        if side == "above":
            conn_end = axis_y - (150 if lvl else 80) * SS
            y_year = conn_end - 40 * SS
            y_label = conn_end - 12 * SS
        else:
            conn_end = axis_y + (150 if lvl else 80) * SS
            y_year = conn_end + 8 * SS
            y_label = conn_end + 38 * SS
        d.line([(x, axis_y), (x, conn_end)], fill=CHART_GRID, width=max(1, SS))
        r = (10 if pos == 1930 else 8) * SS
        d.ellipse([x - r, axis_y - r, x + r, axis_y + r],
                  fill=dot_c, outline=CHART_BG, width=max(1, 2 * SS))
        anchor = "ls" if pos < 1836 else ("rs" if pos > 1924 else "ms")
        d.text((x, y_year), ytext, font=year_font, fill=CHART_TEXT, anchor=anchor)
        d.text((x, y_label), label, font=label_font, fill=CHART_SECONDARY, anchor=anchor)

    d.text((margin, 686 * SS), FOOT, font=foot_font, fill=CHART_MUTED)

    img = img.resize((W, H), Image.LANCZOS)
    OUT.parent.mkdir(parents=True, exist_ok=True)
    img.save(OUT)
    print(f"wrote {OUT}  ({W}x{H})")


if __name__ == "__main__":
    render()
