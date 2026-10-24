"""Short config for the Changi Murals post.

The post's opening, sentences 0-7 (0-76.925s, over the 60s line): Warren
painting a chapel in a prisoners' hospital in 1942, the murals hidden and
still there today inside an air force camp, the prisoners marched to Changi,
the hospital at Roberts Barracks and Warren's arrival. Sentences naming Warren
show pictures with no people. Every slide is letterboxed.
"""

WIDTH, HEIGHT = 1080, 1920

IMAGES = {
    "MUS06": "https://upload.wikimedia.org/wikipedia/commons/6/69/Changi_Museum.jpg",
    "DUNTROON": "https://upload.wikimedia.org/wikipedia/commons/thumb/2/2d/Changi_Chapel_March_2013_2.jpg/1280px-Changi_Chapel_March_2013_2.jpg",
    "MUS23": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/d9/Changi_chapel_museum.jpg/1280px-Changi_chapel_museum.jpg",
    "ENTR": "https://upload.wikimedia.org/wikipedia/commons/thumb/c/cf/Changi_Air_Base_West_entrance.JPG/1280px-Changi_Air_Base_West_entrance.JPG",
    "AWM": "https://upload.wikimedia.org/wikipedia/commons/e/e3/Australian_War_Memorial_132935.JPG",
    "COLE": "https://upload.wikimedia.org/wikipedia/commons/thumb/a/a9/Orderly_on_His_Rounds_in_X_Ward%2C_Changi_Gaol%2C_Singapore%2C_With_Pow%27s_Suffering_from_Starvation_and_Beri-beri_Art.IWMARTLD5618.jpg/1280px-Orderly_on_His_Rounds_in_X_Ward%2C_Changi_Gaol%2C_Singapore%2C_With_Pow%27s_Suffering_from_Starvation_and_Beri-beri_Art.IWMARTLD5618.jpg",
    "MAP": "/assets/images/changi-murals-map.png",
    "RAF58": "https://upload.wikimedia.org/wikipedia/commons/0/06/Changi_Air_Base_1958.jpg",  # thumbnail only
    "REPLICA": "https://upload.wikimedia.org/wikipedia/commons/thumb/1/15/POW_chapel_at_Changi_Prison.jpg/1280px-POW_chapel_at_Changi_Prison.jpg",  # thumbnail only
}

# Every image is captioned in the post or its gallery.
CREDITS = {}

# The main video's thumbnail grid, re-panned for tall cells.
THUMBNAIL = [
    {"img": "AWM", "pan": (0.5, 0.5)},
    {"img": "COLE", "pan": (0.5, 0.5)},
    {"img": "RAF58", "pan": (0.5, 0.45)},
    {"img": "REPLICA", "pan": (0.5, 0.5)},
]

_E = "ease-in-out"
_LB = {"type": "letterbox", "zoom": [1.0, 1.03, 1.06], "pan": [(0.5, 0.5)] * 3, "ease": _E}

SLIDES = [
    {"img": "MUS06", **_LB},      # s0
    {"img": "DUNTROON", **_LB},   # s1
    {"img": "MUS23", **_LB},      # s3
    {"img": "ENTR", **_LB},       # s4
    {"img": "AWM", **_LB},        # s5
    {"img": "COLE", **_LB},       # s6
    {"img": "MAP", **_LB},        # s7
]
SCHEDULE = [(0.0, 0), (5.25, 1), (29.6, 2), (38.15, 3), (44.7, 4), (58.025, 5), (66.375, 6)]
TOTAL_DURATION = 76.925
TIMING_JSON = "audio/the-changi-murals-stanley-warrens-chapel-paintings-at-roberts-barracks.timing.json"

BURN_CAPTIONS = True
CAPTION_FONT_RATIO = 0.032
CAPTION_MAX_WIDTH_FRAC = 0.86
CAPTION_Y_FRAC = 0.70

# The avatar presenter, cartoon with motion: corner bubble for the first and last 30 s.
AVATAR = {"ranges": [(0, 30), (-30, None)], "motion": True}
