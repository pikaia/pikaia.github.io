"""Video config for the John Turnbull Thomson post.

Thomson's Singapore is told through his own pictures (Telok Ayer Market,
Public Offices, Pearl's Hill, the stonecutters, Horsburgh Lighthouse), his
charts (Admiralty 2404, the Tioman chart), and contemporary prints of the town
and harbour (Dyce's Government Hill, the two Atlas pittoresque plates). Named
people get their own picture or none: Thomson's portrait (s2, s9, s49, s76),
Whampoa's two portraits (s46-47, s51), Munshi Abdullah's signature (s53-55);
Coleman (s8), Tan Tock Seng (s57) and the Governor-General (s59) get a
building or a print with no portrait. The small paintings, portraits and
charts are letterboxed with a modest zoom; the timeline and tiger map are
letterboxed and frozen.
Video-only: the Penang painting (s5-6), the gambier plantation photo
(s40-41, s44-45) and tiger map from the wild tigers post, Thomson's sepia
lighthouse and the Pulau Ubin convict quarry from the Horsburgh post, and the
small Hoo Ah Kay portrait and Abdullah's signature.

54 slides, 713.15s. Narration: Kokoro with the OpenVoice clone.
AVATAR: first and last 30s, cartoon with motion.
"""

_U = "https://upload.wikimedia.org/wikipedia/commons"
_C = f"{_U}/thumb"
_A = "/assets/images"

IMAGES = {
    "TELOK": f"{_C}/7/77/Telok_Ayer_Market_-_J.T._Thomson.jpg/1280px-Telok_Ayer_Market_-_J.T._Thomson.jpg",
    "THOMSON": f"{_U}/0/03/JohnTurnbullThomson.jpg",
    "PEARLS": f"{_U}/6/6a/John_Turnbull_Thomson_-_Singapore_Town_from_Pearl%27s_Hill_Looking_East.jpg",
    "ADM2404": f"{_C}/3/32/Admiralty_Chart_No_2404_Strait_of_Singapore_Sheet_3_Surveyed_by_J.T._Thomson_Esq._Government_Survr._1846-54%2C_Published_1855%2C_Corrections_to_1866.jpg/1280px-Admiralty_Chart_No_2404_Strait_of_Singapore_Sheet_3_Surveyed_by_J.T._Thomson_Esq._Government_Survr._1846-54%2C_Published_1855%2C_Corrections_to_1866.jpg",
    "PUBLIC": f"{_U}/d/df/Public_Offices%2C_Singapore_by_John_Turnbull_Thomson_1846.jpg",
    "STONECUT": f"{_U}/3/35/ChineseKayTribeStonecutters-Singapore.jpg",
    "WHAMPOA": f"{_C}/7/7b/The_Hon._Hoh-Ah-Kay_Whampoa%2C_C.M.G.%2C_M.L.C.%2C_and_Consul_for_Wellcome_V0037527.jpg/1280px-The_Hon._Hoh-Ah-Kay_Whampoa%2C_C.M.G.%2C_M.L.C.%2C_and_Consul_for_Wellcome_V0037527.jpg",
    "TTSH": f"{_U}/c/c3/Tan_Tock_Seng_Hospital_circa_1844-1856.jpg",
    "DUNEDIN": f"{_C}/4/41/John_Turnbull_Thomson_Dunedin.jpg/1280px-John_Turnbull_Thomson_Dunedin.jpg",
    "ROAD2": f"{_C}/d/d3/Thomson_Road_Singapore_January_1965_02.jpg/1280px-Thomson_Road_Singapore_January_1965_02.jpg",
    "TIMELINE": f"{_A}/thomson-timeline-chart.png",
    # Gallery images:
    "DYCE": f"{_C}/0/02/Charles_Dyce%2C_Government_Hill_from_the_New_Harbour_Road%2C_Singapore%2C_1846%2C_Watercolour_%26_Ink_on_paper%2C_27.2_x_44.8_cm.png/1280px-Charles_Dyce%2C_Government_Hill_from_the_New_Harbour_Road%2C_Singapore%2C_1846%2C_Watercolour_%26_Ink_on_paper%2C_27.2_x_44.8_cm.png",
    "ATLAS134": f"{_C}/a/a1/Atlas_pittoresque_pl_134.jpg/1280px-Atlas_pittoresque_pl_134.jpg",
    "ATLAS136": f"{_C}/a/a7/Atlas_pittoresque_pl_136.jpg/1280px-Atlas_pittoresque_pl_136.jpg",
    "HORSLITHO": f"{_C}/e/e2/Horsburgh_Lighthouse_by_John_T_Thomson_1851.jpg/1280px-Horsburgh_Lighthouse_by_John_T_Thomson_1851.jpg",
    "TIOMAN": f"{_C}/7/7a/Singapore_to_Tioman_I._By_Mr._J._T._Thomson%2C_Government_Surveyor%2C_1849.png/1280px-Singapore_to_Tioman_I._By_Mr._J._T._Thomson%2C_Government_Surveyor%2C_1849.png",
    "AVENUE": f"{_U}/f/fb/Avenue_to_Whampoa%27s_Gardens_%281886%29.png",
    "OBELISK": f"{_U}/2/29/EmpressPlaceBuilding-DalhousieObelisk-Singapore-1965.jpg",
    "ROAD1": f"{_C}/d/da/Thomson_Road_Singapore_January_1965_01.jpg/1280px-Thomson_Road_Singapore_January_1965_01.jpg",
    "ROCKY": f"{_U}/7/72/One_of_John_Turnbull_Thomson%27s_aquarelles._1860s.jpg",
    "EARNSLAW": f"{_U}/b/b8/Earnslaw00.jpg",
    "STATUE": f"{_C}/0/0d/John_Turnbull_Thompson_statue_looking_towards_Centennial_Milk_Bar_building.jpg/1280px-John_Turnbull_Thompson_statue_looking_towards_Centennial_Milk_Bar_building.jpg",
    # Not in this post's captions (credited below):
    "PENANG": f"{_U}/a/a1/Penang_Museum_historical_painting_537.jpg",
    "GAMBIER": f"{_U}/0/0d/ChineseGambierSingapore.jpg",
    "TIGERMAP": f"{_A}/when-singapore-had-wild-tigers-map.png",
    "SEPIA": f"{_U}/8/82/HorsburghLighthouse-JTThomson-1851-02.jpg",
    "UBIN": f"{_C}/3/33/Convicts_stone-quarrying_at_Pulau_Ubin%2C_Singapore_%28McNair_1899%2C_Plate_XX%29.jpg/1280px-Convicts_stone-quarrying_at_Pulau_Ubin%2C_Singapore_%28McNair_1899%2C_Plate_XX%29.jpg",
    "HOOAHKAY": f"{_U}/c/cc/Hoo_Ah_Kay.jpg",
    "SIG": f"{_C}/6/69/Signature_of_Munshi_Abdullah.jpg/1280px-Signature_of_Munshi_Abdullah.jpg",
}

# Credits for images not captioned in the post or its gallery.
CREDITS = {
    "TIMELINE": "Timeline by Lesser Known Singapore",
    "PENANG": "Penang State Museum and Art Gallery, public domain, via Wikimedia Commons",
    "GAMBIER": "National Archives of Singapore, via Wikimedia Commons, public domain",
    "TIGERMAP": "Map by Lesser Known Singapore; base map data © OpenStreetMap contributors",
    "SEPIA": "John Turnbull Thomson, public domain, via Wikimedia Commons",
    "UBIN": "Unknown author, public domain, via Wikimedia Commons",
    "HOOAHKAY": "Unknown author, public domain, via Wikimedia Commons",
    "SIG": "Abdullah Abdul Kadir, CC0, via Wikimedia Commons",
}

_E = "ease-in-out"
_IN = {"type": "cover", "zoom": [1.0, 1.06, 1.12], "pan": [(0.5, 0.5)] * 3, "ease": _E}
_OUT = {"type": "cover", "zoom": [1.12, 1.06, 1.0], "pan": [(0.5, 0.5)] * 3, "ease": _E}
# Small paintings, portraits, charts and the signature: letterbox, modest zoom.
_PORT = {"type": "letterbox", "zoom": [1.0, 1.04, 1.08], "pan": [(0.5, 0.5)] * 3, "ease": _E}
_PORT_OUT = {"type": "letterbox", "zoom": [1.08, 1.04, 1.0], "pan": [(0.5, 0.5)] * 3, "ease": _E}
# The timeline and tiger map: letterbox, frozen.
_GFX = {"type": "letterbox", "zoom": [1, 1, 1], "pan": [(0.5, 0.5)] * 3}

SLIDES = [
    {"img": "TELOK", **_IN},           # 0  s0   title
    {"img": "ROAD2", **_IN},           # 1  s1   Thomson Road, Thomson Plaza, the TEL line
    {"img": "THOMSON", **_PORT},       # 2  s2   arrived 1841 as Government Surveyor, aged twenty
    {"img": "PUBLIC", **_PORT},        # 3  s3   his pictures: few images of 1840s Singapore
    {"img": "TIMELINE", **_GFX},       # 4  s4   born at Glororum, 1821
    {"img": "PENANG", **_PORT},        # 5  s5   Aberdeen, Newcastle, Penang 1838; the villagers (s6)
    {"img": "DYCE", **_IN},            # 6  s7   appointed Government Surveyor, 25 October 1841
    {"img": "ATLAS134", **_IN},        # 7  s8   Public Works from Coleman, 1844
    {"img": "THOMSON", **_PORT_OUT},   # 8  s9   one young man responsible for it all
    {"img": "PEARLS", **_PORT},        # 9  s10  a town of 30,000; the European quarter (s11)
    {"img": "ATLAS134", **_OUT},       # 10 s12  the Chinese town, Malay villages; fires (s13)
    {"img": "ATLAS136", **_IN},        # 11 s14  the harbour crowded with ships; 200 Europeans (s15)
    {"img": "DYCE", **_OUT},           # 12 s16  Scandal Point; no banks, iron safes (s17)
    {"img": "PEARLS", **_PORT_OUT},    # 13 s18  a harder side; gang robberies (s19)
    {"img": "ATLAS136", **_OUT},       # 14 s20  twenty bodies; a police chief only in 1843 (s21)
    {"img": "ADM2404", **_PORT},       # 15 s22  measurement: the allotment and topographical surveys
    {"img": "TIMELINE", **_GFX},       # 16 s24  the 1846 Plan of Singapore Town (s25-26)
    {"img": "TIOMAN", **_PORT},        # 17 s27  at sea: the strait and the coast to Tioman (s28)
    {"img": "ADM2404", **_PORT_OUT},   # 18 s29  Admiralty charts with his name in the title (s30)
    {"img": "SEPIA", **_PORT},         # 19 s31  no training as an artist; the books (s32)
    {"img": "PUBLIC", **_PORT_OUT},    # 20 s33  the Public Offices
    {"img": "PEARLS", **_PORT},        # 21 s34  the view from Pearl's Hill
    {"img": "TELOK", **_IN},           # 22 s35  Telok Ayer Market on stilts
    {"img": "STONECUT", **_PORT},      # 23 s36  people at work: the stonecutters (s37)
    {"img": "HORSLITHO", **_IN},       # 24 s38  the lighthouse on Pedra Branca; earlier post (s39)
    {"img": "GAMBIER", **_PORT},       # 25 s40  up the Kallang by canoe; gambier and pepper (s41)
    {"img": "TIGERMAP", **_GFX},       # 26 s42  tiger footprints; the pit trap (s43)
    {"img": "GAMBIER", **_PORT_OUT},   # 27 s44  100 Spanish dollars a head; earlier post (s45)
    {"img": "WHAMPOA", **_PORT},       # 28 s46  his friend Whampoa
    {"img": "HOOAHKAY", **_PORT},      # 29 s47  a boy in his father's shop
    {"img": "AVENUE", **_PORT},        # 30 s48  the orange garden at Toa Payoh
    {"img": "THOMSON", **_PORT},       # 31 s49  "scratch" and "sketch" (s50)
    {"img": "WHAMPOA", **_PORT_OUT},   # 32 s51  the portrait kept with care; earlier post (s52)
    {"img": "SIG", **_PORT},           # 33 s53  Munshi Abdullah; the 1874 translation (s54-55)
    {"img": "PUBLIC", **_PORT},        # 34 s56  Superintendent of Public Works
    {"img": "TTSH", **_PORT},          # 35 s57  the Pearl's Hill hospital, Tan Tock Seng
    {"img": "PEARLS", **_PORT_OUT},    # 36 s58  Thomson Bridge; Coleman Bridge
    {"img": "OBELISK", **_IN},         # 37 s59  St Andrew's spire; the Dalhousie Obelisk
    {"img": "ROAD1", **_PORT},         # 38 s60  roads into the interior
    {"img": "UBIN", **_IN},            # 39 s61  convict labourers from India
    {"img": "DYCE", **_IN},            # 40 s62  the 1852 water report
    {"img": "TIMELINE", **_GFX},       # 41 s63  sick leave, August 1853; the News Room (s64)
    {"img": "ROCKY", **_PORT},         # 42 s65  Britain, Europe, New Zealand 1856
    {"img": "DUNEDIN", **_IN},         # 43 s66  Chief Surveyor of Otago; Invercargill (s67)
    {"img": "EARNSLAW", **_PORT},      # 44 s68  Surveyor-General, 1876-79
    {"img": "STONECUT", **_PORT_OUT},  # 45 s69  Some Glimpses into Life in the Far East
    {"img": "TIMELINE", **_GFX},       # 46 s70  died at Invercargill, 1884
    {"img": "STATUE", **_IN},          # 47 s71  the Ranfurly statue
    {"img": "ROAD2", **_OUT},          # 48 s72  his name on the map; Thomson Road (s73)
    {"img": "ROAD1", **_PORT_OUT},     # 49 s74  Thomson Plaza, the TEL line
    {"img": "ADM2404", **_PORT},       # 50 s75  his charts, plan and drawings in collections
    {"img": "THOMSON", **_PORT_OUT},   # 51 s76  why it matters: one man measured and drew it
    {"img": "ATLAS134", **_IN},        # 52 s77  a small, rough and crowded port
    {"img": "TELOK", **_OUT},          # 53 s78  a road, a district and an MRT line
]

SCHEDULE = [(0.0, 0), (5.125, 1), (15.35, 2), (30.35, 3), (46.35, 4), (54.35, 5), (79.55, 6), (90.0, 7), (102.875, 8), (114.025, 9), (133.1, 10), (151.125, 11), (160.9, 12), (182.4, 13), (199.175, 14), (218.6, 15), (231.975, 16), (255.75, 17), (268.975, 18), (281.125, 19), (297.1, 20), (304.175, 21), (313.525, 22), (325.325, 23), (337.925, 24), (353.775, 25), (374.2, 26), (390.375, 27), (401.125, 28), (407.775, 29), (417.025, 30), (426.75, 31), (447.95, 32), (458.825, 33), (484.125, 34), (493.325, 35), (504.2, 36), (512.75, 37), (524.1, 38), (531.85, 39), (540.35, 40), (550.025, 41), (570.45, 42), (579.05, 43), (593.8, 44), (606.675, 45), (622.1, 46), (629.45, 47), (640.65, 48), (657.425, 49), (666.2, 50), (677.375, 51), (690.35, 52), (703.775, 53)]
TOTAL_DURATION = 713.15
TIMING_JSON = "audio/john-turnbull-thomson-the-surveyor-who-drew-1840s-singapore.timing.json"

# The avatar presenter, cartoon with motion: corner bubble for the first and last 30 s.
AVATAR = {"ranges": [(0, 30), (-30, None)], "motion": True}
