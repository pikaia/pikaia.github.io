"""Shorts config for "The Fine City's Fine Print: Which of Singapore's
Famous Rules Still Stick".

Excerpt: the opening hook, sentences 1-4 (0 -> 44.075s, a real sentence
boundary in the timing.json). "A man fined S$2,500 and a Corrective Work
Order for a cigarette butt - his 13th littering conviction" -> "nobody
outside Singapore jokes about the littering law" -> "the one everyone
knows, the chewing gum ban, has actually gotten gentler." Self-contained,
ends before the "the famous ones turned out soft" turn.

2 slides: MRT_SIGN (the fine-city sign, the littering opener) -> GUM (the
gum ban that gets softer).
"""

WIDTH, HEIGHT = 1080, 1920

_C = "https://upload.wikimedia.org/wikipedia/commons"

IMAGES = {
    "MRT_SIGN": f"{_C}/d/dd/Singapore_MRT_Fines.jpg",
    "GUM": f"{_C}/5/52/Chewinggumpharmacysg.jpg",
}

SLIDES = [
    {"img": "MRT_SIGN", "type": "letterbox", "zoom": [1, 1.06, 1.12], "pan": [(0.5, 0.5), (0.5, 0.5), (0.5, 0.5)], "ease": "ease-in-out"},
    {"img": "GUM", "type": "letterbox", "zoom": [1, 1.07, 1.14], "pan": [(0.5, 0.5), (0.5, 0.5), (0.5, 0.5)], "ease": "ease-in"},
]

# Real sentence start from the timing.json: s2 at 24.2.
SCHEDULE = [(0.0, 0), (24.2, 1)]
TOTAL_DURATION = 44.075
TIMING_JSON = "audio/fine-city-fine-print-singapore-rules-still-stick.timing.json"

# Shorts keep burned-in narration captions (muted autoplay); main videos do not -
# they rely on the uploaded .srt. The lines below size the caption box:
BURN_CAPTIONS = True
CAPTION_FONT_RATIO = 0.032
CAPTION_MAX_WIDTH_FRAC = 0.86
CAPTION_Y_FRAC = 0.80
