"""Short config for the Tani Yutaka post.

The post's opening, sentences 0-6 (0-64.65s, over the 60s TikTok line): his
death in Singapore in March 1942, the Kuala Terengganu boyhood, the wartime
legend, the records from his own time and his birth in 1911. His photograph
(the seated copy and the tighter crop) and the two whole newspaper pages are
letterboxed so nothing is cropped; the cemetery and Kuala Terengganu street
photos fill the vertical frame.
"""

_U = "https://upload.wikimedia.org/wikipedia/commons"
_C = f"{_U}/thumb"
_A = "/assets/images"

WIDTH, HEIGHT = 1080, 1920

IMAGES = {
    "HERO": f"{_U}/e/e0/Tani_Yutaka_seated%2C_in_Malay_dress.webp",
    "CEM1": f"{_C}/1/12/Japanese_Cemetery_Park_1.jpg/1280px-Japanese_Cemetery_Park_1.jpg",
    "KT3": f"{_C}/c/c3/KT_Chinatown_3.jpg/1280px-KT_Chinatown_3.jpg",
    "HEROC": f"{_U}/a/a8/Yutaka_Tani.png",
    "SY1943": f"{_A}/syonan-shimbun-1943-07-17-page-2.jpg",
    "TRIBUNE": f"{_A}/malaya-tribune-1933-11-09-page-7.jpg",
    "KT1": f"{_C}/4/4c/KT_Chinatown_1.jpg/1280px-KT_Chinatown_1.jpg",
}

# Credits for images not captioned in the post or its gallery.
CREDITS = {
    "HEROC": "Unknown photographer, public domain, via Wikimedia Commons",
}

_E = "ease-in-out"
_LB = {"type": "letterbox", "zoom": [1.0, 1.03, 1.06], "pan": [(0.5, 0.5)] * 3, "ease": _E}


def _v(zoom, pan):
    return {"type": "cover", "zoom": zoom, "pan": pan, "ease": _E}


SLIDES = [
    {"img": "HERO", **_LB},                                       # s0  title
    {"img": "CEM1", **_v([1.0, 1.04, 1.08], [(0.5, 0.5)] * 3)},  # s1  died in a Singapore hospital, 1942
    {"img": "KT3", **_v([1.0, 1.04, 1.08], [(0.5, 0.5)] * 3)},   # s2  grew up in Kuala Terengganu
    {"img": "HEROC", **_LB},                                      # s3  his name was Tani Yutaka
    {"img": "SY1943", **_LB},                                     # s4  the wartime film
    {"img": "TRIBUNE", **_LB},                                    # s5  the records from his own time
    {"img": "KT1", **_v([1.0, 1.04, 1.08], [(0.5, 0.5)] * 3)},   # s6  born 1911, a barber's son
]
SCHEDULE = [(0.0, 0), (5.375, 1), (16.6, 2), (30.05, 3), (33.175, 4), (42.075, 5), (52.525, 6)]
TOTAL_DURATION = 64.65
TIMING_JSON = "audio/tani-yutaka-the-tiger-of-malaya-the-man-and-the-wartime-legend.timing.json"

BURN_CAPTIONS = True
CAPTION_FONT_RATIO = 0.032
CAPTION_MAX_WIDTH_FRAC = 0.86
CAPTION_Y_FRAC = 0.70
