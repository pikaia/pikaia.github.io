"""Shorts config for "The Ointment Outlasted the Empire It Paid For."

Excerpt: the opening hook, sentences 0-3 (0 -> 41.23s, a real sentence
boundary in the timing.json). The leaping-tiger jar that turns up at any
pharmacy, sold in 100+ countries - and the payoff: "the last everyday
trace of a fortune that once also ran a stable of newspapers and a bank,
and paid for the hillside of painted concrete demons that Singaporeans
know as Haw Par Villa."

3 slides: a Tiger Balm sign -> a Haw Par Villa diorama -> the Ten Courts
of Hell entrance.
"""

WIDTH, HEIGHT = 1080, 1920

_C = "https://upload.wikimedia.org/wikipedia/commons"

IMAGES = {
    "SIGN71": f"{_C}/f/fb/71-528a_Tiger_Balm%2C_Singapore_1971_%2851251929204%29.jpg",
    "HELL8": f"{_C}/0/0b/Eighth_Court_of_Hell_%E2%80%93_Yama_King_Dushi%2C_Haw_Par_Villa_%2814793981305%29.jpg",
    "HELL": f"{_C}/c/c2/Entrance_to_the_Ten_Courts_of_Hell_%EF%BC%88%E5%8D%81%E6%AE%BF%E9%98%8E%E7%BD%97%EF%BC%89%2C_Haw_Par_Villa_%2814791602374%29.jpg",
}

SLIDES = [
    {"img": "SIGN71", "type": "letterbox", "zoom": [1, 1.05, 1.10], "pan": [(0.5, 0.5)] * 3, "ease": "ease-in-out"},
    {"img": "HELL8", "type": "letterbox", "zoom": [1, 1.05, 1.10], "pan": [(0.5, 0.5)] * 3, "ease": "ease-in"},
    {"img": "HELL", "type": "letterbox", "zoom": [1, 1.05, 1.10], "pan": [(0.5, 0.5)] * 3, "ease": "ease-in-out"},
]

# Real sentence starts from the timing.json: s2 at 14.65, s3 at 25.02.
SCHEDULE = [(0.0, 0), (14.65, 1), (25.02, 2)]
TOTAL_DURATION = 41.23
TIMING_JSON = "audio/aw-brothers-tiger-balm-fortune.timing.json"

# Shorts keep burned-in narration captions (muted autoplay); main videos do not -
# they rely on the uploaded .srt. Caption size/position come from the
# DEFAULT_CAPTION_* module constants (small outlined white text, no box).
BURN_CAPTIONS = True
