"""Shorts config for "The Japanese Garden That Reconciliation Built, Then
Forgot" (Seiwaen, Jurong).

Excerpt: the opening hook, sentences 1-3 (0 -> 48.65s, a real sentence
boundary in the timing.json). "When the Japanese Garden reopened in
2024 ... water lilies, a sunken garden, a Breathing Gallery of
terrariums" -> "nothing in the coverage explained why there was a
Japanese garden at Jurong Lake in the first place" -> "fifty years
earlier, its 1973 opening was one of the more understated acts of
postwar reconciliation with the country whose army had occupied it."

3 slides: MOONBRIDGE (the 2024 reopening) -> REDBRIDGE (the garden
itself) -> JGMAP (the Jurong Lake locations map).
"""

WIDTH, HEIGHT = 1080, 1920

_C = "https://upload.wikimedia.org/wikipedia/commons"

IMAGES = {
    "MOONBRIDGE": f"{_C}/a/ac/Moon_bridge%2C_Japanese_Garden%2C_Singapore_202409.jpg",
    "REDBRIDGE": f"{_C}/0/08/Redbridge_%288166305323%29.jpg",
    "JGMAP": "/assets/images/japanese-garden-jurong-lake-map.png",
}

CREDITS = {
    "JGMAP": "Locations map by Lesser Known Singapore; base map data © OpenStreetMap contributors",
}

SLIDES = [
    {"img": "MOONBRIDGE", "type": "letterbox", "zoom": [1, 1.06, 1.12], "pan": [(0.5, 0.5), (0.5, 0.5), (0.5, 0.5)], "ease": "ease-in-out"},
    {"img": "REDBRIDGE", "type": "letterbox", "zoom": [1, 1.06, 1.12], "pan": [(0.5, 0.5), (0.5, 0.5), (0.5, 0.5)], "ease": "ease-in"},
    {"img": "JGMAP", "type": "letterbox", "zoom": [1, 1.02, 1.04], "pan": [(0.5, 0.5), (0.5, 0.5), (0.5, 0.5)], "ease": "linear"},
]

# Real sentence starts from the timing.json: s2 at 23.975, s3 at 32.05.
SCHEDULE = [(0.0, 0), (23.975, 1), (32.05, 2)]
TOTAL_DURATION = 48.65
TIMING_JSON = "audio/japanese-garden-jurong-seiwaen-reconciliation.timing.json"

# Shorts keep burned-in narration captions (muted autoplay); main videos do not -
# they rely on the uploaded .srt. The lines below size the caption box:
BURN_CAPTIONS = True
CAPTION_FONT_RATIO = 0.032
CAPTION_MAX_WIDTH_FRAC = 0.86
CAPTION_Y_FRAC = 0.80
