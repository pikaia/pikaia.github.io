"""Timeline and camp-population chart for the Interned in India post.

Two graphics, each with a dark-theme 1280x720 PNG for the video/Watch slide and
an inline HTML card for the post:

  python scripts/render_interned_in_india_charts.py               # both PNGs
  python scripts/render_interned_in_india_charts.py --svg timeline
  python scripts/render_interned_in_india_charts.py --svg people

The timeline has two axis segments with a break between them (the internment,
1941-46, and its aftermath in Singapore, 1950-56); dated events are dots with
labels staggered on four levels. The people chart is the camp count at Deoli
in May 1943, by origin, on a linear scale.

Sources: C. de Matos and R. Ward, "Forgotten Forced Migrants of War", Journal
of Contemporary History 56 (2021); The Straits Times, 8 Dec 1941 and 19 Sep
1951; Malaya Tribune, 26 Mar 1946; Singapore Standard, 8 Nov 1955. Layout and
drawing follow render_horsburgh_timeline.py and render_convict_crimes_chart.py.
"""
import sys
from pathlib import Path

from PIL import Image, ImageDraw

sys.path.insert(0, str(Path(__file__).resolve().parent))
from render_transfer_timeline import SCRIPT, STYLE  # noqa: E402
from watch_video_lib import (  # noqa: E402
    CHART_BG, CHART_LINE, CHART_MUTED, CHART_SECONDARY, CHART_TEXT, load_font,
)

IMG = Path(__file__).resolve().parent.parent / "assets" / "images"

# ---- Timeline -------------------------------------------------------------

TL_TITLE = "Interned in India, 1941-46, and after"
TL_SUB = "From the arrests in Singapore to the Deoli camp, and what followed in Singapore"
TL_FOOT = "Sources: de Matos and Ward (2021); Straits Times, 8 Dec 1941 and 19 Sep 1951; Malaya Tribune, 26 Mar 1946; Singapore Standard, 8 Nov 1955."
# Each segment: (first year, last year, tick step, share of the drawing width).
SEGMENTS = [(1941.5, 1946.6, 1, 0.72), (1950, 1956, 2, 0.28)]
GAP = 0.06

# (position, date label, label line 1, label line 2, level, anchor, tooltip). Levels: -2, -1 above the axis, 1, 2 below.
EVENTS = [
    (1941.67, "Sep 1941", "Singapore asks India", "to take internees", -2, "start", "The Governor of the Straits Settlements asks the Government of India whether it would receive Malaya's Japanese internees if war came, about 2,000 men and 750 women, at the Malayan governments' expense."),
    (1941.93, "8 Dec 1941", "Japanese residents", "rounded up", 2, "start", "Hours after the attack on Pearl Harbor, police round up Japanese nationals across Malaya. The Straits Times expects 1,300 to have been taken in Singapore by the time it goes to press."),
    (1942.05, "Jan 1942", "Shipped to India;", "tents at Purana Qila", -1, "start", "The men sail on 7 January 1942 and reach Bombay on the 19th, then go by train to the Purana Qila, Delhi's old fort. The women and children sail separately to Calcutta."),
    (1942.6, "Aug 1942", "About 720 leave in", "an exchange", 1, "start", "About 720 internees from Purana Qila are sent home in the Anglo-Japanese civilian exchange at Lourenco Marques, mostly consuls, bank and company managers and teachers."),
    (1943.25, "Mar-Apr 1943", "Moved to Deoli,", "Rajasthan", -1, "start", "The remaining internees, about 2,100, move to brick barracks at Deoli, near Ajmer."),
    (1945.62, "Aug 1945", "Japan", "surrenders", 1, "end", "Japan surrenders. Many internees refuse to believe it, and the camp splits between those who accept the news and those who do not."),
    (1946.15, "Feb 1946", "Guards open fire", "at Deoli", -2, "end", "On 26 February 1946 troops open fire during a confrontation in the camp. Reuters reported 15 internees killed and 16 wounded; later accounts put the deaths at 14 to about 20."),
    (1946.37, "May 1946", "Internees", "released", 2, "end", "The internees leave Deoli in May 1946, nine months after the surrender, and are sent on to Japan, Taiwan and elsewhere."),
    (1951.72, "Sep 1951", "Singapore pays", "its share", -1, "start", "Singapore's Legislative Council approves $4,644,972 as its share of India's bill for keeping the internees, three-fifths of the total."),
    (1955.85, "Nov 1955", "Echigoya", "reopens", 1, "end", "Fukuda Kurahachi, interned in 1941, reopens the Echigoya store on Coleman Street as the first Japanese firm in Malaya after the war with local capital."),
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


def _tick_years():
    out = []
    for a, b, step, _ in SEGMENTS:
        first = int(a) if a == int(a) else int(a) + 1
        out += list(range(first, int(b) + 1, step))
    return out


def _tick_labels():
    below = [e[0] for e in EVENTS if e[4] > 0]
    return [y for y in _tick_years() if all(abs(y - e) > 0.3 for e in below)]


def timeline_png():
    W, H, SS = 1280, 720, 2
    img = Image.new("RGB", (W * SS, H * SS), CHART_BG)
    d = ImageDraw.Draw(img)
    d.text((60 * SS, 40 * SS), TL_TITLE, font=load_font(34 * SS), fill=CHART_TEXT)
    d.text((60 * SS, 84 * SS), TL_SUB, font=load_font(19 * SS, bold=False), fill=CHART_SECONDARY)
    d.text((60 * SS, 680 * SS), TL_FOOT, font=load_font(14 * SS, bold=False), fill=CHART_MUTED)
    sx, spans = _scale(90, 1190)
    ax = 395
    lev = {-2: 175, -1: 270, 1: 520, 2: 615}
    for a, b, p0, p1 in spans:
        d.line([(p0 * SS, ax * SS), (p1 * SS, ax * SS)], fill=CHART_MUTED, width=2 * SS)
    gx = (spans[0][3] + spans[1][2]) / 2
    for dx in (-6, 6):
        d.line([((gx + dx - 5) * SS, (ax + 9) * SS), ((gx + dx + 5) * SS, (ax - 9) * SS)], fill=CHART_MUTED, width=2 * SS)
    for y in _tick_years():
        d.line([(sx(y) * SS, (ax - 5) * SS), (sx(y) * SS, (ax + 5) * SS)], fill=CHART_MUTED, width=SS)
    for y in _tick_labels():
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
    out = IMG / "interned-in-india-timeline-chart.png"
    img.resize((W, H), Image.LANCZOS).save(out)
    print("wrote", out)


def timeline_svg():
    sx, spans = _scale(30, 770)
    ax = 160
    lev = {-2: 30, -1: 80, 1: 232, 2: 282}
    h = 322
    s = [f'<svg viewBox="0 0 800 {h}" width="100%" height="auto" role="img" aria-label="Timeline in two parts, 1941 to 1946 and 1950 to 1956. '
         + " ".join(f"{dl}: {l1} {l2}." for _, dl, l1, l2, _, _, _ in EVENTS) + '">']
    for a, b, p0, p1 in spans:
        s.append(f'  <line x1="{p0:.1f}" y1="{ax}" x2="{p1:.1f}" y2="{ax}" stroke="var(--axis)" stroke-width="1.5"/>')
    gx = (spans[0][3] + spans[1][2]) / 2
    for dx in (-4, 4):
        s.append(f'  <line x1="{gx + dx - 4:.1f}" y1="{ax + 7}" x2="{gx + dx + 4:.1f}" y2="{ax - 7}" stroke="var(--axis)" stroke-width="1.5"/>')
    for y in _tick_years():
        s.append(f'  <line x1="{sx(y):.1f}" y1="{ax - 4}" x2="{sx(y):.1f}" y2="{ax + 4}" stroke="var(--axis)"/>')
    for y in _tick_labels():
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
  <p class="lt-title">{TL_TITLE}</p>
  <p class="lt-subtitle">{TL_SUB}</p>
  <div class="lt-chart-wrap">
{chr(10).join("    " + line for line in s)}
    <div class="lt-tooltip"></div>
  </div>
  <p class="lt-foot">{TL_FOOT}</p>
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


# ---- Who was in the camp, May 1943 -----------------------------------------

PP_TITLE = "Who was in the camp at Deoli, May 1943"
PP_SUB = "Internees by origin, 2,101 in all; linear scale"
PP_FOOT = "Source: camp return of May 1943 (National Archives, Kew, FO 916/776), as given in de Matos and Ward (2021). Most internees had come from Singapore and Malaya."
PEOPLE = [
    ("Japanese", "including Okinawans", 1889, "1,889"),
    ("Taiwanese", "subjects of Japan's empire", 184, "184"),
    ("Chinese", "", 10, "10"),
    ("Thai", "held after Thailand declared war", 7, "7"),
    ("Malay", "mostly women, likely with Japanese partners", 5, "5"),
    ("Korean", "subjects of Japan's empire", 5, "5"),
    ("Russian", "", 1, "1"),
]
VMAX = 2000


def people_png():
    W, H, SS = 1280, 720, 2
    X0, X1 = 470, 1130
    img = Image.new("RGB", (W * SS, H * SS), CHART_BG)
    d = ImageDraw.Draw(img)
    d.text((60 * SS, 40 * SS), PP_TITLE, font=load_font(34 * SS), fill=CHART_TEXT)
    d.text((60 * SS, 86 * SS), PP_SUB, font=load_font(19 * SS, bold=False), fill=CHART_SECONDARY)

    def x(v):
        return (X0 + v * (X1 - X0) / VMAX) * SS

    name_f, lab, val = load_font(22 * SS), load_font(15 * SS, bold=False), load_font(22 * SS)
    top, step, bh = 140, 66, 40
    for i, (name, sub, v, vl) in enumerate(PEOPLE):
        y = (top + i * step) * SS
        if sub:
            d.text(((X0 - 18) * SS, y + 12 * SS), name, font=name_f, fill=CHART_TEXT, anchor="rm")
            d.text(((X0 - 18) * SS, y + 33 * SS), sub, font=lab, fill=CHART_SECONDARY, anchor="rm")
        else:
            d.text(((X0 - 18) * SS, y + 20 * SS), name, font=name_f, fill=CHART_TEXT, anchor="rm")
        right = max(x(v), (X0 + 4) * SS)
        d.rounded_rectangle([X0 * SS, y, right, y + bh * SS], radius=4 * SS, fill=CHART_LINE)
        d.text((right + 12 * SS, y + 20 * SS), vl, font=val, fill=CHART_TEXT, anchor="lm")
    base = (top + len(PEOPLE) * step - 14) * SS
    d.line([(X0 * SS, (top - 10) * SS), (X0 * SS, base)], fill=CHART_MUTED, width=SS)
    tick = load_font(16 * SS, bold=False)
    for t in (0, 500, 1000, 1500, 2000):
        d.text((x(t), base + 22 * SS), f"{t:,}", font=tick, fill=CHART_MUTED, anchor="mm")
    d.text((60 * SS, 680 * SS), "Source: Deoli camp return, May 1943 (FO 916/776), in de Matos and Ward (2021).",
           font=load_font(15 * SS, bold=False), fill=CHART_MUTED)
    out = IMG / "interned-in-india-people-chart.png"
    img.resize((W, H), Image.LANCZOS).save(out)
    print("wrote", out)


def people_svg():
    X0, X1, step, bh, top = 300, 700, 42, 26, 10
    h = top + len(PEOPLE) * step + 34

    def x(v):
        return X0 + v * (X1 - X0) / VMAX

    s = [f'<svg viewBox="0 0 800 {h}" width="100%" height="auto" role="img" aria-label="Bar chart of the 2,101 internees at Deoli in May 1943 by origin: '
         + ", ".join(f"{vl} {name}" for name, _, _, vl in PEOPLE) + '.">']
    for i, (name, sub, v, vl) in enumerate(PEOPLE):
        y = top + i * step
        tip = f"{vl} {name}" + (f" ({sub})" if sub else "") + "."
        right = max(x(v), X0 + 3)
        s.append(f'  <g class="lt-hit" tabindex="0" data-label="{name}" data-val="{tip}">'
                 f'<rect x="0" y="{y - 4}" width="800" height="{step}" fill="transparent"/>'
                 + (f'<text class="lt-year" style="font-size:15px" x="{X0 - 12}" y="{y + 10}" text-anchor="end">{name}</text>'
                    f'<text class="lt-lab" style="font-size:12.5px" x="{X0 - 12}" y="{y + 25}" text-anchor="end">{sub}</text>' if sub else
                    f'<text class="lt-year" style="font-size:15px" x="{X0 - 12}" y="{y + 17}" text-anchor="end">{name}</text>')
                 + f'<rect x="{X0}" y="{y}" width="{right - X0:.1f}" height="{bh}" rx="4" fill="var(--series-1)"/>'
                 f'<text class="lt-year" style="font-size:15px" x="{right + 8:.1f}" y="{y + 17}">{vl}</text></g>')
    base = top + len(PEOPLE) * step - 6
    s.append(f'  <line x1="{X0}" y1="{top - 6}" x2="{X0}" y2="{base}" stroke="var(--axis)"/>')
    for t in (0, 500, 1000, 1500, 2000):
        s.append(f'  <text class="lt-axis" style="font-size:13px" x="{x(t):.1f}" y="{base + 20}" text-anchor="middle">{t:,}</text>')
    s.append("</svg>")
    rows = "\n".join(f"        <tr><td>{name}" + (f" ({sub})" if sub else "") + f"</td><td>{vl}</td></tr>" for name, sub, _, vl in PEOPLE)
    print(STYLE + f"""
<div class="lt-card">
  <p class="lt-title">{PP_TITLE}</p>
  <p class="lt-subtitle">{PP_SUB}</p>
  <div class="lt-chart-wrap">
{chr(10).join("    " + line for line in s)}
    <div class="lt-tooltip"></div>
  </div>
  <p class="lt-foot">{PP_FOOT}</p>
  <details class="lt-details">
    <summary>View as table</summary>
    <table class="lt-table">
      <thead><tr><th>Origin</th><th>Internees</th></tr></thead>
      <tbody>
{rows}
        <tr><td>Total</td><td>2,101</td></tr>
      </tbody>
    </table>
  </details>
</div>
""" + SCRIPT + "\n</div>")


if __name__ == "__main__":
    if "--svg" in sys.argv:
        which = sys.argv[sys.argv.index("--svg") + 1]
        {"timeline": timeline_svg, "people": people_svg}[which]()
    else:
        timeline_png()
        people_png()
