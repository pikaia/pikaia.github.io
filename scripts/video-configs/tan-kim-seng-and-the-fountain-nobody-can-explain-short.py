"""Short config for the Tan Kim Seng post - the fountain hook (sentences
0-3): the dry-spouts irony and the "nobody stops to read it" mystery,
before the reveal of who Tan Kim Seng was. 4 slides, 39.15s.
"""

_U = "https://upload.wikimedia.org/wikipedia/commons"

IMAGES = {
    "PORTRAIT": f"{_U}/a/a1/Qu_Chiqing%2C_Ancestor_portrait_of_Tan_Kim_Seng%2C_Mid_19th_century%2C_Oil_on_canvas%2C_98_x_78_cm%2C_Asian_Civilisations_Museum.png",
    "MODERN": f"{_U}/c/c9/Tan_Kim_Seng_Fountain%2C_2026_01.jpg",
}

_CVZ = {"type": "cover", "zoom": [1.0, 1.06, 1.12], "pan": [(0.5, 0.5)] * 3, "ease": "ease-in-out"}
_CVZO = {"type": "cover", "zoom": [1.12, 1.06, 1.0], "pan": [(0.5, 0.5)] * 3, "ease": "ease-out"}
_LTB = {"type": "letterbox", "zoom": [1.0, 1.04, 1.08], "pan": [(0.5, 0.5)] * 3, "ease": "ease-in-out"}

SLIDES = [
    {"img": "PORTRAIT", **_LTB},    # 0  s0   title
    {"img": "MODERN", **_CVZ},      # 1  s1   ornate fountain has stood
    {"img": "MODERN", **_CVZO},     # 2  s2   joggers and tourists pass it
    {"img": "MODERN", **_CVZ},      # 3  s3   almost none stop to read
]

SCHEDULE = [
    (0.0, 0), (4.0, 1), (27.925, 2), (32.175, 3),
]
TOTAL_DURATION = 39.15
TIMING_JSON = "audio/tan-kim-seng-and-the-fountain-nobody-can-explain.timing.json"
