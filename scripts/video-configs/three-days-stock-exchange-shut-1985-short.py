"""Shorts config for "The Three Days Singapore's Stock Market Closed."

Excerpt: the opening hook, sentences 0-4 (0 -> 35.725s, a real sentence
boundary in the timing.json). On Monday 2 December 1985 the Stock
Exchange of Singapore did not open, and neither did Kuala Lumpur; both
stayed shut for three days, the only time the market has ever closed
completely - forced by one company, Pan-Electric Industries, a
refrigerator maker turned conglomerate, and a web of undisclosed
contracts propping up its share price.

3 slides: the Raffles Place skyline -> Clifford Centre (the exchange's
1980s home) -> Raffles Place in 1971.
"""

WIDTH, HEIGHT = 1080, 1920

_C = "https://upload.wikimedia.org/wikipedia/commons"

IMAGES = {
    "SKYLINE": f"{_C}/1/1e/Singapore_Skyline_Raffles_Place.jpg",
    "CLIFFORD": f"{_C}/b/b8/Clifford_Centre.JPG",
    "RP1971": f"{_C}/d/dc/71-610_Raffles_Place_Singapore_1971_%2851252222815%29.jpg",
}

SLIDES = [
    {"img": "SKYLINE", "type": "letterbox", "zoom": [1, 1.05, 1.10], "pan": [(0.5, 0.5)] * 3, "ease": "ease-in-out"},
    {"img": "CLIFFORD", "type": "letterbox", "zoom": [1, 1.05, 1.10], "pan": [(0.5, 0.5)] * 3, "ease": "ease-in-out"},
    {"img": "RP1971", "type": "letterbox", "zoom": [1, 1.06, 1.12], "pan": [(0.5, 0.5)] * 3, "ease": "ease-in-out"},
]

# Real sentence starts from the timing.json: s2 at 11.65, s4 at 22.075.
SCHEDULE = [(0.0, 0), (11.65, 1), (22.075, 2)]
TOTAL_DURATION = 35.725
TIMING_JSON = "audio/three-days-stock-exchange-shut-1985.timing.json"

# Shorts keep burned-in narration captions (muted autoplay); main videos do not -
# they rely on the uploaded .srt. Caption size/position come from the
# DEFAULT_CAPTION_* module constants (small outlined white text, no box).
BURN_CAPTIONS = True
