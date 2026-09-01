"""Shorts config for "The Bank That Spent a Century Teaching Singapore to
Save."

Excerpt: the opening hook, sentences 0-2 (0 -> 35.33s, a real sentence
boundary in the timing.json). The childhood object - a book of ten-cent
stamps pasted into a card - and the institution behind it, "whose
entire purpose, from 1877 onward, was to get ordinary people into the
habit of putting money aside."

2 slides: the passbook cover -> the passbook's inner pages.
"""

WIDTH, HEIGHT = 1080, 1920

_C = "https://upload.wikimedia.org/wikipedia/commons"

IMAGES = {
    "PASSBOOK": f"{_C}/3/39/Federation_of_Malaya_Post_Office_Savings_Bank_%28POSB%29_Bankbook%2C_Cover.png",
    "PASSBOOK2": f"{_C}/1/13/Federation_of_Malaya_Post_Office_Savings_Bank_%28POSB%29_Bankbook%2C_Inner_Front_Cover_%26_First_Page.png",
}

SLIDES = [
    {"img": "PASSBOOK", "type": "letterbox", "zoom": [1, 1.05, 1.10], "pan": [(0.5, 0.5), (0.5, 0.5), (0.5, 0.5)], "ease": "ease-in-out"},
    {"img": "PASSBOOK2", "type": "letterbox", "zoom": [1, 1.05, 1.10], "pan": [(0.5, 0.5), (0.5, 0.5), (0.5, 0.5)], "ease": "ease-in"},
]

# Real sentence start from the timing.json: s2 at 18.3.
SCHEDULE = [(0.0, 0), (18.3, 1)]
TOTAL_DURATION = 35.33
TIMING_JSON = "audio/posb-peoples-bank-nation-of-savers.timing.json"

# Shorts keep burned-in narration captions (muted autoplay); main videos do not -
# they rely on the uploaded .srt. Caption size/position come from the
# DEFAULT_CAPTION_* module constants (small outlined white text, no box).
BURN_CAPTIONS = True
