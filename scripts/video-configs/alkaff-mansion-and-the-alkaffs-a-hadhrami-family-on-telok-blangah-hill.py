"""Video config for the Alkaff Mansion post.

The mansion in 2006 and 2019, the Hadhramaut on a map of Hadhrami
emigration, Tarim from the air in 1929 and its palaces in 1994, the
Al-Muhdhar minaret, the Alkaff Arcade on two postcards, the Collyer Quay
waterfront, the Hotel de l'Europe in 1897, the Alkaff Lake Gardens on two
old photographs, the two Alkaff mosques, Telok Blangah Hill Park, the
Straits Times pages of 1909 and 1950, the map and the timeline.

Named-person rule: there are no portraits of the Alkaffs, so every sentence
naming a family member, Craik, Buckley or Ingrams shows a place with no
people. The 1950 page (which has a portrait of an unrelated MP) is shown
only under sentences that name no one.

The map, the emigration map, the Tarim aerial, the Tarim minaret, the
portrait Arcade postcard, the small garden photo, the Upper Serangoon
minaret and both newspaper pages are letterboxed; the timeline is fixed.

36 slides, 591.1s. Narration: Kokoro with the OpenVoice clone.
AVATAR: first and last 30s, cartoon with motion.
"""

IMAGES = {
    "HERO": "https://upload.wikimedia.org/wikipedia/commons/6/6c/AlkaffMansion.jpg",
    "MANSION19": "https://upload.wikimedia.org/wikipedia/commons/thumb/a/a3/Alkaff_Mansion.png/1280px-Alkaff_Mansion.png",
    "HADMAP": "https://upload.wikimedia.org/wikipedia/commons/thumb/7/74/Map_of_Hadhrami_emigrations.svg/1280px-Map_of_Hadhrami_emigrations.svg.png",
    "TARIM29": "https://upload.wikimedia.org/wikipedia/commons/d/d4/Tarim_RAF_1929.jpg",
    "WATERFRONT": "https://upload.wikimedia.org/wikipedia/commons/thumb/0/0f/Gebouwen_langs_de_kade_in_de_haven_van_Singapore%2C_KITLV_29186.tiff/lossy-page1-1280px-Gebouwen_langs_de_kade_in_de_haven_van_Singapore%2C_KITLV_29186.tiff.jpg",
    "TARIM94": "https://upload.wikimedia.org/wikipedia/commons/thumb/8/8a/Yemen_Tarim_Hadhramaut_1994_-_167531378_63715937ff_o.jpg/1280px-Yemen_Tarim_Hadhramaut_1994_-_167531378_63715937ff_o.jpg",
    "MINARET_T": "https://upload.wikimedia.org/wikipedia/commons/6/6d/Minaret_Al_Muhdhar_Mosque_Tarim_Yemen.jpg",
    "ARCADE": "https://upload.wikimedia.org/wikipedia/commons/thumb/4/4b/Collyer_Quay%2C_Singapore_postcard.jpg/1280px-Collyer_Quay%2C_Singapore_postcard.jpg",
    "ST1909": "/assets/images/straits-times-1909-11-27-page-7.jpg",
    "ARCADE2": "https://upload.wikimedia.org/wikipedia/commons/thumb/b/b1/De_Arcade_te_Singapore%2C_KITLV_34272.tiff/lossy-page1-960px-De_Arcade_te_Singapore%2C_KITLV_34272.tiff.jpg",
    "EUROPE97": "https://upload.wikimedia.org/wikipedia/commons/thumb/2/2a/KITLV_-_29176_-_Lambert_%26_Co.%2C_G.R._-_Singapore_-_Hotel_de_l%27Europe_at_Singapore_-_1897.tif/lossy-page1-1280px-KITLV_-_29176_-_Lambert_%26_Co.%2C_G.R._-_Singapore_-_Hotel_de_l%27Europe_at_Singapore_-_1897.tif.jpg",
    "MAP": "/assets/images/alkaff-map.png",
    "GARDEN": "https://upload.wikimedia.org/wikipedia/commons/thumb/e/ea/Alkaff_Garden%2C_Singapore.%2C_KITLV_1404907.tiff/lossy-page1-1280px-Alkaff_Garden%2C_Singapore.%2C_KITLV_1404907.tiff.jpg",
    "MOSQUE": "https://upload.wikimedia.org/wikipedia/commons/thumb/4/48/Masjid_Alkaff_Upper_Serangoon%2C_October_2025.jpg/1280px-Masjid_Alkaff_Upper_Serangoon%2C_October_2025.jpg",
    "KMELAYU": "https://upload.wikimedia.org/wikipedia/commons/thumb/1/19/Bedok_-_Masjid_Alkaff_at_Kampung_Melayu.jpg/1280px-Bedok_-_Masjid_Alkaff_at_Kampung_Melayu.jpg",
    "TERRACE": "https://upload.wikimedia.org/wikipedia/commons/thumb/9/9f/Terrace_Garden%2C_Telok_Blangah_Hill_Park%2C_Singapore_-_20100102.jpg/1280px-Terrace_Garden%2C_Telok_Blangah_Hill_Park%2C_Singapore_-_20100102.jpg",
    "GARDEN2": "https://upload.wikimedia.org/wikipedia/commons/d/d6/Alkaff_Gardens%2C_Singapore.jpg",
    "ST1950": "/assets/images/straits-times-1950-07-18-page-7.jpg",
    "TL": "/assets/images/alkaff-timeline-chart.png",
    "MINARET_S": "https://upload.wikimedia.org/wikipedia/commons/thumb/8/8d/Ottoman-styled_minaret_at_Masjid_Alkaff_Upper_Serangoon.jpg/1280px-Ottoman-styled_minaret_at_Masjid_Alkaff_Upper_Serangoon.jpg",
}

# The timeline PNG is the only image not captioned in the post or its gallery.
CREDITS = {
    "TL": "Timeline by Lesser Known Singapore, from Roots.gov.sg, Wikipedia, BiblioAsia, NParks and The Straits Times",
}

# The channel's 2x2 thumbnail grid, earliest to today: Tarim in 1929 (the
# family's home town), the Arcade around 1910, the Alkaff Lake Gardens in
# the 1930s and the mansion in 2019.
THUMBNAIL = [
    {"img": "TARIM29", "pan": (0.5, 0.5)},
    {"img": "ARCADE", "pan": (0.5, 0.4)},
    {"img": "GARDEN", "pan": (0.5, 0.5)},
    {"img": "MANSION19", "pan": (0.5, 0.4)},
]

_E = "ease-in-out"
_IN = {"type": "cover", "zoom": [1.0, 1.06, 1.12], "pan": [(0.5, 0.5)] * 3, "ease": _E}
_OUT = {"type": "cover", "zoom": [1.12, 1.06, 1.0], "pan": [(0.5, 0.5)] * 3, "ease": _E}
# The maps, portrait and small images and the newspaper pages: letterbox, modest zoom.
_PORT = {"type": "letterbox", "zoom": [1.0, 1.04, 1.08], "pan": [(0.5, 0.5)] * 3, "ease": _E}
_PORT_OUT = {"type": "letterbox", "zoom": [1.08, 1.04, 1.0], "pan": [(0.5, 0.5)] * 3, "ease": _E}
# The timeline: letterboxed and still, so its labels stay readable.
_FIX = {"type": "letterbox", "zoom": [1.0, 1.0, 1.0], "pan": [(0.5, 0.5)] * 3, "ease": "linear"}

SLIDES = [
    {"img": "HERO", **_IN},           # 0  s0 title: the mansion
    {"img": "MANSION19", **_IN},      # 1  s1 the white house with a clock tower; built around 1918 (s1-2)
    {"img": "HADMAP", **_PORT},       # 2  s3 the Hadhramaut, a desert valley in Yemen
    {"img": "TARIM29", **_PORT},      # 3  s4 sayyids from Tarim; Indian Ocean traders (s4-5)
    {"img": "HADMAP", **_PORT_OUT},   # 4  s6 Syed Shaik arrives in 1852 (names him: no people)
    {"img": "WATERFRONT", **_IN},     # 5  s7 Alkaff and Company; property owners (s7-9)
    {"img": "TARIM94", **_IN},        # 6  s10 money sent home; the Tarim palaces (s10-11)
    {"img": "MINARET_T", **_PORT},    # 7  s12 Abubakr; school, road, the 1936 truce (names him and Ingrams: no people, s12-14)
    {"img": "ARCADE", **_IN},         # 8  s15 the Alkaff Arcade opens, 1909
    {"img": "ST1909", **_PORT},       # 9  s16 Craik's design; the passage; the Straits Times (names Craik: no people, s16-18)
    {"img": "ARCADE2", **_PORT},      # 10 s19 Guthrie's godowns; the first tenants (s19-20)
    {"img": "ST1909", **_PORT_OUT},   # 11 s21 the luncheon (names Buckley and Syed Shaik: no people)
    {"img": "EUROPE97", **_IN},       # 12 s22 the Hotel de l'Europe
    {"img": "MAP", **_PORT},          # 13 s23 Syed Abdul Rahman's park off Upper Serangoon Road (names him: no people)
    {"img": "GARDEN", **_IN},         # 14 s24 the Japanese garden; lake, bridges, tea houses (s24-25)
    {"img": "MOSQUE", **_IN},         # 15 s26 the Upper Serangoon mosque, 1932 (s26-28)
    {"img": "KMELAYU", **_IN},        # 16 s29 the Kampung Melayu mosque (names Syed Ahmad: no people, s29-30)
    {"img": "TERRACE", **_IN},        # 17 s31 Mount Washington; the land bought in 1916 (s31-32)
    {"img": "HERO", **_OUT},          # 18 s33 the builder (names Syed Abdulrahman: the house only)
    {"img": "TERRACE", **_OUT},       # 19 s34 a weekend house; parties and receptions (s34-36)
    {"img": "GARDEN2", **_PORT},      # 20 s37 1941: the gardens requisitioned, bombed, closed (s37-38)
    {"img": "GARDEN", **_OUT},        # 21 s39 kept out of his own park (names him: the garden only)
    {"img": "WATERFRONT", **_OUT},    # 22 s40 fortunes fade; rent control (s40-41)
    {"img": "TARIM29", **_PORT_OUT},  # 23 s42 he dies in Tarim, 1948 (names him: no people)
    {"img": "ST1950", **_PORT},       # 24 s43 the 1950 sale; the lake to be filled in (s43-44)
    {"img": "MAP", **_PORT_OUT},      # 25 s45 the lake drained in 1964; the school today (s45-46)
    {"img": "ARCADE", **_OUT},        # 26 s47 the Arcade pulled down, 1978
    {"img": "HERO", **_IN},           # 27 s48 the house stands empty
    {"img": "TL", **_FIX},            # 28 s49 restored; the 1990 restaurant; rijsttafel (s49-50)
    {"img": "TERRACE", **_IN},        # 29 s51 the gong and the kebayas, up on the hill
    {"img": "MANSION19", **_OUT},     # 30 s52 Chris's lunch there (s52-55)
    {"img": "HERO", **_OUT},          # 31 s56 closed 2003; conservation; the Italian restaurant (s56-57)
    {"img": "MANSION19", **_IN},      # 32 s58 1-Group since 2019; weddings (s58-59)
    {"img": "MINARET_S", **_PORT},    # 33 s60 the name on the map; the mosques and the new lake (s60-62)
    {"img": "TL", **_FIX},            # 34 s63 where it fits
    {"img": "HERO", **_IN},           # 35 s64 the name outlives them
]

SCHEDULE = [
    (0.0, 0), (5.925, 1), (25.9, 2), (36.425, 3), (54.375, 4), (66.225, 5),
    (93.65, 6), (110.875, 7), (137.925, 8), (147.95, 9), (177.1, 10), (193.9, 11),
    (204.5, 12), (214.825, 13), (224.8, 14), (247.325, 15), (266.825, 16), (282.4, 17),
    (300.55, 18), (316.4, 19), (342.425, 20), (365.925, 21), (370.725, 22), (384.55, 23),
    (391.225, 24), (412.625, 25), (423.9, 26), (434.125, 27), (446.425, 28), (472.25, 29),
    (479.2, 30), (503.075, 31), (520.725, 32), (535.725, 33), (564.175, 34), (579.925, 35),
]
TOTAL_DURATION = 591.1
TIMING_JSON = "audio/alkaff-mansion-and-the-alkaffs-a-hadhrami-family-on-telok-blangah-hill.timing.json"

# The avatar presenter, cartoon with motion: corner bubble for the first and last 30 s.
AVATAR = {"ranges": [(0, 30), (-30, None)], "motion": True}
