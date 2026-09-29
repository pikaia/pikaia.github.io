"""Video config for the vanished-hills post.

The island relief map (scripts/render_hills_maps.py) opens the terrain section
and zooms into the city-centre box on "the waterfront was hilly too"; the four
downtown stage maps (1880s, from 1884, 1905-1932, today) are frozen letterbox
slides timed to each hill's section, and the timeline (render_hills_timeline_chart.py)
is frozen too. Named people get their own portrait (Nathaniel Wallich, Hoo Ah
Kay) or no one (Raffles, John Palmer: painting/hill instead). The Straits Times
Weekly Issue of 22 Nov 1884 is zoomed to the blast report; the 1893 city plan
to the labelled hills.

38 slides, one per sentence.
"""

CREDITS = {
    "TIMELINE": "Chart by Lesser Known Singapore, figures per the post's own Sources list",
    "ISLAND": "Map by Lesser Known Singapore; elevation data from Terrain Tiles (AWS), derived from NASA SRTM",
    "DT0": "Map by Lesser Known Singapore; map data (c) OpenStreetMap contributors",
    "DT1": "Map by Lesser Known Singapore; map data (c) OpenStreetMap contributors",
    "DT2": "Map by Lesser Known Singapore; map data (c) OpenStreetMap contributors",
    "DT3": "Map by Lesser Known Singapore; map data (c) OpenStreetMap contributors",
}

IMAGES = {
    "ANNSIANG": "https://upload.wikimedia.org/wikipedia/commons/thumb/e/e9/Ann_Siang_Hill_Park%2C_Singapore_%28P1100992%29.jpg/1920px-Ann_Siang_Hill_Park%2C_Singapore_%28P1100992%29.jpg",
    "ANNSIANG2": "https://upload.wikimedia.org/wikipedia/commons/thumb/8/88/Ann_Siang_Hill_from_Club_Street.jpg/1920px-Ann_Siang_Hill_from_Club_Street.jpg",
    "ANSON": "https://upload.wikimedia.org/wikipedia/commons/thumb/8/8a/KITLV_-_79926_-_Kleingrothe%2C_C.J._-_Medan_-_Anson_Road%2C_Singapore_-_circa_1910.tif/lossy-page1-1920px-KITLV_-_79926_-_Kleingrothe%2C_C.J._-_Medan_-_Anson_Road%2C_Singapore_-_circa_1910.tif.jpg",
    "C1893": "https://upload.wikimedia.org/wikipedia/commons/thumb/1/18/Plan_map_of_the_City_of_Singapore_of_British_Malaya%2C_from_the_Constable%27s_Hand_Atlas_of_India_%281893%29.jpg/1920px-Plan_map_of_the_City_of_Singapore_of_British_Malaya%2C_from_the_Constable%27s_Hand_Atlas_of_India_%281893%29.jpg",
    "CARPENTER": "https://upload.wikimedia.org/wikipedia/commons/thumb/9/96/At_National_Museum_of_Singapore_2023_067.jpg/1920px-At_National_Museum_of_Singapore_2023_067.jpg",
    "DOCKPANO": "https://upload.wikimedia.org/wikipedia/commons/thumb/0/02/Gezicht_op_gebouwen_en_de_omgeving_van_de_Tanjong_Pagar_Dock_Co._Ltd._in_Singapore_Panorama_of_five_sheets_taken_from_manager%27s_bungalow_%28titel_op_object%29%2C_RP-F-F01140-AA.jpg/1920px-thumbnail.jpg",
    "DT0": "/assets/images/hills-downtown-0.png",
    "DT1": "/assets/images/hills-downtown-1.png",
    "DT2": "/assets/images/hills-downtown-2.png",
    "DT3": "/assets/images/hills-downtown-3.png",
    "HABIBTOMB": "https://upload.wikimedia.org/wikipedia/commons/thumb/8/80/Habib_Noh_Tomb_on_Mount_Palmer.jpg/1920px-Habib_Noh_Tomb_on_Mount_Palmer.jpg",
    "ISLAND": "/assets/images/hills-island.png",
    "KNOLL": "https://upload.wikimedia.org/wikipedia/commons/thumb/1/11/Keramat_Habib_Noh_and_remains_of_former_Mount_Palmer.jpg/1920px-Keramat_Habib_Noh_and_remains_of_former_Mount_Palmer.jpg",
    "PALMERFOOT": "https://upload.wikimedia.org/wikipedia/commons/thumb/1/13/Strand_en_badgasten_aan_de_voet_van_Mount_Palmer_%28Mount_Parsee%2C_Parsee_Hill%29_bij_Singapore_Foot_of_Mount_Palmer._S.pore_%28titel_op_object%29%2C_RP-F-F01104-Z.jpg/1920px-Strand_en_badgasten_aan_de_voet_van_Mount_Palmer_%28Mount_Parsee%2C_Parsee_Hill%29_bij_Singapore_Foot_of_Mount_Palmer._S.pore_%28titel_op_object%29%2C_RP-F-F01104-Z.jpg",
    "ROADTP": "https://upload.wikimedia.org/wikipedia/commons/thumb/a/a8/Singapore._Road_to_Tanjong_Pagar_%28NYPL_Hades-2359714-4044479%29.jpg/1920px-Singapore._Road_to_Tanjong_Pagar_%28NYPL_Hades-2359714-4044479%29.jpg",
    "ROADTP2": "https://upload.wikimedia.org/wikipedia/commons/thumb/8/8b/Singapore._Road_to_Tanjong_Pagar.%2C_KITLV_1404883.tiff/lossy-page1-1920px-Singapore._Road_to_Tanjong_Pagar.%2C_KITLV_1404883.tiff.jpg",
    "ST84": "/assets/images/straits-times-weekly-1884-11-22-page-5.jpg",
    "TIMELINE": "/assets/images/hills-timeline-chart.png",
    "TPROAD": "https://upload.wikimedia.org/wikipedia/commons/thumb/6/6a/KITLV_-_79925_-_Kleingrothe%2C_C.J._-_Medan_-_Tanjong_Pagar_Road_in_Singapore_-_circa_1910.tif/lossy-page1-1920px-KITLV_-_79925_-_Kleingrothe%2C_C.J._-_Medan_-_Tanjong_Pagar_Road_in_Singapore_-_circa_1910.tif.jpg",
    "WALLICH": "https://upload.wikimedia.org/wikipedia/commons/thumb/8/86/Nathaniel_Wallich._Lithograph_by_E._U._Eddis%2C_1830._Wellcome_V0006127.jpg/1920px-Nathaniel_Wallich._Lithograph_by_E._U._Eddis%2C_1830._Wellcome_V0006127.jpg",
    "WHAMPOA": "https://upload.wikimedia.org/wikipedia/commons/thumb/7/7b/The_Hon._Hoh-Ah-Kay_Whampoa%2C_C.M.G.%2C_M.L.C.%2C_and_Consul_for_Wellcome_V0037527.jpg/1280px-The_Hon._Hoh-Ah-Kay_Whampoa%2C_C.M.G.%2C_M.L.C.%2C_and_Consul_for_Wellcome_V0037527.jpg",
}

_P0 = {"type": "cover", "zoom": [1.0, 1.05, 1.1], "pan": [(0.3, 0.5), (0.5, 0.5), (0.7, 0.5)], "ease": "ease-in-out"}
_P1 = {"type": "letterbox", "zoom": [1.0, 1.0, 1.0], "pan": [(0.5, 0.5)] * 3, "ease": "linear"}
_P2 = {"type": "cover", "zoom": [1.0, 1.9, 3.2], "pan": [(0.5, 0.5), (0.56, 0.7), (0.57, 0.76)], "ease": "ease-in-out"}
_P3 = {"type": "cover", "zoom": [1.1, 1.05, 1.0], "pan": [(0.7, 0.5), (0.5, 0.5), (0.3, 0.5)], "ease": "ease-in-out"}
_P4 = {"type": "cover", "zoom": [3.00, 3.07, 3.15], "pan": [(0.455, 0.79), (0.456, 0.801), (0.456, 0.812)], "ease": "ease-in-out"}
_P5 = {"type": "cover", "zoom": [2.60, 2.67, 2.73], "pan": [(0.451, 0.805), (0.452, 0.816), (0.453, 0.827)], "ease": "ease-in-out"}
_P6 = {"type": "cover", "zoom": [1.35, 1.4, 1.45], "pan": [(0.5, 0.5), (0.5, 0.5), (0.5, 0.5)], "ease": "ease-in-out"}
_P7 = {"type": "cover", "zoom": [2.80, 2.87, 2.94], "pan": [(0.236, 0.945), (0.239, 0.955), (0.242, 0.965)], "ease": "ease-in-out"}
_P8 = {"type": "cover", "zoom": [2.60, 2.67, 2.73], "pan": [(0.272, 0.918), (0.276, 0.928), (0.279, 0.938)], "ease": "ease-in-out"}
_P9 = {"type": "cover", "zoom": [2.60, 2.67, 2.73], "pan": [(0.662, 0.058), (0.66, 0.072), (0.658, 0.085)], "ease": "ease-in-out"}
_P10 = {"type": "cover", "zoom": [1.0, 1.03, 1.06], "pan": [(0.5, 0.25), (0.5, 0.28), (0.5, 0.31)], "ease": "ease-in-out"}

SLIDES = [
    {"img": "PALMERFOOT", **_P0},  # s0 The Hills Singapore Dug Into the Sea
    {"img": "DT0", **_P1},  # s1 In the 1880s, three hills stood along the wa
    {"img": "DT3", **_P1},  # s2 Within fifty years, Mount Wallich and most o
    {"img": "KNOLL", **_P0},  # s3 Today the only reminders are a few street na
    {"img": "ISLAND", **_P1},  # s4 Singapore is not flat.
    {"img": "ISLAND", **_P1},  # s5 Its highest point, Bukit Timah Hill, rises t
    {"img": "ISLAND", **_P2},  # s6 In the early town, the waterfront to the sou
    {"img": "DT0", **_P1},  # s7 They sat close to the sea at a time when the
    {"img": "CARPENTER", **_P0},  # s8 The smallest story belongs to Mount Wallich.
    {"img": "WALLICH", **_P1},  # s9 In 1822 the Danish botanist Nathaniel Wallic
    {"img": "CARPENTER", **_P3},  # s10 During his stay Stamford Raffles persuaded h
    {"img": "C1893", **_P4},  # s11 Mount Erskine stood to the north of it, behi
    {"img": "C1893", **_P5},  # s12 It lasted longer than its neighbour: the Str
    {"img": "ANNSIANG2", **_P0},  # s13 Beside it was Ann Siang Hill, which still su
    {"img": "PALMERFOOT", **_P3},  # s14 Mount Palmer was the largest of the three, a
    {"img": "PALMERFOOT", **_P6},  # s15 It was named after John Palmer, a Calcutta m
    {"img": "C1893", **_P7},  # s16 When his business ran into trouble, he sold 
    {"img": "DOCKPANO", **_P0},  # s17 Part of it overlooking the harbour was forti
    {"img": "WHAMPOA", **_P1},  # s18 Its later owners included Hoo Ah Kay, the me
    {"img": "DT0", **_P1},  # s19 The Telok Ayer reclamation, begun in 1879, n
    {"img": "ST84", **_P8},  # s20 On a Thursday evening in November 1884, acco
    {"img": "ST84", **_P9},  # s21 The explosion made the ground tremble for so
    {"img": "DT1", **_P1},  # s22 The hill was taken down over the following y
    {"img": "TPROAD", **_P0},  # s23 Wallich Street, named in 1899, runs across t
    {"img": "ROADTP", **_P0},  # s24 The hills were also in the way.
    {"img": "ROADTP2", **_P0},  # s25 Goods from the docks at Tanjong Pagar had to
    {"img": "DT2", **_P1},  # s26 In 1905 Fort Palmer, the last military post 
    {"img": "TIMELINE", **_P1},  # s27 By the time the basin was completed in 1932,
    {"img": "ANSON", **_P0},  # s28 The road laid out across the site was named 
    {"img": "KNOLL", **_P3},  # s29 On that last knoll stands the Keramat Habib 
    {"img": "HABIBTOMB", **_P0},  # s30 In 2016, when the Prince Edward MRT station 
    {"img": "DT3", **_P1},  # s31 The other names are all on street signs: Wal
    {"img": "ANNSIANG", **_P10},  # s32 Ann Siang Hill, the one hill of the group th
    {"img": "ISLAND", **_P1},  # s33 The largest cutting of hills came after inde
    {"img": "ISLAND", **_P1},  # s34 For the East Coast reclamation, which began 
    {"img": "DT0", **_P1},  # s35 Where it fits in the bigger story: Singapore
    {"img": "TIMELINE", **_P1},  # s36 Much of that land was first a hill somewhere
    {"img": "PALMERFOOT", **_P0},  # s37 The waterfront south of the old town lost th
]

SCHEDULE = [
    (0.0, 0), (3.3, 1), (12.325, 2), (23.075, 3), (29.65, 4),
    (32.175, 5), (43.425, 6), (49.825, 7), (59.4, 8), (62.875, 9),
    (79.25, 10), (89.85, 11), (94.725, 12), (104.2, 13), (109.325, 14),
    (116.375, 15), (125.475, 16), (140.925, 17), (149.75, 18), (155.45, 19),
    (164.3, 20), (182.95, 21), (195.925, 22), (203.425, 23), (210.15, 24),
    (213.125, 25), (226.3, 26), (239.85, 27), (254.125, 28), (261.1, 29),
    (275.25, 30), (289.55, 31), (296.7, 32), (305.95, 33), (310.05, 34),
    (332.4, 35), (339.9, 36), (343.85, 37),
]
TOTAL_DURATION = 353.35
TIMING_JSON = "audio/the-hills-singapore-dug-into-the-sea.timing.json"
