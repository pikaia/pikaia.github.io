"""Short config for the Barings 1995 post.

Excerpt: the opening hook (sentences 0-4, 0.0-42.75 s): Nick Leeson walks out of
Barings' Singapore office on 23 February 1995, the hidden account 88888, and
the 233-year-old bank insolvent three days later. Ends exactly where sentence
5 begins in the main config's own timing. Vertical 1080x1920.
"""

WIDTH, HEIGHT = 1080, 1920

IMAGES = {
    "FIRE": "https://upload.wikimedia.org/wikipedia/commons/thumb/e/ef/Fire_of_Great_Hanshin_earthquake_Seen_from_Portisland.jpg/1280px-Fire_of_Great_Hanshin_earthquake_Seen_from_Portisland.jpg",
    "OUB": "https://upload.wikimedia.org/wikipedia/commons/5/53/OUB_Centre_3.JPG",
    "OUBSKY": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/d2/OUB_Centre_Skyward.JPG/1280px-OUB_Centre_Skyward.JPG",
    "BISH": "https://upload.wikimedia.org/wikipedia/commons/thumb/b/be/Junction_of_Bishopsgate_and_Threadneedle_Street%2C_London%2C_July_1993.jpg/1280px-Junction_of_Bishopsgate_and_Threadneedle_Street%2C_London%2C_July_1993.jpg",
}

_VF = {"type": "cover", "zoom": [1.0, 1.05, 1.1], "pan": [(0.35, 0.5), (0.45, 0.5), (0.55, 0.5)], "ease": "ease-in-out"}
_VU = {"type": "cover", "zoom": [1.0, 1.03, 1.06], "pan": [(0.5, 0.7), (0.5, 0.5), (0.5, 0.3)], "ease": "ease-in-out"}
_VD = {"type": "cover", "zoom": [1.06, 1.03, 1.0], "pan": [(0.5, 0.3), (0.5, 0.5), (0.5, 0.7)], "ease": "ease-in-out"}
_VB = {"type": "cover", "zoom": [1.0, 1.05, 1.1], "pan": [(0.6, 0.5), (0.65, 0.5), (0.7, 0.5)], "ease": "ease-in-out"}

SLIDES = [
    {"img": "FIRE", **_VF},  # s0 title
    {"img": "OUB", **_VU},  # s1 Leeson left the office
    {"img": "OUBSKY", **_VD},  # s2 did not come back
    {"img": "OUB", **_VD},  # s3 SIMEX, account 88888
    {"img": "BISH", **_VB},  # s4 three days later, insolvent
]

SCHEDULE = [(0.0, 0), (7.525, 1), (20.425, 2), (22.35, 3), (36.125, 4)]
TOTAL_DURATION = 42.75
TIMING_JSON = "audio/barings-1995-the-singapore-trading-desk-that-broke-a-233-year-old-bank.timing.json"

BURN_CAPTIONS = True
CAPTION_FONT_RATIO = 0.032
CAPTION_MAX_WIDTH_FRAC = 0.86
CAPTION_Y_FRAC = 0.70

# Made before the over-one-minute rule (2026-10-03); see validate_short_config().
SHORT_UNDER_A_MINUTE_OK = True
