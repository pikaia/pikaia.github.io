"""Short config for the Japanese fishermen post - the hook (sentences 0-2):
Japanese fishermen supplied 40 to 50 per cent of Singapore's fresh fish, and
within a few years the fleet was cut down. 3 slides, 31.5s. Landscape photos in
a vertical frame use letterbox, not cover, so the subject is not cropped out.
"""

WIDTH, HEIGHT = 1080, 1920

_U = "https://upload.wikimedia.org/wikipedia/commons"

IMAGES = {
    "PASIR": f"{_U}/thumb/c/c8/KITLV_-_79910_-_Kleingrothe%2C_C.J._-_Medan_-_Pasir_Puteh_at_Singapore_-_circa_1910.tif/lossy-page1-1280px-KITLV_-_79910_-_Kleingrothe%2C_C.J._-_Medan_-_Pasir_Puteh_at_Singapore_-_circa_1910.tif.jpg",
    "ROCHOR": f"{_U}/thumb/2/2b/KITLV_-_79908_-_Kleingrothe%2C_C.J._-_Medan_-_Rochor%2C_Singapore_proa_harbor_-_circa_1910.tif/lossy-page1-1280px-KITLV_-_79908_-_Kleingrothe%2C_C.J._-_Medan_-_Rochor%2C_Singapore_proa_harbor_-_circa_1910.tif.jpg",
    "ST1003": "/assets/images/straits-times-1939-10-03-page-10.jpg",
}

_LTB = {"type": "letterbox", "zoom": [1.0, 1.04, 1.08], "pan": [(0.5, 0.5)] * 3, "ease": "ease-in-out"}
_LTBO = {"type": "letterbox", "zoom": [1.08, 1.04, 1.0], "pan": [(0.5, 0.5)] * 3, "ease": "ease-out"}

SLIDES = [
    {"img": "PASIR", **_LTBO},        # 0  s0   title
    {"img": "ROCHOR", **_LTB},        # 1  s1   40 to 50 per cent of the fresh fish
    {"img": "ST1003", **_LTBO},       # 2  s2   licence limits, boycott, suspicion
]

SCHEDULE = [
    (0.0, 0), (4.0, 1), (20.0, 2),
]
TOTAL_DURATION = 31.5
TIMING_JSON = "audio/the-japanese-fishermen-who-fed-prewar-singapore.timing.json"

# Shorts keep burned-in narration captions (muted autoplay); main videos do not -
# they rely on the uploaded .srt.
BURN_CAPTIONS = True
CAPTION_FONT_RATIO = 0.032
CAPTION_MAX_WIDTH_FRAC = 0.86
CAPTION_Y_FRAC = 0.80
