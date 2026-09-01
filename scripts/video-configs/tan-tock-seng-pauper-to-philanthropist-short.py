"""Shorts config for "The Vegetable Seller Behind Singapore's Most
Recognisable Hospital Name" (Tan Tock Seng).

Excerpt: the opening hook, sentences 1-3 (0 -> 40.15s, a real sentence
boundary in the timing.json). "In 1819... a 21-year-old migrant from
Malacca arrived with no money, no land, and no name that meant anything
on this side of the strait" -> "Tan Tock Seng sold vegetables and
poultry off a cart to get by" -> "by the time he died in 1850, he'd
become wealthy enough to fund Singapore's first hospital for the poor."

3 slides: PORTRAIT (the man) -> BOATQUAY (the river he worked) ->
HOSPITAL (the Pearl's Hill building his money paid for).
"""

WIDTH, HEIGHT = 1080, 1920

_C = "https://upload.wikimedia.org/wikipedia/commons"
_T = "https://upload.wikimedia.org/wikipedia/commons/thumb"

IMAGES = {
    "PORTRAIT": f"{_C}/4/45/Tan_Tock_Seng.jpg",
    "BOATQUAY": f"{_T}/7/79/KITLV_-_29175_-_View_of_the_harbor_of_Singapore_-_1860.tif/lossy-page1-1920px-KITLV_-_29175_-_View_of_the_harbor_of_Singapore_-_1860.tif.jpg",
    "HOSPITAL": f"{_C}/c/c3/Tan_Tock_Seng_Hospital_circa_1844-1856.jpg",
}

SLIDES = [
    {"img": "PORTRAIT", "type": "letterbox", "zoom": [1, 1.05, 1.10], "pan": [(0.5, 0.5), (0.5, 0.5), (0.5, 0.5)], "ease": "ease-in-out"},
    {"img": "BOATQUAY", "type": "letterbox", "zoom": [1, 1.06, 1.12], "pan": [(0.5, 0.5), (0.5, 0.5), (0.5, 0.5)], "ease": "ease-in"},
    {"img": "HOSPITAL", "type": "letterbox", "zoom": [1, 1.06, 1.12], "pan": [(0.5, 0.5), (0.5, 0.5), (0.5, 0.5)], "ease": "ease-in-out"},
]

# Real sentence starts from the timing.json: s2 at 21.5, s3 at 26.775.
SCHEDULE = [(0.0, 0), (21.5, 1), (26.775, 2)]
TOTAL_DURATION = 40.15
TIMING_JSON = "audio/tan-tock-seng-pauper-to-philanthropist.timing.json"

# Shorts keep burned-in narration captions (muted autoplay); main videos do not -
# they rely on the uploaded .srt. Caption size/position come from the
# DEFAULT_CAPTION_* module constants (small outlined white text, no box).
BURN_CAPTIONS = True
