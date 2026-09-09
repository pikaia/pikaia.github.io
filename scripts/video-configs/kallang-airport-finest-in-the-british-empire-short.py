"""Shorts config for the Kallang Airport post.

Excerpt: the opening hook, sentences 0-6 (0 -> 58.25s, a real sentence
boundary in the timing.json) - the curved butter-coloured building on
the north bank of the Kallang Basin that tens of thousands walk past
every week; for eighteen years the terminal of an airport once called
the finest in the British Empire and, by Amelia Earhart, "an aviation
miracle of the East"; closed in 1955, and still standing there empty.

4 slides: freed POWs at the terminal, 1945 -> the empty terminal today
-> the whole airfield from the air, 1945 -> the empty terminal today.
All roughly square / landscape, so they cover the 1080x1920 frame.
"""

WIDTH, HEIGHT = 1080, 1920

_U = "https://upload.wikimedia.org/wikipedia/commons"
_C = f"{_U}/thumb"

IMAGES = {
    "HERO_POW": f"{_U}/a/a0/Evacuation_of_British_POWs%2C_Kallang_Airport%2C_Singapore_-_19450908.jpg",
    "TERMINAL2021": f"{_C}/f/f3/Kallang_Airport_Terminal.jpg/1280px-Kallang_Airport_Terminal.jpg",
    "AERIAL1945": f"{_U}/d/d4/Kallang_Airport_aerial_photo_1945.jpg",
}

SLIDES = [
    {"img": "HERO_POW", "type": "cover", "zoom": [1.0, 1.05, 1.10], "pan": [(0.5, 0.33)] * 3, "ease": "ease-in-out"},
    {"img": "TERMINAL2021", "type": "cover", "zoom": [1.0, 1.05, 1.10], "pan": [(0.5, 0.5)] * 3, "ease": "ease-in-out"},
    {"img": "AERIAL1945", "type": "cover", "zoom": [1.0, 1.05, 1.10], "pan": [(0.5, 0.5)] * 3, "ease": "ease-in-out"},
    {"img": "TERMINAL2021", "type": "cover", "zoom": [1.10, 1.05, 1.0], "pan": [(0.5, 0.5)] * 3, "ease": "ease-out"},
]

# Real sentence starts from the timing.json: s3 21.675, s4 31.975, s5 47.975.
SCHEDULE = [(0.0, 0), (21.675, 1), (31.975, 2), (47.975, 3)]
TOTAL_DURATION = 58.25
TIMING_JSON = "audio/kallang-airport-finest-in-the-british-empire.timing.json"

# Shorts keep burned-in narration captions (muted autoplay); main videos do not -
# they rely on the uploaded .srt.
BURN_CAPTIONS = True
