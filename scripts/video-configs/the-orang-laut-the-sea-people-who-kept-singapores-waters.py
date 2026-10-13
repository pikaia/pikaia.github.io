"""Video config for the orang laut post.

The photos of the sea people themselves are few and small: the Tropenmuseum
houseboats, sailing boats and fisherman (Riau and Jambi, 1910s-20s, 415-700px)
are always letterboxed, as are the small 1900 Pulau Brani plate, the
Kampong Bahru photochrom and the 2013 square Seletar photo. The Lambert
Pulau Brani village (the hero) returns at the title, the 1699 break and
the close. Raffles appears only under the sentence that says he recorded
the population; the opening sentence that names him and Farquhar gets
Jackson's 1823 view of the shore instead. Parameswara, Pires, Mahmud Shah,
the Temenggong, Rohani Rani, Teo Yen Teck and Firdaus Sani have no image,
so their sentences get places, not people. Abdullah's sentence gets the
1849 Hikayat Abdullah page. Video-only: Jackson's view, the 1822 town plan,
Raffles, Westall's 1803 Bugis prau, today's river mouth and Kallang Basin,
a second Orang Seletar photo, the 1900 Brani plate and the Semakau sea.
The timeline is letterboxed and frozen.

55 slides, 594.125s. AVATAR: first and last 30s, cartoon with motion.
"""

_U = "https://upload.wikimedia.org/wikipedia/commons"
_C = f"{_U}/thumb"
_A = "/assets/images"

IMAGES = {
    "HERO": f"{_C}/5/50/KITLV_-_105809_-_Lambert_%26_Co.%2C_G.R._-_Singapore_-_Malay_village_on_the_island_of_Pulau_Brani_near_Singapore_-_circa_1900.tif/lossy-page1-1280px-KITLV_-_105809_-_Lambert_%26_Co.%2C_G.R._-_Singapore_-_Malay_village_on_the_island_of_Pulau_Brani_near_Singapore_-_circa_1900.tif.jpg",
    "KARIMUN": f"{_C}/0/08/Prasasti_Pasir_Panjang.jpg/1280px-Prasasti_Pasir_Panjang.jpg",
    "HOUSEBOAT": f"{_U}/8/81/COLLECTIE_TROPENMUSEUM_Woonschuit_van_een_Oerang-Laoet_familie_Ka._Toengkal_TMnr_10010488.jpg",
    "KAMPONG": f"{_C}/4/4f/Kampong_in_Singapore%2C_gezien_vanaf_het_water_Campong_Bagoes_Singapore_%28titel_op_object%29%2C_RP-F-00-5018-41.jpg/1280px-Kampong_in_Singapore%2C_gezien_vanaf_het_water_Campong_Bagoes_Singapore_%28titel_op_object%29%2C_RP-F-00-5018-41.jpg",
    "SELETAR": f"{_C}/1/1e/Kampung_Orang_Asal_Seletar%2C_Pasir_Gudang_%2811450591134%29.jpg/1280px-Kampung_Orang_Asal_Seletar%2C_Pasir_Gudang_%2811450591134%29.jpg",
    "SAILING": f"{_U}/a/ab/COLLECTIE_TROPENMUSEUM_Woonschuiten_van_de_Orang-Laoets_langs_de_kusten_van_Djambi_en_Riouw_varende_TMnr_10010489.jpg",
    "SUDONG": f"{_C}/a/af/Pulau_Sudong_June_2026.jpg/1280px-Pulau_Sudong_June_2026.jpg",
    "STATION": f"{_C}/c/c9/Pulau_Semakau_32%2C_Nov_06.JPG/1280px-Pulau_Semakau_32%2C_Nov_06.JPG",
    "TIMELINE": f"{_A}/orang-laut-timeline-chart.png",
    # Gallery images:
    "BRANIPC": f"{_C}/0/06/Malay_-_village_Pulo_Brani_Singapore_%28NYPL_Hades-2359734-4044499%29.jpg/1280px-Malay_-_village_Pulo_Brani_Singapore_%28NYPL_Hades-2359734-4044499%29.jpg",
    "KBARU": f"{_C}/9/91/KITLV_-_105811_-_Lambert_%26_Co.%2C_G.R._-_Singapore_-_Kampong_Baru_at_Singapore_-_circa_1890.tif/lossy-page1-1280px-KITLV_-_105811_-_Lambert_%26_Co.%2C_G.R._-_Singapore_-_Kampong_Baru_at_Singapore_-_circa_1890.tif.jpg",
    "KBAHRU": f"{_U}/b/b3/Singapore_Scene_in_Kampong_Bahru_LCCN2017657641.jpg",
    "MALAYV": f"{_C}/2/28/KITLV_-_1403184_-_Malay_village_-_1900-1906.tif/lossy-page1-1280px-KITLV_-_1403184_-_Malay_village_-_1900-1906.tif.jpg",
    "FISHER": f"{_U}/3/3b/COLLECTIE_TROPENMUSEUM_Een_op_zee_levende_visser_van_Orang-Laoet_afkomst_in_de_delta_van_Retih_en_Inderagiri_in_Riouw_Zuid-Sumatra_TMnr_10005469.jpg",
    "SELETAR2": f"{_U}/f/f9/Kampung_Orang_Asal_Seletar_%2811333481766%29.jpg",
    "BUND": f"{_C}/c/c6/Pulau_Semakau%2C_panorama_3%2C_Nov_06.jpg/1280px-Pulau_Semakau%2C_panorama_3%2C_Nov_06.jpg",
    "BRANI24": f"{_C}/d/df/Pulau_Brani_20240710_161229.jpg/1280px-Pulau_Brani_20240710_161229.jpg",
    "RESERVOIR": f"{_C}/6/6c/Upper_Seletar_Reservoir_5%2C_Oct_05.JPG/1280px-Upper_Seletar_Reservoir_5%2C_Oct_05.JPG",
    "UBIN": f"{_C}/4/45/Pulau_Ubin_kampong_house.jpg/1280px-Pulau_Ubin_kampong_house.jpg",
    # Not in this post's captions (credited below):
    "JACKSON": f"{_C}/8/8a/Singapore_from_the_Sea_June_1823_-_Lt._Phillip_Jackson.jpg/1280px-Singapore_from_the_Sea_June_1823_-_Lt._Phillip_Jackson.jpg",
    "RAFFLES": f"{_U}/a/a0/George_Francis_Joseph_-_Sir_Thomas_Stamford_Bingley_Raffles.jpg",
    "BUGIS": f"{_U}/3/3b/Bugis-Makassan_prauw_William_Westall_1803.jpg",
    "HIK1849": f"{_U}/a/af/AbdullahbinAbdulKadir-HikayatAbdullah-1849.jpg",
    "PLAN": f"{_U}/6/60/Plan_of_the_Town_of_Singapore_%281822%29_by_Lieutenant_Philip_Jackson.jpg",
    "RIVER": f"{_C}/9/93/Mouth_of_Singapore_River.jpg/1280px-Mouth_of_Singapore_River.jpg",
    "KALLANG": f"{_C}/5/5f/Kallang_Basin_from_Centennial_Tower%2C_2024046%2C_RSKY.jpg/1280px-Kallang_Basin_from_Centennial_Tower%2C_2024046%2C_RSKY.jpg",
    "SELETAR3": f"{_C}/a/ab/Kampung_Orang_Asal_Seletar%2C_Pasir_Gudang_%2811450635466%29.jpg/1280px-Kampung_Orang_Asal_Seletar%2C_Pasir_Gudang_%2811450635466%29.jpg",
    "BRANIPL": f"{_U}/a/ab/Photographic_Views_of_Singapore_Plate_12_Malay_Village%2C_Pulau_Brani.jpg",
    "SEMAKAU14": f"{_C}/1/16/Pulau_Semakau_14%2C_Nov_06.JPG/1280px-Pulau_Semakau_14%2C_Nov_06.JPG",
}

# Credits for images not captioned in the post or its gallery.
CREDITS = {
    "TIMELINE": "Timeline by Lesser Known Singapore",
    "JACKSON": "Philip Jackson, public domain, via Wikimedia Commons",
    "RAFFLES": "George Francis Joseph, public domain, via Wikimedia Commons",
    "BUGIS": "William Westall, 1803, public domain, via Wikimedia Commons",
    "HIK1849": "Abdullah bin Abdul Kadir, public domain, via Wikimedia Commons",
    "PLAN": "Philip Jackson, 1822, public domain, via Wikimedia Commons",
    "RIVER": "Jukkabrother, CC BY-SA 4.0, via Wikimedia Commons",
    "KALLANG": "Robert Sim, CC BY-SA 4.0, via Wikimedia Commons",
    "SELETAR3": "Emran Kassim, CC BY 2.0, via Wikimedia Commons",
    "BRANIPL": "G. R. Lambert & Co., public domain, via Wikimedia Commons",
    "SEMAKAU14": "Sengkang, free use, via Wikimedia Commons",
}

_E = "ease-in-out"
_IN = {"type": "cover", "zoom": [1.0, 1.06, 1.12], "pan": [(0.5, 0.5)] * 3, "ease": _E}
_IN2 = {"type": "cover", "zoom": [1.1, 1.16, 1.22], "pan": [(0.4, 0.5), (0.5, 0.5), (0.6, 0.5)], "ease": _E}
_OUT = {"type": "cover", "zoom": [1.12, 1.06, 1.0], "pan": [(0.5, 0.5)] * 3, "ease": _E}
# Small scans, portraits, pages and maps: letterbox, modest zoom.
_PORT = {"type": "letterbox", "zoom": [1.0, 1.04, 1.08], "pan": [(0.5, 0.5)] * 3, "ease": _E}
_PORT_OUT = {"type": "letterbox", "zoom": [1.08, 1.04, 1.0], "pan": [(0.5, 0.5)] * 3, "ease": _E}
# The timeline: letterbox, frozen.
_GFX = {"type": "letterbox", "zoom": [1, 1, 1], "pan": [(0.5, 0.5)] * 3}


def _c(zoom, pan):
    return {"type": "cover", "zoom": zoom, "pan": pan, "ease": _E}


# Jackson's 1823 view: the drawing sits in a band across the paper.
_SHORE = _c([1.4, 1.5, 1.6], [(0.3, 0.58), (0.4, 0.58), (0.5, 0.58)])
# The Semakau bund panorama is long and low: drift along it.
_BUND_R = _c([1.0, 1.04, 1.08], [(0.3, 0.5), (0.5, 0.5), (0.7, 0.5)])
_BUND_L = _c([1.08, 1.04, 1.0], [(0.7, 0.5), (0.5, 0.5), (0.3, 0.5)])
# The two Orang Seletar villagers: keep their faces in frame.
_FACES = _c([1.0, 1.04, 1.08], [(0.5, 0.35)] * 3)
_FACES_OUT = _c([1.08, 1.04, 1.0], [(0.5, 0.35)] * 3)

SLIDES = [
    {"img": "HERO", **_IN},           # 0  s0   title
    {"img": "JACKSON", **_SHORE},     # 1  s1   Raffles and Farquhar come ashore, 1819
    {"img": "HOUSEBOAT", **_PORT},    # 2  s2   these were orang laut
    {"img": "SEMAKAU14", **_IN},      # 3  s3   families moved off the southern islands
    {"img": "SAILING", **_PORT},      # 4  s4   people of the sea
    {"img": "KBAHRU", **_PORT},       # 5  s5   boats, or houses over the water
    {"img": "FISHER", **_PORT},       # 6  s6   the Portuguese called them Çelates
    {"img": "MALAYV", **_IN},         # 7  s7   each suku, its own waters and speech
    {"img": "KAMPONG", **_IN},        # 8  s8   several groups in and around Singapore
    {"img": "KBARU", **_IN},          # 9  s9   the Orang Gelam and the Biduanda Kallang
    {"img": "RESERVOIR", **_IN},      # 10 s10  the Orang Seletar, the northern shore
    {"img": "SUDONG", **_IN},         # 11 s11  the Orang Selat, the southern islands
    {"img": "RAFFLES", **_PORT},      # 12 s12  Raffles recorded about a thousand
    {"img": "SAILING", **_PORT_OUT},  # 13 s13  the naval strength of the Malay kingdoms
    {"img": "HOUSEBOAT", **_PORT_OUT},# 14 s14  Parameswara's sea people
    {"img": "KBAHRU", **_PORT_OUT},   # 15 s15  Pires: the site of Malacca, Bendahara, Laksamana
    {"img": "SUDONG", **_OUT},        # 16 s16  a few villages around Singapore in 1511
    {"img": "KARIMUN", **_IN},        # 17 s17  Karimun and its inscription
    {"img": "KAMPONG", **_OUT},       # 18 s18  serving the sultans of Johor
    {"img": "BRANIPC", **_IN},        # 19 s19  different suku, different duties
    {"img": "BRANIPL", **_PORT},      # 20 s21  titles; Raja Negara Selat
    {"img": "HERO", **_OUT},          # 21 s23  the bond with the royal line; 1699
    {"img": "BUGIS", **_PORT},        # 22 s25  scattered; the Bugis take over
    {"img": "HIK1849", **_PORT},      # 23 s26  outsiders' accounts; Abdullah
    {"img": "HOUSEBOAT", **_PORT},    # 24 s28  "born, lived and died in boats"
    {"img": "RIVER", **_IN},          # 25 s29  the garfish rock at the river mouth
    {"img": "PLAN", **_PORT},         # 26 s30  the British town pushes them aside
    {"img": "BRANIPC", **_OUT},       # 27 s31  the Orang Gelam move to Pulau Brani
    {"img": "MALAYV", **_IN2},        # 28 s32  to the Kallang; Tanjong Rhu
    {"img": "KBARU", **_IN2},         # 29 s33  resettled on the Pulai River; smallpox
    {"img": "KALLANG", **_IN},        # 30 s35  the river still carries their name
    {"img": "RESERVOIR", **_OUT},     # 31 s36  the Orang Seletar kept to the north
    {"img": "SELETAR2", **_PORT},     # 32 s37  Kranji, Kadut and Seletar Island
    {"img": "SELETAR", **_IN},        # 33 s38  across the strait to Johor
    {"img": "SAILING", **_PORT},      # 34 s39  crossing to fish until 1987
    {"img": "SELETAR3", **_FACES},    # 35 s40  nine villages in Johor today
    {"img": "BRANIPL", **_PORT_OUT},  # 36 s41  the southern islands' villages
    {"img": "UBIN", **_IN},           # 37 s42  orang pulau, the island people
    {"img": "MALAYV", **_OUT},        # 38 s43  roots among the sea people
    {"img": "KBAHRU", **_PORT},       # 39 s44  fishing, stilt houses, the catch
    {"img": "SEMAKAU14", **_OUT},     # 40 s45  Pulau Semakau, about 600 people
    {"img": "BUND", **_BUND_R},       # 41 s47  1975: reclaimed for petrochemicals
    {"img": "SUDONG", **_IN2},        # 42 s48  Pulau Seking held out longest; 1994
    {"img": "STATION", **_IN},        # 43 s50  the Semakau Landfill, 1999
    {"img": "KAMPONG", **_IN2},       # 44 s51  former islanders on the move
    {"img": "SEMAKAU14", **_IN2},     # 45 s52  Rohani Rani's words
    {"img": "BUND", **_BUND_L},       # 46 s55  Teo Yen Teck: "more free"
    {"img": "UBIN", **_OUT},          # 47 s56  the descendants tell the story
    {"img": "BRANI24", **_IN},        # 48 s57  Orang Laut SG
    {"img": "SELETAR3", **_FACES_OUT},# 49 s58  the Orang Seletar welcome researchers
    {"img": "TIMELINE", **_GFX},      # 50 s59  the National Library and Heritage Board
    {"img": "HERO", **_IN2},          # 51 s60  why it matters
    {"img": "KARIMUN", **_OUT},       # 52 s61  guarding the straits for centuries
    {"img": "TIMELINE", **_GFX},      # 53 s62  within two generations of 1819
    {"img": "HERO", **_OUT},          # 54 s63  the families who remember
]

SCHEDULE = [(0.0, 0), (4.425, 1), (18.1, 2), (27.15, 3), (39.4, 4), (43.05, 5), (57.475, 6), (62.525, 7), (69.375, 8), (75.025, 9), (85.1, 10), (93.85, 11), (99.575, 12), (110.475, 13), (116.15, 14), (129.975, 15), (148.225, 16), (156.625, 17), (173.875, 18), (179.775, 19), (198.7, 20), (212.55, 21), (231.35, 22), (238.35, 23), (252.05, 24), (263.8, 25), (274.075, 26), (277.275, 27), (285.55, 28), (297.725, 29), (318.45, 30), (328.225, 31), (331.975, 32), (340.9, 33), (349.85, 34), (366.0, 35), (380.9, 36), (387.675, 37), (392.225, 38), (399.225, 39), (406.125, 40), (421.025, 41), (438.625, 42), (451.3, 43), (462.85, 44), (467.025, 45), (482.0, 46), (493.075, 47), (497.325, 48), (514.875, 49), (529.525, 50), (542.35, 51), (554.925, 52), (564.4, 53), (580.75, 54)]
TOTAL_DURATION = 594.125
TIMING_JSON = "audio/the-orang-laut-the-sea-people-who-kept-singapores-waters.timing.json"

# The avatar presenter, cartoon with motion: corner bubble for the first and last 30 s.
AVATAR = {"ranges": [(0, 30), (-30, None)], "motion": True}
