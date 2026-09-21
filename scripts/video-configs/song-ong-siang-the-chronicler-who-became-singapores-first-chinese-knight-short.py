"""Short config for the Song Ong Siang post - the hook (sentences 0-2):
the 602-page book most people rely on and the man few can name. 3
slides, 28.375s. All letterbox (portrait images in a vertical frame).
"""

WIDTH, HEIGHT = 1080, 1920

_U = "https://upload.wikimedia.org/wikipedia/commons"

IMAGES = {
    "COUPLE": f"{_U}/e/e1/Mr_and_Mrs_Song_Ong_Siang%2C_1923.png",
    "CROP": f"{_U}/4/4c/Sir_Song_Ong_Siang%2C_1923_%28cropped%29.png",
    "TKC": f"{_U}/thumb/c/cc/Tan_Kim_Ching.jpg/1280px-Tan_Kim_Ching.jpg",
}

_LTB = {"type": "letterbox", "zoom": [1.0, 1.04, 1.08], "pan": [(0.5, 0.5)] * 3, "ease": "ease-in-out"}
_LTBO = {"type": "letterbox", "zoom": [1.08, 1.04, 1.0], "pan": [(0.5, 0.5)] * 3, "ease": "ease-out"}

SLIDES = [
    {"img": "COUPLE", **_LTB},    # 0  s0   title
    {"img": "TKC", **_LTBO},      # 1  s1   the 602-page book
    {"img": "CROP", **_LTB},      # 2  s2   the author, few know his name
]

SCHEDULE = [
    (0.0, 0), (5.45, 1), (17.8, 2),
]
TOTAL_DURATION = 28.375
TIMING_JSON = "audio/song-ong-siang-the-chronicler-who-became-singapores-first-chinese-knight.timing.json"

# Shorts keep burned-in narration captions (muted autoplay); main videos do not -
# they rely on the uploaded .srt.
BURN_CAPTIONS = True
CAPTION_FONT_RATIO = 0.032
CAPTION_MAX_WIDTH_FRAC = 0.86
CAPTION_Y_FRAC = 0.80
