"""Short config for the 1948 election post.

Excerpt: the opening hook (sentences 0-4, 0.0-45.38s): the first election, six
seats, 22,334 voters, 63 per cent turnout, and 586,098 voters by 1959. Ends
exactly where sentence 5 begins in the main config's own timing. Vertical
1080x1920.
"""

WIDTH, HEIGHT = 1080, 1920

IMAGES = {
    "VT": "https://upload.wikimedia.org/wikipedia/commons/thumb/a/a2/KITLV_A887_-_Victoria_Theatre_en_Memorial_Hall_te_Singapore%2C_KITLV_107516.tiff/lossy-page1-1280px-KITLV_A887_-_Victoria_Theatre_en_Memorial_Hall_te_Singapore%2C_KITLV_107516.tiff.jpg",
    "ST20": "/assets/images/straits-times-1948-03-20-page-1.jpg",
    "ST21": "/assets/images/straits-times-1948-03-21-page-1.jpg",
}

_VA = {"type": "cover", "zoom": [1.0, 1.05, 1.1], "pan": [(0.35, 0.5), (0.5, 0.5), (0.65, 0.5)], "ease": "ease-in-out"}
_VN = {"type": "cover", "zoom": [1.8, 1.85, 1.9], "pan": [(0.3, 0.0), (0.35, 0.03), (0.4, 0.06)], "ease": "ease-in-out"}
_VS = {"type": "cover", "zoom": [1.7, 1.75, 1.8], "pan": [(0.15, 0.03), (0.2, 0.06), (0.25, 0.09)], "ease": "ease-in-out"}
_VB = {"type": "cover", "zoom": [1.1, 1.05, 1.0], "pan": [(0.7, 0.5), (0.55, 0.5), (0.4, 0.5)], "ease": "ease-in-out"}

SLIDES = [
    {"img": "VT", **_VA},  # s0 title
    {"img": "ST20", **_VN},  # s1-2 first election, six seats
    {"img": "ST21", **_VS},  # s3 63 per cent
    {"img": "VT", **_VB},  # s4 586,098 by 1959
]

SCHEDULE = [(0.0, 0), (8.45, 1), (28.0, 2), (35.025, 3)]
TOTAL_DURATION = 45.375
TIMING_JSON = "audio/singapores-first-election-1948-22000-voters-in-a-city-of-940000.timing.json"

BURN_CAPTIONS = True
CAPTION_FONT_RATIO = 0.032
CAPTION_MAX_WIDTH_FRAC = 0.86
CAPTION_Y_FRAC = 0.80
