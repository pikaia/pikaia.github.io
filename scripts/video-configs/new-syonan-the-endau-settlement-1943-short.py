"""Short config for the Endau settlement post.

The post's opening, sentences 0-7 (0-70.825s, over the 60s TikTok line): the
first party leaving Syonan on 1 February 1944, who they were, the 7,000 a year
later, and why Syonan was hungry. The 2 February 1944 page fills the vertical
frame on its headline; the 14 December 1944 page on its anniversary report.
"""

_U = "https://upload.wikimedia.org/wikipedia/commons"
_C = f"{_U}/thumb"
_A = "/assets/images"

WIDTH, HEIGHT = 1080, 1920

IMAGES = {
    "HERO": f"{_C}/b/bb/Endau_Malaya_February_1964.jpg/1280px-Endau_Malaya_February_1964.jpg",
    "FEB2": f"{_A}/syonan-shimbun-1944-02-02-page-2.jpg",
    "DEC14": f"{_A}/syonan-shimbun-1944-12-14-page-2.jpg",
    "CAUSEWAY": f"{_C}/c/c4/Djohor_Baru_Bridge_in_Singapore_%28Syonan%29%2C_Djawa_Baroe%2C_Vol._1%2C_Iss._4_%281943-02-15%29%2C_pp18-19.jpg/1280px-Djohor_Baru_Bridge_in_Singapore_%28Syonan%29%2C_Djawa_Baroe%2C_Vol._1%2C_Iss._4_%281943-02-15%29%2C_pp18-19.jpg",
    "DOWNTOWN": f"{_C}/5/58/Downtown_Singapore_%28Syonan%29%2C_Djawa_Baroe%2C_Vol._1%2C_Iss._4_%281943-02-15%29%2C_p18.jpg/1280px-Downtown_Singapore_%28Syonan%29%2C_Djawa_Baroe%2C_Vol._1%2C_Iss._4_%281943-02-15%29%2C_p18.jpg",
    "SYOMAP": f"{_C}/4/4a/SyonanSingapore.jpg/1920px-SyonanSingapore.jpg",
}

CREDITS = {
    "SYOMAP": "A Japanese map of Syonan-to, 1942, Magyer Lohasa, CC BY-SA 4.0, via Wikimedia Commons",
}

_E = "ease-in-out"


def _v(zoom, pan):
    return {"type": "cover", "zoom": zoom, "pan": pan, "ease": _E}


SLIDES = [
    {"img": "HERO", **_v([1.0, 1.05, 1.1], [(0.4, 0.5)] * 3)},                              # s0  title
    {"img": "FEB2", **_v([1.7, 1.75, 1.8], [(0.42, 0.0), (0.42, 0.01), (0.42, 0.02)])},     # s1  the first party leaves
    {"img": "FEB2", **_v([1.0, 1.03, 1.06], [(0.45, 0.0), (0.45, 0.02), (0.45, 0.04)])},    # s2  "pioneers"
    {"img": "CAUSEWAY", "type": "letterbox", "zoom": [1.0, 1.03, 1.06], "pan": [(0.5, 0.5)] * 3, "ease": _E},  # s3  who they were
    {"img": "DEC14", **_v([1.6, 1.65, 1.7], [(0.05, 0.27), (0.06, 0.28), (0.07, 0.29)])},   # s4  7,000 within a year
    {"img": "DOWNTOWN", "type": "letterbox", "zoom": [1.0, 1.03, 1.06], "pan": [(0.5, 0.5)] * 3, "ease": _E},  # s5 not enough to eat
    {"img": "SYOMAP", **_v([1.0, 1.04, 1.08], [(0.5, 0.5)] * 3)},                           # s6-7 imported rice; shipping lost
]
SCHEDULE = [(0.0, 0), (4.3, 1), (19.625, 2), (24.675, 3), (39.325, 4), (44.625, 5), (52.025, 6)]
TOTAL_DURATION = 70.825
TIMING_JSON = "audio/new-syonan-the-endau-settlement-1943.timing.json"

BURN_CAPTIONS = True
CAPTION_FONT_RATIO = 0.032
CAPTION_MAX_WIDTH_FRAC = 0.86
CAPTION_Y_FRAC = 0.70
