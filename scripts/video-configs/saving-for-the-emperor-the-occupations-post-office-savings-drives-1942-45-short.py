"""Short config for the Saving for the Emperor post.

The post's opening, sentences 0-6 (0-73.1s, over the 60s TikTok line): the
"Fourth time!" bonus advert of 16 July 1945, deposits taken in August as Japan
surrendered, the Postmaster-General's "absolutely safe", three years of
savings drives, and deposits never recognised afterwards. Every slide is
letterboxed: the newspaper pages are portrait-shaped and the note and the
street photo are too wide to crop to a vertical frame.
"""

WIDTH, HEIGHT = 1080, 1920

_U = "https://upload.wikimedia.org/wikipedia/commons"
_C = f"{_U}/thumb"

IMAGES = {
    "HERO": f"{_C}/2/2c/Collectie_Familie_Khouw%2C_KITLV_D14121.tiff/lossy-page1-1280px-Collectie_Familie_Khouw%2C_KITLV_D14121.tiff.jpg",
    "SS450716": "/assets/images/syonan-shimbun-1945-07-16-page-2.jpg",
    "NOTE10": f"{_C}/8/85/Banknote_%28AM_2004.35.4-1%29.jpg/1280px-Banknote_%28AM_2004.35.4-1%29.jpg",
    "STREET": f"{_U}/f/fc/Street_in_Shonan.JPG",
    "ST1947": "/assets/images/straits-times-1947-02-05-page-5.jpg",
    "FALLSTAMPS": f"{_U}/f/f0/1942_Fall_of_Singapore_for_Japanese_stamps.JPG",  # thumbnail only
    "POSB2": f"{_C}/2/25/POSB_Newton_Branch_Entrance.png/1280px-POSB_Newton_Branch_Entrance.png",  # thumbnail only
}

CREDITS = {
    "POSB2": "Deoma12, CC BY-SA 4.0, via Wikimedia Commons",
}

# The main video's thumbnail grid, re-panned for tall cells; the pair of
# stamps is too wide for a tall cell, so it is letterboxed.
THUMBNAIL = [
    {"img": "FALLSTAMPS", "type": "letterbox"},
    {"img": "SS450716", "zoom": 2.2, "pan": (0.95, 0.85)},
    {"img": "ST1947", "zoom": 2.4, "pan": (0.0, 0.07)},
    {"img": "POSB2", "pan": (0.1, 0.5)},
]

_E = "ease-in-out"
_LB = {"type": "letterbox", "zoom": [1.0, 1.03, 1.06], "pan": [(0.5, 0.5)] * 3, "ease": _E}
_LB_OUT = {"type": "letterbox", "zoom": [1.06, 1.03, 1.0], "pan": [(0.5, 0.5)] * 3, "ease": _E}

SLIDES = [
    {"img": "HERO", **_LB},          # s0  title
    {"img": "SS450716", **_LB},      # s1  the Malai Banking Association advert, 16 July 1945 (s2)
    {"img": "NOTE10", **_LB},        # s3  deposits taken in August, draw in October
    {"img": "SS450716", **_LB_OUT},  # s4  "absolutely safe" on the same page
    {"img": "STREET", **_LB},        # s5  three years of pressing people to save
    {"img": "ST1947", **_LB},        # s6  never recognised after it
]
SCHEDULE = [(0, 0), (8.3, 1), (29.5, 2), (40.475, 3), (49.2, 4), (66.875, 5)]
TOTAL_DURATION = 73.1
TIMING_JSON = "audio/saving-for-the-emperor-the-occupations-post-office-savings-drives-1942-45.timing.json"

BURN_CAPTIONS = True
CAPTION_FONT_RATIO = 0.032
CAPTION_MAX_WIDTH_FRAC = 0.86
CAPTION_Y_FRAC = 0.70

# The avatar presenter, cartoon with motion: corner bubble for the first and last 30 s.
AVATAR = {"ranges": [(0, 30), (-30, None)], "motion": True}
