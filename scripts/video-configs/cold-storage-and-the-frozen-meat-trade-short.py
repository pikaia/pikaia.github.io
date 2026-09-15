"""Shorts config for the Cold Storage post.

Excerpt: the opening hook, sentences 0-2 (0 -> 30.25s, a real sentence
boundary in the timing.json) - the 1903 founding and the single narrow
problem (no reliable way to keep meat cold in the tropics) everything
else in the post grew out of.

3 slides, all the Centrepoint hero photo - the only genuinely strong
photograph this thin-image topic has, and Centrepoint is also where the
post's own personal story is anchored.
"""

WIDTH, HEIGHT = 1080, 1920

_U = "https://upload.wikimedia.org/wikipedia/commons"

IMAGES = {
    "HERO": f"{_U}/2/29/Centrepoint_Shopping_Centre%2C_Singapore_-_20060212.jpg",
}

SLIDES = [
    {"img": "HERO", "type": "cover", "zoom": [1.0, 1.06, 1.12], "pan": [(0.5, 0.5)] * 3, "ease": "ease-in-out"},
    {"img": "HERO", "type": "cover", "zoom": [1.12, 1.18, 1.24], "pan": [(0.5, 0.5)] * 3, "ease": "ease-in-out"},
    {"img": "HERO", "type": "cover", "zoom": [1.24, 1.18, 1.12], "pan": [(0.5, 0.5)] * 3, "ease": "ease-out"},
]

# Real sentence starts from the timing.json: s1 3.375, s2 19.05; excerpt
# ends at s3's 30.25.
SCHEDULE = [(0.0, 0), (3.375, 1), (19.05, 2)]
TOTAL_DURATION = 30.25
TIMING_JSON = "audio/cold-storage-and-the-frozen-meat-trade.timing.json"

# Shorts keep burned-in narration captions (muted autoplay); main videos do not -
# they rely on the uploaded .srt.
BURN_CAPTIONS = True
