"""Short config for the Gurkha Contingent post.

Excerpt: the opening hook (sentences 0-3, 0.0-45.9s): the 1949 recruitment in
Nepal, the neutral riot squad, and its first test in 1950. Ends exactly where
sentence 4 begins in the main config's own timing. Vertical 1080x1920.
"""

WIDTH, HEIGHT = 1080, 1920

IMAGES = {
    "PARADE": "https://upload.wikimedia.org/wikipedia/commons/thumb/0/0d/Singapore_Gurkha_01.jpg/1920px-Singapore_Gurkha_01.jpg",
    "ST1949": "/assets/images/straits-times-1949-02-16-page-3.jpg",
    "IOC1": "https://upload.wikimedia.org/wikipedia/commons/4/4a/Gurkha_IOC_1.jpg",
    "ST1213": "/assets/images/straits-times-1950-12-13-page-1.jpg",
}

_VA = {"type": "cover", "zoom": [1.0, 1.05, 1.1], "pan": [(0.3, 0.5), (0.45, 0.5), (0.6, 0.5)], "ease": "ease-in-out"}
_VN = {"type": "cover", "zoom": [2.2, 2.25, 2.3], "pan": [(0.5, 0.2), (0.5, 0.24), (0.5, 0.28)], "ease": "ease-in-out"}
_VI = {"type": "cover", "zoom": [1.0, 1.05, 1.1], "pan": [(0.5, 0.35), (0.5, 0.42), (0.5, 0.5)], "ease": "ease-in-out"}
_VT = {"type": "cover", "zoom": [1.6, 1.65, 1.7], "pan": [(0.3, 0.05), (0.3, 0.1), (0.3, 0.15)], "ease": "ease-in-out"}

SLIDES = [
    {"img": "PARADE", **_VA},  # s0 title
    {"img": "ST1949", **_VN},  # s1 February 1949, 148 Gurkhas
    {"img": "IOC1", **_VI},  # s2 neutral riot squad
    {"img": "ST1213", **_VT},  # s3 tested in the riots
]

SCHEDULE = [(0.0, 0), (6.875, 1), (18.475, 2), (34.425, 3)]
TOTAL_DURATION = 45.9
TIMING_JSON = "audio/the-gurkha-contingent-singapores-neutral-force-1949-1965.timing.json"

BURN_CAPTIONS = True
CAPTION_FONT_RATIO = 0.032
CAPTION_MAX_WIDTH_FRAC = 0.86
CAPTION_Y_FRAC = 0.80
