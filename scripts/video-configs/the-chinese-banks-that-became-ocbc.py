"""Video config for the Chinese banks post.

Kling Street (1870s album photo, 1862 stereograph, 1907 postcard) and Raffles
Place c.1910 carry the street-level story; the Singapore Free Press of 21 Nov
1913 (page 7) is zoomed down the Kwong Yik run report, the Straits Times of
30 Aug 1932 (page 9) to the merger scheme and the "Union is Strength" letter.
Named founders get their own portraits (Lee Choon Guan, Lim Nee Soon, Oei
Tiong Ham, Eu Tong Sen, Lee Kong Chian; frozen letterbox); Wong Ah Fook, Song
Ong Siang and Low Peng Yam have no portrait, so their sentences show streets.
The lifespan chart (scripts/render_chinese_banks_chart.py) is frozen.

41 slides, one per sentence.
"""

CREDITS = {
    "CHART": "Chart by Lesser Known Singapore, figures per the post's own Sources list",
}

IMAGES = {
    "CHART": "/assets/images/chinese-banks-chart.png",
    "ETS": "https://upload.wikimedia.org/wikipedia/commons/3/3a/Eu_Tong_Sen.jpg",
    "KLING1870": "https://upload.wikimedia.org/wikipedia/commons/thumb/4/44/Kling_Street_in_Singapore%2C_RP-F-AA3188-BM.jpg/1920px-Kling_Street_in_Singapore%2C_RP-F-AA3188-BM.jpg",
    "KLING1907": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/d0/Kling_Street%2C_Singapore_%28NYPL_Hades-2359713-4044478%29.jpg/1920px-Kling_Street%2C_Singapore_%28NYPL_Hades-2359713-4044478%29.jpg",
    "LCG": "https://upload.wikimedia.org/wikipedia/commons/0/0d/Lee_Choon_Guan.png",
    "LKC": "https://upload.wikimedia.org/wikipedia/commons/e/e4/Lee_Kong_Chian%2C_1946.png",
    "LNS": "https://upload.wikimedia.org/wikipedia/commons/2/24/Lim_Nee_Soon.png",
    "OTH": "https://upload.wikimedia.org/wikipedia/commons/b/b6/Oei_Tiong_Ham.jpg",
    "PENANG": "https://upload.wikimedia.org/wikipedia/commons/thumb/2/28/OCBC_Art_Deco_Beach_St.jpg/1920px-OCBC_Art_Deco_Beach_St.jpg",
    "PENANG2": "https://upload.wikimedia.org/wikipedia/commons/e/e2/Oversea-Chinese_Banking_Corporation_Building%2C_Beach_Street%2C_George_Town%2C_Penang.jpg",
    "RAFFLES": "https://upload.wikimedia.org/wikipedia/commons/thumb/8/85/KITLV_-_79893_-_Kleingrothe%2C_C.J._-_Medan_-_Raffles_Place_and_King_Street_in_Singapore_-_circa_1910.tif/lossy-page1-1920px-KITLV_-_79893_-_Kleingrothe%2C_C.J._-_Medan_-_Raffles_Place_and_King_Street_in_Singapore_-_circa_1910.tif.jpg",
    "SFP13": "/assets/images/singapore-free-press-1913-11-21-page-7.jpg",
    "ST32": "/assets/images/straits-times-1932-08-30-page-9.jpg",
    "STEREO": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/da/25_stereographs_depicting_Singapore_town_views_Or._27.423_-_photo_007.tif/lossy-page1-1920px-25_stereographs_depicting_Singapore_town_views_Or._27.423_-_photo_007.tif.jpg",
}

_P0 = {"type": "cover", "zoom": [1.0, 1.05, 1.1], "pan": [(0.3, 0.5), (0.5, 0.5), (0.7, 0.5)], "ease": "ease-in-out"}
_P1 = {"type": "cover", "zoom": [1.35, 1.4, 1.45], "pan": [(0.5, 0.5), (0.5, 0.5), (0.5, 0.5)], "ease": "ease-in-out"}
_P2 = {"type": "cover", "zoom": [1.30, 1.33, 1.37], "pan": [(0.24, 0.0), (0.26, 0.0), (0.276, 0.0)], "ease": "ease-in-out"}
_P3 = {"type": "letterbox", "zoom": [1.0, 1.0, 1.0], "pan": [(0.5, 0.5)] * 3, "ease": "linear"}
_P4 = {"type": "cover", "zoom": [1.1, 1.05, 1.0], "pan": [(0.7, 0.5), (0.5, 0.5), (0.3, 0.5)], "ease": "ease-in-out"}
_P5 = {"type": "cover", "zoom": [2.1, 2.15, 2.2], "pan": [(0.5, 0.45), (0.5, 0.46), (0.5, 0.47)], "ease": "ease-in-out"}
_P6 = {"type": "cover", "zoom": [1.9, 1.95, 2.0], "pan": [(0.28, 0.5), (0.3, 0.5), (0.32, 0.5)], "ease": "ease-in-out"}
_P7 = {"type": "cover", "zoom": [2.40, 2.46, 2.52], "pan": [(0.397, 0.0), (0.399, 0.0), (0.401, 0.0)], "ease": "ease-in-out"}
_P8 = {"type": "cover", "zoom": [2.60, 2.67, 2.73], "pan": [(0.403, 0.056), (0.404, 0.07), (0.405, 0.084)], "ease": "ease-in-out"}
_P9 = {"type": "cover", "zoom": [2.60, 2.67, 2.73], "pan": [(0.403, 0.248), (0.404, 0.261), (0.405, 0.274)], "ease": "ease-in-out"}
_P10 = {"type": "cover", "zoom": [1.0, 1.03, 1.06], "pan": [(0.5, 0.35), (0.5, 0.4), (0.5, 0.45)], "ease": "ease-in-out"}
_P11 = {"type": "cover", "zoom": [1.40, 1.43, 1.47], "pan": [(0.0, 0.0), (0.0, 0.0), (0.0, 0.0)], "ease": "ease-in-out"}
_P12 = {"type": "cover", "zoom": [2.40, 2.46, 2.52], "pan": [(0.106, 0.0), (0.112, 0.0), (0.119, 0.009)], "ease": "ease-in-out"}
_P13 = {"type": "cover", "zoom": [2.60, 2.67, 2.73], "pan": [(0.126, 0.464), (0.132, 0.476), (0.137, 0.488)], "ease": "ease-in-out"}
_P14 = {"type": "cover", "zoom": [2.60, 2.67, 2.73], "pan": [(0.126, 0.643), (0.132, 0.654), (0.137, 0.665)], "ease": "ease-in-out"}

SLIDES = [
    {"img": "KLING1907", **_P0},  # s0 The Chinese Banks That Became OCBC
    {"img": "KLING1907", **_P1},  # s1 On the morning of the 20th of November 1913,
    {"img": "SFP13", **_P2},  # s2 Singapore's first Chinese bank had lasted te
    {"img": "CHART", **_P3},  # s3 Over the next two decades, more Chinese bank
    {"img": "RAFFLES", **_P0},  # s4 When the European banks arrived from 1840, m
    {"img": "KLING1907", **_P4},  # s5 By the early 1900s, Singapore's Chinese merc
    {"img": "KLING1870", **_P5},  # s6 The first was the Kwong Yik Bank, which open
    {"img": "STEREO", **_P6},  # s7 It was founded by Cantonese businessmen led 
    {"img": "SFP13", **_P7},  # s8 In November 1913, after weeks of rumours, de
    {"img": "SFP13", **_P8},  # s9 According to the Singapore Free Press, its f
    {"img": "SFP13", **_P9},  # s10 A crowd gathered outside, most of them, the 
    {"img": "RAFFLES", **_P4},  # s11 The bank went into liquidation, and its liqu
    {"img": "RAFFLES", **_P1},  # s12 In 1915 the colony amended its Companies Bil
    {"img": "CHART", **_P3},  # s13 The next banks followed dialect lines.
    {"img": "KLING1907", **_P0},  # s14 The Teochew community's Sze Hai Tong Banking
    {"img": "RAFFLES", **_P0},  # s15 The Hokkien community's first bank, the Chin
    {"img": "LCG", **_P3},  # s16 Its first chairman was Lee-Choon-Guan and it
    {"img": "CHART", **_P3},  # s17 Each bank drew its directors, staff and depo
    {"img": "KLING1907", **_P1},  # s18 On the 4th of August 1914, when war broke ou
    {"img": "RAFFLES", **_P4},  # s19 The government examined its accounts, declar
    {"img": "STEREO", **_P6},  # s20 According to Song Ong Siang, the Teochew bus
    {"img": "RAFFLES", **_P1},  # s21 The boom after the First World War brought t
    {"img": "LNS", **_P3},  # s22 The Oversea-Chinese Bank was formed in 1919 
    {"img": "OTH", **_P3},  # s23 Lim-Boon-Keng persuaded Oei-Tiong-Ham, the w
    {"img": "PENANG2", **_P10},  # s24 It opened branches in Penang, Rangoon, Kuala
    {"img": "KLING1870", **_P5},  # s25 The Cantonese community tried again as well.
    {"img": "ETS", **_P3},  # s26 In March 1920 Eu-Tong-Sen, the tin and medic
    {"img": "CHART", **_P3},  # s27 The Depression hit the Chinese banks hard, b
    {"img": "PENANG", **_P10},  # s28 In 1932 the Oversea-Chinese Bank's Rangoon b
    {"img": "ST32", **_P11},  # s29 Its directors opened confidential talks with
    {"img": "ST32", **_P12},  # s30 On the 30th of August 1932 the Straits Times
    {"img": "ST32", **_P13},  # s31 The directors' letter to shareholders listed
    {"img": "ST32", **_P14},  # s32 One share in the Chinese Commercial Bank was
    {"img": "CHART", **_P3},  # s33 The Oversea-Chinese Banking Corporation was 
    {"img": "LKC", **_P3},  # s34 The talks that created it were led by Tan-Ea
    {"img": "CHART", **_P3},  # s35 The merger joined the three Hokkien banks, b
    {"img": "KLING1907", **_P0},  # s36 The Teochew bank kept its independence for a
    {"img": "PENANG2", **_P10},  # s37 Renamed Four Seas Communications Bank in 196
    {"img": "RAFFLES", **_P0},  # s38 The Cantonese Lee Wah Bank was acquired by U
    {"img": "PENANG", **_P10},  # s39 Where it fits in the bigger story: OCBC is u
    {"img": "KLING1907", **_P4},  # s40 It began as three banks that belonged to one
]

SCHEDULE = [
    (0.0, 0), (3.6, 1), (16.725, 2), (21.125, 3), (35.725, 4),
    (46.45, 5), (60.85, 6), (67.35, 7), (80.6, 8), (86.725, 9),
    (101.675, 10), (112.475, 11), (121.675, 12), (131.525, 13), (134.775, 14),
    (146.2, 15), (161.25, 16), (174.925, 17), (184.075, 18), (197.425, 19),
    (206.125, 20), (219.175, 21), (224.275, 22), (239.575, 23), (250.125, 24),
    (261.25, 25), (265.0, 26), (278.075, 27), (285.275, 28), (300.55, 29),
    (309.225, 30), (315.075, 31), (335.35, 32), (342.1, 33), (362.8, 34),
    (377.725, 35), (382.075, 36), (386.95, 37), (396.225, 38), (402.275, 39),
    (410.0, 40),
]
TOTAL_DURATION = 423.725
TIMING_JSON = "audio/the-chinese-banks-that-became-ocbc.timing.json"
