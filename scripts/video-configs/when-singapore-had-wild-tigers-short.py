"""Shorts config for the wild-tigers post.

Excerpt: the opening hook, sentences 0-5 (0 -> 44.425s, a real sentence
boundary in the timing.json) - a rumoured death a day, the Governor's
"two hundred a year" figure to the House of Commons, the last tiger
shot in 1930, and the payoff that the wild animals never really left,
they just got smaller: an otter family in the financial district now
gets a road sign of its own.

4 slides: the locations map -> the c.1900 gambier plantation photo ->
the map again -> the CBD otter road sign. The timeline PNG is skipped
here - it's 16:9 and neither letterboxes (a band across the middle)
nor covers (loses the end events) into a 1080x1920 frame. The map is
near-square so it letterboxes cleanly; the otter sign is portrait so
it fills the vertical frame.
"""

WIDTH, HEIGHT = 1080, 1920

_C = "https://upload.wikimedia.org/wikipedia/commons"

IMAGES = {
    "MAP": "/assets/images/when-singapore-had-wild-tigers-map.png",
    "GAMBIER": f"{_C}/0/0d/ChineseGambierSingapore.jpg",
    "OTTERSIGN": f"{_C}/5/52/%27Watch_out_for_otters_crossing%27_sign_on_Robertson_Quay_near_Kim_Seng_Park%2C_Singapore.jpg",
}

CREDITS = {
    "MAP": "Map by Lesser Known Singapore; base map data © OpenStreetMap contributors",
}

SLIDES = [
    {"img": "MAP", "type": "letterbox", "zoom": [1.0, 1.02, 1.04], "pan": [(0.5, 0.5)] * 3, "ease": "linear"},
    {"img": "GAMBIER", "type": "cover", "zoom": [1.0, 1.05, 1.10], "pan": [(0.5, 0.5)] * 3, "ease": "ease-in-out"},
    {"img": "MAP", "type": "letterbox", "zoom": [1.0, 1.02, 1.04], "pan": [(0.5, 0.5)] * 3, "ease": "linear"},
    {"img": "OTTERSIGN", "type": "letterbox", "zoom": [1.0, 1.04, 1.08], "pan": [(0.5, 0.5)] * 3, "ease": "ease-in-out"},
]

# Real sentence starts from the timing.json: s2 at 9.975, s3 at 22.35, s5 at 36.875.
SCHEDULE = [(0.0, 0), (9.975, 1), (22.35, 2), (36.875, 3)]
TOTAL_DURATION = 44.425
TIMING_JSON = "audio/when-singapore-had-wild-tigers.timing.json"

# Shorts keep burned-in narration captions (muted autoplay); main videos do not -
# they rely on the uploaded .srt.
BURN_CAPTIONS = True
