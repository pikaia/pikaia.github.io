"""Short config for the John Turnbull Thomson post.

The post's opening, sentences 0-5 (0-69.05s, over the 60s TikTok line): the
roads and MRT line named after him, his arrival in 1841 as Government
Surveyor aged twenty, his pictures of 1840s Singapore, his birth at Glororum
and his start as a surveyor in Penang. Thomson gets his own portrait. The
Telok Ayer Market painting fills the frame and the portrait-format 1965
Thomson Road photo fits the vertical frame as a cover; the portrait, the
stonecutters page, the timeline and the Penang painting are letterboxed.
"""

_U = "https://upload.wikimedia.org/wikipedia/commons"
_C = f"{_U}/thumb"
_A = "/assets/images"

WIDTH, HEIGHT = 1080, 1920

IMAGES = {
    "TELOK": f"{_C}/7/77/Telok_Ayer_Market_-_J.T._Thomson.jpg/1280px-Telok_Ayer_Market_-_J.T._Thomson.jpg",
    "ROAD1": f"{_C}/d/da/Thomson_Road_Singapore_January_1965_01.jpg/1280px-Thomson_Road_Singapore_January_1965_01.jpg",
    "THOMSON": f"{_U}/0/03/JohnTurnbullThomson.jpg",
    "STONECUT": f"{_U}/3/35/ChineseKayTribeStonecutters-Singapore.jpg",
    "TIMELINE": f"{_A}/thomson-timeline-chart.png",
    "PENANG": f"{_U}/a/a1/Penang_Museum_historical_painting_537.jpg",
}

CREDITS = {
    "TIMELINE": "Timeline by Lesser Known Singapore",
    "PENANG": "Penang State Museum and Art Gallery, public domain, via Wikimedia Commons",
}

_E = "ease-in-out"
_LB = {"type": "letterbox", "zoom": [1.0, 1.03, 1.06], "pan": [(0.5, 0.5)] * 3, "ease": _E}
_GFX = {"type": "letterbox", "zoom": [1, 1, 1], "pan": [(0.5, 0.5)] * 3}


def _v(zoom, pan):
    return {"type": "cover", "zoom": zoom, "pan": pan, "ease": _E}


SLIDES = [
    {"img": "TELOK", **_v([1.0, 1.04, 1.08], [(0.5, 0.5)] * 3)},   # s0  title
    {"img": "ROAD1", **_v([1.0, 1.03, 1.06], [(0.5, 0.5)] * 3)},   # s1  Thomson Road, the TEL line
    {"img": "THOMSON", **_LB},                                      # s2  arrived 1841, aged twenty
    {"img": "STONECUT", **_LB},                                     # s3  his pictures of people at work
    {"img": "TIMELINE", **_GFX},                                    # s4  born at Glororum, 1821
    {"img": "PENANG", **_LB},                                       # s5  out to Penang in 1838
]
SCHEDULE = [(0.0, 0), (5.125, 1), (15.35, 2), (30.35, 3), (46.35, 4), (54.35, 5)]
TOTAL_DURATION = 69.05
TIMING_JSON = "audio/john-turnbull-thomson-the-surveyor-who-drew-1840s-singapore.timing.json"

BURN_CAPTIONS = True
CAPTION_FONT_RATIO = 0.032
CAPTION_MAX_WIDTH_FRAC = 0.86
CAPTION_Y_FRAC = 0.70
