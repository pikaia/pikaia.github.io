"""Render the static PNG for the Indian convicts post's video/Watch "chart" slide:

  assets/images/convicts-1873-offences-chart.png  - what the convicts still in
      the Straits Settlements in 1873 had been transported for (the post's
      inline bar chart), from McNair's table, bar lengths on a linear 0-600
      scale. Dark theme matching watch_video_lib's chart palette.

    python scripts/render_convict_crimes_chart.py
"""
import sys
from pathlib import Path

from PIL import Image, ImageDraw

sys.path.insert(0, str(Path(__file__).resolve().parent))
from watch_video_lib import (  # noqa: E402
    CHART_BG, CHART_LINE, CHART_MUTED, CHART_SECONDARY, CHART_TEXT, load_font,
)

IMG = Path(__file__).resolve().parent.parent / "assets" / "images"
W, H = 1280, 720
SS = 2
X0, X1, VMAX = 400, 1120, 600

ROWS = [
    ("Dacoity", "armed gang robbery", 581, "581"),
    ("Robbery with murder", "incl. highway and gang robbery", 269, "269"),
    ("Thuggee", "robbing and killing travellers", 256, "256"),
    ("Professional poisoning", "", 21, "21"),
]


def main():
    img = Image.new("RGB", (W * SS, H * SS), CHART_BG)
    d = ImageDraw.Draw(img)
    d.text((60 * SS, 40 * SS), "What the last convicts had been transported for, 1873", font=load_font(34 * SS), fill=CHART_TEXT)
    d.text((60 * SS, 86 * SS), "Convicts in the Straits Settlements when the system ended, four offences (1,127 in all); linear scale",
           font=load_font(19 * SS, bold=False), fill=CHART_SECONDARY)

    def x(v):
        return (X0 + v * (X1 - X0) / VMAX) * SS

    name_f, lab, val = load_font(24 * SS), load_font(17 * SS, bold=False), load_font(24 * SS)
    top, step, bh = 160, 100, 56
    for i, (name, sub, v, vl) in enumerate(ROWS):
        y = (top + i * step) * SS
        if sub:
            d.text(((X0 - 20) * SS, y + 18 * SS), name, font=name_f, fill=CHART_TEXT, anchor="rm")
            d.text(((X0 - 20) * SS, y + 44 * SS), sub, font=lab, fill=CHART_SECONDARY, anchor="rm")
        else:
            d.text(((X0 - 20) * SS, y + 28 * SS), name, font=name_f, fill=CHART_TEXT, anchor="rm")
        d.rounded_rectangle([X0 * SS, y, max(x(v), (X0 + 4) * SS), y + bh * SS], radius=5 * SS, fill=CHART_LINE)
        d.text((max(x(v), (X0 + 4) * SS) + 14 * SS, y + 28 * SS), vl, font=val, fill=CHART_TEXT, anchor="lm")

    base = (top + len(ROWS) * step - 20) * SS
    d.line([(X0 * SS, (top - 12) * SS), (X0 * SS, base)], fill=CHART_MUTED, width=SS)
    tick = load_font(17 * SS, bold=False)
    for t in (0, 200, 400, 600):
        d.text((x(t), base + 24 * SS), str(t), font=tick, fill=CHART_MUTED, anchor="mm")

    d.text((60 * SS, 686 * SS), "Source: J. F. A. McNair and W. D. Bayliss, Prisoners Their Own Warders (1899), page 146.",
           font=load_font(15 * SS, bold=False), fill=CHART_MUTED)
    out = IMG / "convicts-1873-offences-chart.png"
    img.resize((W, H), Image.LANCZOS).save(out)
    print(f"wrote {out}  ({W}x{H})")


if __name__ == "__main__":
    main()
