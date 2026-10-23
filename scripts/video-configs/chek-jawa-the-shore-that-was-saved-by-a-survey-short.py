"""Short config for the Chek Jawa post.

The post's opening, sentences 0-6 (0-64.475s, over the 60s TikTok line):
Joseph Lai's visit in December 2000, the flats at low tide, the plan to
reclaim them, the crowds and the deferral, and Pulau Ubin on the map.
Every slide is letterboxed: the photos and the map are too wide to crop
to a vertical frame.
"""

WIDTH, HEIGHT = 1080, 1920

IMAGES = {
    "HERO": "https://upload.wikimedia.org/wikipedia/commons/thumb/3/36/Chek_Jawa_35%2C_Aug_07.JPG/1280px-Chek_Jawa_35%2C_Aug_07.JPG",
    "ROCKS09": "https://upload.wikimedia.org/wikipedia/commons/a/a8/Chek_Jawa%2C_Singapore_%283940295137%29.jpg",
    "CJ25": "https://upload.wikimedia.org/wikipedia/commons/thumb/5/5e/Chek_Jawa_25%2C_Aug_07.JPG/1280px-Chek_Jawa_25%2C_Aug_07.JPG",
    "CJ40": "https://upload.wikimedia.org/wikipedia/commons/thumb/3/35/Singapore_Pulau_Ubin_Chek_Jawa_40.jpg/1280px-Singapore_Pulau_Ubin_Chek_Jawa_40.jpg",
    "JETTY07": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/dd/Chek_Jawa_30%2C_Aug_07.JPG/1280px-Chek_Jawa_30%2C_Aug_07.JPG",
    "COASTBW": "https://upload.wikimedia.org/wikipedia/commons/thumb/f/f7/Chek_Jawa_15%2C_Aug_07.JPG/1280px-Chek_Jawa_15%2C_Aug_07.JPG",
    "MAP": "/assets/images/chek-jawa-map.png",
    "HOUSE07": "https://upload.wikimedia.org/wikipedia/commons/thumb/c/c0/Chek_Jawa%2C_Aug_07.JPG/1280px-Chek_Jawa%2C_Aug_07.JPG",  # thumbnail only
    "MUD": "https://upload.wikimedia.org/wikipedia/commons/thumb/f/f6/Chek_Jawa_12%2C_Aug_07.JPG/1280px-Chek_Jawa_12%2C_Aug_07.JPG",  # thumbnail only
    "BOULD15": "https://upload.wikimedia.org/wikipedia/commons/thumb/0/0f/Singapore_Pulau_Ubin_Chek_Jawa_20.jpg/1280px-Singapore_Pulau_Ubin_Chek_Jawa_20.jpg",  # thumbnail only
}

# Credits for images not captioned in the post or its gallery.
CREDITS = {
    "CJ25": "Sengkang, CC BY-SA 3.0, via Wikimedia Commons",
    "CJ40": "Zairon, CC BY-SA 4.0, via Wikimedia Commons",
}

# The main video's thumbnail grid, re-panned for tall cells.
THUMBNAIL = [
    {"img": "HOUSE07", "pan": (0.45, 0.45)},
    {"img": "MUD", "pan": (0.85, 0.5)},
    {"img": "HERO", "pan": (0.55, 0.5)},
    {"img": "BOULD15", "pan": (0.32, 0.5)},
]

_E = "ease-in-out"
_LB = {"type": "letterbox", "zoom": [1.0, 1.03, 1.06], "pan": [(0.5, 0.5)] * 3, "ease": _E}

SLIDES = [
    {"img": "HERO", **_LB},           # s0
    {"img": "ROCKS09", **_LB},        # s1
    {"img": "CJ25", **_LB},           # s2
    {"img": "CJ40", **_LB},           # s3
    {"img": "JETTY07", **_LB},        # s4
    {"img": "COASTBW", **_LB},        # s5
    {"img": "MAP", **_LB},            # s6
]
SCHEDULE = [(0.0, 0), (3.65, 1), (15.525, 2), (22.55, 3), (27.075, 4), (44.75, 5), (53.75, 6)]
TOTAL_DURATION = 64.475
TIMING_JSON = "audio/chek-jawa-the-shore-that-was-saved-by-a-survey.timing.json"

BURN_CAPTIONS = True
CAPTION_FONT_RATIO = 0.032
CAPTION_MAX_WIDTH_FRAC = 0.86
CAPTION_Y_FRAC = 0.70

# The avatar presenter, cartoon with motion: corner bubble for the first and last 30 s.
AVATAR = {"ranges": [(0, 30), (-30, None)], "motion": True}
