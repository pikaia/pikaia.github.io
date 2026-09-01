"""Shorts config for "How a Japanese Greengrocer Changed the Way
Singapore Shops."

Excerpt: the opening hook, sentences 0-4 (0 -> 47.0s, a real sentence
boundary in the timing.json). Yaohan's Plaza Singapura opening in 1974,
the first-week crowds, and the payoff - "the idea it arrived with, good
food sold cheaply in the basement, has outlasted all of them."

3 slides: Plaza Singapura outside -> the mall interior -> the survivor,
Ngee Ann City.
"""

WIDTH, HEIGHT = 1080, 1920

_C = "https://upload.wikimedia.org/wikipedia/commons"

IMAGES = {
    "PLAZA": f"{_C}/c/c3/Plaza_Singapura%2C_Dec_05.JPG",
    "PLAZAINT": f"{_C}/2/28/Large_interior_view_of_Plaza_Singapura_Shopping_mall_Orchard_Road_Singapore.jpg",
    "NGEEANN": f"{_C}/2/2e/Ngee_Ann_City%2C_Dec_05.JPG",
}

SLIDES = [
    {"img": "PLAZA", "type": "letterbox", "zoom": [1, 1.05, 1.10], "pan": [(0.5, 0.5)] * 3, "ease": "ease-in-out"},
    {"img": "PLAZAINT", "type": "letterbox", "zoom": [1, 1.05, 1.10], "pan": [(0.5, 0.5)] * 3, "ease": "ease-in"},
    {"img": "NGEEANN", "type": "letterbox", "zoom": [1, 1.05, 1.10], "pan": [(0.5, 0.5)] * 3, "ease": "ease-in-out"},
]

# Real sentence starts from the timing.json: s2 at 21.77, s4 at 31.32.
SCHEDULE = [(0.0, 0), (21.77, 1), (31.32, 2)]
TOTAL_DURATION = 47.0
TIMING_JSON = "audio/yaohan-japanese-department-stores-orchard-road.timing.json"

# Shorts keep burned-in narration captions (muted autoplay); main videos do not -
# they rely on the uploaded .srt. Caption size/position come from the
# DEFAULT_CAPTION_* module constants (small outlined white text, no box).
BURN_CAPTIONS = True
