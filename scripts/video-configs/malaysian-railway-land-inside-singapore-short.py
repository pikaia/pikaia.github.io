"""Shorts config for "The Strip of Malaysia That Ran Through Singapore
Until 2011."

Excerpt: the opening hook, sentences 0-3 (0 -> 39.88s, a real sentence
boundary in the timing.json). Until 2011 you cleared Malaysian
immigration in the centre of Singapore, because the station, its
platforms and a ribbon of land the length of the island were run by
Malaysia's railway - foreign-administered ground through the country for
46 years after Separation.

3 slides: the station facade -> the map of the line down the island ->
the platforms.
"""

WIDTH, HEIGHT = 1080, 1920

_C = "https://upload.wikimedia.org/wikipedia/commons"

IMAGES = {
    "FACADE": f"{_C}/0/0c/Tanjong_Pagar_Railway_Station_exterior_view%281_retouched%29.jpg",
    "MAP": "/assets/images/malaysian-railway-land-map.png",
    "PLATFORM": f"{_C}/f/fe/Platforms_and_tracks%2C_Tanjong_Pagar_Railway_Station%2C_Singapore_-_20100619-01.jpg",
}

CREDITS = {
    "MAP": "Map by Lesser Known Singapore; base map data © OpenStreetMap contributors",
}

SLIDES = [
    {"img": "FACADE", "type": "letterbox", "zoom": [1, 1.05, 1.10], "pan": [(0.5, 0.5)] * 3, "ease": "ease-in-out"},
    {"img": "MAP", "type": "letterbox", "zoom": [1, 1.03, 1.05], "pan": [(0.5, 0.5)] * 3, "ease": "linear"},
    {"img": "PLATFORM", "type": "letterbox", "zoom": [1, 1.05, 1.10], "pan": [(0.5, 0.5)] * 3, "ease": "ease-in-out"},
]

# Real sentence starts from the timing.json: s2 at 21.68, s3 at 30.90.
SCHEDULE = [(0.0, 0), (21.68, 1), (30.90, 2)]
TOTAL_DURATION = 39.88
TIMING_JSON = "audio/malaysian-railway-land-inside-singapore.timing.json"

# Shorts keep burned-in narration captions (muted autoplay); main videos do not -
# they rely on the uploaded .srt. Caption size/position come from the
# DEFAULT_CAPTION_* module constants (small outlined white text, no box).
BURN_CAPTIONS = True
