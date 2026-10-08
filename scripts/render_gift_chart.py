"""The $50 million "gift" of 1942, against Malaya's money supply, for the post.

Three horizontal bars on one dollar scale (millions of Straits dollars):
all the currency in Malaya in 1942, including bank reserves ($220 million);
the sum demanded, split into Singapore's $10 million and the rest of Malaya's
$40 million; and how it was paid, $28 million raised by 20 June 1942 and $22
million borrowed from the Yokohama Specie Bank. Figures from the National
Library Board's Infopedia article on the Oversea Chinese Association.

    python scripts/render_gift_chart.py          # assets/images/fifty-million-gift-chart.png (dark video slide)
    python scripts/render_gift_chart.py --svg    # prints the post's inline card HTML
"""
import sys
from pathlib import Path

from PIL import Image, ImageDraw

sys.path.insert(0, str(Path(__file__).resolve().parent))
from watch_video_lib import (  # noqa: E402
    CHART_BG, CHART_GRID, CHART_MUTED, CHART_SECONDARY, CHART_TEXT, load_font,
)

OUT = Path(__file__).resolve().parent.parent / "assets" / "images" / "fifty-million-gift-chart.png"
TITLE = "The $50 million against all the money in Malaya"
SUB = "Millions of Straits dollars, 1942"
FOOT = "Source: National Library Board, Infopedia, \"Oversea Chinese Association\". Currency figure includes reserves held by banks."
VMAX = 240

# (row label, [(value, colour key, segment label, tooltip)])
ROWS = [
    ("All currency in Malaya", [(220, "neutral", "$220m",
                                 "About $220 million of currency in circulation in Malaya, including reserves held by banks")]),
    ("Sum demanded", [(10, "a", "Singapore $10m", "$10 million from the Chinese in Singapore"),
                      (40, "b", "Rest of Malaya $40m", "$40 million from the Chinese in the rest of Malaya")]),
    ("How it was paid", [(28, "a", "Raised $28m", "$28 million raised by 20 June 1942, after three extensions"),
                         (22, "b", "Borrowed $22m", "$22 million borrowed from the Yokohama Specie Bank at 6 per cent")]),
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
    x0, x1, top = 330, 1200, 170
    sx = lambda v: (x0 + v / VMAX * (x1 - x0)) * SS  # noqa: E731
    f, fl = load_font(15 * SS, bold=False), load_font(20 * SS)
    for v in range(0, VMAX + 1, 40):
        d.line([(sx(v), (top - 20) * SS), (sx(v), 590 * SS)], fill=CHART_GRID if v else CHART_MUTED, width=SS)
        d.text((sx(v), 612 * SS), f"${v}m", font=f, fill=CHART_MUTED, anchor="mm")
    rowh = 140
    for i, (lab, segs) in enumerate(ROWS):
        cy = top + 40 + i * rowh
        d.text(((x0 - 18) * SS, cy * SS), lab, font=fl, fill=CHART_TEXT, anchor="rm")
        acc = 0
        for v, key, seg, _ in segs:
            d.rectangle([sx(acc) + (2 * SS if acc else 0), (cy - 26) * SS, sx(acc + v), (cy + 26) * SS], fill=PNG_COL[key])
            acc += v
        if len(segs) == 1:
            d.text(((sx(0) + sx(acc)) / 2, cy * SS), segs[0][2], font=load_font(20 * SS), fill=CHART_TEXT, anchor="mm")
            continue
        # short stacked bars: one swatch + label line per segment, right of the bar end
        lx = sx(acc) + 20 * SS
        for j, (v, key, seg, _) in enumerate(segs):
            ly = (cy - 14 + j * 28) * SS
            d.rectangle([lx, ly - 7 * SS, lx + 14 * SS, ly + 7 * SS], fill=PNG_COL[key])
            d.text((lx + 24 * SS, ly), seg, font=load_font(19 * SS, bold=False), fill=CHART_SECONDARY, anchor="lm")
    img.resize((W, H), Image.LANCZOS).save(OUT)
    print("wrote", OUT)


def svg_card():
    x0, x1, top, rowh = 170, 770, 24, 78
    sx = lambda v: x0 + v / VMAX * (x1 - x0)  # noqa: E731
    h = top + rowh * len(ROWS) + 30
    aria = ("Horizontal bar chart in millions of Straits dollars. All currency in Malaya in 1942, including bank reserves: "
            "about 220. Sum demanded: 50, made up of 10 from Singapore and 40 from the rest of Malaya. How it was paid: "
            "28 raised by 20 June 1942 and 22 borrowed from the Yokohama Specie Bank.")
    s = [f'<svg viewBox="0 0 800 {h}" width="100%" height="auto" role="img" aria-label="{aria}">']
    for v in range(0, VMAX + 1, 40):
        s.append(f'  <line x1="{sx(v):.1f}" y1="{top - 10}" x2="{sx(v):.1f}" y2="{top + rowh * len(ROWS) - 20}" stroke="var({"--axis" if v == 0 else "--grid"})"/>')
        s.append(f'  <text class="gc-axis" x="{sx(v):.1f}" y="{top + rowh * len(ROWS) - 4}" text-anchor="middle">${v}m</text>')
    for i, (lab, segs) in enumerate(ROWS):
        cy = top + 14 + i * rowh
        s.append(f'  <text class="gc-row" x="{x0 - 10}" y="{cy + 5}" text-anchor="end">{lab}</text>')
        acc = 0
        for j, (v, key, seg, tip) in enumerate(segs):
            gap = 2 if acc else 0
            s.append(f'  <g class="gc-hit" tabindex="0" data-label="{seg}" data-val="{tip}">'
                     f'<rect x="{sx(acc) + gap:.1f}" y="{cy - 13}" width="{sx(acc + v) - sx(acc) - gap:.1f}" height="26" rx="3" fill="var({SVG_VAR[key]})"/></g>')
            if len(segs) == 1:
                s.append(f'  <text class="gc-in" x="{(sx(acc) + sx(acc + v)) / 2:.1f}" y="{cy + 5}" text-anchor="middle">{seg}</text>')
            acc += v
        if len(segs) > 1:
            lx = sx(acc) + 12
            for j, (_, key, seg, _) in enumerate(segs):
                ly = cy - 7 + j * 16
                s.append(f'  <rect x="{lx:.1f}" y="{ly - 5}" width="10" height="10" rx="2" fill="var({SVG_VAR[key]})"/>')
                s.append(f'  <text class="gc-seg" x="{lx + 16:.1f}" y="{ly + 4}">{seg}</text>')
    s.append("</svg>")
    rows = "\n".join(f"        <tr><td>{lab}</td><td>{seg}</td><td>{tip}</td></tr>" for lab, segs in ROWS for _, _, seg, tip in segs)
    print(STYLE + f"""
<div class="gc-card">
  <p class="gc-title">{TITLE}</p>
  <p class="gc-subtitle">{SUB}</p>
  <div class="gc-legend">
    <span><i class="gc-swatch" style="background: var(--series-1)"></i>Singapore / raised</span>
    <span><i class="gc-swatch" style="background: var(--series-2)"></i>Rest of Malaya / borrowed</span>
    <span><i class="gc-swatch" style="background: var(--neutral)"></i>All currency in Malaya</span>
  </div>
  <div class="gc-chart-wrap">
{chr(10).join("    " + line for line in s)}
    <div class="gc-tooltip"></div>
  </div>
  <p class="gc-foot">{FOOT}</p>
  <details class="gc-details">
    <summary>View as table</summary>
    <table class="gc-table">
      <thead><tr><th>Row</th><th>Part</th><th>Detail</th></tr></thead>
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
  --series-2:       #008300;
  --neutral:        #b4b2a9;
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
    --series-2:       #1fa61f;
    --neutral:        #6e6c66;
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
  --series-2:       #1fa61f;
  --neutral:        #6e6c66;
  --border:         rgba(255,255,255,0.10);
}
.gc-card { background: var(--surface-1); border: 1px solid var(--border); border-radius: 10px; padding: 20px 20px 12px; margin: 1.5em 0; }
.gc-title { font-size: 16px; font-weight: 600; color: var(--text-primary); margin: 0 0 2px; }
.gc-subtitle { font-size: 13px; color: var(--text-secondary); margin: 0 0 12px; }
.gc-legend { display: flex; gap: 18px; flex-wrap: wrap; font-size: 12.5px; color: var(--text-secondary); margin: 0 0 8px; }
.gc-legend span { display: inline-flex; align-items: center; gap: 6px; }
.gc-swatch { width: 12px; height: 12px; border-radius: 3px; display: inline-block; }
.gc-chart-wrap { position: relative; }
.gc-tooltip { position: absolute; pointer-events: none; opacity: 0; transition: opacity 120ms; background: var(--surface-1); border: 1px solid var(--border); border-radius: 6px; padding: 6px 10px; font-size: 12.5px; color: var(--text-primary); box-shadow: 0 2px 8px rgba(0,0,0,0.12); max-width: 260px; }
.gc-tooltip.visible { opacity: 1; }
.gc-tooltip-val { font-weight: 600; margin-bottom: 2px; }
.gc-tooltip-label { color: var(--text-secondary); }
.gc-foot { font-size: 11.5px; color: var(--text-muted); margin-top: 6px; }
.gc-details { margin-top: 10px; }
.gc-details summary { font-size: 12.5px; color: var(--text-secondary); cursor: pointer; }
.gc-table { width: 100%; border-collapse: collapse; margin-top: 8px; font-size: 12.5px; }
.gc-table th, .gc-table td { text-align: left; padding: 4px 8px; border-bottom: 1px solid var(--grid); color: var(--text-primary); }
.gc-table th { color: var(--text-secondary); font-weight: 600; }
.gc-axis { font-size: 11px; fill: var(--text-muted); }
.gc-row { font-size: 13px; font-weight: 600; fill: var(--text-primary); }
.gc-in { font-size: 12.5px; font-weight: 600; fill: var(--surface-1); }
.gc-seg { font-size: 11.5px; fill: var(--text-secondary); }
.gc-hit:focus { outline: none; }
.gc-hit:focus rect, .gc-hit:hover rect { stroke: var(--text-primary); stroke-width: 1.5; }
</style>"""

SCRIPT = """<script>
(function() {
  var card = document.currentScript.previousElementSibling;
  var svg = card.querySelector('.gc-chart-wrap svg');
  var wrap = svg.parentElement;
  var tooltip = wrap.querySelector('.gc-tooltip');
  svg.querySelectorAll('.gc-hit').forEach(function(hit) {
    function show() {
      tooltip.innerHTML = '<div class="gc-tooltip-val">' + hit.getAttribute('data-label') + '</div>' +
        '<div class="gc-tooltip-label">' + hit.getAttribute('data-val') + '</div>';
      var b = hit.getBoundingClientRect(), w = wrap.getBoundingClientRect();
      tooltip.style.left = Math.min(Math.max(b.left - w.left + b.width / 2 - 130, 0), w.width - 260) + 'px';
      tooltip.style.top = Math.max(b.top - w.top - 56, 0) + 'px';
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
