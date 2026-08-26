"""Video config for the fishball-noodle hawker-rent-gap post's Watch
widget and main video.

Only 3 real images exist for this post (no gallery - the topic is
genuinely thin on relevant photography beyond what's already inline):
GOLDENMILE (2005, where Ng's stall began), MEEPOK (the dish itself),
MARINEPARADE (2025, the 2024 record-bid site). 20 slides across those
3 images with varied zoom/pan/ease, same reuse pattern as the Dear You
config. All three are landscape enough (1.33-1.5 aspect) for "cover" -
no letterbox needed.
"""

IMAGES = {
    "GOLDENMILE": "https://upload.wikimedia.org/wikipedia/commons/2/21/Golden_Mile_Food_Centre%2C_Dec_05.JPG",
    "MEEPOK": "https://upload.wikimedia.org/wikipedia/commons/0/01/FishBallMeePok.jpg",
    "MARINEPARADE": "https://upload.wikimedia.org/wikipedia/commons/f/fc/84_Marine_Parade_Central_Market_and_Food_Centre.jpg",
}

SLIDES = [
    {"img": "GOLDENMILE", "type": "cover", "zoom": [1, 1.08, 1.15], "pan": [(0.50, 0.45), (0.50, 0.50), (0.50, 0.55)], "ease": "ease-in-out"},
    {"img": "MEEPOK", "type": "cover", "zoom": [1.15, 1.06, 1], "pan": [(0.55, 0.45), (0.50, 0.50), (0.45, 0.55)], "ease": "ease-out"},
    {"img": "MEEPOK", "type": "cover", "zoom": [1, 1.06, 1.12], "pan": [(0.40, 0.50), (0.50, 0.50), (0.60, 0.50)], "ease": "linear"},
    {"img": "GOLDENMILE", "type": "cover", "zoom": [1, 1.09, 1.16], "pan": [(0.60, 0.40), (0.50, 0.50), (0.40, 0.60)], "ease": "ease-in"},
    {"img": "GOLDENMILE", "type": "cover", "zoom": [1.15, 1.07, 1], "pan": [(0.45, 0.55), (0.50, 0.50), (0.55, 0.45)], "ease": "ease-in-out"},
    {"img": "MEEPOK", "type": "cover", "zoom": [1, 1.07, 1.14], "pan": [(0.50, 0.40), (0.50, 0.50), (0.50, 0.60)], "ease": "ease-out"},
    {"img": "GOLDENMILE", "type": "cover", "zoom": [1, 1.05, 1.1], "pan": [(0.5, 0.5), (0.5, 0.5), (0.5, 0.5)], "ease": "linear"},
    {"img": "GOLDENMILE", "type": "cover", "zoom": [1.1, 1.05, 1], "pan": [(0.40, 0.45), (0.50, 0.50), (0.60, 0.55)], "ease": "ease-in"},
    {"img": "MEEPOK", "type": "cover", "zoom": [1, 1.08, 1.16], "pan": [(0.55, 0.50), (0.50, 0.50), (0.45, 0.50)], "ease": "ease-in-out"},
    {"img": "GOLDENMILE", "type": "cover", "zoom": [1, 1.06, 1.12], "pan": [(0.50, 0.60), (0.50, 0.50), (0.50, 0.40)], "ease": "ease-out"},
    {"img": "GOLDENMILE", "type": "cover", "zoom": [1.12, 1.06, 1], "pan": [(0.45, 0.40), (0.50, 0.50), (0.55, 0.60)], "ease": "linear"},
    {"img": "MEEPOK", "type": "cover", "zoom": [1, 1.09, 1.18], "pan": [(0.60, 0.55), (0.50, 0.50), (0.40, 0.45)], "ease": "ease-in"},
    {"img": "MARINEPARADE", "type": "cover", "zoom": [1, 1.05, 1.1], "pan": [(0.5, 0.5), (0.5, 0.5), (0.5, 0.5)], "ease": "ease-in-out"},
    {"img": "MEEPOK", "type": "cover", "zoom": [1.15, 1.07, 1], "pan": [(0.50, 0.45), (0.50, 0.50), (0.50, 0.55)], "ease": "ease-out"},
    {"img": "MARINEPARADE", "type": "cover", "zoom": [1, 1.08, 1.15], "pan": [(0.40, 0.50), (0.50, 0.50), (0.60, 0.50)], "ease": "ease-in"},
    {"img": "MARINEPARADE", "type": "cover", "zoom": [1.15, 1.06, 1], "pan": [(0.55, 0.40), (0.50, 0.50), (0.45, 0.60)], "ease": "linear"},
    {"img": "GOLDENMILE", "type": "cover", "zoom": [1, 1.07, 1.14], "pan": [(0.45, 0.50), (0.50, 0.50), (0.55, 0.50)], "ease": "ease-in-out"},
    {"img": "MARINEPARADE", "type": "cover", "zoom": [1, 1.06, 1.12], "pan": [(0.50, 0.55), (0.50, 0.50), (0.50, 0.45)], "ease": "ease-out"},
    {"img": "GOLDENMILE", "type": "cover", "zoom": [1.1, 1.05, 1], "pan": [(0.55, 0.55), (0.50, 0.50), (0.45, 0.45)], "ease": "ease-in"},
    {"img": "MEEPOK", "type": "cover", "zoom": [1, 1.08, 1.16], "pan": [(0.50, 0.50), (0.45, 0.50), (0.55, 0.50)], "ease": "ease-in-out"},
]

# Real values from audio/the-fishball-noodle-that-exposed-singapores-hawker-rent-gap.timing.json,
# re-derived a second time after also fixing "stung" (misaki's lexicon
# wrongly gave it "strung"'s phonemes) and retuning "Ng" from "ing" to
# "ung" (same 39 sentences/order, offsets shifted slightly shorter again).
SCHEDULE = [
    (0.0, 0), (18.73, 1), (43.5, 2), (67.58, 3), (85.62, 4),
    (104.15, 5), (126.45, 6), (135.8, 7), (161.32, 8), (187.72, 9),
    (203.95, 10), (226.03, 11), (255.43, 12), (262.43, 13), (289.93, 14),
    (322.05, 15), (351.55, 16), (371.48, 17), (387.45, 18), (410.48, 19),
]
TOTAL_DURATION = 437.8
TIMING_JSON = "audio/the-fishball-noodle-that-exposed-singapores-hawker-rent-gap.timing.json"
