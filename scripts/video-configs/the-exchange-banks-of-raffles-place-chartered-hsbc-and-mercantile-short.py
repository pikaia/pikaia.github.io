"""Short config for the exchange banks of Raffles Place post.

The post's opening, sentences 0-6 (0-67.325s, over the 60s line): the money
of Singapore's trade passing through one square, the three exchange banks,
the towers that replaced their buildings, and what an exchange bank did.
Every slide is letterboxed.
"""

WIDTH, HEIGHT = 1080, 1920

IMAGES = {
    "CB_RP": "https://upload.wikimedia.org/wikipedia/commons/thumb/5/59/The_Chartered_Bank_aan_Raffles_Place_te_Singapore%2C_KITLV_104795.tiff/lossy-page1-1280px-The_Chartered_Bank_aan_Raffles_Place_te_Singapore%2C_KITLV_104795.tiff.jpg",
    "RP1885": "https://upload.wikimedia.org/wikipedia/commons/thumb/9/9f/KITLV_-_103746_-_Lambert_%26_Co._-_Raffles_Place_in_Singapore_-_circa_1885.tif/lossy-page1-1280px-KITLV_-_103746_-_Lambert_%26_Co._-_Raffles_Place_in_Singapore_-_circa_1885.tif.jpg",
    "RP1971": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/dc/71-610_Raffles_Place_Singapore_1971_%2851252222815%29.jpg/1280px-71-610_Raffles_Place_Singapore_1971_%2851252222815%29.jpg",
    "RP1890": "https://upload.wikimedia.org/wikipedia/commons/thumb/8/8d/KITLV_-_103753_-_Raffles_Place%2C_Singapore_-_circa_1890.tif/lossy-page1-1280px-KITLV_-_103753_-_Raffles_Place%2C_Singapore_-_circa_1890.tif.jpg",
    "PIER": "https://upload.wikimedia.org/wikipedia/commons/thumb/0/0f/Johnston_%27s_Pier_and_Hongkong_Shanghai_Bank_Singapore%2C_KITLV_1404895.tiff/lossy-page1-1280px-Johnston_%27s_Pier_and_Hongkong_Shanghai_Bank_Singapore%2C_KITLV_1404895.tiff.jpg",
    "UOBVIEW": "https://upload.wikimedia.org/wikipedia/commons/2/29/View_from_UOB_Plaza_1%2C_Singapore_-_20091211.jpg",  # thumbnail only
}

# Every image is captioned in the post or its gallery.
CREDITS = {}

# The main video's thumbnail grid, re-panned for tall cells.
THUMBNAIL = [
    {"img": "RP1885", "pan": (0.5, 0.5)},
    {"img": "CB_RP", "pan": (0.5, 0.5)},
    {"img": "RP1971", "pan": (0.22, 0.5)},
    {"img": "UOBVIEW", "pan": (0.5, 0.5)},
]

_E = "ease-in-out"
_LB = {"type": "letterbox", "zoom": [1.0, 1.03, 1.06], "pan": [(0.5, 0.5)] * 3, "ease": _E}

SLIDES = [
    {"img": "CB_RP", **_LB},      # s0
    {"img": "RP1885", **_LB},     # s1
    {"img": "RP1971", **_LB},     # s3
    {"img": "RP1890", **_LB},     # s4
    {"img": "PIER", **_LB},       # s6
]
SCHEDULE = [(0.0, 0), (5.7, 1), (28.35, 2), (39.625, 3), (52.6, 4)]
TOTAL_DURATION = 67.325
TIMING_JSON = "audio/the-exchange-banks-of-raffles-place-chartered-hsbc-and-mercantile.timing.json"

BURN_CAPTIONS = True
CAPTION_FONT_RATIO = 0.032
CAPTION_MAX_WIDTH_FRAC = 0.86
CAPTION_Y_FRAC = 0.70

# The avatar presenter, cartoon with motion: corner bubble for the first and last 30 s.
AVATAR = {"ranges": [(0, 30), (-30, None)], "motion": True}
