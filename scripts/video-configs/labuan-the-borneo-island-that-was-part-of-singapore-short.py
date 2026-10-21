"""Short config for the Labuan post.

The post's opening, sentences 0-5 (0-61.825s, over the 60s TikTok line): an
island off Borneo governed from Singapore for almost forty years, part of the
Settlement of Singapore from 1907 and a settlement of its own from 1912, a
federal territory and offshore centre today, and why Britain wanted it in the
1840s. Every slide is letterboxed: the 1848 engraving and the chart are too
wide to crop to a vertical frame, and the map and stamp are portrait-shaped.
"""

WIDTH, HEIGHT = 1080, 1920

_U = "https://upload.wikimedia.org/wikipedia/commons"
_C = f"{_U}/thumb"

IMAGES = {
    "HERO": f"{_C}/9/9e/H.C._steamer_Phlegethon_at_Labuan%2C_August_1848.jpg/1280px-H.C._steamer_Phlegethon_at_Labuan%2C_August_1848.jpg",
    "MAP1930": f"{_C}/c/c3/Labuan_1930_img0035_AccNo128_1.jpg/1280px-Labuan_1930_img0035_AccNo128_1.jpg",
    "STAMP": f"{_U}/0/07/1906straitssettlements2c.jpg",
    "FINPARK": f"{_C}/6/61/Labuan_Financial_Park_-_01.JPG/1280px-Labuan_Financial_Park_-_01.JPG",
    "CHART1848": f"{_C}/6/6c/Admiralty_Chart_No_1844_Labuan_Island%2C_Published_1848%2C_Large_Corrections_1902.jpg/1280px-Admiralty_Chart_No_1844_Labuan_Island%2C_Published_1848%2C_Large_Corrections_1902.jpg",
    "FLAG": f"{_U}/0/06/Ceremony_of_Hoisting_the_British_Flag_on_the_island_of_Labuan%2C_N._W._Coast_of_Borneo.jpg",
    "SURRENDER": f"{_U}/5/5f/Japanese_Surrender%2C_Labuan_%28AWM_115989%29.JPG",  # thumbnail only
}

CREDITS = {
    "CHART1848": "United Kingdom Hydrographic Office, public domain, via Wikimedia Commons",
}

# The main video's thumbnail grid, re-panned for tall cells.
THUMBNAIL = [
    {"img": "FLAG", "pan": (0.62, 0.5)},
    "STAMP",
    {"img": "SURRENDER", "pan": (0.5, 0.4)},
    {"img": "FINPARK", "pan": (0.35, 0.5)},
]

_E = "ease-in-out"
_LB = {"type": "letterbox", "zoom": [1.0, 1.03, 1.06], "pan": [(0.5, 0.5)] * 3, "ease": _E}

SLIDES = [
    {"img": "HERO", **_LB},       # s0  title
    {"img": "MAP1930", **_LB},    # s1  governed from Singapore (Singapore's own 1930 map)
    {"img": "STAMP", **_LB},      # s2  part of the Settlement of Singapore, then a settlement of its own
    {"img": "FINPARK", **_LB},    # s3  a federal territory and offshore centre today
    {"img": "CHART1848", **_LB},  # s4  coal and a sheltered harbour on the China route
    {"img": "FLAG", **_LB},       # s5  labuhan, an anchorage
]
SCHEDULE = [(0, 0), (4.075, 1), (16.3, 2), (31.7, 3), (41.75, 4), (55.925, 5)]
TOTAL_DURATION = 61.825
TIMING_JSON = "audio/labuan-the-borneo-island-that-was-part-of-singapore.timing.json"

BURN_CAPTIONS = True
CAPTION_FONT_RATIO = 0.032
CAPTION_MAX_WIDTH_FRAC = 0.86
CAPTION_Y_FRAC = 0.70

# The avatar presenter, cartoon with motion: corner bubble for the first and last 30 s.
AVATAR = {"ranges": [(0, 30), (-30, None)], "motion": True}
