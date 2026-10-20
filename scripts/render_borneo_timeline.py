"""Timeline of the links between Sarawak, North Borneo and Singapore, for the
From Borneo to Singapore post.

One axis (1830-2030) with the Japanese Occupation and the Malaysia years
shaded, and dated events as dots with labels staggered on four levels (two
above the axis, two below) so neighbours never overlap. The same EVENTS
drive both outputs:

  python scripts/render_borneo_timeline.py        # assets/images/borneo-timeline-chart.png
                                                  # (dark-theme 1280x720 video/Watch slide)
  python scripts/render_borneo_timeline.py --svg  # prints the post's inline card HTML

Dates are from Wikipedia (Ong Ewe Hai, Borneo Company, Crown Colony of
Labuan, H. R. S. Zehnder, 2015 Sabah earthquake), UOB and the Straits Times
(1 October 1935), Malay Wikipedia (Siput Sarawak) and NLB Infopedia. Layout
and drawing follow render_blakang_mati_timeline.py.
"""
import sys
from pathlib import Path

from PIL import Image, ImageDraw

sys.path.insert(0, str(Path(__file__).resolve().parent))
from render_transfer_timeline import SCRIPT, STYLE  # noqa: E402
from watch_video_lib import (  # noqa: E402
    CHART_BG, CHART_LINE, CHART_MUTED, CHART_SECONDARY, CHART_TEXT, load_font,
)

OUT = Path(__file__).resolve().parent.parent / "assets" / "images" / "borneo-timeline-chart.png"
TITLE = "Borneo and Singapore, 1839-2015"
SUB = "People and links between Sarawak, North Borneo and Singapore"
FOOT = "Sources: Wikipedia; NLB Infopedia; UOB; Straits Times (1935); Malay Wikipedia (Siput Sarawak)."
Y0, Y1 = 1830, 2030
TICK = 25

# (position, date label, label line 1, label line 2, level, anchor, tooltip). Levels: -2, -1 above the axis, 1, 2 below.
EVENTS = [
    (1839, "1839", "James Brooke sails", "from Singapore", -1, "start", "James Brooke sails from Singapore to Sarawak in his schooner, the Royalist. By 1841 he is Rajah of Sarawak, and its trade runs through Singapore."),
    (1846, "1846", "Ong Ewe Hai", "moves to Kuching", 1, "start", "Ong Ewe Hai, born in Singapore around 1830, goes to Sarawak at 16 as a trader, on credit from Singapore firms. He becomes Kuching's leading merchant and Kapitan Cina."),
    (1857, "1857", "Borneo Company", "opens in Singapore", -2, "start", "The Borneo Company, formed in London in 1856 to trade in Sarawak, opens its Singapore branch on 31 July 1857. Sarawak's antimony reaches Europe through Singapore."),
    (1881, "1881", "North Borneo", "Company chartered", 1, "start", "The British North Borneo Company receives its royal charter to govern North Borneo, now Sabah."),
    (1896, "1896", "SS Rajah Brooke", "wrecked", -1, "start", "The Kuching-Singapore steamer Rajah Brooke leaves Kuching on 22 July 1896 and is wrecked on a rock on the night of 31 July."),
    (1907, "1907", "Labuan joins the", "Settlement of Singapore", 2, "start", "From 1 January 1907 the island of Labuan, off Borneo, is part of the Settlement of Singapore. It becomes a separate settlement of the Straits Settlements in 1912."),
    (1910, "1910", "Hugh Zehnder called", "to the bar", -2, "start", "Hugh Zehnder, born in Sarawak in 1879, is called to the Singapore bar on 23 May 1910. He goes on to lead the Eurasian Association and sit on the Legislative Council."),
    (1929, "1929", "Elizabeth Choy", "comes to school", 1, "end", "Elizabeth Choy, born in Kudat in North Borneo in 1910, comes to Singapore in December 1929 to study at the Convent of the Holy Infant Jesus."),
    (1935, "1935", "United Chinese", "Bank opens", -1, "start", "The United Chinese Bank, founded by a group led by the Kuching-born Wee Kheng Chiang, opens in Singapore on 1 October 1935. It is now UOB."),
    (1947, "1947", "Siput Sarawak's", "first film", 2, "start", "The Kuching-born actress Siput Sarawak makes her first film, Singapura di Waktu Malam, and goes on to act in about 50 Malay films made in Singapore."),
    (1963, "1963", "Malaysia", "is formed", -2, "start", "On 16 September 1963 Malaya, Singapore, North Borneo (renamed Sabah) and Sarawak form Malaysia."),
    (1965, "1965", "Singapore leaves", "Malaysia", -1, "start", "On 9 August 1965 Singapore separates from Malaysia and becomes independent. Sabah and Sarawak remain in Malaysia."),
    (2015, "2015", "Kinabalu", "earthquake", -1, "end", "An earthquake on 5 June 2015 kills 18 people on Mount Kinabalu, among them ten Singaporeans, mostly pupils and teachers of Tanjong Katong Primary School, and four Sabahan mountain guides."),
]
BANDS = [  # (from, to, label, kind)
    (1942, 1945, "Japanese Occupation", "war"),
    (1963, 1965, "Malaysia, 1963-65", "bank"),
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
