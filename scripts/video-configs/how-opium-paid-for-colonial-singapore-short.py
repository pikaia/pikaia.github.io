"""Short config for the opium-farming post.

Excerpt: the opening hook through the first strong beat (sentences 0-3,
0.0-45.88s) - "For most of the nineteenth century... a free port that
famously charged no import duties, and the arrangement ran for well over
a century before Singapore turned around and made the very trade that had
funded it a crime." A clean self-contained hook->payoff, ending exactly
where sentence 4 begins in the main config's own timing.

Same PROTECTORATE image and pan/zoom values as the main config's opening
slides - cover-crop normalizes to the vertical frame unchanged.
"""

WIDTH, HEIGHT = 1080, 1920

_U = "https://upload.wikimedia.org/wikipedia/commons"

IMAGES = {
    "PROTECTORATE": f"{_U}/thumb/5/53/Chinese_Protectorate%2C_Singapore%2C_KITLV_1404946.tiff/lossy-page1-1920px-Chinese_Protectorate%2C_Singapore%2C_KITLV_1404946.tiff.jpg",
}

_PROTA = {"type": "cover", "zoom": [1.0, 1.05, 1.1], "pan": [(0.5, 0.4)] * 3, "ease": "ease-in-out"}
_PROTB = {"type": "cover", "zoom": [1.15, 1.08, 1.0], "pan": [(0.35, 0.45)] * 3, "ease": "ease-out"}
_PROTC = {"type": "cover", "zoom": [1.0, 1.06, 1.12], "pan": [(0.65, 0.45)] * 3, "ease": "ease-in-out"}

SLIDES = [
    {"img": "PROTECTORATE", **_PROTA},  # s0-1 title + govt paid bills with opium
    {"img": "PROTECTORATE", **_PROTB},  # s2   not smuggling, openly auctioned...40-60%
    {"img": "PROTECTORATE", **_PROTC},  # s3   single largest source...a crime
]

SCHEDULE = [(0.0, 0), (10.68, 1), (29.5, 2)]
TOTAL_DURATION = 45.88
TIMING_JSON = "audio/how-opium-paid-for-colonial-singapore.timing.json"

BURN_CAPTIONS = True
CAPTION_FONT_RATIO = 0.032
CAPTION_MAX_WIDTH_FRAC = 0.86
CAPTION_Y_FRAC = 0.80
