"""Short config for the Syed Mohamed Alsagoff post.

The post's opening, sentences 0-6 (0-63.925s, over the 60s line): the
estate notes printed in 1878, his estates on Kukup and the Sultan of Johor's
grant, his birth in 1836 into a Hadhrami family, and his grandfather. Every
sentence names him or his family, so every slide shows a picture with no
people. Every slide is letterboxed.
"""

WIDTH, HEIGHT = 1080, 1920

IMAGES = {
    "KUKUP05": "https://upload.wikimedia.org/wikipedia/commons/thumb/2/29/Pulau_Kukup.JPG/1280px-Pulau_Kukup.JPG",
    "KUKUP25": "https://upload.wikimedia.org/wikipedia/commons/thumb/6/6c/Kukup_%28250511-0910%29.jpg/1280px-Kukup_%28250511-0910%29.jpg",
    "MAP": "/assets/images/alsagoff-map.png",
    "DGRAVE": "https://upload.wikimedia.org/wikipedia/commons/thumb/3/34/Hajjah_Fatimah_Mosque%2C_double_grave.jpg/1280px-Hajjah_Fatimah_Mosque%2C_double_grave.jpg",
    "BURIAL": "https://upload.wikimedia.org/wikipedia/commons/thumb/f/fb/Alsagoff_burial_ground%2C_panorama.jpg/1280px-Alsagoff_burial_ground%2C_panorama.jpg",
    "HADH1880": "https://upload.wikimedia.org/wikipedia/commons/1/12/Hadhrami_Arab_neighborhood%2C_Surabaya_1880.jpg",  # thumbnail only
    "RAF1": "https://upload.wikimedia.org/wikipedia/commons/thumb/3/30/The_Raffles_Hotel%2C_Singapore%2C_KITLV_1404942.tiff/lossy-page1-1280px-The_Raffles_Hotel%2C_Singapore%2C_KITLV_1404942.tiff.jpg",  # thumbnail only
    "SCH23": "https://upload.wikimedia.org/wikipedia/commons/thumb/1/11/Alsagoff_Arabic_School%2C_Singapore_%282023-06%29_img_01.jpg/1280px-Alsagoff_Arabic_School%2C_Singapore_%282023-06%29_img_01.jpg",  # thumbnail only
}

# Every image is captioned in the post or its gallery.
CREDITS = {}

# The main video's thumbnail grid, re-panned for tall cells.
THUMBNAIL = [
    {"img": "HADH1880", "pan": (0.5, 0.5)},
    {"img": "RAF1", "pan": (0.5, 0.5)},
    {"img": "SCH23", "pan": (0.5, 0.5)},
    {"img": "KUKUP25", "pan": (0.5, 0.5)},
]

_E = "ease-in-out"
_LB = {"type": "letterbox", "zoom": [1.0, 1.03, 1.06], "pan": [(0.5, 0.5)] * 3, "ease": _E}

SLIDES = [
    {"img": "KUKUP05", **_LB},    # s0
    {"img": "KUKUP25", **_LB},    # s1
    {"img": "MAP", **_LB},        # s3
    {"img": "DGRAVE", **_LB},     # s5
    {"img": "BURIAL", **_LB},     # s6
]
SCHEDULE = [(0.0, 0), (4.875, 1), (22.475, 2), (39.95, 3), (52.425, 4)]
TOTAL_DURATION = 63.925
TIMING_JSON = "audio/syed-mohamed-alsagoff-and-the-estate-that-printed-its-own-money.timing.json"

BURN_CAPTIONS = True
CAPTION_FONT_RATIO = 0.032
CAPTION_MAX_WIDTH_FRAC = 0.86
CAPTION_Y_FRAC = 0.70

# The avatar presenter, cartoon with motion: corner bubble for the first and last 30 s.
AVATAR = {"ranges": [(0, 30), (-30, None)], "motion": True}
