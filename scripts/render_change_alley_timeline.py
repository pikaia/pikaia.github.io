"""Timeline of Change Alley, from its naming in 1890 to the arcade of today, for the Change Alley post.

One year axis (1880-2020) with the years of the open-air bazaar shaded, and
dated events as dots with labels staggered on four levels (two above the axis,
two below) so neighbours never overlap. The same EVENTS drive both outputs:

  python scripts/render_change_alley_timeline.py          # assets/images/change-alley-timeline-chart.png
                                                          # (dark-theme 1280x720 video/Watch slide)
  python scripts/render_change_alley_timeline.py --svg    # prints the post's inline card HTML

Dates are from the Daily Advertiser, 12 November 1890; the Singapore Free Press,
25 February 1931; the Sunday Times, 12 February 1939; and the National Library
Board's Infopedia article on Change Alley.
"""
import sys
from pathlib import Path

from PIL import Image, ImageDraw

sys.path.insert(0, str(Path(__file__).resolve().parent))
from watch_video_lib import (  # noqa: E402
    CHART_BG, CHART_LINE, CHART_MUTED, CHART_SECONDARY, CHART_TEXT, load_font,
)

OUT = Path(__file__).resolve().parent.parent / "assets" / "images" / "change-alley-timeline-chart.png"
TITLE = "Change Alley, 1890 to today"
SUB = "From a named lane to a bargain bazaar, and then an air-conditioned arcade"
FOOT = "Sources: Daily Advertiser, 12 Nov 1890; Singapore Free Press, 25 Feb 1931; Sunday Times, 12 Feb 1939; NLB Infopedia, Change Alley."
Y0, Y1 = 1880, 2020
TICK = 10

# (year, label line 1, label line 2, level, anchor, tooltip). Levels: -2, -1 above the axis, 1, 2 below.
EVENTS = [
    (1890, "Named", "Change Alley", -1, "start", "On 11 November 1890 the municipal commissioners choose the name Change Alley over Change Lane."),
    (1905, "Winchester House", "at the quay end", 1, "middle", "Winchester House, at the Collyer Quay entrance, dates from 1905."),
    (1931, "From Mincing Lane", "to Petticoat Lane", -1, "middle", "The Singapore Free Press finds a produce exchange at the back and a crowded bazaar of hawkers in front."),
    (1939, "Singapore's", "bargain mart", 1, "middle", "The Sunday Times devotes its back page to the alley's 50 yards of shops."),
    (1960, "Shell House at the", "Raffles Place end", -1, "middle", "The 14-storey Shell House, later Singapore Rubber House, is completed at the Raffles Place entrance."),
    (1973, "Aerial Plaza", "opens", 1, "middle", "An air-conditioned shopping arcade opens on the bridge from Clifford Pier to the alley."),
    (1989, "Last day,", "30 April", -1, "end", "After weeks of clearance sales, the shops open for the last time on 30 April 1989."),
    (1993, "Reopens as", "an arcade", 1, "middle", "An air-conditioned arcade opens between the new Caltex House and Hitachi Tower."),
]
BAND_LABEL_AT = 1956   # band label centre, clear of the event stems
BANDS = [  # (from, to, label, kind)
    (1930.0, 1989.33, "Open-air bazaar, about 1930 to 1989", "bank"),
]


def _decades():
    below = [e[0] for e in EVENTS if e[3] > 0]
    return [y for y in range(Y0, Y1 + 1, TICK) if all(abs(y - b) > 1.5 for b in below)]


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
    war = (90, 90, 88)
    for a, b, lab, kind in BANDS:
        colr = war if kind == "war" else (28, 52, 82)
        top, bot = (ax - 30, ax + 30) if kind == "bank" else (ax - 44, ax + 44)
        d.rectangle([sx(a) * SS, top * SS, sx(b) * SS, bot * SS], fill=colr)
    d.text((sx(BAND_LABEL_AT) * SS, (ax + 18) * SS), BANDS[0][2], font=load_font(15 * SS, bold=False), fill=CHART_SECONDARY, anchor="mm")
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
    s = [f'<svg viewBox="0 0 800 {h}" width="100%" height="auto" role="img" aria-label="Timeline from 1825 to 1870. '
         + " ".join(f"{yr}: {l1} {l2}." for yr, l1, l2, _, _, _ in EVENTS)
         + ' The years of the open-air bazaar, about 1930 to 1989, are shaded.">']
    for a, b, lab, kind in BANDS:
        top, bot = (ax - 20, ax + 20) if kind == "bank" else (ax - 28, ax + 28)
        var = "--band-bank" if kind == "bank" else "--band-war"
        s.append(f'  <rect x="{sx(a):.1f}" y="{top}" width="{sx(b) - sx(a):.1f}" height="{bot - top}" rx="3" fill="var({var})"/>')
    s.append(f'  <text class="lt-band" x="{sx(BAND_LABEL_AT):.1f}" y="{ax + 14}" text-anchor="middle">{BANDS[0][2]}</text>')
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
    print(STYLE + f"""
<div class="lt-card">
  <p class="lt-title">{TITLE}</p>
  <p class="lt-subtitle">{SUB}</p>
  <div class="lt-legend">
    <span><i class="lt-swatch" style="background: var(--band-bank)"></i>Open-air bazaar, about 1930 to 1989</span>
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


STYLE = """<div class="viz-root" style="clear: both;">
<style>
.viz-root {
  color-scheme: light;
  --surface-1:      #fcfcfb;
  --text-primary:   #0b0b0b;
  --text-secondary: #52514e;
  --text-muted:     #898781;
  --grid:           #e1e0d9;
  --axis:           #c3c2b7;
  --series-1:       #2a78d6;
  --band-bank:      #dbe8f8;
  --band-war:       #e6e5df;
  --border:         rgba(11,11,11,0.10);
  font-family: system-ui, -apple-system, "Segoe UI", sans-serif;
}
@media (prefers-color-scheme: dark) {
  :root:where(:not([data-theme="light"])) .viz-root {
    color-scheme: dark;
    --surface-1:      #1a1a19;
    --text-primary:   #ffffff;
    --text-secondary: #c3c2b7;
    --text-muted:     #898781;
    --grid:           #2c2c2a;
    --axis:           #4a4a46;
    --series-1:       #3987e5;
    --band-bank:      #1c3452;
    --band-war:       #3a3a37;
    --border:         rgba(255,255,255,0.10);
  }
}
:root[data-theme="dark"] .viz-root {
  color-scheme: dark;
  --surface-1:      #1a1a19;
  --text-primary:   #ffffff;
  --text-secondary: #c3c2b7;
  --text-muted:     #898781;
  --grid:           #2c2c2a;
  --axis:           #4a4a46;
  --series-1:       #3987e5;
  --band-bank:      #1c3452;
  --band-war:       #3a3a37;
  --border:         rgba(255,255,255,0.10);
}
.lt-card { background: var(--surface-1); border: 1px solid var(--border); border-radius: 10px; padding: 20px 20px 12px; margin: 1.5em 0; }
.lt-title { font-size: 16px; font-weight: 600; color: var(--text-primary); margin: 0 0 2px; }
.lt-subtitle { font-size: 13px; color: var(--text-secondary); margin: 0 0 12px; }
.lt-legend { display: flex; gap: 18px; flex-wrap: wrap; font-size: 12.5px; color: var(--text-secondary); margin: 0 0 4px; }
.lt-legend span { display: inline-flex; align-items: center; gap: 6px; }
.lt-swatch { width: 12px; height: 12px; border-radius: 3px; display: inline-block; }
.lt-chart-wrap { position: relative; }
.lt-tooltip { position: absolute; pointer-events: none; opacity: 0; transition: opacity 120ms; background: var(--surface-1); border: 1px solid var(--border); border-radius: 6px; padding: 6px 10px; font-size: 12.5px; color: var(--text-primary); box-shadow: 0 2px 8px rgba(0,0,0,0.12); max-width: 260px; }
.lt-tooltip.visible { opacity: 1; }
.lt-tooltip-val { font-weight: 600; margin-bottom: 2px; }
.lt-tooltip-label { color: var(--text-secondary); }
.lt-foot { font-size: 11.5px; color: var(--text-muted); margin-top: 6px; }
.lt-details { margin-top: 10px; }
.lt-details summary { font-size: 12.5px; color: var(--text-secondary); cursor: pointer; }
.lt-table { width: 100%; border-collapse: collapse; margin-top: 8px; font-size: 12.5px; }
.lt-table th, .lt-table td { text-align: left; padding: 4px 8px; border-bottom: 1px solid var(--grid); color: var(--text-primary); }
.lt-table th { color: var(--text-secondary); font-weight: 600; }
.lt-axis { font-size: 11px; fill: var(--text-muted); }
.lt-band { font-size: 10.5px; fill: var(--text-secondary); }
.lt-year { font-size: 12px; font-weight: 600; fill: var(--text-primary); }
.lt-lab { font-size: 10.5px; fill: var(--text-secondary); }
.lt-dot { fill: var(--surface-1); stroke: var(--series-1); stroke-width: 2.5; }
.lt-hit:focus { outline: none; }
.lt-hit:focus .lt-dot, .lt-hit:hover .lt-dot { fill: var(--series-1); }
</style>"""

SCRIPT = """<script>
(function() {
  var card = document.currentScript.previousElementSibling;
  var svg = card.querySelector('.lt-chart-wrap svg');
  var wrap = svg.parentElement;
  var tooltip = wrap.querySelector('.lt-tooltip');
  svg.querySelectorAll('.lt-hit').forEach(function(hit) {
    function show() {
      tooltip.innerHTML = '<div class="lt-tooltip-val">' + hit.getAttribute('data-label') + '</div>' +
        '<div class="lt-tooltip-label">' + hit.getAttribute('data-val') + '</div>';
      var b = hit.getBoundingClientRect(), w = wrap.getBoundingClientRect();
      tooltip.style.left = Math.min(Math.max(b.left - w.left + b.width / 2 - 130, 0), w.width - 260) + 'px';
      tooltip.style.top = Math.max(b.top - w.top - 20, 0) + 'px';
      tooltip.classList.add('visible');
    }
    function hide() { tooltip.classList.remove('visible'); }
    hit.addEventListener('pointerenter', show); hit.addEventListener('focus', show);
    hit.addEventListener('pointerleave', hide); hit.addEventListener('blur', hide);
  });
})();
</script>"""


if __name__ == "__main__":
    if "--svg" in sys.argv:
        svg_card()
    else:
        render_png()
