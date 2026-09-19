"""Short config for the John Crawfurd post - the hook (sentences 0-2):
Raffles's name is everywhere, but the man who actually secured the
island has a bridge named after him - misspelled. 3 slides, 34.2s.
"""

WIDTH, HEIGHT = 1080, 1920

_U = "https://upload.wikimedia.org/wikipedia/commons"

IMAGES = {
    "HERO": f"{_U}/8/84/View_of_the_town_and_roads_of_Singapore_from_the_government_hill_published_1828.jpg",
    "BRIDGE": f"{_U}/c/c9/Crawford_Bridge_-_2022-08-13.jpg",
}

_CVZ = {"type": "cover", "zoom": [1.0, 1.06, 1.12], "pan": [(0.5, 0.5)] * 3, "ease": "ease-in-out"}
_CVZO = {"type": "cover", "zoom": [1.12, 1.06, 1.0], "pan": [(0.5, 0.5)] * 3, "ease": "ease-out"}

SLIDES = [
    {"img": "HERO", **_CVZ},      # 0  s0   title
    {"img": "HERO", **_CVZO},     # 1  s1   Raffles's name stamped across Singapore
    {"img": "BRIDGE", **_CVZ},    # 2  s2   all three spell his name wrong
]

SCHEDULE = [
    (0.0, 0), (5.575, 1), (31.4, 2),
]
TOTAL_DURATION = 34.2
TIMING_JSON = "audio/john-crawfurd-the-diplomat-scholar-who-secured-singapores-ground.timing.json"

# Shorts keep burned-in narration captions (muted autoplay); main videos do not -
# they rely on the uploaded .srt.
BURN_CAPTIONS = True
CAPTION_FONT_RATIO = 0.032
CAPTION_MAX_WIDTH_FRAC = 0.86
CAPTION_Y_FRAC = 0.80
