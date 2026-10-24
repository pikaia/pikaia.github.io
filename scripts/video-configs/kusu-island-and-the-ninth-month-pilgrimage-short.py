"""Short config for the Kusu Island post.

The post's opening, sentences 0-7 (0-72.875s, over the 60s line): the
record crossing of 17 October 1948, the shrine on the hill, this year's
season, the Straits Times front page and the pilgrims' offerings. Every
slide is letterboxed.
"""

WIDTH, HEIGHT = 1080, 1920

IMAGES = {
    "AERIAL": "https://upload.wikimedia.org/wikipedia/commons/thumb/1/19/Aerial_perspective_of_Kusu_Island%2C_Singapore._Shot_in_2016.jpg/1280px-Aerial_perspective_of_Kusu_Island%2C_Singapore._Shot_in_2016.jpg",
    "BOAT11": "https://upload.wikimedia.org/wikipedia/commons/thumb/4/4c/Kusu_Island%2C_Singapore_-_20110227-03.jpg/1280px-Kusu_Island%2C_Singapore_-_20110227-03.jpg",
    "KERAMAT": "https://upload.wikimedia.org/wikipedia/commons/thumb/3/38/Keramat_Kusu%2C_Kusu_Island_%2870917%29.jpg/1280px-Keramat_Kusu%2C_Kusu_Island_%2870917%29.jpg",
    "FERRY": "https://upload.wikimedia.org/wikipedia/commons/thumb/b/bc/SP1471A_Singapore_Island_Cruise_Marina_South_Pier_to_Saint_John%27s_Island_and_Kusu_Island_17-05-2024%287%29.jpg/1280px-SP1471A_Singapore_Island_Cruise_Marina_South_Pier_to_Saint_John%27s_Island_and_Kusu_Island_17-05-2024%287%29.jpg",
    "ST48A": "/assets/images/straits-times-1948-10-18-page-1.jpg",
    "TEMPLE06": "https://upload.wikimedia.org/wikipedia/commons/8/85/KusuIsland01.JPG",
    "TEMPLE23": "https://upload.wikimedia.org/wikipedia/commons/thumb/5/58/Kusu_Island_Tua_Pek_Kong_Temple_Photo.jpg/1280px-Kusu_Island_Tua_Pek_Kong_Temple_Photo.jpg",  # thumbnail only
}

# Every image is captioned in the post or its gallery.
CREDITS = {}

# The main video's thumbnail grid, re-panned for tall cells.
THUMBNAIL = [
    {"img": "ST48A", "pan": (0.5, 0.3)},
    {"img": "TEMPLE06", "pan": (0.5, 0.5)},
    {"img": "AERIAL", "pan": (0.5, 0.5)},
    {"img": "TEMPLE23", "pan": (0.5, 0.5)},
]

_E = "ease-in-out"
_LB = {"type": "letterbox", "zoom": [1.0, 1.03, 1.06], "pan": [(0.5, 0.5)] * 3, "ease": _E}

SLIDES = [
    {"img": "AERIAL", **_LB},     # s0
    {"img": "BOAT11", **_LB},     # s1
    {"img": "KERAMAT", **_LB},    # s3
    {"img": "FERRY", **_LB},      # s4
    {"img": "ST48A", **_LB},      # s5
    {"img": "TEMPLE06", **_LB},   # s7
]
SCHEDULE = [(0.0, 0), (3.575, 1), (25.775, 2), (33.925, 3), (42.15, 4), (58.025, 5)]
TOTAL_DURATION = 72.875
TIMING_JSON = "audio/kusu-island-and-the-ninth-month-pilgrimage.timing.json"

BURN_CAPTIONS = True
CAPTION_FONT_RATIO = 0.032
CAPTION_MAX_WIDTH_FRAC = 0.86
CAPTION_Y_FRAC = 0.70

# The avatar presenter, cartoon with motion: corner bubble for the first and last 30 s.
AVATAR = {"ranges": [(0, 30), (-30, None)], "motion": True}
