"""Timeline of Thomas Dunman's life, for the Thomas Dunman post.

One axis (1810-1890) with his years in the police shaded, and dated events
as dots with labels staggered on four levels (two above the axis, two below)
so neighbours never overlap. Events sit at fractional-year positions and carry
their own date label. The same EVENTS drive both outputs:

  python scripts/render_dunman_timeline.py        # assets/images/dunman-timeline-chart.png
                                                  # (dark-theme 1280x720 video/Watch slide)
  python scripts/render_dunman_timeline.py --svg  # prints the post's inline card HTML

Dates are from C. B. Buckley's Anecdotal History of Old Times in Singapore
(1902), BiblioAsia's police history (2015), the Singapore Police Force and
Wikipedia. Layout and drawing follow render_thomson_timeline.py.
"""
import sys
from pathlib import Path

from PIL import Image, ImageDraw

sys.path.insert(0, str(Path(__file__).resolve().parent))
from render_transfer_timeline import SCRIPT, STYLE  # noqa: E402
from watch_video_lib import (  # noqa: E402
    CHART_BG, CHART_LINE, CHART_MUTED, CHART_SECONDARY, CHART_TEXT, load_font,
)

OUT = Path(__file__).resolve().parent.parent / "assets" / "images" / "dunman-timeline-chart.png"
TITLE = "Thomas Dunman, 1814-1887"
SUB = "A merchant's clerk who ran Singapore's police for 28 years"
FOOT = "Sources: C. B. Buckley, An Anecdotal History of Old Times in Singapore (1902); BiblioAsia (2015); Singapore Police Force; Wikipedia."
Y0, Y1 = 1810, 1890
TICK = 10

# (position, date label, label line 1, label line 2, level, anchor, tooltip). Levels: -2, -1 above the axis, 1, 2 below.
EVENTS = [
    (1814.5, "1814", "Born in", "England", -1, "start", "Born in England in 1814."),
    (1840.5, "1840", "Clerk at", "Martin Dyce & Co.", 1, "end", "Comes to Singapore as an assistant in the merchant firm Martin Dyce & Co."),
    (1843.7, "1843", "Takes charge", "of the police", -2, "end", "After a public meeting on crime in February, the government appoints him Deputy Magistrate and Superintendent of Police."),
    (1846.8, "1846", "First police rules", "and uniforms", 2, "end", "The first rules and regulations for the force are issued in October 1846, with uniforms for the Indian and Malay constables."),
    (1854.35, "May 1854", "Hokkien-Teochew", "riots", -1, "start", "Riots between Hokkien and Teochew Chinese last ten to twelve days; Governor Butterworth later gives Dunman a sword."),
    (1857.4, "1857", "First full-time", "Commissioner", 1, "start", "Under the Police Act of 1856 the post of Commissioner of Police is separated from the Resident Councillor's, and Dunman takes it."),
    (1865.8, "1865", "Tanglin Club", "founded", -2, "start", "He presides over the interim committee that founds the Tanglin Club."),
    (1871.5, "1871", "Retires from", "the police", 2, "start", "Retires on a pension after 28 years in charge of the force."),
    (1875.5, "1875", "Leaves for", "England", -1, "start", "After four years on his coconut plantation at Tanjong Katong, he retires to England."),
    (1887.8, "1887", "Dies at", "Bournemouth", 1, "end", "Dies at Bournemouth in England in October 1887, aged 73."),
]
BANDS = [  # (from, to, label, kind)
    (1843.7, 1871.5, "In charge of the police", "bank"),
]


def _ticks():
    below = [e[0] for e in EVENTS if e[4] > 0]
    return [y for y in range(Y0, Y1 + 1, TICK) if all(abs(y - b) > 1.2 for b in below)]


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
    colours = {"bank": (28, 52, 82), "war": (60, 72, 60)}
    for a, b, _, kind in BANDS:
        d.rectangle([sx(a) * SS, (ax - 30) * SS, sx(b) * SS, (ax + 30) * SS], fill=colours[kind])
    # Band legend, under the subtitle.
    lx, ly0 = 60, 128
    for _, _, lab, kind in BANDS:
        d.rectangle([lx * SS, (ly0 - 8) * SS, (lx + 16) * SS, (ly0 + 8) * SS], fill=colours[kind])
        d.text(((lx + 24) * SS, ly0 * SS), lab, font=load_font(15 * SS, bold=False), fill=CHART_SECONDARY, anchor="lm")
        lx += 24 + d.textlength(lab, font=load_font(15 * SS, bold=False)) / SS + 36
    d.line([(sx(Y0) * SS, ax * SS), (sx(Y1) * SS, ax * SS)], fill=CHART_MUTED, width=2 * SS)
    for y in range(Y0, Y1 + 1, TICK):
        d.line([(sx(y) * SS, (ax - 5) * SS), (sx(y) * SS, (ax + 5) * SS)], fill=CHART_MUTED, width=SS)
    for y in _ticks():
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
        var = "--band-bank" if kind == "bank" else "--band-war"
        s.append(f'  <rect x="{sx(a):.1f}" y="{ax - 20}" width="{sx(b) - sx(a):.1f}" height="40" rx="3" fill="var({var})"/>')
    s.append(f'  <line x1="{sx(Y0):.1f}" y1="{ax}" x2="{sx(Y1):.1f}" y2="{ax}" stroke="var(--axis)" stroke-width="1.5"/>')
    for y in range(Y0, Y1 + 1, TICK):
        s.append(f'  <line x1="{sx(y):.1f}" y1="{ax - 4}" x2="{sx(y):.1f}" y2="{ax + 4}" stroke="var(--axis)"/>')
    for y in _ticks():
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
