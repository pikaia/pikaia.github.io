"""Video config for the 1914 bank-run post.

Street scenes from the Souvenir of Singapore 1914 album and c.1910 Kling
Street, Raffles Place and South Bridge Road carry the 1914 story; three
newspaper pages are zoomed down their columns: the Straits Times of 24 Sep 1914
(page 8, "The War and the Banks"), the Malaya Tribune of 27 Aug 1914 (page 12,
the government's proclamation) and the Straits Echo of 5 Oct 1914 (page 3, the
reopening). Seow Poh Leng and Maxwell have no portraits, so their sentences
show a street or the proclamation itself. The modern section uses the CBD
skyline, the MAS Building (portrait, frozen letterbox) and SVB's former
Santa Clara headquarters. The cash chart (scripts/render_bank_run_1914_chart.py)
is frozen.

44 slides, one per sentence.
"""

CREDITS = {
    "CHART": "Chart by Lesser Known Singapore, figures from the Straits Times (24 Sep 1914) and Straits Echo (5 Oct 1914)",
    "SKY": "Basile Morin, CC BY-SA 4.0, via Wikimedia Commons",
    "MAS": "Nicolas Lannuzel, CC BY-SA 2.0, via Wikimedia Commons",
    "SVB": "Coolcaesar, CC BY-SA 4.0, via Wikimedia Commons",
}

IMAGES = {
    "ANDERSON": "https://upload.wikimedia.org/wikipedia/commons/5/59/Souvenir_of_Singapore%2C_1914_-_Plate_01_-_Anderson_Bridge.jpg",
    "CHART": "/assets/images/bank-run-1914-chart.png",
    "CHQ": "https://upload.wikimedia.org/wikipedia/commons/c/c4/Souvenir_of_Singapore%2C_1914_-_Plate_11_-_Chinese_Quarters.jpg",
    "FOUR": "https://upload.wikimedia.org/wikipedia/commons/thumb/e/e6/Singapore._Linksboven_Raffles_Place._Rechtsboven_Raffles_Place._Linksonder_Ra%2C_Bestanddeelnr_844_07.jpg/1280px-Singapore._Linksboven_Raffles_Place._Rechtsboven_Raffles_Place._Linksonder_Ra%2C_Bestanddeelnr_844_07.jpg",
    "HARBOUR": "https://upload.wikimedia.org/wikipedia/commons/e/e5/Souvenir_of_Singapore%2C_1914_-_Plate_06_-_Harbour_View.jpg",
    "KLING1907": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/d0/Kling_Street%2C_Singapore_%28NYPL_Hades-2359713-4044478%29.jpg/1280px-Kling_Street%2C_Singapore_%28NYPL_Hades-2359713-4044478%29.jpg",
    "MAS": "https://upload.wikimedia.org/wikipedia/commons/0/09/MASBuilding-Singapore-20090914.jpg",
    "MT": "/assets/images/malaya-tribune-1914-08-27-page-12.jpg",
    "RAFF91": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/da/KITLV_-_79891_-_Kleingrothe%2C_C.J._-_Medan_-_Raffles_Place%2C_Singapore_-_circa_1910.tif/lossy-page1-1280px-KITLV_-_79891_-_Kleingrothe%2C_C.J._-_Medan_-_Raffles_Place%2C_Singapore_-_circa_1910.tif.jpg",
    "RAFF92": "https://upload.wikimedia.org/wikipedia/commons/thumb/c/c7/KITLV_-_79892_-_Kleingrothe%2C_C.J._-_Medan_-_Raffles_Place%2C_Singapore_-_circa_1910.tif/lossy-page1-1280px-KITLV_-_79892_-_Kleingrothe%2C_C.J._-_Medan_-_Raffles_Place%2C_Singapore_-_circa_1910.tif.jpg",
    "SBR": "https://upload.wikimedia.org/wikipedia/commons/thumb/6/66/KITLV_-_79923_-_Kleingrothe%2C_C.J._-_Medan_-_South_Bridge_Road%2C_Singapore_-_circa_1910.tif/lossy-page1-1280px-KITLV_-_79923_-_Kleingrothe%2C_C.J._-_Medan_-_South_Bridge_Road%2C_Singapore_-_circa_1910.tif.jpg",
    "SE": "/assets/images/straits-echo-1914-10-05-page-3.jpg",
    "SKY": "https://upload.wikimedia.org/wikipedia/commons/thumb/9/94/Skyline_of_the_Central_Business_District_of_Singapore_with_Esplanade_Bridge_in_the_evening.jpg/1920px-Skyline_of_the_Central_Business_District_of_Singapore_with_Esplanade_Bridge_in_the_evening.jpg",
    "ST": "/assets/images/straits-times-1914-09-24-page-8.jpg",
    "SVB": "https://upload.wikimedia.org/wikipedia/commons/thumb/4/46/3003_Tasman_Drive.jpg/1920px-3003_Tasman_Drive.jpg",
}

_P0 = {"type": "cover", "zoom": [1.0, 1.05, 1.1], "pan": [(0.3, 0.5), (0.5, 0.5), (0.7, 0.5)], "ease": "ease-in-out"}
_P1 = {"type": "cover", "zoom": [1.35, 1.4, 1.45], "pan": [(0.5, 0.5), (0.5, 0.5), (0.5, 0.5)], "ease": "ease-in-out"}
_P2 = {"type": "letterbox", "zoom": [1.0, 1.0, 1.0], "pan": [(0.5, 0.5)] * 3, "ease": "linear"}
_P3 = {"type": "cover", "zoom": [1.80, 1.84, 1.89], "pan": [(0.432, 0.736), (0.434, 0.747), (0.436, 0.758)], "ease": "ease-in-out"}
_P4 = {"type": "cover", "zoom": [2.60, 2.67, 2.73], "pan": [(0.435, 0.883), (0.436, 0.893), (0.437, 0.903)], "ease": "ease-in-out"}
_P5 = {"type": "cover", "zoom": [2.60, 2.67, 2.73], "pan": [(0.711, 0.165), (0.708, 0.179), (0.705, 0.192)], "ease": "ease-in-out"}
_P6 = {"type": "cover", "zoom": [2.60, 2.67, 2.73], "pan": [(0.679, 0.5), (0.676, 0.512), (0.674, 0.524)], "ease": "ease-in-out"}
_P7 = {"type": "cover", "zoom": [2.2, 2.25, 2.3], "pan": [(0.2, 0.25), (0.22, 0.25), (0.24, 0.25)], "ease": "ease-in-out"}
_P8 = {"type": "cover", "zoom": [1.50, 1.54, 1.58], "pan": [(0.26, 0.0), (0.271, 0.0), (0.281, 0.0)], "ease": "ease-in-out"}
_P9 = {"type": "cover", "zoom": [3.00, 3.07, 3.15], "pan": [(0.545, 0.273), (0.544, 0.285), (0.544, 0.297)], "ease": "ease-in-out"}
_P10 = {"type": "cover", "zoom": [3.00, 3.07, 3.15], "pan": [(0.545, 0.364), (0.544, 0.376), (0.544, 0.387)], "ease": "ease-in-out"}
_P11 = {"type": "cover", "zoom": [3.00, 3.07, 3.15], "pan": [(0.545, 0.443), (0.544, 0.455), (0.544, 0.466)], "ease": "ease-in-out"}
_P12 = {"type": "cover", "zoom": [3.00, 3.07, 3.15], "pan": [(0.545, 0.103), (0.544, 0.116), (0.544, 0.128)], "ease": "ease-in-out"}
_P13 = {"type": "cover", "zoom": [1.1, 1.05, 1.0], "pan": [(0.7, 0.5), (0.5, 0.5), (0.3, 0.5)], "ease": "ease-in-out"}
_P14 = {"type": "cover", "zoom": [1.60, 1.64, 1.68], "pan": [(0.0, 0.737), (0.0, 0.748), (0.0, 0.76)], "ease": "ease-in-out"}
_P15 = {"type": "cover", "zoom": [2.60, 2.67, 2.73], "pan": [(0.0, 0.814), (0.0, 0.825), (0.0, 0.835)], "ease": "ease-in-out"}
_P16 = {"type": "cover", "zoom": [2.60, 2.67, 2.73], "pan": [(0.0, 0.935), (0.0, 0.945), (0.0, 0.955)], "ease": "ease-in-out"}

SLIDES = [
    {"img": "CHQ", **_P0},  # s0 The Run on the Banks, 1914: When War in Euro
    {"img": "CHQ", **_P1},  # s1 On Tuesday the 4th of August 1914, the day b
    {"img": "CHART", **_P2},  # s2 By the next evening they had taken out more 
    {"img": "KLING1907", **_P0},  # s3 It would stay shut for eight weeks, and the 
    {"img": "SBR", **_P0},  # s4 The Chinese Commercial Bank was the first Ho
    {"img": "RAFF91", **_P0},  # s5 It had opened in December 1912, and by 1914 
    {"img": "KLING1907", **_P1},  # s6 It also opened only a year before Singapore'
    {"img": "ST", **_P3},  # s7 The Straits Times later wrote that the Kwong
    {"img": "ST", **_P4},  # s8 According to the same editorial, it was "gen
    {"img": "ST", **_P5},  # s9 The Chinese Commercial Bank, the paper added
    {"img": "ST", **_P6},  # s10 The editorial set out what happened, day by 
    {"img": "CHART", **_P2},  # s11 On the 4th of August, the day before the new
    {"img": "CHART", **_P2},  # s12 The next day the run continued, and despite 
    {"img": "FOUR", **_P7},  # s13 Its secretary, Seow-Poh-Leng, wrote to the M
    {"img": "RAFF92", **_P0},  # s14 The bank was closed while the inspection wen
    {"img": "MT", **_P8},  # s15 On the 26th of August the government posted 
    {"img": "MT", **_P9},  # s16 It said the government had "examined thoroug
    {"img": "MT", **_P10},  # s17 If the shareholders could raise money, eithe
    {"img": "MT", **_P11},  # s18 It ended with a warning to everyone in the c
    {"img": "MT", **_P12},  # s19 The Malaya Tribune headlined it "Stern Warni
    {"img": "KLING1907", **_P13},  # s20 The Teochew community's bank, Sze Hai Tong, 
    {"img": "HARBOUR", **_P0},  # s21 According to the National Library Board's ac
    {"img": "ST", **_P2},  # s22 On the 24th of September the Straits Times r
    {"img": "SE", **_P14},  # s23 It reopened at ten o'clock on Thursday the 1
    {"img": "SE", **_P15},  # s24 According to the Straits Echo, Kling Street 
    {"img": "SE", **_P16},  # s25 A couple of Malay policemen and a watchman s
    {"img": "ANDERSON", **_P0},  # s26 Afterwards the bank kept a much larger share
    {"img": "CHQ", **_P13},  # s27 In 1914, a bank in trouble depended on its c
    {"img": "SKY", **_P0},  # s28 Today the safety net is set out in advance.
    {"img": "SKY", **_P1},  # s29 Singapore has had a deposit insurance scheme
    {"img": "SKY", **_P13},  # s30 Since April 2024 it covers Singapore dollar 
    {"img": "MAS", **_P2},  # s31 In October 2008, during the global financial
    {"img": "RAFF92", **_P13},  # s32 No claims were made under the guarantee.
    {"img": "CHQ", **_P1},  # s33 Could it happen again?
    {"img": "MAS", **_P2},  # s34 Several of the conditions behind the 1914 ru
    {"img": "MAS", **_P2},  # s35 Banks in Singapore are supervised by the Mon
    {"img": "SKY", **_P0},  # s36 Most ordinary depositors are fully insured, 
    {"img": "SVB", **_P0},  # s37 But runs have not disappeared, and they have
    {"img": "SVB", **_P1},  # s38 On the 9th of March 2023, customers of Silic
    {"img": "SVB", **_P13},  # s39 Regulators closed the bank on the 10th of Ma
    {"img": "CHART", **_P2},  # s40 In 1914 the run on the Chinese Commercial Ba
    {"img": "KLING1907", **_P13},  # s41 The lesson that carries over from Kling Stre
    {"img": "RAFF91", **_P13},  # s42 Where it fits in the bigger story: The Chine
    {"img": "SKY", **_P13},  # s43 A century later, deposit insurance, the 2008
]

SCHEDULE = [
    (0.0, 0), (5.875, 1), (18.85, 2), (26.05, 3), (36.525, 4),
    (41.8, 5), (50.075, 6), (65.325, 7), (78.05, 8), (93.0, 9),
    (98.425, 10), (102.3, 11), (113.025, 12), (128.125, 13), (141.8, 14),
    (145.55, 15), (155.75, 16), (172.525, 17), (182.025, 18), (199.075, 19),
    (205.675, 20), (211.875, 21), (229.125, 22), (244.75, 23), (249.75, 24),
    (260.375, 25), (278.4, 26), (285.325, 27), (294.35, 28), (298.25, 29),
    (307.05, 30), (323.2, 31), (337.475, 32), (341.025, 33), (343.05, 34),
    (349.45, 35), (368.4, 36), (375.375, 37), (380.125, 38), (400.8, 39),
    (404.6, 40), (415.4, 41), (427.15, 42), (440.675, 43),
]
TOTAL_DURATION = 459.225
TIMING_JSON = "audio/the-run-on-the-banks-1914-when-war-in-europe-emptied-a-singapore-bank.timing.json"
