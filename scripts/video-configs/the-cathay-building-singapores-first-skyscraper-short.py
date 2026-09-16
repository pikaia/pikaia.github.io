"""Short config for the Cathay Building post - the hidden-landmark hook
(sentences 0-2): the facade fronting a modern mall, and the fact that
almost nobody walking past it knows it's a national monument even
though the building it belonged to was torn down. 3 slides, 33.525s.
"""

WIDTH, HEIGHT = 1080, 1920

_U = "https://upload.wikimedia.org/wikipedia/commons"

IMAGES = {
    "HERO": f"{_U}/5/57/The_Cathay_Building_in_Singapore_1945.jpg",
    "MODERN": f"{_U}/c/cf/The_Cathay%2C_October_2025.jpg",
}

_CVZ = {"type": "cover", "zoom": [1.0, 1.06, 1.12], "pan": [(0.5, 0.5)] * 3, "ease": "ease-in-out"}
_CVZO = {"type": "cover", "zoom": [1.12, 1.06, 1.0], "pan": [(0.5, 0.5)] * 3, "ease": "ease-out"}
_LTB = {"type": "letterbox", "zoom": [1.0, 1.04, 1.08], "pan": [(0.5, 0.5)] * 3, "ease": "ease-in-out"}

SLIDES = [
    {"img": "HERO", **_LTB},     # 0  s0   title
    {"img": "MODERN", **_CVZ},   # 1  s1   corner of Handy Road and Dhoby Ghaut
    {"img": "MODERN", **_CVZO},  # 2  s2   most people walking under it
]

SCHEDULE = [
    (0.0, 0), (3.975, 1), (15.4, 2),
]
TOTAL_DURATION = 33.525
TIMING_JSON = "audio/the-cathay-building-singapores-first-skyscraper.timing.json"

# Shorts keep burned-in narration captions (muted autoplay); main videos do not -
# they rely on the uploaded .srt.
BURN_CAPTIONS = True
CAPTION_FONT_RATIO = 0.032
CAPTION_MAX_WIDTH_FRAC = 0.86
CAPTION_Y_FRAC = 0.80
