"""Short config for the Bhai Maharaj Singh post.

Excerpt: the opening hook (sentences 0-3, 0.0-37.25s): the 1850 arrival, who he
was, and the shrine that moved twice. Ends exactly where sentence 4 begins in the
main config's own timing. Vertical 1080x1920.
"""

WIDTH, HEIGHT = 1080, 1920

IMAGES = {
    "PRISON": "https://upload.wikimedia.org/wikipedia/commons/thumb/5/54/Photograph_of_Outram_Prison_%28Pearl%E2%80%99s_Hill_Prison%29_in_the_1850%27s.jpg/1920px-Photograph_of_Outram_Prison_%28Pearl%E2%80%99s_Hill_Prison%29_in_the_1850%27s.jpg",
    "ST50": "/assets/images/straits-times-1850-06-18-page-4.jpg",
    "CELL": "https://upload.wikimedia.org/wikipedia/commons/8/83/Bhai_Maharaj_Singh_and_Companion_%28Khurruck_Singh%29_in_a_Prison_Cell.jpg",
    "SILAT2015": "https://upload.wikimedia.org/wikipedia/commons/thumb/8/88/Silat_Road_Sikh_Temple%2C_Singapore.jpg/1920px-Silat_Road_Sikh_Temple%2C_Singapore.jpg",
}

_VA = {"type": "cover", "zoom": [1.0, 1.05, 1.1], "pan": [(0.3, 0.5), (0.45, 0.5), (0.6, 0.5)], "ease": "ease-in-out"}
_VN = {"type": "cover", "zoom": [2.4, 2.45, 2.5], "pan": [(0.0, 0.86), (0.02, 0.88), (0.04, 0.9)], "ease": "ease-in-out"}
_VC = {"type": "cover", "zoom": [1.0, 1.05, 1.1], "pan": [(0.5, 0.3), (0.5, 0.4), (0.5, 0.5)], "ease": "ease-in-out"}
_VS = {"type": "cover", "zoom": [1.0, 1.05, 1.1], "pan": [(0.35, 0.5), (0.45, 0.5), (0.55, 0.5)], "ease": "ease-in-out"}

SLIDES = [
    {"img": "PRISON", **_VA},  # s0 title
    {"img": "ST50", **_VN},  # s1 June 1850 report
    {"img": "CELL", **_VC},  # s2 Bhai Maharaj Singh
    {"img": "SILAT2015", **_VS},  # s3 the shrine today
]

SCHEDULE = [(0.0, 0), (4.675, 1), (14.35, 2), (25.375, 3)]
TOTAL_DURATION = 37.25
TIMING_JSON = "audio/the-sikh-prisoner-of-outram-road-and-the-shrine-that-moved-twice.timing.json"

BURN_CAPTIONS = True
CAPTION_FONT_RATIO = 0.032
CAPTION_MAX_WIDTH_FRAC = 0.86
CAPTION_Y_FRAC = 0.70

# Made before the over-one-minute rule (2026-10-03); see validate_short_config().
SHORT_UNDER_A_MINUTE_OK = True
