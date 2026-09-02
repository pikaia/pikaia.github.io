"""Render assets/images/three-days-stock-exchange-shut-1985-forward.png -
the static PNG explaining the forward-contract mechanism at the centre of
the Pan-Electric crisis, for the video / Watch slide.

Mirrors the post's inline .pe-forward diagram: the setup (sell now, agree
to buy back later at a fixed price) and the fork - the price rises (the
bet works) versus the price falls (1985, the loss lands somewhere). Dark
theme matching watch_video_lib's chart palette, rendered once,
near-full-frame.

Committed binary, same documented exception as the OSM maps / other
chart PNGs.

    python scripts/render_three_days_forward_contract.py
"""
import sys
from pathlib import Path

from PIL import Image, ImageDraw

sys.path.insert(0, str(Path(__file__).resolve().parent))
from watch_video_lib import (  # noqa: E402
    CHART_BG, CHART_GRID, CHART_LINE, CHART_MUTED, CHART_SECONDARY, CHART_TEXT, load_font,
)

OUT = (Path(__file__).resolve().parent.parent / "assets" / "images"
       / "three-days-stock-exchange-shut-1985-forward.png")
W, H = 1280, 720
SS = 2

TITLE = "How a forward contract held the share price up"
FOOT = ("Pan-Electric's contracts were unusually large and mostly undisclosed, so the losses "
        "stayed hidden until it failed. Sources: MAS Staff Paper No. 32 (2004); SAL (2022).")


def _outcome_box(d, xy, title, lines, title_font, body_font, accent):
    x0, y0, x1, y1 = xy
    head_h = 46 * SS
    d.rounded_rectangle([x0, y0, x1, y1], radius=12 * SS,
                        outline=CHART_LINE if accent else CHART_GRID,
                        width=(3 if accent else 2) * SS)
    d.rounded_rectangle([x0, y0, x1, y0 + head_h + 12 * SS], radius=12 * SS,
                        fill=CHART_LINE if accent else CHART_GRID)
    d.rectangle([x0, y0 + head_h - 6 * SS, x1, y0 + head_h + 12 * SS],
                fill=CHART_LINE if accent else CHART_GRID)
    d.text(((x0 + x1) / 2, y0 + head_h / 2), title, font=title_font,
           fill=CHART_TEXT if accent else CHART_SECONDARY, anchor="mm")
    step = 40 * SS
    block_h = step * len(lines)
    ty = y0 + head_h + 12 * SS + ((y1 - y0 - head_h - 12 * SS) - block_h) / 2 + step / 2
    for ln in lines:
        d.text((x0 + 26 * SS, ty), ln, font=body_font, fill=CHART_TEXT, anchor="lm")
        ty += step


def _harrow(d, x0, y, x1, label, font, below=False):
    d.line([(x0, y), (x1, y)], fill=CHART_SECONDARY, width=2 * SS)
    dirn = 1 if x1 > x0 else -1
    d.polygon([(x1, y), (x1 - dirn * 13 * SS, y - 7 * SS), (x1 - dirn * 13 * SS, y + 7 * SS)],
              fill=CHART_SECONDARY)
    d.text(((x0 + x1) / 2, y + (16 if below else -16) * SS), label,
           font=font, fill=CHART_MUTED, anchor="mm")


def render():
    w, h = W * SS, H * SS
    img = Image.new("RGB", (w, h), CHART_BG)
    d = ImageDraw.Draw(img)

    title_font = load_font(int(33 * SS), bold=True)
    box_title_font = load_font(int(20 * SS), bold=True)
    body_font = load_font(int(20 * SS), bold=False)
    note_font = load_font(int(19 * SS), bold=False)
    foot_font = load_font(int(15 * SS), bold=False)

    margin = 60 * SS
    d.text((margin, 40 * SS), TITLE, font=title_font, fill=CHART_TEXT)

    # --- setup row: shareholder <-> broking firm ---
    top = 140 * SS
    bw, bh = 290 * SS, 88 * SS
    sh_x0 = margin
    bf_x1 = (W - 60) * SS
    bf_x0 = bf_x1 - bw
    for x0, label in ((sh_x0, "Shareholder"), (bf_x0, "Broking firm")):
        d.rounded_rectangle([x0, top, x0 + bw, top + bh], radius=12 * SS,
                            outline=CHART_SECONDARY, width=2 * SS)
        d.text((x0 + bw / 2, top + bh / 2), label, font=box_title_font, fill=CHART_TEXT, anchor="mm")

    _harrow(d, sh_x0 + bw + 16 * SS, top + 26 * SS, bf_x0 - 16 * SS,
            "sells a block of shares now", note_font, below=False)
    _harrow(d, bf_x0 - 16 * SS, top + bh - 26 * SS, sh_x0 + bw + 16 * SS,
            "pays cash now", note_font, below=True)

    note_y = top + bh + 44 * SS
    d.text((W * SS / 2, note_y),
           "…and the shareholder agrees to buy the shares back in a few months, "
           "at a price fixed today.",
           font=note_font, fill=CHART_SECONDARY, anchor="mm")

    # --- fork into the two outcomes ---
    box_y0 = note_y + 54 * SS
    box_y1 = box_y0 + 250 * SS
    gap = 48 * SS
    left = (margin, box_y0, W * SS / 2 - gap / 2, box_y1)
    right = (W * SS / 2 + gap / 2, box_y0, (W - 60) * SS, box_y1)
    lc = (left[0] + left[2]) / 2
    rc = (right[0] + right[2]) / 2

    d.line([(W * SS / 2, note_y + 16 * SS), (W * SS / 2, note_y + 32 * SS)], fill=CHART_GRID, width=2 * SS)
    d.line([(lc, note_y + 32 * SS), (rc, note_y + 32 * SS)], fill=CHART_GRID, width=2 * SS)
    d.line([(lc, note_y + 32 * SS), (lc, box_y0)], fill=CHART_GRID, width=2 * SS)
    d.line([(rc, note_y + 32 * SS), (rc, box_y0)], fill=CHART_GRID, width=2 * SS)

    _outcome_box(d, left, "If the price RISES  —  the bet works",
                 ["Buy the shares back below the",
                  "fixed price, and pocket the difference.",
                  "The downside looked small."],
                 box_title_font, body_font, accent=False)
    _outcome_box(d, right, "If the price FALLS  —  1985",
                 ["Buy back above the market price.",
                  "The loss lands on whoever is left",
                  "holding the shares."],
                 box_title_font, body_font, accent=True)

    d.text((margin, 676 * SS), FOOT, font=foot_font, fill=CHART_MUTED)

    img = img.resize((W, H), Image.LANCZOS)
    OUT.parent.mkdir(parents=True, exist_ok=True)
    img.save(OUT)
    print(f"wrote {OUT}  ({W}x{H})")


if __name__ == "__main__":
    render()
