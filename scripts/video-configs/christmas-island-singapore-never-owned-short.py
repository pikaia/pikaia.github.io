"""Shorts config for "Singapore 'Sold' Christmas Island in 1958 - Except It
Never Owned It".

Excerpt: the opening hook, sentences 1-4 (0 -> 36.625s, a real sentence
boundary in the timing.json). "Ask most Singaporeans and you'll hear
Singapore owned Christmas Island and sold it cheap to Australia in 1958"
-> "it's a tidy story ... it's also wrong: Singapore never owned it, so
there was nothing for it to sell."

2 slides: COVE (the island) -> MAP (Singapore and Christmas Island
~1,550 km apart - nothing like a neighbouring island to sell).
"""

WIDTH, HEIGHT = 1080, 1920

_C = "https://upload.wikimedia.org/wikipedia/commons"

IMAGES = {
    "COVE": f"{_C}/6/6b/Flying_Fish_Cove_%2825341355156%29.jpg",
    "MAP": "/assets/images/osm-singapore-christmas-island.png",
}

CREDITS = {
    "MAP": "Locator map: map data © OpenStreetMap contributors",
}

SLIDES = [
    {"img": "COVE", "type": "letterbox", "zoom": [1, 1.06, 1.12], "pan": [(0.5, 0.5), (0.5, 0.5), (0.5, 0.5)], "ease": "ease-in-out"},
    {"img": "MAP", "type": "letterbox", "zoom": [1, 1.05, 1.10], "pan": [(0.5, 0.5), (0.5, 0.5), (0.5, 0.5)], "ease": "ease-in"},
]

# Real sentence start from the timing.json: s2 at 19.45.
SCHEDULE = [(0.0, 0), (19.45, 1)]
TOTAL_DURATION = 36.625
TIMING_JSON = "audio/christmas-island-singapore-never-owned.timing.json"

# Shorts want smaller/higher captions than the landscape default:
CAPTION_FONT_RATIO = 0.032
CAPTION_MAX_WIDTH_FRAC = 0.86
CAPTION_Y_FRAC = 0.80
