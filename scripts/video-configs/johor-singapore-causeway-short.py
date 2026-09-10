"""Shorts config for the Johor-Singapore Causeway post.

Excerpt: the opening hook, sentences 0-4 (0 -> 43.75s, a real sentence
boundary in the timing.json) - the Causeway has two rush hours running
in opposite directions: before dawn tens of thousands of Johor residents
pour south to jobs in Singapore; on the weekend the current reverses as
Singaporeans head north for cheaper petrol, groceries, dental work and
food. One kilometre of road on a bank of rock, worked from both ends by
the same currency gap.

4 slides: the empty Causeway at night -> the bus queue at Woodlands ->
an AEON mall in Johor Bahru -> the Causeway by day.
"""

WIDTH, HEIGHT = 1080, 1920

_U = "https://upload.wikimedia.org/wikipedia/commons"
_C = f"{_U}/thumb"

IMAGES = {
    "HERO_EMPTY": f"{_C}/9/9d/Empty_Singapore-Malaysia_Causeway_2.jpg/1280px-Empty_Singapore-Malaysia_Causeway_2.jpg",
    "BUSQUEUE": f"{_C}/f/f5/Woodlands_Checkpoint_Departure_Bus_Causeway_Link_-_Nov_2025.jpg/1280px-Woodlands_Checkpoint_Departure_Bus_Causeway_Link_-_Nov_2025.jpg",
    "AEON": f"{_C}/8/84/Aeon_Mall_and_a_rainbow%2C_Bukit_Indah%2C_Johor_Bahru%2C_Johor%2C_Malaysia.jpg/1280px-Aeon_Mall_and_a_rainbow%2C_Bukit_Indah%2C_Johor_Bahru%2C_Johor%2C_Malaysia.jpg",
    "CAUSEWAY_DAY": f"{_C}/c/c0/Johor_Causeway.jpg/1280px-Johor_Causeway.jpg",
}

SLIDES = [
    {"img": "HERO_EMPTY", "type": "cover", "zoom": [1.0, 1.05, 1.10], "pan": [(0.5, 0.5)] * 3, "ease": "ease-in-out"},
    {"img": "BUSQUEUE", "type": "cover", "zoom": [1.0, 1.05, 1.10], "pan": [(0.5, 0.5)] * 3, "ease": "ease-in-out"},
    {"img": "AEON", "type": "cover", "zoom": [1.0, 1.05, 1.10], "pan": [(0.5, 0.5)] * 3, "ease": "ease-in-out"},
    {"img": "CAUSEWAY_DAY", "type": "cover", "zoom": [1.10, 1.05, 1.0], "pan": [(0.5, 0.5)] * 3, "ease": "ease-out"},
]

# Real sentence starts from the timing.json: s2 10.625, s3 18.925, s4 36.125.
SCHEDULE = [(0.0, 0), (10.625, 1), (18.925, 2), (36.125, 3)]
TOTAL_DURATION = 43.75
TIMING_JSON = "audio/johor-singapore-causeway.timing.json"

# Shorts keep burned-in narration captions (muted autoplay); main videos do not -
# they rely on the uploaded .srt.
BURN_CAPTIONS = True
