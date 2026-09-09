"""Shorts config for the Coney Island post.

Excerpt: the opening hook, sentences 0-5 (0 -> 42.525s, a real sentence
boundary in the timing.json) - New York's Coney Island against
Singapore's locked gate and gravel track, the 1950 name and the failed
playground plan, and the payoff that what opened in 2015 was close to
the opposite of a resort.

5 slides: New York's Luna Park at night (1905) for the title and the
"New York had a switchback railway..." line -> the Singapore entrance
gate (letterbox - a centred landscape band; cover-cropping the wide
gate photo to a vertical frame chopped the lettering oddly) -> the
locator map -> the island panorama. The gate and panorama are
landscape; NYLUNA is near-square and covers the 1080x1920 frame on its
central lit tower; the map letterboxes cleanly.
"""

WIDTH, HEIGHT = 1080, 1920

_C = "https://upload.wikimedia.org/wikipedia/commons"

IMAGES = {
    "NYLUNA": f"{_C}/8/82/Night_in_Luna_Park%2C_Coney_Island_%281905%29.jpg",
    "GATE": f"{_C}/8/87/Coney_Island_Gate.jpg",
    "MAP": "/assets/images/coney-island-before-it-was-a-nature-park-map.png",
    "PANO2022": "/assets/images/coney-island-2022.jpg",
}

CREDITS = {
    "MAP": "Map by Lesser Known Singapore; base map data © OpenStreetMap contributors",
    "PANO2022": "Photograph: Lesser Known Singapore",
}

SLIDES = [
    {"img": "NYLUNA", "type": "cover", "zoom": [1.0, 1.05, 1.10], "pan": [(0.5, 0.5)] * 3, "ease": "ease-in-out"},
    {"img": "NYLUNA", "type": "cover", "zoom": [1.10, 1.05, 1.0], "pan": [(0.5, 0.5)] * 3, "ease": "ease-out"},
    {"img": "GATE", "type": "letterbox", "zoom": [1.0, 1.03, 1.06], "pan": [(0.5, 0.5)] * 3, "ease": "ease-in-out"},
    {"img": "MAP", "type": "letterbox", "zoom": [1.0, 1.02, 1.04], "pan": [(0.5, 0.5)] * 3, "ease": "linear"},
    {"img": "PANO2022", "type": "cover", "zoom": [1.0, 1.05, 1.10], "pan": [(0.5, 0.5)] * 3, "ease": "ease-in-out"},
]

# Real sentence starts from the timing.json: s1 3.65, s2 11.25, s3 19.625, s4 30.55.
SCHEDULE = [(0.0, 0), (3.65, 1), (11.25, 2), (19.625, 3), (30.55, 4)]
TOTAL_DURATION = 42.525
TIMING_JSON = "audio/coney-island-before-it-was-a-nature-park.timing.json"

# Shorts keep burned-in narration captions (muted autoplay); main videos do not -
# they rely on the uploaded .srt.
BURN_CAPTIONS = True
