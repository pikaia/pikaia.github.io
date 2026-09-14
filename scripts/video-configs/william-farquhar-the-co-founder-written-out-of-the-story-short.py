"""Shorts config for the William Farquhar post.

Excerpt: the opening hook, sentences 0-2 (0 -> 28.425s, a real sentence
boundary in the timing.json) - the Farquhar Garden at Fort Canning,
framed like his own natural history drawings, and the fact that almost
nobody who walks through it knows who he was.

3 slides: the hero portrait, the present-day garden, back to the hero.
"""

WIDTH, HEIGHT = 1080, 1920

_U = "https://upload.wikimedia.org/wikipedia/commons"

IMAGES = {
    "HERO": f"{_U}/f/f9/Portrait_of_William_Farquhar_%28c._1830%29.jpg",
    "GARDEN": f"{_U}/1/1d/View_from_William_Farquhar%27s_Garden.jpg",
}

SLIDES = [
    {"img": "HERO", "type": "letterbox", "zoom": [1.0, 1.04, 1.08], "pan": [(0.5, 0.5)] * 3, "ease": "ease-in-out"},
    {"img": "GARDEN", "type": "cover", "zoom": [1.0, 1.06, 1.12], "pan": [(0.5, 0.5)] * 3, "ease": "ease-in-out"},
    {"img": "HERO", "type": "letterbox", "zoom": [1.08, 1.04, 1.0], "pan": [(0.5, 0.5)] * 3, "ease": "ease-out"},
]

# Real sentence starts from the timing.json: s1 5.025, s2 22.575; excerpt ends at s3's 28.425.
SCHEDULE = [(0.0, 0), (5.025, 1), (22.575, 2)]
TOTAL_DURATION = 28.425
TIMING_JSON = "audio/william-farquhar-the-co-founder-written-out-of-the-story.timing.json"

# Shorts keep burned-in narration captions (muted autoplay); main videos do not -
# they rely on the uploaded .srt.
BURN_CAPTIONS = True
