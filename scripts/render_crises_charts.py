"""Charts for the Great Depression / contagion post, from official data in
assets/data/singapore-crises-data.json (SingStat tables M015721 and M450981):

  assets/images/singapore-gdp-growth-chart.png       - annual real GDP growth,
      1961-2025, falls in red, each recession year labelled
  assets/images/singapore-crisis-sectors-chart.png   - growth of five industries
      in each crisis year (1985, 1998, 2001, 2009, 2020)
  assets/images/singapore-electronics-share-chart.png - electronics' share of
      non-oil domestic exports, 1997-2025

PNGs are the dark-theme video/Watch "chart" slides. With --svg the script
instead prints the post's inline SVG markup for the same three charts (theme
tokens, per-mark hover data attributes), to paste into the post.

    python scripts/render_crises_charts.py [--svg]
"""
import json
import sys
from pathlib import Path

from PIL import Image, ImageDraw

sys.path.insert(0, str(Path(__file__).resolve().parent))
from watch_video_lib import (  # noqa: E402
    CHART_BG, CHART_GRID, CHART_MUTED, CHART_SECONDARY, CHART_TEXT, load_font,
)

ROOT = Path(__file__).resolve().parent.parent
DATA = json.loads((ROOT / "assets" / "data" / "singapore-crises-data.json").read_text(encoding="utf-8"))
IMG = ROOT / "assets" / "images"
W, H, SS = 1280, 720, 2
UP = (57, 135, 229)     # #3987e5, dark-mode diverging blue (growth)
DOWN = (230, 103, 103)  # #e66767, dark-mode diverging red (fall)

GROWTH = {int(k): v for k, v in DATA["growth"].items()}
CRISIS = {int(k): v for k, v in DATA["crisis"].items()}
SHARE = {int(k): v for k, v in DATA["share"].items()}
LABELS = {1964: "1964", 1985: "1985", 1998: "1998", 2001: "2001", 2009: "2009", 2020: "2020"}
CRISIS_NAMES = {1985: "1985 recession", 1998: "Asian financial crisis", 2001: "Dot-com bust",
                2009: "Global financial crisis", 2020: "Pandemic"}
SECTORS = list(next(iter(CRISIS.values())).keys())


def _frame(title, sub, foot):
    img = Image.new("RGB", (W * SS, H * SS), CHART_BG)
    d = ImageDraw.Draw(img)
    d.text((60 * SS, 40 * SS), title, font=load_font(34 * SS), fill=CHART_TEXT)
    d.text((60 * SS, 84 * SS), sub, font=load_font(19 * SS, bold=False), fill=CHART_SECONDARY)
    d.text((60 * SS, 680 * SS), foot, font=load_font(14 * SS, bold=False), fill=CHART_MUTED)
    return img, d


def _save(img, name):
    img.resize((W, H), Image.LANCZOS).save(IMG / name)
    print("wrote", IMG / name)


def gdp_png():
    img, d = _frame("Singapore's economy, year by year", "Annual growth of real GDP, 1961 to 2025",
                    "Source: Singapore Department of Statistics, GDP in chained (2015) dollars (table M015721).")
    x0, x1, vmin, vmax, top, bot = 110, 1220, -6, 16, 140, 600
    zy = top + (vmax - 0) / (vmax - vmin) * (bot - top)
    sy = lambda v: (top + (vmax - v) / (vmax - vmin) * (bot - top)) * SS  # noqa: E731
    f = load_font(15 * SS, bold=False)
    for v in (-5, 0, 5, 10, 15):
        d.line([(x0 * SS, sy(v)), (x1 * SS, sy(v))], fill=CHART_GRID if v else CHART_MUTED, width=SS)
        d.text(((x0 - 12) * SS, sy(v)), f"{v}%", font=f, fill=CHART_MUTED, anchor="rm")
    years = sorted(GROWTH)
    step = (x1 - x0) / len(years)
    for i, yv in enumerate(years):
        v = GROWTH[yv]
        bx = (x0 + i * step + step * 0.15) * SS
        bw = step * 0.7 * SS
        d.rectangle([bx, min(sy(v), zy * SS), bx + bw, max(sy(v), zy * SS)], fill=DOWN if v < 0 else UP)
        if yv in LABELS:
            lab = f"{LABELS[yv]}: {v:+.1f}%"
            yy = sy(min(v, 0)) + 16 * SS if v < 1 else sy(v) - 14 * SS  # near-zero years: below the axis
            d.text((bx + bw / 2, yy), lab, font=load_font(14 * SS), fill=CHART_TEXT, anchor="mm")
        if yv % 10 == 0:
            d.text((bx + bw / 2, (bot + 22) * SS), str(yv), font=f, fill=CHART_MUTED, anchor="mm")
    _save(img, "singapore-gdp-growth-chart.png")


def sectors_png():
    img, d = _frame("Where each crisis hit hardest", "Growth of five industries in each crisis year (real terms)",
                    "Source: Singapore Department of Statistics, GDP by industry in chained (2015) dollars (table M015721).")
    years = sorted(CRISIS)
    lab_w, x0, x1, top, bot = 300, 330, 1230, 160, 610
    col = (x1 - x0) / len(years)
    rowh = (bot - top - 40) / len(SECTORS)
    scale = col * 0.27 / 42  # px per percentage point: +22.3 and -41.7 labels side by side still fit
    fh, fv, fl = load_font(16 * SS), load_font(14 * SS, bold=False), load_font(17 * SS)
    for j, yv in enumerate(years):
        cx = x0 + col * (j + 0.5)
        d.text((cx * SS, (top + 4) * SS), str(yv), font=fh, fill=CHART_TEXT, anchor="mm")
        d.text((cx * SS, (top + 24) * SS), CRISIS_NAMES[yv], font=fv, fill=CHART_SECONDARY, anchor="mm")
        d.line([(cx * SS, (top + 40) * SS), (cx * SS, bot * SS)], fill=CHART_MUTED, width=SS)
    for i, s in enumerate(SECTORS):
        cy = top + 40 + rowh * (i + 0.5)
        d.text(((lab_w + 10) * SS, cy * SS), s, font=fl, fill=CHART_TEXT, anchor="rm")
        for j, yv in enumerate(years):
            v = CRISIS[yv][s]
            cx = x0 + col * (j + 0.5)
            ex = cx + v * scale
            d.rectangle([min(cx, ex) * SS, (cy - 9) * SS, max(cx, ex) * SS, (cy + 9) * SS], fill=DOWN if v < 0 else UP)
            tx, anc = (ex - 6, "rm") if v < 0 else (ex + 6, "lm")
            d.text((tx * SS, cy * SS), f"{v:+.1f}", font=fv, fill=CHART_SECONDARY, anchor=anc)
    _save(img, "singapore-crisis-sectors-chart.png")


def share_png():
    img, d = _frame("Less riding on electronics", "Electronics as a share of Singapore's non-oil domestic exports, 1997 to 2025",
                    "Source: Singapore Department of Statistics, domestic exports of major non-oil products (table M450981).")
    years = sorted(SHARE)
    x0, x1, top, bot = 110, 1200, 150, 600
    sx = lambda yv: (x0 + (yv - years[0]) / (years[-1] - years[0]) * (x1 - x0)) * SS  # noqa: E731
    sy = lambda v: (bot - v / 80 * (bot - top)) * SS  # noqa: E731
    f = load_font(15 * SS, bold=False)
    for v in (0, 20, 40, 60, 80):
        d.line([(x0 * SS, sy(v)), (x1 * SS, sy(v))], fill=CHART_GRID if v else CHART_MUTED, width=SS)
        d.text(((x0 - 12) * SS, sy(v)), f"{v}%", font=f, fill=CHART_MUTED, anchor="rm")
    for yv in (2000, 2005, 2010, 2015, 2020, 2025):
        d.text((sx(yv), (bot + 22) * SS), str(yv), font=f, fill=CHART_MUTED, anchor="mm")
    d.line([(sx(yv), sy(SHARE[yv])) for yv in years], fill=UP, width=4 * SS, joint="curve")
    for yv in (2000, 2025):
        x, y = sx(yv), sy(SHARE[yv])
        d.ellipse([x - 7 * SS, y - 7 * SS, x + 7 * SS, y + 7 * SS], fill=CHART_BG, outline=UP, width=3 * SS)
        d.text((x, y - 22 * SS), f"{yv}: {SHARE[yv]:.0f}%", font=load_font(16 * SS), fill=CHART_TEXT, anchor="mm")
    _save(img, "singapore-electronics-share-chart.png")


def svg():
    """Inline SVG for the post (theme tokens; hover data on every mark)."""
    out = []
    # GDP growth bars
    x0, x1, vmin, vmax, top, bot = 46, 790, -6, 16, 14, 230
    sy = lambda v: top + (vmax - v) / (vmax - vmin) * (bot - top)  # noqa: E731
    years = sorted(GROWTH)
    step = (x1 - x0) / len(years)
    g = ['<svg viewBox="0 0 800 260" width="100%" height="auto" role="img" aria-label="Bar chart of Singapore\'s annual real GDP growth from 1961 to 2025. Growth was negative in 1964 (-3.1%), 1985 (-0.6%), 1998 (-2.2%), 2001 (-1.1%) and 2020 (-3.6%), and close to zero in 2009 (0.1%).">']
    for v in (-5, 0, 5, 10, 15):
        g.append(f'  <line x1="{x0}" y1="{sy(v):.1f}" x2="{x1}" y2="{sy(v):.1f}" stroke="var({"--axis" if v == 0 else "--grid"})"/>')
        g.append(f'  <text class="cc-axis" x="{x0 - 6}" y="{sy(v) + 4:.1f}" text-anchor="end">{v}%</text>')
    for i, yv in enumerate(years):
        v = GROWTH[yv]
        bx, bw = x0 + i * step + step * 0.15, step * 0.7
        y0, y1 = min(sy(v), sy(0)), max(sy(v), sy(0))
        g.append(f'  <g class="cc-hit" tabindex="0" data-label="{yv}" data-val="Real GDP growth {v:+.1f}%">'
                 f'<rect x="{bx:.1f}" y="{y0:.1f}" width="{bw:.1f}" height="{max(y1 - y0, 0.8):.1f}" rx="1.5" fill="var({"--down" if v < 0 else "--up"})"/></g>')
        if yv in LABELS:
            yy = sy(min(v, 0)) + 12 if v < 1 else sy(v) - 5
            g.append(f'  <text class="cc-lab" x="{bx + bw / 2:.1f}" y="{yy:.1f}" text-anchor="middle">{LABELS[yv]}</text>')
        if yv % 10 == 0:
            g.append(f'  <text class="cc-axis" x="{bx + bw / 2:.1f}" y="{bot + 18}" text-anchor="middle">{yv}</text>')
    g.append("</svg>")
    out.append("\n".join(g))
    # Sector small multiples
    yrs = sorted(CRISIS)
    lab_w, x0, x1, top = 150, 160, 795, 40
    col = (x1 - x0) / len(yrs)
    rowh = 34
    scale = col * 0.27 / 42
    aria = "; ".join(f"{yv}: " + ", ".join(f"{s.lower()} {CRISIS[yv][s]:+.1f}%" for s in SECTORS) for yv in yrs)
    s = [f'<svg viewBox="0 0 800 {top + rowh * len(SECTORS) + 10}" width="100%" height="auto" role="img" aria-label="Growth of five industries in each crisis year. {aria}.">']
    for j, yv in enumerate(yrs):
        cx = x0 + col * (j + 0.5)
        s.append(f'  <text class="cc-colhead" x="{cx:.1f}" y="14" text-anchor="middle">{yv}</text>')
        s.append(f'  <text class="cc-colsub" x="{cx:.1f}" y="28" text-anchor="middle">{CRISIS_NAMES[yv]}</text>')
        s.append(f'  <line x1="{cx:.1f}" y1="{top - 4}" x2="{cx:.1f}" y2="{top + rowh * len(SECTORS)}" stroke="var(--axis)"/>')
    for i, sec in enumerate(SECTORS):
        cy = top + rowh * (i + 0.5)
        s.append(f'  <text class="cc-row" x="{lab_w}" y="{cy + 4:.1f}" text-anchor="end">{sec}</text>')
        for j, yv in enumerate(yrs):
            v = CRISIS[yv][sec]
            cx = x0 + col * (j + 0.5)
            ex = cx + v * scale
            s.append(f'  <g class="cc-hit" tabindex="0" data-label="{sec}, {yv}" data-val="{v:+.1f}% in real terms">'
                     f'<rect x="{min(cx, ex):.1f}" y="{cy - 7:.1f}" width="{max(abs(ex - cx), 0.8):.1f}" height="14" rx="2" fill="var({"--down" if v < 0 else "--up"})"/></g>')
            tx, anc = (ex - 4, "end") if v < 0 else (ex + 4, "start")
            s.append(f'  <text class="cc-val" x="{tx:.1f}" y="{cy + 4:.1f}" text-anchor="{anc}">{v:+.1f}</text>')
    s.append("</svg>")
    out.append("\n".join(s))
    # Electronics share line
    yrs = sorted(SHARE)
    x0, x1, top, bot = 46, 780, 20, 200
    sx = lambda yv: x0 + (yv - yrs[0]) / (yrs[-1] - yrs[0]) * (x1 - x0)  # noqa: E731
    syy = lambda v: bot - v / 80 * (bot - top)  # noqa: E731
    e = [f'<svg viewBox="0 0 800 230" width="100%" height="auto" role="img" aria-label="Line chart of electronics as a share of Singapore\'s non-oil domestic exports, from {SHARE[1997]:.0f}% in 1997 and {SHARE[2000]:.0f}% in 2000 down to {SHARE[2023]:.0f}% in 2023 and {SHARE[2025]:.0f}% in 2025.">']
    for v in (0, 20, 40, 60, 80):
        e.append(f'  <line x1="{x0}" y1="{syy(v):.1f}" x2="{x1}" y2="{syy(v):.1f}" stroke="var({"--axis" if v == 0 else "--grid"})"/>')
        e.append(f'  <text class="cc-axis" x="{x0 - 6}" y="{syy(v) + 4:.1f}" text-anchor="end">{v}%</text>')
    for yv in (2000, 2005, 2010, 2015, 2020, 2025):
        e.append(f'  <text class="cc-axis" x="{sx(yv):.1f}" y="{bot + 18}" text-anchor="middle">{yv}</text>')
    pts = " ".join(f"{sx(yv):.1f},{syy(SHARE[yv]):.1f}" for yv in yrs)
    e.append(f'  <polyline points="{pts}" fill="none" stroke="var(--up)" stroke-width="2" stroke-linejoin="round"/>')
    for yv in yrs:
        r = 4 if yv in (2000, 2025) else 3
        e.append(f'  <g class="cc-hit" tabindex="0" data-label="{yv}" data-val="Electronics {SHARE[yv]:.1f}% of non-oil domestic exports">'
                 f'<circle cx="{sx(yv):.1f}" cy="{syy(SHARE[yv]):.1f}" r="9" fill="transparent"/>'
                 f'<circle class="cc-dot" cx="{sx(yv):.1f}" cy="{syy(SHARE[yv]):.1f}" r="{r}"/></g>')
    for yv in (2000, 2025):
        anchor = "end" if yv == yrs[-1] else "middle"  # the last label would run off the right edge
        e.append(f'  <text class="cc-lab" x="{sx(yv):.1f}" y="{syy(SHARE[yv]) - 10:.1f}" text-anchor="{anchor}">{yv}: {SHARE[yv]:.0f}%</text>')
    e.append("</svg>")
    out.append("\n".join(e))
    print("\n\n<!-- next chart -->\n\n".join(out))


if __name__ == "__main__":
    if "--svg" in sys.argv:
        svg()
    else:
        gdp_png()
        sectors_png()
        share_png()
