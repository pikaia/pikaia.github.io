"""Short config for the Robinsons post.

The post's opening, sentences 0-5 (0-62.375s, over the 60s TikTok line):
the 1972 fire, the store's 114 years, its reopening on Orchard Road, and
its founding on Commercial Square in 1858 with the Singapore Free Press
page carrying its advertisement. Every slide is letterboxed: the photos
and the newspaper page are too wide or too tall to crop to a vertical
frame.
"""

WIDTH, HEIGHT = 1080, 1920

IMAGES = {
    "HERO": "https://upload.wikimedia.org/wikipedia/commons/thumb/2/28/522a_Singapore_1971_%2851316419105%29.jpg/1280px-522a_Singapore_1971_%2851316419105%29.jpg",
    "R71B": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/dc/71-610_Raffles_Place_Singapore_1971_%2851252222815%29.jpg/1280px-71-610_Raffles_Place_Singapore_1971_%2851252222815%29.jpg",
    "KITLV1910": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/da/KITLV_-_79891_-_Kleingrothe%2C_C.J._-_Medan_-_Raffles_Place%2C_Singapore_-_circa_1910.tif/lossy-page1-1280px-KITLV_-_79891_-_Kleingrothe%2C_C.J._-_Medan_-_Raffles_Place%2C_Singapore_-_circa_1910.tif.jpg",
    "SPEC": "https://upload.wikimedia.org/wikipedia/commons/thumb/1/15/SpecialistsShoppingCentre.JPG/1280px-SpecialistsShoppingCentre.JPG",
    "SFP1858": "/assets/images/singapore-free-press-1858-03-25-page-2.jpg",
    "JL1870": "https://upload.wikimedia.org/wikipedia/commons/thumb/8/84/KITLV_-_155824_-_Shop_John_Little_%26_Co.%2C_Singapore_-_circa_1870.tif/lossy-page1-1280px-KITLV_-_155824_-_Shop_John_Little_%26_Co.%2C_Singapore_-_circa_1870.tif.jpg",  # thumbnail only
    "ORP25": "https://upload.wikimedia.org/wikipedia/commons/thumb/f/f6/One_Raffles_Place_20250903_%281%29.jpg/1280px-One_Raffles_Place_20250903_%281%29.jpg",  # thumbnail only
}

# Credits for images not captioned in the post or its gallery.
CREDITS = {
    "R71B": "Wilford Peloquin, CC BY 2.0, via Wikimedia Commons",
}

# The main video's thumbnail grid, re-panned for tall cells.
THUMBNAIL = [
    {"img": "JL1870", "pan": (0.3, 0.5)},
    {"img": "KITLV1910", "pan": (0.35, 0.5)},
    {"img": "HERO", "pan": (0.85, 0.5)},
    {"img": "ORP25", "pan": (0.5, 0.5)},
]

_E = "ease-in-out"
_LB = {"type": "letterbox", "zoom": [1.0, 1.03, 1.06], "pan": [(0.5, 0.5)] * 3, "ease": _E}

SLIDES = [
    {"img": "HERO", **_LB},           # s0
    {"img": "R71B", **_LB},           # s1-2
    {"img": "KITLV1910", **_LB},      # s3
    {"img": "SPEC", **_LB},           # s4
    {"img": "SFP1858", **_LB},        # s5
]
SCHEDULE = [(0.0, 0), (8.15, 1), (30.55, 2), (35.05, 3), (46.975, 4)]
TOTAL_DURATION = 62.375
TIMING_JSON = "audio/robinsons-and-the-1972-fire-162-years-of-singapores-oldest-department-store.timing.json"

BURN_CAPTIONS = True
CAPTION_FONT_RATIO = 0.032
CAPTION_MAX_WIDTH_FRAC = 0.86
CAPTION_Y_FRAC = 0.70

# The avatar presenter, cartoon with motion: corner bubble for the first and last 30 s.
AVATAR = {"ranges": [(0, 30), (-30, None)], "motion": True}
