"""Video config for the Dear You / Speak Mandarin Campaign post's YouTube
Shorts excerpt.

Self-contained hook: the post's opening (0-47s) - the title, the
"understand but can't speak" gap most 40-and-50-something Singaporeans
recognize, "not an accident... the direct result of a 1979 language
policy", closing on "which is what made it strange... Dear You sell out
its original-dialect screenings faster than the Mandarin-dubbed version
everyone expected to dominate" - a real cliffhanger, not a mid-sentence
cut, same pattern as every prior Short.

TEMPLE (1600x1200 = 1.33) is close to 4:3, far from the vertical
1080x1920 target (0.5625) - letterbox here, same lesson as every prior
Short.
"""

WIDTH, HEIGHT = 1080, 1920

IMAGES = {
    "TEMPLE": "https://upload.wikimedia.org/wikipedia/commons/7/71/Yueh_Hai_Ching_Temple_8%2C_Mar_06.JPG",
}

SLIDES = [
    {"img": "TEMPLE", "type": "letterbox", "zoom": [1, 1.05, 1.1], "pan": [(0.5, 0.5), (0.5, 0.5), (0.5, 0.5)]},
    {"img": "TEMPLE", "type": "letterbox", "zoom": [1.1, 1.05, 1], "pan": [(0.5, 0.5), (0.5, 0.5), (0.5, 0.5)]},
    {"img": "TEMPLE", "type": "letterbox", "zoom": [1, 1.06, 1.12], "pan": [(0.5, 0.5), (0.5, 0.5), (0.5, 0.5)]},
]

SCHEDULE = [(0.0, 0), (15.7, 1), (31.4, 2)]
TOTAL_DURATION = 47.0
TIMING_JSON = "audio/dear-you-and-the-dialect-singapore-tried-to-retire.timing.json"

CAPTION_FONT_RATIO = 0.032
CAPTION_MAX_WIDTH_FRAC = 0.86
CAPTION_Y_FRAC = 0.80
