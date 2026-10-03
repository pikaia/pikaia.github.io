"""Short config for the UOB / United Chinese Bank post.

The post's opening, sentences 0-6 (0-67.675s, over the 60s TikTok line):
the 1935 opening at Chulia and Bonham Street, the founders and capital, UOB
ninety years on, growth by acquisition, and Wee Kheng Chiang. Tall photos
fill the vertical frame with `cover`; the 1935 pages push in on the
"New bank opens" report and on Wee Kheng Chiang's photo.
"""

_U = "https://upload.wikimedia.org/wikipedia/commons"
_C = f"{_U}/thumb"
_A = "/assets/images"

WIDTH, HEIGHT = 1080, 1920

IMAGES = {
    "RP1920S": f"{_C}/7/7c/KITLV_A723_-_Raffles_Place_te_Singapore%2C_KITLV_87929.tiff/lossy-page1-1280px-KITLV_A723_-_Raffles_Place_te_Singapore%2C_KITLV_87929.tiff.jpg",
    "BONHAM": f"{_U}/a/a1/Bonham_Building_1907.jpg",
    "PLAZA_OUB": f"{_C}/c/c9/Oub-uob-towers_cropped.jpg/1280px-Oub-uob-towers_cropped.jpg",
    "PLAQUE": f"{_C}/3/36/United_Overseas_Bank_History_Plaque.jpg/1280px-United_Overseas_Bank_History_Plaque.jpg",
    "ST351001": f"{_A}/straits-times-1935-10-01-page-12.jpg",
    "MT13": f"{_A}/malaya-tribune-1935-10-02-page-13.jpg",
}

_E = "ease-in-out"
SLIDES = [
    {"img": "RP1920S", "type": "cover", "zoom": [1.0, 1.05, 1.1], "pan": [(0.45, 0.5)] * 3, "ease": _E},     # s0  title
    {"img": "BONHAM", "type": "cover", "zoom": [1.0, 1.05, 1.1], "pan": [(0.42, 0.5)] * 3, "ease": _E},      # s1  opened 1 Oct 1935
    {"img": "MT13", "type": "cover", "zoom": [2.2, 2.3, 2.4], "pan": [(0.25, 0.12)] * 3, "ease": _E},        # s2  "New bank opens"
    {"img": "PLAZA_OUB", "type": "cover", "zoom": [1.0, 1.04, 1.08], "pan": [(0.5, 0.4)] * 3, "ease": _E},   # s3  UOB today
    {"img": "PLAQUE", "type": "cover", "zoom": [1.0, 1.04, 1.08], "pan": [(0.5, 0.45)] * 3, "ease": _E},     # s4  buying other banks
    {"img": "ST351001", "type": "cover", "zoom": [2.2, 2.3, 2.4], "pan": [(0.66, 0.19), (0.66, 0.2), (0.66, 0.21)], "ease": _E},  # s5-6 Wee Kheng Chiang
]
SCHEDULE = [(0.0, 0), (6.375, 1), (21.475, 2), (34.275, 3), (41.6, 4), (47.275, 5)]
TOTAL_DURATION = 67.675
TIMING_JSON = "audio/uob-the-united-chinese-bank-of-1935-and-the-family-that-built-it.timing.json"

BURN_CAPTIONS = True
CAPTION_FONT_RATIO = 0.032
CAPTION_MAX_WIDTH_FRAC = 0.86
CAPTION_Y_FRAC = 0.70
