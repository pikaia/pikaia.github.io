"""Video config for the Benjamin Sheares post's YouTube Shorts excerpt.

Self-contained hook: the post's opening (0-46.55s) - the "who is this
ceremonial president" setup, closing on the actual reveal: the same man
who engineered Singapore's fertility decline as a working obstetrician,
years before he ever became president. A real payoff, not a mid-
sentence cut - the excerpt ends exactly where sentence 3 (the reveal
sentence) ends.

Story beat: open on his face (title), cut away to an "ordinary early
career" photo during the abstract policy-intro sentence, then return to
his face for the reveal itself - so the visual pays off the same way
the words do.

HERO (0.798 aspect) is close enough to the vertical 1080x1920 target
(0.5625) to use as cover here, same reasoning as other posts' Shorts.
ACADEMIC1940S (0.594) is even closer to portrait and also works as
cover.
"""

WIDTH, HEIGHT = 1080, 1920

IMAGES = {
    "HERO": "https://upload.wikimedia.org/wikipedia/commons/0/03/Benjamin_Sheares%2C_1951.jpg",
    "ACADEMIC1940S": "https://upload.wikimedia.org/wikipedia/commons/2/22/Benjamin_Sheares_1940s_full_photo.jpg",
}

SLIDES = [
    {"img": "HERO", "type": "cover", "zoom": [1, 1.06, 1.12], "pan": [(0.5, 0.5), (0.5, 0.5), (0.5, 0.5)]},
    {"img": "ACADEMIC1940S", "type": "cover", "zoom": [1.12, 1.06, 1], "pan": [(0.5, 0.45), (0.5, 0.5), (0.5, 0.55)]},
    {"img": "HERO", "type": "cover", "zoom": [1, 1.05, 1.1], "pan": [(0.5, 0.55), (0.5, 0.5), (0.5, 0.45)]},
]

SCHEDULE = [(0.0, 0), (5.025, 1), (25.1, 2)]
TOTAL_DURATION = 46.55  # real sentence-timing boundary for this post's opening hook
TIMING_JSON = "audio/benjamin-sheares-doctor-behind-the-baby-bust.timing.json"

CAPTION_FONT_RATIO = 0.032
CAPTION_MAX_WIDTH_FRAC = 0.86
CAPTION_Y_FRAC = 0.80
