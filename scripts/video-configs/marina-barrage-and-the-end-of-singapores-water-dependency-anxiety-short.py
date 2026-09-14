"""Shorts config for the Marina Barrage post.

Excerpt: the opening hook, sentences 0-2 (0 -> 32.05s, a real sentence
boundary in the timing.json) - the barrage itself, and the fact that it
created Singapore's largest reservoir.

3 slides: the crest gates, held a beat longer, then the rooftop lawn.
Avoids the wide panorama source here - cover-cropping a 5:1 panorama
into a 9:16 portrait frame would reduce it to an unreadable sliver.
"""

WIDTH, HEIGHT = 1080, 1920

IMAGES = {
    "HERO": "/assets/images/marina-barrage-crest-gates.jpg",
    "ROOFTOP": "/assets/images/marina-barrage-rooftop-lawn.jpg",
}

SLIDES = [
    {"img": "HERO", "type": "cover", "zoom": [1.0, 1.06, 1.12], "pan": [(0.5, 0.5)] * 3, "ease": "ease-in-out"},
    {"img": "HERO", "type": "cover", "zoom": [1.12, 1.18, 1.24], "pan": [(0.5, 0.5)] * 3, "ease": "ease-in-out"},
    {"img": "ROOFTOP", "type": "cover", "zoom": [1.0, 1.06, 1.12], "pan": [(0.5, 0.5)] * 3, "ease": "ease-out"},
]

# Real sentence starts from the timing.json: s1 5.550, s2 17.200; excerpt ends at s3's 32.050.
SCHEDULE = [(0.0, 0), (5.550, 1), (17.200, 2)]
TOTAL_DURATION = 32.050
TIMING_JSON = "audio/marina-barrage-and-the-end-of-singapores-water-dependency-anxiety.timing.json"

# Shorts keep burned-in narration captions (muted autoplay); main videos do not -
# they rely on the uploaded .srt.
BURN_CAPTIONS = True
