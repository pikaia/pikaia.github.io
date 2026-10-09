"""Short config for the Straits dollar post.

The post's opening, sentences 0-6 (0-72.2s, over the 60s TikTok line): the
fixing of the dollar at 2s 4d on 29 January 1906, the next morning's
Straits Times, and the silver dollars Singapore had used before its own.
The 1906 page fills the vertical frame on its EXCHANGE report.
"""

_U = "https://upload.wikimedia.org/wikipedia/commons"
_C = f"{_U}/thumb"
_A = "/assets/images"

WIDTH, HEIGHT = 1080, 1920

IMAGES = {
    "HERO": f"{_C}/e/ee/1_dollar_of_Straits_Settlements%2C_Edward_VII_-_1903_B.png/1280px-1_dollar_of_Straits_Settlements%2C_Edward_VII_-_1903_B.png",
    "ST1906": f"{_A}/straits-times-1906-01-30-page-5.jpg",
    "D1903B": f"{_U}/e/ef/Straits_settlements-1Dollar-1903.jpg",
    "MEX": f"{_C}/3/33/1888_M%C3%A9xico_8_Reals_Trade_Coin_Silver.jpg/1280px-1888_M%C3%A9xico_8_Reals_Trade_Coin_Silver.jpg",
}

_E = "ease-in-out"
_LB = {"type": "letterbox", "zoom": [1.0, 1.03, 1.06], "pan": [(0.5, 0.5)] * 3, "ease": _E}
# The coin photos show both faces side by side; in the vertical frame a cover
# crop centred on the left-hand face fills the frame (the rim is trimmed).
_FACE = {"type": "cover", "zoom": [1.0, 1.03, 1.06], "pan": [(0.15, 0.5), (0.15, 0.5), (0.15, 0.5)], "ease": _E}


def _v(zoom, pan):
    return {"type": "cover", "zoom": zoom, "pan": pan, "ease": _E}


SLIDES = [
    {"img": "HERO", **_FACE},                                                                 # s0  title
    {"img": "ST1906", **_v([1.6, 1.65, 1.7], [(0.0, 0.0), (0.0, 0.01), (0.0, 0.02)])},      # s1  fixed at 2s 4d
    {"img": "ST1906", **_v([1.6, 1.65, 1.7], [(0.0, 0.18), (0.0, 0.22), (0.0, 0.26)])},     # s2  the headline and the letter
    {"img": "ST1906", **_v([1.0, 1.03, 1.06], [(0.2, 0.0), (0.2, 0.02), (0.2, 0.04)])},     # s3  what the day settled
    {"img": "D1903B", **_FACE},                                                               # s4  a dollar of its own
    {"img": "MEX", **_FACE},                                                                  # s5-6 Spanish, then Mexican dollars
]
SCHEDULE = [(0.0, 0), (5.05, 1), (17.625, 2), (34.7, 3), (38.75, 4), (54.675, 5)]
TOTAL_DURATION = 72.2
TIMING_JSON = "audio/the-straits-dollar-singapores-first-money-of-its-own-1903.timing.json"

BURN_CAPTIONS = True
CAPTION_FONT_RATIO = 0.032
CAPTION_MAX_WIDTH_FRAC = 0.86
CAPTION_Y_FRAC = 0.70
