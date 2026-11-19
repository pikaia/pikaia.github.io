"""Short config for the Pulau Bukom post - a synopsis re-cut.

Built with: python scripts/build_short_audio.py pulau-bukom-the-kerosene-island-that-became-singapores-first-refinery 2,3,6,14,20,24,33,38,47,57,61,67,72
(13 sentences, 170.78s - under the 3-minute Shorts ceiling
with margin, and well over TikTok's 1-minute floor.)

The post's points, and the sentences that carry each:
1. The island today: closed, reached by a workers' ferry, handling oil since 1892. (s2)
2. Its arc in one line: storage island, town of five thousand, first refinery. (s3)
3. Before oil: a mangrove freshwater island. (s6)
4. 1892: the Murex lands the first shipment at the first depot of its kind in the East. (s14)
5. 1942: the British torched forty-two tanks; a POW camp followed. (s20)
6. The town of five thousand, with its mosque, schools and cinema. (s24)
7. 1961: Pioneer Certificate No. 1 - Singapore's first refinery opens. (s33)
8. The emptying: some two thousand resettled; the workers become ferry commuters. (s38)
9. 1974: the Laju attack, Singapore's first encounter with international terrorism. (s47)
10. The great theft: over 350,000 tonnes of gas oil, over S$200 million. (s57)
11. 2025: Shell sells; the island trades as the Aster Energy and Chemicals Park. (s61)
12. The future: the Western Island plan. (s67)
13. The close: the industry's first address, and it has never closed. (s72)

Every slide is letterboxed and carries its photo title, as
in the main config. The pool holds no portraits, so the
named-person rule is met by construction.
"""

WIDTH, HEIGHT = 1080, 1920

IMAGES = {
    "HERO": "https://upload.wikimedia.org/wikipedia/commons/e/e0/Pulau_Bukom_June_2026.jpg",
    "MAP": "https://upload.wikimedia.org/wikipedia/commons/b/b5/Pulau_Bukum_locator_map.png",
    "LANTERN": "https://upload.wikimedia.org/wikipedia/commons/9/94/Butterfly_Lantern_%28front_view%29.jpg",
    "MASJID": "https://upload.wikimedia.org/wikipedia/commons/2/28/Masjid_in_Pulau_Bukom%2C_or_Bukom_Island.jpg",
    "PANORAMA": "https://upload.wikimedia.org/wikipedia/commons/0/02/Pulau_Bukom%2C_panorama%2C_Nov_06.jpg",
    "WORKERS": "https://upload.wikimedia.org/wikipedia/commons/d/de/Worker_accommodations_on_Pulau_Bukom.jpg",
    "CLOSE": "https://upload.wikimedia.org/wikipedia/commons/9/9c/Pulau_Bukom_20260620_152408.jpg",
    "BOARDING": "https://upload.wikimedia.org/wikipedia/commons/2/2e/Pasir_Panjang_Ferry_Terminal_20260620_124930.jpg",
    "ISS": "https://upload.wikimedia.org/wikipedia/commons/d/d8/ISS041-E-4927_-_View_of_Singapore.jpg",
    "SWEEP": "https://upload.wikimedia.org/wikipedia/commons/5/59/Pulau_Bukom_20260620_152913.jpg",
    "TANKFARM": "https://upload.wikimedia.org/wikipedia/commons/5/5a/Pulau_Bukom_20260620_152517.jpg",
    "PLANT": "https://upload.wikimedia.org/wikipedia/commons/c/c4/Pulau_Bukom_20260620_152757.jpg",
    "ANCHOR": "https://upload.wikimedia.org/wikipedia/commons/f/fe/Pulau_Bukom_20260620_152307.jpg",
    "BIGTANKERS": "https://upload.wikimedia.org/wikipedia/commons/5/5d/Pulau_Bukom_20260620_134005.jpg",
    "REDTANKER": "https://upload.wikimedia.org/wikipedia/commons/e/e5/Pulau_Bukom_20260620_130617.jpg",
    "WHARVES": "https://upload.wikimedia.org/wikipedia/commons/6/60/Pulau_Bukom_20260620_133645.jpg",
    "TERMINAL": "https://upload.wikimedia.org/wikipedia/commons/e/ea/Pasir_Panjang_Ferry_Terminal_20260620_160035.jpg",
    "DUSK": "https://upload.wikimedia.org/wikipedia/commons/f/f5/Pulau_Bukom_from_Sentosa.JPG",
    "ITIKAF": "https://upload.wikimedia.org/wikipedia/commons/5/50/Itikaf_area_inside_mosque_at_Pulau_Bukom.jpg",
}

# Every image is captioned in the post or its gallery.
CREDITS = {}

# The main video's thumbnail grid, re-panned for tall cells.
THUMBNAIL = [
    {"img": "HERO", "pan": (0.5, 0.5)},
    {"img": "LANTERN", "pan": (0.5, 0.5)},
    {"img": "MASJID", "pan": (0.5, 0.5)},
    {"img": "ISS", "pan": (0.5, 0.5)},
]

_E = "ease-in-out"
_LB = {"type": "letterbox", "zoom": [1.0, 1.03, 1.06], "pan": [(0.5, 0.5)] * 3, "ease": _E}

SLIDES = [
    {"img": "DUSK", **_LB, "title": "Pulau Bukom at dusk, from Sentosa"},   # s2 closed to the public, ferry-only, oil since 1892 (15.82s)
    {"img": "SWEEP", **_LB, "title": "The full sweep of the Bukom plant"},   # s3 storage island, town of five thousand, first refinery (7.30s)
    {"img": "HERO", **_LB, "title": "The Bukom refinery skyline from the water"},   # s6 Freshwater Island, before oil (10.60s)
    {"img": "LANTERN", **_LB, "title": "A Butterfly kerosene pressure lantern"},   # s14 1892: the Murex, first depot of its kind in the East (8.00s)
    {"img": "PANORAMA", **_LB, "title": "Pulau Bukom in 2006"},   # s20 1942: forty-two tanks torched; a POW camp (9.22s)
    {"img": "WORKERS", **_LB, "title": "Housing on Pulau Bukom"},   # s24 a town of five thousand: mosque, schools, cinema (9.05s)
    {"img": "TANKFARM", **_LB, "title": "A tanker alongside the Bukom tank farm"},   # s33 1961: Pioneer Certificate No. 1, the first refinery (17.12s)
    {"img": "WHARVES", **_LB, "title": "The wharves and plant from the water"},   # s38 the emptying: two thousand resettled (19.85s)
    {"img": "CLOSE", **_LB, "title": "A tanker off Bukom, the tank farm behind"},   # s47 1974: the Laju attack (9.55s)
    {"img": "REDTANKER", **_LB, "title": "A red tanker in the Bukom roadstead"},   # s57 the great theft: 350,000 tonnes, over $200 million (12.32s)
    {"img": "BIGTANKERS", **_LB, "title": "Two large tankers in the Bukom roadstead"},   # s61 2025: sold - the Aster Energy and Chemicals Park (22.12s)
    {"img": "MAP", **_LB, "title": "Where Bukom sits, southwest of the mainland"},   # s67 the Western Island plan (24.85s)
    {"img": "ISS", **_LB, "title": "Singapore at night, from the space station"},   # s72 the industry's first address, never closed (4.95s)
]
SCHEDULE = [
    (0.000, 0), (15.825, 1), (23.125, 2), (33.725, 3), (41.725, 4), (50.950, 5),
    (60.000, 6), (77.125, 7), (96.975, 8), (106.525, 9), (118.850, 10), (140.975, 11),
    (165.825, 12)
]
TOTAL_DURATION = 170.775
TIMING_JSON = "audio/pulau-bukom-the-kerosene-island-that-became-singapores-first-refinery-short.timing.json"

BURN_CAPTIONS = True
CAPTION_FONT_RATIO = 0.032
CAPTION_MAX_WIDTH_FRAC = 0.86
CAPTION_Y_FRAC = 0.70

# The avatar presenter, cartoon with motion: corner bubble for the first and last 30 s.
AVATAR = {"ranges": [(0, 30), (-30, None)], "motion": True}
