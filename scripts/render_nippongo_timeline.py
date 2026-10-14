"""Timeline of the Occupation's Japanese-language drive, for the Learning Nippon-go post.

One axis (1942-1946) with the Occupation shaded, and dated events as dots with
labels staggered on four levels (two above the axis, two below) so neighbours
never overlap. The same EVENTS drive both outputs:

  python scripts/render_nippongo_timeline.py        # assets/images/nippongo-timeline-chart.png
                                                    # (dark-theme 1280x720 video/Watch slide)
  python scripts/render_nippongo_timeline.py --svg  # prints the post's inline card HTML

Dates are from the Syonan Times / Syonan Shimbun via NewspaperSG (21 Feb, 4 Jun,
9 Jun, 1 Jul and 1 Aug 1942; 11 and 13 Nov 1943; 12 May 1945) and BiblioAsia for
the paper's last issue. Layout and drawing follow render_tani_timeline.py.
"""
import sys
from pathlib import Path

from PIL import Image, ImageDraw

sys.path.insert(0, str(Path(__file__).resolve().parent))
from render_transfer_timeline import SCRIPT, STYLE  # noqa: E402
from watch_video_lib import (  # noqa: E402
    CHART_BG, CHART_LINE, CHART_MUTED, CHART_SECONDARY, CHART_TEXT, load_font,
)

OUT = Path(__file__).resolve().parent.parent / "assets" / "images" / "nippongo-timeline-chart.png"
TITLE = "Learning Nippon-go in Syonan, 1942-45"
SUB = "How the Japanese-language drive unfolded, from the first lesson to the last newspaper"
FOOT = "Sources: Syonan Times / Syonan Shimbun, 1942-45 (NewspaperSG); BiblioAsia (last issue, 4 Sep 1945)."
Y0, Y1 = 1942, 1946
TICK = 1

# (position, date label, label line 1, label line 2, level, anchor, tooltip). Levels: -2, -1 above the axis, 1, 2 below.
EVENTS = [
    (1942.14, "Feb 1942", "First Nippon Lesson", "in the Syonan Times", -2, "start", "On 21 February 1942, six days after the surrender, the Syonan Times prints its first Nippon Lesson: greetings and the numbers one to twenty-one."),
    (1942.33, "May 1942", "Syonan Nippon Gakuen", "opens on Queen Street", -1, "start", "The Syonan Nippon Gakuen, a Japanese-language school under the poet Jinbo Kotaro, opens on 1 May 1942."),
    (1942.42, "Jun 1942", "First Nippon-go", "Week", 1, "end", "The first Nippon-go Popularizing Week runs from 1 to 7 June 1942, with help from the radio station and the Gakuen."),
    (1942.5, "Jul 1942", "English dropped as", "a school subject", 2, "start", "On 1 July 1942 the Syonan Times reports that Nippon-go is compulsory in the city's schools and English has been dropped as a subject."),
    (1943.86, "Nov 1943", "Allowances raised;", "second Nippon-go Week", -1, "start", "On 11 November 1943 the paper reports higher monthly Nippon-go allowances for government staff, from $5 to $50 by grade; Syonan's second Nippon-go Week opens on 14 November."),
    (1945.12, "Feb 1945", "Graded examinations", "across Malai", 1, "start", "Nippon-go examinations at primary, middle and higher grades are held throughout Malai in February 1945 under new rules."),
    (1945.67, "Sep 1945", "Last issue of the", "Syonan Shimbun", -2, "end", "The Syonan Shimbun prints its last issue on 4 September 1945, as British forces return."),
]
BANDS = [  # (from, to, label, kind)
    (1942.12, 1945.68, "Japanese Occupation", "war"),
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
