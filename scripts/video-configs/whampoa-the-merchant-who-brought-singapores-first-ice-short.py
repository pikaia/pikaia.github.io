"""Shorts config for the Whampoa post.

Excerpt: the opening hook, sentences 0-2 (0 -> 34.25s, a real sentence
boundary in the timing.json) - Whampoa is a place most Singaporeans
know without knowing the man: the Royal Navy provisioner, ice
importer, Legislative Council member and honorary consul for three
empires behind the name.

3 slides: the hero portrait, the hawker centre lit up at night, then
back to the hero.
"""

WIDTH, HEIGHT = 1080, 1920

_U = "https://upload.wikimedia.org/wikipedia/commons"
_C = f"{_U}/thumb"

IMAGES = {
    "HERO": f"{_C}/7/7b/The_Hon._Hoh-Ah-Kay_Whampoa%2C_C.M.G.%2C_M.L.C.%2C_and_Consul_for_Wellcome_V0037527.jpg/1280px-The_Hon._Hoh-Ah-Kay_Whampoa%2C_C.M.G.%2C_M.L.C.%2C_and_Consul_for_Wellcome_V0037527.jpg",
    "WHAMPOA_MAKAN": f"{_C}/c/c9/Whampoa_Makan_Place%2C_exterior.jpg/1280px-Whampoa_Makan_Place%2C_exterior.jpg",
}

SLIDES = [
    {"img": "HERO", "type": "letterbox", "zoom": [1.0, 1.04, 1.08], "pan": [(0.5, 0.5)] * 3, "ease": "ease-in-out"},
    {"img": "WHAMPOA_MAKAN", "type": "cover", "zoom": [1.0, 1.06, 1.12], "pan": [(0.5, 0.5)] * 3, "ease": "ease-in-out"},
    {"img": "HERO", "type": "letterbox", "zoom": [1.08, 1.04, 1.0], "pan": [(0.5, 0.5)] * 3, "ease": "ease-out"},
]

# Real sentence starts from the timing.json: s1 3.975, s2 15.725; excerpt ends at s3's 34.250.
SCHEDULE = [(0.0, 0), (3.975, 1), (15.725, 2)]
TOTAL_DURATION = 34.250
TIMING_JSON = "audio/whampoa-the-merchant-who-brought-singapores-first-ice.timing.json"

# Shorts keep burned-in narration captions (muted autoplay); main videos do not -
# they rely on the uploaded .srt.
BURN_CAPTIONS = True
