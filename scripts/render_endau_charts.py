"""Two charts for the Endau settlement post, each a PNG video slide and an inline card.

rice: the monthly rice ration per person, in katis, in Syonan (20 at the start
of the Occupation, falling to 8 for men, 6 for women and 4 for children; Lee
Geok Boi, BiblioAsia 2019) and at Endau (18 in the first months, later 4 to 5;
the settler Wan Leong Gay's oral history, via Huang 2020).

food: the share of what Singapore eats that is produced locally, 2025 against
the 2035 targets of Singapore Food Story 2 (Singapore Food Agency, Singapore
Food Statistics 2025): fibre 8% against 20%, protein 25% against 30%.

    python scripts/render_endau_charts.py              # both PNGs (dark video slides)
    python scripts/render_endau_charts.py --svg rice   # prints that chart's inline card HTML
"""
import sys
from pathlib import Path

from PIL import Image, ImageDraw

sys.path.insert(0, str(Path(__file__).resolve().parent))
from render_gift_chart import SCRIPT, STYLE  # noqa: E402
from watch_video_lib import (  # noqa: E402
    CHART_BG, CHART_GRID, CHART_MUTED, CHART_SECONDARY, CHART_TEXT, load_font,
)

ASSETS = Path(__file__).resolve().parent.parent / "assets" / "images"
PNG_COL = {"a": (57, 135, 229), "b": (31, 166, 31), "neutral": (110, 108, 102)}
SVG_VAR = {"a": "--series-1", "b": "--series-2", "neutral": "--neutral"}

CHARTS = {
    "rice": {
        "out": ASSETS / "endau-rice-ration-chart.png",
        "title": "Rice for one person for a month",
        "sub": "Katis of rice per person per month (1 kati is about 0.6 kg)",
        "foot": "Sources: Lee Geok Boi, BiblioAsia (2019); Wan Leong Gay, oral history, National Archives of Singapore, via Huang (2020).",
        "unit": "", "vmax": 20, "step": 5, "tick": lambda v: f"{v}",
        "legend": [("a", "Syonan (Singapore)"), ("b", "Endau settlement")],
        "rows": [
            ("Syonan, early Occupation", 20, "a", "20", "The rice ration in Syonan started at 20 katis a person a month"),
            ("Endau, first months", 18, "b", "18", "Endau settlers were given 18 katis a month for the first few months"),
            ("Syonan, later: men", 8, "a", "8", "Later in the Occupation the Syonan ration fell to 8 katis for men"),
            ("Syonan, later: women", 6, "a", "6", "6 katis for women"),
            ("Endau, later", 4.5, "b", "4-5", "At Endau the ration later fell to 4 or 5 katis a month"),
            ("Syonan, later: children", 4, "a", "4", "4 katis for each child"),
        ],
    },
    "food": {
        "out": ASSETS / "singapore-local-food-share-chart.png",
        "title": "How much of its food Singapore grows",
        "sub": "Share of what Singapore eats that is produced locally",
        "foot": "Source: Singapore Food Agency, Singapore Food Statistics 2025. Fibre: vegetables, beansprouts, mushrooms. Protein: eggs, seafood.",
        "unit": "%", "vmax": 40, "step": 10, "tick": lambda v: f"{v}%",
        "legend": [("a", "2025"), ("neutral", "2035 target")],
        "rows": [
            ("Fibre, 2025", 8, "a", "8%", "About 8% of the fibre Singapore ate in 2025 was grown locally"),
            ("Fibre, 2035 target", 20, "neutral", "20%", "Target: 20% of fibre from local farms by 2035"),
            ("Protein, 2025", 25, "a", "25%", "About 25% of the protein (eggs and seafood) was produced locally in 2025"),
            ("Protein, 2035 target", 30, "neutral", "30%", "Target: 30% of protein from local farms by 2035"),
        ],
    },
}


def render_png(c):
    W, H, SS = 1280, 720, 2
    img = Image.new("RGB", (W * SS, H * SS), CHART_BG)
    d = ImageDraw.Draw(img)
    d.text((60 * SS, 40 * SS), c["title"], font=load_font(34 * SS), fill=CHART_TEXT)
    d.text((60 * SS, 84 * SS), c["sub"], font=load_font(19 * SS, bold=False), fill=CHART_SECONDARY)
    d.text((60 * SS, 680 * SS), c["foot"], font=load_font(14 * SS, bold=False), fill=CHART_MUTED)
    lx = 60
    for key, lab in c["legend"]:
        d.rectangle([lx * SS, 122 * SS, (lx + 14) * SS, 136 * SS], fill=PNG_COL[key])
        d.text(((lx + 22) * SS, 129 * SS), lab, font=load_font(17 * SS, bold=False), fill=CHART_SECONDARY, anchor="lm")
        lx += 40 + int(d.textlength(lab, font=load_font(17, bold=False)))
    x0, x1, top, bottom = 380, 1180, 160, 590
    sx = lambda v: (x0 + v / c["vmax"] * (x1 - x0)) * SS  # noqa: E731
    for v in range(0, c["vmax"] + 1, c["step"]):
        d.line([(sx(v), top * SS), (sx(v), bottom * SS)], fill=CHART_GRID if v else CHART_MUTED, width=SS)
        d.text((sx(v), 612 * SS), c["tick"](v), font=load_font(15 * SS, bold=False), fill=CHART_MUTED, anchor="mm")
    rowh = (bottom - top) / len(c["rows"])
    bh = min(44, rowh * 0.6)
    for i, (lab, v, key, vlab, _) in enumerate(c["rows"]):
        cy = top + rowh * (i + 0.5)
        d.text(((x0 - 18) * SS, cy * SS), lab, font=load_font(19 * SS), fill=CHART_TEXT, anchor="rm")
        d.rectangle([sx(0), (cy - bh / 2) * SS, sx(v), (cy + bh / 2) * SS], fill=PNG_COL[key])
        d.text((sx(v) + 12 * SS, cy * SS), vlab, font=load_font(19 * SS), fill=CHART_TEXT, anchor="lm")
    img.resize((W, H), Image.LANCZOS).save(c["out"])
    print("wrote", c["out"])


def svg_card(c):
    x0, x1, top, rowh = 190, 740, 10, 40
    sx = lambda v: x0 + v / c["vmax"] * (x1 - x0)  # noqa: E731
    n = len(c["rows"])
    h = top + rowh * n + 30
    aria = c["title"] + ". " + "; ".join(f"{lab}: {vlab}" for lab, _, _, vlab, _ in c["rows"]) + "."
    s = [f'<svg viewBox="0 0 800 {h}" width="100%" height="auto" role="img" aria-label="{aria}">']
    for v in range(0, c["vmax"] + 1, c["step"]):
        s.append(f'  <line x1="{sx(v):.1f}" y1="{top}" x2="{sx(v):.1f}" y2="{top + rowh * n}" stroke="var({"--axis" if v == 0 else "--grid"})"/>')
        s.append(f'  <text class="gc-axis" x="{sx(v):.1f}" y="{top + rowh * n + 16}" text-anchor="middle">{c["tick"](v)}</text>')
    for i, (lab, v, key, vlab, tip) in enumerate(c["rows"]):
        cy = top + rowh * (i + 0.5)
        s.append(f'  <text class="gc-row" x="{x0 - 10}" y="{cy + 5:.1f}" text-anchor="end">{lab}</text>')
        s.append(f'  <g class="gc-hit" tabindex="0" data-label="{lab}: {vlab}" data-val="{tip}">'
                 f'<rect x="{x0}" y="{cy - 12:.1f}" width="{sx(v) - x0:.1f}" height="24" rx="3" fill="var({SVG_VAR[key]})"/></g>')
        s.append(f'  <text class="gc-seg" x="{sx(v) + 8:.1f}" y="{cy + 4:.1f}">{vlab}</text>')
    s.append("</svg>")
    legend = "\n".join(f'    <span><i class="gc-swatch" style="background: var({SVG_VAR[k]})"></i>{lab}</span>' for k, lab in c["legend"])
    rows = "\n".join(f"        <tr><td>{lab}</td><td>{vlab}</td><td>{tip}</td></tr>" for lab, _, _, vlab, tip in c["rows"])
    print(STYLE + f"""
<div class="gc-card">
  <p class="gc-title">{c["title"]}</p>
  <p class="gc-subtitle">{c["sub"]}</p>
  <div class="gc-legend">
{legend}
  </div>
  <div class="gc-chart-wrap">
{chr(10).join("    " + line for line in s)}
    <div class="gc-tooltip"></div>
  </div>
  <p class="gc-foot">{c["foot"]}</p>
  <details class="gc-details">
    <summary>View as table</summary>
    <table class="gc-table">
      <thead><tr><th>Row</th><th>Value</th><th>Detail</th></tr></thead>
      <tbody>
{rows}
      </tbody>
    </table>
  </details>
</div>
""" + SCRIPT + "\n</div>")


if __name__ == "__main__":
    if "--svg" in sys.argv:
        svg_card(CHARTS[sys.argv[sys.argv.index("--svg") + 1]])
    else:
        for c in CHARTS.values():
            render_png(c)
