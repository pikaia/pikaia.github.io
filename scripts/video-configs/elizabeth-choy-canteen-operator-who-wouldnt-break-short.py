"""Shorts config for the Elizabeth Choy post.

Excerpt: the opening hook, sentences 0-2 (0 -> 34.0s, a real sentence
boundary in the timing.json) - cross the junction where Orchard Road
meets Stamford Road, opposite the National Museum, and there's a YMCA
building with buses idling outside. Almost nobody waiting there knows
the building on this exact spot was once the Kempeitai's East District
Branch, where a schoolteacher named Elizabeth Choy spent roughly 200
days tortured for information she never gave up.

2 slides: the YMCA building today, zoomed in then pulled back.
"""

WIDTH, HEIGHT = 1080, 1920

_U = "https://upload.wikimedia.org/wikipedia/commons"
_C = f"{_U}/thumb"

IMAGES = {
    "HERO_YMCA": f"{_C}/b/b8/YMCA_Building_2.JPG/1280px-YMCA_Building_2.JPG",
}

SLIDES = [
    {"img": "HERO_YMCA", "type": "cover", "zoom": [1.0, 1.08, 1.16], "pan": [(0.5, 0.5)] * 3, "ease": "ease-in-out"},
    {"img": "HERO_YMCA", "type": "cover", "zoom": [1.16, 1.08, 1.0], "pan": [(0.5, 0.5)] * 3, "ease": "ease-out"},
]

# Real sentence start from the timing.json: s2 17.350.
SCHEDULE = [(0.0, 0), (17.350, 1)]
TOTAL_DURATION = 34.0
TIMING_JSON = "audio/elizabeth-choy-canteen-operator-who-wouldnt-break.timing.json"

# Shorts keep burned-in narration captions (muted autoplay); main videos do not -
# they rely on the uploaded .srt.
BURN_CAPTIONS = True
