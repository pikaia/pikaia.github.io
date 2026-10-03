"""Short config for the Progressive Party post.

The post's opening, sentences 0-4 (0-45.15s): the 1955 defeat, the two
earlier wins, C. C. Tan losing Cairnhill to David Marshall, and the party
dissolving ten months later. Newspaper pages pan to their headlines in the
vertical frame (pan_y 0 keeps the headline in view).
"""

_U = "https://upload.wikimedia.org/wikipedia/commons"
_A = "/assets/images"

WIDTH, HEIGHT = 1080, 1920

IMAGES = {
    "HALL": f"{_U}/thumb/b/b6/172a_Victoria_Hall_Singapore_%2851253058494%29.jpg/1280px-172a_Victoria_Hall_Singapore_%2851253058494%29.jpg",
    "CCTAN": f"{_U}/b/b6/Tan_Chye_Cheng.png",
    "S510411": f"{_A}/straits-times-1951-04-11-page-1.jpg",
    "S550404": f"{_A}/straits-times-1955-04-04-page-1.jpg",
    "S560206": f"{_A}/straits-times-1956-02-06-page-1.jpg",
}

_E = "ease-in-out"
SLIDES = [
    {"img": "HALL", "type": "cover", "zoom": [1.0, 1.06, 1.12], "pan": [(0.45, 0.5)] * 3, "ease": _E},       # s0  title
    {"img": "S550404", "type": "cover", "zoom": [1.06, 1.12, 1.17], "pan": [(0.0, 0.0)] * 3, "ease": _E},    # s1  1955
    {"img": "S510411", "type": "cover", "zoom": [1.0, 1.04, 1.08], "pan": [(0.5, 0.0)] * 3, "ease": _E},     # s2  1948, 1951
    {"img": "CCTAN", "type": "cover", "zoom": [1.0, 1.04, 1.08], "pan": [(0.5, 0.33)] * 3, "ease": _E},      # s3  C. C. Tan
    {"img": "S560206", "type": "cover", "zoom": [2.16, 2.28, 2.4],                                          # s4  dissolved
     "pan": [(0.807, 0.0), (0.794, 0.0), (0.783, 0.0)], "ease": _E},
]
SCHEDULE = [(0.0, 0), (6.5, 1), (15.3, 2), (25.75, 3), (34.6, 4)]
TOTAL_DURATION = 45.15
TIMING_JSON = "audio/the-progressive-party-the-colonial-era-party-that-won-singapores-first-elections-then-vanished.timing.json"

BURN_CAPTIONS = True
CAPTION_FONT_RATIO = 0.032
CAPTION_MAX_WIDTH_FRAC = 0.86
CAPTION_Y_FRAC = 0.70

# Made before the over-one-minute rule (2026-10-03); see validate_short_config().
SHORT_UNDER_A_MINUTE_OK = True
