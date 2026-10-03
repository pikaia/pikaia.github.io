"""Short config for the Indian convicts post.

Excerpt: the opening hook (sentences 0-3, 0.0-38.27 s): the Horatio's 80 convicts
in April 1825, 122 more a week later, and 48 years of convict-built Singapore.
Ends exactly where sentence 4 begins in the main config's own timing. Vertical
1080x1920.
"""

WIDTH, HEIGHT = 1080, 1920

IMAGES = {
    "SA1860": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/d4/KITLV_-_29163_-_St._Andrew%27s_Cathedral%2C_belonging_to_the_Anglican_Church%2C_Singapore_-_1860.tif/lossy-page1-1920px-KITLV_-_29163_-_St._Andrew%27s_Cathedral%2C_belonging_to_the_Anglican_Church%2C_Singapore_-_1860.tif.jpg",
    "SAWC": "https://upload.wikimedia.org/wikipedia/commons/thumb/2/2f/Malaysia%3B_view_across_the_harbour_to_Fort_Canning_and_the_ca_Wellcome_V0037489.jpg/1920px-Malaysia%3B_view_across_the_harbour_to_Fort_Canning_and_the_ca_Wellcome_V0037489.jpg",
    "MUSTER": "https://upload.wikimedia.org/wikipedia/commons/thumb/1/16/General_monthly_muster_of_the_convicts%2C_Singapore_Jail_%28McNair_1899%2C_frontispiece%29.jpg/1920px-General_monthly_muster_of_the_convicts%2C_Singapore_Jail_%28McNair_1899%2C_frontispiece%29.jpg",
    "GH1869": "https://upload.wikimedia.org/wikipedia/commons/thumb/5/56/Government_House%2C_Singapore%2C_approaching_completion%2C_1869_%28McNair_1899%2C_Plate_XVIII%29.jpg/1920px-Government_House%2C_Singapore%2C_approaching_completion%2C_1869_%28McNair_1899%2C_Plate_XVIII%29.jpg",
}

_VS = {"type": "cover", "zoom": [1.0, 1.05, 1.1], "pan": [(0.15, 0.5), (0.25, 0.5), (0.35, 0.5)], "ease": "ease-in-out"}
_VW = {"type": "cover", "zoom": [1.0, 1.05, 1.1], "pan": [(0.45, 0.5), (0.55, 0.5), (0.65, 0.5)], "ease": "ease-in-out"}
_VM = {"type": "cover", "zoom": [1.0, 1.05, 1.1], "pan": [(0.55, 0.5), (0.65, 0.5), (0.75, 0.5)], "ease": "ease-in-out"}
_VG = {"type": "cover", "zoom": [1.0, 1.05, 1.1], "pan": [(0.35, 0.5), (0.42, 0.5), (0.5, 0.5)], "ease": "ease-in-out"}

SLIDES = [
    {"img": "SA1860", **_VS},  # s0 title
    {"img": "SAWC", **_VW},  # s1 the Horatio arrives
    {"img": "MUSTER", **_VM},  # s2 122 more from Bengal
    {"img": "GH1869", **_VG},  # s3 48 years, the town they built
]

SCHEDULE = [(0.0, 0), (6.9, 1), (19.425, 2), (24.425, 3)]
TOTAL_DURATION = 38.275
TIMING_JSON = "audio/the-indian-convicts-who-built-colonial-singapore-1825-1873.timing.json"

BURN_CAPTIONS = True
CAPTION_FONT_RATIO = 0.032
CAPTION_MAX_WIDTH_FRAC = 0.86
CAPTION_Y_FRAC = 0.70

# Made before the over-one-minute rule (2026-10-03); see validate_short_config().
SHORT_UNDER_A_MINUTE_OK = True
