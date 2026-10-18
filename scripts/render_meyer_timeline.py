"""Timeline of Sir Manasseh Meyer's life and legacy, for the Manasseh Meyer post.

One axis (1840-2030) with his years as a Municipal Commissioner and the Japanese
Occupation shaded, and dated events as dots with labels staggered on four levels
(two above the axis, two below) so neighbours never overlap. The same EVENTS
drive both outputs:

  python scripts/render_meyer_timeline.py        # assets/images/meyer-timeline-chart.png
                                                 # (dark-theme 1280x720 video/Watch slide)
  python scripts/render_meyer_timeline.py --svg  # prints the post's inline card HTML

Dates are from W. Makepeace (1921), the Straits Times (1929, 1930, 1949), NLB
Infopedia, the Einstein Papers and Roots.gov.sg. Layout and drawing follow
render_katong_timeline.py.
"""
import sys
from pathlib import Path

from PIL import Image, ImageDraw

sys.path.insert(0, str(Path(__file__).resolve().parent))
from render_transfer_timeline import SCRIPT, STYLE  # noqa: E402
from watch_video_lib import (  # noqa: E402
    CHART_BG, CHART_LINE, CHART_MUTED, CHART_SECONDARY, CHART_TEXT, load_font,
)

OUT = Path(__file__).resolve().parent.parent / "assets" / "images" / "meyer-timeline-chart.png"
TITLE = "Sir Manasseh Meyer and what he left, 1861-2016"
SUB = "A trader turned landlord, two synagogues, and the institutions that still carry his name"
FOOT = "Sources: W. Makepeace (1921); Straits Times (1929, 1930, 1949); NLB Infopedia; Einstein Papers; Roots.gov.sg."
Y0, Y1 = 1840, 2030
TICK = 20

# (position, date label, label line 1, label line 2, level, anchor, tooltip). Levels: -2, -1 above the axis, 1, 2 below.
EVENTS = [
    (1861, "1861", "Arrives from", "Calcutta, aged 15", -1, "start", "Manasseh Meyer, born in Baghdad in 1846 and schooled in Calcutta, first comes to Singapore in 1861 and studies at St Joseph's Institution."),
    (1873, "1873", "Founds Meyer", "Brothers", 2, "end", "After six years trading in Rangoon, he returns and founds the import and export firm Meyer Brothers, which grows into the largest local firm in the India trade."),
    (1878, "1878", "Maghain Aboth", "synagogue opens", 1, "start", "The Maghain Aboth synagogue on Waterloo Street opens on 4 April 1878, after Meyer persuades the government to let the community sell its old Synagogue Street building."),
    (1890, "1890", "Buys Killiney House:", "Belle Vue", -2, "start", "Five years after his first property purchase, he buys Killiney House at Oxley Rise, built in 1842 for the surgeon Thomas Oxley, and makes it his family home, Belle Vue. His largest purchases come in 1890-92."),
    (1905, "1905", "Chesed-El", "opens", -1, "start", "His private synagogue, Chesed-El, built at his own cost in the grounds of Belle Vue, is dedicated on 14 April 1905."),
    (1922, "1922", "Hosts Einstein", "at Belle Vue", 2, "start", "On 2 November 1922 about 300 guests hear Albert Einstein speak at Belle Vue, at a reception for the Hebrew University in Jerusalem."),
    (1929, "1929", "Knighted", "", -2, "start", "He is made a Knight Bachelor for public services and benevolence, the only honour given to Malaya in that year's New Year list."),
    (1930, "1930", "Dies at", "Belle Vue, aged 84", 1, "start", "He dies at his house in Oxley Rise on 1 July 1930. His will endows the synagogue and his Hebrew school with rents from six houses."),
    (1949, "1949", "Estate offered", "for sale: $6m", -1, "start", "The Meyer estate's properties, worth about six million dollars, are offered for sale to wind up the estate; auctions follow in 1950."),
    (1998, "1998", "Both synagogues", "national monuments", 1, "end", "Maghain Aboth (27 February) and Chesed-El (18 December) are gazetted as national monuments."),
    (2009, "2009", "Manasseh Meyer", "Building: monument", -1, "end", "The Manasseh Meyer Building, paid for by his $150,000 gift to Raffles College, is gazetted with five other former Raffles College buildings."),
    (2016, "2016", "School named after", "him moves to Sembawang", 2, "end", "The Jewish nursery started in 1996 becomes the Sir Manasseh Meyer International School and moves to a campus in Sembawang."),
]
BANDS = [  # (from, to, label, kind)
    (1893, 1900, "Municipal Commissioner", "bank"),
    (1942, 1945, "Japanese Occupation", "war"),
]


def _ticks():
    """(year, side) for every tick label. A label next to a below-axis stem is
    nudged to the far side of it (side -1/+1) instead of being dropped, which
    left gaps in the axis on the Ya'acob timeline."""
    below = [e[0] for e in EVENTS if e[4] > 0]
    out = []
    for y in range(Y0, Y1 + 1, TICK):
        near = [b for b in below if abs(y - b) <= (Y1 - Y0) * 0.016]
        out.append((y, 0 if not near else (-1 if near[0] > y else 1)))
    return out


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
    for y, side in _ticks():
        d.text(((sx(y) + side * 22) * SS, (ax + 58) * SS), str(y), font=load_font(14 * SS, bold=False), fill=CHART_MUTED, anchor="mm")
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
    for y, side in _ticks():
        s.append(f'  <text class="lt-axis" x="{sx(y) + side * 16:.1f}" y="{ax + 44}" text-anchor="middle">{y}</text>')
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
