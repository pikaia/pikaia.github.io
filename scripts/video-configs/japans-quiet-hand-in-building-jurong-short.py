"""Video config for the Jurong post's YouTube Shorts excerpt.

Self-contained hook: the post's opening (0-48.65s) - Bridgestone breaking
ground in Singapore barely eighteen years after occupation, the louder
"blood debt" story, closing on "the quieter story... started before the
loud one was even finished" - a cliffhanger, not a mid-sentence cut.

HERO's aspect (4917x3253 = 1.512) is close to 16:9 for the horizontal
video's cover crop but far from the vertical 1080x1920 target (0.5625) -
letterbox here, same lesson as every prior Short.
"""

WIDTH, HEIGHT = 1080, 1920

IMAGES = {
    "HERO": "https://upload.wikimedia.org/wikipedia/commons/0/04/Signs_pointing_to_Jurong_Industrial_Estate_in_Singapore_June_1964.jpg",
}

SLIDES = [
    {"img": "HERO", "type": "letterbox", "zoom": [1, 1.05, 1.1], "pan": [(0.5, 0.5), (0.5, 0.5), (0.5, 0.5)]},
    {"img": "HERO", "type": "letterbox", "zoom": [1.1, 1.05, 1], "pan": [(0.5, 0.5), (0.5, 0.5), (0.5, 0.5)]},
    {"img": "HERO", "type": "letterbox", "zoom": [1, 1.06, 1.12], "pan": [(0.5, 0.5), (0.5, 0.5), (0.5, 0.5)]},
]

SCHEDULE = [(0.0, 0), (16.2, 1), (32.4, 2)]
TOTAL_DURATION = 48.65
TIMING_JSON = "audio/japans-quiet-hand-in-building-jurong.timing.json"

BURN_CAPTIONS = True
