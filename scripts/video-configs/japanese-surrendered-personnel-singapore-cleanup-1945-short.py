"""Shorts config for "The Japanese Soldiers Who Rebuilt Postwar Singapore
Were Never Called Prisoners."

Excerpt: the opening hook, sentences 0-4 (0 -> 43.75s, a real sentence
boundary in the timing.json). The Jan 1947 drain-strike vignette
through the payoff line - "Officially they were not prisoners of war,
and that distinction was the whole point."

3 slides: SE4843 (civilians watching the POWs at work) -> IND4826 (the
army that ran the island, marched to labour) -> SE4843 (the Straits
Times photo, and the caption that would not name them).
"""

WIDTH, HEIGHT = 1080, 1920

_C = "https://upload.wikimedia.org/wikipedia/commons"

IMAGES = {
    "SE4843": f"{_C}/7/70/The_British_Reoccupation_of_Singapore_SE4843.jpg",
    "IND4826": f"{_C}/e/e5/British_Reoccupation_of_Singapore%2C_1945_IND4826.jpg",
}

SLIDES = [
    {"img": "SE4843", "type": "letterbox", "zoom": [1, 1.05, 1.10], "pan": [(0.5, 0.5), (0.5, 0.5), (0.5, 0.5)], "ease": "ease-in-out"},
    {"img": "IND4826", "type": "letterbox", "zoom": [1, 1.05, 1.10], "pan": [(0.5, 0.5), (0.5, 0.5), (0.5, 0.5)], "ease": "ease-in"},
    {"img": "SE4843", "type": "letterbox", "zoom": [1.10, 1.05, 1], "pan": [(0.5, 0.5), (0.5, 0.5), (0.5, 0.5)], "ease": "ease-out"},
]

# Real sentence starts from the timing.json: s2 at 19.48, s3 at 25.15.
SCHEDULE = [(0.0, 0), (19.48, 1), (25.15, 2)]
TOTAL_DURATION = 43.75
TIMING_JSON = "audio/japanese-surrendered-personnel-singapore-cleanup-1945.timing.json"

# Shorts want smaller/higher captions than the landscape default:
CAPTION_FONT_RATIO = 0.032
CAPTION_MAX_WIDTH_FRAC = 0.86
CAPTION_Y_FRAC = 0.80
