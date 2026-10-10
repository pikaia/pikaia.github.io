"""Timeline of P. Govindasamy Pillai's life and business, for the PGP post.

One year axis (1900-2020) with the years he ran the business shaded and the
Japanese Occupation marked, and dated events as dots with labels staggered on
four levels (two above the axis, two below) so neighbours never overlap. The
same EVENTS drive both outputs:

  python scripts/render_pgp_timeline.py          # assets/images/pgp-timeline-chart.png
                                                 # (dark-theme 1280x720 video/Watch slide)
  python scripts/render_pgp_timeline.py --svg    # prints the post's inline card HTML

Dates are from NLB Infopedia (Sitragandi Arunasalam, "P. Govindasamy Pillai"),
Roots.gov.sg and the Singapore Memory Project. The card's style and hover script
are shared with the 1867 transfer timeline.
"""
import sys
from pathlib import Path

from PIL import Image, ImageDraw

sys.path.insert(0, str(Path(__file__).resolve().parent))
from render_transfer_timeline import SCRIPT, STYLE  # noqa: E402
from watch_video_lib import (  # noqa: E402
    CHART_BG, CHART_LINE, CHART_MUTED, CHART_SECONDARY, CHART_TEXT, load_font,
)

OUT = Path(__file__).resolve().parent.parent / "assets" / "images" / "pgp-timeline-chart.png"
TITLE = "From shop boy to retail pioneer"
SUB = "P. Govindasamy Pillai's life, his business, and the stores that carried his name"
FOOT = "Sources: NLB Infopedia; Roots.gov.sg (National Heritage Board); Singapore Memory Project."
Y0, Y1 = 1900, 2020
TICK = 10

# (year, label line 1, label line 2, level, anchor, tooltip). Levels: -2, -1 above the axis, 1, 2 below.
EVENTS = [
    (1905, "Lands at", "Tanjong Pagar", -1, "start", "Arrives as a teenage runaway and finds work for food and board at a provision store at 50 Serangoon Road."),
    (1929, "Buys the shop on", "a $2,000 loan", 1, "middle", "The owner dies and the shop is put up for sale; he buys it with $2,000 borrowed from Chettiar moneylenders."),
    (1937, "Indian Chamber", "of Commerce", -1, "middle", "A founder-member of the Indian Chamber of Commerce, set up this year."),
    (1939, "Justice of", "the Peace", 2, "middle", "Appointed a Justice of the Peace."),
    (1945, "Starts again", "after the war", -2, "middle", "Back from India after the Japanese Occupation, in which he lost his property and goods, he rebuilds the business."),
    (1952, "Ramakrishna", "Mission home", 1, "middle", "A new home for the Ramakrishna Mission is built at Bartley Road with his donation."),
    (1963, "Retires; $3m", "to his children", -1, "middle", "He retires and hands the family business, valued at S$3 million, to his children."),
    (1965, "PGP Hall", "opens", 2, "middle", "The wedding hall he funded at the Sri Srinivasa Perumal Temple is opened on 19 June 1965."),
    (1979, "Temple gopuram", "completed", -1, "middle", "The temple's five-tier gopuram, which he funded at a cost of $300,000, is completed."),
    (1980, "Dies,", "aged 93", 1, "middle", "He dies of a heart attack on 21 July 1980."),
    (1998, "PGP stores", "close", -2, "middle", "Run by his daughter-in-law after his youngest son's death, the stores run into heavy debts and close."),
    (2001, "Postage", "stamps", 2, "middle", "Singapore Post issues stamps featuring him on 28 February 2001."),
    (2019, "Bicentennial", "$20 note", -1, "end", "He is one of the eight pioneers on the back of the Bicentennial commemorative $20 note."),
]
BANDS = [  # (from, to, label, kind)
    (1929.0, 1963.0, "Pillai's own business, 1929 to 1963", "bank"),
    (1942.1, 1945.7, "Japanese Occupation, 1942 to 1945", "war"),
]


def _decades():
    below = [e[0] for e in EVENTS if e[3] > 0]
    return [y for y in range(Y0, Y1 + 1, TICK) if all(abs(y - b) > 3 for b in below)]


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
    for yr, l1, l2, lv, an, _ in EVENTS:
        x, ly = sx(yr), lev[lv]
        d.line([(x * SS, ax * SS), (x * SS, (ly + (34 if lv < 0 else -26)) * SS)], fill=CHART_MUTED, width=SS)
        d.ellipse([(x - 7) * SS, (ax - 7) * SS, (x + 7) * SS, (ax + 7) * SS], fill=CHART_BG, outline=CHART_LINE, width=3 * SS)
        anc = {"start": "l", "end": "r", "middle": "m"}[an]
        tx = x - 4 if anc == "l" else (x + 4 if anc == "r" else x)
        d.text((tx * SS, (ly - 22) * SS), str(yr), font=fy, fill=CHART_TEXT, anchor=anc + "m")
        d.text((tx * SS, ly * SS), l1, font=fl, fill=CHART_SECONDARY, anchor=anc + "m")
        d.text((tx * SS, (ly + 20) * SS), l2, font=fl, fill=CHART_SECONDARY, anchor=anc + "m")
    img.resize((W, H), Image.LANCZOS).save(OUT)
    print("wrote", OUT)


def svg_card():
    sx = _layout(30, 770)
    ax = 160
    lev = {-2: 30, -1: 80, 1: 232, 2: 282}
    h = 322
    s = [f'<svg viewBox="0 0 800 {h}" width="100%" height="auto" role="img" aria-label="Timeline from 1900 to 2020. '
         + " ".join(f"{yr}: {l1} {l2}." for yr, l1, l2, _, _, _ in EVENTS)
         + ' The years 1929 to 1963, when he ran the business himself, are shaded, with the Japanese Occupation of 1942 to 1945 marked.">']
    for a, b, _, kind in BANDS:
        top, bot = (ax - 20, ax + 20) if kind == "bank" else (ax - 28, ax + 28)
        var = "--band-bank" if kind == "bank" else "--band-war"
        s.append(f'  <rect x="{sx(a):.1f}" y="{top}" width="{sx(b) - sx(a):.1f}" height="{bot - top}" rx="3" fill="var({var})"/>')
    s.append(f'  <line x1="{sx(Y0):.1f}" y1="{ax}" x2="{sx(Y1):.1f}" y2="{ax}" stroke="var(--axis)" stroke-width="1.5"/>')
    for y in range(Y0, Y1 + 1, TICK):
        s.append(f'  <line x1="{sx(y):.1f}" y1="{ax - 4}" x2="{sx(y):.1f}" y2="{ax + 4}" stroke="var(--axis)"/>')
    for y in _decades():
        s.append(f'  <text class="lt-axis" x="{sx(y):.1f}" y="{ax + 44}" text-anchor="middle">{y}</text>')
    for yr, l1, l2, lv, anc, tip in EVENTS:
        x, ly = sx(yr), lev[lv]
        tx = x - 3 if anc == "start" else (x + 3 if anc == "end" else x)
        stem_end = ly + 22 if lv < 0 else ly - 26
        s.append(f'  <g class="lt-hit" tabindex="0" data-label="{yr}: {l1} {l2}" data-val="{tip}">'
                 f'<rect x="{x - 40:.1f}" y="{min(ly - 30, ax - 8)}" width="80" height="{abs(ax - ly) + 40}" fill="transparent"/>'
                 f'<line x1="{x:.1f}" y1="{ax}" x2="{x:.1f}" y2="{stem_end}" stroke="var(--axis)"/>'
                 f'<circle class="lt-dot" cx="{x:.1f}" cy="{ax}" r="5"/>'
                 f'<text class="lt-year" x="{tx:.1f}" y="{ly - 12}" text-anchor="{anc}">{yr}</text>'
                 f'<text class="lt-lab" x="{tx:.1f}" y="{ly + 2}" text-anchor="{anc}">{l1}</text>'
                 f'<text class="lt-lab" x="{tx:.1f}" y="{ly + 15}" text-anchor="{anc}">{l2}</text></g>')
    s.append("</svg>")
    rows = "\n".join(f"        <tr><td>{yr}</td><td>{tip}</td></tr>" for yr, _, _, _, _, tip in EVENTS)
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
      <thead><tr><th>Year</th><th>Event</th></tr></thead>
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
