"""Short config for the Fullerton Building post - the hook (sentences
0-2): a post office whose rooftop beacon swept the harbour for twenty
years. 3 slides, 26.975s. Landscape photos in a vertical frame use
letterbox, not cover, so the building is not cropped out.
"""

WIDTH, HEIGHT = 1080, 1920

_U = "https://upload.wikimedia.org/wikipedia/commons"

IMAGES = {
    "HERO": f"{_U}/thumb/1/19/Singapore%2C_KITLV_1404891.tiff/lossy-page1-1280px-Singapore%2C_KITLV_1404891.tiff.jpg",
    "MODERN2018": f"{_U}/f/f3/Singapore_-_The_Fullerton_Hotel_IMG_9254.jpg",
}

_LTB = {"type": "letterbox", "zoom": [1.0, 1.04, 1.08], "pan": [(0.5, 0.5)] * 3, "ease": "ease-in-out"}
_LTBO = {"type": "letterbox", "zoom": [1.08, 1.04, 1.0], "pan": [(0.5, 0.5)] * 3, "ease": "ease-out"}

SLIDES = [
    {"img": "HERO", **_LTBO},         # 0  s0   title
    {"img": "HERO", **_LTB},          # 1  s1   beacon for twenty years
    {"img": "MODERN2018", **_LTBO},   # 2  s2   many people walk past the hotel
]

SCHEDULE = [
    (0.0, 0), (4.7, 1), (18.6, 2),
]
TOTAL_DURATION = 26.975
TIMING_JSON = "audio/the-fullerton-building-the-post-office-with-a-lighthouse-on-the-roof.timing.json"

# Shorts keep burned-in narration captions (muted autoplay); main videos do not -
# they rely on the uploaded .srt.
BURN_CAPTIONS = True
CAPTION_FONT_RATIO = 0.032
CAPTION_MAX_WIDTH_FRAC = 0.86
CAPTION_Y_FRAC = 0.80
