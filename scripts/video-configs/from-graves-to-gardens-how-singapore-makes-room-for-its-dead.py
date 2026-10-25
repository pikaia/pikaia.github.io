"""Video config for the cemeteries post.

Bukit Brown, Bidadari, Fort Canning Green and Choa Chu Kang, Peck San Theng,
Mount Vernon and Mandai, a 1930s postcard of the Bidadari gates, a 1946 RAF
aerial photograph of Bukit Brown, a 1953 funeral at Bukit Brown, the Straits
Times page of 21 May 1952 on the burial grounds committee, and the map of
former cemeteries.

Named-person rule: there are no pictures here of Ng Thian Eng, Manasseh
Meyer or the author's family, so their sentences show the map, empty
graveyards or buildings. The 1953 funeral photograph sits under the sentence
before Ng Thian Eng is named.

The small or narrow images (the 1946 aerial photo, the 1953 funeral, the
1930s postcard, the 2007 Choa Chu Kang photo, Cuppage's obelisk, the crest),
the newspaper page and the map are letterboxed.

44 slides, 664.65s. Narration: Kokoro with the OpenVoice clone.
AVATAR: first and last 30s, cartoon with motion.
"""

IMAGES = {
    "AERIAL": "https://upload.wikimedia.org/wikipedia/commons/2/27/Aerial_photography_of_Bukit_Brown_Cemetery.png",
    "BID13": "https://upload.wikimedia.org/wikipedia/commons/thumb/e/e8/Bidadari_cemetery.jpg/1280px-Bidadari_cemetery.jpg",
    "BID1": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/d7/Bidadari_cemetery_1.jpg/1280px-Bidadari_cemetery_1.jpg",
    "BID5": "https://upload.wikimedia.org/wikipedia/commons/thumb/b/b5/Bidadari_cemetery_5.jpg/1280px-Bidadari_cemetery_5.jpg",
    "HERO": "https://upload.wikimedia.org/wikipedia/commons/thumb/0/09/Bukit_Brown_Cemetery%2C_Singapore_-_20110326-01.jpg/1280px-Bukit_Brown_Cemetery%2C_Singapore_-_20110326-01.jpg",
    "BB03": "https://upload.wikimedia.org/wikipedia/commons/thumb/7/7c/Bukit_Brown_Cemetery%2C_Singapore_-_20110326-03.jpg/1280px-Bukit_Brown_Cemetery%2C_Singapore_-_20110326-03.jpg",
    "BB04": "https://upload.wikimedia.org/wikipedia/commons/thumb/4/49/Bukit_Brown_Cemetery%2C_Singapore_-_20111210-04.JPG/1280px-Bukit_Brown_Cemetery%2C_Singapore_-_20111210-04.JPG",
    "CCKPATH": "https://upload.wikimedia.org/wikipedia/commons/thumb/2/2b/Chinese_Cemetery_Path_4%2C_2014.jpg/1280px-Chinese_Cemetery_Path_4%2C_2014.jpg",
    "CCK07": "https://upload.wikimedia.org/wikipedia/commons/5/58/Choa_Chu_Kang_Chinese_Cemetery%2C_Singapore_-_20070615.jpg",
    "CCK09": "https://upload.wikimedia.org/wikipedia/commons/e/ed/Choa_Chu_Kang_Chinese_Cemetery%2C_Singapore_-_20090913.jpg",
    "CREST": "https://upload.wikimedia.org/wikipedia/commons/thumb/9/9e/Crest_of_the_Singapore_Municipal_Commission_on_the_gate_of_the_former_Bidadari_Cemetery%2C_Bidadari_Garden%2C_Singapore_-_20121008.jpg/1280px-Crest_of_the_Singapore_Municipal_Commission_on_the_gate_of_the_former_Bidadari_Cemetery%2C_Bidadari_Garden%2C_Singapore_-_20121008.jpg",
    "FUN53": "https://upload.wikimedia.org/wikipedia/commons/2/2d/Funeral_of_Ng_Thian_Eng_at_Bukit_Brown.jpg",
    "BIDGATE": "https://upload.wikimedia.org/wikipedia/commons/thumb/5/58/Gate_of_the_former_Bidadari_Cemetery%2C_Bidadari_Garden%2C_Singapore_-_20121008-02.jpg/1280px-Gate_of_the_former_Bidadari_Cemetery%2C_Bidadari_Garden%2C_Singapore_-_20121008-02.jpg",
    "BIDPC": "https://upload.wikimedia.org/wikipedia/commons/6/6c/Gates_of_Bidadari_Cemetery.jpg",
    "BBSTONE": "https://upload.wikimedia.org/wikipedia/commons/thumb/7/73/Gravestone_in_Bukit_Brown_Cemetery%2C_Singapore_-_20130728.JPG/1280px-Gravestone_in_Bukit_Brown_Cemetery%2C_Singapore_-_20130728.JPG",
    "MKOI": "https://upload.wikimedia.org/wikipedia/commons/thumb/0/06/Mandai_Crematorium%2C_Singapore_-_20150802-01.jpg/1280px-Mandai_Crematorium%2C_Singapore_-_20150802-01.jpg",
    "MANDAI": "https://upload.wikimedia.org/wikipedia/commons/thumb/f/fd/Mandai_Crematorium_and_Columbarium_Complex_Overview%2C_2015.jpg/1280px-Mandai_Crematorium_and_Columbarium_Complex_Overview%2C_2015.jpg",
    "MUSLIM": "https://upload.wikimedia.org/wikipedia/commons/thumb/e/e9/Muslim_Cemetery%2C_Choa_Chu_Kang_01.jpg/1280px-Muslim_Cemetery%2C_Choa_Chu_Kang_01.jpg",
    "PUSARA": "https://upload.wikimedia.org/wikipedia/commons/thumb/8/80/Pusara_Abadi.jpg/1280px-Pusara_Abadi.jpg",
    "CUPP": "https://upload.wikimedia.org/wikipedia/commons/thumb/5/57/Gravestone_of_William_Cuppage%2C_Fort_Canning_Green%2C_Singapore_-_20130401-01.jpg/1280px-Gravestone_of_William_Cuppage%2C_Fort_Canning_Green%2C_Singapore_-_20130401-01.jpg",
    "FCG1": "https://upload.wikimedia.org/wikipedia/commons/thumb/a/a1/Gravestones_in_Fort_Canning_Green%2C_Singapore%2C_relocated_from_Bukit_Timah_Cemetery_-_20130401-01.jpg/1280px-Gravestones_in_Fort_Canning_Green%2C_Singapore%2C_relocated_from_Bukit_Timah_Cemetery_-_20130401-01.jpg",
    "FCG2": "https://upload.wikimedia.org/wikipedia/commons/thumb/c/cb/Gravestones_in_Fort_Canning_Green%2C_Singapore%2C_relocated_from_Bukit_Timah_Cemetery_-_20130401-02.jpg/1280px-Gravestones_in_Fort_Canning_Green%2C_Singapore%2C_relocated_from_Bukit_Timah_Cemetery_-_20130401-02.jpg",
    "FCG11": "https://upload.wikimedia.org/wikipedia/commons/thumb/3/31/Gravestones_in_Fort_Canning_Green%2C_Singapore_-_20110116.jpg/1280px-Gravestones_in_Fort_Canning_Green%2C_Singapore_-_20110116.jpg",
    "PST": "https://upload.wikimedia.org/wikipedia/commons/thumb/5/52/Kwong_Wai_Siew_Peck_San_Theng.jpg/1280px-Kwong_Wai_Siew_Peck_San_Theng.jpg",
    "MANDAI3": "https://upload.wikimedia.org/wikipedia/commons/thumb/4/42/Mandai_Crematorium_and_Columbarium_Complex_Overview_3%2C_2015.jpg/1280px-Mandai_Crematorium_and_Columbarium_Complex_Overview_3%2C_2015.jpg",
    "MVN": "https://upload.wikimedia.org/wikipedia/commons/thumb/c/cd/Niches%2C_Mount_Vernon_columbarium_complex.jpg/1280px-Niches%2C_Mount_Vernon_columbarium_complex.jpg",
    "ST52": "/assets/images/straits-times-1952-05-21-page-8.jpg",
    "MAP": "/assets/images/singapore-former-cemeteries-map.png",
}

# Credits for images not captioned in the post or its gallery.
CREDITS = {
    "BID1": "ProjectManhattan, CC BY-SA 3.0, via Wikimedia Commons",
    "BB04": "Jacklee, CC BY-SA 3.0, via Wikimedia Commons",
    "CCKPATH": "Jnzl, CC BY 2.0, via Wikimedia Commons",
    "CREST": "Smuconlaw, CC BY-SA 3.0, via Wikimedia Commons",
    "MKOI": "Jacklee, CC BY-SA 4.0, via Wikimedia Commons",
    "PUSARA": "M. Adrian Jurhami, CC BY 4.0, via Wikimedia Commons",
    "FCG2": "Smuconlaw, CC BY-SA 3.0, via Wikimedia Commons",
    "FCG11": "David Lee, CC BY-SA 2.0, via Wikimedia Commons",
}

# The channel's 2x2 thumbnail grid, 1930s to today: the Bidadari gates in the
# 1930s, a funeral at Bukit Brown in 1953, the emptied Bidadari ground in 2013,
# and the Mandai crematorium and columbarium in 2015.
THUMBNAIL = [
    {"img": "BIDPC", "pan": (0.5, 0.5)},
    {"img": "FUN53", "pan": (0.5, 0.5)},
    {"img": "BID13", "pan": (0.5, 0.5)},
    {"img": "MANDAI", "pan": (0.5, 0.5)},
]

_E = "ease-in-out"
_IN = {"type": "cover", "zoom": [1.0, 1.06, 1.12], "pan": [(0.5, 0.5)] * 3, "ease": _E}
_OUT = {"type": "cover", "zoom": [1.12, 1.06, 1.0], "pan": [(0.5, 0.5)] * 3, "ease": _E}
# Small or narrow photos, the newspaper page and the map: letterbox, modest zoom.
_PORT = {"type": "letterbox", "zoom": [1.0, 1.04, 1.08], "pan": [(0.5, 0.5)] * 3, "ease": _E}
_PORT_OUT = {"type": "letterbox", "zoom": [1.08, 1.04, 1.0], "pan": [(0.5, 0.5)] * 3, "ease": _E}

SLIDES = [
    {"img": "HERO", **_IN},           # 0  s0 title
    {"img": "BID13", **_IN},          # 1  s1 21 cemeteries cleared by 1985
    {"img": "BID5", **_IN},           # 2  s2 Bidadari emptied; graves leased for 15 years
    {"img": "MANDAI", **_IN},         # 3  s3 burial to cremation to gardens
    {"img": "FCG11", **_IN},          # 4  s4 Fort Canning, 1823-1865
    {"img": "FCG1", **_IN},           # 5  s5 the Bukit Timah Road cemetery
    {"img": "CUPP", **_PORT},         # 6  s6 a dozen stones moved to Fort Canning Green
    {"img": "BIDPC", **_PORT},        # 7  s7 the municipal cemeteries; Bidadari, 1908 (s7-8)
    {"img": "AERIAL", **_PORT},       # 8  s9 Bukit Brown, 1922
    {"img": "PST", **_IN},            # 9  s10 the clan cemeteries; Peck San Theng
    {"img": "MAP", **_PORT},          # 10 s11 the Jewish cemeteries; Manasseh Meyer (map only)
    {"img": "FUN53", **_PORT},        # 11 s12 funerals as public events
    {"img": "BB03", **_IN},           # 12 s13 Ng Thian Eng's funeral (no people)
    {"img": "ST52", **_PORT},         # 13 s14 the 1950 committee; its 1952 report (s14-15)
    {"img": "BB04", **_IN},           # 14 s16 1,730 acres; flats on old graveyards
    {"img": "ST52", **_PORT_OUT},     # 15 s17 a crematorium; not compulsory (s17-19)
    {"img": "BBSTONE", **_IN},        # 16 s20 the Chinese community's support
    {"img": "MVN", **_IN},            # 17 s21 Mount Vernon, 1962 and 1976
    {"img": "CCK07", **_PORT},        # 18 s22 Choa Chu Kang, 1947
    {"img": "BID1", **_IN},           # 19 s23 the last burials, 1972-73
    {"img": "CCKPATH", **_IN},        # 20 s24 the only cemetery still open
    {"img": "MAP", **_PORT_OUT},      # 21 s25 closed land taken for development
    {"img": "PST", **_OUT},           # 22 s26 Peck San Theng exhumed for Bishan (s26-27)
    {"img": "MAP", **_PORT},          # 23 s28 Thomson Road cleared for Novena (s28-29)
    {"img": "BIDGATE", **_IN},        # 24 s30 Bidadari exhumed, 2001-06
    {"img": "MUSLIM", **_IN},         # 25 s31 reburied at Choa Chu Kang; ashes at sea
    {"img": "AERIAL", **_PORT_OUT},   # 26 s32 Bukit Brown loses 3,746 graves
    {"img": "MANDAI3", **_IN},        # 27 s33 cremation the norm; Mandai (s33-34)
    {"img": "MKOI", **_IN},           # 28 s35 66 to 80 per cent; niches (s35-36)
    {"img": "MVN", **_OUT},           # 29 s37 Mount Vernon columbarium closed (s37-38)
    {"img": "MANDAI", **_OUT},        # 30 s39 fixed-term niches (s39-40)
    {"img": "MANDAI3", **_OUT},       # 31 s41 my family at St Theresa's (no people)
    {"img": "CCK09", **_PORT},        # 32 s42 fifteen years; exhumations from 2004 (s42-44)
    {"img": "PUSARA", **_IN},         # 33 s45 Tengah Air Base, 2017
    {"img": "CCK07", **_PORT_OUT},    # 34 s46 cremated the same day; scattering (s46-47)
    {"img": "MUSLIM", **_OUT},        # 35 s48 reburial in smaller plots
    {"img": "MAP", **_PORT},          # 36 s49 at sea; my father off Punggol End (s49-50)
    {"img": "CCKPATH", **_OUT},       # 37 s51 the Garden of Peace (s51-53)
    {"img": "MKOI", **_OUT},          # 38 s54 demand; the Garden of Serenity (s54-55)
    {"img": "CREST", **_PORT},        # 39 s56 my mother and brother (no people, s56-58)
    {"img": "FCG2", **_IN},           # 40 s59 Catholic teaching (s59-62)
    {"img": "BBSTONE", **_OUT},       # 41 s63 pragmatism
    {"img": "BB03", **_OUT},          # 42 s64 where it fits (s64-65)
    {"img": "HERO", **_OUT},          # 43 s66 close
]

SCHEDULE = [
    (0.0, 0), (4.8, 1), (16.575, 2), (29.1, 3), (42.225, 4), (52.975, 5),
    (64.225, 6), (74.15, 7), (89.2, 8), (101.35, 9), (117.85, 10), (132.025, 11),
    (136.45, 12), (148.975, 13), (176.375, 14), (189.525, 15), (218.4, 16), (227.05, 17),
    (236.675, 18), (244.475, 19), (257.3, 20), (263.45, 21), (268.475, 22), (291.625, 23),
    (308.4, 24), (321.625, 25), (332.45, 26), (342.525, 27), (360.575, 28), (381.475, 29),
    (396.1, 30), (416.025, 31), (428.825, 32), (449.95, 33), (464.65, 34), (478.9, 35),
    (489.55, 36), (507.95, 37), (530.075, 38), (552.225, 39), (574.2, 40), (611.025, 41),
    (623.85, 42), (649.9, 43),
]
TOTAL_DURATION = 664.975
TIMING_JSON = "audio/from-graves-to-gardens-how-singapore-makes-room-for-its-dead.timing.json"

# The avatar presenter, cartoon with motion: corner bubble for the first and last 30 s.
AVATAR = {"ranges": [(0, 30), (-30, None)], "motion": True}
