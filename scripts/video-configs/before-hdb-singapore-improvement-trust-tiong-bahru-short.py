"""Shorts config for the Tiong Bahru / SIT post.

Excerpt: the opening hook, sentences 0-3 (0 -> 38.35s, a real sentence
boundary in the timing.json) - Tiong Bahru's Art Deco corners and
porthole windows read as a heritage flex today, but almost none of it
was built to be charming: it was Singapore's first public housing,
built to clear exactly the kind of slum it had once been.

3 slides: the hero corner block, then the 82 Tiong Poh Road fin detail,
then back to the hero.
"""

WIDTH, HEIGHT = 1080, 1920

_U = "https://upload.wikimedia.org/wikipedia/commons"
_C = f"{_U}/thumb"

IMAGES = {
    "HERO": f"{_C}/1/12/Tiong_Bahru_8%2C_Jul_06.JPG/1280px-Tiong_Bahru_8%2C_Jul_06.JPG",
    "FIN82": f"{_U}/a/ae/Tiong_Bahru_13%2C_Jul_06.JPG",
}

SLIDES = [
    {"img": "HERO", "type": "cover", "zoom": [1.0, 1.08, 1.16], "pan": [(0.5, 0.5)] * 3, "ease": "ease-in-out"},
    {"img": "FIN82", "type": "cover", "zoom": [1.0, 1.06, 1.12], "pan": [(0.5, 0.5)] * 3, "ease": "ease-in-out"},
    {"img": "HERO", "type": "cover", "zoom": [1.16, 1.08, 1.0], "pan": [(0.5, 0.5)] * 3, "ease": "ease-out"},
]

# Real sentence starts from the timing.json: s2 20.975, s3 24.425; excerpt ends at s4's 38.350.
SCHEDULE = [(0.0, 0), (20.975, 1), (24.425, 2)]
TOTAL_DURATION = 38.350
TIMING_JSON = "audio/before-hdb-singapore-improvement-trust-tiong-bahru.timing.json"

# Shorts keep burned-in narration captions (muted autoplay); main videos do not -
# they rely on the uploaded .srt.
BURN_CAPTIONS = True
