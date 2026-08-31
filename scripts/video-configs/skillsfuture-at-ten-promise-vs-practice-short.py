"""Shorts config for "SkillsFuture at Ten: The Promise Still Outruns the
Practice".

Excerpt: the opening hook, sentences 1-4 (0 -> 49.725s, a real sentence
boundary in the timing.json). "A $500 government credit quietly expired
at the end of 2025 - seven in ten Singaporeans let it lapse" -> "weeks
later an MP was still asking Parliament whether the unclaimed money
could at least go to an elderly parent." Ends on the question, before
the Ministry's answer.

2 slides: PARLIAMENT (the debate) -> OLD_PARLIAMENT (the older chamber,
"parliamentary questions have always been this institution's business").
"""

WIDTH, HEIGHT = 1080, 1920

_C = "https://upload.wikimedia.org/wikipedia/commons"

IMAGES = {
    "PARLIAMENT": f"{_C}/8/89/Parliament_House_Singapore.jpg",
    "OLD_PARLIAMENT": f"{_C}/7/7c/Old_Parliament_House%2C_Singapore%2C_Feb_06.JPG",
}

SLIDES = [
    {"img": "PARLIAMENT", "type": "letterbox", "zoom": [1, 1.06, 1.12], "pan": [(0.5, 0.5), (0.5, 0.5), (0.5, 0.5)], "ease": "ease-in-out"},
    {"img": "OLD_PARLIAMENT", "type": "letterbox", "zoom": [1, 1.07, 1.14], "pan": [(0.5, 0.5), (0.5, 0.5), (0.5, 0.5)], "ease": "ease-in"},
]

# Real sentence start from the timing.json: s3 at 26.75.
SCHEDULE = [(0.0, 0), (26.75, 1)]
TOTAL_DURATION = 49.725
TIMING_JSON = "audio/skillsfuture-at-ten-promise-vs-practice.timing.json"

# Shorts keep burned-in narration captions (muted autoplay); main videos do not -
# they rely on the uploaded .srt. The lines below size the caption box:
BURN_CAPTIONS = True
CAPTION_FONT_RATIO = 0.032
CAPTION_MAX_WIDTH_FRAC = 0.86
CAPTION_Y_FRAC = 0.80
