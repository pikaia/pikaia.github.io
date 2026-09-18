"""Short config for the "Banana Money" post - the hook (sentences 0-3):
a $10 note that promised ten dollars and never paid out. 4 slides,
29.85s.
"""

WIDTH, HEIGHT = 1080, 1920

_U = "https://upload.wikimedia.org/wikipedia/commons"

IMAGES = {
    "HERO": f"{_U}/b/ba/MAL-M7c-Malaya-Japanese_Occupation-10_Dollars_ND_%281944%29.jpg",
}

_LTB = {"type": "letterbox", "zoom": [1.0, 1.04, 1.08], "pan": [(0.5, 0.5)] * 3, "ease": "ease-in-out"}
_LTBO = {"type": "letterbox", "zoom": [1.08, 1.04, 1.0], "pan": [(0.5, 0.5)] * 3, "ease": "ease-out"}

SLIDES = [
    {"img": "HERO", **_LTB},      # 0  s0   title
    {"img": "HERO", **_LTBO},     # 1  s1   sells today for a few dollars
    {"img": "HERO", **_LTB},      # 2  s2   note promises pay the bearer
    {"img": "HERO", **_LTBO},     # 3  s3   it never did
]

SCHEDULE = [
    (0.0, 0), (4.675, 1), (21.325, 2), (28.0, 3),
]
TOTAL_DURATION = 29.85
TIMING_JSON = "audio/banana-money-the-wartime-currency-that-inflated-to-nothing.timing.json"

# Shorts keep burned-in narration captions (muted autoplay); main videos do not -
# they rely on the uploaded .srt.
BURN_CAPTIONS = True
CAPTION_FONT_RATIO = 0.032
CAPTION_MAX_WIDTH_FRAC = 0.86
CAPTION_Y_FRAC = 0.80
