"""Video config for the Forbidden Hill post.

There is no Commons photo of the 1984 dig, so the excavation sentences get
the trench kept open on the hill (two 2023 views), the finds on display at
Fort Canning (the porcelain compass, glass beads, Chinese coins) and Yuan
blue-and-white wares in the Shanghai Museum (the plate, plus a vase and a
jar, video-only) for the porcelain. Dyce's 1840s watercolour (the hero) and
Elliot's view from the summit carry the hill; the 1825 survey carries the
old walls and the river; the Keramat, the Sang Nila Utama Garden and the
Spice Garden carry the hill today. Raffles, Farquhar and Crawfurd appear
only under the sentences that name them, and Abdullah's sentence gets his
1849 book. The 1928 gold gets the 2009 and 2023 museum photos; the
Singapore Stone takes its one mention; Parliament House, Empress Place and
Itier's 1844 view take the riverside digs. The timeline is letterboxed and
frozen.

70 slides, 796.025s. AVATAR: first and last 30s, cartoon with motion.
"""

_U = "https://upload.wikimedia.org/wikipedia/commons"
_C = f"{_U}/thumb"
_A = "/assets/images"

IMAGES = {
    "HERO": f"{_C}/0/02/Charles_Dyce%2C_Government_Hill_from_the_New_Harbour_Road%2C_Singapore%2C_1846%2C_Watercolour_%26_Ink_on_paper%2C_27.2_x_44.8_cm.png/1280px-Charles_Dyce%2C_Government_Hill_from_the_New_Harbour_Road%2C_Singapore%2C_1846%2C_Watercolour_%26_Ink_on_paper%2C_27.2_x_44.8_cm.png",
    "YUAN": f"{_C}/d/da/Yuan_Underglaze_Blue_Jingdezhen_Porcelain_Plate.jpg/1280px-Yuan_Underglaze_Blue_Jingdezhen_Porcelain_Plate.jpg",
    "VIEW1828": f"{_C}/8/84/View_of_the_town_and_roads_of_Singapore_from_the_government_hill_published_1828.jpg/1280px-View_of_the_town_and_roads_of_Singapore_from_the_government_hill_published_1828.jpg",
    "SULA": f"{_U}/2/2d/Excerpt_from_the_Sulalatus_Salatin_manuscript%2C_copied_in_the_year_1808%2C_chapter_on_the_Death_of_Hang_Tuah.jpg",
    "GOLD09": f"{_C}/b/bf/JavaneseGoldOrnaments-14C-NationalMuseumofSingapore-20090712.jpg/1280px-JavaneseGoldOrnaments-14C-NationalMuseumofSingapore-20090712.jpg",
    "COMPASS": f"{_C}/9/98/At_Fort_Canning_2023_031.jpg/1280px-At_Fort_Canning_2023_031.jpg",
    "EMPRESS": f"{_C}/4/4a/Empress_Place_Building%2C_Singapore_-_20140723.jpg/1280px-Empress_Place_Building%2C_Singapore_-_20140723.jpg",
    "KERAMAT11": f"{_C}/f/fb/Keramat_Iskandar_Syah%2C_Fort_Canning_Park%2C_Singapore_-_20110924.jpg/1280px-Keramat_Iskandar_Syah%2C_Fort_Canning_Park%2C_Singapore_-_20110924.jpg",
    "PITS091": f"{_C}/1/12/At_Fort_Canning_2023_091.jpg/1280px-At_Fort_Canning_2023_091.jpg",
    "TIMELINE": f"{_A}/forbidden-hill-timeline-chart.png",
    # Gallery images:
    "MAP25": f"{_C}/9/9f/Part_of_Singapore_Island_%28British_Library_India_Office_Records%2C_1825%2C_detail%29.jpg/1280px-Part_of_Singapore_Island_%28British_Library_India_Office_Records%2C_1825%2C_detail%29.jpg",
    "ITIER": f"{_U}/e/ef/Jules_Itier%E2%80%99s_1844_daguerreotype_of_Boat_Quay_and_Singapore_River_from_Government_Hill%2C_1844%2C_12.6_x_15_x_0.3_cm%2C_National_Museum_of_Singapore.png",
    "GOLD23": f"{_C}/b/b5/At_National_Museum_of_Singapore_2023_044.jpg/1280px-At_National_Museum_of_Singapore_2023_044.jpg",
    "BEADS": f"{_C}/f/fc/At_Fort_Canning_2023_033.jpg/1280px-At_Fort_Canning_2023_033.jpg",
    "COINS": f"{_C}/8/80/At_Fort_Canning_2023_032.jpg/1280px-At_Fort_Canning_2023_032.jpg",
    "PITS089": f"{_C}/1/11/At_Fort_Canning_2023_089.jpg/1280px-At_Fort_Canning_2023_089.jpg",
    "KERAMAT12": f"{_C}/f/ff/Keramat_Iskandar_Shah.jpg/1280px-Keramat_Iskandar_Shah.jpg",
    "SNU": f"{_C}/3/31/Sang_nila_utama_garden.jpg/1280px-Sang_nila_utama_garden.jpg",
    "SPICE": f"{_C}/5/51/Singapore_Fort_Canning_Park_spice_garden_IMG_9727.jpg/1280px-Singapore_Fort_Canning_Park_spice_garden_IMG_9727.jpg",
    "PARL": f"{_C}/5/5d/Parliament_House%2C_Singapore.jpg/1280px-Parliament_House%2C_Singapore.jpg",
    # Not in this post's captions (credited below):
    "YUANVASE": f"{_C}/8/81/Yuan_Underglaze_Blue_Jingdezhen_Porcelain_Vase.jpg/1280px-Yuan_Underglaze_Blue_Jingdezhen_Porcelain_Vase.jpg",
    "YUANJAR": f"{_C}/0/02/Yuan_Underglaze_Blue_Jingdezhen_Porcelain_Jar.jpg/1280px-Yuan_Underglaze_Blue_Jingdezhen_Porcelain_Jar.jpg",
    "RAFFLES": f"{_U}/a/a0/George_Francis_Joseph_-_Sir_Thomas_Stamford_Bingley_Raffles.jpg",
    "FARQ": f"{_U}/f/f9/Portrait_of_William_Farquhar_%28c._1830%29.jpg",
    "CRAWP": f"{_U}/f/f2/Artist_Unknown%2C_Portrait_of_John_Crawfurd%2C_British_Resident_of_Singapore_%281823%E2%80%931826%29%2C_1857%2C_Oil_on_canvas%2C_210_x_134_cm%2C_National_Museum_Singapore.jpg",
    "HIK1849": f"{_U}/a/af/AbdullahbinAbdulKadir-HikayatAbdullah-1849.jpg",
    "JACKSON": f"{_C}/8/8a/Singapore_from_the_Sea_June_1823_-_Lt._Phillip_Jackson.jpg/1280px-Singapore_from_the_Sea_June_1823_-_Lt._Phillip_Jackson.jpg",
    "PLAN": f"{_U}/6/60/Plan_of_the_Town_of_Singapore_%281822%29_by_Lieutenant_Philip_Jackson.jpg",
    "STONE09": f"{_C}/0/08/SingaporeStone-NationalMuseumofSingapore-20090712.jpg/1280px-SingaporeStone-NationalMuseumofSingapore-20090712.jpg",
}

# Credits for images not captioned in the post or its gallery.
CREDITS = {
    "TIMELINE": "Timeline by Lesser Known Singapore, dates from Wheatley (1961), the Malay Annals, Buckley (1902), Crawfurd (1828), Winstedt (1928) and NUS Press site reports",
    "YUANVASE": "Yuan dynasty blue-and-white porcelain vase, Jingdezhen, Shanghai Museum, Gary Lee Todd, CC0, via Wikimedia Commons",
    "YUANJAR": "Yuan dynasty blue-and-white porcelain jar, Jingdezhen, Shanghai Museum, Gary Lee Todd, CC0, via Wikimedia Commons",
    "RAFFLES": "Sir Thomas Stamford Raffles, 1817, George Francis Joseph, public domain, via Wikimedia Commons",
    "FARQ": "William Farquhar, about 1830, unknown artist, public domain, via Wikimedia Commons",
    "CRAWP": "John Crawfurd, 1857, unknown artist, National Museum of Singapore, public domain, via Wikimedia Commons",
    "HIK1849": "A page from a first edition of the Hikayat Abdullah, 1849, Abdullah bin Abdul Kadir, public domain, via Wikimedia Commons",
    "JACKSON": "Singapore from the Sea, June 1823, Lieutenant Philip Jackson, public domain, via Wikimedia Commons",
    "PLAN": "Plan of the Town of Singapore, 1822, Lieutenant Philip Jackson, public domain, via Wikimedia Commons",
    "STONE09": "The Singapore Stone, National Museum of Singapore, 2009, Jon Callas, CC BY 2.0, via Wikimedia Commons",
}

_E = "ease-in-out"
_IN = {"type": "cover", "zoom": [1.0, 1.06, 1.12], "pan": [(0.5, 0.5)] * 3, "ease": _E}
_IN2 = {"type": "cover", "zoom": [1.1, 1.16, 1.22], "pan": [(0.4, 0.5), (0.5, 0.5), (0.6, 0.5)], "ease": _E}
_OUT = {"type": "cover", "zoom": [1.12, 1.06, 1.0], "pan": [(0.5, 0.5)] * 3, "ease": _E}
# Portraits, tall photos, pages and small scans: letterbox, modest zoom.
_PORT = {"type": "letterbox", "zoom": [1.0, 1.04, 1.08], "pan": [(0.5, 0.5)] * 3, "ease": _E}
_PORT_OUT = {"type": "letterbox", "zoom": [1.08, 1.04, 1.0], "pan": [(0.5, 0.5)] * 3, "ease": _E}
# The timeline: letterbox, frozen.
_GFX = {"type": "letterbox", "zoom": [1, 1, 1], "pan": [(0.5, 0.5)] * 3}


def _c(zoom, pan):
    return {"type": "cover", "zoom": zoom, "pan": pan, "ease": _E}


# Dyce's watercolour: the hill and Government House rise on the left.
_HILL = _c([1.3, 1.4, 1.5], [(0.3, 0.35), (0.33, 0.37), (0.36, 0.4)])
_HILL_OUT = _c([1.5, 1.35, 1.2], [(0.36, 0.4), (0.33, 0.37), (0.3, 0.35)])
# Elliot's long view from the summit: drift across it.
_VIEW_R = _c([1.0, 1.04, 1.08], [(0.2, 0.5), (0.5, 0.5), (0.8, 0.5)])
_VIEW_L = _c([1.0, 1.04, 1.08], [(0.8, 0.5), (0.5, 0.5), (0.2, 0.5)])
_HARBOUR = _c([1.2, 1.3, 1.4], [(0.75, 0.55), (0.8, 0.55), (0.85, 0.55)])
# The 1825 survey: the hill and walls, then down to the river mouth.
_MAP_PAN = _c([1.1, 1.15, 1.2], [(0.35, 0.45), (0.4, 0.5), (0.45, 0.55)])
_MAP_RIVER = _c([1.2, 1.35, 1.5], [(0.5, 0.6), (0.55, 0.65), (0.6, 0.7)])
# Jackson's 1823 view: the drawing sits in a band across the paper.
_SHORE = _c([1.4, 1.5, 1.6], [(0.3, 0.58), (0.4, 0.58), (0.5, 0.58)])
_SEA = _c([1.3, 1.4, 1.5], [(0.8, 0.6), (0.75, 0.6), (0.7, 0.6)])
# Close-ups: the kala plaque on the 2009 armlet; the trench walls.
_PLAQUE = _c([1.4, 1.55, 1.7], [(0.55, 0.5), (0.57, 0.5), (0.59, 0.5)])
_TRENCH = _c([1.3, 1.4, 1.5], [(0.4, 0.6), (0.45, 0.62), (0.5, 0.64)])

SLIDES = [
    {"img": "HERO", **_IN},           # 0  s0   title
    {"img": "KERAMAT11", **_IN},      # 1  s1   January 1984, beside the Keramat
    {"img": "PITS091", **_IN},        # 2  s2   almost nothing at first
    {"img": "YUAN", **_IN},           # 3  s3   the soil changed; blue-and-white
    {"img": "HERO", **_HILL},         # 4  s4   a town on the hill
    {"img": "VIEW1828", **_VIEW_R},   # 5  s5   plans for the hill
    {"img": "PITS089", **_IN},        # 6  s6   the museum staff invite Miksic
    {"img": "KERAMAT12", **_IN},      # 7  s7   18 to 28 January
    {"img": "PITS091", **_TRENCH},    # 8  s8   the crew
    {"img": "SPICE", **_IN},          # 9  s9   rain, a goat, a helmet
    {"img": "YUANVASE", **_PORT},     # 10 s10  "the soil colour change"
    {"img": "YUAN", **_OUT},          # 11 s11  Yuan dynasty porcelain
    {"img": "COMPASS", **_IN},        # 12 s12  1,346 sherds
    {"img": "SULA", **_PORT},         # 13 s13  "the fabulous kingdom of Temasek"
    {"img": "PITS089", **_OUT},       # 14 s14  plans changed; more digging
    {"img": "TIMELINE", **_GFX},      # 15 s15  clues piling up for 160 years
    {"img": "JACKSON", **_SHORE},     # 16 s16  January 1819
    {"img": "HERO", **_HILL_OUT},     # 17 s17  Bukit Larangan
    {"img": "KERAMAT12", **_OUT},     # 18 s18  tombs; haunted
    {"img": "HIK1849", **_PORT},      # 19 s19  Abdullah's account
    {"img": "FARQ", **_PORT},         # 20 s20  Farquhar's gun and flagpole
    {"img": "VIEW1828", **_VIEW_L},   # 21 s21  the hill cleared
    {"img": "RAFFLES", **_PORT},      # 22 s22  Raffles's bungalow
    {"img": "CRAWP", **_PORT},        # 23 s23  Crawfurd, February 1822
    {"img": "MAP25", **_MAP_PAN},     # 24 s24  the old wall and moat
    {"img": "HERO", **_HILL},         # 25 s27  the hill, foundations of buildings
    {"img": "PLAN", **_PORT},         # 26 s28  the square terrace
    {"img": "PITS091", **_OUT},       # 27 s29  fourteen post bases; a temple?
    {"img": "KERAMAT11", **_OUT},     # 28 s31  the grave of Iskandar Shah
    {"img": "SPICE", **_OUT},         # 29 s32  the old fruit trees
    {"img": "COINS", **_PORT},        # 30 s33  pottery and Chinese coins
    {"img": "SULA", **_PORT_OUT},     # 31 s34  the Sejarah Melayu
    {"img": "SNU", **_IN},            # 32 s35  five kings; the fall
    {"img": "JACKSON", **_SEA},       # 33 s36  the king flees up the coast
    {"img": "TIMELINE", **_GFX},      # 34 s37  dates are a reconstruction
    {"img": "YUANJAR", **_IN},        # 35 s38  an outside witness: Wang Dayuan
    {"img": "VIEW1828", **_HARBOUR},  # 36 s40  Longyamen and the strait
    {"img": "HERO", **_OUT},          # 37 s41  Banzu on the hill
    {"img": "SNU", **_OUT},           # 38 s42  the forbidden spring
    {"img": "JACKSON", **_SHORE},     # 39 s43  the Siamese fleet
    {"img": "SULA", **_PORT},         # 40 s44  more legend than history
    {"img": "STONE09", **_IN},        # 41 s45  the Singapore Stone
    {"img": "GOLD09", **_IN},         # 42 s46  7 July 1928
    {"img": "GOLD23", **_IN},         # 43 s47  eleven ornaments
    {"img": "PITS089", **_TRENCH},    # 44 s48  just below the old soil
    {"img": "GOLD09", **_PLAQUE},     # 45 s49  the kala plaque
    {"img": "GOLD23", **_OUT},        # 46 s50  van Stein Callenfels, Winstedt
    {"img": "GOLD09", **_OUT},        # 47 s51  what survives
    {"img": "HERO", **_IN2},          # 48 s53  a single hoard
    {"img": "PITS091", **_IN2},       # 49 s54  seven more excavations
    {"img": "KERAMAT12", **_IN},      # 50 s55  volunteers
    {"img": "BEADS", **_IN},          # 51 s56  beads, porcelain, the compass
    {"img": "COMPASS", **_OUT},       # 52 s57  the workshop
    {"img": "BEADS", **_OUT},         # 53 s58  a high-status quarter
    {"img": "YUANVASE", **_PORT_OUT}, # 54 s59  the 2018 dig
    {"img": "MAP25", **_MAP_RIVER},   # 55 s60  down to the river
    {"img": "PARL", **_IN},           # 56 s61  Parliament House, 1995-96
    {"img": "EMPRESS", **_IN},        # 57 s62  Empress Place, 1998
    {"img": "ITIER", **_PORT},        # 58 s63  the Padang and St Andrew's
    {"img": "PITS089", **_OUT},       # 59 s64  Miksic kept digging
    {"img": "YUAN", **_IN2},          # 60 s65  the book; the prize
    {"img": "SPICE", **_IN},          # 61 s66  his death, 2025
    {"img": "VIEW1828", **_VIEW_R},   # 62 s67  "not just a minor fishing village"
    {"img": "KERAMAT11", **_IN2},     # 63 s69  the Keramat today
    {"img": "PITS091", **_IN},        # 64 s70  the excavation under its roof
    {"img": "SNU", **_IN2},           # 65 s71  the hill's later history
    {"img": "TIMELINE", **_GFX},      # 66 s72  why it matters
    {"img": "EMPRESS", **_OUT},       # 67 s73  a working port town
    {"img": "HERO", **_HILL},         # 68 s74  the Bicentennial on the hill
    {"img": "HERO", **_OUT},          # 69 s75  a trowel at a time
]

SCHEDULE = [(0.0, 0), (7.15, 1), (21.4, 2), (25.825, 3), (34.1, 4), (46.575, 5), (58.075, 6), (76.225, 7), (81.75, 8), (96.05, 9), (106.8, 10), (114.65, 11), (124.4, 12), (136.55, 13), (148.85, 14), (156.675, 15), (163.425, 16), (175.4, 17), (192.65, 18), (198.8, 19), (211.225, 20), (220.4, 21), (224.975, 22), (235.325, 23), (245.925, 24), (268.2, 25), (282.5, 26), (289.75, 27), (310.7, 28), (325.35, 29), (336.3, 30), (344.925, 31), (359.675, 32), (371.025, 33), (375.875, 34), (386.65, 35), (400.475, 36), (405.1, 37), (413.1, 38), (426.7, 39), (435.75, 40), (444.25, 41), (456.975, 42), (466.95, 43), (475.525, 44), (483.7, 45), (492.975, 46), (509.1, 47), (523.425, 48), (536.15, 49), (549.7, 50), (558.425, 51), (576.2, 52), (584.275, 53), (597.35, 54), (606.1, 55), (611.475, 56), (631.55, 57), (650.65, 58), (665.3, 59), (669.825, 60), (684.65, 61), (690.85, 62), (698.95, 63), (714.6, 64), (733.275, 65), (743.975, 66), (756.3, 67), (773.65, 68), (789.45, 69)]
TOTAL_DURATION = 796.025
TIMING_JSON = "audio/forbidden-hill-the-1984-dig-that-found-14th-century-singapura-on-fort-canning.timing.json"

# The avatar presenter, cartoon with motion: corner bubble for the first and last 30 s.
AVATAR = {"ranges": [(0, 30), (-30, None)], "motion": True}
