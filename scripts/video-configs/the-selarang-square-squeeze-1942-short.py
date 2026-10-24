"""Short config for the Selarang Square post.

The post's opening, sentences 0-5 (0-61.725s, over the 60s TikTok line):
the squeeze of 2 September 1942, the square built for one battalion,
George Aspinall and his secret photographs, and the Changi garrison of the
1930s. Every slide is letterboxed: the 640px AWM photos and the 1941 photo
are too small or too wide to crop to a vertical frame.
"""

WIDTH, HEIGHT = 1080, 1920

IMAGES = {
    "HERO": "/assets/images/awm-132937-selarang-square-1942.jpg",
    "SQ03": "/assets/images/awm-132933-selarang-square-1942.jpg",
    "P160": "/assets/images/awm-p02569-160-selarang.jpg",
    "P154": "/assets/images/awm-p02569-154-selarang.jpg",
    "C1941": "https://upload.wikimedia.org/wikipedia/commons/thumb/4/49/Changi_1941_ii.jpg/1280px-Changi_1941_ii.jpg",
    "REL45": "https://upload.wikimedia.org/wikipedia/commons/c/c7/The_Release_of_Allied_Prisoners_of_War_From_Changi_Prison%2C_1945_CF722.jpg",  # thumbnail only
    "GATE": "https://upload.wikimedia.org/wikipedia/commons/thumb/c/cc/Changi_Museum_gates.jpg/1280px-Changi_Museum_gates.jpg",  # thumbnail only
}

# The main video's thumbnail grid, re-panned for tall cells.
THUMBNAIL = [
    {"img": "C1941", "pan": (0.5, 0.5)},
    {"img": "HERO", "pan": (0.5, 0.5)},
    {"img": "REL45", "pan": (0.5, 0.5)},
    {"img": "GATE", "pan": (0.5, 0.5)},
]

_E = "ease-in-out"
_LB = {"type": "letterbox", "zoom": [1.0, 1.03, 1.06], "pan": [(0.5, 0.5)] * 3, "ease": _E}

SLIDES = [
    {"img": "HERO", **_LB},           # s0
    {"img": "SQ03", **_LB},           # s1
    {"img": "P160", **_LB},           # s2-3
    {"img": "P154", **_LB},           # s4 George Aspinall (him, left)
    {"img": "C1941", **_LB},          # s5
]
SCHEDULE = [(0.0, 0), (3.7, 1), (21.35, 2), (37.15, 3), (48.925, 4)]
TOTAL_DURATION = 61.725
TIMING_JSON = "audio/the-selarang-square-squeeze-1942.timing.json"

BURN_CAPTIONS = True
CAPTION_FONT_RATIO = 0.032
CAPTION_MAX_WIDTH_FRAC = 0.86
CAPTION_Y_FRAC = 0.70

# The avatar presenter, cartoon with motion: corner bubble for the first and last 30 s.
AVATAR = {"ranges": [(0, 30), (-30, None)], "motion": True}
