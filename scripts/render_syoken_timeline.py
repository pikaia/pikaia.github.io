"""Timeline of the Occupation's government lotteries, for the Syonan Syoken post.

One axis (1942-1946) with the Occupation and the run of monthly Konan Saiken
issues shaded, and dated events as dots with labels staggered on four levels
(two above the axis, two below) so neighbours never overlap. Events sit at
fractional-year positions and carry their own date label. The same EVENTS
drive both outputs:

  python scripts/render_syoken_timeline.py        # assets/images/syoken-timeline-chart.png
                                                  # (dark-theme 1280x720 video/Watch slide)
  python scripts/render_syoken_timeline.py --svg  # prints the post's inline card HTML

Dates are from the Syonan Times and Syonan Shimbun (via NewspaperSG) and the
National Library Board. Layout and drawing follow render_orang_laut_timeline.py;
the card's style and hover script are shared with the 1867 transfer timeline.
"""
import sys
from pathlib import Path

from PIL import Image, ImageDraw

sys.path.insert(0, str(Path(__file__).resolve().parent))
from render_transfer_timeline import SCRIPT, STYLE  # noqa: E402
from watch_video_lib import (  # noqa: E402
    CHART_BG, CHART_LINE, CHART_MUTED, CHART_SECONDARY, CHART_TEXT, load_font,
)

OUT = Path(__file__).resolve().parent.parent / "assets" / "images" / "syoken-timeline-chart.png"
TITLE = "The Occupation's government lotteries"
SUB = "From the first million-dollar draw to the 27th monthly issue"
FOOT = "Sources: Syonan Times and Syonan Shimbun, 1942-1945, via NewspaperSG; National Library Board."
Y0, Y1 = 1942, 1946
TICK = 1

# (position, date label, label line 1, label line 2, level, anchor, tooltip). Levels: -2, -1 above the axis, 1, 2 below.
EVENTS = [
    (1942.12, "Feb 1942", "Singapore", "falls", 1, "start", "Singapore falls to Japan on 15 February 1942 and is renamed Syonan."),
    (1942.41, "May 1942", "A $1 million", "lottery announced", -1, "start", "On 29 May the military administration announces a $1,000,000 lottery to raise revenue and absorb spending money."),
    (1942.48, "Jun 1942", "The $50 million", "'gift' handed over", 2, "start", "On 25 June Chinese leaders hand over the $50 million demanded of the community."),
    (1942.69, "Sep 1942", "Syonan Syoken", "drawn", -2, "start", "On 10 September the million tickets are drawn at the old Victoria Theatre; the first prize is $100,000."),
    (1943.30, "1943", "Monthly Konan", "Saiken begins", 1, "start", "A Malaya-wide government lottery, sold in monthly issues of 300,000 to 400,000 tickets at $1."),
    (1945.42, "Jun 1945", "Engo Saiken", "at $5 a ticket", -2, "end", "A second 'relief lottery' is on sale at $5 a ticket alongside the monthly Konan Saiken."),
    (1945.51, "Jul 1945", "25th Konan", "Saiken drawn", 1, "end", "The 25th issue, 500,000 tickets, is drawn at the Kokaido on 5 July 1945."),
    (1945.62, "Aug 1945", "Japan", "surrenders", -1, "end", "Japan surrenders on 15 August 1945, while the 27th issue is on sale."),
    (1945.68, "Sep 1945", "27th draw", "was due", 2, "end", "The 27th issue was due to be drawn on 5 September 1945, the day British troops returned."),
]
BANDS = [  # (from, to, label, kind)
    (1942.12, 1945.68, "Japanese Occupation", "war"),
    (1943.30, 1945.68, "Monthly Konan Saiken", "bank"),
]


def _decades():
    below = [e[0] for e in EVENTS if e[4] > 0]
    return [y for y in range(Y0, Y1 + 1, TICK) if all(abs(y - b) > 0.1 for b in below)]


def _layout(x0, x1):
    sx = lambda y: x0 + (y - Y0) / (Y1 - Y0) * (x1 - x0)  # noqa: E731
    return sx


def render_png():
    W, H, SS = 1280, 720, 2
    img = Image.new("RGB", (W * SS, H * SS), CHART_BG)
    d = ImageDraw.Draw(img)
    d.text((60 * SS, 40 * SS), TITLE, font=load_font(34 * SS), fill=CHART_TEXT)
    d.text((60 * SS, 84 * SS), SUB, font=load_font(19 * SS, bold=False), fill=CHART_SECONDARY)
    d.text((60 * SS, 680 * SS), FOOT, font=load_font(14 * SS, bold=False), fill=CHART_MUTED)
    sx = _layout(90, 1190)
    ax = 395
    lev = {-2: 175, -1: 270, 1: 520, 2: 615}
    colours = {"bank": (28, 52, 82), "war": (90, 90, 88)}
    for a, b, _, kind in BANDS:
        top, bot = (ax - 30, ax + 30) if kind == "bank" else (ax - 44, ax + 44)
        d.rectangle([sx(a) * SS, top * SS, sx(b) * SS, bot * SS], fill=colours[kind])
    # Band legend, top right under the subtitle.
    lx, ly0 = 60, 128
    for _, _, lab, kind in BANDS:
        d.rectangle([lx * SS, (ly0 - 8) * SS, (lx + 16) * SS, (ly0 + 8) * SS], fill=colours[kind])
        d.text(((lx + 24) * SS, ly0 * SS), lab, font=load_font(15 * SS, bold=False), fill=CHART_SECONDARY, anchor="lm")
        lx += 24 + d.textlength(lab, font=load_font(15 * SS, bold=False)) / SS + 36
    d.line([(sx(Y0) * SS, ax * SS), (sx(Y1) * SS, ax * SS)], fill=CHART_MUTED, width=2 * SS)
    for y in range(Y0, Y1 + 1, TICK):
        d.line([(sx(y) * SS, (ax - 5) * SS), (sx(y) * SS, (ax + 5) * SS)], fill=CHART_MUTED, width=SS)
    for y in _decades():
        d.text((sx(y) * SS, (ax + 58) * SS), str(y), font=load_font(14 * SS, bold=False), fill=CHART_MUTED, anchor="mm")
    fy, fl = load_font(20 * SS), load_font(16 * SS, bold=False)
    for yr, dl, l1, l2, lv, an, _ in EVENTS:
        x, ly = sx(yr), lev[lv]
        d.line([(x * SS, ax * SS), (x * SS, (ly + (34 if lv < 0 else -26)) * SS)], fill=CHART_MUTED, width=SS)
        d.ellipse([(x - 7) * SS, (ax - 7) * SS, (x + 7) * SS, (ax + 7) * SS], fill=CHART_BG, outline=CHART_LINE, width=3 * SS)
        anc = {"start": "l", "end": "r", "middle": "m"}[an]
        tx = x - 4 if anc == "l" else (x + 4 if anc == "r" else x)
        d.text((tx * SS, (ly - 22) * SS), dl, font=fy, fill=CHART_TEXT, anchor=anc + "m")
        d.text((tx * SS, ly * SS), l1, font=fl, fill=CHART_SECONDARY, anchor=anc + "m")
        d.text((tx * SS, (ly + 20) * SS), l2, font=fl, fill=CHART_SECONDARY, anchor=anc + "m")
    img.resize((W, H), Image.LANCZOS).save(OUT)
    print("wrote", OUT)


def svg_card():
    sx = _layout(30, 770)
    ax = 160
    lev = {-2: 30, -1: 80, 1: 232, 2: 282}
    h = 322
    s = [f'<svg viewBox="0 0 800 {h}" width="100%" height="auto" role="img" aria-label="Timeline from {Y0} to {Y1}. '
         + " ".join(f"{dl}: {l1} {l2}." for _, dl, l1, l2, _, _, _ in EVENTS)
         + "".join(f" Shaded: {lab}." for _, _, lab, _ in BANDS) + '">']
    for a, b, _, kind in BANDS:
        top, bot = (ax - 20, ax + 20) if kind == "bank" else (ax - 28, ax + 28)
        var = "--band-bank" if kind == "bank" else "--band-war"
        s.append(f'  <rect x="{sx(a):.1f}" y="{top}" width="{sx(b) - sx(a):.1f}" height="{bot - top}" rx="3" fill="var({var})"/>')
    s.append(f'  <line x1="{sx(Y0):.1f}" y1="{ax}" x2="{sx(Y1):.1f}" y2="{ax}" stroke="var(--axis)" stroke-width="1.5"/>')
    for y in range(Y0, Y1 + 1, TICK):
        s.append(f'  <line x1="{sx(y):.1f}" y1="{ax - 4}" x2="{sx(y):.1f}" y2="{ax + 4}" stroke="var(--axis)"/>')
    for y in _decades():
        s.append(f'  <text class="lt-axis" x="{sx(y):.1f}" y="{ax + 44}" text-anchor="middle">{y}</text>')
    for yr, dl, l1, l2, lv, anc, tip in EVENTS:
        x, ly = sx(yr), lev[lv]
        tx = x - 3 if anc == "start" else (x + 3 if anc == "end" else x)
        stem_end = ly + 22 if lv < 0 else ly - 26
        s.append(f'  <g class="lt-hit" tabindex="0" data-label="{dl}: {l1} {l2}" data-val="{tip}">'
                 f'<rect x="{x - 40:.1f}" y="{min(ly - 30, ax - 8)}" width="80" height="{abs(ax - ly) + 40}" fill="transparent"/>'
                 f'<line x1="{x:.1f}" y1="{ax}" x2="{x:.1f}" y2="{stem_end}" stroke="var(--axis)"/>'
                 f'<circle class="lt-dot" cx="{x:.1f}" cy="{ax}" r="5"/>'
                 f'<text class="lt-year" x="{tx:.1f}" y="{ly - 12}" text-anchor="{anc}">{dl}</text>'
                 f'<text class="lt-lab" x="{tx:.1f}" y="{ly + 2}" text-anchor="{anc}">{l1}</text>'
                 f'<text class="lt-lab" x="{tx:.1f}" y="{ly + 15}" text-anchor="{anc}">{l2}</text></g>')
    s.append("</svg>")
    rows = "\n".join(f"        <tr><td>{dl}</td><td>{tip}</td></tr>" for _, dl, _, _, _, _, tip in EVENTS)
    legend = "\n".join(
        f'    <span><i class="lt-swatch" style="background: var({"--band-bank" if kind == "bank" else "--band-war"})"></i>{lab}</span>'
        for _, _, lab, kind in BANDS)
    print(STYLE + f"""
<div class="lt-card">
  <p class="lt-title">{TITLE}</p>
  <p class="lt-subtitle">{SUB}</p>
  <div class="lt-legend">
{legend}
  </div>
  <div class="lt-chart-wrap">
{chr(10).join("    " + line for line in s)}
    <div class="lt-tooltip"></div>
  </div>
  <p class="lt-foot">{FOOT}</p>
  <details class="lt-details">
    <summary>View as table</summary>
    <table class="lt-table">
      <thead><tr><th>Date</th><th>Event</th></tr></thead>
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
