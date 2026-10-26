"""Short config for the Alkaff Mansion post.

The post's opening, sentences 0-6 (0-66.225s, over the 60s line): the
mansion on Telok Blangah Hill, built around 1918, the Hadhramaut, Tarim and
the family's arrival in 1852. Syed Shaik's sentence shows Tarim's palaces,
with no people. Every slide is letterboxed.
"""

WIDTH, HEIGHT = 1080, 1920

IMAGES = {
    "HERO": "https://upload.wikimedia.org/wikipedia/commons/6/6c/AlkaffMansion.jpg",
    "MANSION19": "https://upload.wikimedia.org/wikipedia/commons/thumb/a/a3/Alkaff_Mansion.png/1280px-Alkaff_Mansion.png",
    "HADMAP": "https://upload.wikimedia.org/wikipedia/commons/thumb/7/74/Map_of_Hadhrami_emigrations.svg/1280px-Map_of_Hadhrami_emigrations.svg.png",
    "TARIM29": "https://upload.wikimedia.org/wikipedia/commons/d/d4/Tarim_RAF_1929.jpg",
    "TARIM94": "https://upload.wikimedia.org/wikipedia/commons/thumb/8/8a/Yemen_Tarim_Hadhramaut_1994_-_167531378_63715937ff_o.jpg/1280px-Yemen_Tarim_Hadhramaut_1994_-_167531378_63715937ff_o.jpg",
    "ARCADE": "https://upload.wikimedia.org/wikipedia/commons/thumb/4/4b/Collyer_Quay%2C_Singapore_postcard.jpg/1280px-Collyer_Quay%2C_Singapore_postcard.jpg",  # thumbnail only
    "GARDEN": "https://upload.wikimedia.org/wikipedia/commons/thumb/e/ea/Alkaff_Garden%2C_Singapore.%2C_KITLV_1404907.tiff/lossy-page1-1280px-Alkaff_Garden%2C_Singapore.%2C_KITLV_1404907.tiff.jpg",  # thumbnail only
}

# Every image is captioned in the post or its gallery.
CREDITS = {}

# The main video's thumbnail grid, re-panned for tall cells.
THUMBNAIL = [
    {"img": "TARIM29", "pan": (0.5, 0.5)},
    {"img": "ARCADE", "pan": (0.18, 0.4)},
    {"img": "GARDEN", "pan": (0.5, 0.5)},
    {"img": "MANSION19", "pan": (0.5, 0.4)},
]

_E = "ease-in-out"
_LB = {"type": "letterbox", "zoom": [1.0, 1.03, 1.06], "pan": [(0.5, 0.5)] * 3, "ease": _E}

SLIDES = [
    {"img": "HERO", **_LB},       # s0
    {"img": "MANSION19", **_LB},  # s1
    {"img": "HADMAP", **_LB},     # s3
    {"img": "TARIM29", **_LB},    # s4
    {"img": "TARIM94", **_LB},    # s6
]
SCHEDULE = [(0.0, 0), (5.925, 1), (25.9, 2), (36.425, 3), (54.375, 4)]
TOTAL_DURATION = 66.225
TIMING_JSON = "audio/alkaff-mansion-and-the-alkaffs-a-hadhrami-family-on-telok-blangah-hill.timing.json"

BURN_CAPTIONS = True
CAPTION_FONT_RATIO = 0.032
CAPTION_MAX_WIDTH_FRAC = 0.86
CAPTION_Y_FRAC = 0.70

# The avatar presenter, cartoon with motion: corner bubble for the first and last 30 s.
AVATAR = {"ranges": [(0, 30), (-30, None)], "motion": True}
