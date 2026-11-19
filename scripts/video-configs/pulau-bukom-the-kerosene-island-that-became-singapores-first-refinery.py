"""Video config for the Pulau Bukom post.

The pool is all nineteen pictures from the post and its
gallery: the June 2026 water views of the plant (the hero,
the full sweep, the tank farm, the close tanker, the
moored vessel, the anchored and red tankers, the wharves),
the 2006 panorama, the locator map, the Butterfly kerosene
lantern, the mosque outside and in, the island housing, the
Pasir Panjang ferry terminal inside and at boarding, the
Sentosa dusk view, and the ISS night view of Singapore.
Nineteen pictures for just over thirteen minutes: images
recur at new story beats with varied pans and alternating
zoom direction, never twice in a row.

Named-person rule: the pool holds no portraits, so the
rule is met by construction. Named-place audit: the
locator map sits under the sentence placing the island
southwest of the mainland; the kerosene lantern under the
sentence on importing Russian kerosene for lamps; the
mosque under the sentence naming the mosque among the
town's institutions; the boarding photograph under the
sentences on the instructor ferried in and the Leng
family's commute; the wharves under the sentence on the
Laju hijacked at the Bukom jetty; the ISS night view under
the sentence calling Bukom a lit shore across the water.

Every slide carries its discreet photo title (standing
rule, Chris, 2026-11-11): the short form of its image's
post/gallery caption, drawn small in the top corner on a
soft dark backing for the slide's whole run.

45 slides, 788.025s. No slide over 30s; the
longest is the name-etymology pair at 28.6s. Narration:
Kokoro with the OpenVoice clone. Pronunciation overrides
for the Bukom names filed 2026-11-19, NOT ear-verified yet.
AVATAR: first and last 30s, cartoon with motion.
"""

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

# The channel's 2x2 thumbnail grid, in story order: the
# island plant, the kerosene lantern, the island mosque,
# the night shore from orbit.
THUMBNAIL = [
    {"img": "HERO", "pan": (0.5, 0.5)},
    {"img": "LANTERN", "pan": (0.5, 0.5)},
    {"img": "MASJID", "pan": (0.5, 0.5)},
    {"img": "ISS", "pan": (0.5, 0.5)},
]

_E = "ease-in-out"

SLIDES = [
    {"img": "HERO", **{"type": "cover", "title": "The Bukom refinery skyline from the water", "zoom": [1.0, 1.06, 1.12], "pan": [(0.5, 0.5)] * 3, "ease": _E}},  # 0  s0 title (5.72s)
    {"img": "DUSK", **{"type": "cover", "title": "Pulau Bukom at dusk, from Sentosa", "zoom": [1.12, 1.06, 1.0], "pan": [(0.35, 0.5)] * 3, "ease": _E}},  # 1  s1-2 from the Sentosa waterfront; closed, ferry-only, oil since 1892 (25.85s)
    {"img": "SWEEP", **{"type": "cover", "title": "The full sweep of the Bukom plant", "zoom": [1.0, 1.06, 1.12], "pan": [(0.65, 0.5)] * 3, "ease": _E}},  # 2  s3-4 storage island, town, first refinery; the story in one line (12.80s)
    {"img": "MAP", **{"type": "cover", "title": "Where Bukom sits, southwest of the mainland", "zoom": [1.12, 1.06, 1.0], "pan": [(0.5, 0.4)] * 3, "ease": _E}},  # 3  s5 five and a half kilometres southwest of the mainland (7.50s)
    {"img": "HERO", **{"type": "cover", "title": "The Bukom refinery skyline from the water", "zoom": [1.0, 1.06, 1.12], "pan": [(0.5, 0.5)] * 3, "ease": _E}},  # 4  s6-7 Freshwater Island; the name from rangkek bukom (28.62s)
    {"img": "PANORAMA", **{"type": "cover", "title": "Pulau Bukom in 2006", "zoom": [1.12, 1.06, 1.0], "pan": [(0.35, 0.5)] * 3, "ease": _E}},  # 5  s8-9 Gaggino; the decision taken in London in 1891 (12.47s)
    {"img": "LANTERN", **{"type": "cover", "title": "A Butterfly kerosene pressure lantern", "zoom": [1.0, 1.06, 1.12], "pan": [(0.65, 0.5)] * 3, "ease": _E}},  # 6  s10 Russian kerosene for the region's lamps (16.07s)
    {"img": "TANKFARM", **{"type": "cover", "title": "A tanker alongside the Bukom tank farm", "zoom": [1.12, 1.06, 1.0], "pan": [(0.5, 0.4)] * 3, "ease": _E}},  # 7  s11-12 Syme & Co. build the depot offshore (23.00s)
    {"img": "WHARVES", **{"type": "cover", "title": "The wharves and plant from the water", "zoom": [1.0, 1.06, 1.12], "pan": [(0.5, 0.5)] * 3, "ease": _E}},  # 8  s13-14 the depot's wharf and pipelines; the Murex arrives, 1892 (17.77s)
    {"img": "CLOSE", **{"type": "cover", "title": "A tanker off Bukom, the tank farm behind", "zoom": [1.12, 1.06, 1.0], "pan": [(0.35, 0.5)] * 3, "ease": _E}},  # 9  s15-16 the first depot of its kind in the East (19.38s)
    {"img": "PLANT", **{"type": "cover", "title": "The plant and a moored vessel", "zoom": [1.0, 1.06, 1.12], "pan": [(0.65, 0.5)] * 3, "ease": _E}},  # 10  s17 1897: Shell Transport and Trading (19.00s)
    {"img": "ANCHOR", **{"type": "cover", "title": "Tankers at anchor off Bukom", "zoom": [1.12, 1.06, 1.0], "pan": [(0.5, 0.4)] * 3, "ease": _E}},  # 11  s18 Lee Chim Tuan's stevedores; the flag at half-mast (20.45s)
    {"img": "PANORAMA", **{"type": "cover", "title": "Pulau Bukom in 2006", "zoom": [1.0, 1.06, 1.12], "pan": [(0.5, 0.5)] * 3, "ease": _E}},  # 12  s19-20 sixty tanks by 1942; forty-two torched (15.43s)
    {"img": "HERO", **{"type": "cover", "title": "The Bukom refinery skyline from the water", "zoom": [1.12, 1.06, 1.0], "pan": [(0.35, 0.5)] * 3, "ease": _E}},  # 13  s21-22 the POW camp; repaired by 1950 (20.77s)
    {"img": "WORKERS", **{"type": "cover", "title": "Housing on Pulau Bukom", "zoom": [1.0, 1.06, 1.12], "pan": [(0.65, 0.5)] * 3, "ease": _E}},  # 14  s23-24 not just a tank farm but a town of five thousand (14.20s)
    {"img": "MASJID", **{"type": "cover", "title": "The mosque on Pulau Bukom", "zoom": [1.12, 1.06, 1.0], "pan": [(0.5, 0.4)] * 3, "ease": _E}},  # 15  s25 chapels and a mosque, a temple, schools, a cinema (9.05s)
    {"img": "WORKERS", **{"type": "cover", "title": "Housing on Pulau Bukom", "zoom": [1.0, 1.06, 1.12], "pan": [(0.5, 0.5)] * 3, "ease": _E}},  # 16  s26 rumah putih and rumah merah, the company's quarters (17.45s)
    {"img": "ITIKAF", **{"type": "cover", "title": "Inside the island mosque", "zoom": [1.12, 1.06, 1.0], "pan": [(0.35, 0.5)] * 3, "ease": _E}},  # 17  s27-28 one islander's story: Madi, born and bred on Bukom (13.40s)
    {"img": "CLOSE", **{"type": "cover", "title": "A tanker off Bukom, the tank farm behind", "zoom": [1.0, 1.06, 1.12], "pan": [(0.65, 0.5)] * 3, "ease": _E}},  # 18  s29 resettled to Kaki Bukit in 1961; Fireman 18 (19.40s)
    {"img": "ANCHOR", **{"type": "cover", "title": "Tankers at anchor off Bukom", "zoom": [1.12, 1.06, 1.0], "pan": [(0.5, 0.4)] * 3, "ease": _E}},  # 19  s30-31 the family leaves in the 1990s; the biggest storage centre by 1959 (14.28s)
    {"img": "PANORAMA", **{"type": "cover", "title": "Pulau Bukom in 2006", "zoom": [1.0, 1.06, 1.12], "pan": [(0.5, 0.5)] * 3, "ease": _E}},  # 20  s32-33 a refinery announced; opened 26 July 1961 (21.55s)
    {"img": "SWEEP", **{"type": "cover", "title": "The full sweep of the Bukom plant", "zoom": [1.12, 1.06, 1.0], "pan": [(0.35, 0.5)] * 3, "ease": _E}},  # 21  s34-35 Pioneer Certificate No. 1; $30 million, 20,000 barrels a day (17.35s)
    {"img": "TANKFARM", **{"type": "cover", "title": "A tanker alongside the Bukom tank farm", "zoom": [1.0, 1.06, 1.12], "pan": [(0.65, 0.5)] * 3, "ease": _E}},  # 22  s36-37 four more refineries; growth consumed the island (14.23s)
    {"img": "WHARVES", **{"type": "cover", "title": "The wharves and plant from the water", "zoom": [1.12, 1.06, 1.0], "pan": [(0.5, 0.4)] * 3, "ease": _E}},  # 23  s38 two thousand resettled from Bukom Kechil for crude storage (19.85s)
    {"img": "PLANT", **{"type": "cover", "title": "The plant and a moored vessel", "zoom": [1.0, 1.06, 1.12], "pan": [(0.5, 0.5)] * 3, "ease": _E}},  # 24  s39-40 the 1969 bridge; hills levelled, Pulau Ular reclaimed (16.65s)
    {"img": "WORKERS", **{"type": "cover", "title": "Housing on Pulau Bukom", "zoom": [1.12, 1.06, 1.0], "pan": [(0.35, 0.5)] * 3, "ease": _E}},  # 25  s41-42 twelve hundred remain; the last families hold on (15.20s)
    {"img": "BOARDING", **{"type": "cover", "title": "Boarding the Bukom ferry at Pasir Panjang", "zoom": [1.0, 1.06, 1.12], "pan": [(0.65, 0.5)] * 3, "ease": _E}},  # 26  s43-44 the Leng family; a dance instructor ferried in every Wednesday (20.00s)
    {"img": "TERMINAL", **{"type": "cover", "title": "Inside Pasir Panjang Ferry Terminal", "zoom": [1.12, 1.06, 1.0], "pan": [(0.5, 0.4)] * 3, "ease": _E}},  # 27  s45-46 the move to West Coast, 1997; father and son still commute (14.70s)
    {"img": "PANORAMA", **{"type": "cover", "title": "Pulau Bukom in 2006", "zoom": [1.0, 1.06, 1.12], "pan": [(0.5, 0.5)] * 3, "ease": _E}},  # 28  s47-48 31 January 1974: the Laju attack (24.18s)
    {"img": "WHARVES", **{"type": "cover", "title": "The wharves and plant from the water", "zoom": [1.12, 1.06, 1.0], "pan": [(0.35, 0.5)] * 3, "ease": _E}},  # 29  s49-50 the fire out; the ferryboat Laju hijacked at the jetty (25.65s)
    {"img": "ANCHOR", **{"type": "cover", "title": "Tankers at anchor off Bukom", "zoom": [1.0, 1.06, 1.12], "pan": [(0.65, 0.5)] * 3, "ease": _E}},  # 30  s51-52 the island went back to work; two darker chapters (7.90s)
    {"img": "CLOSE", **{"type": "cover", "title": "A tanker off Bukom, the tank farm behind", "zoom": [1.12, 1.06, 1.0], "pan": [(0.5, 0.4)] * 3, "ease": _E}},  # 31  s53-54 the 2011 fire; thirty hours to put out (23.25s)
    {"img": "REDTANKER", **{"type": "cover", "title": "A red tanker in the Bukom roadstead", "zoom": [1.0, 1.06, 1.12], "pan": [(0.5, 0.5)] * 3, "ease": _E}},  # 32  s55-56 the second chapter: gas oil siphoned and sold at sea (18.38s)
    {"img": "TANKFARM", **{"type": "cover", "title": "A tanker alongside the Bukom tank farm", "zoom": [1.12, 1.06, 1.0], "pan": [(0.35, 0.5)] * 3, "ease": _E}},  # 33  s57-58 350,000 tonnes in court; the masterminds jailed (28.17s)
    {"img": "SWEEP", **{"type": "cover", "title": "The full sweep of the Bukom plant", "zoom": [1.0, 1.06, 1.12], "pan": [(0.65, 0.5)] * 3, "ease": _E}},  # 34  s59 2010: the Eastern Petrochemicals Complex (17.60s)
    {"img": "BIGTANKERS", **{"type": "cover", "title": "Two large tankers in the Bukom roadstead", "zoom": [1.12, 1.06, 1.0], "pan": [(0.5, 0.4)] * 3, "ease": _E}},  # 35  s60 2024: Shell announces the sale (18.88s)
    {"img": "ANCHOR", **{"type": "cover", "title": "Tankers at anchor off Bukom", "zoom": [1.0, 1.06, 1.12], "pan": [(0.5, 0.5)] * 3, "ease": _E}},  # 36  s61 the Aster Energy and Chemicals Park today (22.12s)
    {"img": "TERMINAL", **{"type": "cover", "title": "Inside Pasir Panjang Ferry Terminal", "zoom": [1.12, 1.06, 1.0], "pan": [(0.35, 0.5)] * 3, "ease": _E}},  # 37  s62-63 only the name changed; even the ferry renewed (7.40s)
    {"img": "BOARDING", **{"type": "cover", "title": "Boarding the Bukom ferry at Pasir Panjang", "zoom": [1.0, 1.06, 1.12], "pan": [(0.65, 0.5)] * 3, "ease": _E}},  # 38  s64 fully electric ferries from Pasir Panjang since 2023 (15.78s)
    {"img": "PANORAMA", **{"type": "cover", "title": "Pulau Bukom in 2006", "zoom": [1.12, 1.06, 1.0], "pan": [(0.5, 0.4)] * 3, "ease": _E}},  # 39  s65 the 2024 leaks; Shell charged, case before the courts (20.75s)
    {"img": "HERO", **{"type": "cover", "title": "The Bukom refinery skyline from the water", "zoom": [1.0, 1.06, 1.12], "pan": [(0.5, 0.5)] * 3, "ease": _E}},  # 40  s66-67 the Western Island plan, National Day Rally 2026 (28.05s)
    {"img": "DUSK", **{"type": "cover", "title": "Pulau Bukom at dusk, from Sentosa", "zoom": [1.12, 1.06, 1.0], "pan": [(0.35, 0.5)] * 3, "ease": _E}},  # 41  s68 reinvented once a generation since 1892 (15.12s)
    {"img": "ISS", **{"type": "cover", "title": "Singapore at night, from the space station", "zoom": [1.0, 1.06, 1.12], "pan": [(0.65, 0.5)] * 3, "ease": _E}},  # 42  s69 a lit shore across the water (11.75s)
    {"img": "SWEEP", **{"type": "cover", "title": "The full sweep of the Bukom plant", "zoom": [1.12, 1.06, 1.0], "pan": [(0.5, 0.4)] * 3, "ease": _E}},  # 43  s70-71 the bigger story: it began in 1892 (25.95s)
    {"img": "ISS", **{"type": "cover", "title": "Singapore at night, from the space station", "zoom": [1.0, 1.06, 1.12], "pan": [(0.5, 0.5)] * 3, "ease": _E}},  # 44  s72 the industry's first address, and it has never closed (4.95s)
]

SCHEDULE = [
    (0.000, 0), (5.725, 1), (31.575, 2), (44.375, 3), (51.875, 4), (80.500, 5),
    (92.975, 6), (109.050, 7), (132.050, 8), (149.825, 9), (169.200, 10), (188.200, 11),
    (208.650, 12), (224.075, 13), (244.850, 14), (259.050, 15), (268.100, 16), (285.550, 17),
    (298.950, 18), (318.350, 19), (332.625, 20), (354.175, 21), (371.525, 22), (385.750, 23),
    (405.600, 24), (422.250, 25), (437.450, 26), (457.450, 27), (472.150, 28), (496.325, 29),
    (521.975, 30), (529.875, 31), (553.125, 32), (571.500, 33), (599.675, 34), (617.275, 35),
    (636.150, 36), (658.275, 37), (665.675, 38), (681.450, 39), (702.200, 40), (730.250, 41),
    (745.375, 42), (757.125, 43), (783.075, 44)
]
TOTAL_DURATION = 788.025
TIMING_JSON = "audio/pulau-bukom-the-kerosene-island-that-became-singapores-first-refinery.timing.json"

# The avatar presenter, cartoon with motion: corner bubble for the first and last 30 s.
AVATAR = {"ranges": [(0, 30), (-30, None)], "motion": True}
