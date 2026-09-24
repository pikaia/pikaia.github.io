"""Short config for the newspapers post.

Excerpt: the opening hook (sentences 0-4, 0.0-43.225s), from the Chronicle's four
small pages to "public money is once more part of the answer." Ends exactly where
sentence 5 begins in the main config's own timing.
"""

WIDTH, HEIGHT = 1080, 1920

IMAGES = {
    "HERO": "https://upload.wikimedia.org/wikipedia/commons/thumb/9/9f/KITLV_-_103746_-_Lambert_%26_Co._-_Raffles_Place_in_Singapore_-_circa_1885.tif/lossy-page1-1280px-KITLV_-_103746_-_Lambert_%26_Co._-_Raffles_Place_in_Singapore_-_circa_1885.tif.jpg",
    "R1890": "https://upload.wikimedia.org/wikipedia/commons/thumb/8/8d/KITLV_-_103753_-_Raffles_Place%2C_Singapore_-_circa_1890.tif/lossy-page1-1280px-KITLV_-_103753_-_Raffles_Place%2C_Singapore_-_circa_1890.tif.jpg",
    "PV03": "https://upload.wikimedia.org/wikipedia/commons/4/44/Photographic_Views_of_Singapore_Plate_03_Raffles%27_Square.jpg",
}

_PA = {"type": "cover", "zoom": [1.0, 1.05, 1.1], "pan": [(0.5, 0.4), (0.5, 0.5), (0.5, 0.6)], "ease": "ease-in-out"}
_PB = {"type": "cover", "zoom": [1.1, 1.05, 1.0], "pan": [(0.5, 0.6), (0.5, 0.5), (0.5, 0.4)], "ease": "ease-in-out"}

SLIDES = [
    {"img": "HERO", **_PA},  # s0-1 title
    {"img": "R1890", **_PA},  # s2 first newspaper, four small pages
    {"img": "PV03", **_PB},  # s3 subsidy
    {"img": "HERO", **_PB},  # s4 two centuries later
]

SCHEDULE = [(0.0, 0), (6.525, 1), (16.875, 2), (29.725, 3)]
TOTAL_DURATION = 43.225
TIMING_JSON = "audio/who-pays-for-the-news-singapore-has-been-asking-since-1824.timing.json"

BURN_CAPTIONS = True
CAPTION_FONT_RATIO = 0.032
CAPTION_MAX_WIDTH_FRAC = 0.86
CAPTION_Y_FRAC = 0.80
