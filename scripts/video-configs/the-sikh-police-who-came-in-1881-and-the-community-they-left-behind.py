"""Video config for the Sikh Police Contingent post.

Photos: the contingent at the Silat Road gurdwara in 1931 (a mounted print, so
zoomed 1.45+ to stay inside the photograph), the Tanjong Pagar police station and
barracks from the dock company's album (album pages, zoomed to the photograph),
the Police Court c.1900, the gurdwara in 1924 and today, Christmas Island and
Penang. The portrait-format and small photos (uniform, traffic wings, riot
shields) are frozen letterbox. The Straits Times of 19 December 1922 (page 10)
is zoomed down the column carrying the foundation-stone report.

44 slides, one per sentence.
"""

IMAGES = {
    "BARRACKS": "https://upload.wikimedia.org/wikipedia/commons/thumb/f/f1/Politiebureau_van_Tanjong_Pagar_in_Singapore_Police_barracks_%28titel_op_object%29%2C_RP-F-F01140-R.jpg/1920px-Politiebureau_van_Tanjong_Pagar_in_Singapore_Police_barracks_%28titel_op_object%29%2C_RP-F-F01140-R.jpg",
    "COURT": "https://thumb.wikimedia.org/wikipedia/commons/thumb/b/b1/KITLV_-_50214_-_Lambert_%26_Co.%2C_G.R._-_Singapore_-_Police_Court_in_Singapore_-_circa_1900.jpg/1920px-KITLV_-_50214_-_Lambert_%26_Co.%2C_G.R._-_Singapore_-_Police_Court_in_Singapore_-_circa_1900.jpg",
    "MEMBER": "https://upload.wikimedia.org/wikipedia/commons/b/b0/Sikh_Contingent_member%2C_Straits_Settlements_Police.jpg",
    "PENANG": "https://upload.wikimedia.org/wikipedia/commons/9/9a/Sikh_Police_Straits_Settlements_Penang_Court.jpg",
    "POL1931": "https://upload.wikimedia.org/wikipedia/commons/0/0a/Photograph_of_members_of_the_Sikh_Police_Contingent_in-front_of_Gurdwara_Sahib_Silat_Road_in_1931.jpg",
    "POLICE": "https://upload.wikimedia.org/wikipedia/commons/thumb/c/c0/Politieagenten_voor_het_politiebureau_van_Tanjong_Pagar_in_Singapore_Tanjong_Pagar_police_station_%28titel_op_object%29%2C_RP-F-F01140-AQ.jpg/1920px-Politieagenten_voor_het_politiebureau_van_Tanjong_Pagar_in_Singapore_Tanjong_Pagar_police_station_%28titel_op_object%29%2C_RP-F-F01140-AQ.jpg",
    "SHIELD": "https://upload.wikimedia.org/wikipedia/commons/b/b0/SSPF_riot_shield.png",
    "SILAT1924": "https://thumb.wikimedia.org/wikipedia/commons/thumb/e/e3/Gurdwara_Sahib_Silat_Road_in_Singapore_after_construction_was_just_completed_in_1924.jpg/1920px-Gurdwara_Sahib_Silat_Road_in_Singapore_after_construction_was_just_completed_in_1924.jpg",
    "SILAT2015": "https://thumb.wikimedia.org/wikipedia/commons/thumb/8/88/Silat_Road_Sikh_Temple%2C_Singapore.jpg/1920px-Silat_Road_Sikh_Temple%2C_Singapore.jpg",
    "ST1922": "/assets/images/straits-times-1922-12-19-page-10.jpg",
    "WINGS": "https://upload.wikimedia.org/wikipedia/commons/8/84/Sikh_Singapore_traffic_wings.jpg",
    "XMAS": "https://upload.wikimedia.org/wikipedia/commons/8/89/Sikh_Contingent_at_Christmas_Island.png",
}

_P0 = {"type": "cover", "zoom": [1.45, 1.5, 1.55], "pan": [(0.42, 0.45), (0.5, 0.47), (0.58, 0.5)], "ease": "ease-in-out"}
_P1 = {"type": "cover", "zoom": [1.35, 1.38, 1.42], "pan": [(0.5, 0.649), (0.5, 0.669), (0.5, 0.689)], "ease": "ease-in-out"}
_P2 = {"type": "letterbox", "zoom": [1.0, 1.0, 1.0], "pan": [(0.5, 0.5)] * 3, "ease": "linear"}
_P3 = {"type": "cover", "zoom": [1.0, 1.05, 1.1], "pan": [(0.4, 0.5), (0.5, 0.5), (0.6, 0.5)], "ease": "ease-in-out"}
_P4 = {"type": "cover", "zoom": [1.1, 1.05, 1.0], "pan": [(0.6, 0.5), (0.5, 0.5), (0.4, 0.5)], "ease": "ease-in-out"}
_P5 = {"type": "cover", "zoom": [1.55, 1.5, 1.45], "pan": [(0.58, 0.5), (0.5, 0.47), (0.42, 0.45)], "ease": "ease-in-out"}
_P6 = {"type": "cover", "zoom": [1.5, 1.55, 1.6], "pan": [(0.45, 0.42), (0.5, 0.45), (0.55, 0.48)], "ease": "ease-in-out"}
_P7 = {"type": "cover", "zoom": [1.3, 1.35, 1.4], "pan": [(0.5, 0.45), (0.5, 0.45), (0.5, 0.45)], "ease": "ease-in-out"}
_P8 = {"type": "cover", "zoom": [1.60, 1.64, 1.68], "pan": [(0.553, 0.528), (0.551, 0.555), (0.549, 0.581)], "ease": "ease-in-out"}
_P9 = {"type": "cover", "zoom": [2.1, 2.2, 2.3], "pan": [(0.3, 0.68), (0.45, 0.68), (0.6, 0.68)], "ease": "ease-in-out"}
_P10 = {"type": "cover", "zoom": [1.6, 1.55, 1.5], "pan": [(0.55, 0.48), (0.5, 0.45), (0.45, 0.42)], "ease": "ease-in-out"}
_P11 = {"type": "cover", "zoom": [2.00, 2.05, 2.10], "pan": [(0.3, 0.706), (0.354, 0.704), (0.405, 0.703)], "ease": "ease-in-out"}
_P12 = {"type": "cover", "zoom": [2.60, 2.67, 2.73], "pan": [(0.126, 0.022), (0.132, 0.036), (0.137, 0.05)], "ease": "ease-in-out"}
_P13 = {"type": "cover", "zoom": [2.80, 2.87, 2.94], "pan": [(0.142, 0.052), (0.147, 0.066), (0.151, 0.08)], "ease": "ease-in-out"}
_P14 = {"type": "cover", "zoom": [2.80, 2.87, 2.94], "pan": [(0.142, 0.147), (0.147, 0.16), (0.151, 0.173)], "ease": "ease-in-out"}
_P15 = {"type": "cover", "zoom": [2.80, 2.87, 2.94], "pan": [(0.142, 0.453), (0.147, 0.465), (0.151, 0.477)], "ease": "ease-in-out"}
_P16 = {"type": "cover", "zoom": [2.80, 2.87, 2.94], "pan": [(0.142, 0.641), (0.147, 0.652), (0.151, 0.664)], "ease": "ease-in-out"}

SLIDES = [
    {"img": "POL1931", **_P0},  # s0 The Sikh Police Who Came in 1881, and the Co
    {"img": "POLICE", **_P1},  # s1 On the 26th of March 1881 an assistant super
    {"img": "MEMBER", **_P2},  # s2 By the end of the year the Sikh Police Conti
    {"img": "SILAT2015", **_P3},  # s3 The contingent was disbanded in 1945, but th
    {"img": "COURT", **_P3},  # s4 The first Sikhs recorded in Singapore did no
    {"img": "COURT", **_P4},  # s5 In 1850 two Sikh political prisoners, Bhai M
    {"img": "POL1931", **_P5},  # s6 The police recruitment came three decades la
    {"img": "SHIELD", **_P2},  # s7 In the 1870s the Straits Settlements Police 
    {"img": "BARRACKS", **_P6},  # s8 A police report in 1856 had already complain
    {"img": "COURT", **_P7},  # s9 In 1879 a commission of enquiry into the pol
    {"img": "PENANG", **_P3},  # s10 According to the Singapore Police Force's ow
    {"img": "POLICE", **_P8},  # s11 The first group landed on the 26th of March 
    {"img": "POL1931", **_P9},  # s12 About 100 Sikh policemen were in Singapore b
    {"img": "BARRACKS", **_P10},  # s13 The European constables did not adapt well t
    {"img": "MEMBER", **_P2},  # s14 The terms of service were strict.
    {"img": "POL1931", **_P0},  # s15 Recruits had to be at least 175 centimetres 
    {"img": "POL1931", **_P5},  # s16 They were also baptised at the contingent's 
    {"img": "COURT", **_P4},  # s17 The contingent kept order in town and guarde
    {"img": "SHIELD", **_P2},  # s18 A riot squad of 50 men was kept on standby a
    {"img": "WINGS", **_P2},  # s19 Later they also took on beat and traffic dut
    {"img": "XMAS", **_P3},  # s20 A detachment was sent to Christmas Island, t
    {"img": "POLICE", **_P11},  # s21 The contingent's reputation made Sikh guards
    {"img": "POLICE", **_P1},  # s22 The Tanjong Pagar Dock Company hired Sikhs a
    {"img": "BARRACKS", **_P6},  # s23 Others guarded the Straits Trading Company's
    {"img": "BARRACKS", **_P10},  # s24 The contingent built its own gurdwara at its
    {"img": "POL1931", **_P9},  # s25 As more Sikhs came to Singapore, the communi
    {"img": "SILAT1924", **_P3},  # s26 In 1912 civilian Sikhs, in a committee led b
    {"img": "ST1922", **_P12},  # s27 The police Sikhs then petitioned for land of
    {"img": "ST1922", **_P13},  # s28 The Straits Times of the 19th of December 19
    {"img": "ST1922", **_P14},  # s29 The address read to him that day explained t
    {"img": "ST1922", **_P15},  # s30 The paper reported that $22,000 had already 
    {"img": "ST1922", **_P16},  # s31 That evening the Sikhs held a farewell recep
    {"img": "SILAT1924", **_P4},  # s32 The gurdwara was completed in 1924 at a cost
    {"img": "SILAT1924", **_P7},  # s33 It was the first gurdwara in Singapore built
    {"img": "POL1931", **_P5},  # s34 During the Japanese occupation it housed and
    {"img": "PENANG", **_P4},  # s35 The Sikh Police Contingent did not survive t
    {"img": "BARRACKS", **_P6},  # s36 The National Library Board's history of the 
    {"img": "WINGS", **_P2},  # s37 Individual Sikh officers continued to serve 
    {"img": "XMAS", **_P4},  # s38 In 1949 the police formed a new guard force 
    {"img": "SILAT2015", **_P3},  # s39 The community outlasted the contingent.
    {"img": "SILAT2015", **_P4},  # s40 Singapore had 12,051 resident Sikhs in 2020,
    {"img": "POL1931", **_P0},  # s41 Where it fits in the bigger story: Singapore
    {"img": "POLICE", **_P11},  # s42 The Sikh Police Contingent was recruited to 
    {"img": "POL1931", **_P9},  # s43 The men it brought from Punjab, and the guar
]

SCHEDULE = [
    (0.0, 0), (5.975, 1), (21.625, 2), (27.875, 3), (38.95, 4),
    (44.025, 5), (54.65, 6), (60.075, 7), (71.775, 8), (85.95, 9),
    (94.15, 10), (109.525, 11), (118.075, 12), (128.075, 13), (138.825, 14),
    (141.625, 15), (154.675, 16), (167.15, 17), (172.075, 18), (183.425, 19),
    (187.375, 20), (197.0, 21), (203.075, 22), (208.225, 23), (220.575, 24),
    (231.3, 25), (236.2, 26), (247.225, 27), (261.4, 28), (279.1, 29),
    (292.05, 30), (304.25, 31), (310.55, 32), (321.35, 33), (328.6, 34),
    (340.525, 35), (344.625, 36), (365.3, 37), (370.875, 38), (380.725, 39),
    (384.25, 40), (402.45, 41), (410.675, 42), (424.8, 43),
]
TOTAL_DURATION = 437.975
TIMING_JSON = "audio/the-sikh-police-who-came-in-1881-and-the-community-they-left-behind.timing.json"
