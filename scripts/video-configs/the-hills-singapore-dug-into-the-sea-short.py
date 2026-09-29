"""Short config for the vanished-hills post.

Excerpt: the opening hook (sentences 0-3, 0.0-29.65 s): three waterfront hills in
the 1880s, gone within fifty years, and the street names and knoll left behind.
Ends exactly where sentence 4 begins in the main config's own timing. Vertical
1080x1920. The stage maps are cover-cropped onto the three hills.
"""

WIDTH, HEIGHT = 1080, 1920

CREDITS = {
    "DT0": "Map by Lesser Known Singapore; map data (c) OpenStreetMap contributors",
    "DT3": "Map by Lesser Known Singapore; map data (c) OpenStreetMap contributors",
}

IMAGES = {
    "PALMERFOOT": "https://upload.wikimedia.org/wikipedia/commons/thumb/1/13/Strand_en_badgasten_aan_de_voet_van_Mount_Palmer_%28Mount_Parsee%2C_Parsee_Hill%29_bij_Singapore_Foot_of_Mount_Palmer._S.pore_%28titel_op_object%29%2C_RP-F-F01104-Z.jpg/1920px-Strand_en_badgasten_aan_de_voet_van_Mount_Palmer_%28Mount_Parsee%2C_Parsee_Hill%29_bij_Singapore_Foot_of_Mount_Palmer._S.pore_%28titel_op_object%29%2C_RP-F-F01104-Z.jpg",
    "DT0": "/assets/images/hills-downtown-0.png",
    "DT3": "/assets/images/hills-downtown-3.png",
    "KNOLL": "https://upload.wikimedia.org/wikipedia/commons/thumb/1/11/Keramat_Habib_Noh_and_remains_of_former_Mount_Palmer.jpg/1920px-Keramat_Habib_Noh_and_remains_of_former_Mount_Palmer.jpg",
}

_VP = {"type": "cover", "zoom": [1.0, 1.05, 1.1], "pan": [(0.55, 0.5), (0.62, 0.5), (0.7, 0.5)], "ease": "ease-in-out"}
_VM = {"type": "cover", "zoom": [1.0, 1.03, 1.06], "pan": [(0.42, 0.5), (0.43, 0.5), (0.44, 0.5)], "ease": "ease-in-out"}
_VK = {"type": "cover", "zoom": [1.0, 1.05, 1.1], "pan": [(0.25, 0.5), (0.3, 0.5), (0.35, 0.5)], "ease": "ease-in-out"}

SLIDES = [
    {"img": "PALMERFOOT", **_VP},  # s0 title
    {"img": "DT0", **_VM},  # s1 three hills in the 1880s
    {"img": "DT3", **_VM},  # s2 gone within fifty years
    {"img": "KNOLL", **_VK},  # s3 street names and a knoll
]

SCHEDULE = [(0.0, 0), (3.3, 1), (12.325, 2), (23.075, 3)]
TOTAL_DURATION = 29.65
TIMING_JSON = "audio/the-hills-singapore-dug-into-the-sea.timing.json"

BURN_CAPTIONS = True
CAPTION_FONT_RATIO = 0.032
CAPTION_MAX_WIDTH_FRAC = 0.86
CAPTION_Y_FRAC = 0.80
