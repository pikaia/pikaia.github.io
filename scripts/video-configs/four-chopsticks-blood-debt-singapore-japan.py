"""Video config for the "Four Chopsticks and the Blood Debt" post's Watch
widget and main video.

6 real images: MEMORIAL (present-day Civilian War Memorial, the post's
hero), ITEMS (recovered mass-grave items, present-day museum photo),
and 4 WWII-era images from the gallery (YAMASHITA - the Feb 1942
surrender talks, MARCH - Japanese troops entering the city, SHRINE -
a Shinto shrine under occupation, SURRENDER - the Sept 1945 Japanese
surrender). 23 slides across those 6 images with heavy, varied reuse -
the post's back half (2002 EPA, AOTS, comfort women, Nanjing Massacre,
Yasukuni Shrine) has no directly matching photo, so those stretches
reuse WWII/memorial imagery thematically (e.g. SHRINE for the Yasukuni
Shrine beat, MEMORIAL as the recurring symbol of reconciliation).

MEMORIAL is a tall portrait shot (4480x6720, 0.667 aspect) - letterbox.
The other 5 are all landscape enough (1.44-2.14 aspect) for cover.
"""

IMAGES = {
    "MEMORIAL": "https://upload.wikimedia.org/wikipedia/commons/2/27/Civilian_War_Memorial%2C_Singapore-3276.jpg",
    "ITEMS": "https://upload.wikimedia.org/wikipedia/commons/a/a4/Items_found_in_mass_graves_due_to_the_Sook_Ching_massacre_of_1942_by_the_Japanese.jpg",
    "YAMASHITA": "https://upload.wikimedia.org/wikipedia/commons/4/40/Yamashita_and_Percival_discuss_surrender_terms.jpg",
    "MARCH": "https://upload.wikimedia.org/wikipedia/commons/1/15/JapaneseMarchSgpCity.jpg",
    "SHRINE": "https://upload.wikimedia.org/wikipedia/commons/8/80/Shinto_shrine_in_Shonan_%28Singapore%29_-_194210.jpg",
    "SURRENDER": "https://upload.wikimedia.org/wikipedia/commons/c/c8/Japanese_Surrender_at_Singapore%2C_12_September_1945_A30492.jpg",
}

SLIDES = [
    {"img": "MEMORIAL", "type": "letterbox", "zoom": [1, 1.05, 1.1], "pan": [(0.5, 0.5), (0.5, 0.5), (0.5, 0.5)], "ease": "ease-in-out"},
    {"img": "MEMORIAL", "type": "letterbox", "zoom": [1.1, 1.05, 1], "pan": [(0.5, 0.5), (0.5, 0.5), (0.5, 0.5)], "ease": "ease-out"},
    {"img": "ITEMS", "type": "cover", "zoom": [1, 1.08, 1.15], "pan": [(0.50, 0.45), (0.50, 0.50), (0.50, 0.55)], "ease": "linear"},
    {"img": "YAMASHITA", "type": "cover", "zoom": [1.15, 1.06, 1], "pan": [(0.55, 0.45), (0.50, 0.50), (0.45, 0.55)], "ease": "ease-in"},
    {"img": "MARCH", "type": "cover", "zoom": [1, 1.07, 1.14], "pan": [(0.40, 0.50), (0.50, 0.50), (0.60, 0.50)], "ease": "ease-in-out"},
    {"img": "SHRINE", "type": "cover", "zoom": [1, 1.09, 1.16], "pan": [(0.60, 0.40), (0.50, 0.50), (0.40, 0.60)], "ease": "ease-out"},
    {"img": "SURRENDER", "type": "cover", "zoom": [1.15, 1.07, 1], "pan": [(0.45, 0.55), (0.50, 0.50), (0.55, 0.45)], "ease": "ease-in"},
    {"img": "ITEMS", "type": "cover", "zoom": [1, 1.06, 1.12], "pan": [(0.50, 0.60), (0.50, 0.50), (0.50, 0.40)], "ease": "linear"},
    {"img": "YAMASHITA", "type": "cover", "zoom": [1, 1.08, 1.16], "pan": [(0.55, 0.50), (0.50, 0.50), (0.45, 0.50)], "ease": "ease-in-out"},
    {"img": "MEMORIAL", "type": "letterbox", "zoom": [1, 1.06, 1.12], "pan": [(0.5, 0.5), (0.5, 0.5), (0.5, 0.5)], "ease": "ease-out"},
    {"img": "MEMORIAL", "type": "letterbox", "zoom": [1.12, 1.06, 1], "pan": [(0.5, 0.5), (0.5, 0.5), (0.5, 0.5)], "ease": "ease-in"},
    {"img": "YAMASHITA", "type": "cover", "zoom": [1, 1.09, 1.18], "pan": [(0.60, 0.55), (0.50, 0.50), (0.40, 0.45)], "ease": "ease-in-out"},
    {"img": "MEMORIAL", "type": "letterbox", "zoom": [1, 1.05, 1.1], "pan": [(0.5, 0.5), (0.5, 0.5), (0.5, 0.5)], "ease": "ease-out"},
    {"img": "SURRENDER", "type": "cover", "zoom": [1, 1.06, 1.12], "pan": [(0.50, 0.45), (0.50, 0.50), (0.50, 0.55)], "ease": "ease-in"},
    {"img": "SHRINE", "type": "cover", "zoom": [1.15, 1.06, 1], "pan": [(0.40, 0.50), (0.50, 0.50), (0.60, 0.50)], "ease": "ease-in-out"},
    {"img": "MARCH", "type": "cover", "zoom": [1, 1.08, 1.15], "pan": [(0.55, 0.40), (0.50, 0.50), (0.45, 0.60)], "ease": "ease-out"},
    {"img": "YAMASHITA", "type": "cover", "zoom": [1, 1.07, 1.14], "pan": [(0.45, 0.50), (0.50, 0.50), (0.55, 0.50)], "ease": "ease-in"},
    {"img": "ITEMS", "type": "cover", "zoom": [1.1, 1.05, 1], "pan": [(0.50, 0.55), (0.50, 0.50), (0.50, 0.45)], "ease": "linear"},
    {"img": "MEMORIAL", "type": "letterbox", "zoom": [1, 1.06, 1.12], "pan": [(0.5, 0.5), (0.5, 0.5), (0.5, 0.5)], "ease": "ease-in-out"},
    {"img": "MARCH", "type": "cover", "zoom": [1.15, 1.06, 1], "pan": [(0.55, 0.55), (0.50, 0.50), (0.45, 0.45)], "ease": "ease-out"},
    {"img": "SHRINE", "type": "cover", "zoom": [1, 1.08, 1.16], "pan": [(0.50, 0.60), (0.50, 0.50), (0.50, 0.40)], "ease": "ease-in"},
    {"img": "SHRINE", "type": "cover", "zoom": [1, 1.07, 1.14], "pan": [(0.45, 0.45), (0.50, 0.50), (0.55, 0.55)], "ease": "ease-in-out"},
    {"img": "MEMORIAL", "type": "letterbox", "zoom": [1, 1.05, 1.1], "pan": [(0.5, 0.5), (0.5, 0.5), (0.5, 0.5)], "ease": "ease-out"},
]

# Real values from audio/four-chopsticks-blood-debt-singapore-japan.timing.json,
# re-derived a third time after fixing the "DD Month" date-ordinal
# convention ("25 August" -> "the 25th of August") - same 29
# sentences/order; total duration grew by ~1.2s from the added "the ...
# of" words in 5 dates.
SCHEDULE = [
    (0.0, 0), (5.425, 1), (21.125, 2), (38.325, 3), (50.825, 4),
    (77.625, 5), (88.9, 6), (93.2, 7), (106.775, 8), (120.975, 9),
    (134.4, 10), (157.0, 11), (175.875, 12), (186.375, 13), (215.025, 14),
    (220.1, 15), (245.875, 16), (259.925, 17), (272.225, 18), (279.55, 19),
    (297.95, 20), (309.975, 21), (339.775, 22),
]
TOTAL_DURATION = 362.95
TIMING_JSON = "audio/four-chopsticks-blood-debt-singapore-japan.timing.json"
