"""Short config for the Change Alley post.

The post's opening, sentences 0-6 (0-64.95s, over the 60s TikTok line): the
lane from Clifford Pier to Raffles Place, its money-changers and bazaar, the
1989 closure and the 1890 naming. The 1939 Sunday Times back page fills the
vertical frame for the bazaar sentence.
"""

_U = "https://upload.wikimedia.org/wikipedia/commons"
_C = f"{_U}/thumb"
_A = "/assets/images"

WIDTH, HEIGHT = 1080, 1920

IMAGES = {
    "HERO": f"{_C}/f/f2/Change_Alley_Singapore_street_sign_January_1965.jpg/1280px-Change_Alley_Singapore_street_sign_January_1965.jpg",
    "CLIFFORD71": f"{_C}/9/9d/545a_Singapore_1971_%2851316139004%29.jpg/1280px-545a_Singapore_1971_%2851316139004%29.jpg",
    "COLLYER1910": f"{_C}/4/4b/Collyer_Quay%2C_Singapore_postcard.jpg/1280px-Collyer_Quay%2C_Singapore_postcard.jpg",
    "ST1939": f"{_A}/sunday-times-1939-02-12-page-32.jpg",
    "ARCADE05": f"{_U}/e/e0/Change_Alley%2C_Dec_05.JPG",
    "MAP1890": f"{_C}/b/b9/Map_of_Raffles_Place_from_The_Stranger%27s_Guide_to_Singapore_%281890%29.jpg/1280px-Map_of_Raffles_Place_from_The_Stranger%27s_Guide_to_Singapore_%281890%29.jpg",
}

CREDITS = {
    "MAP1890": "Map of Raffles Place from The Stranger's Guide to Singapore, 1890, B. D. d'Aranjo, public domain, via Wikimedia Commons",
}

_E = "ease-in-out"


def _v(zoom, pan):
    return {"type": "cover", "zoom": zoom, "pan": pan, "ease": _E}


SLIDES = [
    {"img": "HERO", **_v([1.0, 1.03, 1.06], [(0.55, 0.3)] * 3)},          # s0   title: the street sign
    {"img": "CLIFFORD71", **_v([1.0, 1.03, 1.06], [(0.66, 0.5)] * 3)},    # s1   from the sea, Clifford Pier and Shell House
    {"img": "COLLYER1910", **_v([1.0, 1.03, 1.06], [(0.19, 0.5)] * 3)},   # s2   Collyer Quay to Raffles Place
    {"img": "ST1939", **_v([1.0, 1.03, 1.06], [(0.5, 0.3)] * 3)},         # s3   money-changers and the bazaar
    {"img": "ARCADE05", **_v([1.0, 1.03, 1.06], [(0.5, 0.5)] * 3)},       # s4   closed 1989; the arcade now
    {"img": "MAP1890", **_v([1.0, 1.03, 1.06], [(0.5, 0.5)] * 3)},        # s5-6 named in 1890
]
SCHEDULE = [(0.0, 0), (4.6, 1), (14.325, 2), (24.325, 3), (42.65, 4), (51.375, 5)]
TOTAL_DURATION = 64.95
TIMING_JSON = "audio/change-alley-singapores-lane-of-money-changers-and-bargains.timing.json"

BURN_CAPTIONS = True
CAPTION_FONT_RATIO = 0.032
CAPTION_MAX_WIDTH_FRAC = 0.86
CAPTION_Y_FRAC = 0.70
