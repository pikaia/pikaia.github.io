"""Short config for the 1915 Singapore Mutiny post - the hook (sentences
0-3): a regiment rising on Chinese New Year and the warships that put it
down. 4 slides, 36.65s. Landscape and portrait images in a vertical
frame all use letterbox so nothing is cropped out.
"""

WIDTH, HEIGHT = 1080, 1920

_U = "https://upload.wikimedia.org/wikipedia/commons"

IMAGES = {
    "SAILORS": f"{_U}/thumb/4/46/REVIEW_OF_JAPANESE_SAILORS_ALTER_THE_MUTINY_AT_SINGAPORE%2C_1915.png/1280px-REVIEW_OF_JAPANESE_SAILORS_ALTER_THE_MUTINY_AT_SINGAPORE%2C_1915.png",
    "HAV": f"{_U}/7/7b/A_Musalman_Rajput_Havildar_of_the_5th_light_infantry_and_a_Jat_Havildar_of_the_6th_Jat_light_infantry.jpg",
}

_LTB = {"type": "letterbox", "zoom": [1.0, 1.04, 1.08], "pan": [(0.5, 0.5)] * 3, "ease": "ease-in-out"}
_LTBO = {"type": "letterbox", "zoom": [1.08, 1.04, 1.0], "pan": [(0.5, 0.5)] * 3, "ease": "ease-out"}

SLIDES = [
    {"img": "SAILORS", **_LTB},    # 0  s0   title
    {"img": "HAV", **_LTB},        # 1  s1   afternoon of 15 Feb, Alexandra Barracks
    {"img": "HAV", **_LTBO},       # 2  s2   by evening turned their rifles
    {"img": "SAILORS", **_LTBO},   # 3  s3   warships from Japan, France, Russia
]

SCHEDULE = [
    (0.0, 0), (6.375, 1), (23.875, 2), (30.1, 3),
]
TOTAL_DURATION = 36.65
TIMING_JSON = "audio/the-1915-singapore-mutiny-the-week-a-regiment-rose-on-chinese-new-year.timing.json"

# Shorts keep burned-in narration captions (muted autoplay); main videos do not -
# they rely on the uploaded .srt.
BURN_CAPTIONS = True
CAPTION_FONT_RATIO = 0.032
CAPTION_MAX_WIDTH_FRAC = 0.86
CAPTION_Y_FRAC = 0.80
