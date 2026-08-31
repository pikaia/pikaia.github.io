"""Video config for the fishball-noodle hawker-rent-gap post's YouTube
Shorts excerpt.

Self-contained hook: the post's opening (0-43.5s) - Douglas Ng at the
2015 Bukit Panjang tender briefing, the $2.70-fishball-noodle vs.
$5.80-pasta price floor, closing on his own math: after ingredients
and labour, he was clearing about fifty cents of profit a bowl - a
real punchline, not a mid-sentence cut. (Re-derived a second time
after also fixing "stung" and retuning "Ng" to "ung" - same sentences,
offsets shifted slightly shorter again.)

Only GOLDENMILE and MEEPOK are used (MARINEPARADE is a present-day
image, doesn't fit this 2015-only excerpt). Both are landscape enough
(1.33-1.5 aspect) to diverge from the vertical 1080x1920 target -
letterbox, same lesson as every prior Short.
"""

WIDTH, HEIGHT = 1080, 1920

IMAGES = {
    "GOLDENMILE": "https://upload.wikimedia.org/wikipedia/commons/2/21/Golden_Mile_Food_Centre%2C_Dec_05.JPG",
    "MEEPOK": "https://upload.wikimedia.org/wikipedia/commons/0/01/FishBallMeePok.jpg",
}

SLIDES = [
    {"img": "GOLDENMILE", "type": "letterbox", "zoom": [1, 1.05, 1.1], "pan": [(0.5, 0.5), (0.5, 0.5), (0.5, 0.5)]},
    {"img": "MEEPOK", "type": "letterbox", "zoom": [1.1, 1.05, 1], "pan": [(0.5, 0.5), (0.5, 0.5), (0.5, 0.5)]},
    {"img": "GOLDENMILE", "type": "letterbox", "zoom": [1, 1.06, 1.12], "pan": [(0.5, 0.5), (0.5, 0.5), (0.5, 0.5)]},
]

SCHEDULE = [(0.0, 0), (18.73, 1), (33.02, 2)]
TOTAL_DURATION = 43.5  # real sentence-timing boundary for this post's opening hook
TIMING_JSON = "audio/the-fishball-noodle-that-exposed-singapores-hawker-rent-gap.timing.json"

BURN_CAPTIONS = True
CAPTION_FONT_RATIO = 0.032
CAPTION_MAX_WIDTH_FRAC = 0.86
CAPTION_Y_FRAC = 0.80
