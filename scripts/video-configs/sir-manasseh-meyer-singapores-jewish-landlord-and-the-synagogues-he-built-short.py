"""Short config for the Sir Manasseh Meyer post.

The post's opening, sentences 0-7 (0-77.925s, over the 60s TikTok line): who he
was, what he built and what lasted, and his early years. The Chesed-El photo and
his 1921 portrait fill the vertical frame as covers; the old street photos and
the 1929 page are letterboxed; the property map is letterboxed and frozen.
"""

WIDTH, HEIGHT = 1080, 1920

IMAGES = {
    "HERO": "https://upload.wikimedia.org/wikipedia/commons/thumb/2/21/Chesed-El_Synagogue%2C_Singapore_-_20060529.jpg/1280px-Chesed-El_Synagogue%2C_Singapore_-_20060529.jpg",
    "MEYER": "https://upload.wikimedia.org/wikipedia/commons/4/4b/Manasseh_Meyer.jpg",
    "RP1890": "https://upload.wikimedia.org/wikipedia/commons/thumb/8/8d/KITLV_-_103753_-_Raffles_Place%2C_Singapore_-_circa_1890.tif/lossy-page1-1280px-KITLV_-_103753_-_Raffles_Place%2C_Singapore_-_circa_1890.tif.jpg",
    "MAP1": "/assets/images/meyer-map-1.png",
    "ST1929": "/assets/images/straits-times-1929-03-01-page-11.jpg",
    "COLLYER": "https://upload.wikimedia.org/wikipedia/commons/thumb/5/50/KITLV_-_103744_-_Collyer_Quay_in_Singapore_-_circa_1890.tif/lossy-page1-1280px-KITLV_-_103744_-_Collyer_Quay_in_Singapore_-_circa_1890.tif.jpg",
    "NBR": "https://upload.wikimedia.org/wikipedia/commons/thumb/8/80/KITLV_-_43317_-_Lambert_%26_Co.%2C_G.R._-_Singapore_-_The_North_Bridge_Road%2C_Singapore_-_circa_1900.tiff/lossy-page1-1280px-KITLV_-_43317_-_Lambert_%26_Co.%2C_G.R._-_Singapore_-_The_North_Bridge_Road%2C_Singapore_-_circa_1900.tiff.jpg",
}

CREDITS = {
    "MAP1": "Map by Lesser Known Singapore; map data (c) OpenStreetMap contributors",
    "NBR": "G. R. Lambert & Co., KITLV, CC BY-SA 4.0, via Wikimedia Commons",
}

_E = "ease-in-out"
_LB = {"type": "letterbox", "zoom": [1.0, 1.03, 1.06], "pan": [(0.5, 0.5)] * 3, "ease": _E}
_GFX = {"type": "letterbox", "zoom": [1, 1, 1], "pan": [(0.5, 0.5)] * 3}


def _v(zoom, pan):
    return {"type": "cover", "zoom": zoom, "pan": pan, "ease": _E}


SLIDES = [
    {"img": "HERO", **_v([1.0, 1.04, 1.08], [(0.5, 0.5)] * 3)}, # s0  title
    {"img": "MEYER", **_v([1.0, 1.03, 1.06], [(0.5, 0.4)] * 3)},# s1  arrived 1861, died 1930 (names him)
    {"img": "RP1890", **_LB},                                   # s2  trading firm, property, synagogues
    {"img": "MAP1", **_GFX},                                    # s3  what is gone, what lasted
    {"img": "ST1929", **_LB},                                   # s4  born in Baghdad (names him; the page carries his portrait)
    {"img": "COLLYER", **_LB},                                  # s5  uncle Joshua's firm (no portrait)
    {"img": "NBR", **_LB},                                      # s6  St Joseph's; back to Calcutta (s7)
]
SCHEDULE = [(0.0, 0), (5.425, 1), (20.7, 2), (32.95, 3), (41.9, 4), (52.525, 5), (61.35, 6)]
TOTAL_DURATION = 77.925
TIMING_JSON = "audio/sir-manasseh-meyer-singapores-jewish-landlord-and-the-synagogues-he-built.timing.json"

BURN_CAPTIONS = True
CAPTION_FONT_RATIO = 0.032
CAPTION_MAX_WIDTH_FRAC = 0.86
CAPTION_Y_FRAC = 0.70
