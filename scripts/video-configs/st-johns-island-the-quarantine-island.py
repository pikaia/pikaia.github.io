"""Video config for the St John's Island post.

The pool is all fifteen pictures from the post and its
gallery: the three 1909 Wellington photographs of the
quarantine station (from the hill, from the water, and a
station house in the trees), F. R. Sayers' two 1930
photographs of the station at work (the disinfection
buildings; vaccination on landing), Bob Tan's 2022 aerial
of the jetty and his Seringat-Lazarus panorama, and Denis
Barthel's 2023 series of the island today (Pier Beach from
three sides, the downhill path, the northern view, the
water towers, the marine laboratories, and the city seen
across the water). Fifteen pictures for just over
seventeen minutes: images recur at new story beats with
varied pans and alternating zoom direction, never twice
in a row.

Named-person rule: the pool holds no portraits, so the
rule is met by construction. Named-place audit: the
disinfection buildings sit under the muster-shed and
disinfection sentences; the vaccination photograph under
the camps-and-vaccination sentence; the Seringat-Lazarus
panorama under the burial-ground passage (the dead were
moved to Lazarus) and again under the 2006 causeway
sentence; the jetty aerial under the ferry sentence; the
laboratories under the marine-science sentences; the
aquaculture passage takes the island's water towers.

Every slide carries its discreet photo title (standing
rule, Chris, 2026-11-11): the short form of its image's
post/gallery caption, drawn small in the top corner on a
soft dark backing for the slide's whole run.

60 slides, 1028.225s. No slide over 30s; the
longest is the 1935 inventory at 26.27s. Narration:
Kokoro with the OpenVoice clone. Pronunciation overrides
for the island's names filed 2026-11-20, NOT ear-verified
yet. AVATAR: first and last 30s, cartoon with motion.
"""

IMAGES = {
    "HILL": "https://upload.wikimedia.org/wikipedia/commons/9/93/St._John%27s_Island%2C_Singapore%3B_the_Quarantine_Station%2C_Wellcome_V0030663.jpg",
    "SEA": "https://upload.wikimedia.org/wikipedia/commons/6/68/The_Quarantine_Station%2C_St._John%27s_Island%2C_Singapore._Wellcome_V0030662.jpg",
    "HOUSE": "https://upload.wikimedia.org/wikipedia/commons/7/70/The_Quarantine_Station%2C_St._John%27s_Island%2C_Singapore_Wellcome_V0030660.jpg",
    "DISINFECT": "https://upload.wikimedia.org/wikipedia/commons/c/cc/Quarantine_Centre_disinfection_buildings_on_St_John_Island_by_FR_Sayers_%281930%29.jpg",
    "VACCINATE": "https://upload.wikimedia.org/wikipedia/commons/9/9a/Photo_of_vaccination_of_male_passengers_on_St_John_Island_by_FR_Sayers_%281930%29.jpg",
    "JETTY": "https://upload.wikimedia.org/wikipedia/commons/0/0d/St_John%27s_Island_jetty.jpg",
    "PIER": "https://upload.wikimedia.org/wikipedia/commons/a/a6/St._John%27s_Island%2C_Singapore%2C_2023_1.jpg",
    "LAB": "https://upload.wikimedia.org/wikipedia/commons/5/5d/St._John%27s_Island%2C_Singapore%2C_2023_4.jpg",
    "SKYLINE": "https://upload.wikimedia.org/wikipedia/commons/0/0e/St._John%27s_Island%2C_Singapore%2C_2023_3.jpg",
    "BEACH2": "https://upload.wikimedia.org/wikipedia/commons/7/74/St._John%27s_Island%2C_Singapore%2C_2023_2.jpg",
    "DOWNHILL": "https://upload.wikimedia.org/wikipedia/commons/8/86/St._John%27s_Island%2C_Singapore%2C_2023_5.jpg",
    "NORTHVIEW": "https://upload.wikimedia.org/wikipedia/commons/9/91/St._John%27s_Island%2C_Singapore%2C_2023_7.jpg",
    "BEACHWATER": "https://upload.wikimedia.org/wikipedia/commons/4/44/St._John%27s_Island%2C_Singapore%2C_2023_8.jpg",
    "TOWERS": "https://upload.wikimedia.org/wikipedia/commons/4/40/St._John%27s_Island%2C_Singapore%2C_2023_6.jpg",
    "PANO": "https://upload.wikimedia.org/wikipedia/commons/8/8a/St_John%27s_Island_Panorama.jpg",
}

# Every image is captioned in the post or its gallery.
CREDITS = {}

# The channel's 2x2 thumbnail grid, in story order: the
# station in 1909, disinfection in 1930, the jetty today,
# the city across the water.
THUMBNAIL = [
    {"img": "HILL", "pan": (0.5, 0.5)},
    {"img": "DISINFECT", "pan": (0.5, 0.5)},
    {"img": "JETTY", "pan": (0.5, 0.5)},
    {"img": "SKYLINE", "pan": (0.5, 0.5)},
]

_E = "ease-in-out"

SLIDES = [
    {"img": "HILL", **{"type": "cover", "title": "The quarantine station from the hill, 1909", "zoom": [1.0, 1.06, 1.12], "pan": [(0.5, 0.5)] * 3, "ease": _E}},  # 0  s0 title (3.67s),
    {"img": "SEA", **{"type": "cover", "title": "St John's Island from the water, 1909", "zoom": [1.12, 1.06, 1.0], "pan": [(0.35, 0.5)] * 3, "ease": _E}},  # 1  s1 every stranger who came by sea began here (13.57s),
    {"img": "HILL", **{"type": "cover", "title": "The quarantine station from the hill, 1909", "zoom": [1.0, 1.06, 1.12], "pan": [(0.65, 0.5)] * 3, "ease": _E}},  # 2  s2-3 landed, examined, disinfected, held; the largest station in the Empire (20.50s),
    {"img": "JETTY", **{"type": "cover", "title": "The island's jetty from above, 2022", "zoom": [1.12, 1.06, 1.0], "pan": [(0.5, 0.4)] * 3, "ease": _E}},  # 3  s4-5 today: a lodge, laboratories and cats; the island that stood guard (17.62s),
    {"img": "SEA", **{"type": "cover", "title": "St John's Island from the water, 1909", "zoom": [1.0, 1.06, 1.12], "pan": [(0.5, 0.5)] * 3, "ease": _E}},  # 4  s6-7 the doorstep; Raffles' fleet anchors off the island, 28 January 1819 (20.30s),
    {"img": "HOUSE", **{"type": "cover", "title": "A station house among the trees, 1909", "zoom": [1.12, 1.06, 1.0], "pan": [(0.35, 0.5)] * 3, "ease": _E}},  # 5  s8-9 the landing next day; the signal post years (14.30s),
    {"img": "SEA", **{"type": "cover", "title": "St John's Island from the water, 1909", "zoom": [1.0, 1.06, 1.12], "pan": [(0.65, 0.5)] * 3, "ease": _E}},  # 6  s10 Raffles' signal instructions of February 1819 (17.00s),
    {"img": "HOUSE", **{"type": "cover", "title": "A station house among the trees, 1909", "zoom": [1.12, 1.06, 1.0], "pan": [(0.5, 0.4)] * 3, "ease": _E}},  # 7  s11 the flagstaff of 1823, kept in the name Sekijang Bendera (17.65s),
    {"img": "BEACHWATER", **{"type": "cover", "title": "Pier Beach from the water, 2023", "zoom": [1.0, 1.06, 1.12], "pan": [(0.5, 0.5)] * 3, "ease": _E}},  # 8  s12 Lazarus, Sekijang Pelepah, the palm-frond island (13.45s),
    {"img": "BEACH2", **{"type": "cover", "title": "Pier Beach, the landing shore, 2023", "zoom": [1.12, 1.06, 1.0], "pan": [(0.35, 0.5)] * 3, "ease": _E}},  # 9  s13-14 1834: the signal station abandoned, one old inhabitant (14.93s),
    {"img": "HILL", **{"type": "cover", "title": "The quarantine station from the hill, 1909", "zoom": [1.0, 1.06, 1.12], "pan": [(0.65, 0.5)] * 3, "ease": _E}},  # 10  s15-16 it would not stay quiet; the Quarantine Ordinance of 1868 (22.55s),
    {"img": "SEA", **{"type": "cover", "title": "St John's Island from the water, 1909", "zoom": [1.12, 1.06, 1.0], "pan": [(0.5, 0.4)] * 3, "ease": _E}},  # 11  s17-18 merchants grumble; cholera from Bangkok, 1873 (22.00s),
    {"img": "HILL", **{"type": "cover", "title": "The quarantine station from the hill, 1909", "zoom": [1.0, 1.06, 1.12], "pan": [(0.5, 0.5)] * 3, "ease": _E}},  # 12  s19-21 shipboard orders not enough; Ellis proposes the lazaretto (21.38s),
    {"img": "HOUSE", **{"type": "cover", "title": "A station house among the trees, 1909", "zoom": [1.12, 1.06, 1.0], "pan": [(0.35, 0.5)] * 3, "ease": _E}},  # 13  s22 approved, announced 21 March 1874 (8.97s),
    {"img": "HILL", **{"type": "cover", "title": "The quarantine station from the hill, 1909", "zoom": [1.0, 1.06, 1.12], "pan": [(0.65, 0.5)] * 3, "ease": _E}},  # 14  s23 November 1874: the cholera ship Milton, the first intake (19.35s),
    {"img": "PANO", **{"type": "cover", "title": "Seringat and Lazarus Islands from the air, 2022", "zoom": [1.12, 1.06, 1.0], "pan": [(0.5, 0.4)] * 3, "ease": _E}},  # 15  s24-25 the burial ground: Cheang Hong Lim's objection over Kusu (22.57s),
    {"img": "SEA", **{"type": "cover", "title": "St John's Island from the water, 1909", "zoom": [1.0, 1.06, 1.12], "pan": [(0.5, 0.5)] * 3, "ease": _E}},  # 16  s26 the dead buried instead on Lazarus (10.57s),
    {"img": "HOUSE", **{"type": "cover", "title": "A station house among the trees, 1909", "zoom": [1.12, 1.06, 1.0], "pan": [(0.35, 0.5)] * 3, "ease": _E}},  # 17  s27-28 the routine: infected and suspected ships (13.30s),
    {"img": "DISINFECT", **{"type": "cover", "title": "The disinfection buildings, 1930", "zoom": [1.0, 1.06, 1.12], "pan": [(0.65, 0.5)] * 3, "ease": _E}},  # 18  s29 muster sheds, steamed clothes, disinfection (17.18s),
    {"img": "VACCINATE", **{"type": "cover", "title": "Vaccination on landing, 1930", "zoom": [1.12, 1.06, 1.0], "pan": [(0.5, 0.4)] * 3, "ease": _E}},  # 19  s30-31 ships fumigated with sulphur; the camps, vaccination for everyone (21.38s),
    {"img": "HOUSE", **{"type": "cover", "title": "A station house among the trees, 1909", "zoom": [1.0, 1.06, 1.12], "pan": [(0.5, 0.5)] * 3, "ease": _E}},  # 20  s32-33 the class system: cabin passengers walk ashore (16.93s),
    {"img": "SEA", **{"type": "cover", "title": "St John's Island from the water, 1909", "zoom": [1.12, 1.06, 1.0], "pan": [(0.35, 0.5)] * 3, "ease": _E}},  # 21  s34 Haj pilgrims: the Queen Margaret, 1890 (23.05s),
    {"img": "DISINFECT", **{"type": "cover", "title": "The disinfection buildings, 1930", "zoom": [1.0, 1.06, 1.12], "pan": [(0.65, 0.5)] * 3, "ease": _E}},  # 22  s35 the diseases: cholera, smallpox, plague (24.20s),
    {"img": "HOUSE", **{"type": "cover", "title": "A station house among the trees, 1909", "zoom": [1.12, 1.06, 1.0], "pan": [(0.5, 0.4)] * 3, "ease": _E}},  # 23  s36 chickenpox, measles and beri-beri too (4.78s),
    {"img": "HILL", **{"type": "cover", "title": "The quarantine station from the hill, 1909", "zoom": [1.0, 1.06, 1.12], "pan": [(0.5, 0.5)] * 3, "ease": _E}},  # 24  s37 from attap huts to a station covering the island (17.05s),
    {"img": "SEA", **{"type": "cover", "title": "St John's Island from the water, 1909", "zoom": [1.12, 1.06, 1.0], "pan": [(0.35, 0.5)] * 3, "ease": _E}},  # 25  s38 the 1935 inventory of the place (26.27s),
    {"img": "HILL", **{"type": "cover", "title": "The quarantine station from the hill, 1909", "zoom": [1.0, 1.06, 1.12], "pan": [(0.65, 0.5)] * 3, "ease": _E}},  # 26  s39-40 6,000 people in 22 camps; 8 million inspected, 1903-1923 (22.15s),
    {"img": "HOUSE", **{"type": "cover", "title": "A station house among the trees, 1909", "zoom": [1.12, 1.06, 1.0], "pan": [(0.5, 0.4)] * 3, "ease": _E}},  # 27  s41-42 the Wembley model; the largest in the Empire (24.60s),
    {"img": "SEA", **{"type": "cover", "title": "St John's Island from the water, 1909", "zoom": [1.0, 1.06, 1.12], "pan": [(0.5, 0.5)] * 3, "ease": _E}},  # 28  s43-44 the official view was sunny: five blissful days (20.27s),
    {"img": "HOUSE", **{"type": "cover", "title": "A station house among the trees, 1909", "zoom": [1.12, 1.06, 1.0], "pan": [(0.35, 0.5)] * 3, "ease": _E}},  # 29  s45-46 the oral histories; Teo Choon Hong, 1937 (17.15s),
    {"img": "HILL", **{"type": "cover", "title": "The quarantine station from the hill, 1909", "zoom": [1.0, 1.06, 1.12], "pan": [(0.65, 0.5)] * 3, "ease": _E}},  # 30  s47-49 the cabins did not have to go; bossed around like chickens and ducks (13.25s),
    {"img": "SEA", **{"type": "cover", "title": "St John's Island from the water, 1909", "zoom": [1.12, 1.06, 1.0], "pan": [(0.5, 0.4)] * 3, "ease": _E}},  # 31  s50 Teong Eng Siong, 1948, remembered it mildly (18.70s),
    {"img": "HOUSE", **{"type": "cover", "title": "A station house among the trees, 1909", "zoom": [1.0, 1.06, 1.12], "pan": [(0.5, 0.5)] * 3, "ease": _E}},  # 32  s51-52 Saravana Perumal: the centipedes, and his return as staff (25.18s),
    {"img": "HILL", **{"type": "cover", "title": "The quarantine station from the hill, 1909", "zoom": [1.12, 1.06, 1.0], "pan": [(0.35, 0.5)] * 3, "ease": _E}},  # 33  s53-54 never quarantine only: German internees of the First World War (18.03s),
    {"img": "SEA", **{"type": "cover", "title": "St John's Island from the water, 1909", "zoom": [1.0, 1.06, 1.12], "pan": [(0.65, 0.5)] * 3, "ease": _E}},  # 34  s55 the Second World War repeats the pattern (19.82s),
    {"img": "HOUSE", **{"type": "cover", "title": "A station house among the trees, 1909", "zoom": [1.12, 1.06, 1.0], "pan": [(0.5, 0.4)] * 3, "ease": _E}},  # 35  s56-57 the moon gate; Emergency detention from 1948 (26.23s),
    {"img": "HILL", **{"type": "cover", "title": "The quarantine station from the hill, 1909", "zoom": [1.0, 1.06, 1.12], "pan": [(0.5, 0.5)] * 3, "ease": _E}},  # 36  s58 Devan Nair and St John's University; Lee Kuan Yew's 1952 visit (17.02s),
    {"img": "SEA", **{"type": "cover", "title": "St John's Island from the water, 1909", "zoom": [1.12, 1.06, 1.0], "pan": [(0.35, 0.5)] * 3, "ease": _E}},  # 37  s59 Operation Coldstore, 1963: 99 of 113 to the island (19.10s),
    {"img": "HOUSE", **{"type": "cover", "title": "A station house among the trees, 1909", "zoom": [1.0, 1.06, 1.12], "pan": [(0.65, 0.5)] * 3, "ease": _E}},  # 38  s60-61 the other cure: 16,000 opium addicts, 1,400 dens (20.25s),
    {"img": "HILL", **{"type": "cover", "title": "The quarantine station from the hill, 1909", "zoom": [1.12, 1.06, 1.0], "pan": [(0.5, 0.4)] * 3, "ease": _E}},  # 39  s62 February 1955: the Opium Treatment Centre opens (14.88s),
    {"img": "SEA", **{"type": "cover", "title": "St John's Island from the water, 1909", "zoom": [1.0, 1.06, 1.12], "pan": [(0.5, 0.5)] * 3, "ease": _E}},  # 40  s63 the regime in phases: withdrawal, rehabilitation, follow-up (17.93s),
    {"img": "HOUSE", **{"type": "cover", "title": "A station house among the trees, 1909", "zoom": [1.12, 1.06, 1.0], "pan": [(0.35, 0.5)] * 3, "ease": _E}},  # 41  s64-65 4,000 treated by 1966; the first Drug Rehabilitation Centre, 1973 (20.05s),
    {"img": "BEACH2", **{"type": "cover", "title": "Pier Beach, the landing shore, 2023", "zoom": [1.0, 1.06, 1.12], "pan": [(0.65, 0.5)] * 3, "ease": _E}},  # 42  s66 1975: South Vietnamese refugees, the last intake (9.88s),
    {"img": "SEA", **{"type": "cover", "title": "St John's Island from the water, 1909", "zoom": [1.12, 1.06, 1.0], "pan": [(0.5, 0.4)] * 3, "ease": _E}},  # 43  s67-68 quarantine dies by stages: the aeroplane and the health certificate (19.35s),
    {"img": "HILL", **{"type": "cover", "title": "The quarantine station from the hill, 1909", "zoom": [1.0, 1.06, 1.12], "pan": [(0.5, 0.5)] * 3, "ease": _E}},  # 44  s69 14 January 1976: the station closes (9.72s),
    {"img": "BEACH2", **{"type": "cover", "title": "Pier Beach, the landing shore, 2023", "zoom": [1.12, 1.06, 1.0], "pan": [(0.35, 0.5)] * 3, "ease": _E}},  # 45  s70 the islanders relocated to the mainland (21.73s),
    {"img": "NORTHVIEW", **{"type": "cover", "title": "The northern view from the island, 2023", "zoom": [1.0, 1.06, 1.12], "pan": [(0.65, 0.5)] * 3, "ease": _E}},  # 46  s71-72 the last residents leave in 2017; the detention centre that was never used (25.62s),
    {"img": "JETTY", **{"type": "cover", "title": "The island's jetty from above, 2022", "zoom": [1.12, 1.06, 1.0], "pan": [(0.5, 0.4)] * 3, "ease": _E}},  # 47  s73 the afterlife: a subsidised holiday camp, 1976 (15.32s),
    {"img": "PIER", **{"type": "cover", "title": "Pier Beach, 2023", "zoom": [1.0, 1.06, 1.12], "pan": [(0.5, 0.5)] * 3, "ease": _E}},  # 48  s74 the St John's Island Lodge in the old camps (13.80s),
    {"img": "JETTY", **{"type": "cover", "title": "The island's jetty from above, 2022", "zoom": [1.12, 1.06, 1.0], "pan": [(0.35, 0.5)] * 3, "ease": _E}},  # 49  s75 ferries from Marina South Pier; the jetty closed, landing at Seringat (17.50s),
    {"img": "PANO", **{"type": "cover", "title": "Seringat and Lazarus Islands from the air, 2022", "zoom": [1.0, 1.06, 1.12], "pan": [(0.65, 0.5)] * 3, "ease": _E}},  # 50  s76 2006: the causeway joins St John's to Lazarus (16.57s),
    {"img": "LAB", **{"type": "cover", "title": "The marine laboratories, 2023", "zoom": [1.12, 1.06, 1.0], "pan": [(0.5, 0.4)] * 3, "ease": _E}},  # 51  s77-78 science moves in: the National Marine Laboratory, 2016 (24.12s),
    {"img": "TOWERS", **{"type": "cover", "title": "The water towers at the island's centre, 2023", "zoom": [1.0, 1.06, 1.12], "pan": [(0.5, 0.5)] * 3, "ease": _E}},  # 52  s79 the Marine Aquaculture Centre, breeding food fish (9.15s),
    {"img": "BEACHWATER", **{"type": "cover", "title": "Pier Beach from the water, 2023", "zoom": [1.12, 1.06, 1.0], "pan": [(0.35, 0.5)] * 3, "ease": _E}},  # 53  s80 the western reefs inside the Sisters' Islands Marine Park (17.25s),
    {"img": "BEACH2", **{"type": "cover", "title": "Pier Beach, the landing shore, 2023", "zoom": [1.0, 1.06, 1.12], "pan": [(0.65, 0.5)] * 3, "ease": _E}},  # 54  s81-82 and then there are the cats: over a hundred in 2014 (12.10s),
    {"img": "DOWNHILL", **{"type": "cover", "title": "Downhill to the beach, 2023", "zoom": [1.12, 1.06, 1.0], "pan": [(0.5, 0.4)] * 3, "ease": _E}},  # 55  s83 sterilised, aged, thinned; cared for by volunteers (16.57s),
    {"img": "SKYLINE", **{"type": "cover", "title": "Singapore from St John's Island, 2023", "zoom": [1.0, 1.06, 1.12], "pan": [(0.5, 0.5)] * 3, "ease": _E}},  # 56  s84 the island's story ends, for now (12.28s),
    {"img": "SEA", **{"type": "cover", "title": "St John's Island from the water, 1909", "zoom": [1.12, 1.06, 1.0], "pan": [(0.35, 0.5)] * 3, "ease": _E}},  # 57  s85 the bigger story: the island posts face outward; this one faced inward (8.97s),
    {"img": "SKYLINE", **{"type": "cover", "title": "Singapore from St John's Island, 2023", "zoom": [1.0, 1.06, 1.12], "pan": [(0.65, 0.5)] * 3, "ease": _E}},  # 58  s86 the filter every newcomer passed through (15.50s),
    {"img": "JETTY", **{"type": "cover", "title": "The island's jetty from above, 2022", "zoom": [1.12, 1.06, 1.0], "pan": [(0.5, 0.4)] * 3, "ease": _E}},  # 59  s87 the door has closed; the doorstep remains (3.65s),
]

SCHEDULE = [
    (0.000, 0), (3.675, 1), (17.250, 2),
    (37.750, 3), (55.375, 4), (75.675, 5),
    (89.975, 6), (106.975, 7), (124.625, 8),
    (138.075, 9), (153.000, 10), (175.550, 11),
    (197.550, 12), (218.925, 13), (227.900, 14),
    (247.250, 15), (269.825, 16), (280.400, 17),
    (293.700, 18), (310.875, 19), (332.250, 20),
    (349.175, 21), (372.225, 22), (396.425, 23),
    (401.200, 24), (418.250, 25), (444.525, 26),
    (466.675, 27), (491.275, 28), (511.550, 29)
]
TOTAL_DURATION = 1028.225
TIMING_JSON = "audio/st-johns-island-the-quarantine-island.timing.json"

# The avatar presenter, cartoon with motion: corner bubble for the first and last 30 s.
AVATAR = {"ranges": [(0, 30), (-30, None)], "motion": True}
