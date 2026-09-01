"""Video config for the HDB post's YouTube Shorts excerpt.

Self-contained hook: the post's opening (0-36.25s) - today's $662/sqft
price, the $80/sqft 1990 starting point, closing on "thirty-five years of
Singapore's economic history is hiding somewhere in the distance between
those two numbers" - a cliffhanger, not a mid-sentence cut.

HERO's aspect (3598x1921 = 1.873) is close to 16:9 for the horizontal
video's cover crop but far from the vertical 1080x1920 target (0.5625) -
letterbox here, same lesson as every prior Short.
"""

WIDTH, HEIGHT = 1080, 1920

IMAGES = {
    "HERO": "https://upload.wikimedia.org/wikipedia/commons/d/d3/HDB_flats_in_Singapore_2.jpg",
}

SLIDES = [
    {"img": "HERO", "type": "letterbox", "zoom": [1, 1.05, 1.1], "pan": [(0.5, 0.5), (0.5, 0.5), (0.5, 0.5)]},
    {"img": "HERO", "type": "letterbox", "zoom": [1.1, 1.05, 1], "pan": [(0.5, 0.5), (0.5, 0.5), (0.5, 0.5)]},
    {"img": "HERO", "type": "letterbox", "zoom": [1, 1.06, 1.12], "pan": [(0.5, 0.5), (0.5, 0.5), (0.5, 0.5)]},
]

SCHEDULE = [(0.0, 0), (12.1, 1), (24.2, 2)]
TOTAL_DURATION = 36.25
TIMING_JSON = "audio/what-a-square-foot-of-hdb-flat-has-cost.timing.json"

BURN_CAPTIONS = True
