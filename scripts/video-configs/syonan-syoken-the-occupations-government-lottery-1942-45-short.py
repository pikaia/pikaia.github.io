"""Short config for the Syonan Syoken post.

The post's opening, sentences 0-5 (0-60.55s, just over the 60s TikTok line):
the 1942 draw at the old Victoria Theatre, the $100,000 first prize, the
thirty-odd lotteries that followed, and the May 1942 announcement. The
tickets, the postcard and the two newspaper pages are letterboxed so nothing
is cropped; the large 1942 map of Syonan fills the vertical frame.
"""

_U = "https://upload.wikimedia.org/wikipedia/commons"
_C = f"{_U}/thumb"
_A = "/assets/images"

WIDTH, HEIGHT = 1080, 1920

IMAGES = {
    "HERO": f"{_C}/6/66/JapLotteryTicket-SIN-Occupation_SINMuseum_20171213_02.jpg/1280px-JapLotteryTicket-SIN-Occupation_SINMuseum_20171213_02.jpg",
    "VICT": f"{_U}/e/e6/Victoria_Theatre_and_Victoria_Memorial_Hall_-_c_1930.jpg",
    "SY0911": f"{_A}/syonan-shimbun-1942-09-11-page-1.jpg",
    "SY0913": f"{_A}/syonan-shimbun-1942-09-13-page-1.jpg",
    "T1": f"{_C}/9/9f/JapLotteryTicket-SIN-Occupation_SINMuseum_20171213_05.jpg/1280px-JapLotteryTicket-SIN-Occupation_SINMuseum_20171213_05.jpg",
    "MAP": f"{_C}/4/4a/SyonanSingapore.jpg/1280px-SyonanSingapore.jpg",
}

# Credits for images not captioned in the post or its gallery.
CREDITS = {}

_E = "ease-in-out"
_LB = {"type": "letterbox", "zoom": [1.0, 1.03, 1.06], "pan": [(0.5, 0.5)] * 3, "ease": _E}


def _v(zoom, pan):
    return {"type": "cover", "zoom": zoom, "pan": pan, "ease": _E}


SLIDES = [
    {"img": "HERO", **_LB},                                       # s0  title
    {"img": "VICT", **_LB},                                       # s1  the draw at the old Victoria Theatre
    {"img": "SY0911", **_LB},                                     # s2  women turn the drums; 62 winners
    {"img": "SY0913", **_LB},                                     # s3  the $100,000 first prize
    {"img": "T1", **_LB},                                         # s4  the first of more than thirty
    {"img": "MAP", **_v([1.0, 1.04, 1.08], [(0.5, 0.5)] * 3)},   # s5  announced 29 May 1942
]
SCHEDULE = [(0.0, 0), (7.2, 1), (20.35, 2), (30.575, 3), (40.6, 4), (54.95, 5)]
TOTAL_DURATION = 60.55
TIMING_JSON = "audio/syonan-syoken-the-occupations-government-lottery-1942-45.timing.json"

BURN_CAPTIONS = True
CAPTION_FONT_RATIO = 0.032
CAPTION_MAX_WIDTH_FRAC = 0.86
CAPTION_Y_FRAC = 0.70
