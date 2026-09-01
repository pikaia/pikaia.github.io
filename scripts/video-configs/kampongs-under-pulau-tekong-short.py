"""Shorts config for "The Kampongs Under Tekong".

Excerpt: the opening hook, sentences 1-4 (0 -> 42.925s, a real sentence
boundary in the timing.json). "Every enlisted man marches through
training areas called Selabin, Permatang, San Yong Kong, without being
told what the names mean" -> "they aren't codenames - they're kampongs,
real villages, that stood on Tekong until it was cleared for the SAF" ->
"all that's left is the geography, still labelled with names nobody
explains."

3 slides: BMTC (the training island) -> LOCATOR (where it is) -> BUANGKOK
(what a kampong looked like).
"""

WIDTH, HEIGHT = 1080, 1920

_C = "https://upload.wikimedia.org/wikipedia/commons"

IMAGES = {
    "BMTC": f"{_C}/d/dd/Pulau_Tekong_BMTC.JPG",
    "LOCATOR": "/assets/images/osm-pulau-tekong-locator.png",
    "BUANGKOK": f"{_C}/4/48/An_old_house_in_Lorong_Buangkok_Singapore.JPG",
}

CREDITS = {
    "LOCATOR": "Locator map: map data © OpenStreetMap contributors",
}

SLIDES = [
    {"img": "BMTC", "type": "letterbox", "zoom": [1, 1.06, 1.12], "pan": [(0.5, 0.5), (0.5, 0.5), (0.5, 0.5)], "ease": "ease-in-out"},
    {"img": "LOCATOR", "type": "letterbox", "zoom": [1, 1.05, 1.10], "pan": [(0.5, 0.5), (0.5, 0.5), (0.5, 0.5)], "ease": "ease-in"},
    {"img": "BUANGKOK", "type": "cover", "zoom": [1, 1.05, 1.10], "pan": [(0.36, 0.5), (0.5, 0.5), (0.62, 0.5)], "ease": "ease-in-out"},
]

# Real sentence starts from the timing.json: s2 at 21.075, s4 at 34.625.
SCHEDULE = [(0.0, 0), (21.075, 1), (34.625, 2)]
TOTAL_DURATION = 42.925
TIMING_JSON = "audio/kampongs-under-pulau-tekong.timing.json"

# Shorts keep burned-in narration captions (muted autoplay); main videos do not -
# they rely on the uploaded .srt. Caption size/position come from the
# DEFAULT_CAPTION_* module constants (small outlined white text, no box).
BURN_CAPTIONS = True
