"""Video config for the Victoria Memorial Hall post's YouTube Shorts excerpt.

Self-contained hook: the post's opening (0-37.75s) - concertgoers file into
Victoria Concert Hall unaware the room once staged Japanese wartime
propaganda then hosted a war-crimes courtroom, closing on "as if nothing
else had ever happened inside it" - mystery framing with a natural cliffhanger
ending, not a mid-sentence cut.

HERO's aspect (710x437 = 1.625) is close to 16:9 for the horizontal video's
cover crop, but far from the vertical 1080x1920 target (0.5625) - letterbox
here, same lesson as every prior Short (Lim Kim San, Syonan Jinja): check
the actual aspect against the actual output target, it doesn't carry over
between orientations.
"""

WIDTH, HEIGHT = 1080, 1920

IMAGES = {
    "HERO": "https://upload.wikimedia.org/wikipedia/commons/e/e6/Victoria_Theatre_and_Victoria_Memorial_Hall_-_c_1930.jpg",
}

SLIDES = [
    {"img": "HERO", "type": "letterbox", "zoom": [1, 1.05, 1.1], "pan": [(0.5, 0.5), (0.5, 0.5), (0.5, 0.5)]},
    {"img": "HERO", "type": "letterbox", "zoom": [1.1, 1.05, 1], "pan": [(0.5, 0.5), (0.5, 0.5), (0.5, 0.5)]},
    {"img": "HERO", "type": "letterbox", "zoom": [1, 1.06, 1.12], "pan": [(0.5, 0.5), (0.5, 0.5), (0.5, 0.5)]},
]

SCHEDULE = [(0.0, 0), (13.0, 1), (26.0, 2)]
TOTAL_DURATION = 37.75
TIMING_JSON = "audio/victoria-memorial-hall-culture-war-crimes-trials.timing.json"

BURN_CAPTIONS = True
CAPTION_FONT_RATIO = 0.032
CAPTION_MAX_WIDTH_FRAC = 0.86
CAPTION_Y_FRAC = 0.80
