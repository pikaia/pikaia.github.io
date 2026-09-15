"""Shorts config for the Linggiu Reservoir post.

Excerpt: the opening hook, sentences 0-3 (0 -> 41.75s, a real sentence
boundary in the timing.json) - the 1962 treaty's guarantee, and the
fact that Singapore paid to build a dam inside another country just to
keep that guarantee working.

4 slides, all the Johor River hero photo - the only genuinely usable
photograph this thin-image topic has; the map (a labelled diagram)
doesn't read well at Shorts speed/size so it's reserved for the main
video only.
"""

WIDTH, HEIGHT = 1080, 1920

_U = "https://upload.wikimedia.org/wikipedia/commons"

IMAGES = {
    "HERO": f"{_U}/a/ac/Johor_River.jpg",
}

SLIDES = [
    {"img": "HERO", "type": "cover", "zoom": [1.0, 1.06, 1.12], "pan": [(0.5, 0.5)] * 3, "ease": "ease-in-out"},
    {"img": "HERO", "type": "cover", "zoom": [1.12, 1.18, 1.24], "pan": [(0.5, 0.5)] * 3, "ease": "ease-in-out"},
    {"img": "HERO", "type": "cover", "zoom": [1.24, 1.18, 1.12], "pan": [(0.5, 0.5)] * 3, "ease": "ease-out"},
    {"img": "HERO", "type": "cover", "zoom": [1.12, 1.06, 1.0], "pan": [(0.5, 0.5)] * 3, "ease": "ease-out"},
]

# Real sentence starts from the timing.json: s1 6.8, s2 20.5, s3 24.475;
# excerpt ends at s4's 41.75.
SCHEDULE = [(0.0, 0), (6.8, 1), (20.5, 2), (24.475, 3)]
TOTAL_DURATION = 41.75
TIMING_JSON = "audio/linggiu-reservoir-the-dam-singapore-built-inside-another-country-to-secure-its-own-water.timing.json"

# Shorts keep burned-in narration captions (muted autoplay); main videos do not -
# they rely on the uploaded .srt.
BURN_CAPTIONS = True
