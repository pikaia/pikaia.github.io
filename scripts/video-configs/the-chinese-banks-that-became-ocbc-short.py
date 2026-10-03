"""Short config for the Chinese banks post.

Excerpt: the opening hook (sentences 0-3, 0.0-35.73 s): the crowd outside the
Kwong Yik Bank in November 1913, ten years of Singapore's first Chinese bank,
and the dialect banks that followed. Ends exactly where sentence 4 begins in
the main config's own timing. Vertical 1080x1920.
"""

WIDTH, HEIGHT = 1080, 1920

IMAGES = {
    "KLING1907": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/d0/Kling_Street%2C_Singapore_%28NYPL_Hades-2359713-4044478%29.jpg/1920px-Kling_Street%2C_Singapore_%28NYPL_Hades-2359713-4044478%29.jpg",
    "SFP13": "/assets/images/singapore-free-press-1913-11-21-page-7.jpg",
    "PENANG": "https://upload.wikimedia.org/wikipedia/commons/thumb/2/28/OCBC_Art_Deco_Beach_St.jpg/1920px-OCBC_Art_Deco_Beach_St.jpg",
}

_VK = {"type": "cover", "zoom": [1.0, 1.05, 1.1], "pan": [(0.55, 0.5), (0.65, 0.5), (0.75, 0.5)], "ease": "ease-in-out"}
_VN = {"type": "cover", "zoom": [1.3, 1.35, 1.4], "pan": [(0.4, 0.0), (0.42, 0.04), (0.44, 0.08)], "ease": "ease-in-out"}
_VP = {"type": "cover", "zoom": [1.0, 1.03, 1.06], "pan": [(0.5, 0.35), (0.5, 0.4), (0.5, 0.45)], "ease": "ease-in-out"}

SLIDES = [
    {"img": "KLING1907", **_VK},  # s0 title
    {"img": "KLING1907", **_VK},  # s1 crowd outside Kwong Yik
    {"img": "SFP13", **_VN},  # s2 lasted ten years
    {"img": "PENANG", **_VP},  # s3 the banks that followed, OCBC
]

SCHEDULE = [(0.0, 0), (3.6, 1), (16.725, 2), (21.125, 3)]
TOTAL_DURATION = 35.725
TIMING_JSON = "audio/the-chinese-banks-that-became-ocbc.timing.json"

BURN_CAPTIONS = True
CAPTION_FONT_RATIO = 0.032
CAPTION_MAX_WIDTH_FRAC = 0.86
CAPTION_Y_FRAC = 0.70

# Made before the over-one-minute rule (2026-10-03); see validate_short_config().
SHORT_UNDER_A_MINUTE_OK = True
