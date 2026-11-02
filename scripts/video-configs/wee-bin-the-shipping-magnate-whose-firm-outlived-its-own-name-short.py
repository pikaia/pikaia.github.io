"""Short config for the Wee Bin post.

The post's opening, sentences 0-7 (0-70.28s): the March 1911
announcement of the winding-up, the auction of the steamers, the
puzzle of the founder's grave - he had died in 1868 - the firm at
its height, and who Wee Bin was. Sentences 0-6 would have ended at
62.25s, too close to TikTok's 1-minute floor for Creator Rewards,
so the Short runs one sentence longer, to 70.28s. The founder is
named in s4-7; his portrait shows only under his own sentences
(s4-5), panned high to the face. Every slide is letterboxed.
"""

WIDTH, HEIGHT = 1080, 1920

IMAGES = {
    "PORT": "https://upload.wikimedia.org/wikipedia/commons/thumb/5/5e/KITLV_-_150813_-_Lambert_%26_Co.%2C_G.R._-_Singapore_-_Port_at_Singapore_-_circa_1890.tif/lossy-page1-1280px-KITLV_-_150813_-_Lambert_%26_Co.%2C_G.R._-_Singapore_-_Port_at_Singapore_-_circa_1890.tif.jpg",
    "WEEBIN": "https://upload.wikimedia.org/wikipedia/commons/e/ee/Wee_Bin.jpg",
    "QUAY": "https://upload.wikimedia.org/wikipedia/commons/f/fe/Binnenhaven_van_Singapore_The_boat_quay_Singapore_%28titel_op_object%29%2C_RP-F-00-5018-39.jpg",
    "DOCK": "https://upload.wikimedia.org/wikipedia/commons/thumb/c/c1/KITLV_-_29164_-_The_steamship_Brisbane_in_dry_dock_in_Singapore_-_1860.tif/lossy-page1-1280px-KITLV_-_29164_-_The_steamship_Brisbane_in_dry_dock_in_Singapore_-_1860.tif.jpg",
    "NBQ1900": "https://upload.wikimedia.org/wikipedia/commons/b/b6/Singapore_Boat_Quay_ca._1900.jpg",
    "COLLYER": "https://upload.wikimedia.org/wikipedia/commons/thumb/f/f0/KITLV_-_79887_-_Kleingrothe%2C_C.J._-_Medan_-_Collyer_Quay%2C_Quay_in_Singapore_-_circa_1910.tif/lossy-page1-1280px-KITLV_-_79887_-_Kleingrothe%2C_C.J._-_Medan_-_Collyer_Quay%2C_Quay_in_Singapore_-_circa_1910.tif.jpg",
    "RIVER1870": "https://upload.wikimedia.org/wikipedia/commons/thumb/a/a2/KITLV_-_106514_-_Port_on_the_river_in_Singapore_-_circa_1870.tif/lossy-page1-1280px-KITLV_-_106514_-_Port_on_the_river_in_Singapore_-_circa_1870.tif.jpg"
}

# Every image is captioned in the post or its gallery.
CREDITS = {}

# The main video's thumbnail grid, re-panned for tall cells.
THUMBNAIL = [
    {"img": "PORT", "pan": (0.5, 0.5)},
    {"img": "WEEBIN", "pan": (0.5, 0.25)},
    {"img": "DOCK", "pan": (0.5, 0.5)},
    {"img": "COLLYER", "pan": (0.5, 0.5)},
]

_E = "ease-in-out"
_LB = {"type": "letterbox", "zoom": [1.0, 1.03, 1.06], "pan": [(0.5, 0.5)] * 3, "ease": _E}
# The tall portrait in letterbox: keep the whole frame, no pan needed.
_LBP = {"type": "letterbox", "zoom": [1.0, 1.03, 1.06], "pan": [(0.5, 0.5)] * 3, "ease": _E}

SLIDES = [
    {"img": "PORT", **_LB},   # s0 title: the port at Singapore, c. 1890
    {"img": "NBQ1900", **_LB},   # s1 the March 1911 announcement
    {"img": "QUAY", **_LB},   # s2-3 the quote; the steamers sold by auction
    {"img": "WEEBIN", **_LBP},   # s4-5 the founder's grave: died 1868 (his portrait)
    {"img": "PORT", **_LB},   # s6 the largest Chinese shipping business in Singapore
    {"img": "RIVER1870", **_LB},   # s7 a Hokkien, born 1823 in Longxi county
]
SCHEDULE = [(0, 0), (4.75, 1), (12.575, 2), (31.35, 3), (41.925, 4), (62.25, 5)]
TOTAL_DURATION = 70.28
TIMING_JSON = "audio/wee-bin-the-shipping-magnate-whose-firm-outlived-its-own-name.timing.json"

BURN_CAPTIONS = True
CAPTION_FONT_RATIO = 0.032
CAPTION_MAX_WIDTH_FRAC = 0.86
CAPTION_Y_FRAC = 0.70

# The avatar presenter, cartoon with motion: corner bubble for the first and last 30 s.
AVATAR = {"ranges": [(0, 30), (-30, None)], "motion": True}
