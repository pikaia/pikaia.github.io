"""Shorts config for "The Satay Club Moved Four Times. The Satay Stayed
the Same."

Excerpt: the opening hook, sentences 1-5 (0 -> 30.725s, a real sentence
boundary in the timing.json). "I remember going to the Satay Club at
the Esplanade as a kid" -> "when I looked into it properly as an adult,
I found that wasn't where it started" -> "the place moved four times
before it finally closed for good, and the Esplanade ... wasn't its
first home."

3 slides: HERO (satay at the Esplanade Satay Club) -> ESP_VIEW (a
general view of it) -> SATMAP (the locations map: it moved four times).
"""

WIDTH, HEIGHT = 1080, 1920

_C = "https://upload.wikimedia.org/wikipedia/commons"

IMAGES = {
    "HERO": f"{_C}/0/0a/Singapore-Satay-1973-74-WUS08150.jpg",
    "ESP_VIEW": f"{_C}/6/6d/Singapore-Hawker_Centre.1973-74-WUS08151.jpg",
    "SATMAP": "/assets/images/satay-club-locations-map.png",
}

CREDITS = {
    "SATMAP": "Locations map by Lesser Known Singapore; base map data © OpenStreetMap contributors",
}

SLIDES = [
    {"img": "HERO", "type": "letterbox", "zoom": [1, 1.06, 1.12], "pan": [(0.5, 0.5), (0.5, 0.5), (0.5, 0.5)], "ease": "ease-in-out"},
    {"img": "ESP_VIEW", "type": "letterbox", "zoom": [1, 1.06, 1.12], "pan": [(0.5, 0.5), (0.5, 0.5), (0.5, 0.5)], "ease": "ease-in"},
    {"img": "SATMAP", "type": "letterbox", "zoom": [1, 1.02, 1.04], "pan": [(0.5, 0.5), (0.5, 0.5), (0.5, 0.5)], "ease": "linear"},
]

# Real sentence starts from the timing.json: s2 at 5.7, s3 at 15.375.
SCHEDULE = [(0.0, 0), (5.7, 1), (15.375, 2)]
TOTAL_DURATION = 30.725
TIMING_JSON = "audio/satay-club-esplanade-alhambra-history.timing.json"

# Shorts keep burned-in narration captions (muted autoplay); main videos do not -
# they rely on the uploaded .srt. The lines below size the caption box:
BURN_CAPTIONS = True
CAPTION_FONT_RATIO = 0.032
CAPTION_MAX_WIDTH_FRAC = 0.86
CAPTION_Y_FRAC = 0.80
