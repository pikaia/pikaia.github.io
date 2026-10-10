"""Chinese letters sent home through Singapore's Chinese Sub-Post Office, for the remittance-houses post.

From T. A. Melville, "The Post Office and Its History", in Walter Makepeace
et al., One Hundred Years of Singapore (1921), vol. 2: about 80,000 letters
in 1880, 77,000 in 1881, 90,876 in 1882, 180,000 in 1886 and 280,000 in
1889; the coolie letters in clubbed packets "exceeded a million" in 1914 and
were "still over a million" in 1917, so those two are drawn at one million
and marked as lower bounds.

    python scripts/render_qiaopi_letters_chart.py          # PNG (dark video slide)
    python scripts/render_qiaopi_letters_chart.py --svg    # prints the post's inline card HTML
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from render_endau_charts import render_png, svg_card  # noqa: E402

CHART = {
    "out": Path(__file__).resolve().parent.parent / "assets" / "images" / "qiaopi-letters-chart.png",
    "title": "Letters home to China through Singapore's post office",
    "sub": "Chinese letters sent each year through the Chinese Sub-Post Office, in thousands",
    "foot": "Source: T. A. Melville, in W. Makepeace et al., One Hundred Years of Singapore (1921), vol. 2. 1914 and 1917 reported only as over a million.",
    "unit": "", "vmax": 1200, "step": 200, "tick": lambda v: f"{v}k" if v else "0",
    "legend": [("a", "Letters counted that year"), ("b", "Reported as over a million")],
    "rows": [
        ("1880", 80, "a", "about 80,000", "About 80,000 Chinese letters went through the sub-post office in 1880"),
        ("1881", 77, "a", "about 77,000", "About 77,000 in 1881"),
        ("1882", 91, "a", "90,876", "90,876 in 1882"),
        ("1886", 180, "a", "about 180,000", "About 180,000 in 1886"),
        ("1889", 280, "a", "about 280,000", "About 280,000 in 1889"),
        ("1914", 1000, "b", "over a million", "In 1914 the letters in clubbed packets exceeded a million"),
        ("1917", 1000, "b", "over a million", "Still over a million in 1917"),
    ],
}


if __name__ == "__main__":
    if "--svg" in sys.argv:
        svg_card(CHART)
    else:
        render_png(CHART)
