"""Video config for the Bugis Street post's YouTube Shorts excerpt.

Self-contained hook: the post's opening (0-47s) - a good night on Bugis
Street in the 1970s, hawkers and sailors and the nightly transgender
performers who outshone everyone, fame from Newsweek and guidebooks,
closing on "Singapore bulldozed the whole street" - a cliffhanger, not
a mid-sentence cut, same pattern as every prior Short.

MARKET2014A's aspect (3760x2496 = 1.506) is close to 16:9 for the
horizontal video's cover crop but far from the vertical 1080x1920
target (0.5625) - letterbox here, same lesson as every prior Short.
"""

WIDTH, HEIGHT = 1080, 1920

IMAGES = {
    "MARKET2014A": "https://upload.wikimedia.org/wikipedia/commons/e/ec/New_Bugis_Street%2C_Singapore%2C_2014_%2801%29.JPG",
}

SLIDES = [
    {"img": "MARKET2014A", "type": "letterbox", "zoom": [1, 1.05, 1.1], "pan": [(0.5, 0.5), (0.5, 0.5), (0.5, 0.5)]},
    {"img": "MARKET2014A", "type": "letterbox", "zoom": [1.1, 1.05, 1], "pan": [(0.5, 0.5), (0.5, 0.5), (0.5, 0.5)]},
    {"img": "MARKET2014A", "type": "letterbox", "zoom": [1, 1.06, 1.12], "pan": [(0.5, 0.5), (0.5, 0.5), (0.5, 0.5)]},
]

SCHEDULE = [(0.0, 0), (15.7, 1), (31.4, 2)]
TOTAL_DURATION = 47.0
TIMING_JSON = "audio/bugis-street-before-redevelopment.timing.json"

BURN_CAPTIONS = True
CAPTION_FONT_RATIO = 0.032
CAPTION_MAX_WIDTH_FRAC = 0.86
CAPTION_Y_FRAC = 0.80
