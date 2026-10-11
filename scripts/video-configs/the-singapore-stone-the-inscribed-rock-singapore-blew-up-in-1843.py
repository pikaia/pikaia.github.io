"""Video config for the Singapore Stone post.

The stone itself carries the opening and the close: Bland's 1837 copy (the
hero), Laidlay's 1848 drawings of the fragments, and the 2009 and 2012
photos of the surviving fragment. The two 1825 survey maps take the point
at the river mouth; Jackson's 1823 view and 1822 plan take the town;
Crawfurd, Raffles, Prinsep and Butterworth appear only under the sentences
that name them (there is no usable portrait of Low, Stevenson or Bonham,
so their lines get the stone or the town). Coleman's Public Offices (1846,
video-only) take the paragraph that wrongly blames him. The Sulalatus
Salatin page and the 2016 parade photo carry Badang; the Calcutta museum
photos carry the fragments' years in India; three Kawi-script stones (the
Batavia copy, Pengkalan Kempas, and the 792 CE Manjusrigrha inscription,
video-only) carry the scholars. The Fullerton postcard, the 1973 Merlion
and the 2019 hotel carry the site today. The timeline is letterboxed and
frozen.

56 slides, 704.1s. AVATAR: first and last 30s, cartoon with motion.
"""

_U = "https://upload.wikimedia.org/wikipedia/commons"
_C = f"{_U}/thumb"
_A = "/assets/images"

IMAGES = {
    "HERO": f"{_C}/a/a1/1837-SingaporeStone-WBlanddrawing.jpg/1280px-1837-SingaporeStone-WBlanddrawing.jpg",
    "MAP25C": f"{_C}/2/2d/Part_of_Singapore_Island_%28British_Library_India_Office_Records%2C_1825%2C_detail%29_-_cropped.jpg/1280px-Part_of_Singapore_Island_%28British_Library_India_Office_Records%2C_1825%2C_detail%29_-_cropped.jpg",
    "CRAWP": f"{_U}/f/f2/Artist_Unknown%2C_Portrait_of_John_Crawfurd%2C_British_Resident_of_Singapore_%281823%E2%80%931826%29%2C_1857%2C_Oil_on_canvas%2C_210_x_134_cm%2C_National_Museum_Singapore.jpg",
    "SULA": f"{_U}/2/2d/Excerpt_from_the_Sulalatus_Salatin_manuscript%2C_copied_in_the_year_1808%2C_chapter_on_the_Death_of_Hang_Tuah.jpg",
    "LAID": f"{_U}/8/88/SingaporeStone-drawings.jpg",
    "CHOW": f"{_C}/1/1b/The_Museum%2C_Chowringhee.jpg/1280px-The_Museum%2C_Chowringhee.jpg",
    "KEMPAS": f"{_C}/1/13/Pengkalan_Kempas_tomb_Kawi_script_south_side_in_1919_by_C._Boden_Kloss.png/1280px-Pengkalan_Kempas_tomb_Kawi_script_south_side_in_1919_by_C._Boden_Kloss.png",
    "STONE09": f"{_C}/0/08/SingaporeStone-NationalMuseumofSingapore-20090712.jpg/1280px-SingaporeStone-NationalMuseumofSingapore-20090712.jpg",
    "BADANG": f"{_C}/c/c5/Badang_lifting_the_Singapore_Stone_at_National_Day_Parade_2016.jpg/1280px-Badang_lifting_the_Singapore_Stone_at_National_Day_Parade_2016.jpg",
    "FULL19": f"{_C}/7/7a/Singapore_%28SG%29%2C_The_Fullerton_Hotel_--_2019_--_4708.jpg/1280px-Singapore_%28SG%29%2C_The_Fullerton_Hotel_--_2019_--_4708.jpg",
    "TIMELINE": f"{_A}/stone-timeline-chart.png",
    # Gallery images:
    "LAIDDET": f"{_U}/e/e4/SingaporeStone-drawings-detail.jpg",
    "STONE12": f"{_C}/5/59/Singapore_Stone_-_20121019.jpg/1280px-Singapore_Stone_-_20121019.jpg",
    "MAP25": f"{_C}/9/9f/Part_of_Singapore_Island_%28British_Library_India_Office_Records%2C_1825%2C_detail%29.jpg/1280px-Part_of_Singapore_Island_%28British_Library_India_Office_Records%2C_1825%2C_detail%29.jpg",
    "JACKSON": f"{_C}/8/8a/Singapore_from_the_Sea_June_1823_-_Lt._Phillip_Jackson.jpg/1280px-Singapore_from_the_Sea_June_1823_-_Lt._Phillip_Jackson.jpg",
    "PRINSEP": f"{_U}/3/37/James_Prinsep.jpg",
    "BUTTER": f"{_U}/2/2f/William_J_Butterworth.jpg",
    "IM1906": f"{_C}/6/6e/Indian_Museum%2C_Calcutta_in_1906.jpg/1280px-Indian_Museum%2C_Calcutta_in_1906.jpg",
    "KAWI": f"{_C}/4/45/Copy_of_a_stone_stele_written_in_Kawi_script.jpg/1280px-Copy_of_a_stone_stele_written_in_Kawi_script.jpg",
    "NMS": f"{_U}/3/30/The_National_Museum_of_Singapore.jpg",
    # Not in this post's captions (credited below):
    "HIK1849": f"{_U}/a/af/AbdullahbinAbdulKadir-HikayatAbdullah-1849.jpg",
    "RAFFLES": f"{_U}/a/a0/George_Francis_Joseph_-_Sir_Thomas_Stamford_Bingley_Raffles.jpg",
    "PLAN": f"{_U}/6/60/Plan_of_the_Town_of_Singapore_%281822%29_by_Lieutenant_Philip_Jackson.jpg",
    "PUBLICOFF": f"{_U}/d/df/Public_Offices%2C_Singapore_by_John_Turnbull_Thomson_1846.jpg",
    "MANJU": f"{_C}/a/ab/Manjusrigrha_Inscription_1.jpg/1280px-Manjusrigrha_Inscription_1.jpg",
    "FULL1920": f"{_C}/1/19/Singapore%2C_KITLV_1404891.tiff/lossy-page1-1280px-Singapore%2C_KITLV_1404891.tiff.jpg",
    "R1973": f"{_C}/e/e4/Singapore-Merlion-1973-74-WUS08176.jpg/1280px-Singapore-Merlion-1973-74-WUS08176.jpg",
}

# Credits for images not captioned in the post or its gallery.
CREDITS = {
    "TIMELINE": "Timeline by Lesser Known Singapore, dates from Crawfurd (1828), Buckley (1902), Histories (2023) and the National Heritage Board",
    "HIK1849": "A page from a first edition of the Hikayat Abdullah, 1849, Abdullah bin Abdul Kadir, public domain, via Wikimedia Commons",
    "RAFFLES": "Sir Thomas Stamford Raffles, 1817, George Francis Joseph, public domain, via Wikimedia Commons",
    "PLAN": "Plan of the Town of Singapore, 1822, Lieutenant Philip Jackson, public domain, via Wikimedia Commons",
    "PUBLICOFF": "Public Offices, Singapore, designed by G. D. Coleman, sketch by John Turnbull Thomson, 1846, public domain, via Wikimedia Commons",
    "MANJU": "The Manjusrigrha inscription, 792 CE, Sewu temple, Java, Gunawan Kartapranata, CC BY-SA 4.0, via Wikimedia Commons",
    "FULL1920": "The Fullerton Building across the harbour, postcard, 1920 to 1940, anonymous, KITLV, Leiden University Library, CC BY 4.0, via Wikimedia Commons",
    "R1973": "The Fullerton Building and the Merlion, 1973 or 1974, Rainer Halama, CC BY-SA 4.0, via Wikimedia Commons",
}

_E = "ease-in-out"
_IN = {"type": "cover", "zoom": [1.0, 1.06, 1.12], "pan": [(0.5, 0.5)] * 3, "ease": _E}
_IN2 = {"type": "cover", "zoom": [1.1, 1.16, 1.22], "pan": [(0.4, 0.5), (0.5, 0.5), (0.6, 0.5)], "ease": _E}
_OUT = {"type": "cover", "zoom": [1.12, 1.06, 1.0], "pan": [(0.5, 0.5)] * 3, "ease": _E}
# Portraits, drawings, text pages and small scans: letterbox, modest zoom.
_PORT = {"type": "letterbox", "zoom": [1.0, 1.04, 1.08], "pan": [(0.5, 0.5)] * 3, "ease": _E}
_PORT_OUT = {"type": "letterbox", "zoom": [1.08, 1.04, 1.0], "pan": [(0.5, 0.5)] * 3, "ease": _E}
# The timeline: letterbox, frozen.
_GFX = {"type": "letterbox", "zoom": [1, 1, 1], "pan": [(0.5, 0.5)] * 3}


def _c(zoom, pan):
    return {"type": "cover", "zoom": zoom, "pan": pan, "ease": _E}


# Bland's copy: push in on the rows of letters, left half then right.
_BLAND_L = _c([1.3, 1.4, 1.5], [(0.35, 0.45), (0.4, 0.47), (0.45, 0.5)])
_BLAND_R = _c([1.3, 1.4, 1.5], [(0.75, 0.6), (0.7, 0.62), (0.65, 0.65)])
# The full 1825 survey: drift from the hills down to Rocky Point.
_MAP_PAN = _c([1.1, 1.15, 1.2], [(0.35, 0.45), (0.45, 0.55), (0.55, 0.65)])
_MAP_PAN_R = _c([1.2, 1.15, 1.1], [(0.55, 0.65), (0.45, 0.55), (0.35, 0.45)])
# The cropped survey: push in on "Rocky point" at the river mouth, right of centre.
_POINT = _c([1.2, 1.4, 1.6], [(0.65, 0.5), (0.72, 0.5), (0.78, 0.5)])
_POINT_OUT = _c([1.5, 1.3, 1.1], [(0.78, 0.5), (0.7, 0.5), (0.6, 0.5)])
# Jackson's 1823 view: the drawing sits in a band across the paper.
_SEA = _c([1.3, 1.4, 1.5], [(0.8, 0.6), (0.75, 0.6), (0.7, 0.6)])
_SHORE = _c([1.4, 1.5, 1.6], [(0.3, 0.58), (0.4, 0.58), (0.5, 0.58)])
# The 2009 fragment photo: close on the letters.
_LETTERS = _c([1.3, 1.4, 1.5], [(0.45, 0.45), (0.5, 0.47), (0.55, 0.5)])

SLIDES = [
    {"img": "HERO", **_IN},          # 0  s0   title
    {"img": "STONE09", **_IN},       # 1  s1   January 1843: the slab blasted
    {"img": "HERO", **_BLAND_L},     # 2  s2   about fifty lines on its face
    {"img": "LAIDDET", **_PORT},     # 3  s3   the only ancient inscription; never read
    {"img": "MAP25", **_MAP_PAN},    # 4  s4   June 1819: clearing the point
    {"img": "JACKSON", **_SHORE},    # 5  s5   Montgomerie; the Bengali sailors
    {"img": "MAP25C", **_POINT},     # 6  s7   three metres; a split boulder
    {"img": "HERO", **_BLAND_R},     # 7  s9   the writing inside a raised rim
    {"img": "CRAWP", **_PORT},       # 8  s10  Crawfurd, February 1822
    {"img": "STONE12", **_IN},       # 9  s11  rough carving, worn letters; Pali?
    {"img": "HIK1849", **_PORT},     # 10 s14  Abdullah remembers the crowds
    {"img": "RAFFLES", **_PORT},     # 11 s16  with Raffles and Thomsen
    {"img": "HERO", **_PORT},        # 12 s17  flour and lard in the grooves
    {"img": "STONE09", **_LETTERS},  # 13 s18  Raffles's acids
    {"img": "SULA", **_PORT},        # 14 s19  the Sejarah Melayu; Badang the slave
    {"img": "JACKSON", **_SEA},      # 15 s21  the spirit in the net; to court
    {"img": "BADANG", **_IN},        # 16 s23  the contest: lifting the rock
    {"img": "MAP25C", **_POINT_OUT}, # 17 s25  writers link the slab with the story
    {"img": "STONE12", **_OUT},      # 18 s26  nothing beyond the legend
    {"img": "PLAN", **_PORT},        # 19 s27  Stevenson takes over public works
    {"img": "MAP25C", **_POINT},     # 20 s28  blasted for Fort Fullerton
    {"img": "HERO", **_OUT},         # 21 s29  Low protests; the work goes ahead
    {"img": "PUBLICOFF", **_PORT},   # 22 s30  the blame laid on Coleman
    {"img": "LAID", **_PORT},        # 23 s33  Low saves the legible fragments
    {"img": "LAIDDET", **_PORT_OUT}, # 24 s34  one to Bonham, three kept
    {"img": "BUTTER", **_PORT},      # 25 s35  a seat at the Treasury; Butterworth
    {"img": "PLAN", **_PORT_OUT},    # 26 s36  a fragment at Government House
    {"img": "HIK1849", **_PORT_OUT}, # 27 s38  Abdullah's verdict
    {"img": "LAID", **_PORT_OUT},    # 28 s40  Laidlay asks for the fragments, 1848
    {"img": "JACKSON", **_SHORE},    # 29 s41  the Rob Roy, February 1848
    {"img": "LAIDDET", **_PORT},     # 30 s42  Calcutta; charcoal dust in the grooves
    {"img": "CHOW", **_IN},          # 31 s43  the Calcutta museum; seventy years
    {"img": "NMS", **_IN},           # 32 s45  the Raffles Museum asks, 1918
    {"img": "STONE09", **_OUT},      # 33 s46  one fragment back, 1919
    {"img": "KAWI", **_PORT},        # 34 s48  no agreement on the language
    {"img": "PRINSEP", **_PORT},     # 35 s49  Bland and Prinsep
    {"img": "KEMPAS", **_PORT},      # 36 s50  Laidlay: Kawi
    {"img": "MANJU", **_PORT},       # 37 s51  Kern, Krom
    {"img": "KAWI", **_PORT_OUT},    # 38 s54  de Casparis, Boechari
    {"img": "STONE12", **_IN2},      # 39 s56  Miksic
    {"img": "NMS", **_OUT},          # 40 s57  the National Museum's dating
    {"img": "STONE09", **_LETTERS},  # 41 s58  Sinclair's "kesariva"
    {"img": "KEMPAS", **_PORT_OUT},  # 42 s62  Lee and Perono Cacciafoco, 2023
    {"img": "STONE12", **_IN},       # 43 s63  74 centimetres; National Treasure
    {"img": "TIMELINE", **_GFX},     # 44 s64  2006
    {"img": "BADANG", **_OUT},       # 45 s66  the 2016 National Day Parade
    {"img": "R1973", **_IN},         # 46 s68  the Merlion, 1972
    {"img": "FULL1920", **_IN},      # 47 s69  Fort Fullerton gone; the GPO, 1928
    {"img": "FULL19", **_IN},        # 48 s71  nothing marks the place
    {"img": "MAP25", **_MAP_PAN_R},  # 49 s72  no law in 1843
    {"img": "FULL19", **_OUT},       # 50 s73  the Preservation of Monuments Act
    {"img": "HERO", **_PORT_OUT},    # 51 s75  the stone came too early
    {"img": "TIMELINE", **_GFX},     # 52 s76  why it matters
    {"img": "STONE12", **_OUT},      # 53 s77  the one piece of writing found here
    {"img": "MAP25C", **_POINT_OUT}, # 54 s78  lost in a morning
    {"img": "HERO", **_OUT},         # 55 s79  a thinner record
]

SCHEDULE = [(0.0, 0), (5.575, 1), (20.125, 2), (28.75, 3), (38.125, 4), (50.75, 5), (69.9, 6), (85.05, 7), (97.625, 8), (112.225, 9), (133.15, 10), (150.95, 11), (160.825, 12), (171.975, 13), (184.975, 14), (199.125, 15), (212.5, 16), (229.425, 17), (241.35, 18), (249.1, 19), (257.7, 20), (268.225, 21), (276.55, 22), (301.85, 23), (311.625, 24), (316.525, 25), (328.925, 26), (343.325, 27), (358.775, 28), (368.575, 29), (377.7, 30), (388.9, 31), (396.05, 32), (401.475, 33), (414.875, 34), (421.15, 35), (435.05, 36), (445.4, 37), (464.75, 38), (481.45, 39), (496.1, 40), (505.5, 41), (532.725, 42), (547.675, 43), (556.125, 44), (575.3, 45), (588.95, 46), (601.075, 47), (617.6, 48), (622.1, 49), (630.825, 50), (652.825, 51), (663.025, 52), (674.825, 53), (685.1, 54), (692.975, 55)]
TOTAL_DURATION = 704.1
TIMING_JSON = "audio/the-singapore-stone-the-inscribed-rock-singapore-blew-up-in-1843.timing.json"

# The avatar presenter, cartoon with motion: corner bubble for the first and last 30 s.
AVATAR = {"ranges": [(0, 30), (-30, None)], "motion": True}
