"""Timeline of Horsburgh Lighthouse, for the Horsburgh Lighthouse post.

Two axis segments with a break between them: the building of the light
(1834-1852) and the question of who owns the rock (1950-2025). Dated events are
dots with labels staggered on four levels (two above each axis, two below) so
neighbours never overlap. The same EVENTS drive both outputs:

  python scripts/render_horsburgh_timeline.py        # assets/images/horsburgh-timeline-chart.png
                                                     # (dark-theme 1280x720 video/Watch slide)
  python scripts/render_horsburgh_timeline.py --svg  # prints the post's inline card HTML

Dates are from J. T. Thomson's 1852 account of the lighthouse, the Singapore
Free Press of 6 October 1851, the ICJ judgment of 23 May 2008 and the ICJ order
of 29 May 2018. Layout and drawing follow render_tani_timeline.py.
"""
import sys
from pathlib import Path

from PIL import Image, ImageDraw

sys.path.insert(0, str(Path(__file__).resolve().parent))
from render_transfer_timeline import SCRIPT, STYLE  # noqa: E402
from watch_video_lib import (  # noqa: E402
    CHART_BG, CHART_LINE, CHART_MUTED, CHART_SECONDARY, CHART_TEXT, load_font,
)

OUT = Path(__file__).resolve().parent.parent / "assets" / "images" / "horsburgh-timeline-chart.png"
TITLE = "Horsburgh Lighthouse: the light and the rock"
SUB = "Building the light, 1836-1851, and the question of who owns Pedra Branca, 1953-2018"
FOOT = "Sources: J. T. Thomson (1852); Singapore Free Press, 6 Oct 1851; ICJ judgment, 23 May 2008; ICJ order, 29 May 2018."
# Each segment: (first year, last year, tick step, share of the drawing width).
SEGMENTS = [(1834, 1852, 2, 0.40), (1950, 2025, 10, 0.60)]
GAP = 0.06  # share of the width left blank between the segments

# (position, date label, label line 1, label line 2, level, anchor, tooltip). Levels: -2, -1 above the axis, 1, 2 below.
EVENTS = [
    (1836.37, "May 1836", "James Horsburgh", "dies in England", -1, "start", "The East India Company's hydrographer, author of the standard sailing directory for these seas, dies on 14 May 1836. Merchants later raise a fund for a lighthouse in his memory."),
    (1847.47, "Jun 1847", "Pedra Branca chosen", "as the site", 1, "end", "On 21 June 1847 the government tells Thomson the light will go on Pedra Branca rather than Peak Rock, on the Admiralty's advice."),
    (1850.39, "May 1850", "Foundation stone", "laid", -2, "end", "On 24 May 1850, Queen Victoria's birthday, Freemasons of Lodge Zetland in the East lay the stone with Masonic honours, watched by Governor Butterworth."),
    (1851.79, "Oct 1851", "The light is shown", "every night", 2, "end", "The Notice to Mariners says the light will be exhibited from the night of 15 October 1851, and every night thereafter from sunset to sunrise."),
    (1953.72, "Sep 1953", "Johor: no claim", "to ownership", -1, "start", "On 21 September 1953 the Acting State Secretary of Johor replies to Singapore that the Johore Government does not claim ownership of Pedra Branca."),
    (1979.97, "Dec 1979", "Malaysian map shows", "the island as its own", 1, "start", "Malaysia publishes a map placing Pedra Branca in its territorial waters. Singapore protests by diplomatic note on 14 February 1980."),
    (2003.1, "Feb 2003", "Both agree to go", "to the ICJ", -1, "end", "Malaysia and Singapore sign a Special Agreement at Putrajaya on 6 February 2003 to put the question to the International Court of Justice."),
    (2008.39, "May 2008", "ICJ: Pedra Branca", "to Singapore", -2, "end", "On 23 May 2008 the Court awards Pedra Branca to Singapore by 12 votes to 4, Middle Rocks to Malaysia by 15 to 1, and South Ledge to the state in whose waters it lies."),
    (2017.6, "2017-18", "Malaysia asks for review,", "then withdraws", 2, "end", "Malaysia files for revision in February 2017 and for interpretation in June 2017, and discontinues both in May 2018; the Court removes the case from its list on 29 May 2018."),
]


def _scale(x0, x1):
    """Return year -> x for the two segments, and each segment's pixel span."""
    usable = (x1 - x0) * (1 - GAP)
    spans, cur = [], x0
    for a, b, _, share in SEGMENTS:
        w = usable * share
        spans.append((a, b, cur, cur + w))
        cur += w + (x1 - x0) * GAP
    def sx(y):
        for a, b, p0, p1 in spans:
            if a <= y <= b:
                return p0 + (y - a) / (b - a) * (p1 - p0)
        raise ValueError(y)
    return sx, spans


def _ticks():
    below = [e[0] for e in EVENTS if e[4] > 0]
    out = []
    for a, b, step, _ in SEGMENTS:
        first = a if a % step == 0 else a + step - a % step
        out += [y for y in range(first, b + 1, step) if all(abs(y - e) > 1.2 * step / 2 for e in below)]
    return out


def render_png():
    W, H, SS = 1280, 720, 2
    img = Image.new("RGB", (W * SS, H * SS), CHART_BG)
    d = ImageDraw.Draw(img)
    d.text((60 * SS, 40 * SS), TITLE, font=load_font(34 * SS), fill=CHART_TEXT)
    d.text((60 * SS, 84 * SS), SUB, font=load_font(19 * SS, bold=False), fill=CHART_SECONDARY)
    d.text((60 * SS, 680 * SS), FOOT, font=load_font(14 * SS, bold=False), fill=CHART_MUTED)
    sx, spans = _scale(90, 1190)
    ax = 395
    lev = {-2: 175, -1: 270, 1: 520, 2: 615}
    for a, b, p0, p1 in spans:
        d.line([(p0 * SS, ax * SS), (p1 * SS, ax * SS)], fill=CHART_MUTED, width=2 * SS)
    # The break between the segments.
    gx = (spans[0][3] + spans[1][2]) / 2
    for dx in (-6, 6):
        d.line([((gx + dx - 5) * SS, (ax + 9) * SS), ((gx + dx + 5) * SS, (ax - 9) * SS)], fill=CHART_MUTED, width=2 * SS)
    for a, b, step, _ in SEGMENTS:
        first = a if a % step == 0 else a + step - a % step
        for y in range(first, b + 1, step):
            d.line([(sx(y) * SS, (ax - 5) * SS), (sx(y) * SS, (ax + 5) * SS)], fill=CHART_MUTED, width=SS)
    for y in _ticks():
        d.text((sx(y) * SS, (ax + 28) * SS), str(y), font=load_font(14 * SS, bold=False), fill=CHART_MUTED, anchor="mm")
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
    sx, spans = _scale(30, 770)
    ax = 160
    lev = {-2: 30, -1: 80, 1: 232, 2: 282}
    h = 322
    s = [f'<svg viewBox="0 0 800 {h}" width="100%" height="auto" role="img" aria-label="Timeline in two parts, 1834 to 1852 and 1950 to 2025. '
         + " ".join(f"{dl}: {l1} {l2}." for _, dl, l1, l2, _, _, _ in EVENTS) + '">']
    for a, b, p0, p1 in spans:
        s.append(f'  <line x1="{p0:.1f}" y1="{ax}" x2="{p1:.1f}" y2="{ax}" stroke="var(--axis)" stroke-width="1.5"/>')
    gx = (spans[0][3] + spans[1][2]) / 2
    for dx in (-4, 4):
        s.append(f'  <line x1="{gx + dx - 4:.1f}" y1="{ax + 7}" x2="{gx + dx + 4:.1f}" y2="{ax - 7}" stroke="var(--axis)" stroke-width="1.5"/>')
    for a, b, step, _ in SEGMENTS:
        first = a if a % step == 0 else a + step - a % step
        for y in range(first, b + 1, step):
            s.append(f'  <line x1="{sx(y):.1f}" y1="{ax - 4}" x2="{sx(y):.1f}" y2="{ax + 4}" stroke="var(--axis)"/>')
    for y in _ticks():
        s.append(f'  <text class="lt-axis" x="{sx(y):.1f}" y="{ax + 20}" text-anchor="middle">{y}</text>')
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
    print(STYLE + f"""
<div class="lt-card">
  <p class="lt-title">{TITLE}</p>
  <p class="lt-subtitle">{SUB}</p>
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
