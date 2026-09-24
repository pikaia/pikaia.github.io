"""Short config for the Spanish dollar post.

Excerpt: the opening hook (sentences 0-3, 0.0-40.65s) - the 1824 treaty priced in
Spanish dollars, "and it stayed Singapore's everyday money for another eighty
years." Ends exactly where sentence 4 begins in the main config's own timing.
"""

WIDTH, HEIGHT = 1080, 1920

_U = "https://upload.wikimedia.org/wikipedia/commons"

IMAGES = {
    "COINSG": f"{_U}/3/33/1789_Charles_IV_Spanish_dollar_countermarked_with_Chinese_words_meaning_%22Singapore%22.jpg",
    "PILLAR": f"{_U}/f/f9/Mexico_Carlos_III_Pillar_Dollar_of_8_Reales_1771.jpg",
}

_CNA = {"type": "letterbox", "zoom": [1.0, 1.05, 1.1], "pan": [(0.5, 0.5)] * 3, "ease": "ease-in-out"}
_PLA = {"type": "letterbox", "zoom": [1.0, 1.05, 1.1], "pan": [(0.5, 0.5)] * 3, "ease": "ease-in-out"}

SLIDES = [
    {"img": "COINSG", **_CNA},  # s0-1 title + 1824, the bill written in a foreign coin
    {"img": "PILLAR", **_PLA},  # s2-3 33,200 dollars; struck in Mexico and Peru
]

SCHEDULE = [(0.0, 0), (14.72, 1)]
TOTAL_DURATION = 40.65
TIMING_JSON = "audio/the-spanish-dollar-that-ruled-singapores-early-economy.timing.json"

BURN_CAPTIONS = True
CAPTION_FONT_RATIO = 0.032
CAPTION_MAX_WIDTH_FRAC = 0.86
CAPTION_Y_FRAC = 0.80
