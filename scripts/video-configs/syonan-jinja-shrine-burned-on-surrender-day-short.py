"""Video config for the Syonan Jinja post's YouTube Shorts excerpt (vertical).

Self-contained hook: the post's opening four sentences (0-38.325s) - the
shrine burned by its own builders on the day of surrender, built by POWs to
be the grandest shrine outside Tokyo, burned rather than let the British
see it standing.

CONSTRUCTION's aspect (490x341 = 1.437) is close enough to 16:9 for a cover
crop in the horizontal video, but far from the vertical 1080x1920 target
(0.5625) - the letterbox treatment is used here instead, even though the
same image is `cover` in the full-video config. Check the actual aspect
against the actual output target every time; it doesn't carry over between
orientations (see the Lim Kim San post's video-config for the mirror-image
case: a portrait source that needed letterbox horizontally but not
vertically).
"""

WIDTH, HEIGHT = 1080, 1920

IMAGES = {
    "CONSTRUCTION": "https://upload.wikimedia.org/wikipedia/commons/8/80/Shinto_shrine_in_Shonan_%28Singapore%29_-_194210.jpg",
}

SLIDES = [
    {"img": "CONSTRUCTION", "type": "letterbox", "zoom": [1, 1.05, 1.1], "pan": [(0.5, 0.5), (0.5, 0.5), (0.5, 0.5)]},
    {"img": "CONSTRUCTION", "type": "letterbox", "zoom": [1.1, 1.05, 1], "pan": [(0.5, 0.5), (0.5, 0.5), (0.5, 0.5)]},
    {"img": "CONSTRUCTION", "type": "letterbox", "zoom": [1, 1.06, 1.12], "pan": [(0.5, 0.5), (0.5, 0.5), (0.5, 0.5)]},
]

SCHEDULE = [(0.0, 0), (13.0, 1), (26.0, 2)]
TOTAL_DURATION = 38.325
TIMING_JSON = "audio/syonan-jinja-shrine-burned-on-surrender-day.timing.json"

BURN_CAPTIONS = True
CAPTION_FONT_RATIO = 0.032
CAPTION_MAX_WIDTH_FRAC = 0.86
CAPTION_Y_FRAC = 0.80
