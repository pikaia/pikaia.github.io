"""Video config for the exchange banks of Raffles Place post.

Raffles Place and its banks from about 1885 to today: the Lambert, KITLV and
Kleingrothe photographs of the square, Battery Road and Collyer Quay, the
Chartered Bank's 1895 palazzo and its 1916 domed building, the Hongkong and
Shanghai Bank's 1894 building and the 1926 Hongkong Bank Chambers, the 1953
Straits Times page, Raffles Place in 1971, Six Battery Road, the HSBC
Building, the view over Marina Bay, the Raffles Place map and the timeline.

Named-person rule: the sentence naming Sir John Nicoll shows the 1953 page,
which carries his photograph; the sentences naming Queen Victoria show the
timeline. Chris's aside shows the HSBC Building itself.

The small or portrait images (the 1894 and 1926 HSBC buildings, the 1908
palazzo, Battery Road in 1905, Six Battery Road, the HSBC Building, the UOB
Plaza view) and the newspaper page and map are letterboxed; the timeline is
shown fixed.

33 slides, 467.35s. Narration: Kokoro with the OpenVoice clone.
AVATAR: first and last 30s, cartoon with motion.
"""

IMAGES = {
    "CB_RP": "https://upload.wikimedia.org/wikipedia/commons/thumb/5/59/The_Chartered_Bank_aan_Raffles_Place_te_Singapore%2C_KITLV_104795.tiff/lossy-page1-1280px-The_Chartered_Bank_aan_Raffles_Place_te_Singapore%2C_KITLV_104795.tiff.jpg",
    "RP1885": "https://upload.wikimedia.org/wikipedia/commons/thumb/9/9f/KITLV_-_103746_-_Lambert_%26_Co._-_Raffles_Place_in_Singapore_-_circa_1885.tif/lossy-page1-1280px-KITLV_-_103746_-_Lambert_%26_Co._-_Raffles_Place_in_Singapore_-_circa_1885.tif.jpg",
    "RP1971": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/dc/71-610_Raffles_Place_Singapore_1971_%2851252222815%29.jpg/1280px-71-610_Raffles_Place_Singapore_1971_%2851252222815%29.jpg",
    "RP1890": "https://upload.wikimedia.org/wikipedia/commons/thumb/8/8d/KITLV_-_103753_-_Raffles_Place%2C_Singapore_-_circa_1890.tif/lossy-page1-1280px-KITLV_-_103753_-_Raffles_Place%2C_Singapore_-_circa_1890.tif.jpg",
    "PIER": "https://upload.wikimedia.org/wikipedia/commons/thumb/0/0f/Johnston_%27s_Pier_and_Hongkong_Shanghai_Bank_Singapore%2C_KITLV_1404895.tiff/lossy-page1-1280px-Johnston_%27s_Pier_and_Hongkong_Shanghai_Bank_Singapore%2C_KITLV_1404895.tiff.jpg",
    "BATT1905": "https://upload.wikimedia.org/wikipedia/commons/4/42/Battery_Road%2C_c._1905.jpg",
    "ST1953": "/assets/images/straits-times-1953-08-01-page-8.jpg",
    "KING1910": "https://upload.wikimedia.org/wikipedia/commons/thumb/8/85/KITLV_-_79893_-_Kleingrothe%2C_C.J._-_Medan_-_Raffles_Place_and_King_Street_in_Singapore_-_circa_1910.tif/lossy-page1-1280px-KITLV_-_79893_-_Kleingrothe%2C_C.J._-_Medan_-_Raffles_Place_and_King_Street_in_Singapore_-_circa_1910.tif.jpg",
    "RP1930": "https://upload.wikimedia.org/wikipedia/commons/thumb/7/7c/KITLV_A723_-_Raffles_Place_te_Singapore%2C_KITLV_87929.tiff/lossy-page1-1280px-KITLV_A723_-_Raffles_Place_te_Singapore%2C_KITLV_87929.tiff.jpg",
    "TL": "/assets/images/exchange-banks-timeline-chart.png",
    "MAP": "/assets/images/exchange-banks-map.png",
    "CB_LOC": "https://upload.wikimedia.org/wikipedia/commons/thumb/8/82/Singapore._Chartered_Bank_Buildings._Battery_Road_LCCN2017657651.jpg/1280px-Singapore._Chartered_Bank_Buildings._Battery_Road_LCCN2017657651.jpg",
    "CB1908": "https://upload.wikimedia.org/wikipedia/commons/7/79/Chartered_Bank_Building_Singapore.jpg",
    "HSBC1900": "https://upload.wikimedia.org/wikipedia/commons/8/81/Photographic_Views_of_Singapore_Plate_05_Hongkong_and_Shanghai_Bank.jpg",
    "BATT1910": "https://upload.wikimedia.org/wikipedia/commons/thumb/8/89/KITLV_-_79890_-_Kleingrothe%2C_C.J._-_Medan_-_Battery_Road_at_Singapore_-_circa_1910.tif/lossy-page1-1280px-KITLV_-_79890_-_Kleingrothe%2C_C.J._-_Medan_-_Battery_Road_at_Singapore_-_circa_1910.tif.jpg",
    "HSBC1926": "https://upload.wikimedia.org/wikipedia/commons/4/40/Hongkong_Bank_Chambers%2C_Collyer_Quay_Singapore_1926.png",
    "SQ1910": "https://upload.wikimedia.org/wikipedia/commons/thumb/2/22/KITLV_-_79888_-_Kleingrothe%2C_C.J._-_Medan_-_Square_at_Singapore_-_circa_1910.tif/lossy-page1-1280px-KITLV_-_79888_-_Kleingrothe%2C_C.J._-_Medan_-_Square_at_Singapore_-_circa_1910.tif.jpg",
    "RP1910": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/da/KITLV_-_79891_-_Kleingrothe%2C_C.J._-_Medan_-_Raffles_Place%2C_Singapore_-_circa_1910.tif/lossy-page1-1280px-KITLV_-_79891_-_Kleingrothe%2C_C.J._-_Medan_-_Raffles_Place%2C_Singapore_-_circa_1910.tif.jpg",
    "RP_KITLV": "https://upload.wikimedia.org/wikipedia/commons/thumb/8/87/Raffles_Place_Singapore%2C_KITLV_1404977.tiff/lossy-page1-1280px-Raffles_Place_Singapore%2C_KITLV_1404977.tiff.jpg",
    "SIXBR": "https://upload.wikimedia.org/wikipedia/commons/d/d1/Six_Battery_Road%2C_Jan_06.JPG",
    "HSBC2018": "https://upload.wikimedia.org/wikipedia/commons/thumb/6/65/Singapore_-_Collyer_Quay_-_HSBC_Building_IMG_9255.jpg/1280px-Singapore_-_Collyer_Quay_-_HSBC_Building_IMG_9255.jpg",
    "UOBVIEW": "https://upload.wikimedia.org/wikipedia/commons/2/29/View_from_UOB_Plaza_1%2C_Singapore_-_20091211.jpg",
}

# The timeline PNG is the only image not captioned in the post or its gallery.
CREDITS = {
    "TL": "Timeline by Lesser Known Singapore, from Wikipedia, HSBC, Roots.gov.sg, The Straits Times and The Business Times",
}

# The channel's 2x2 thumbnail grid, 1885 to today: Raffles Place around 1885,
# the Chartered Bank's domed building, Raffles Place in 1971 and the view
# over Marina Bay from UOB Plaza in 2009.
THUMBNAIL = [
    {"img": "RP1885", "pan": (0.5, 0.5)},
    {"img": "CB_RP", "pan": (0.5, 0.5)},
    {"img": "RP1971", "pan": (0.5, 0.5)},
    {"img": "UOBVIEW", "pan": (0.5, 0.5)},
]

_E = "ease-in-out"
_IN = {"type": "cover", "zoom": [1.0, 1.06, 1.12], "pan": [(0.5, 0.5)] * 3, "ease": _E}
_OUT = {"type": "cover", "zoom": [1.12, 1.06, 1.0], "pan": [(0.5, 0.5)] * 3, "ease": _E}
# The map, the newspaper page and the small or portrait images: letterbox, modest zoom.
_PORT = {"type": "letterbox", "zoom": [1.0, 1.04, 1.08], "pan": [(0.5, 0.5)] * 3, "ease": _E}
_PORT_OUT = {"type": "letterbox", "zoom": [1.08, 1.04, 1.0], "pan": [(0.5, 0.5)] * 3, "ease": _E}
# The timeline: letterboxed and still, so its labels stay readable.
_FIX = {"type": "letterbox", "zoom": [1.0, 1.0, 1.0], "pan": [(0.5, 0.5)] * 3, "ease": "linear"}

SLIDES = [
    {"img": "CB_RP", **_IN},          # 0  s0 title: the Chartered Bank on Raffles Place
    {"img": "RP1885", **_IN},         # 1  s1 the money through one square; three exchange banks (s1-2)
    {"img": "RP1971", **_IN},         # 2  s3 domes replaced by towers
    {"img": "RP1890", **_IN},         # 3  s4 the first banks; the exchange banks (s4-5)
    {"img": "PIER", **_IN},           # 4  s6 trade finance; bills of exchange (s6-7)
    {"img": "BATT1905", **_PORT},     # 5  s8 the banks' own notes until 1899
    {"img": "ST1953", **_PORT},       # 6  s9 Sir John Nicoll (the page carries his photograph)
    {"img": "KING1910", **_IN},       # 7  s10 the Mercantile Bank, Bombay 1853 (s10-11)
    {"img": "RP1930", **_IN},         # 8  s12 105 years in Singapore; its Raffles Place building (s12-13)
    {"img": "TL", **_FIX},            # 9  s14 Queen Victoria's charter; 19 Feb 1859; Commercial Square (no people, s14-16)
    {"img": "CB_LOC", **_IN},         # 10 s17 the 1895 palazzo, Swan and Maclaren (s17-18)
    {"img": "CB_RP", **_OUT},         # 11 s19 the 1916 domed building on the square
    {"img": "CB1908", **_PORT},       # 12 s20 the old palazzo becomes the Bank of China
    {"img": "HSBC1900", **_PORT},     # 13 s21 the Hongkong and Shanghai Bank; Collyer Quay 1877 (s21-22)
    {"img": "BATT1910", **_IN},       # 14 s23 the 1977 centenary
    {"img": "BATT1905", **_PORT_OUT}, # 15 s24 the 1894 building at Battery Road and Collyer Quay
    {"img": "HSBC1926", **_PORT},     # 16 s25 the Hongkong Bank Chambers, mid-1920s
    {"img": "SQ1910", **_IN},         # 17 s26 the busiest time
    {"img": "RP1910", **_IN},         # 18 s27 rubber and tin
    {"img": "RP_KITLV", **_IN},       # 19 s28 motor cars; the Bank of Taiwan
    {"img": "MAP", **_PORT},          # 20 s29 the war; the first air raid (s29-30)
    {"img": "TL", **_FIX},            # 21 s31 the British banks closed, 1942
    {"img": "HSBC1926", **_PORT_OUT}, # 22 s32 the Yokohama Specie Bank in the HSBC building
    {"img": "RP1930", **_OUT},        # 23 s33 the banks reopen, 1945
    {"img": "ST1953", **_PORT_OUT},   # 24 s34 rebuilding; the 1953 foundation stone (s34-36)
    {"img": "RP1971", **_OUT},        # 25 s37 HSBC buys the Mercantile; Standard Chartered (s37-39)
    {"img": "MAP", **_PORT_OUT},      # 26 s40 the Hongkong Bank Chambers pulled down; the 1983 tower (s40-41)
    {"img": "SIXBR", **_PORT},        # 27 s42 Six Battery Road, 1984
    {"img": "HSBC2018", **_PORT},     # 28 s43 aside: Security Pacific in the HSBC Building (s43-44)
    {"img": "UOBVIEW", **_PORT},      # 29 s45 Marina Bay today
    {"img": "RP1885", **_OUT},        # 30 s46 where it fits
    {"img": "TL", **_FIX},            # 31 s47 palazzos to domes to towers
    {"img": "HSBC2018", **_PORT_OUT}, # 32 s48 the towers on the old corners
]

SCHEDULE = [
    (0.0, 0), (5.7, 1), (28.35, 2), (39.625, 3), (52.6, 4), (78.35, 5),
    (92.275, 6), (107.7, 7), (125.25, 8), (140.5, 9), (163.675, 10), (182.25, 11),
    (196.225, 12), (202.375, 13), (218.325, 14), (230.45, 15), (246.2, 16), (255.175, 17),
    (260.1, 18), (266.325, 19), (278.95, 20), (290.25, 21), (297.975, 22), (314.775, 23),
    (320.775, 24), (350.3, 25), (374.35, 26), (390.475, 27), (403.975, 28), (424.925, 29),
    (436.5, 30), (446.075, 31), (454.55, 32),
]
TOTAL_DURATION = 467.35
TIMING_JSON = "audio/the-exchange-banks-of-raffles-place-chartered-hsbc-and-mercantile.timing.json"

# The avatar presenter, cartoon with motion: corner bubble for the first and last 30 s.
AVATAR = {"ranges": [(0, 30), (-30, None)], "motion": True}
