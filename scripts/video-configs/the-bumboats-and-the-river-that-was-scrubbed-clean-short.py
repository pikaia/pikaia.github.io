"""Shorts config for the bumboats/river clean-up post.

Excerpt: the opening hook, sentences 0-1 (0 -> 25.7s, a real sentence
boundary in the timing.json) - for over a century the Singapore River
was Singapore's main cargo terminal with no proper dock, worked
entirely by hand-loaded lighters.

2 slides: the 1960 bumboat photo, zoomed in then pulled back.
"""

WIDTH, HEIGHT = 1080, 1920

_U = "https://upload.wikimedia.org/wikipedia/commons"

IMAGES = {
    "HERO": f"{_U}/f/f6/SingaporeRiver-bumboats-196009.jpg",
}

SLIDES = [
    {"img": "HERO", "type": "cover", "zoom": [1.0, 1.08, 1.16], "pan": [(0.5, 0.5)] * 3, "ease": "ease-in-out"},
    {"img": "HERO", "type": "cover", "zoom": [1.16, 1.08, 1.0], "pan": [(0.5, 0.5)] * 3, "ease": "ease-out"},
]

# Real sentence start from the timing.json: s1 3.800; excerpt ends at s2's 25.700.
SCHEDULE = [(0.0, 0), (3.800, 1)]
TOTAL_DURATION = 25.700
TIMING_JSON = "audio/the-bumboats-and-the-river-that-was-scrubbed-clean.timing.json"

# Shorts keep burned-in narration captions (muted autoplay); main videos do not -
# they rely on the uploaded .srt.
BURN_CAPTIONS = True
