"""Short config for the Sisters' Islands post.

The post's opening, sentences 0-7 (0-66.425s, over the 60s line): the two
islands and their legend, howitzer practice, the 1970s lagoons and the
marine park, the islands' names, and the start of the Minah and Linah story,
which shows the islands with no people. Every slide is letterboxed.
"""

WIDTH, HEIGHT = 1080, 1920

IMAGES = {
    "HERO": "https://upload.wikimedia.org/wikipedia/commons/thumb/8/8e/Sisters_Islands%2C_Singapore_SF0001.jpg/1280px-Sisters_Islands%2C_Singapore_SF0001.jpg",
    "PAINT": "https://upload.wikimedia.org/wikipedia/commons/thumb/5/59/John_Edmund_Taylor%2C_St._John%27s_Island_%26_the_Sisters._From_Tanjong_Katong_Singapore_%281879%2C_Wellcome_V0037483%29.jpg/1280px-John_Edmund_Taylor%2C_St._John%27s_Island_%26_the_Sisters._From_Tanjong_Katong_Singapore_%281879%2C_Wellcome_V0037483%29.jpg",
    "SW": "https://upload.wikimedia.org/wikipedia/commons/thumb/5/56/Big_Sisters%27_Islands%2C_Southwest_Beach_SF0001.jpg/1280px-Big_Sisters%27_Islands%2C_Southwest_Beach_SF0001.jpg",
    "MAP": "/assets/images/sisters-islands-map.png",
    "PAIR2010": "https://upload.wikimedia.org/wikipedia/commons/thumb/4/4c/Sisters_Islands.JPG/1280px-Sisters_Islands.JPG",
    "CLAM1883": "https://upload.wikimedia.org/wikipedia/commons/5/53/FMIB_33102_%22Great_Oyster%22_%28giant_clam%3B_Tridacna_gigas%29_from_Singapore%2C_International_Fisheries_Exhibition%2C_London%2C_1883.jpg",  # thumbnail only
    "BOARD": "https://upload.wikimedia.org/wikipedia/commons/thumb/8/87/View_from_Big_Sisters%27_Islands_SF0001.jpg/1280px-View_from_Big_Sisters%27_Islands_SF0001.jpg",  # thumbnail only
}

# Every image is captioned in the post or its gallery.
CREDITS = {}

# The main video's thumbnail grid, re-panned for tall cells.
THUMBNAIL = [
    {"img": "PAINT", "pan": (0.5, 0.5)},
    {"img": "CLAM1883", "pan": (0.5, 0.5)},
    {"img": "PAIR2010", "pan": (0.22, 0.5)},
    {"img": "BOARD", "pan": (0.5, 0.5)},
]

_E = "ease-in-out"
_LB = {"type": "letterbox", "zoom": [1.0, 1.03, 1.06], "pan": [(0.5, 0.5)] * 3, "ease": _E}

SLIDES = [
    {"img": "HERO", **_LB},       # s0
    {"img": "PAINT", **_LB},      # s1
    {"img": "SW", **_LB},         # s3
    {"img": "MAP", **_LB},        # s4
    {"img": "PAIR2010", **_LB},   # s7
]
SCHEDULE = [(0.0, 0), (4.4, 1), (18.3, 2), (36.125, 3), (58.5, 4)]
TOTAL_DURATION = 66.425
TIMING_JSON = "audio/the-sisters-islands-and-singapores-first-marine-park.timing.json"

BURN_CAPTIONS = True
CAPTION_FONT_RATIO = 0.032
CAPTION_MAX_WIDTH_FRAC = 0.86
CAPTION_Y_FRAC = 0.70

# The avatar presenter, cartoon with motion: corner bubble for the first and last 30 s.
AVATAR = {"ranges": [(0, 30), (-30, None)], "motion": True}
