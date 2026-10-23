"""Video config for the Robinsons post.

From Raffles Place around 1870 to One Raffles Place today: the store-
locations OSM map (twice), the four pre-1956 newspaper pages (1858, 1932,
1937, 1947), Raffles Place from the 1890s to 1971, the Orchard Road and
Raffles City stores, and the OUB Centre on the fire site.

Named-person rule: Philip Robinson, James Gaborian Spicer, George Rappa,
Stamford Raffles Robinson, Eu Tong Sen, W. H. MacGregor, Benjamin Sheares,
F. A. Chua and Kenzo Tange have no free photographs here, so their
sentences show the newspaper pages, the map, the empty street outside
or the OUB Centre tower with nobody in it.

The map, the newspaper pages and the portrait-shaped photos are
letterboxed, and so is the small 640px Raffles City photo.

41 slides, 639.275s. Narration: Kokoro with the OpenVoice clone.
AVATAR: first and last 30s, cartoon with motion.
"""

IMAGES = {
    "HERO": "https://upload.wikimedia.org/wikipedia/commons/thumb/2/28/522a_Singapore_1971_%2851316419105%29.jpg/1280px-522a_Singapore_1971_%2851316419105%29.jpg",
    "R71B": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/dc/71-610_Raffles_Place_Singapore_1971_%2851252222815%29.jpg/1280px-71-610_Raffles_Place_Singapore_1971_%2851252222815%29.jpg",
    "KITLV1910": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/da/KITLV_-_79891_-_Kleingrothe%2C_C.J._-_Medan_-_Raffles_Place%2C_Singapore_-_circa_1910.tif/lossy-page1-1280px-KITLV_-_79891_-_Kleingrothe%2C_C.J._-_Medan_-_Raffles_Place%2C_Singapore_-_circa_1910.tif.jpg",
    "SPEC": "https://upload.wikimedia.org/wikipedia/commons/thumb/1/15/SpecialistsShoppingCentre.JPG/1280px-SpecialistsShoppingCentre.JPG",
    "SFP1858": "/assets/images/singapore-free-press-1858-03-25-page-2.jpg",
    "MAP": "/assets/images/robinsons-stores-map.png",
    "PLATE03": "https://upload.wikimedia.org/wikipedia/commons/4/44/Photographic_Views_of_Singapore_Plate_03_Raffles%27_Square.jpg",
    "SQ1910": "https://upload.wikimedia.org/wikipedia/commons/thumb/2/22/KITLV_-_79888_-_Kleingrothe%2C_C.J._-_Medan_-_Square_at_Singapore_-_circa_1910.tif/lossy-page1-1280px-KITLV_-_79888_-_Kleingrothe%2C_C.J._-_Medan_-_Square_at_Singapore_-_circa_1910.tif.jpg",
    "ST1932": "/assets/images/straits-times-1932-04-23-page-12.jpg",
    "ST1937": "/assets/images/straits-times-1937-04-23-page-12.jpg",
    "A723": "https://upload.wikimedia.org/wikipedia/commons/thumb/7/7c/KITLV_A723_-_Raffles_Place_te_Singapore%2C_KITLV_87929.tiff/lossy-page1-1280px-KITLV_A723_-_Raffles_Place_te_Singapore%2C_KITLV_87929.tiff.jpg",
    "K1404977": "https://upload.wikimedia.org/wikipedia/commons/thumb/8/87/Raffles_Place_Singapore%2C_KITLV_1404977.tiff/lossy-page1-1280px-Raffles_Place_Singapore%2C_KITLV_1404977.tiff.jpg",
    "ST1947": "/assets/images/sunday-tribune-1947-09-21-page-2.jpg",
    "RSQ1963": "https://upload.wikimedia.org/wikipedia/commons/thumb/b/bf/SG_Singapore_Raffles_Square_-_1963_%28W63-K27-15%29.jpg/1280px-SG_Singapore_Raffles_Square_-_1963_%28W63-K27-15%29.jpg",
    "R71A": "https://upload.wikimedia.org/wikipedia/commons/thumb/0/01/71-610a_Raffles_Place_Singapore_1971_%2851251176861%29.jpg/1280px-71-610a_Raffles_Place_Singapore_1971_%2851251176861%29.jpg",
    "OUBDEC05": "https://upload.wikimedia.org/wikipedia/commons/b/b4/OUB_Centre%2C_Dec_05.JPG",
    "RP24": "https://upload.wikimedia.org/wikipedia/commons/thumb/c/c4/Raffles_Place_12-05-2024%281%29.jpg/1280px-Raffles_Place_12-05-2024%281%29.jpg",
    "ORP25": "https://upload.wikimedia.org/wikipedia/commons/thumb/f/f6/One_Raffles_Place_20250903_%281%29.jpg/1280px-One_Raffles_Place_20250903_%281%29.jpg",
    "CPXMAS": "https://upload.wikimedia.org/wikipedia/commons/thumb/3/39/Centrepoint%2C_Singapore%2C_decorated_for_Christmas_-_20041231.jpg/1280px-Centrepoint%2C_Singapore%2C_decorated_for_Christmas_-_20041231.jpg",
    "CP06": "https://upload.wikimedia.org/wikipedia/commons/thumb/2/29/Centrepoint_Shopping_Centre%2C_Singapore_-_20060212.jpg/1280px-Centrepoint_Shopping_Centre%2C_Singapore_-_20060212.jpg",
    "OUB02": "https://upload.wikimedia.org/wikipedia/commons/c/cd/Raffles_Place_in_front_of_OUB_Centre%2C_Singapore_-_20020829.jpg",
    "RCITY": "https://upload.wikimedia.org/wikipedia/commons/4/47/Robinsons_and_Marks_%26_Spencer%2C_Raffles_City_Shopping_Centre%2C_Singapore_-_20051211.jpg",
    "HEEREN": "https://upload.wikimedia.org/wikipedia/commons/1/14/The_Heeren%2C_Dec_05.JPG",
    "JEM": "https://upload.wikimedia.org/wikipedia/commons/thumb/0/01/Jem_Office_Tower%2C_Jurong_East_Mrt_Station.jpg/1280px-Jem_Office_Tower%2C_Jurong_East_Mrt_Station.jpg",
    "RCSC": "https://upload.wikimedia.org/wikipedia/commons/6/67/Raffles_City_Shopping_Centre%2C_Dec_05.JPG",
    "JL1870": "https://upload.wikimedia.org/wikipedia/commons/thumb/8/84/KITLV_-_155824_-_Shop_John_Little_%26_Co.%2C_Singapore_-_circa_1870.tif/lossy-page1-1280px-KITLV_-_155824_-_Shop_John_Little_%26_Co.%2C_Singapore_-_circa_1870.tif.jpg",
    "CPNOV05": "https://upload.wikimedia.org/wikipedia/commons/thumb/2/26/Centrepoint_Nov_05.JPG/1280px-Centrepoint_Nov_05.JPG",
}

# Credits for images not captioned in the post or its gallery.
CREDITS = {
    "R71B": "Wilford Peloquin, CC BY 2.0, via Wikimedia Commons",
    "PLATE03": "G. R. Lambert & Company, public domain, via Wikimedia Commons",
    "OUBDEC05": "Mailer diablo, copyrighted free use, via Wikimedia Commons",
    "RP24": "LN9267, CC BY-SA 4.0, via Wikimedia Commons",
    "JEM": "Teojincheng, CC0, via Wikimedia Commons",
    "RCSC": "Mailer diablo, copyrighted free use, via Wikimedia Commons",
    "CPNOV05": "Sengkang, copyrighted free use, via Wikimedia Commons",
}

# The channel's 2x2 thumbnail grid, 1870 to today: John Little's shop on
# the square around 1870, Raffles Place around 1910, Robinsons in 1971
# (right of the frame), and One Raffles Place on the fire site in 2025.
THUMBNAIL = [
    {"img": "JL1870", "pan": (0.5, 0.5)},
    {"img": "KITLV1910", "pan": (0.5, 0.5)},
    {"img": "HERO", "pan": (0.85, 0.5)},
    {"img": "ORP25", "pan": (0.5, 0.3)},
]

_E = "ease-in-out"
_IN = {"type": "cover", "zoom": [1.0, 1.06, 1.12], "pan": [(0.5, 0.5)] * 3, "ease": _E}
_OUT = {"type": "cover", "zoom": [1.12, 1.06, 1.0], "pan": [(0.5, 0.5)] * 3, "ease": _E}
# The map, the newspaper pages and the portrait photos: letterbox, modest zoom.
_PORT = {"type": "letterbox", "zoom": [1.0, 1.04, 1.08], "pan": [(0.5, 0.5)] * 3, "ease": _E}
_PORT_OUT = {"type": "letterbox", "zoom": [1.08, 1.04, 1.0], "pan": [(0.5, 0.5)] * 3, "ease": _E}
# The small 640px photo: letterbox, no zoom.
_LB = {"type": "letterbox", "zoom": [1.0, 1.0, 1.0], "pan": [(0.5, 0.5)] * 3, "ease": _E}

SLIDES = [
    {"img": "HERO", **_IN},           # 0  s0  title
    {"img": "R71B", **_IN},           # 1  s1  the fire; nine dead (s1-2)
    {"img": "KITLV1910", **_IN},      # 2  s3  114 years old
    {"img": "SPEC", **_IN},           # 3  s4  reopened on Orchard Road; to 2021
    {"img": "SFP1858", **_PORT},      # 4  s5  Robinson and Spicer (page only); the first advert (s5-6)
    {"img": "MAP", **_PORT},          # 5  s7  Rappa (map only); the early moves (s7-8)
    {"img": "SFP1858", **_PORT_OUT},  # 6  s9  Philip and Stamford Raffles Robinson (page only)
    {"img": "PLATE03", **_IN},        # 7  s10 back to Raffles Place, c. 1891
    {"img": "SQ1910", **_IN},         # 8  s11 Raleigh bicycles
    {"img": "MAP", **_PORT_OUT},      # 9  s12 limited company; Eu Tong Sen (map only)
    {"img": "ST1932", **_PORT},       # 10 s13 the Depression; the 1932 loss (s13-14)
    {"img": "ST1937", **_PORT},       # 11 s15 back in profit; 1941
    {"img": "A723", **_IN},           # 12 s16 Raffles Chambers; the 1941 bombs (s16-17)
    {"img": "K1404977", **_IN},       # 13 s18 bombed again, looted
    {"img": "ST1947", **_PORT},       # 14 s19 MacGregor (page only); reopened; the 1947 profit (s19-21)
    {"img": "HERO", **_OUT},          # 15 s22 air-conditioning; the 1957 facelift
    {"img": "RSQ1963", **_IN},        # 16 s23 the underground car park
    {"img": "R71A", **_IN},           # 17 s24 the fire starts (s24-26)
    {"img": "R71B", **_OUT},          # 18 s27 the lifts; nine dead (s27-29)
    {"img": "KITLV1910", **_OUT},     # 19 s30 the Fire Brigade; the river (s30-32)
    {"img": "A723", **_OUT},          # 20 s33 Mercury; shares; cars (s33-35)
    {"img": "R71A", **_OUT},          # 21 s36 the loss; Third time unlucky (s36-37)
    {"img": "OUBDEC05", **_PORT},     # 22 s38 Sheares and Chua (no people): the inquiry
    {"img": "RP24", **_IN},           # 23 s39 the findings
    {"img": "ORP25", **_PORT},        # 24 s40 Fire Brigade not blamed; Building Control Act (s40-41)
    {"img": "CPXMAS", **_IN},         # 25 s42 reopened at the Specialists' Centre with Christmas stock
    {"img": "MAP", **_PORT_OUT},      # 26 s43 the government acquires the site
    {"img": "SPEC", **_OUT},          # 27 s44 Chris's memory (s44-46)
    {"img": "CP06", **_IN},           # 28 s47 The Centrepoint, 1983
    {"img": "OUB02", **_IN},          # 29 s48 the Clifford Centre branch
    {"img": "RCITY", **_LB},          # 30 s49 Raffles City; Al-Futtaim
    {"img": "HEEREN", **_PORT},       # 31 s50 The Heeren; Jem
    {"img": "JEM", **_IN},            # 32 s51 the 2020 closures
    {"img": "RCSC", **_PORT},         # 33 s52 Raffles City closes, January 2021
    {"img": "OUBDEC05", **_PORT_OUT}, # 34 s53 the OUB Centre; Kenzo Tange (no people)
    {"img": "RP24", **_OUT},          # 35 s54 One Raffles Place; the financial district (s54-55)
    {"img": "JL1870", **_IN},         # 36 s56 John Little
    {"img": "ORP25", **_PORT_OUT},    # 37 s57 online; the legacy (s57-58)
    {"img": "PLATE03", **_OUT},       # 38 s59 where it fits
    {"img": "CPNOV05", **_IN},        # 39 s60 Raffles Place, then Orchard Road
    {"img": "HERO", **_OUT},          # 40 s61 close
]

SCHEDULE = [
    (0.0, 0), (8.15, 1), (30.55, 2), (35.05, 3), (46.975, 4), (68.8, 5),
    (92.125, 6), (99.1, 7), (111.35, 8), (118.6, 9), (131.975, 10), (149.225, 11),
    (170.5, 12), (189.85, 13), (197.625, 14), (226.175, 15), (244.95, 16), (254.575, 17),
    (284.275, 18), (303.85, 19), (327.075, 20), (354.225, 21), (372.25, 22), (382.7, 23),
    (403.1, 24), (417.85, 25), (429.6, 26), (442.8, 27), (463.825, 28), (476.925, 29),
    (489.225, 30), (502.85, 31), (513.85, 32), (527.475, 33), (539.4, 34), (556.55, 35),
    (567.85, 36), (578.375, 37), (599.25, 38), (611.775, 39), (620.85, 40),
]
TOTAL_DURATION = 639.275
TIMING_JSON = "audio/robinsons-and-the-1972-fire-162-years-of-singapores-oldest-department-store.timing.json"

# The avatar presenter, cartoon with motion: corner bubble for the first and last 30 s.
AVATAR = {"ranges": [(0, 30), (-30, None)], "motion": True}
