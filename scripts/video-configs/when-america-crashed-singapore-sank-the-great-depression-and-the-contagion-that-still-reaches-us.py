"""Video config for the Great Depression / contagion post.

The 1929-33 half runs on period photos (rubber tapping, the Ford line, tin
mines in Perak, Pulau Brani, the harbour, Raffles Place, Wall Street) and two
whole Straits Times pages, each pushed in on its story: "Still Falling" (2 April
1931) and "Free Passages to China" (28 May 1932). Clementi's sentence sits on
his own portrait. The later-crises half alternates the four chart PNGs
(letterbox, frozen) with photos of the city, the port and Jurong Island; the
crisis-by-industry chart returns once for each crisis the text walks through.

47 slides, 747.95s. AVATAR: first and last 30s (avatar test #5).
"""

_U = "https://upload.wikimedia.org/wikipedia/commons"
_C = f"{_U}/thumb"
_A = "/assets/images"

IMAGES = {
    "TAP1914": f"{_U}/9/99/Souvenir_of_Singapore%2C_1914_-_Plate_10_-_Rubber_Tapping.jpg",
    "TAPK": f"{_C}/7/7b/Tapping_Rubber%2C_KITLV_1404050.tiff/lossy-page1-1920px-Tapping_Rubber%2C_KITLV_1404050.tiff.jpg",
    "FORD": f"{_U}/8/86/Ford_Motor_Company_assembly_line.jpg",
    "BRANI": f"{_C}/5/56/Gezicht_op_de_tinsmelterijen_op_het_eiland_Pulau_Brani_bij_Singapore_View_of_Pulo_Brani_tin_smelting_works_%28titel_op_object%29%2C_RP-F-F01140-AH.jpg/1280px-Gezicht_op_de_tinsmelterijen_op_het_eiland_Pulau_Brani_bij_Singapore_View_of_Pulo_Brani_tin_smelting_works_%28titel_op_object%29%2C_RP-F-F01140-AH.jpg",
    "BRANIK": f"{_C}/a/ad/KITLV_-_79928_-_Kleingrothe%2C_C.J._-_Medan_-_Tin_industry_at_the_island_of_Pulau_Brani%2C_Singapore_-_circa_1910.tif/lossy-page1-1280px-KITLV_-_79928_-_Kleingrothe%2C_C.J._-_Medan_-_Tin_industry_at_the_island_of_Pulau_Brani%2C_Singapore_-_circa_1910.tif.jpg",
    "TRONOH": f"{_C}/4/4f/KITLV_-_79980_-_Kleingrothe%2C_C.J._-_Medan_-_Tin_mine_at_Tronoh_in_Ipoh%2C_Malaysia_-_circa_1910.tif/lossy-page1-1920px-KITLV_-_79980_-_Kleingrothe%2C_C.J._-_Medan_-_Tin_mine_at_Tronoh_in_Ipoh%2C_Malaysia_-_circa_1910.tif.jpg",
    "TAIPING": f"{_C}/e/e3/KITLV_-_79982_-_Kleingrothe%2C_C.J._-_Medan_-_Open_Chinese_tin_mine_in_Taiping_-_circa_1910.tif/lossy-page1-1920px-KITLV_-_79982_-_Kleingrothe%2C_C.J._-_Medan_-_Open_Chinese_tin_mine_in_Taiping_-_circa_1910.tif.jpg",
    "HARB": f"{_C}/3/37/Haven_van_Singapore%2C_KITLV_104789.tiff/lossy-page1-1920px-Haven_van_Singapore%2C_KITLV_104789.tiff.jpg",
    "HARBPAN": f"{_C}/0/0e/De_haven_van_Singapore%2C_KITLV_29185.tiff/lossy-page1-1920px-De_haven_van_Singapore%2C_KITLV_29185.tiff.jpg",
    "WHARF": f"{_C}/d/dc/KITLV_A1041_-_Haven_van_Singapore%2C_KITLV_140424.tiff/lossy-page1-1920px-KITLV_A1041_-_Haven_van_Singapore%2C_KITLV_140424.tiff.jpg",
    "CHARTERED": f"{_C}/5/59/The_Chartered_Bank_aan_Raffles_Place_te_Singapore%2C_KITLV_104795.tiff/lossy-page1-1920px-The_Chartered_Bank_aan_Raffles_Place_te_Singapore%2C_KITLV_104795.tiff.jpg",
    "NYSE24": f"{_C}/3/3f/Crowds_gathering_outside_New_York_Stock_Exchange.jpg/1280px-Crowds_gathering_outside_New_York_Stock_Exchange.jpg",
    "NYSE29": f"{_U}/e/e1/Crowd_outside_nyse.jpg",
    "CITYHALL": f"{_C}/5/56/Unemployed_people_gathering_outside_City_Hall.jpg/1920px-Unemployed_people_gathering_outside_City_Hall.jpg",
    "CLEMENTI": f"{_U}/a/a0/Sir-Cecil-Clementi.jpg",
    "STAMP": f"{_U}/c/c3/1961tappingrubber.png",
    "SG1978": f"{_C}/c/c0/153_Singapore%2C_Jan_1978_%2852023517826%29.jpg/1920px-153_Singapore%2C_Jan_1978_%2852023517826%29.jpg",
    "UOB2001": f"{_U}/a/a8/Evening_view_of_UOB_Plaza%2C_OUB_Centre_and_OCBC_Centre_near_the_Singapore_River_-_20010608.jpg",
    "MBFC": f"{_C}/c/c1/2016_Singapur%2C_Downtown_Core%2C_Marina_Bay_Financial_Centre.jpg/1280px-2016_Singapur%2C_Downtown_Core%2C_Marina_Bay_Financial_Centre.jpg",
    "CONTAINER": f"{_C}/a/a9/Container_port_%2812848714813%29.jpg/1280px-Container_port_%2812848714813%29.jpg",
    "TPAGAR": f"{_C}/6/6b/Singapore_%28SG%29%2C_Tanjong_Pagar_Terminal_--_2019_--_4728.jpg/1280px-Singapore_%28SG%29%2C_Tanjong_Pagar_Terminal_--_2019_--_4728.jpg",
    "MBSCB": f"{_C}/0/04/Marina_Bay_Sands_during_Circuit_Breaker.jpg/1920px-Marina_Bay_Sands_during_Circuit_Breaker.jpg",
    "JURONG": f"{_C}/c/ca/Jurong_Island_viewed_from_the_top_of_Jurong_Hill_Tower.jpg/1920px-Jurong_Island_viewed_from_the_top_of_Jurong_Hill_Tower.jpg",
    "DATACTR": f"{_C}/5/5d/BalticServers_data_center.jpg/1920px-BalticServers_data_center.jpg",
    "MAS": f"{_U}/8/8e/MAS_Building%2C_Springleaf_Tower.JPG",
    "ST1931": f"{_A}/straits-times-1931-04-02-page-11.jpg",
    "ST1932": f"{_A}/straits-times-1932-05-28-page-11.jpg",
    "GDP": f"{_A}/singapore-gdp-growth-chart.png",
    "SECTORS": f"{_A}/singapore-crisis-sectors-chart.png",
    "SIZE": f"{_A}/singapore-sector-size-chart.png",
    "ELEC": f"{_A}/singapore-electronics-share-chart.png",
}

# Credits for images not captioned in the post or its gallery.
CREDITS = {
    "TAPK": "Tapping rubber, KITLV 1404050, unknown photographer, CC BY 4.0, via Wikimedia Commons",
    "TRONOH": "Tin mine at Tronoh, Perak, about 1910, C. J. Kleingrothe, KITLV 79980, public domain, via Wikimedia Commons",
    "TAIPING": "Open Chinese tin mine in Taiping, about 1910, C. J. Kleingrothe, KITLV 79982, public domain, via Wikimedia Commons",
    "HARB": "The harbour of Singapore, KITLV 104789, unknown photographer, CC BY 4.0, via Wikimedia Commons",
    "HARBPAN": "The harbour of Singapore, KITLV 29185, unknown photographer, CC BY 4.0, via Wikimedia Commons",
    "WHARF": "The harbour of Singapore, KITLV 140424, unknown photographer, CC BY 4.0, via Wikimedia Commons",
    "CHARTERED": "The Chartered Bank at Raffles Place, KITLV 104795, unknown photographer, CC BY 4.0, via Wikimedia Commons",
    "CITYHALL": "Unemployed people outside City Hall, New York, 9 October 1930, Associated Press, public domain, via Wikimedia Commons",
    "CLEMENTI": "Sir Cecil Clementi, early 1930s, unknown photographer, public domain, via Wikimedia Commons",
    "SG1978": "Singapore, January 1978, Wilford Peloquin, CC BY 2.0, via Wikimedia Commons",
    "MBSCB": "Marina Bay Sands during the circuit breaker, April 2020, maja kuzmanovic, CC BY-SA 2.0, via Wikimedia Commons",
    "JURONG": "Jurong Island from Jurong Hill Tower, 2021, Wzhkevin, CC BY-SA 4.0, via Wikimedia Commons",
    "DATACTR": "A data centre, BalticServers.com, CC BY-SA 3.0, via Wikimedia Commons",
    "MAS": "The MAS Building, 2006, Terence Ong, CC BY 2.5, via Wikimedia Commons",
    "GDP": "Chart by Lesser Known Singapore, data from the Singapore Department of Statistics",
    "SECTORS": "Chart by Lesser Known Singapore, data from the Singapore Department of Statistics",
    "SIZE": "Chart by Lesser Known Singapore, data from the Singapore Department of Statistics",
    "ELEC": "Chart by Lesser Known Singapore, data from the Singapore Department of Statistics",
}

_E = "ease-in-out"
_IN = {"type": "cover", "zoom": [1.0, 1.06, 1.12], "pan": [(0.5, 0.5)] * 3, "ease": _E}
_OUT = {"type": "cover", "zoom": [1.12, 1.06, 1.0], "pan": [(0.5, 0.5)] * 3, "ease": _E}
_INL = {"type": "cover", "zoom": [1.0, 1.08, 1.16], "pan": [(0.35, 0.45)] * 3, "ease": _E}
_INR = {"type": "cover", "zoom": [1.0, 1.08, 1.16], "pan": [(0.65, 0.45)] * 3, "ease": _E}
# Tall photos (the KITLV tapper, Clementi, the MAS tower): letterbox, modest zoom.
_PORT = {"type": "letterbox", "zoom": [1.0, 1.04, 1.08], "pan": [(0.5, 0.5)] * 3, "ease": _E}
# Graphics (the charts, the stamp): letterbox, frozen.
_GFX = {"type": "letterbox", "zoom": [1, 1, 1], "pan": [(0.5, 0.5)] * 3}


def _c(zoom, pan):
    return {"type": "cover", "zoom": zoom, "pan": pan, "ease": _E}


# Whole-page newspaper push-ins, zoom capped at 2.4x.
_ST31_HEAD = _c([1.0, 1.08, 1.16], [(0.5, 0.0), (0.5, 0.0), (0.5, 0.0)])
_ST31_PENCE = _c([2.2, 2.3, 2.4], [(1.0, 0.03), (1.0, 0.04), (1.0, 0.05)])
_ST32_FREE = _c([2.2, 2.3, 2.4], [(0.39, 0.04), (0.395, 0.05), (0.4, 0.06)])
# The Rijksmuseum print sits on its album mount: zoom past the card edges.
_BRANI = _c([1.5, 1.55, 1.6], [(0.6, 0.6)] * 3)

SLIDES = [
    {"img": "TAP1914", **_IN},        # 0  s0      title
    {"img": "TAPK", **_PORT},         # 1  s1-2    34 cents to 4.95 cents
    {"img": "HARB", **_INL},          # 2  s3      processing, financing, shipping
    {"img": "UOB2001", **_IN},        # 3  s4      later recessions, other routes
    {"img": "DATACTR", **_IN},        # 4  s5      chips and AI
    {"img": "HARBPAN", **_IN},        # 5  s6      rubber graded, packed, shipped
    {"img": "BRANI", **_BRANI},       # 6  s7      tin smelted on Pulau Brani
    {"img": "WHARF", **_IN},          # 7  s8      "dependent on international trade"
    {"img": "NYSE24", **_IN},         # 8  s9      the crash; the car industry
    {"img": "FORD", **_INR},          # 9  s10     fewer cars, fewer tyres
    {"img": "ST1931", **_ST31_HEAD},  # 10 s11     "Still Falling"
    {"img": "ST1931", **_ST31_PENCE}, # 11 s12-13  3 1/4d a pound; "resigned to anything"
    {"img": "TRONOH", **_IN},         # 12 s14-15  price and volume; exports down 84%
    {"img": "CHARTERED", **_IN},      # 13 s16     500 shops closed
    {"img": "TAIPING", **_IN},        # 14 s17-18  estates and mines laid off workers
    {"img": "WHARF", **_OUT},         # 15 s19     recruiting in India stopped
    {"img": "ST1932", **_ST32_FREE},  # 16 s20     free passages to China
    {"img": "HARB", **_OUT},          # 17 s21-22  the quota; arrivals fell
    {"img": "CHARTERED", **_OUT},     # 18 s23-24  the banks; the 1932 merger
    {"img": "STAMP", **_GFX},         # 19 s25     prices recovered
    {"img": "CLEMENTI", **_PORT},     # 20 s26     Clementi, July 1933
    {"img": "CITYHALL", **_IN},       # 21 s27     the chain: a crash abroad
    {"img": "GDP", **_GFX},           # 22 s28-30  growth since 1961
    {"img": "SECTORS", **_GFX},       # 23 s31-33  the chart by industry
    {"img": "SG1978", **_IN},         # 24 s34-36  1985, home-made
    {"img": "SECTORS", **_GFX},       # 25 s37     construction and manufacturing
    {"img": "MBFC", **_IN},           # 26 s38-39  1998, the baht
    {"img": "SECTORS", **_GFX},       # 27 s40-41  finance -20.2%
    {"img": "UOB2001", **_OUT},       # 28 s42-44  2001, electronics 69%
    {"img": "CONTAINER", **_IN},      # 29 s45     electronics exports fell
    {"img": "SECTORS", **_GFX},       # 30 s46-47  manufacturing -3.0 points
    {"img": "TPAGAR", **_IN},         # 31 s48-50  2008-09 through trade
    {"img": "MBSCB", **_IN},          # 32 s51-53  2020, the circuit breaker
    {"img": "SECTORS", **_GFX},       # 33 s54     construction -41.7%
    {"img": "CONTAINER", **_OUT},     # 34 s55-56  two routes: goods
    {"img": "MBFC", **_OUT},          # 35 s57     the money route
    {"img": "SECTORS", **_GFX},       # 36 s58-60  size matters as much as the fall
    {"img": "JURONG", **_IN},         # 37 s61-63  diversification
    {"img": "SIZE", **_GFX},          # 38 s64-65  more evenly spread
    {"img": "DATACTR", **_OUT},       # 39 s66-67  AI-related capital expenditure
    {"img": "MAS", **_PORT},          # 40 s68     the MAS statement
    {"img": "NYSE29", **_IN},         # 41 s69-70  American spending on technology
    {"img": "ELEC", **_GFX},          # 42 s71-73  electronics a quarter of NODX
    {"img": "JURONG", **_OUT},        # 43 s74     pharmaceuticals, chemicals
    {"img": "HARBPAN", **_OUT},       # 44 s75-76  the route has not changed
    {"img": "TAP1914", **_OUT},       # 45 s77     where it fits
    {"img": "BRANIK", **_OUT},        # 46 s78     what the world is buying
]

SCHEDULE = [
    (0.0, 0), (6.5, 1), (20.275, 2), (37.225, 3), (51.7, 4), (61.725, 5), (67.9, 6),
    (76.8, 7), (88.95, 8), (98.3, 9), (103.975, 10), (114.0, 11), (135.475, 12),
    (150.6, 13), (156.45, 14), (167.125, 15), (173.35, 16), (187.775, 17), (215.075, 18),
    (231.05, 19), (234.8, 20), (248.3, 21), (266.025, 22), (288.15, 23), (312.0, 24),
    (334.25, 25), (347.075, 26), (360.625, 27), (379.6, 28), (396.225, 29), (408.175, 30),
    (420.1, 31), (447.725, 32), (461.625, 33), (478.35, 34), (493.825, 35), (502.05, 36),
    (538.0, 37), (572.675, 38), (600.025, 39), (630.875, 40), (655.525, 41), (669.875, 42),
    (698.825, 43), (709.575, 44), (725.75, 45), (739.85, 46),
]
TOTAL_DURATION = 747.95
TIMING_JSON = "audio/when-america-crashed-singapore-sank-the-great-depression-and-the-contagion-that-still-reaches-us.timing.json"

# The avatar presenter, Phase 1 test #5: corner bubble for the first and last 30 s.
AVATAR = {"ranges": [(0, 30), (-30, None)]}
