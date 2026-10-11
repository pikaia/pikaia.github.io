"""Short config for the Singapore Stone post.

The post's opening, sentences 0-7 (0-74.35s, over the 60s TikTok line): the
1843 blast, the fifty unread lines, and the 1819 find by frightened sailors
at the river mouth. The surviving fragment is cropped to fill the vertical
frame; Bland's copy, Laidlay's drawing, the 1825 survey and Jackson's 1823
view are wide, so they are letterboxed.
"""

_U = "https://upload.wikimedia.org/wikipedia/commons"
_C = f"{_U}/thumb"

WIDTH, HEIGHT = 1080, 1920

IMAGES = {
    "HERO": f"{_C}/a/a1/1837-SingaporeStone-WBlanddrawing.jpg/1280px-1837-SingaporeStone-WBlanddrawing.jpg",
    "STONE09": f"{_C}/0/08/SingaporeStone-NationalMuseumofSingapore-20090712.jpg/1280px-SingaporeStone-NationalMuseumofSingapore-20090712.jpg",
    "LAIDDET": f"{_U}/e/e4/SingaporeStone-drawings-detail.jpg",
    "MAP25": f"{_C}/9/9f/Part_of_Singapore_Island_%28British_Library_India_Office_Records%2C_1825%2C_detail%29.jpg/1280px-Part_of_Singapore_Island_%28British_Library_India_Office_Records%2C_1825%2C_detail%29.jpg",
    "JACKSON": f"{_C}/8/8a/Singapore_from_the_Sea_June_1823_-_Lt._Phillip_Jackson.jpg/1280px-Singapore_from_the_Sea_June_1823_-_Lt._Phillip_Jackson.jpg",
}

_E = "ease-in-out"
_LB = {"type": "letterbox", "zoom": [1.0, 1.03, 1.06], "pan": [(0.5, 0.5)] * 3, "ease": _E}


def _v(zoom, pan):
    return {"type": "cover", "zoom": zoom, "pan": pan, "ease": _E}


SLIDES = [
    {"img": "HERO", **_LB},                                       # s0   title: Bland's 1837 copy
    {"img": "STONE09", **_v([1.0, 1.04, 1.08], [(0.5, 0.5)] * 3)}, # s1   January 1843: the blast
    {"img": "HERO", **_LB},                                       # s2   fifty lines on its face
    {"img": "LAIDDET", **_LB},                                    # s3   never read
    {"img": "MAP25", **_LB},                                      # s4   June 1819: clearing the point
    {"img": "JACKSON", **_LB},                                    # s5-7 the sailors; three metres high
]
SCHEDULE = [(0.0, 0), (5.575, 1), (20.125, 2), (28.75, 3), (38.125, 4), (50.75, 5)]
TOTAL_DURATION = 74.35
TIMING_JSON = "audio/the-singapore-stone-the-inscribed-rock-singapore-blew-up-in-1843.timing.json"

BURN_CAPTIONS = True
CAPTION_FONT_RATIO = 0.032
CAPTION_MAX_WIDTH_FRAC = 0.86
CAPTION_Y_FRAC = 0.70
