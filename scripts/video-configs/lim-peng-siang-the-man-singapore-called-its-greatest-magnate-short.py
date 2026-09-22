"""Short config for the Lim Peng Siang post - the hook (sentences 0-2):
the 1936 "greatest magnates" line and what he built. 3 slides, 26.925s.
Landscape photos in a vertical frame use letterbox, not cover, so the
harbour scene is not cropped out.
"""

WIDTH, HEIGHT = 1080, 1920

_U = "https://upload.wikimedia.org/wikipedia/commons"

IMAGES = {
    "BOATQUAY": f"{_U}/thumb/f/fe/Binnenhaven_van_Singapore_The_boat_quay_Singapore_%28titel_op_object%29%2C_RP-F-00-5018-39.jpg/1920px-Binnenhaven_van_Singapore_The_boat_quay_Singapore_%28titel_op_object%29%2C_RP-F-00-5018-39.jpg",
    "PORTRAIT": f"{_U}/1/1c/Lim_Peng_Siang.png",
}

_LTB = {"type": "letterbox", "zoom": [1.0, 1.04, 1.08], "pan": [(0.5, 0.5)] * 3, "ease": "ease-in-out"}
_LTBO = {"type": "letterbox", "zoom": [1.08, 1.04, 1.0], "pan": [(0.5, 0.5)] * 3, "ease": "ease-out"}

SLIDES = [
    {"img": "BOATQUAY", **_LTBO},      # 0  s0   title
    {"img": "PORTRAIT", **_LTB},       # 1  s1   1936 greatest magnates
    {"img": "BOATQUAY", **_LTB},       # 2  s2   rice mill and oil mill into a group
]

SCHEDULE = [
    (0.0, 0), (4.9, 1), (14.925, 2),
]
TOTAL_DURATION = 26.925
TIMING_JSON = "audio/lim-peng-siang-the-man-singapore-called-its-greatest-magnate.timing.json"

# Shorts keep burned-in narration captions (muted autoplay); main videos do not -
# they rely on the uploaded .srt.
BURN_CAPTIONS = True
CAPTION_FONT_RATIO = 0.032
CAPTION_MAX_WIDTH_FRAC = 0.86
CAPTION_Y_FRAC = 0.80
