"""Shorts config for the nutmeg / Orchard Road post.

Excerpt: the opening hook, sentences 0-4 (0 -> 51.275s, a real sentence
boundary in the timing.json) - Orchard Road today is glass towers and
malls, but its name is a leftover clue: in the 1830s and 40s this
ground was thick with actual orchards, nutmeg the biggest bet of all,
and the men who planted it are still on the street signs. Singapore's
most expensive shopping street is, underneath its signage, a map of a
spice that failed.

4 slides: Orchard Road at night -> the 1819-23 nutmeg watercolour ->
the Nutmeg Road street sign -> ION Orchard.
"""

WIDTH, HEIGHT = 1080, 1920

_U = "https://upload.wikimedia.org/wikipedia/commons"
_C = f"{_U}/thumb"

IMAGES = {
    "HERO_NIGHT": f"{_C}/a/a0/Orchard_Road_at_night%2C_2011.jpg/1280px-Orchard_Road_at_night%2C_2011.jpg",
    "FARQUHAR": f"{_U}/5/5d/Booa_Palla%3B_Nutmeg%3B_Myristica_moschata_%28William_Farquhar_Collection%2C_1819%E2%80%931823%29.jpg",
    "NUTMEG_ROAD": f"{_C}/3/34/Nutmeg_Road_2.JPG/1280px-Nutmeg_Road_2.JPG",
    "ION_ORCHARD": f"{_C}/8/8d/ION_Orchard.jpg/1280px-ION_Orchard.jpg",
}

SLIDES = [
    {"img": "HERO_NIGHT", "type": "cover", "zoom": [1.0, 1.05, 1.10], "pan": [(0.5, 0.5)] * 3, "ease": "ease-in-out"},
    {"img": "FARQUHAR", "type": "cover", "zoom": [1.0, 1.05, 1.10], "pan": [(0.5, 0.5)] * 3, "ease": "ease-in-out"},
    {"img": "NUTMEG_ROAD", "type": "cover", "zoom": [1.0, 1.05, 1.10], "pan": [(0.5, 0.5)] * 3, "ease": "ease-in-out"},
    {"img": "ION_ORCHARD", "type": "cover", "zoom": [1.10, 1.05, 1.0], "pan": [(0.5, 0.5)] * 3, "ease": "ease-out"},
]

# Real sentence starts from the timing.json: s2 14.375, s3 30.375, s4 43.975.
SCHEDULE = [(0.0, 0), (14.375, 1), (30.375, 2), (43.975, 3)]
TOTAL_DURATION = 51.275
TIMING_JSON = "audio/the-nutmeg-estates-that-became-orchard-road.timing.json"

# Shorts keep burned-in narration captions (muted autoplay); main videos do not -
# they rely on the uploaded .srt.
BURN_CAPTIONS = True
