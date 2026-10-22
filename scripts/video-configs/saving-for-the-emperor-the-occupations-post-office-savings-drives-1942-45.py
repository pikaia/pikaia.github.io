"""Video config for the Saving for the Emperor post.

From the pre-war General Post Office and the fall of Singapore to POSB and
deposit insurance today: the Syonan Shimbun pages of the drives (23 August
1943, 8 and 10 February 1944, 24 April 1944, 16 and 25 July 1945), the
occupation stamps and notes, the Syonan Jinja, a street in Syonan and a ration
card, the British return in September 1945, the Straits Times pages of 1945,
1947 and 1951, and the Fullerton Building then and now.

Named-person rule: Seiji Hamada, Lim Beng Quan and Mr Suzuki have no free
photographs, so their sentences show stamps, notes and newspaper pages only,
never a crowd or a street.

The deposit totals (sentences 54-57) are a "chart" slide drawing the post's
own line, with yearly x ticks and a month readout, since it spans only
three years. Newspaper pages, stamps, notes and small photos are letterboxed
with a modest zoom.

58 slides, 1018.05s. Narration: Kokoro with the OpenVoice clone.
AVATAR: first and last 30s, cartoon with motion.
"""

_U = "https://upload.wikimedia.org/wikipedia/commons"
_C = f"{_U}/thumb"

IMAGES = {
    "HERO": f"{_C}/2/2c/Collectie_Familie_Khouw%2C_KITLV_D14121.tiff/lossy-page1-1280px-Collectie_Familie_Khouw%2C_KITLV_D14121.tiff.jpg",
    "SS430823": "/assets/images/syonan-shimbun-1943-08-23-page-2.jpg",
    "SS440208": "/assets/images/syonan-shimbun-1944-02-08-page-2.jpg",
    "SS440210": "/assets/images/syonan-shimbun-1944-02-10-page-2.jpg",
    "SS440424": "/assets/images/syonan-shimbun-1944-04-24-page-2.jpg",
    "SS450716": "/assets/images/syonan-shimbun-1945-07-16-page-2.jpg",
    "SS450725": "/assets/images/syonan-shimbun-1945-07-25-page-2.jpg",
    "ST1945": "/assets/images/straits-times-1945-10-12-page-4.jpg",
    "ST1947": "/assets/images/straits-times-1947-02-05-page-5.jpg",
    "ST1951": "/assets/images/straits-times-1951-05-09-page-4.jpg",
    "STAMP3": f"{_U}/2/23/Stamp_Malaya_Japan_occupation_1943_3c.jpg",
    "STAMP4": f"{_U}/1/13/Stamp_Malaya_Japan_occupation_1943_4c.jpg",
    "JINJASTAMP": f"{_U}/8/8f/%E6%98%AD%E5%8D%97%E7%A5%9E%E7%A4%BE%E9%82%AE%E7%A5%A8%EF%BC%88%E6%97%A5%E6%B2%BB%E9%A9%AC%E6%9D%A5%EF%BC%89.jpg",
    "FALLSTAMPS": f"{_U}/f/f0/1942_Fall_of_Singapore_for_Japanese_stamps.JPG",
    "REVENUE": f"{_U}/1/17/3d-Malaya-DutyStamps_SIN-20171213.jpg",
    "NOTE10": f"{_C}/8/85/Banknote_%28AM_2004.35.4-1%29.jpg/1280px-Banknote_%28AM_2004.35.4-1%29.jpg",
    "STREET": f"{_U}/f/fc/Street_in_Shonan.JPG",
    "RATION": f"{_C}/e/ea/RationBook-ExtraRice_SIN_1945_20171213.jpg/1280px-RationBook-ExtraRice_SIN_1945_20171213.jpg",
    "POSB": f"{_U}/a/a4/POSB_Newton_Branch.png",
    "GPO1900": f"{_U}/5/57/General_Post_Office_Singapore_1900.jpg",
    "NOTE1": f"{_C}/1/11/MAL-M5c-Malaya-Japanese_Occupation-One_Dollar_ND_%281942%29.jpg/1280px-MAL-M5c-Malaya-Japanese_Occupation-One_Dollar_ND_%281942%29.jpg",
    "NOTE100": f"{_C}/3/37/MAL-M9-Malaya-Japanese_Occupation-100_Dollars_ND_%281945%29.jpg/1280px-MAL-M9-Malaya-Japanese_Occupation-100_Dollars_ND_%281945%29.jpg",
    "NOTE1000": f"{_C}/d/d6/MAL-M10b-Malaya-Japanese_Occupation-1000_Dollars_ND_%281945%29.jpg/1280px-MAL-M10b-Malaya-Japanese_Occupation-1000_Dollars_ND_%281945%29.jpg",
    "JINJA": f"{_U}/8/80/Shinto_shrine_in_Shonan_%28Singapore%29_-_194210.jpg",
    "REOCC": f"{_U}/e/e3/British_Reoccupation_of_Singapore%2C_1945_SE4641.jpg",
    "POSB2": f"{_C}/2/25/POSB_Newton_Branch_Entrance.png/1280px-POSB_Newton_Branch_Entrance.png",
    "FULLERTON": f"{_C}/7/7a/Singapore_%28SG%29%2C_The_Fullerton_Hotel_--_2019_--_4708.jpg/1280px-Singapore_%28SG%29%2C_The_Fullerton_Hotel_--_2019_--_4708.jpg",
}

# Credits for images not captioned in the post or its gallery.
CREDITS = {
    "GPO1900": "Unknown author, public domain, via Wikimedia Commons",
    "NOTE1": "Japanese Government, National Museum of American History, public domain, via Wikimedia Commons",
    "NOTE100": "Japanese Government, National Museum of American History, public domain, via Wikimedia Commons",
    "NOTE1000": "Japanese Government, National Museum of American History, public domain, via Wikimedia Commons",
    "JINJA": "Unknown author, public domain, via Wikimedia Commons",
    "REOCC": "Sgt Frederick Wackett, No 9 Army Film and Photographic Unit, public domain, via Wikimedia Commons",
    "POSB2": "Deoma12, CC BY-SA 4.0, via Wikimedia Commons",
    "FULLERTON": "Dietmar Rabich, CC BY-SA 4.0, via Wikimedia Commons",
}

# The channel's 2x2 thumbnail grid, 1942 to today: the fall of Singapore
# stamps, the "Fourth time!" bonus advert of July 1945, the 1947 "Jap
# Deposits Worthless" headline, and a POSB branch. Whole newspaper pages are
# unreadable at cell size, so the two pages are zoomed to the advert and
# the headline.
THUMBNAIL = [
    "FALLSTAMPS",
    {"img": "SS450716", "zoom": 2.9, "pan": (0.93, 0.85)},
    {"img": "ST1947", "zoom": 3.0, "pan": (0.0, 0.07)},
    {"img": "POSB2", "pan": (0.45, 0.5)},
]

# The post's inline chart: postal savings across Malaya, $ million.
SAVINGS = [
    (1942.704, 0), (1943.244, 0.5), (1943.633, 1.0), (1943.775, 1.4),
    (1943.956, 2.0), (1944.101, 3.0), (1944.2, 4.0), (1944.304, 5.0),
    (1944.397, 6.0), (1944.468, 7.0), (1944.562, 8.0), (1944.773, 10.0),
    (1944.99, 16.57), (1945.493, 30.19),
]

_E = "ease-in-out"
_IN = {"type": "cover", "zoom": [1.0, 1.06, 1.12], "pan": [(0.5, 0.5)] * 3, "ease": _E}
_OUT = {"type": "cover", "zoom": [1.12, 1.06, 1.0], "pan": [(0.5, 0.5)] * 3, "ease": _E}
# Newspaper pages, stamps, notes and small photos: letterbox, modest zoom.
_PORT = {"type": "letterbox", "zoom": [1.0, 1.04, 1.08], "pan": [(0.5, 0.5)] * 3, "ease": _E}
_PORT_OUT = {"type": "letterbox", "zoom": [1.08, 1.04, 1.0], "pan": [(0.5, 0.5)] * 3, "ease": _E}

CHART = {
    "type": "chart",
    "data": SAVINGS,
    "x_range": (1942.5, 1945.75),
    "x_tick_step": 1,
    "time_label": "month",
    "y_range": (0, 35),
    "y_tick_step": 5,
    "y_tick_format": "${:.0f}M",
    "value_format": "${:.1f}M",
    "title": "Postal savings across Malaya, 1942-1945 (occupation dollars)",
    "annotations": [
        (1943.633, 1.0, "$1M", "above"),
        (1944.304, 5.0, "$5M", "above"),
        (1944.99, 16.57, "$16.6M", "left"),
    ],
    # s54 opens the slide; s55 ("$5 million in April 1944 and $10 million in
    # October") sweeps to October 1944; s56 is the end of 1944; s57 June 1945.
    "year_checkpoints": [
        (566.45, 1942.704), (569.225, 1943.3), (580.725, 1944.773),
        (590.15, 1944.99), (602.0, 1945.493),
    ],
}

SLIDES = [
    {"img": "HERO", **_IN},             # 0  s0  title
    {"img": "SS450716", **_PORT},       # 1  s1  the Malai Banking Association advert, 16 July 1945 (s2)
    {"img": "NOTE10", **_IN},           # 2  s3  deposits taken in August, draw in October
    {"img": "SS450716", **_PORT_OUT},   # 3  s4  "absolutely safe" on the same page
    {"img": "STREET", **_PORT},         # 4  s5  three years of pressing people to save
    {"img": "ST1947", **_PORT},         # 5  s6  never recognised after it
    {"img": "GPO1900", **_PORT},        # 6  s7  a post office savings bank since 1877
    {"img": "REVENUE", **_PORT},        # 7  s8  Straits Settlements only; the Malay states (s9)
    {"img": "FALLSTAMPS", **_PORT},     # 8  s10 the fall of Singapore
    {"img": "NOTE1", **_PORT},          # 9  s11 withdrawal limits; raised December 1942 (s12)
    {"img": "STAMP4", **_PORT},         # 10 s13 Seiji Hamada (no photo of him); Malai (s14)
    {"img": "HERO", **_OUT},            # 11 s15 a savings bank at the post offices (s16)
    {"img": "STAMP3", **_PORT},         # 12 s17 three per cent; run from Syonan
    {"img": "STREET", **_PORT_OUT},     # 13 s18 the Controller of Posts quoted; "every good citizen" (s19)
    {"img": "SS430823", **_PORT},       # 14 s20 a slow start; the first $1 million (s21)
    {"img": "NOTE1000", **_PORT},       # 15 s22 banana money printed every year; prices (s23-24)
    {"img": "NOTE100", **_PORT},        # 16 s25 the government lottery
    {"img": "NOTE10", **_OUT},          # 17 s26 the Radio Syonan talk (no photo of the speaker) (s27)
    {"img": "RATION", **_PORT},         # 18 s28 "the high cost of living is mounting"
    {"img": "SS430823", **_PORT_OUT},   # 19 s29 the Promotion Week, September 1943 (s30-31)
    {"img": "HERO", **_IN},             # 20 s32 the travelling post office
    {"img": "NOTE1", **_PORT_OUT},      # 21 s33 three times the monthly average
    {"img": "NOTE10", **_IN},           # 22 s34 the banks join in; "Save for Victory" (s35-36)
    {"img": "FALLSTAMPS", **_PORT_OUT}, # 23 s37 the administration's calendar
    {"img": "SS440210", **_PORT},       # 24 s38 the second promotion week, February 1944
    {"img": "JINJA", **_PORT},          # 25 s39 the date stamp: father and son on their way to the Syonan Jinja
    {"img": "JINJASTAMP", **_PORT},     # 26 s40 picture slides in the cinemas
    {"img": "SS440424", **_PORT},       # 27 s41 $5 million; free cinema shows for Tencho Setsu (s42-43)
    {"img": "SS440208", **_PORT},       # 28 s44 the banks' prize draws (s45-46)
    {"img": "NOTE100", **_PORT_OUT},    # 29 s47 $8.5 million; the Kyoei Gekijo draw
    {"img": "SS450716", **_PORT},       # 30 s48 a second round; the fourth by July 1945
    {"img": "RATION", **_PORT_OUT},     # 31 s49 into the workplaces; Penang group savings (s50-51)
    {"img": "STAMP4", **_PORT_OUT},     # 32 s52 the Auxiliary Police (no photo of the speaker) (s53)
    CHART,                              # 33 s54 the totals, $1M to $30.2M (s55-57)
    {"img": "SS440424", **_PORT_OUT},   # 34 s58 Singapore's share (s59)
    {"img": "NOTE1000", **_PORT_OUT},   # 35 s60 paper money, not wealth (s61)
    {"img": "NOTE10", **_OUT},          # 36 s62 the egg
    {"img": "NOTE1", **_PORT},          # 37 s63 $41 and $60 an account (s64)
    {"img": "SS450725", **_PORT},       # 38 s65 half a million depositors; the commemoration weeks (s66)
    {"img": "SS450716", **_PORT_OUT},   # 39 s67 Mr Suzuki (no photo of him), 15 July 1945 (s68)
    {"img": "STREET", **_PORT},         # 40 s69 the evacuation from Syonan (s70)
    {"img": "NOTE10", **_IN},           # 41 s71 the fourth bonus scheme opens, 1 August 1945
    {"img": "REOCC", **_PORT},          # 42 s72 the surrender; British forces back, 5 September
    {"img": "NOTE100", **_PORT},        # 43 s73 banana money declared of no value
    {"img": "ST1945", **_PORT},         # 44 s74 the bank reopens, October 1945; "no withdrawals or enquiries" (s75)
    {"img": "ST1947", **_PORT_OUT},     # 45 s76 "still considered worthless", 1947 (s77-78)
    {"img": "NOTE1", **_PORT_OUT},      # 46 s79 hit twice: the Sungei Siput letter (s80-81)
    {"img": "GPO1900", **_PORT_OUT},    # 47 s82 "A Raw Deal For The Small Man", 1949
    {"img": "ST1951", **_PORT},         # 48 s83 the revaluation laws, 1950 and 1951 (s84)
    {"img": "REVENUE", **_PORT_OUT},    # 49 s85 claims from May 1951
    {"img": "ST1951", **_PORT_OUT},     # 50 s86 the sliding scale
    {"img": "SS450725", **_PORT_OUT},   # 51 s87 the occupation's deposits never recognised
    {"img": "HERO", **_OUT},            # 52 s88 the pre-war bank went on; POSB and DBS (s89)
    {"img": "POSB", **_PORT},           # 53 s90 protection written down in advance
    {"img": "POSB2", **_IN},            # 54 s91 the Deposit Insurance Scheme
    {"img": "FULLERTON", **{**_IN, "pan": [(0.5, 0.65)] * 3}},  # 55 s92 why it matters today
    {"img": "SS430823", **_PORT},       # 56 s93 the totals rose while the currency fell
    {"img": "HERO", **_OUT},            # 57 s94 only as safe as the money and the institution
]

SCHEDULE = [
    (0.0, 0), (8.3, 1), (29.5, 2), (40.475, 3), (49.2, 4), (66.875, 5),
    (73.1, 6), (87.2, 7), (101.85, 8), (110.675, 9), (137.1, 10),
    (150.375, 11), (164.375, 12), (181.675, 13), (209.35, 14), (227.525, 15),
    (246.725, 16), (256.675, 17), (283.325, 18), (297.45, 19), (326.925, 20),
    (336.725, 21), (354.075, 22), (380.25, 23), (385.3, 24), (399.45, 25),
    (409.9, 26), (416.2, 27), (449.075, 28), (483.975, 29), (499.4, 30),
    (508.85, 31), (543.25, 32), (566.45, 33), (605.075, 34), (628.25, 35),
    (641.425, 36), (651.625, 37), (670.95, 38), (688.125, 39), (706.775, 40),
    (732.625, 41), (739.35, 42), (752.825, 43), (761.35, 44), (788.425, 45),
    (820.475, 46), (848.6, 47), (866.325, 48), (889.25, 49), (905.375, 50),
    (922.275, 51), (928.225, 52), (946.6, 53), (952.1, 54), (975.5, 55),
    (994.75, 56), (1005.325, 57),
]
TOTAL_DURATION = 1018.05
TIMING_JSON = "audio/saving-for-the-emperor-the-occupations-post-office-savings-drives-1942-45.timing.json"

# The avatar presenter, cartoon with motion: corner bubble for the first and last 30 s.
AVATAR = {"ranges": [(0, 30), (-30, None)], "motion": True}
