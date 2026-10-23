"""Short config for the Turf Club post.

The post's opening, sentences 0-6 (0-69.3s, over the 60s TikTok line):
the last meeting at Kranji, the 100th Gold Cup, the three racecourses on
the map, and the club's founding in 1842 with the Singapore Free Press
notice of its new course. Every slide is letterboxed: the photos, the map
and the newspaper page are too wide or too tall to crop to a vertical
frame.
"""

WIDTH, HEIGHT = 1080, 1920

IMAGES = {
    "HERO": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/de/Kranji_Racecourse_05-12-2024.jpg/1280px-Kranji_Racecourse_05-12-2024.jpg",
    "SIGN15": "https://upload.wikimedia.org/wikipedia/commons/thumb/0/0f/Singapore_Turf_Club%2C_2015.jpg/1280px-Singapore_Turf_Club%2C_2015.jpg",
    "TURF15": "https://upload.wikimedia.org/wikipedia/commons/thumb/4/4e/Singapore_Turf_Club_building%2C_2015.jpg/1280px-Singapore_Turf_Club_building%2C_2015.jpg",
    "MAP": "/assets/images/turf-club-racecourses-map.png",
    "SFP1842": "/assets/images/singapore-free-press-1842-12-08-page-3.jpg",
    "SKETCH3": "https://upload.wikimedia.org/wikipedia/commons/thumb/f/f0/Singapore%3B_two_race-going_celebrities_talk_as_a_race_horse_i_Wellcome_V0037531.jpg/1280px-Singapore%3B_two_race-going_celebrities_talk_as_a_race_horse_i_Wellcome_V0037531.jpg",  # thumbnail only
    "KITLV1910": "https://upload.wikimedia.org/wikipedia/commons/thumb/1/1e/KITLV_-_79903_-_Kleingrothe%2C_C.J._-_Medan_-_Tanks_and_the_racecourse_at_Singapore_-_circa_1910.tif/lossy-page1-1280px-KITLV_-_79903_-_Kleingrothe%2C_C.J._-_Medan_-_Tanks_and_the_racecourse_at_Singapore_-_circa_1910.tif.jpg",  # thumbnail only
    "TURFCITY3": "https://upload.wikimedia.org/wikipedia/commons/thumb/1/16/Turf_City_3%2C_Dec_06.JPG/1280px-Turf_City_3%2C_Dec_06.JPG",  # thumbnail only
}

# The main video's thumbnail grid, re-panned for tall cells.
THUMBNAIL = [
    {"img": "SKETCH3", "pan": (0.15, 0.5)},
    {"img": "KITLV1910", "pan": (0.5, 0.5)},
    {"img": "TURFCITY3", "pan": (0.4, 0.5)},
    {"img": "HERO", "pan": (0.5, 0.5)},
]

_E = "ease-in-out"
_LB = {"type": "letterbox", "zoom": [1.0, 1.03, 1.06], "pan": [(0.5, 0.5)] * 3, "ease": _E}

SLIDES = [
    {"img": "HERO", **_LB},           # s0
    {"img": "SIGN15", **_LB},         # s1
    {"img": "TURF15", **_LB},         # s2
    {"img": "MAP", **_LB},            # s3-4
    {"img": "SFP1842", **_LB},        # s5-6
]
SCHEDULE = [(0.0, 0), (5.9, 1), (15.425, 2), (26.125, 3), (46.325, 4)]
TOTAL_DURATION = 69.3
TIMING_JSON = "audio/the-last-race-at-kranji-182-years-of-the-singapore-turf-club.timing.json"

BURN_CAPTIONS = True
CAPTION_FONT_RATIO = 0.032
CAPTION_MAX_WIDTH_FRAC = 0.86
CAPTION_Y_FRAC = 0.70

# The avatar presenter, cartoon with motion: corner bubble for the first and last 30 s.
AVATAR = {"ranges": [(0, 30), (-30, None)], "motion": True}
