"""Video config for the Bhai Maharaj Singh post.

A thin pool. The 1850s Outram prison photo (landscape, cover) doubles as a
neutral image for sentences about Punjab and Dalhousie (no portrait of anyone
else is shown under a named person). Bhai Maharaj Singh appears in the 1850
prison-cell drawing (frozen) and the 19th-century darbar painting. The shrine
photo (small, grainy) is frozen. The Straits Times pages of 18 June 1850 and
8 July 1856 are zoomed to the arrival and death reports.

29 slides, one per sentence.
"""

IMAGES = {
    "DALHOUSIE": "https://upload.wikimedia.org/wikipedia/commons/f/f8/Maharaja_Duleep_Singh_and_Governor-General_Lord_Dalhousie%2C_Lahore%2C_Punjab%2C_ca.1849%E2%80%9350.jpg",
    "CELL": "https://upload.wikimedia.org/wikipedia/commons/8/83/Bhai_Maharaj_Singh_and_Companion_%28Khurruck_Singh%29_in_a_Prison_Cell.jpg",
    "DARBAR": "https://upload.wikimedia.org/wikipedia/commons/thumb/4/4b/Painting_of_the_Sikh_warrior%2C_Bhai_Maharaj_Singh%2C_holding_court_in_his_darbar.jpg/1920px-Painting_of_the_Sikh_warrior%2C_Bhai_Maharaj_Singh%2C_holding_court_in_his_darbar.jpg",
    "POL1931": "https://upload.wikimedia.org/wikipedia/commons/0/0a/Photograph_of_members_of_the_Sikh_Police_Contingent_in-front_of_Gurdwara_Sahib_Silat_Road_in_1931.jpg",
    "PRISON": "https://upload.wikimedia.org/wikipedia/commons/thumb/5/54/Photograph_of_Outram_Prison_%28Pearl%E2%80%99s_Hill_Prison%29_in_the_1850%27s.jpg/1920px-Photograph_of_Outram_Prison_%28Pearl%E2%80%99s_Hill_Prison%29_in_the_1850%27s.jpg",
    "SAMADHI": "https://upload.wikimedia.org/wikipedia/commons/thumb/f/f3/Photograph_of_the_Samadhi_of_Bhai_Maharaj_Singh_%28then_referred_to_as_%27Baba_Karam_Singh%27%29_on_the_grounds_of_Singapore_General_Hospital.jpg/1280px-Photograph_of_the_Samadhi_of_Bhai_Maharaj_Singh_%28then_referred_to_as_%27Baba_Karam_Singh%27%29_on_the_grounds_of_Singapore_General_Hospital.jpg",
    "SILAT1924": "https://upload.wikimedia.org/wikipedia/commons/thumb/e/e3/Gurdwara_Sahib_Silat_Road_in_Singapore_after_construction_was_just_completed_in_1924.jpg/1920px-Gurdwara_Sahib_Silat_Road_in_Singapore_after_construction_was_just_completed_in_1924.jpg",
    "SILAT2015": "https://upload.wikimedia.org/wikipedia/commons/thumb/8/88/Silat_Road_Sikh_Temple%2C_Singapore.jpg/1920px-Silat_Road_Sikh_Temple%2C_Singapore.jpg",
    "ST50": "/assets/images/straits-times-1850-06-18-page-4.jpg",
    "ST56": "/assets/images/straits-times-1856-07-08-page-4.jpg",
}

_P0 = {"type": "cover", "zoom": [1.0, 1.05, 1.1], "pan": [(0.3, 0.5), (0.5, 0.5), (0.7, 0.5)], "ease": "ease-in-out"}
_P1 = {"type": "cover", "zoom": [2.40, 2.46, 2.52], "pan": [(0.0, 0.803), (0.0, 0.813), (0.0, 0.823)], "ease": "ease-in-out"}
_P2 = {"type": "letterbox", "zoom": [1.0, 1.0, 1.0], "pan": [(0.5, 0.5)] * 3, "ease": "linear"}
_P3 = {"type": "cover", "zoom": [1.3, 1.35, 1.4], "pan": [(0.5, 0.35), (0.5, 0.4), (0.5, 0.45)], "ease": "ease-in-out"}
_P4 = {"type": "cover", "zoom": [1.1, 1.05, 1.0], "pan": [(0.7, 0.5), (0.5, 0.5), (0.3, 0.5)], "ease": "ease-in-out"}
_P5 = {"type": "cover", "zoom": [1.4, 1.45, 1.5], "pan": [(0.5, 0.45), (0.5, 0.45), (0.5, 0.45)], "ease": "ease-in-out"}
_P6 = {"type": "cover", "zoom": [1.30, 1.33, 1.37], "pan": [(0.5, 0.077), (0.5, 0.095), (0.5, 0.113)], "ease": "ease-in-out"}
_P7 = {"type": "cover", "zoom": [2.80, 2.87, 2.94], "pan": [(0.0, 0.933), (0.0, 0.943), (0.0, 0.953)], "ease": "ease-in-out"}
_P8 = {"type": "cover", "zoom": [2.80, 2.87, 2.94], "pan": [(0.0, 0.962), (0.0, 0.972), (0.0, 0.982)], "ease": "ease-in-out"}
_P9 = {"type": "cover", "zoom": [2.20, 2.25, 2.31], "pan": [(0.775, 0.053), (0.77, 0.067), (0.765, 0.081)], "ease": "ease-in-out"}
_P10 = {"type": "cover", "zoom": [2.80, 2.87, 2.94], "pan": [(0.757, 0.604), (0.753, 0.615), (0.75, 0.626)], "ease": "ease-in-out"}
_P11 = {"type": "cover", "zoom": [1.45, 1.5, 1.55], "pan": [(0.42, 0.45), (0.5, 0.47), (0.58, 0.5)], "ease": "ease-in-out"}

SLIDES = [
    {"img": "PRISON", **_P0},  # s0 The Sikh Prisoner of Outram Road and the Shr
    {"img": "ST50", **_P1},  # s1 In June 1850 the Straits Times reported, in 
    {"img": "CELL", **_P2},  # s2 One of them was Bhai Maharaj Singh, a Sikh r
    {"img": "SAMADHI", **_P2},  # s3 The place where he was cremated became a shr
    {"img": "DARBAR", **_P3},  # s4 Bhai Maharaj Singh was the head of a Sikh re
    {"img": "PRISON", **_P4},  # s5 After the death of Maharaja Ranjit Singh in 
    {"img": "DARBAR", **_P5},  # s6 Sikh accounts describe Maharaj Singh as a le
    {"img": "PRISON", **_P5},  # s7 He was arrested near Adampur on the 28th of 
    {"img": "DALHOUSIE", **_P2},  # s8 The Governor-General, Lord Dalhousie, decide
    {"img": "ST50", **_P7},  # s9 The Straits Times of the 18th of June 1850 r
    {"img": "ST50", **_P8},  # s10 The paper described them as the instigators 
    {"img": "DALHOUSIE", **_P2},  # s11 According to the Central Sikh Gurdwara Board
    {"img": "CELL", **_P2},  # s12 He was nevertheless kept in a cell on the up
    {"img": "CELL", **_P2},  # s13 His health failed.
    {"img": "PRISON", **_P4},  # s14 He was almost blind within three years, suff
    {"img": "ST56", **_P9},  # s15 He died in the jail on the 5th of July 1856.
    {"img": "ST56", **_P10},  # s16 The Straits Times of the 8th of July reporte
    {"img": "CELL", **_P2},  # s17 Khurruck Singh was later moved to Penang, wh
    {"img": "CELL", **_P2},  # s18 According to the gurdwara board, it was Khur
    {"img": "SAMADHI", **_P2},  # s19 The cremation site did not stay anonymous.
    {"img": "SAMADHI", **_P2},  # s20 According to accounts collected by the Sikh 
    {"img": "PRISON", **_P5},  # s21 Muslims later put up green flags around it a
    {"img": "DARBAR", **_P3},  # s22 Many people in Singapore came to know the ma
    {"img": "SAMADHI", **_P2},  # s23 In the 1940s the shrine was moved from the p
    {"img": "POL1931", **_P11},  # s24 In 1961 a Sikh police officer installed a co
    {"img": "SILAT1924", **_P0},  # s25 The Sikh community and the government agreed
    {"img": "SILAT2015", **_P0},  # s26 A memorial building dedicated to Bhai Mahara
    {"img": "PRISON", **_P4},  # s27 Where it fits in the bigger story: The Outra
    {"img": "SILAT2015", **_P4},  # s28 What kept this story alive in Singapore was 
]

SCHEDULE = [
    (0.0, 0), (4.675, 1), (14.35, 2), (25.375, 3), (37.25, 4),
    (44.025, 5), (58.4, 6), (70.55, 7), (78.725, 8), (86.725, 9),
    (101.475, 10), (120.275, 11), (134.975, 12), (144.1, 13), (146.0, 14),
    (157.55, 15), (162.35, 16), (177.55, 17), (182.05, 18), (188.75, 19),
    (192.35, 20), (200.45, 21), (208.85, 22), (220.625, 23), (229.6, 24),
    (242.9, 25), (260.425, 26), (276.0, 27), (288.8, 28),
]
TOTAL_DURATION = 306.375
TIMING_JSON = "audio/the-sikh-prisoner-of-outram-road-and-the-shrine-that-moved-twice.timing.json"
