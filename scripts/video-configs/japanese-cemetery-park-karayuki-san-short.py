"""Video config for the Japanese Cemetery Park post's YouTube Shorts excerpt.

Self-contained hook: the post's opening (0-49.2s) - the oldest graves at
the Japanese Cemetery Park belong to trafficked women, not soldiers or
merchants, the cemetery holds 910 tombstones with close to half marking
karayuki-san graves, closing on "it exists because a brothel keeper paid
for it" - a mystery-framing cliffhanger, not a mid-sentence cut, same
pattern as the Victoria Memorial Hall and Syonan Jinja Shorts.

HERO's aspect (3555x2208 = 1.61) is close to 16:9 for the horizontal
video's cover crop, but far from the vertical 1080x1920 target (0.5625) -
letterbox here, same lesson as every prior Short: check the actual aspect
against the actual output target, it doesn't carry over between
orientations.
"""

WIDTH, HEIGHT = 1080, 1920

IMAGES = {
    "HERO": "https://upload.wikimedia.org/wikipedia/commons/6/6c/Japanese_Cemetery_Park.jpg",
}

SLIDES = [
    {"img": "HERO", "type": "letterbox", "zoom": [1, 1.05, 1.1], "pan": [(0.5, 0.5), (0.5, 0.5), (0.5, 0.5)]},
    {"img": "HERO", "type": "letterbox", "zoom": [1.1, 1.05, 1], "pan": [(0.5, 0.5), (0.5, 0.5), (0.5, 0.5)]},
    {"img": "HERO", "type": "letterbox", "zoom": [1, 1.06, 1.12], "pan": [(0.5, 0.5), (0.5, 0.5), (0.5, 0.5)]},
]

SCHEDULE = [(0.0, 0), (16.4, 1), (32.8, 2)]
TOTAL_DURATION = 49.2
TIMING_JSON = "audio/japanese-cemetery-park-karayuki-san.timing.json"

CAPTION_FONT_RATIO = 0.032
CAPTION_MAX_WIDTH_FRAC = 0.86
CAPTION_Y_FRAC = 0.80
