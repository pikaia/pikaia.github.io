"""Shorts config for the P.S. Hunter post.

Excerpt: the opening hook, sentences 0-2 (0 -> 34.475s, a real sentence
boundary in the timing.json) - Tiong Bahru's Art Deco flats, and the
fact that almost nobody who photographs them knows the man behind
them, whose real name barely survives in the record.

3 slides, all the Tiong Bahru flat - it's the only image in this post
that's genuinely his own legacy rather than a supporting illustration.
"""

WIDTH, HEIGHT = 1080, 1920

_U = "https://upload.wikimedia.org/wikipedia/commons"

IMAGES = {
    "HERO": f"{_U}/8/8d/Tiong_Bahru_11%2C_Jul_06.JPG",
}

SLIDES = [
    {"img": "HERO", "type": "cover", "zoom": [1.0, 1.06, 1.12], "pan": [(0.5, 0.5)] * 3, "ease": "ease-in-out"},
    {"img": "HERO", "type": "cover", "zoom": [1.12, 1.18, 1.24], "pan": [(0.5, 0.5)] * 3, "ease": "ease-in-out"},
    {"img": "HERO", "type": "cover", "zoom": [1.24, 1.18, 1.12], "pan": [(0.5, 0.5)] * 3, "ease": "ease-out"},
]

# Real sentence starts from the timing.json: s1 5.400, s2 23.025; excerpt ends at s3's 34.475.
SCHEDULE = [(0.0, 0), (5.400, 1), (23.025, 2)]
TOTAL_DURATION = 34.475
TIMING_JSON = "audio/peter-sinclair-hunter-the-health-officer-whose-one-report-built-tiong-bahru.timing.json"

# Shorts keep burned-in narration captions (muted autoplay); main videos do not -
# they rely on the uploaded .srt.
BURN_CAPTIONS = True
