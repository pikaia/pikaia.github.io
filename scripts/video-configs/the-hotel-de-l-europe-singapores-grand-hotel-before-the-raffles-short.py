"""Short config for the Hotel de l'Europe post.

The post's opening, sentences 0-6 (0-72.47s): Kipling's advice, the
borrowed line, the great rival across the Padang, and the site as it
stands today, ending on the domed Gallery wing. Six sentences would
have ended at 58.35s — under TikTok's 1-minute floor for Creator
Rewards (Chris's catch, 2026-10-31) — so the Short runs one sentence
longer. Kipling is named in s1; the pool has no portrait of him, so
his sentence shows the old hotel. Every slide is letterboxed.
"""

WIDTH, HEIGHT = 1080, 1920

IMAGES = {
    "HERO": "https://upload.wikimedia.org/wikipedia/commons/5/57/Souvenir_of_Singapore%2C_1914_-_Plate_03_-_Europe_Hotel.jpg",
    "OLD97": "https://upload.wikimedia.org/wikipedia/commons/thumb/2/2a/KITLV_-_29176_-_Lambert_%26_Co.%2C_G.R._-_Singapore_-_Hotel_de_l%27Europe_at_Singapore_-_1897.tif/lossy-page1-1280px-KITLV_-_29176_-_Lambert_%26_Co.%2C_G.R._-_Singapore_-_Hotel_de_l%27Europe_at_Singapore_-_1897.tif.jpg",
    "G1890": "https://upload.wikimedia.org/wikipedia/commons/thumb/7/72/KITLV_-_377459_-_Hotel_d%27Europe_at_Singapore_-_circa_1890.tif/lossy-page1-1280px-KITLV_-_377459_-_Hotel_d%27Europe_at_Singapore_-_circa_1890.tif.jpg",
    "CARR": "https://upload.wikimedia.org/wikipedia/commons/thumb/9/9b/Koetsen_voor_het_Hotel_de_l%27Europe_in_Singapore%2C_SFA002022355.jpg/1280px-Koetsen_voor_het_Hotel_de_l%27Europe_in_Singapore%2C_SFA002022355.jpg",
    "HIGH": "https://upload.wikimedia.org/wikipedia/commons/2/26/Singapore._High_Street_with_Hotel_Europe_LCCN2017657652.jpg",
    "GRND": "https://upload.wikimedia.org/wikipedia/commons/thumb/9/91/KITLV_A1225_-_Hotel_d_%27Europe_te_Singapore%2C_KITLV_142885.tiff/lossy-page1-1280px-KITLV_A1225_-_Hotel_d_%27Europe_te_Singapore%2C_KITLV_142885.tiff.jpg",
    "BIRD": "https://upload.wikimedia.org/wikipedia/commons/9/96/Souvenir_of_Singapore%2C_1914_-_Plate_02_-_Dining_Room.jpg",
    "PAD14": "https://upload.wikimedia.org/wikipedia/commons/4/41/Souvenir_of_Singapore%2C_1914_-_Plate_12_-_Singapore_Cricket_Club%2C_Town_Hall%2C_Supreme_Court_and_Europe_Hotel.jpg",
    "COURT": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/d4/Former_Supreme_Court_Singapore.jpg/1280px-Former_Supreme_Court_Singapore.jpg",
    "GAL": "https://upload.wikimedia.org/wikipedia/commons/thumb/5/5e/National_Gallery_Singapore_1.jpg/1280px-National_Gallery_Singapore_1.jpg"
}

# Every image is captioned in the post or its gallery.
CREDITS = {}

# The main video's thumbnail grid, re-panned for tall cells.
THUMBNAIL = [
    {"img": "G1890", "pan": (0.5, 0.5)},
    {"img": "HIGH", "pan": (0.5, 0.5)},
    {"img": "HERO", "pan": (0.5, 0.5)},
    {"img": "GAL", "pan": (0.5, 0.5)},
]

_E = "ease-in-out"
_LB = {"type": "letterbox", "zoom": [1.0, 1.03, 1.06], "pan": [(0.5, 0.5)] * 3, "ease": _E}

SLIDES = [
    {"img": "HERO", **_LB},   # s0
    {"img": "OLD97", **_LB},   # s1
    {"img": "PAD14", **_LB},   # s2
    {"img": "G1890", **_LB},   # s3
    {"img": "COURT", **_LB},   # s4
    {"img": "GAL", **_LB},   # s6
]
SCHEDULE = [(0, 0), (4.925, 1), (18.95, 2), (28.825, 3), (46.4, 4), (58.35, 5)]
TOTAL_DURATION = 72.47
TIMING_JSON = "audio/the-hotel-de-l-europe-singapores-grand-hotel-before-the-raffles.timing.json"

BURN_CAPTIONS = True
CAPTION_FONT_RATIO = 0.032
CAPTION_MAX_WIDTH_FRAC = 0.86
CAPTION_Y_FRAC = 0.70

# The avatar presenter, cartoon with motion: corner bubble for the first and last 30 s.
AVATAR = {"ranges": [(0, 30), (-30, None)], "motion": True}
