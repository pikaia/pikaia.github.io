"""Short config for the 1867 transfer post.

The post's opening, sentences 0-9 (0-89.825s, over the 60s TikTok line): the
Town Hall ceremony of 1 April 1867, the forty years under India, the
merchants' campaign, and Governor Ord walking in without removing his hat.
"""

_U = "https://upload.wikimedia.org/wikipedia/commons"
_C = f"{_U}/thumb"

WIDTH, HEIGHT = 1080, 1920

IMAGES = {
    "TOWNHALL": f"{_U}/6/66/Town_Hall%2C_Singapore_-_1860s.jpg",
    "ESPLANADE": f"{_C}/d/d4/Gezicht_op_de_Esplanade_te_Singapore%2C_RP-F-F01025-BH.jpg/1280px-Gezicht_op_de_Esplanade_te_Singapore%2C_RP-F-F01025-BH.jpg",
    "HARBOUR": f"{_C}/7/79/KITLV_-_29175_-_View_of_the_harbor_of_Singapore_-_1860.tif/lossy-page1-1920px-KITLV_-_29175_-_View_of_the_harbor_of_Singapore_-_1860.tif.jpg",
    "TOWN": f"{_C}/1/16/Gezicht_op_Singapore%2C_RP-F-F01025-AZ.jpg/1280px-Gezicht_op_Singapore%2C_RP-F-F01025-AZ.jpg",
    "ORD": f"{_U}/3/3c/Sir_Harry_Ord.jpg",
    "ORD2": f"{_U}/7/7f/HarryStGeorgeOrd-1867-1873.jpg",
}

CREDITS = {
    "ORD2": "Harry Ord as Governor of the Straits Settlements, 1867-73, G. R. Lambert, public domain, via Wikimedia Commons",
}

_E = "ease-in-out"
_LB = {"type": "letterbox", "zoom": [1.0, 1.03, 1.06], "pan": [(0.5, 0.5)] * 3, "ease": _E}


def _v(zoom, pan):
    return {"type": "cover", "zoom": zoom, "pan": pan, "ease": _E}


SLIDES = [
    {"img": "TOWNHALL", **_v([1.0, 1.04, 1.08], [(0.45, 0.5)] * 3)},                    # s0  title
    {"img": "TOWNHALL", **_v([1.1, 1.15, 1.2], [(0.6, 0.5)] * 3)},                      # s1  the salute, 1 April 1867
    {"img": "ESPLANADE", **_v([1.6, 1.65, 1.7], [(0.45, 0.4)] * 3)},                   # s2  the crowd; the Order read
    {"img": "HARBOUR", **_v([1.15, 1.15, 1.15], [(0.1, 0.5), (0.5, 0.5), (0.9, 0.5)])},    # s3-4 forty years; now London
    {"img": "TOWN", **_v([1.4, 1.45, 1.5], [(0.75, 0.5)] * 3)},                         # s5-6 the merchants' campaign
    {"img": "TOWNHALL", **_v([1.2, 1.15, 1.1], [(0.4, 0.5)] * 3)},                      # s7  Buckley's account
    {"img": "ORD", **_LB},                                                               # s8  Ord keeps his hat on
    {"img": "ORD2", **_LB},                                                              # s9  "was never removed"
]
SCHEDULE = [(0.0, 0), (7.2, 1), (19.7, 2), (28.3, 3), (43.1, 4), (59.1, 5), (74.9, 6), (85.275, 7)]
TOTAL_DURATION = 89.825
TIMING_JSON = "audio/why-singapore-merchants-asked-to-leave-british-india-1867.timing.json"

BURN_CAPTIONS = True
CAPTION_FONT_RATIO = 0.032
CAPTION_MAX_WIDTH_FRAC = 0.86
CAPTION_Y_FRAC = 0.70
