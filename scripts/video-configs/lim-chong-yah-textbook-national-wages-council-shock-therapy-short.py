"""Shorts config for "He Wrote Singapore's Economics Textbook, Then Spent
30 Years Defying It" (Lim Chong Yah).

Excerpt: the opening hook, sentences 1-3 (0 -> 40.625s, a real sentence
boundary in the timing.json). "Almost every Singaporean who sat for
pre-university economics learned supply and demand from the same
textbook: Elements of Economic Theory" -> "its lead author, Lim Chong
Yah, taught a generation the clean logic of free markets" -> "then, for
30 years running Singapore's actual wage-setting machinery, he spent
much of his career deciding when that logic should be overruled."

3 slides: TEXTBOOK (the book) -> OEI (the campus, the theory) ->
STRIKE (the labour disputes the wage machinery replaced).
"""

WIDTH, HEIGHT = 1080, 1920

_C = "https://upload.wikimedia.org/wikipedia/commons"

IMAGES = {
    "TEXTBOOK": "https://eservice.nlb.gov.sg/bookcoverwrapper/cover/0195846125?s=LG",
    "OEI": f"{_C}/4/4a/Oei_Tiong_Ham_Building.jpg",
    "STRIKE": f"{_C}/d/d3/Singapore_Glass_Factory_1951_strike.jpg",
}

CREDITS = {
    "TEXTBOOK": "Book cover of 'Elements of Economic Theory': National Library Board Singapore",
}

SLIDES = [
    {"img": "TEXTBOOK", "type": "letterbox", "zoom": [1, 1.04, 1.08], "pan": [(0.5, 0.5), (0.5, 0.5), (0.5, 0.5)], "ease": "ease-in-out"},
    {"img": "OEI", "type": "letterbox", "zoom": [1, 1.06, 1.12], "pan": [(0.5, 0.5), (0.5, 0.5), (0.5, 0.5)], "ease": "ease-in"},
    {"img": "STRIKE", "type": "letterbox", "zoom": [1, 1.06, 1.12], "pan": [(0.5, 0.5), (0.5, 0.5), (0.5, 0.5)], "ease": "ease-in-out"},
]

# Real sentence starts from the timing.json: s2 at 24.65, s3 at 30.925.
SCHEDULE = [(0.0, 0), (24.65, 1), (30.925, 2)]
TOTAL_DURATION = 40.625
TIMING_JSON = "audio/lim-chong-yah-textbook-national-wages-council-shock-therapy.timing.json"

# Shorts keep burned-in narration captions (muted autoplay); main videos do not -
# they rely on the uploaded .srt. Caption size/position come from the
# DEFAULT_CAPTION_* module constants (small outlined white text, no box).
BURN_CAPTIONS = True
