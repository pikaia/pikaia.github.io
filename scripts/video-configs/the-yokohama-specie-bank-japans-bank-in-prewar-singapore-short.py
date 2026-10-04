"""Short config for the Yokohama Specie Bank post.

The post's opening, sentences 0-7 (0-70.575s, over the 60s TikTok line): the
bank reopening in occupied Singapore in March 1942 in the British bank's
building, its 25 years in Raffles Place, and what the bank was. The Syonan
notices fill the vertical frame; the Shanghai postcard is already portrait.
"""

_U = "https://upload.wikimedia.org/wikipedia/commons"
_C = f"{_U}/thumb"
_A = "/assets/images"

WIDTH, HEIGHT = 1080, 1920

IMAGES = {
    "CQ1910": f"{_C}/f/f0/KITLV_-_79887_-_Kleingrothe%2C_C.J._-_Medan_-_Collyer_Quay%2C_Quay_in_Singapore_-_circa_1910.tif/lossy-page1-1920px-KITLV_-_79887_-_Kleingrothe%2C_C.J._-_Medan_-_Collyer_Quay%2C_Quay_in_Singapore_-_circa_1910.tif.jpg",
    "BONHAM": f"{_U}/a/a1/Bonham_Building_1907.jpg",
    "HQ1923": f"{_U}/e/e5/Yokohama_shokin_bank_Kanto_Daishinsai.jpg",
    "SHANGHAI": f"{_U}/c/ce/Yokohama_Specie_Bank_03.jpg",
    "SB1930": f"{_A}/straits-budget-1930-12-04-page-2.jpg",
    "SY420317": f"{_A}/syonan-shimbun-1942-03-17-page-4.jpg",
    "SY420320": f"{_A}/syonan-shimbun-1942-03-20-page-2.jpg",
}

_E = "ease-in-out"
SLIDES = [
    {"img": "CQ1910", "type": "cover", "zoom": [1.0, 1.05, 1.1], "pan": [(0.75, 0.4)] * 3, "ease": _E},    # s0  title
    {"img": "SY420317", "type": "cover", "zoom": [2.21, 2.3, 2.4], "pan": [(1.0, 0.617), (1.0, 0.613), (1.0, 0.609)], "ease": _E},  # s1 reopening
    {"img": "SB1930", "type": "cover", "zoom": [1.29, 1.35, 1.4], "pan": [(0.278, 0.0), (0.307, 0.0), (0.325, 0.0)], "ease": _E},  # s2 Meyer Chambers
    {"img": "SY420320", "type": "cover", "zoom": [2.21, 2.3, 2.4], "pan": [(1.0, 0.397), (1.0, 0.401), (1.0, 0.404)], "ease": _E},  # s3 new address
    {"img": "BONHAM", "type": "cover", "zoom": [1.0, 1.05, 1.1], "pan": [(0.5, 0.5)] * 3, "ease": _E},    # s4-5 since 1916
    {"img": "HQ1923", "type": "cover", "zoom": [1.0, 1.05, 1.1], "pan": [(0.45, 0.5)] * 3, "ease": _E},   # s6 founded 1880
    {"img": "SHANGHAI", "type": "cover", "zoom": [1.0, 1.04, 1.08], "pan": [(0.5, 0.4)] * 3, "ease": _E},  # s7 specie
]
SCHEDULE = [(0.0, 0), (4.775, 1), (16.45, 2), (20.65, 3), (32.225, 4), (53.925, 5), (63.9, 6)]
TOTAL_DURATION = 70.575
TIMING_JSON = "audio/the-yokohama-specie-bank-japans-bank-in-prewar-singapore.timing.json"

BURN_CAPTIONS = True
CAPTION_FONT_RATIO = 0.032
CAPTION_MAX_WIDTH_FRAC = 0.86
CAPTION_Y_FRAC = 0.70
