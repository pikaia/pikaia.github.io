"""Short config for the 1914 bank-run post.

Excerpt: the opening hook (sentences 0-3, 0.0-36.52 s): depositors rush the
Chinese Commercial Bank on 4 August 1914, $300,000 out by the next evening,
and eight weeks shut. Ends exactly where sentence 4 begins in the main
config's own timing. Vertical 1080x1920.
"""

WIDTH, HEIGHT = 1080, 1920

IMAGES = {
    "CHQ": "https://upload.wikimedia.org/wikipedia/commons/c/c4/Souvenir_of_Singapore%2C_1914_-_Plate_11_-_Chinese_Quarters.jpg",
    "MT": "/assets/images/malaya-tribune-1914-08-27-page-12.jpg",
    "KLING1907": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/d0/Kling_Street%2C_Singapore_%28NYPL_Hades-2359713-4044478%29.jpg/1280px-Kling_Street%2C_Singapore_%28NYPL_Hades-2359713-4044478%29.jpg",
}

_VC = {"type": "cover", "zoom": [1.0, 1.05, 1.1], "pan": [(0.35, 0.5), (0.45, 0.5), (0.55, 0.5)], "ease": "ease-in-out"}
_VZ = {"type": "cover", "zoom": [1.2, 1.25, 1.3], "pan": [(0.55, 0.5), (0.6, 0.5), (0.65, 0.5)], "ease": "ease-in-out"}
_VN = {"type": "cover", "zoom": [1.0, 1.04, 1.08], "pan": [(0.43, 0.0), (0.43, 0.02), (0.43, 0.04)], "ease": "ease-in-out"}
_VK = {"type": "cover", "zoom": [1.0, 1.05, 1.1], "pan": [(0.55, 0.5), (0.65, 0.5), (0.75, 0.5)], "ease": "ease-in-out"}

SLIDES = [
    {"img": "CHQ", **_VC},  # s0 title
    {"img": "CHQ", **_VZ},  # s1 depositors rush the bank
    {"img": "MT", **_VN},  # s2 $300,000, doors closed
    {"img": "KLING1907", **_VK},  # s3 shut eight weeks
]

SCHEDULE = [(0.0, 0), (5.875, 1), (18.85, 2), (26.05, 3)]
TOTAL_DURATION = 36.525
TIMING_JSON = "audio/the-run-on-the-banks-1914-when-war-in-europe-emptied-a-singapore-bank.timing.json"

BURN_CAPTIONS = True
CAPTION_FONT_RATIO = 0.032
CAPTION_MAX_WIDTH_FRAC = 0.86
CAPTION_Y_FRAC = 0.80
