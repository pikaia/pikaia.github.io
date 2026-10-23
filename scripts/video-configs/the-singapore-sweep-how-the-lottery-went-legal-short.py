"""Short config for the Singapore Sweep post.

The post's opening, sentences 0-6 (0-62.875s, over the 60s TikTok line):
the monthly draw, the word "sweepstakes" from the racecourse, Singapore
Pools in 1968, the three games, and racing at Farrer Park from 1842.
Every slide is letterboxed: the photos and sketches are too wide to crop
to a vertical frame.
"""

WIDTH, HEIGHT = 1080, 1920

IMAGES = {
    "HERO": "https://upload.wikimedia.org/wikipedia/commons/thumb/8/84/Totoghimmoh.jpg/1280px-Totoghimmoh.jpg",
    "HQ21": "https://upload.wikimedia.org/wikipedia/commons/thumb/3/3d/Singapore_Pools_Head_Office_20210503_125649.jpg/1280px-Singapore_Pools_Head_Office_20210503_125649.jpg",
    "HORSE1881": "https://upload.wikimedia.org/wikipedia/commons/thumb/9/94/Singapore%3B_a_stubborn_horse_at_the_start_of_Singapore_raceco_Wellcome_V0037529.jpg/1280px-Singapore%3B_a_stubborn_horse_at_the_start_of_Singapore_raceco_Wellcome_V0037529.jpg",
    "MIDDLE": "https://upload.wikimedia.org/wikipedia/commons/thumb/6/6f/Sede_de_Singapore_Pools%2C_Middle_Road%2C_Singapur%2C_2023-08-16%2C_DD_02.jpg/1280px-Sede_de_Singapore_Pools%2C_Middle_Road%2C_Singapur%2C_2023-08-16%2C_DD_02.jpg",
    "PRINSEP": "https://upload.wikimedia.org/wikipedia/commons/thumb/0/0b/Prinsep_Street_Singapore_Pools_01-12-2024.jpg/1280px-Prinsep_Street_Singapore_Pools_01-12-2024.jpg",
    "POLICE1881": "https://upload.wikimedia.org/wikipedia/commons/thumb/9/91/Singapore%3B_a_police_officer_clearing_two_race-goers_from_the_Wellcome_V0037530.jpg/1280px-Singapore%3B_a_police_officer_clearing_two_race-goers_from_the_Wellcome_V0037530.jpg",
    "HAPPY": "https://upload.wikimedia.org/wikipedia/commons/d/d9/Happy_World_Amusement_Park.jpg",  # thumbnail only
    "NATTHEATRE": "https://upload.wikimedia.org/wikipedia/commons/thumb/4/49/Singapore-National_Theater-1973-74-WUS08168.jpg/1280px-Singapore-National_Theater-1973-74-WUS08168.jpg",  # thumbnail only
    "LAVENDER": "https://upload.wikimedia.org/wikipedia/commons/thumb/e/ec/Lavender_Singapore_Pools_12-05-2024.jpg/1280px-Lavender_Singapore_Pools_12-05-2024.jpg",  # thumbnail only
}

# Credits for images not captioned in the post or its gallery.
CREDITS = {
    "PRINSEP": "LN9267, CC BY-SA 4.0, via Wikimedia Commons",
}

# The main video's thumbnail grid, re-panned for tall cells.
THUMBNAIL = [
    {"img": "HORSE1881", "pan": (0.35, 0.5)},
    {"img": "HAPPY", "pan": (0.5, 0.5)},
    {"img": "NATTHEATRE", "pan": (0.48, 0.45)},
    {"img": "LAVENDER", "pan": (0.3, 0.5)},
]

_E = "ease-in-out"
_LB = {"type": "letterbox", "zoom": [1.0, 1.03, 1.06], "pan": [(0.5, 0.5)] * 3, "ease": _E}

SLIDES = [
    {"img": "HERO", **_LB},           # s0
    {"img": "HQ21", **_LB},           # s1
    {"img": "HORSE1881", **_LB},      # s2
    {"img": "MIDDLE", **_LB},         # s3
    {"img": "PRINSEP", **_LB},        # s4
    {"img": "POLICE1881", **_LB},     # s5-6
]
SCHEDULE = [(0.0, 0), (3.7, 1), (16.4, 2), (28.1, 3), (41.95, 4), (50.075, 5)]
TOTAL_DURATION = 62.875
TIMING_JSON = "audio/the-singapore-sweep-how-the-lottery-went-legal.timing.json"

BURN_CAPTIONS = True
CAPTION_FONT_RATIO = 0.032
CAPTION_MAX_WIDTH_FRAC = 0.86
CAPTION_Y_FRAC = 0.70

# The avatar presenter, cartoon with motion: corner bubble for the first and last 30 s.
AVATAR = {"ranges": [(0, 30), (-30, None)], "motion": True}
