"""Where each $1 lottery ticket went, for the Syonan Syoken post.

Two stacked horizontal bars on one scale (cents of each $1 ticket): the
first government lottery, Syonan Syoken (1942: $300,000 of prizes on
$1,000,000 of tickets, the $700,000 balance announced for charity and
health), and the fourth monthly issue of Konan Saiken (1943: $240,000 of
prizes on $400,000 of tickets). Figures from the Syonan Times of 23 July
and 3 October 1942 and the Syonan Shimbun of 31 July 1943, via NewspaperSG.

    python scripts/render_syoken_dollar_chart.py          # assets/images/syoken-dollar-chart.png (dark video slide)
    python scripts/render_syoken_dollar_chart.py --svg    # prints the post's inline card HTML
"""
import sys
from pathlib import Path

from PIL import Image, ImageDraw

sys.path.insert(0, str(Path(__file__).resolve().parent))
from render_gift_chart import SCRIPT, STYLE  # noqa: E402
from watch_video_lib import (  # noqa: E402
    CHART_BG, CHART_GRID, CHART_MUTED, CHART_SECONDARY, CHART_TEXT, load_font,
)

OUT = Path(__file__).resolve().parent.parent / "assets" / "images" / "syoken-dollar-chart.png"
TITLE = "Where each $1 lottery ticket went"
SUB = "Cents of every dollar of tickets sold"
FOOT = "Sources: Syonan Times, 23 July and 3 October 1942; Syonan Shimbun, 31 July 1943 (NewspaperSG)."
VMAX = 100

# (row label, [(cents, colour key, segment label, tooltip)])
ROWS = [
    ("Syonan Syoken, 1942", [(30, "a", "Prizes 30c", "$300,000 in 62 prizes on $1,000,000 of tickets"),
                             (70, "b", "Charity and health 70c", "The $700,000 balance, announced for four charity and health bodies")]),
    ("Konan Saiken, 1943", [(60, "a", "Prizes 60c", "$240,000 in 3,239 prizes on 400,000 tickets (fourth issue)"),
                            (40, "neutral", "Rest 40c", "The other $160,000 of the issue; the tickets named health facilities and refugee relief as its causes")]),
]
PNG_COL = {"neutral": (110, 108, 102), "a": (57, 135, 229), "b": (31, 166, 31)}
SVG_VAR = {"neutral": "--neutral", "a": "--series-1", "b": "--series-2"}


def render_png():
    W, H, SS = 1280, 720, 2
    img = Image.new("RGB", (W * SS, H * SS), CHART_BG)
    d = ImageDraw.Draw(img)
    d.text((60 * SS, 40 * SS), TITLE, font=load_font(34 * SS), fill=CHART_TEXT)
    d.text((60 * SS, 84 * SS), SUB, font=load_font(19 * SS, bold=False), fill=CHART_SECONDARY)
    d.text((60 * SS, 680 * SS), FOOT, font=load_font(14 * SS, bold=False), fill=CHART_MUTED)
    x0, x1, top = 330, 1200, 200
    sx = lambda v: (x0 + v / VMAX * (x1 - x0)) * SS  # noqa: E731
    f, fl = load_font(15 * SS, bold=False), load_font(20 * SS)
    for v in range(0, VMAX + 1, 20):
        d.line([(sx(v), (top - 30) * SS), (sx(v), 560 * SS)], fill=CHART_GRID if v else CHART_MUTED, width=SS)
        d.text((sx(v), 590 * SS), f"{v}c", font=f, fill=CHART_MUTED, anchor="mm")
    rowh = 190
    for i, (lab, segs) in enumerate(ROWS):
        cy = top + 60 + i * rowh
        d.text(((x0 - 18) * SS, cy * SS), lab, font=fl, fill=CHART_TEXT, anchor="rm")
        acc = 0
        for v, key, seg, _ in segs:
            a, b = sx(acc) + (2 * SS if acc else 0), sx(acc + v)
            d.rectangle([a, (cy - 34) * SS, b, (cy + 34) * SS], fill=PNG_COL[key])
            d.text(((a + b) / 2, cy * SS), seg, font=load_font(20 * SS), fill=CHART_BG, anchor="mm")
            acc += v
    img.resize((W, H), Image.LANCZOS).save(OUT)
    print("wrote", OUT)


def svg_card():
    x0, x1, top, rowh = 170, 770, 24, 70
    sx = lambda v: x0 + v / VMAX * (x1 - x0)  # noqa: E731
    h = top + rowh * len(ROWS) + 30
    aria = ("Stacked bar chart in cents of each one-dollar ticket. Syonan Syoken, 1942: 30 cents in prizes and 70 cents "
            "announced for charity and health. Konan Saiken fourth issue, 1943: 60 cents in prizes and 40 cents left over for the administration.")
    s = [f'<svg viewBox="0 0 800 {h}" width="100%" height="auto" role="img" aria-label="{aria}">']
    for v in range(0, VMAX + 1, 20):
        s.append(f'  <line x1="{sx(v):.1f}" y1="{top - 10}" x2="{sx(v):.1f}" y2="{top + rowh * len(ROWS) - 20}" stroke="var({"--axis" if v == 0 else "--grid"})"/>')
        s.append(f'  <text class="gc-axis" x="{sx(v):.1f}" y="{top + rowh * len(ROWS) - 4}" text-anchor="middle">{v}c</text>')
    for i, (lab, segs) in enumerate(ROWS):
        cy = top + 14 + i * rowh
        s.append(f'  <text class="gc-row" x="{x0 - 10}" y="{cy + 5}" text-anchor="end">{lab}</text>')
        acc = 0
        for v, key, seg, tip in segs:
            gap = 2 if acc else 0
            s.append(f'  <g class="gc-hit" tabindex="0" data-label="{seg}" data-val="{tip}">'
                     f'<rect x="{sx(acc) + gap:.1f}" y="{cy - 15}" width="{sx(acc + v) - sx(acc) - gap:.1f}" height="30" rx="3" fill="var({SVG_VAR[key]})"/>'
                     f'<text class="gc-in" x="{(sx(acc) + sx(acc + v)) / 2:.1f}" y="{cy + 5}" text-anchor="middle">{seg}</text></g>')
            acc += v
    s.append("</svg>")
    rows = "\n".join(f"        <tr><td>{lab}</td><td>{seg}</td><td>{tip}</td></tr>" for lab, segs in ROWS for _, _, seg, tip in segs)
    print(STYLE + f"""
<div class="gc-card">
  <p class="gc-title">{TITLE}</p>
  <p class="gc-subtitle">{SUB}</p>
  <div class="gc-legend">
    <span><i class="gc-swatch" style="background: var(--series-1)"></i>Paid out in prizes</span>
    <span><i class="gc-swatch" style="background: var(--series-2)"></i>Announced for charity and health</span>
    <span><i class="gc-swatch" style="background: var(--neutral)"></i>Rest of the takings</span>
  </div>
  <div class="gc-chart-wrap">
{chr(10).join("    " + line for line in s)}
    <div class="gc-tooltip"></div>
  </div>
  <p class="gc-foot">{FOOT}</p>
  <details class="gc-details">
    <summary>View as table</summary>
    <table class="gc-table">
      <thead><tr><th>Lottery</th><th>Part</th><th>Detail</th></tr></thead>
      <tbody>
{rows}
      </tbody>
    </table>
  </details>
</div>
""" + SCRIPT + "\n</div>")


if __name__ == "__main__":
    if "--svg" in sys.argv:
        svg_card()
    else:
        render_png()
