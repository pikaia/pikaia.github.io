"""Shorts config for "The Shadow Tuition Economy: Singapore's $1.8 Billion
Bet Against Its Own Meritocracy".

Excerpt: the opening hook, sentences 1-3 (0 -> 45.95s, a real sentence
boundary in the timing.json). "The Ministry of Education has never made
private tuition a requirement for anything - officially it doesn't exist
as part of the system at all" -> "and yet Singaporean households spent
S$1.8 billion on it in 2023, more than seven in ten students now receive
some form of it, and it has become the single largest discretionary
expense in a typical family's education budget." Ends on the number.

2 slides: POPULAR (a bookstore's assessment-book aisles) -> CHART (the
S$680M-to-S$1.8B climb).
"""

WIDTH, HEIGHT = 1080, 1920

_C = "https://upload.wikimedia.org/wikipedia/commons"

IMAGES = {
    "POPULAR": f"{_C}/8/83/Popular_Book_Store%2C_Singapore.jpg",
    "CHART": "/assets/images/shadow-tuition-spend.png",
}

CREDITS = {
    "CHART": ("Tuition-spend chart by Lesser Known Singapore, from the Household "
              "Expenditure Survey figures cited in the post"),
}

SLIDES = [
    {"img": "POPULAR", "type": "letterbox", "zoom": [1, 1.06, 1.12], "pan": [(0.5, 0.5), (0.5, 0.5), (0.5, 0.5)], "ease": "ease-in-out"},
    {"img": "CHART", "type": "letterbox", "zoom": [1, 1.02, 1.04], "pan": [(0.5, 0.5), (0.5, 0.5), (0.5, 0.5)], "ease": "linear"},
]

# Real sentence start from the timing.json: s3 at 22.725.
SCHEDULE = [(0.0, 0), (22.725, 1)]
TOTAL_DURATION = 45.95
TIMING_JSON = "audio/shadow-tuition-economy-singapore-meritocracy.timing.json"

# Shorts keep burned-in narration captions (muted autoplay); main videos do not -
# they rely on the uploaded .srt. Caption size/position come from the
# DEFAULT_CAPTION_* module constants (small outlined white text, no box).
BURN_CAPTIONS = True
