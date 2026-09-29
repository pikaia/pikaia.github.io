"""Video config for the shoreline/reclamation post.

The six stage maps (scripts/render_reclamation_map.py; today, +1822, +1864,
+1879-97, +1893-1932, +after 1965) are frozen letterbox slides timed to each
era in the narration, and the land-area chart (scripts/render_land_area_chart.py)
is frozen too. Photos: Collyer Quay c.1890 (two KITLV prints, a 1890 Photochrom,
c.1910), Thian Hock Keng c.1890, the Nagore Dargah, Raffles Place, Cecil Street
and Finlayson Green c.1910, harbour panoramas, Lau Pa Sat, Marina Bay; period
maps (Jackson 1822, the 1893 city plan, Telok Ayer 1913 and 1932, 1951 town).
The Singapore Free Press of 17 Nov 1896 (page 309) is zoomed to the cost
statement. Named officials (Raffles, Collyer, MacRitchie) get places, not
portraits.

47 slides, one per sentence.
"""

CREDITS = {
    "CHART": "Chart by Lesser Known Singapore, figures per the post's own Sources list",
    "MAP0": "Map by Lesser Known Singapore; map data (c) OpenStreetMap contributors",
    "MAP1": "Map by Lesser Known Singapore; map data (c) OpenStreetMap contributors",
    "MAP2": "Map by Lesser Known Singapore; map data (c) OpenStreetMap contributors",
    "MAP3": "Map by Lesser Known Singapore; map data (c) OpenStreetMap contributors",
    "MAP4": "Map by Lesser Known Singapore; map data (c) OpenStreetMap contributors",
    "MAP5": "Map by Lesser Known Singapore; map data (c) OpenStreetMap contributors",
    "LI0": "Map by Lesser Known Singapore; map data (c) OpenStreetMap contributors",
    "LI1": "Map by Lesser Known Singapore; map data (c) OpenStreetMap contributors",
}

IMAGES = {
    "C1893": "https://upload.wikimedia.org/wikipedia/commons/thumb/1/18/Plan_map_of_the_City_of_Singapore_of_British_Malaya%2C_from_the_Constable%27s_Hand_Atlas_of_India_%281893%29.jpg/1920px-Plan_map_of_the_City_of_Singapore_of_British_Malaya%2C_from_the_Constable%27s_Hand_Atlas_of_India_%281893%29.jpg",
    "CECIL": "https://upload.wikimedia.org/wikipedia/commons/thumb/8/84/KITLV_-_79924_-_Kleingrothe%2C_C.J._-_Medan_-_Cecil_Street%2C_Singapore_-_circa_1910.tif/lossy-page1-1920px-KITLV_-_79924_-_Kleingrothe%2C_C.J._-_Medan_-_Cecil_Street%2C_Singapore_-_circa_1910.tif.jpg",
    "CHART": "/assets/images/singapore-land-area-chart.png",
    "CQ1890": "https://upload.wikimedia.org/wikipedia/commons/thumb/5/50/KITLV_-_103744_-_Collyer_Quay_in_Singapore_-_circa_1890.tif/lossy-page1-1920px-KITLV_-_103744_-_Collyer_Quay_in_Singapore_-_circa_1890.tif.jpg",
    "CQ1890B": "https://upload.wikimedia.org/wikipedia/commons/thumb/c/ca/KITLV_-_377460_-_Collyer_quay_in_Singapore_-_circa_1890.tif/lossy-page1-1920px-KITLV_-_377460_-_Collyer_quay_in_Singapore_-_circa_1890.tif.jpg",
    "CQ1910": "https://upload.wikimedia.org/wikipedia/commons/thumb/f/f0/KITLV_-_79887_-_Kleingrothe%2C_C.J._-_Medan_-_Collyer_Quay%2C_Quay_in_Singapore_-_circa_1910.tif/lossy-page1-1920px-KITLV_-_79887_-_Kleingrothe%2C_C.J._-_Medan_-_Collyer_Quay%2C_Quay_in_Singapore_-_circa_1910.tif.jpg",
    "CQLOC": "https://upload.wikimedia.org/wikipedia/commons/thumb/1/1d/Singapore._Collyer_Quai_LCCN2017657654.jpg/1920px-Singapore._Collyer_Quai_LCCN2017657654.jpg",
    "FINLAYSON": "https://upload.wikimedia.org/wikipedia/commons/thumb/3/30/KITLV_-_79894_-_Kleingrothe%2C_C.J._-_Medan_-_Finlayson_Green_at_Singapore_-_circa_1910.tif/lossy-page1-1920px-KITLV_-_79894_-_Kleingrothe%2C_C.J._-_Medan_-_Finlayson_Green_at_Singapore_-_circa_1910.tif.jpg",
    "JACKSON": "https://upload.wikimedia.org/wikipedia/commons/b/bc/Plan_of_the_Town_of_Singapore_%281822%29_by_Lieutenant_Philip_Jackson_original.jpg",
    "LI0": "/assets/images/long-island-map-0.png",
    "LI1": "/assets/images/long-island-map-1.png",
    "LPS": "https://upload.wikimedia.org/wikipedia/commons/thumb/0/00/Built_in_1894_as_a_market%2C_with_cast-iron_supports._it%27s_a_hawker_centre_now_%28Singapore_version_of_a_food_court%29_%288235341079%29.jpg/1920px-Built_in_1894_as_a_market%2C_with_cast-iron_supports._it%27s_a_hawker_centre_now_%28Singapore_version_of_a_food_court%29_%288235341079%29.jpg",
    "M1951": "https://upload.wikimedia.org/wikipedia/commons/thumb/6/66/Map_of_Singapore_City_in_1951.png/1920px-Map_of_Singapore_City_in_1951.png",
    "MAP0": "/assets/images/reclamation-map-0.png",
    "MAP1": "/assets/images/reclamation-map-1.png",
    "MAP1913": "https://upload.wikimedia.org/wikipedia/commons/2/21/Telok_Ayer_Singapore_1913.png",
    "MAP1932": "https://upload.wikimedia.org/wikipedia/commons/6/67/Telok_Ayer_Singapore_1932.png",
    "MAP2": "/assets/images/reclamation-map-2.png",
    "MAP3": "/assets/images/reclamation-map-3.png",
    "MAP4": "/assets/images/reclamation-map-4.png",
    "MAP5": "/assets/images/reclamation-map-5.png",
    "MARINA": "https://upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Singapore_Marina_Bay_Dusk_2018-02-27.jpg/1920px-Singapore_Marina_Bay_Dusk_2018-02-27.jpg",
    "NAGORE": "https://upload.wikimedia.org/wikipedia/commons/thumb/c/c4/Moskee_te_Singapore%2C_vermoedelijk_de_Nagore_Durgha_Shrine_aan_Telok_Ayer_Street%2C_KITLV_104803.tiff/lossy-page1-1920px-Moskee_te_Singapore%2C_vermoedelijk_de_Nagore_Durgha_Shrine_aan_Telok_Ayer_Street%2C_KITLV_104803.tiff.jpg",
    "PANO1": "https://upload.wikimedia.org/wikipedia/commons/thumb/0/0f/Gebouwen_langs_de_kade_in_de_haven_van_Singapore%2C_KITLV_29186.tiff/lossy-page1-1920px-Gebouwen_langs_de_kade_in_de_haven_van_Singapore%2C_KITLV_29186.tiff.jpg",
    "PANO2": "https://upload.wikimedia.org/wikipedia/commons/thumb/9/9a/Kade_te_Singapore%2C_KITLV_104787.tiff/lossy-page1-1920px-Kade_te_Singapore%2C_KITLV_104787.tiff.jpg",
    "SFP": "/assets/images/singapore-free-press-1896-11-17-page-309.jpg",
    "SQUARE": "https://upload.wikimedia.org/wikipedia/commons/thumb/2/22/KITLV_-_79888_-_Kleingrothe%2C_C.J._-_Medan_-_Square_at_Singapore_-_circa_1910.tif/lossy-page1-1920px-KITLV_-_79888_-_Kleingrothe%2C_C.J._-_Medan_-_Square_at_Singapore_-_circa_1910.tif.jpg",
    "THK": "https://upload.wikimedia.org/wikipedia/commons/thumb/8/81/KITLV_-_103742_-_Lambert_%26_Co._-_Thian_Hock_Keng_Temple_in_Singapore_-_circa_1890.tif/lossy-page1-1920px-KITLV_-_103742_-_Lambert_%26_Co._-_Thian_Hock_Keng_Temple_in_Singapore_-_circa_1890.tif.jpg",
}

_P0 = {"type": "cover", "zoom": [1.0, 1.05, 1.1], "pan": [(0.3, 0.5), (0.5, 0.5), (0.7, 0.5)], "ease": "ease-in-out"}
_P1 = {"type": "cover", "zoom": [1.35, 1.4, 1.45], "pan": [(0.5, 0.5), (0.5, 0.5), (0.5, 0.5)], "ease": "ease-in-out"}
_P2 = {"type": "letterbox", "zoom": [1.0, 1.0, 1.0], "pan": [(0.5, 0.5)] * 3, "ease": "linear"}
_P3 = {"type": "cover", "zoom": [1.6, 1.65, 1.7], "pan": [(0.62, 0.35), (0.6, 0.38), (0.58, 0.4)], "ease": "ease-in-out"}
_P4 = {"type": "cover", "zoom": [1.1, 1.05, 1.0], "pan": [(0.7, 0.5), (0.5, 0.5), (0.3, 0.5)], "ease": "ease-in-out"}
_P5 = {"type": "cover", "zoom": [1.40, 1.43, 1.47], "pan": [(0.5, 0.0), (0.5, 0.0), (0.5, 0.0)], "ease": "ease-in-out"}
_P6 = {"type": "cover", "zoom": [2.60, 2.67, 2.73], "pan": [(0.272, 0.691), (0.276, 0.702), (0.279, 0.713)], "ease": "ease-in-out"}
_P7 = {"type": "cover", "zoom": [2.80, 2.87, 2.94], "pan": [(0.282, 0.723), (0.285, 0.734), (0.288, 0.744)], "ease": "ease-in-out"}
_P8 = {"type": "cover", "zoom": [1.30, 1.33, 1.37], "pan": [(0.587, 0.704), (0.58, 0.717), (0.575, 0.729)], "ease": "ease-in-out"}

SLIDES = [
    {"img": "CQ1890", **_P0},  # s0 When Telok Ayer Street Was the Beach: Singap
    {"img": "THK", **_P0},  # s1 When the Thian Hock Keng temple was built on
    {"img": "THK", **_P1},  # s2 Sailors landing from China came up from the 
    {"img": "MAP0", **_P2},  # s3 By the end of the century it was four street
    {"img": "MAP5", **_P2},  # s4 The land in front of it was made by the colo
    {"img": "JACKSON", **_P0},  # s5 Singapore's reclamation began three years af
    {"img": "JACKSON", **_P3},  # s6 The south bank of the Singapore River was lo
    {"img": "MAP1", **_P2},  # s7 About 300 labourers did the work in roughly 
    {"img": "SQUARE", **_P0},  # s8 The new ground became Boat Quay along the ri
    {"img": "THK", **_P4},  # s9 Along the coast to the south, Telok Ayer Str
    {"img": "NAGORE", **_P0},  # s10 The Nagore Dargah shrine, built between 1828
    {"img": "CQ1890B", **_P0},  # s11 The next stretch was the waterfront east of 
    {"img": "CQ1890", **_P4},  # s12 From the late 1850s a seawall was built from
    {"img": "CQ1890", **_P1},  # s13 The work was done by Indian convict labour, 
    {"img": "CQ1890B", **_P4},  # s14 According to the National Library Board's hi
    {"img": "MAP2", **_P2},  # s15 It was finished in 1864 and named Collyer Qu
    {"img": "CQLOC", **_P0},  # s16 The largest project of the century came next
    {"img": "MAP3", **_P2},  # s17 Between 1879 and 1897 the Public Works Depar
    {"img": "CECIL", **_P0},  # s18 The first stretch, as far as Cecil Street, w
    {"img": "C1893", **_P0},  # s19 The roads linked the commercial district wit
    {"img": "PANO1", **_P0},  # s20 In April 1881, the Singapore Daily Times wro
    {"img": "C1893", **_P4},  # s21 The old Telok Ayer Market, which had stood o
    {"img": "LPS", **_P0},  # s22 Its replacement, designed by the municipal e
    {"img": "LPS", **_P4},  # s23 That building survives today as Lau-Pa-Sat.
    {"img": "SFP", **_P5},  # s24 In November 1896, at the request of a member
    {"img": "SFP", **_P6},  # s25 According to the statement, printed in the S
    {"img": "FINLAYSON", **_P0},  # s26 About 88,000 square feet had gone to Finlays
    {"img": "SFP", **_P7},  # s27 The government had sold 653,028 square feet 
    {"img": "CECIL", **_P4},  # s28 The statement put the cost of reclamation at
    {"img": "MAP1913", **_P2},  # s29 Even before the Telok Ayer works were finish
    {"img": "PANO2", **_P0},  # s30 Started in 1893, it was meant to reclaim 88 
    {"img": "MAP1913", **_P2},  # s31 In 1910 engineers found that the seawall was
    {"img": "MAP1932", **_P2},  # s32 The unfinished section was turned into a tid
    {"img": "MAP4", **_P2},  # s33 Work resumed in 1930 and was completed in 19
    {"img": "M1951", **_P8},  # s34 A road built along the new land, Raffles Way
    {"img": "CQ1910", **_P0},  # s35 According to the National Library Board's ac
    {"img": "CHART", **_P2},  # s36 Between 1965 and 2015, the country reclaimed
    {"img": "MAP5", **_P2},  # s37 The Telok Ayer Basin itself was filled in be
    {"img": "CHART", **_P2},  # s38 According to the Singapore Land Authority, t
    {"img": "MARINA", **_P0},  # s39 Two confirmed projects will move the shoreli
    {"img": "MARINA", **_P1},  # s40 At Tuas, the Maritime and Port Authority is 
    {"img": "PANO2", **_P4},  # s41 The first phase of reclamation was completed
    {"img": "LI0", **_P2},  # s42 Off the East Coast, the Urban Redevelopment 
    {"img": "LI1", **_P2},  # s43 As described when it was announced in Novemb
    {"img": "LI1", **_P2},  # s44 As of its update in March 2026, the plans we
    {"img": "MAP5", **_P2},  # s45 Where it fits in the bigger story: Much of d
    {"img": "CQ1890", **_P0},  # s46 The shoreline has been moving since 1822, fi
]

SCHEDULE = [
    (0.0, 0), (5.8, 1), (15.1, 2), (23.25, 3), (30.1, 4),
    (38.1, 5), (43.475, 6), (56.575, 7), (61.225, 8), (69.775, 9),
    (76.95, 10), (90.175, 11), (98.525, 12), (110.35, 13), (115.075, 14),
    (128.8, 15), (138.125, 16), (141.825, 17), (159.8, 18), (172.675, 19),
    (177.9, 20), (188.95, 21), (200.875, 22), (213.6, 23), (217.5, 24),
    (229.125, 25), (247.525, 26), (253.55, 27), (272.675, 28), (282.275, 29),
    (288.85, 30), (296.675, 31), (311.175, 32), (318.25, 33), (329.85, 34),
    (336.8, 35), (346.65, 36), (360.775, 37), (372.025, 38), (388.1, 39),
    (392.075, 40), (399.9, 41), (418.125, 42), (437.125, 43), (454.5, 44),
    (466.075, 45), (473.075, 46),
]
TOTAL_DURATION = 487.425
TIMING_JSON = "audio/when-telok-ayer-street-was-the-beach-singapores-first-land-reclamations.timing.json"
