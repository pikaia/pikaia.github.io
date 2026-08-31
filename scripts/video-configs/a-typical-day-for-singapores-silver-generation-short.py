"""Video config for the silver-generation post's YouTube Shorts excerpt.

Self-contained hook: the post's opening (0-30.55s) - a real "morning in
the life" arc: the Active Ageing Centre routine, the fitness-corner
stretch, and the hawker centre work - a real vignette payoff, not a
mid-sentence cut. Ends exactly where sentence 3 ends.

HERO (1.778 aspect) and BedokHawker (1.5) are both close enough to the
vertical 1080x1920 target for cover. HaigRoad (1.332, one of Chris's
own photos) needs letterbox here too, same as in the main video.
"""

WIDTH, HEIGHT = 1080, 1920

IMAGES = {
    "HERO": "https://upload.wikimedia.org/wikipedia/commons/7/7a/Our_Tampines_Hub_Town_Square.jpg",
    "HAIGROAD": "/assets/images/haig_road_park_connector.jpeg",
    "BEDOKHAWKER": "https://upload.wikimedia.org/wikipedia/commons/6/66/Bedok_Hawker_Centre.jpg",
}

SLIDES = [
    {"img": "HERO", "type": "cover", "zoom": [1, 1.06, 1.12], "pan": [(0.5, 0.5), (0.5, 0.5), (0.5, 0.5)]},
    {"img": "HAIGROAD", "type": "letterbox", "zoom": [1.12, 1.06, 1], "pan": [(0.5, 0.5), (0.5, 0.5), (0.5, 0.5)]},
    {"img": "BEDOKHAWKER", "type": "cover", "zoom": [1, 1.07, 1.14], "pan": [(0.55, 0.5), (0.5, 0.5), (0.45, 0.5)]},
]

SCHEDULE = [(0.0, 0), (15.125, 1), (23.5, 2)]
TOTAL_DURATION = 30.55  # real sentence-timing boundary for this post's opening hook
TIMING_JSON = "audio/a-typical-day-for-singapores-silver-generation.timing.json"

BURN_CAPTIONS = True
CAPTION_FONT_RATIO = 0.032
CAPTION_MAX_WIDTH_FRAC = 0.86
CAPTION_Y_FRAC = 0.80
