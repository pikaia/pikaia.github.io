"""Short config for the Munshi Abdullah post.

The post's opening, sentences 0-7 (0-65.975s, over the 60s TikTok line): the
evening in March 1823 when Abdullah met Farquhar on the road, the attack, the
Hikayat, and the debt behind it. The tall kris fills the vertical frame; the
1823 sketch, Farquhar's portrait, the 1849 page and the Bugis prau are small
or wide, so they are letterboxed.
"""

_U = "https://upload.wikimedia.org/wikipedia/commons"
_C = f"{_U}/thumb"

WIDTH, HEIGHT = 1080, 1920

IMAGES = {
    "HERO": f"{_C}/8/8a/Singapore_from_the_Sea_June_1823_-_Lt._Phillip_Jackson.jpg/1280px-Singapore_from_the_Sea_June_1823_-_Lt._Phillip_Jackson.jpg",
    "FARQ": f"{_U}/f/f9/Portrait_of_William_Farquhar_%28c._1830%29.jpg",
    "KRIS": f"{_C}/0/08/Kris_with_Sheath_MET_DT11927.jpg/1280px-Kris_with_Sheath_MET_DT11927.jpg",
    "HIK1849": f"{_U}/a/af/AbdullahbinAbdulKadir-HikayatAbdullah-1849.jpg",
    "BUGIS": f"{_U}/3/3b/Bugis-Makassan_prauw_William_Westall_1803.jpg",
}

# Credits for images not captioned in the post or its gallery.
CREDITS = {
    "KRIS": "Kris with sheath, 18th to 19th century, The Metropolitan Museum of Art, CC0, via Wikimedia Commons",
}

_E = "ease-in-out"
_LB = {"type": "letterbox", "zoom": [1.0, 1.03, 1.06], "pan": [(0.5, 0.5)] * 3, "ease": _E}


def _v(zoom, pan):
    return {"type": "cover", "zoom": zoom, "pan": pan, "ease": _E}


SLIDES = [
    {"img": "HERO", **_LB},                                     # s0   title: Singapore from the sea, 1823
    {"img": "FARQ", **_LB},                                     # s1   the teacher meets Farquhar
    {"img": "KRIS", **_v([1.0, 1.04, 1.08], [(0.5, 0.5)] * 3)}, # s2-3 a man run amok; Farquhar falls
    {"img": "HIK1849", **_LB},                                  # s4   Abdullah and the Hikayat
    {"img": "BUGIS", **_LB},                                    # s5-7 the debt
]
SCHEDULE = [(0.0, 0), (4.475, 1), (19.925, 2), (34.6, 3), (49.55, 4)]
TOTAL_DURATION = 65.975
TIMING_JSON = "audio/munshi-abdullah-the-scribe-who-watched-singapore-begin.timing.json"

BURN_CAPTIONS = True
CAPTION_FONT_RATIO = 0.032
CAPTION_MAX_WIDTH_FRAC = 0.86
CAPTION_Y_FRAC = 0.70
