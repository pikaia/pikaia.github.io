"""Short config for the cemeteries post.

The post's opening, sentences 0-6 (0-73.95s, over the 60s line): 21
cemeteries and 120,000 graves cleared by 1985, Bidadari emptied, the 15-year
grave, the move to cremation and gardens, and the first Christian cemeteries
at Fort Canning and on Bukit Timah Road. Every slide is letterboxed.
"""

WIDTH, HEIGHT = 1080, 1920

IMAGES = {
    "HERO": "https://upload.wikimedia.org/wikipedia/commons/thumb/0/09/Bukit_Brown_Cemetery%2C_Singapore_-_20110326-01.jpg/1280px-Bukit_Brown_Cemetery%2C_Singapore_-_20110326-01.jpg",
    "BID13": "https://upload.wikimedia.org/wikipedia/commons/thumb/e/e8/Bidadari_cemetery.jpg/1280px-Bidadari_cemetery.jpg",
    "BID5": "https://upload.wikimedia.org/wikipedia/commons/thumb/b/b5/Bidadari_cemetery_5.jpg/1280px-Bidadari_cemetery_5.jpg",
    "MANDAI": "https://upload.wikimedia.org/wikipedia/commons/thumb/f/fd/Mandai_Crematorium_and_Columbarium_Complex_Overview%2C_2015.jpg/1280px-Mandai_Crematorium_and_Columbarium_Complex_Overview%2C_2015.jpg",
    "FCG11": "https://upload.wikimedia.org/wikipedia/commons/thumb/3/31/Gravestones_in_Fort_Canning_Green%2C_Singapore_-_20110116.jpg/1280px-Gravestones_in_Fort_Canning_Green%2C_Singapore_-_20110116.jpg",
    "FCG1": "https://upload.wikimedia.org/wikipedia/commons/thumb/a/a1/Gravestones_in_Fort_Canning_Green%2C_Singapore%2C_relocated_from_Bukit_Timah_Cemetery_-_20130401-01.jpg/1280px-Gravestones_in_Fort_Canning_Green%2C_Singapore%2C_relocated_from_Bukit_Timah_Cemetery_-_20130401-01.jpg",
    "CUPP": "https://upload.wikimedia.org/wikipedia/commons/thumb/5/57/Gravestone_of_William_Cuppage%2C_Fort_Canning_Green%2C_Singapore_-_20130401-01.jpg/1280px-Gravestone_of_William_Cuppage%2C_Fort_Canning_Green%2C_Singapore_-_20130401-01.jpg",
    "BIDPC": "https://upload.wikimedia.org/wikipedia/commons/6/6c/Gates_of_Bidadari_Cemetery.jpg",  # thumbnail only
    "FUN53": "https://upload.wikimedia.org/wikipedia/commons/2/2d/Funeral_of_Ng_Thian_Eng_at_Bukit_Brown.jpg",  # thumbnail only
}

# Credits for images not captioned in the post or its gallery.
CREDITS = {
    "FCG11": "David Lee, CC BY-SA 2.0, via Wikimedia Commons",
}

# The main video's thumbnail grid, re-panned for tall cells.
THUMBNAIL = [
    {"img": "BIDPC", "pan": (0.5, 0.5)},
    {"img": "FUN53", "pan": (0.5, 0.5)},
    {"img": "BID13", "pan": (0.5, 0.5)},
    {"img": "MANDAI", "pan": (0.5, 0.5)},
]

_E = "ease-in-out"
_LB = {"type": "letterbox", "zoom": [1.0, 1.03, 1.06], "pan": [(0.5, 0.5)] * 3, "ease": _E}

SLIDES = [
    {"img": "HERO", **_LB},       # s0
    {"img": "BID13", **_LB},      # s1
    {"img": "BID5", **_LB},       # s2
    {"img": "MANDAI", **_LB},     # s3
    {"img": "FCG11", **_LB},      # s4
    {"img": "FCG1", **_LB},       # s5
    {"img": "CUPP", **_LB},       # s6
]
SCHEDULE = [(0.0, 0), (4.6, 1), (16.375, 2), (28.9, 3), (42.025, 4), (52.775, 5), (64.025, 6)]
TOTAL_DURATION = 73.95
TIMING_JSON = "audio/from-graves-to-gardens-how-singapore-makes-room-for-its-dead.timing.json"

BURN_CAPTIONS = True
CAPTION_FONT_RATIO = 0.032
CAPTION_MAX_WIDTH_FRAC = 0.86
CAPTION_Y_FRAC = 0.70

# The avatar presenter, cartoon with motion: corner bubble for the first and last 30 s.
AVATAR = {"ranges": [(0, 30), (-30, None)], "motion": True}
