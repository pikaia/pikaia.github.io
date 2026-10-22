"""Short config for the Southern Special Students post.

The post's opening, sentences 0-5 (0-62.5s, over the 60s TikTok line): the
Syonan Shimbun of 4 June 1943 on the 33 trainees at Woodsville, the fifteen
best bound for Japan, the two from Syonan (Bostam and Kasmani), the 200 or
so Southern Special Students, and Hiroshima. Every slide is letterboxed: the
newspaper pages are portrait-shaped and the photos too wide to crop to a
vertical frame.
"""

WIDTH, HEIGHT = 1080, 1920

_U = "https://upload.wikimedia.org/wikipedia/commons"
_C = f"{_U}/thumb"

IMAGES = {
    "HERO": f"{_C}/c/cc/Ruins_of_Hiroshima_University_of_Literature_and_Science.jpg/1280px-Ruins_of_Hiroshima_University_of_Literature_and_Science.jpg",
    "SS430604": "/assets/images/syonan-shimbun-1943-06-04-page-1.jpg",
    "WOODS": f"{_C}/7/72/Upp_Serangoon_Rd_bef_Woodsville_Flyover_20060409.jpg/1280px-Upp_Serangoon_Rd_bef_Woodsville_Flyover_20060409.jpg",
    "SS430807": "/assets/images/syonan-shimbun-1943-08-07-page-2.jpg",
    "CLOUDK": f"{_U}/6/65/Atomic_cloud_over_Hiroshima_from_the_Kure_Naval_Arsenal.jpg",
    "CENOTAPH": f"{_C}/d/d8/Hiroshima_Peace_Memorial_Park_cenotaph.jpg/1280px-Hiroshima_Peace_Memorial_Park_cenotaph.jpg",  # thumbnail only
}

# The main video's thumbnail grid, re-panned for tall cells.
THUMBNAIL = [
    {"img": "SS430604", "zoom": 2.6, "pan": (0.45, 0.75)},
    {"img": "CLOUDK", "pan": (0.5, 0.4)},
    {"img": "HERO", "pan": (0.45, 0.5)},
    {"img": "CENOTAPH", "pan": (0.5, 0.5)},
]

_E = "ease-in-out"
_LB = {"type": "letterbox", "zoom": [1.0, 1.03, 1.06], "pan": [(0.5, 0.5)] * 3, "ease": _E}
_LB_OUT = {"type": "letterbox", "zoom": [1.06, 1.03, 1.0], "pan": [(0.5, 0.5)] * 3, "ease": _E}

SLIDES = [
    {"img": "HERO", **_LB},          # s0  title
    {"img": "SS430604", **_LB},      # s1  33 trainees at Woodsville
    {"img": "WOODS", **_LB},         # s2  the fifteen best to Japan
    {"img": "SS430604", **_LB_OUT},  # s3  Bostam and Kasmani
    {"img": "SS430807", **_LB},      # s4  about 200 Southern Special Students
    {"img": "CLOUDK", **_LB},        # s5  Hiroshima
]
SCHEDULE = [(0, 0), (7.65, 1), (25.325, 2), (31.4, 3), (38.35, 4), (50.55, 5)]
TOTAL_DURATION = 62.5
TIMING_JSON = "audio/the-southern-special-students-malayan-youths-sent-to-japan-1943-45.timing.json"

BURN_CAPTIONS = True
CAPTION_FONT_RATIO = 0.032
CAPTION_MAX_WIDTH_FRAC = 0.86
CAPTION_Y_FRAC = 0.70

# The avatar presenter, cartoon with motion: corner bubble for the first and last 30 s.
AVATAR = {"ranges": [(0, 30), (-30, None)], "motion": True}
