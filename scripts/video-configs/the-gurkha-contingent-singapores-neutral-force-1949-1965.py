"""Video config for the Gurkha Contingent post.

Photos: 2/9th Gurkha Rifles in the Malayan jungle, 1941 (small square scans,
frozen letterbox), the Kranji grave and the 2005 Police Day Parade (cover),
and 2005 guard-duty and pipe-band photos (portrait, frozen letterbox). The
Straits Times pages of 16 February 1949 (page 3) and 12 and 13 December 1950
(front pages) are zoomed to the headline, photos and the relevant columns.

28 slides, one per sentence.
"""

IMAGES = {
    "BAND": "https://upload.wikimedia.org/wikipedia/commons/c/cb/Gurkha_Band.jpg",
    "FE237": "https://upload.wikimedia.org/wikipedia/commons/6/6e/The_British_Army_in_Malaya_1941_FE237.jpg",
    "FE239": "https://upload.wikimedia.org/wikipedia/commons/0/00/The_British_Army_in_Malaya_1941_FE239.jpg",
    "FE248": "https://upload.wikimedia.org/wikipedia/commons/a/a4/The_British_Army_in_Malaya_1941_FE248.jpg",
    "IOC1": "https://upload.wikimedia.org/wikipedia/commons/4/4a/Gurkha_IOC_1.jpg",
    "IOC2": "https://upload.wikimedia.org/wikipedia/commons/9/9b/Gurkha_IOC_2.jpg",
    "KRANJI": "https://upload.wikimedia.org/wikipedia/commons/a/a5/A_Gurkha_soldier%27s_tombstone_at_Kranji_War_Cemetery%2C_Singapore.jpg",
    "PARADE": "https://upload.wikimedia.org/wikipedia/commons/thumb/0/0d/Singapore_Gurkha_01.jpg/1920px-Singapore_Gurkha_01.jpg",
    "ST1212": "/assets/images/straits-times-1950-12-12-page-1.jpg",
    "ST1213": "/assets/images/straits-times-1950-12-13-page-1.jpg",
    "ST1949": "/assets/images/straits-times-1949-02-16-page-3.jpg",
}

_P0 = {"type": "letterbox", "zoom": [1.0, 1.0, 1.0], "pan": [(0.5, 0.5)] * 3, "ease": "linear"}
_P1 = {"type": "cover", "zoom": [2.20, 2.25, 2.31], "pan": [(0.5, 0.152), (0.5, 0.167), (0.5, 0.181)], "ease": "ease-in-out"}
_P2 = {"type": "cover", "zoom": [1.25, 1.28, 1.31], "pan": [(0.5, 0.0), (0.5, 0.0), (0.5, 0.0)], "ease": "ease-in-out"}
_P3 = {"type": "cover", "zoom": [1.0, 1.05, 1.1], "pan": [(0.2, 0.5), (0.25, 0.5), (0.3, 0.5)], "ease": "ease-in-out"}
_P4 = {"type": "cover", "zoom": [1.1, 1.05, 1.0], "pan": [(0.6, 0.5), (0.5, 0.5), (0.4, 0.5)], "ease": "ease-in-out"}
_P5 = {"type": "cover", "zoom": [2.60, 2.67, 2.73], "pan": [(0.5, 0.153), (0.5, 0.166), (0.5, 0.18)], "ease": "ease-in-out"}
_P6 = {"type": "cover", "zoom": [2.60, 2.67, 2.73], "pan": [(0.5, 0.213), (0.5, 0.226), (0.5, 0.239)], "ease": "ease-in-out"}
_P7 = {"type": "cover", "zoom": [2.60, 2.67, 2.73], "pan": [(0.419, 0.284), (0.42, 0.297), (0.421, 0.31)], "ease": "ease-in-out"}
_P8 = {"type": "cover", "zoom": [2.60, 2.67, 2.73], "pan": [(0.419, 0.38), (0.42, 0.393), (0.421, 0.405)], "ease": "ease-in-out"}
_P9 = {"type": "cover", "zoom": [1.0, 1.05, 1.1], "pan": [(0.3, 0.4), (0.45, 0.42), (0.6, 0.45)], "ease": "ease-in-out"}
_P10 = {"type": "cover", "zoom": [1.1, 1.05, 1.0], "pan": [(0.7, 0.45), (0.55, 0.42), (0.4, 0.4)], "ease": "ease-in-out"}
_P11 = {"type": "cover", "zoom": [1.50, 1.54, 1.58], "pan": [(0.0, 0.0), (0.0, 0.0), (0.0, 0.004)], "ease": "ease-in-out"}
_P12 = {"type": "cover", "zoom": [1.80, 1.84, 1.89], "pan": [(0.432, 0.237), (0.434, 0.252), (0.436, 0.267)], "ease": "ease-in-out"}
_P13 = {"type": "cover", "zoom": [2.00, 2.05, 2.10], "pan": [(0.06, 0.143), (0.07, 0.158), (0.08, 0.173)], "ease": "ease-in-out"}
_P14 = {"type": "cover", "zoom": [2.80, 2.87, 2.94], "pan": [(0.376, 0.535), (0.377, 0.547), (0.379, 0.559)], "ease": "ease-in-out"}
_P15 = {"type": "cover", "zoom": [1.80, 1.84, 1.89], "pan": [(0.77, 0.237), (0.762, 0.252), (0.755, 0.267)], "ease": "ease-in-out"}

SLIDES = [
    {"img": "FE237", **_P0},  # s0 The Gurkha Contingent: Singapore's Neutral F
    {"img": "ST1949", **_P1},  # s1 In February 1949 an officer of the Singapore
    {"img": "FE239", **_P0},  # s2 They were to form a new riot squad, replacin
    {"img": "ST1213", **_P2},  # s3 Within two years that quality was tested in 
    {"img": "FE248", **_P0},  # s4 The Sikh Police Contingent was disbanded aft
    {"img": "KRANJI", **_P3},  # s5 The Britainâ€“Indiaâ€“Nepal agreement of 194
    {"img": "KRANJI", **_P4},  # s6 The National Library Board's account notes t
    {"img": "ST1949", **_P5},  # s7 The Straits Times of the 16th of February 19
    {"img": "ST1949", **_P6},  # s8 It reported that R. A. H. Cowan, an assistan
    {"img": "ST1949", **_P7},  # s9 The men and most of their families were to b
    {"img": "ST1949", **_P8},  # s10 The paper also recalled that during the occu
    {"img": "PARADE", **_P9},  # s11 The Gurkha Contingent was formed as part of 
    {"img": "PARADE", **_P10},  # s12 Its first commanding officer, according to t
    {"img": "ST1212", **_P11},  # s13 Its first real test came within two years.
    {"img": "ST1212", **_P12},  # s14 On the 2nd of December 1950 the High Court r
    {"img": "ST1213", **_P13},  # s15 The Straits Times of the 13th of December re
    {"img": "ST1213", **_P14},  # s16 Its reporters wrote that "hundreds of Britis
    {"img": "ST1213", **_P15},  # s17 The paper did not separate the police contin
    {"img": "FE239", **_P0},  # s18 The same reasoning applied through the 1950s
    {"img": "KRANJI", **_P4},  # s19 The contingent was used again during the Hoc
    {"img": "IOC2", **_P0},  # s20 Lee Kuan Yew later explained the value of th
    {"img": "PARADE", **_P9},  # s21 Using Chinese policemen against Malays, or M
    {"img": "IOC1", **_P0},  # s22 When Singapore became independent in 1965, i
    {"img": "PARADE", **_P10},  # s23 The contingent remains a unit of the Singapo
    {"img": "BAND", **_P0},  # s24 According to the National Library Board and 
    {"img": "IOC1", **_P0},  # s25 It guards selected installations, augments t
    {"img": "FE237", **_P0},  # s26 Where it fits in the bigger story: The Gurkh
    {"img": "PARADE", **_P9},  # s27 Its value was tested in 1950, within two yea
]

SCHEDULE = [
    (0.0, 0), (6.875, 1), (18.475, 2), (34.425, 3), (45.9, 4),
    (57.725, 5), (73.25, 6), (85.0, 7), (94.15, 8), (112.65, 9),
    (126.8, 10), (143.675, 11), (156.325, 12), (163.175, 13), (166.85, 14),
    (182.325, 15), (197.2, 16), (203.775, 17), (219.45, 18), (223.55, 19),
    (240.95, 20), (246.725, 21), (258.825, 22), (266.7, 23), (271.575, 24),
    (291.5, 25), (300.5, 26), (317.9, 27),
]
TOTAL_DURATION = 336.825
TIMING_JSON = "audio/the-gurkha-contingent-singapores-neutral-force-1949-1965.timing.json"
