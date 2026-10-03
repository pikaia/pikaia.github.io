"""Short config for the shoreline post.

Excerpt: the opening hook (sentences 0-4, 0.0-38.1 s): Thian Hock Keng on the
beach, sailors thanking Mazu, and the land made in front of it. Ends exactly
where sentence 5 begins in the main config's own timing. Vertical 1080x1920.
The stage maps are cover-cropped here onto the shaded downtown strip.
"""

WIDTH, HEIGHT = 1080, 1920

CREDITS = {
    "MAP0": "Map by Lesser Known Singapore; map data (c) OpenStreetMap contributors",
    "MAP5": "Map by Lesser Known Singapore; map data (c) OpenStreetMap contributors",
}

IMAGES = {
    "CQ1890": "https://upload.wikimedia.org/wikipedia/commons/thumb/5/50/KITLV_-_103744_-_Collyer_Quay_in_Singapore_-_circa_1890.tif/lossy-page1-1920px-KITLV_-_103744_-_Collyer_Quay_in_Singapore_-_circa_1890.tif.jpg",
    "THK": "https://upload.wikimedia.org/wikipedia/commons/thumb/8/81/KITLV_-_103742_-_Lambert_%26_Co._-_Thian_Hock_Keng_Temple_in_Singapore_-_circa_1890.tif/lossy-page1-1920px-KITLV_-_103742_-_Lambert_%26_Co._-_Thian_Hock_Keng_Temple_in_Singapore_-_circa_1890.tif.jpg",
    "MAP0": "/assets/images/reclamation-map-0.png",
    "MAP5": "/assets/images/reclamation-map-5.png",
}

_VC = {"type": "cover", "zoom": [1.0, 1.05, 1.1], "pan": [(0.3, 0.5), (0.45, 0.5), (0.6, 0.5)], "ease": "ease-in-out"}
_VT = {"type": "cover", "zoom": [1.0, 1.05, 1.1], "pan": [(0.35, 0.5), (0.45, 0.5), (0.55, 0.5)], "ease": "ease-in-out"}
_VZ = {"type": "cover", "zoom": [1.3, 1.35, 1.4], "pan": [(0.45, 0.45), (0.45, 0.45), (0.45, 0.45)], "ease": "ease-in-out"}
_VM = {"type": "cover", "zoom": [1.0, 1.03, 1.06], "pan": [(0.44, 0.5), (0.46, 0.5), (0.48, 0.5)], "ease": "ease-in-out"}

SLIDES = [
    {"img": "CQ1890", **_VC},  # s0 title
    {"img": "THK", **_VT},  # s1 the temple on the beach
    {"img": "THK", **_VZ},  # s2 sailors, Mazu
    {"img": "MAP0", **_VM},  # s3 four streets from the sea
    {"img": "MAP5", **_VM},  # s4 the land made in front of it
]

SCHEDULE = [(0.0, 0), (5.8, 1), (15.1, 2), (23.25, 3), (30.1, 4)]
TOTAL_DURATION = 38.1
TIMING_JSON = "audio/when-telok-ayer-street-was-the-beach-singapores-first-land-reclamations.timing.json"

BURN_CAPTIONS = True
CAPTION_FONT_RATIO = 0.032
CAPTION_MAX_WIDTH_FRAC = 0.86
CAPTION_Y_FRAC = 0.70

# Made before the over-one-minute rule (2026-10-03); see validate_short_config().
SHORT_UNDER_A_MINUTE_OK = True
