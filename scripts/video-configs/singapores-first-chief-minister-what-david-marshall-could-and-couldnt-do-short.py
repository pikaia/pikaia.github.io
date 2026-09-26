"""Short config for the David Marshall post.

Excerpt: the opening hook (sentences 0-4, 0.0-51.7s) - the resignation on 7 June
1956 and the fourteen months before it. Ends exactly where sentence 5 begins in
the main config's own timing. Vertical 1080x1920. The 8 June 1956 front page is
shown whole (frozen letterbox) rather than zoomed in vertically, because a tall
window on it would include an unrelated photograph below the headline.
"""

WIDTH, HEIGHT = 1080, 1920

IMAGES = {
    "DEL": "https://thumb.wikimedia.org/wikipedia/commons/thumb/0/0c/Singaporean_delegation_at_the_1956_constitutional_talks.png/1920px-Singaporean_delegation_at_the_1956_constitutional_talks.png",
    "S0516": "/assets/images/straits-times-1956-05-16-page-1.jpg",
    "S0608": "/assets/images/straits-times-1956-06-08-page-1.jpg",
}

_DA = {"type": "cover", "zoom": [1.3, 1.35, 1.4], "pan": [(0.15, 0.5), (0.35, 0.5), (0.55, 0.5)], "ease": "ease-in-out"}
_DB = {"type": "cover", "zoom": [1.4, 1.35, 1.3], "pan": [(0.85, 0.5), (0.65, 0.5), (0.45, 0.5)], "ease": "ease-in-out"}
_PG = {"type": "cover", "zoom": [1.3, 1.35, 1.4], "pan": [(0.5, 0.0), (0.5, 0.04), (0.5, 0.08)], "ease": "ease-in-out"}
_FIX = {"type": "letterbox", "zoom": [1.0, 1.0, 1.0], "pan": [(0.5, 0.5)] * 3, "ease": "linear"}

SLIDES = [
    {"img": "DEL", **_DA},  # s0 title
    {"img": "S0608", **_FIX},  # s1 resigned 5 p.m. 7 June 1956
    {"img": "S0516", **_PG},  # s2 promise to resign
    {"img": "S0608", **_FIX},  # s3 the next morning's headline
    {"img": "DEL", **_DB},  # s4 the fourteen months
]

SCHEDULE = [(0.0, 0), (8.35, 1), (24.73, 2), (31.8, 3), (43.58, 4)]
TOTAL_DURATION = 51.7
TIMING_JSON = "audio/singapores-first-chief-minister-what-david-marshall-could-and-couldnt-do.timing.json"

BURN_CAPTIONS = True
CAPTION_FONT_RATIO = 0.032
CAPTION_MAX_WIDTH_FRAC = 0.86
CAPTION_Y_FRAC = 0.80
