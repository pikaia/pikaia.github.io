"""Short config for the Marquis post.

The post's opening, sentences 0-6 (0-62.325s, over the 60s TikTok line): the
Syonan Times of 5 September 1942 on the Marquis's appointment, the
nobleman who once hunted tigers, the two British botanists, and the
collections today. Every slide is letterboxed: the newspaper page and the
portrait are portrait-shaped and the photos too wide to crop to a vertical
frame.
"""

WIDTH, HEIGHT = 1080, 1920

IMAGES = {
    "HERO": "https://upload.wikimedia.org/wikipedia/commons/thumb/f/f5/KITLV_-_105738_-_Raffles_Museum_in_Singapore_-_circa_1900.tif/lossy-page1-1280px-KITLV_-_105738_-_Raffles_Museum_in_Singapore_-_circa_1900.tif.jpg",
    "SS420905": "/assets/images/syonan-shimbun-1942-09-05-page-4.jpg",
    "TOK1929": "https://upload.wikimedia.org/wikipedia/commons/1/1f/Tokugawa_Yoshichika_01.jpg",
    "GARD1910": "https://upload.wikimedia.org/wikipedia/commons/thumb/b/b3/KITLV_-_79909_-_Kleingrothe%2C_C.J._-_Medan_-_Botanical_Gardens%2C_Singapore_-_circa_1910.tif/lossy-page1-1280px-KITLV_-_79909_-_Kleingrothe%2C_C.J._-_Medan_-_Botanical_Gardens%2C_Singapore_-_circa_1910.tif.jpg",
    "LKC2026": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/d9/Lee_Kong_Chian_Natural_History_Museum_Jul2026_01.jpg/1280px-Lee_Kong_Chian_Natural_History_Museum_Jul2026_01.jpg",
}

# Credits for images not captioned in the post or its gallery.
CREDITS = {
    "GARD1910": "C. J. Kleingrothe, public domain, via Wikimedia Commons",
}

# The main video's thumbnail grid, re-panned for tall cells.
THUMBNAIL = [
    {"img": "HERO", "pan": (0.45, 0.5)},
    {"img": "TOK1929", "pan": (0.5, 0.4)},
    {"img": "SS420905", "zoom": 2.8, "pan": (0.63, 0.70)},
    {"img": "LKC2026", "pan": (0.5, 0.5)},
]

_E = "ease-in-out"
_LB = {"type": "letterbox", "zoom": [1.0, 1.03, 1.06], "pan": [(0.5, 0.5)] * 3, "ease": _E}

SLIDES = [
    {"img": "HERO", **_LB},           # s0
    {"img": "SS420905", **_LB},       # s1
    {"img": "TOK1929", **_LB},        # s4
    {"img": "GARD1910", **_LB},       # s5
    {"img": "LKC2026", **_LB},        # s6
]
SCHEDULE = [(0.0, 0), (7.975, 1), (36.85, 2), (47.475, 3), (55.175, 4)]
TOTAL_DURATION = 62.325
TIMING_JSON = "audio/the-marquis-and-the-museum-tokugawa-yoshichika-in-syonan.timing.json"

BURN_CAPTIONS = True
CAPTION_FONT_RATIO = 0.032
CAPTION_MAX_WIDTH_FRAC = 0.86
CAPTION_Y_FRAC = 0.70

# The avatar presenter, cartoon with motion: corner bubble for the first and last 30 s.
AVATAR = {"ranges": [(0, 30), (-30, None)], "motion": True}
