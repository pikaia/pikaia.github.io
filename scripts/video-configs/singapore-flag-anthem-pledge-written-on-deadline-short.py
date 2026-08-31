"""Shorts config for "Singapore's National Symbols Were All Written on a
Deadline."

Excerpt: the opening hook, sentences 1-3 (0 -> 39.95s, a real sentence
boundary in the timing.json). "Singapore's national anthem was not
written for a nation - it was written for the reopening of a concert
hall" -> "that anthem, the flag flown outside every void deck, and the
pledge ... exist because two different governments needed something to
point to on a tight deadline: once in 1959 ... and again in 1966."

2 slides: VICTORIA (the concert hall the anthem was written for) ->
FLAG (the symbol the deadline produced).
"""

WIDTH, HEIGHT = 1080, 1920

_C = "https://upload.wikimedia.org/wikipedia/commons"
_T = "https://upload.wikimedia.org/wikipedia/commons/thumb"

IMAGES = {
    "VICTORIA": f"{_C}/3/34/Rear_entrance_of_Victoria_Theatre_and_Concert_Hall%2C_Singapore_-_20141101-02.JPG",
    "FLAG": f"{_T}/4/48/Flag_of_Singapore.svg/1280px-Flag_of_Singapore.svg.png",
}

SLIDES = [
    {"img": "VICTORIA", "type": "letterbox", "zoom": [1, 1.06, 1.12], "pan": [(0.5, 0.5), (0.5, 0.5), (0.5, 0.5)], "ease": "ease-in-out"},
    {"img": "FLAG", "type": "letterbox", "zoom": [1, 1.04, 1.08], "pan": [(0.5, 0.5), (0.5, 0.5), (0.5, 0.5)], "ease": "linear"},
]

# Real sentence start from the timing.json: s3 at 13.075.
SCHEDULE = [(0.0, 0), (13.075, 1)]
TOTAL_DURATION = 39.95
TIMING_JSON = "audio/singapore-flag-anthem-pledge-written-on-deadline.timing.json"

# Shorts keep burned-in narration captions (muted autoplay); main videos do not -
# they rely on the uploaded .srt. The lines below size the caption box:
BURN_CAPTIONS = True
CAPTION_FONT_RATIO = 0.032
CAPTION_MAX_WIDTH_FRAC = 0.86
CAPTION_Y_FRAC = 0.80
