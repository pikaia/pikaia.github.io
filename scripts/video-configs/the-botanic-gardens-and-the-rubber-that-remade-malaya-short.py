"""Short config for the Botanic Gardens/rubber post - the hidden-origin
hook (sentences 0-3): a beautifully kept UNESCO garden that doesn't
look like the place that single-handedly decided Malaya's economic
future. 4 slides, 39.775s.
"""

WIDTH, HEIGHT = 1080, 1920

_U = "https://upload.wikimedia.org/wikipedia/commons"

IMAGES = {
    "HERO": f"{_U}/2/21/Henry_Nicholas_Ridley%2C_Botanist_%281855-1956%29.jpg",
    "MODERN": f"{_U}/9/93/UNESCO_HERITAGE_AT_BOTANIC_GARDEN_1859.jpg",
}

_LTB = {"type": "letterbox", "zoom": [1.0, 1.04, 1.08], "pan": [(0.5, 0.5)] * 3, "ease": "ease-in-out"}
_LTBO = {"type": "letterbox", "zoom": [1.08, 1.04, 1.0], "pan": [(0.5, 0.5)] * 3, "ease": "ease-out"}

SLIDES = [
    {"img": "HERO", **_LTB},      # 0  s0   title
    {"img": "MODERN", **_LTBO},   # 1  s1   joggers, wedding photographers
    {"img": "MODERN", **_LTB},    # 2  s2   UNESCO World Heritage Site since 2015
    {"img": "MODERN", **_LTBO},   # 3  s3   doesn't look like the place that decided
]

SCHEDULE = [
    (0.0, 0), (4.25, 1), (19.775, 2), (31.45, 3),
]
TOTAL_DURATION = 39.775
TIMING_JSON = "audio/the-botanic-gardens-and-the-rubber-that-remade-malaya.timing.json"

# Shorts keep burned-in narration captions (muted autoplay); main videos do not -
# they rely on the uploaded .srt.
BURN_CAPTIONS = True
CAPTION_FONT_RATIO = 0.032
CAPTION_MAX_WIDTH_FRAC = 0.86
CAPTION_Y_FRAC = 0.80
