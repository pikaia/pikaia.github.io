"""Short config for the Post Office riot post.

The post's opening, sentences 0-7 (0-69.5s, over the 60s line): the
sub-post office at 81 Market Street, the riot and its three dead, and how
labourers sent money home by junk and through the Teochew merchants. No
sentence names a person. Every slide is letterboxed.
"""

WIDTH, HEIGHT = 1080, 1920

IMAGES = {
    "GPO": "https://upload.wikimedia.org/wikipedia/commons/thumb/f/f6/KITLV_-_89905_-_Post_office%2C_Exchange_building_and_square_in_Singapore_-_before_1880.tif/lossy-page1-1280px-KITLV_-_89905_-_Post_office%2C_Exchange_building_and_square_in_Singapore_-_before_1880.tif.jpg",
    "MARKET": "https://upload.wikimedia.org/wikipedia/commons/a/a6/Corner_of_Market_St_and_Robinson_Rd_Singapore%2C_1925-1930.jpg",
    "ST2": "/assets/images/straits-times-overland-journal-1876-12-27-page-2.jpg",
    "SOUP": "https://upload.wikimedia.org/wikipedia/commons/thumb/6/62/John_Edmund_Taylor%2C_A_Chinese_Soup_Seller_Trading_in_Singapore_%28c_1880%2C_Wellcome_V0037508%29.jpg/1280px-John_Edmund_Taylor%2C_A_Chinese_Soup_Seller_Trading_in_Singapore_%28c_1880%2C_Wellcome_V0037508%29.jpg",
    "SWJUNK": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/d0/Swatow_MET_DP165628.jpg/1280px-Swatow_MET_DP165628.jpg",
    "PIER": "https://upload.wikimedia.org/wikipedia/commons/thumb/5/5e/KITLV_-_103750_-_Johnston%27s_pier_at_Singapore_-_circa_1890.tif/lossy-page1-1280px-KITLV_-_103750_-_Johnston%27s_pier_at_Singapore_-_circa_1890.tif.jpg",  # thumbnail only
    "PAGODA": "https://upload.wikimedia.org/wikipedia/commons/thumb/4/4f/Singapore_%28SG%29%2C_China_Town%2C_Pagoda_Street_--_2019_--_4507.jpg/1280px-Singapore_%28SG%29%2C_China_Town%2C_Pagoda_Street_--_2019_--_4507.jpg",  # thumbnail only
}

# Every image is captioned in the post or its gallery.
CREDITS = {}

# The main video's thumbnail grid, re-panned for tall cells.
THUMBNAIL = [
    {"img": "GPO", "pan": (0.5, 0.5)},
    {"img": "PIER", "pan": (0.5, 0.6)},
    {"img": "MARKET", "pan": (0.5, 0.5)},
    {"img": "PAGODA", "pan": (0.5, 0.5)},
]

_E = "ease-in-out"
_LB = {"type": "letterbox", "zoom": [1.0, 1.03, 1.06], "pan": [(0.5, 0.5)] * 3, "ease": _E}

SLIDES = [
    {"img": "GPO", **_LB},        # s0
    {"img": "MARKET", **_LB},     # s1
    {"img": "ST2", **_LB},        # s3
    {"img": "SOUP", **_LB},       # s4
    {"img": "SWJUNK", **_LB},     # s5
]
SCHEDULE = [(0.0, 0), (3.875, 1), (26.475, 2), (36.175, 3), (43.8, 4)]
TOTAL_DURATION = 69.5
TIMING_JSON = "audio/the-post-office-riot-of-1876.timing.json"

BURN_CAPTIONS = True
CAPTION_FONT_RATIO = 0.032
CAPTION_MAX_WIDTH_FRAC = 0.86
CAPTION_Y_FRAC = 0.70

# The avatar presenter, cartoon with motion: corner bubble for the first and last 30 s.
AVATAR = {"ranges": [(0, 30), (-30, None)], "motion": True}
