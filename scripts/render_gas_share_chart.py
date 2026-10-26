"""Natural gas's share of Singapore's electricity, for the gas pipelines post.

Share of the fuel mix for electricity generation: 26% in 2001 (SG101, "Our
Energy Security"); 62% in 2003, 82% in 2009 and 79% in 2010 (EMA, launch of
the inaugural Singapore Energy Statistics, 2011); 95.5% in 2014 (Singapore
Energy Statistics 2015); 94.0% in 2024 (EMA, Singapore Energy Statistics,
chapter 2). The rest was mostly fuel oil and other petroleum products.

    python scripts/render_gas_share_chart.py          # PNG (dark video slide)
    python scripts/render_gas_share_chart.py --svg    # prints the post's inline card HTML
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from render_endau_charts import render_png, svg_card  # noqa: E402

CHART = {
    "out": Path(__file__).resolve().parent.parent / "assets" / "images" / "gas-share-electricity-chart.png",
    "title": "How much of Singapore's electricity comes from gas",
    "sub": "Natural gas's share of the fuel used to generate electricity",
    "foot": "Sources: SG101; Energy Market Authority, Singapore Energy Statistics (2011, 2015, 2025). The rest was mostly fuel oil.",
    "unit": "%", "vmax": 100, "step": 20, "tick": lambda v: f"{v}%",
    "legend": [("a", "Share of electricity generated from natural gas")],
    "rows": [
        ("2001", 26, "a", "26%", "In 2001 natural gas made about 26% of Singapore's electricity; oil made most of the rest"),
        ("2003", 62, "a", "62%", "62% in 2003, after the West Natuna and Grissik pipelines opened"),
        ("2009", 82, "a", "82%", "82% in 2009"),
        ("2010", 79, "a", "79%", "79% in 2010"),
        ("2014", 95.5, "a", "95.5%", "95.5% in 2014, the year after the LNG terminal opened"),
        ("2024", 94, "a", "94%", "94% in 2024"),
    ],
}


if __name__ == "__main__":
    if "--svg" in sys.argv:
        svg_card(CHART)
    else:
        render_png(CHART)
