"""The silver dollar's falling sterling value, and the 1906 fixed rate, for the Straits dollar post.

What one dollar in Singapore was worth in British pence (12 pence to the
shilling), from Walter Makepeace et al., One Hundred Years of Singapore (1921),
vol. 2: about 4s 6d around 1870; nearly 10d more than the 1893 average around
1890; about 2s 7d in 1893; about 2s 2d in 1896; as low as about 1s 6d in 1902;
then fixed at 2s 4d (28 pence) on 29 January 1906. The scanned text garbles the
fractions of a penny, so every figure is rounded and labelled "about".

    python scripts/render_straits_dollar_chart.py          # PNG (dark video slide)
    python scripts/render_straits_dollar_chart.py --svg    # prints the post's inline card HTML
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from render_endau_charts import render_png, svg_card  # noqa: E402

CHART = {
    "out": Path(__file__).resolve().parent.parent / "assets" / "images" / "straits-dollar-value-chart.png",
    "title": "What a dollar was worth in British money",
    "sub": "Value of one silver dollar in Singapore, in British pence (12 pence to the shilling)",
    "foot": "Source: W. Makepeace et al., One Hundred Years of Singapore (1921), vol. 2. Figures rounded; the scanned text garbles fractions.",
    "unit": "d", "vmax": 60, "step": 10, "tick": lambda v: f"{v}d",
    "legend": [("a", "Silver dollar, falling with the price of silver"), ("b", "Straits dollar, fixed from 1906")],
    "rows": [
        ("About 1870", 54, "a", "about 54d (4s 6d)", "Around 1870 a dollar was worth about four shillings and sixpence"),
        ("About 1890", 41, "a", "about 41d", "Around 1890, nearly 10 pence more than the 1893 average"),
        ("1893", 31, "a", "about 31d (2s 7d)", "The 1893 average, the year the first calls for a fixed value were made"),
        ("1896", 26, "a", "about 26d (2s 2d)", "The 1896 average"),
        ("1902, at its lowest", 18, "a", "about 18d (1s 6d)", "In 1902 the dollar fell to about one shilling and sixpence"),
        ("Fixed, 29 Jan 1906", 28, "b", "28d (2s 4d)", "Fixed at two shillings and fourpence on 29 January 1906"),
    ],
}


if __name__ == "__main__":
    if "--svg" in sys.argv:
        svg_card(CHART)
    else:
        render_png(CHART)
