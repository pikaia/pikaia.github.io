"""Video config for the Syed Mohamed Alsagoff post.

No portrait of Syed Mohamed is known to survive, and the National Museum's
photographs of the 1878 estate notes need NHB permission (requested), so the
video uses Pulau Kukup in 2005 and 2025, the Kukup map and the timeline, the
1881 and 1906 Straits Times pages, the Alsagoff graves at Hajjah Fatimah's
mosque, early Raffles Hotel photographs, pilgrims at the Dutch consulate in
Jeddah around 1880, Sultan Abu Bakar, the Hadhrami quarter of Surabaya,
Habib Noh's shrine, the Alsagoff Arab School and the Alkaff Garden and
Mansion.

Named-person rule: every sentence naming Syed Mohamed, his father, Buckley,
Hadji Daoud, Gullick, Syed Omar or Faisal Tehrani shows a picture with no
people in it. Sultan Abu Bakar's portrait appears only under sentences about
the Sultan.

The small or grainy scans (the pilgrims, Surabaya, the 1932 hotel entrance)
and the two newspaper pages are letterboxed; the Sultan's portrait and the
timeline are shown fixed.

45 slides, 614.525s. Narration: Kokoro with the OpenVoice clone.
AVATAR: first and last 30s, cartoon with motion.
"""

IMAGES = {
    "KUKUP05": "https://upload.wikimedia.org/wikipedia/commons/thumb/2/29/Pulau_Kukup.JPG/1280px-Pulau_Kukup.JPG",
    "KUKUP25": "https://upload.wikimedia.org/wikipedia/commons/thumb/6/6c/Kukup_%28250511-0910%29.jpg/1280px-Kukup_%28250511-0910%29.jpg",
    "MAP": "/assets/images/alsagoff-map.png",
    "TL": "/assets/images/alsagoff-timeline-chart.png",
    "ST1881": "/assets/images/straits-times-overland-journal-1881-07-28-page-2.jpg",
    "ST1906": "/assets/images/straits-times-1906-07-04-page-5.jpg",
    "DGRAVE": "https://upload.wikimedia.org/wikipedia/commons/thumb/3/34/Hajjah_Fatimah_Mosque%2C_double_grave.jpg/1280px-Hajjah_Fatimah_Mosque%2C_double_grave.jpg",
    "BURIAL": "https://upload.wikimedia.org/wikipedia/commons/thumb/f/fb/Alsagoff_burial_ground%2C_panorama.jpg/1280px-Alsagoff_burial_ground%2C_panorama.jpg",
    "RAF1": "https://upload.wikimedia.org/wikipedia/commons/thumb/3/30/The_Raffles_Hotel%2C_Singapore%2C_KITLV_1404942.tiff/lossy-page1-1280px-The_Raffles_Hotel%2C_Singapore%2C_KITLV_1404942.tiff.jpg",
    "RAF2": "https://upload.wikimedia.org/wikipedia/commons/thumb/3/37/Raffles_Hotel_te_Singapore%2C_KITLV_156148.tiff/lossy-page1-1280px-Raffles_Hotel_te_Singapore%2C_KITLV_156148.tiff.jpg",
    "RAF3": "https://upload.wikimedia.org/wikipedia/commons/thumb/8/85/Singapore_Raffels_Hotel.%2C_KITLV_1404887.tiff/lossy-page1-1280px-Singapore_Raffels_Hotel.%2C_KITLV_1404887.tiff.jpg",
    "RAF1932": "https://upload.wikimedia.org/wikipedia/commons/d/d5/COLLECTIE_TROPENMUSEUM_Entree_van_het_Raffles_Hotel_Singapore_TMnr_60018239.jpg",
    "PILG_AMB": "https://upload.wikimedia.org/wikipedia/commons/b/bd/COLLECTIE_TROPENMUSEUM_Mekkagangers_uit_Ambon_Key_en_Banda_%28Molukken%29_in_het_Nederlandse_Consulaat_in_Jeddah_Saoedi_Arabi%C3%AB_TMnr_10001261.jpg",
    "PILG_MAN": "https://upload.wikimedia.org/wikipedia/commons/c/c1/COLLECTIE_TROPENMUSEUM_Mekkagangers_uit_Mandeling_Sumatra_in_het_Nederlandse_Consulaat_in_Jeddah_Saoedi_Arabi%C3%AB_TMnr_10001258.jpg",
    "ABUBAKAR": "https://upload.wikimedia.org/wikipedia/commons/b/ba/Johor-AbuBakar.jpg",
    "HADH1880": "https://upload.wikimedia.org/wikipedia/commons/1/12/Hadhrami_Arab_neighborhood%2C_Surabaya_1880.jpg",
    "HADH1920": "https://upload.wikimedia.org/wikipedia/commons/c/cf/Hadhrami_immigrants_at_Surabaya_1920s.jpg",
    "NOHCX": "https://upload.wikimedia.org/wikipedia/commons/thumb/1/17/Keramat_Habib_Noh_religious_complex.jpg/1280px-Keramat_Habib_Noh_religious_complex.jpg",
    "SCH23": "https://upload.wikimedia.org/wikipedia/commons/thumb/1/11/Alsagoff_Arabic_School%2C_Singapore_%282023-06%29_img_01.jpg/1280px-Alsagoff_Arabic_School%2C_Singapore_%282023-06%29_img_01.jpg",
    "SCH06": "https://upload.wikimedia.org/wikipedia/commons/thumb/a/a5/Alsagoff_Arab_School%2C_Jan_06.JPG/1280px-Alsagoff_Arab_School%2C_Jan_06.JPG",
    "SCH12": "https://upload.wikimedia.org/wikipedia/commons/thumb/0/0a/Alsagoff_Arab_School_-_panoramio.jpg/1280px-Alsagoff_Arab_School_-_panoramio.jpg",
    "ALKAFFG": "https://upload.wikimedia.org/wikipedia/commons/thumb/e/ea/Alkaff_Garden%2C_Singapore.%2C_KITLV_1404907.tiff/lossy-page1-1280px-Alkaff_Garden%2C_Singapore.%2C_KITLV_1404907.tiff.jpg",
    "ALKAFFM": "https://upload.wikimedia.org/wikipedia/commons/thumb/a/a3/Alkaff_Mansion.png/1280px-Alkaff_Mansion.png",
}

# The timeline PNG is the only image not captioned in the post or its gallery.
CREDITS = {
    "TL": "Timeline by Lesser Known Singapore, from Wikipedia, Roots.gov.sg, BiblioAsia, Free Malaysia Today and The Straits Times",
}

# The channel's 2x2 thumbnail grid, 1880 to today: the Hadhrami quarter of
# Surabaya around 1880, the Raffles Hotel on an early postcard, the Alsagoff
# Arab School in 2023 and Kukup in 2025.
THUMBNAIL = [
    {"img": "HADH1880", "pan": (0.5, 0.5)},
    {"img": "RAF1", "pan": (0.5, 0.5)},
    {"img": "SCH23", "pan": (0.5, 0.5)},
    {"img": "KUKUP25", "pan": (0.5, 0.5)},
]

_E = "ease-in-out"
_IN = {"type": "cover", "zoom": [1.0, 1.06, 1.12], "pan": [(0.5, 0.5)] * 3, "ease": _E}
_OUT = {"type": "cover", "zoom": [1.12, 1.06, 1.0], "pan": [(0.5, 0.5)] * 3, "ease": _E}
# The map, the newspaper pages and the small scans: letterbox, modest zoom.
_PORT = {"type": "letterbox", "zoom": [1.0, 1.04, 1.08], "pan": [(0.5, 0.5)] * 3, "ease": _E}
_PORT_OUT = {"type": "letterbox", "zoom": [1.08, 1.04, 1.0], "pan": [(0.5, 0.5)] * 3, "ease": _E}
# The timeline and the Sultan's small portrait: letterboxed and still.
_FIX = {"type": "letterbox", "zoom": [1.0, 1.0, 1.0], "pan": [(0.5, 0.5)] * 3, "ease": "linear"}

SLIDES = [
    {"img": "KUKUP05", **_IN},        # 0  s0 title (names him: no people)
    {"img": "KUKUP25", **_IN},        # 1  s1 the 1878 notes (s1-2)
    {"img": "MAP", **_PORT},          # 2  s3 his estates on Kukup; the Sultan's grant (no people, s3-4)
    {"img": "TL", **_FIX},            # 3  s5 born 1836, Hadhramaut (no people)
    {"img": "DGRAVE", **_IN},         # 4  s6 his grandfather (no people)
    {"img": "BURIAL", **_IN},         # 5  s7 Syed Ahmed, Raja Siti, Hajjah Fatimah (no people, s7-8)
    {"img": "RAF3", **_IN},           # 6  s9 Syed Ahmed's firm; Buckley (no people, s9-10)
    {"img": "PILG_AMB", **_PORT},     # 7  s11 pilgrims between Southeast Asia and Jeddah
    {"img": "KUKUP05", **_OUT},       # 8  s12 he inherits the firm (no people)
    {"img": "ABUBAKAR", **_FIX},      # 9  s13 Sultan Abu Bakar (shows the Sultan)
    {"img": "MAP", **_PORT_OUT},      # 10 s14 Pulau Kukup; Constantinople (s14-15)
    {"img": "KUKUP25", **_OUT},       # 11 s16 the crops; 200 men
    {"img": "TL", **_FIX},            # 12 s17 the right to issue money; the 1878 notes (s17-18)
    {"img": "KUKUP05", **_IN},        # 13 s19 the surviving notes; the museum (s19-21)
    {"img": "PILG_MAN", **_PORT},     # 14 s22 labour from the pilgrim trade (s22-23)
    {"img": "ST1881", **_PORT},       # 15 s24 his agent in Jeddah; the Police Court (names him: no people, s24-25)
    {"img": "MAP", **_PORT},          # 16 s26 52 pilgrims; Hadji Daoud (no people, s26-27)
    {"img": "KUKUP25", **_OUT},       # 17 s28 locked up; told to go to Kukup; Siglap (s28-30)
    {"img": "ST1881", **_PORT_OUT},   # 18 s31 debt-slaves; the magistrate (s31-32)
    {"img": "PILG_AMB", **_PORT_OUT}, # 19 s33 the new rule in Jeddah
    {"img": "PILG_MAN", **_PORT_OUT}, # 20 s34 the other side; the Dutch consul (s34-35)
    {"img": "KUKUP05", **_OUT},       # 21 s36 no man sent against his will; cleared (names him: no people, s36-37)
    {"img": "TL", **_FIX},            # 22 s38 Gullick, 1984 (no people)
    {"img": "RAF2", **_IN},           # 23 s39 his land; the Raffles Hotel and Perseverance (names him: no people, s39-40)
    {"img": "MAP", **_PORT_OUT},      # 24 s41 Bukit Tunggal
    {"img": "RAF1", **_IN},           # 25 s42 a public figure; Ottoman consul, Aceh (s42-43)
    {"img": "ABUBAKAR", **_FIX},      # 26 s44 the Sultan of Johor's gifts (shows the Sultan)
    {"img": "NOHCX", **_IN},          # 27 s45 Habib Noh's tomb; the Victoria Memorial Hall (no people, s45-46)
    {"img": "ST1906", **_PORT},       # 28 s47 he dies, 1906; head of the Arab community (names him: no people, s47-48)
    {"img": "RAF1932", **_PORT},      # 29 s49 lying in state; the bier (s49-50)
    {"img": "ST1906", **_PORT_OUT},   # 30 s51 the crowd chanting
    {"img": "BURIAL", **_OUT},        # 31 s52 buried beside his parents; a dollar each (s52-53)
    {"img": "RAF3", **_OUT},          # 32 s54 Johor offices closed; Raffles flag at half-mast
    {"img": "DGRAVE", **_OUT},        # 33 s55 Syed Omar; Faisal Tehrani (no people, s55-56)
    {"img": "KUKUP25", **_IN},        # 34 s57 Pulau Kukup national park, Ramsar
    {"img": "SCH23", **_IN},          # 35 s58 the SMA Wakaf; the school opens 1912 (s58-59)
    {"img": "SCH06", **_IN},          # 36 s60 the oldest madrasah
    {"img": "HADH1920", **_PORT},     # 37 s61 the Hadhrami families
    {"img": "HADH1880", **_PORT},     # 38 s62 the Aljunieds and the Alkaffs
    {"img": "ALKAFFG", **_IN},        # 39 s63 aside: courting, Aljunied Road (s63-64)
    {"img": "ALKAFFM", **_IN},        # 40 s65 aside: Alkaff Mansion (s65-66)
    {"img": "ALKAFFG", **_OUT},       # 41 s67 aside: cooler up there; out of the way now (s67-68)
    {"img": "SCH12", **_IN},          # 42 s69 where it fits (names him: no people)
    {"img": "TL", **_FIX},            # 43 s70 the estate notes and the 1881 case
    {"img": "SCH23", **_OUT},         # 44 s71 a tomb, a school and a trust
]

SCHEDULE = [
    (0.0, 0), (4.875, 1), (22.475, 2), (39.95, 3), (52.425, 4), (63.925, 5),
    (76.9, 6), (95.475, 7), (109.175, 8), (116.4, 9), (128.775, 10), (144.425, 11),
    (153.025, 12), (166.975, 13), (187.425, 14), (201.075, 15), (221.5, 16), (238.05, 17),
    (261.55, 18), (277.675, 19), (290.075, 20), (304.05, 21), (325.1, 22), (335.65, 23),
    (354.5, 24), (366.2, 25), (382.55, 26), (387.2, 27), (403.45, 28), (415.125, 29),
    (436.425, 30), (440.8, 31), (454.475, 32), (465.275, 33), (482.975, 34), (494.425, 35),
    (513.975, 36), (520.25, 37), (527.825, 38), (538.05, 39), (556.225, 40), (567.975, 41),
    (578.95, 42), (592.35, 43), (606.825, 44),
]
TOTAL_DURATION = 614.525
TIMING_JSON = "audio/syed-mohamed-alsagoff-and-the-estate-that-printed-its-own-money.timing.json"

# The avatar presenter, cartoon with motion: corner bubble for the first and last 30 s.
AVATAR = {"ranges": [(0, 30), (-30, None)], "motion": True}
