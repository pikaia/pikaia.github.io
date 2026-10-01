"""Video config for the Barings 1995 post.

1995 Singapore is thin on freely licensed photos (Straits Times pages from that
year are still SPH copyright), so the Singapore story is carried by OUB Centre
(SIMEX's trading floor) and Raffles Place around 2001-2002, tilting up and down
the towers; London by Bishopsgate in 1993, the 1920s partners painting and an
1892 letter of credit; the Kobe earthquake by City of Kobe and Akiyoshi's Room
photos. Leeson, Richard Hu, Kerviel and Adoboli have no free portraits, so their
sentences show buildings or streets. Sir Francis Baring's portrait and the 1892
letter are frozen letterbox, as is the losses chart
(scripts/render_barings_losses_chart.py).

68 slides, one per sentence.
"""

CREDITS = {
    "CHART": "Chart by Lesser Known Singapore, figures from the Singapore inspectors' report (1995) via NLB Infopedia",
    "RP2002": "Sippala (Timo Sippala), CC BY-SA 2.5, via Wikimedia Commons",
    "EVE2001": "Steven Byles, CC BY-SA 2.0, via Wikimedia Commons",
}

IMAGES = {
    "A001": "https://upload.wikimedia.org/wikipedia/commons/thumb/b/b4/Images_from_The_Great_Hanshin-Awaji_Earthquake-a001.jpg/1280px-Images_from_The_Great_Hanshin-Awaji_Earthquake-a001.jpg",
    "BISH": "https://upload.wikimedia.org/wikipedia/commons/thumb/b/be/Junction_of_Bishopsgate_and_Threadneedle_Street%2C_London%2C_July_1993.jpg/1280px-Junction_of_Bishopsgate_and_Threadneedle_Street%2C_London%2C_July_1993.jpg",
    "BISH22": "https://upload.wikimedia.org/wikipedia/commons/thumb/5/5e/22_Bishopsgate%2C_London_1993.jpg/1280px-22_Bishopsgate%2C_London_1993.jpg",
    "CHART": "/assets/images/barings-losses-chart.png",
    "EVE2001": "https://upload.wikimedia.org/wikipedia/commons/a/a8/Evening_view_of_UOB_Plaza%2C_OUB_Centre_and_OCBC_Centre_near_the_Singapore_River_-_20010608.jpg",
    "FBARING": "https://upload.wikimedia.org/wikipedia/commons/thumb/9/90/Sir_Francis_Baring%2C_1st_Baronet.jpg/1280px-Sir_Francis_Baring%2C_1st_Baronet.jpg",
    "FIRE": "https://upload.wikimedia.org/wikipedia/commons/thumb/e/ef/Fire_of_Great_Hanshin_earthquake_Seen_from_Portisland.jpg/1280px-Fire_of_Great_Hanshin_earthquake_Seen_from_Portisland.jpg",
    "HYOGO": "https://upload.wikimedia.org/wikipedia/commons/thumb/4/41/Hanshin-Awaji_earthquake_1995_Hyogo-ku_Kobe_city_Hyogo_prefecture_001.jpg/1280px-Hanshin-Awaji_earthquake_1995_Hyogo-ku_Kobe_city_Hyogo_prefecture_001.jpg",
    "KOBE001": "https://upload.wikimedia.org/wikipedia/commons/thumb/c/c1/Hanshin-Awaji_earthquake_1995_Chuo-ku_Kobe_city_Hyogo_prefecture_001.jpg/1280px-Hanshin-Awaji_earthquake_1995_Chuo-ku_Kobe_city_Hyogo_prefecture_001.jpg",
    "LETTER": "https://upload.wikimedia.org/wikipedia/commons/thumb/b/b6/Barings_circular_letter_of_credit_1892.jpg/1280px-Barings_circular_letter_of_credit_1892.jpg",
    "OUB": "https://upload.wikimedia.org/wikipedia/commons/5/53/OUB_Centre_3.JPG",
    "OUBSKY": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/d2/OUB_Centre_Skyward.JPG/1280px-OUB_Centre_Skyward.JPG",
    "PARTNERS": "https://upload.wikimedia.org/wikipedia/commons/1/1a/Messrs_Baring_Brothers_%26_Co.jpg",
    "RP2002": "https://upload.wikimedia.org/wikipedia/commons/c/cd/Raffles_Place_in_front_of_OUB_Centre%2C_Singapore_-_20020829.jpg",
    "SGX": "https://upload.wikimedia.org/wikipedia/commons/thumb/4/49/SGX_Centre%2C_Singapore_-_20121015.jpg/960px-SGX_Centre%2C_Singapore_-_20121015.jpg",
    "SGX2": "https://upload.wikimedia.org/wikipedia/commons/b/bd/SGX_Centre_Two.JPG",
}

_P0 = {"type": "cover", "zoom": [1.0, 1.05, 1.1], "pan": [(0.3, 0.5), (0.5, 0.5), (0.7, 0.5)], "ease": "ease-in-out"}
_P1 = {"type": "cover", "zoom": [1.0, 1.02, 1.04], "pan": [(0.5, 0.85), (0.5, 0.5), (0.5, 0.15)], "ease": "ease-in-out"}
_P2 = {"type": "cover", "zoom": [1.04, 1.02, 1.0], "pan": [(0.5, 0.15), (0.5, 0.5), (0.5, 0.85)], "ease": "ease-in-out"}
_P3 = {"type": "letterbox", "zoom": [1.0, 1.0, 1.0], "pan": [(0.5, 0.5)] * 3, "ease": "linear"}
_P4 = {"type": "cover", "zoom": [1.0, 1.03, 1.06], "pan": [(0.5, 0.15), (0.5, 0.25), (0.5, 0.35)], "ease": "ease-in-out"}
_P5 = {"type": "cover", "zoom": [1.1, 1.05, 1.0], "pan": [(0.7, 0.5), (0.5, 0.5), (0.3, 0.5)], "ease": "ease-in-out"}
_P6 = {"type": "cover", "zoom": [1.2, 1.25, 1.3], "pan": [(0.5, 0.45), (0.5, 0.5), (0.5, 0.55)], "ease": "ease-in-out"}

SLIDES = [
    {"img": "FIRE", **_P0},  # s0 Barings, 1995: The Singapore Trading Desk Th
    {"img": "OUB", **_P1},  # s1 On the afternoon of Thursday the 23rd of Feb
    {"img": "OUBSKY", **_P2},  # s2 He did not come back.
    {"img": "RP2002", **_P0},  # s3 Leeson ran the bank's futures business on th
    {"img": "BISH", **_P0},  # s4 Three days later Barings, a London bank foun
    {"img": "FBARING", **_P3},  # s5 Barings was founded in 1762 by Francis Barin
    {"img": "LETTER", **_P3},  # s6 It had come close to failing once before.
    {"img": "LETTER", **_P4},  # s7 In 1890, heavy losses on Argentine debt thre
    {"img": "PARTNERS", **_P0},  # s8 A century later it was a respected but old-f
    {"img": "EVE2001", **_P1},  # s9 Barings' futures arm in Singapore, Baring Fu
    {"img": "BISH22", **_P0},  # s10 It was a small unit, and for most of its lif
    {"img": "BISH", **_P5},  # s11 Leeson had joined Barings in London in 1989 
    {"img": "RP2002", **_P5},  # s12 He arrived in Singapore in April 1992 to man
    {"img": "OUB", **_P1},  # s13 In July 1992 Baring Futures (Singapore) star
    {"img": "CHART", **_P3},  # s14 On the 3rd of July 1992 he opened an error a
    {"img": "OUBSKY", **_P1},  # s15 Error accounts are a normal part of a tradin
    {"img": "EVE2001", **_P2},  # s16 Leeson used this one to hide the losses on h
    {"img": "CHART", **_P3},  # s17 By the end of September 1992, according to t
    {"img": "OUB", **_P2},  # s18 In June 1993 Leeson was made general manager
    {"img": "OUBSKY", **_P2},  # s19 He was in charge of the front office, which 
    {"img": "RP2002", **_P6},  # s20 The person placing the trades was therefore 
    {"img": "BISH", **_P0},  # s21 An internal audit in July and August 1994 wa
    {"img": "BISH22", **_P5},  # s22 Those reported profits had made him a star i
    {"img": "CHART", **_P3},  # s23 By the end of December 1994, the losses hidd
    {"img": "PARTNERS", **_P5},  # s24 In January 1995 a senior auditor found a dis
    {"img": "BISH", **_P6},  # s25 Leeson explained it with a story about a tra
    {"img": "OUB", **_P1},  # s26 In the same month, SIMEX alerted Barings to 
    {"img": "PARTNERS", **_P6},  # s27 Barings' senior management told SIMEX that t
    {"img": "EVE2001", **_P1},  # s28 Leeson's positions in early 1995 depended on
    {"img": "FIRE", **_P6},  # s29 At 5.46 in the morning on the 17th of Januar
    {"img": "KOBE001", **_P0},  # s30 Japanese shares fell, and by the 23rd of Jan
    {"img": "A001", **_P0},  # s31 Instead of cutting his losses, Leeson bought
    {"img": "CHART", **_P3},  # s32 It kept sliding, and on the 23rd of February
    {"img": "OUBSKY", **_P1},  # s33 That afternoon, a senior settlements clerk o
    {"img": "RP2002", **_P0},  # s34 Leeson said he had to go to the hospital, an
    {"img": "OUB", **_P2},  # s35 At first his colleagues feared he had stolen
    {"img": "CHART", **_P3},  # s36 On the 24th of February they found account e
    {"img": "BISH", **_P5},  # s37 Barings did not have the money to cover the 
    {"img": "BISH22", **_P0},  # s38 The Bank of England tried to arrange a rescu
    {"img": "EVE2001", **_P2},  # s39 The next day SIMEX placed Baring Futures (Si
    {"img": "PARTNERS", **_P0},  # s40 On the 6th of March the Dutch group ING comp
    {"img": "OUBSKY", **_P2},  # s41 Leeson and his wife went on from Kuala Lumpu
    {"img": "RP2002", **_P5},  # s42 They were detained on arrival at Frankfurt a
    {"img": "SGX", **_P1},  # s43 Leeson first fought Singapore's request to e
    {"img": "SGX2", **_P1},  # s44 He was extradited on the 23rd of November 19
    {"img": "SGX", **_P2},  # s45 On the 1st of December he pleaded guilty to 
    {"img": "SGX2", **_P2},  # s46 He was released on the 3rd of July 1999 with
    {"img": "BISH", **_P0},  # s47 The collapse was reported around the world a
    {"img": "SGX", **_P1},  # s48 In early March the Commercial Affairs Depart
    {"img": "SGX2", **_P1},  # s49 Their report, released on the 17th of Octobe
    {"img": "OUB", **_P1},  # s50 In June 1996 the Commercial Affairs Departme
    {"img": "EVE2001", **_P1},  # s51 SIMEX itself made no loss from the collapse,
    {"img": "SGX", **_P2},  # s52 Even so, the Futures Trading Act was amended
    {"img": "RP2002", **_P0},  # s53 At the time I was on the short-term interest
    {"img": "PARTNERS", **_P5},  # s54 In the foreign exchange and money markets, B
    {"img": "LETTER", **_P3},  # s55 It was known as a top British credit, and no
    {"img": "OUBSKY", **_P1},  # s56 When the news broke, it sounded like a story
    {"img": "OUB", **_P6},  # s57 The lesson I took from it, and never forgot,
    {"img": "EVE2001", **_P2},  # s58 There are people who make money from specula
    {"img": "FIRE", **_P5},  # s59 Could it happen again?
    {"img": "OUB", **_P1},  # s60 The particular weakness at Barings Singapore
    {"img": "SGX", **_P1},  # s61 The Monetary Authority of Singapore's guidel
    {"img": "BISH22", **_P0},  # s62 Rogue trading has not disappeared, however.
    {"img": "BISH", **_P5},  # s63 In January 2008 the French bank Société Géné
    {"img": "BISH22", **_P5},  # s64 Both banks survived, but in both cases the p
    {"img": "HYOGO", **_P0},  # s65 The 1914 run on a Singapore bank showed how 
    {"img": "RP2002", **_P5},  # s66 Where it fits in the bigger story: Barings i
    {"img": "EVE2001", **_P1},  # s67 The most useful lesson from it is a simple o
]

SCHEDULE = [
    (0.0, 0), (7.525, 1), (20.425, 2), (22.35, 3), (36.125, 4),
    (42.75, 5), (52.65, 6), (56.075, 7), (65.5, 8), (74.875, 9),
    (82.725, 10), (89.05, 11), (100.675, 12), (115.625, 13), (128.525, 14),
    (135.45, 15), (145.575, 16), (151.35, 17), (164.025, 18), (171.125, 19),
    (179.4, 20), (184.625, 21), (198.3, 22), (202.65, 23), (213.575, 24),
    (220.625, 25), (231.0, 26), (241.8, 27), (248.475, 28), (259.2, 29),
    (270.75, 30), (279.225, 31), (285.025, 32), (296.125, 33), (305.7, 34),
    (312.325, 35), (317.325, 36), (322.125, 37), (326.075, 38), (340.975, 39),
    (347.35, 40), (359.625, 41), (370.3, 42), (375.825, 43), (386.7, 44),
    (391.85, 45), (401.075, 46), (407.625, 47), (417.4, 48), (431.525, 49),
    (446.425, 50), (460.85, 51), (468.775, 52), (489.2, 53), (504.975, 54),
    (511.275, 55), (515.575, 56), (528.275, 57), (534.75, 58), (545.1, 59),
    (547.125, 60), (556.2, 61), (577.65, 62), (581.225, 63), (601.45, 64),
    (609.4, 65), (621.075, 66), (640.675, 67),
]
TOTAL_DURATION = 650.975
TIMING_JSON = "audio/barings-1995-the-singapore-trading-desk-that-broke-a-233-year-old-bank.timing.json"
