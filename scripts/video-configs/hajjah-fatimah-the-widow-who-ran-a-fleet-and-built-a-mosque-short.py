"""Short config for the Hajjah Fatimah post.

The post's opening, sentences 0-7 (0-71.275s, over the 60s line): the
widow from Malacca, the robbery and fire on Java Road, the mosque built on
the site in 1845-46, the plaque's "Malacca Malay lady", and her first
marriage. Every slide is letterboxed: the plan and the minaret are portrait,
and the prints are too wide to crop to a vertical frame.
"""

WIDTH, HEIGHT = 1080, 1920

IMAGES = {
    "HERO": "https://upload.wikimedia.org/wikipedia/commons/thumb/e/e6/Masjid_Hajjah_Fatimah%2C_October_2025.jpg/1280px-Masjid_Hajjah_Fatimah%2C_October_2025.jpg",
    "HARB": "https://upload.wikimedia.org/wikipedia/commons/thumb/a/a1/Atlas_pittoresque_pl_134.jpg/1280px-Atlas_pittoresque_pl_134.jpg",
    "PLAN": "https://upload.wikimedia.org/wikipedia/commons/thumb/4/44/Plan_of_the_British_settlement_of_Singapore_published_1828.jpg/1280px-Plan_of_the_British_settlement_of_Singapore_published_1828.jpg",
    "MIN10": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/de/Minaret_of_Masjid_Hajjah_Fatimah%2C_Singapore_-_20101016-02.JPG/1280px-Minaret_of_Masjid_Hajjah_Fatimah%2C_Singapore_-_20101016-02.JPG",
    "EXT": "https://upload.wikimedia.org/wikipedia/commons/thumb/c/c8/Masjid_Hajjah_Fatimah%2C_full_exterior_view.jpg/1280px-Masjid_Hajjah_Fatimah%2C_full_exterior_view.jpg",
    "PLAQUE": "https://upload.wikimedia.org/wikipedia/commons/thumb/a/ac/Preservation_of_Monuments_Board_plaque%2C_Masjid_Hajjah_Fatimah%2C_Singapore_-_20101016-01.JPG/1280px-Preservation_of_Monuments_Board_plaque%2C_Masjid_Hajjah_Fatimah%2C_Singapore_-_20101016-01.JPG",
    "JUNK1841": "https://upload.wikimedia.org/wikipedia/commons/thumb/b/bc/Junks_of_Siam_at_Anchor_in_Singapore_1841_Francois-Edmond_Paris.png/1280px-Junks_of_Siam_at_Anchor_in_Singapore_1841_Francois-Edmond_Paris.png",
    "DEC05": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/d0/Hajjah_Fatimah_Mosque%2C_Dec_05.JPG/1280px-Hajjah_Fatimah_Mosque%2C_Dec_05.JPG",  # thumbnail only
}

# The main video's thumbnail grid, re-panned for tall cells.
THUMBNAIL = [
    {"img": "PLAN", "pan": (0.5, 0.8)},
    {"img": "HARB", "pan": (0.6, 0.5)},
    {"img": "DEC05", "pan": (0.2, 0.5)},
    {"img": "HERO", "pan": (0.5, 0.5)},
]

_E = "ease-in-out"
_LB = {"type": "letterbox", "zoom": [1.0, 1.03, 1.06], "pan": [(0.5, 0.5)] * 3, "ease": _E}

SLIDES = [
    {"img": "HERO", **_LB},       # s0
    {"img": "HARB", **_LB},       # s1
    {"img": "PLAN", **_LB},       # s2
    {"img": "MIN10", **_LB},      # s3
    {"img": "EXT", **_LB},        # s4
    {"img": "PLAQUE", **_LB},     # s5
    {"img": "JUNK1841", **_LB},   # s7
]
SCHEDULE = [(0.0, 0), (4.5, 1), (16.475, 2), (24.2, 3), (34.45, 4), (42.625, 5), (53.725, 6)]
TOTAL_DURATION = 71.275
TIMING_JSON = "audio/hajjah-fatimah-the-widow-who-ran-a-fleet-and-built-a-mosque.timing.json"

BURN_CAPTIONS = True
CAPTION_FONT_RATIO = 0.032
CAPTION_MAX_WIDTH_FRAC = 0.86
CAPTION_Y_FRAC = 0.70

# The avatar presenter, cartoon with motion: corner bubble for the first and last 30 s.
AVATAR = {"ranges": [(0, 30), (-30, None)], "motion": True}
