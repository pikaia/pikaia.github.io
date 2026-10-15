"""Video config for the Horsburgh Lighthouse post.

The building of the light (1847-51) is told through Thomson's own pictures,
his plan of the rock, Horsburgh's and the Admiralty's charts, and the whole
1851, 1932, 1950 and 1955 newspaper pages (always letterboxed, never cropped
to one story); the ownership case through the location map, the 1620 map, the
Peace Palace, the timeline and present-day photos of the light. Named people
get their own picture or none: Thomson's portrait (s4, s17, s73), Horsburgh's
charts for Horsburgh (s3, s13-14) and Alan Stevenson's portrait for the
lantern (s36); Lane (s46) gets the 1950 page that carries his article. The
Thomson paintings, the Daniell aquatint and Pearl's Hill view are small, so
they are letterboxed with a modest zoom.
Video-only: Alan Stevenson's portrait, a 2017 photo of the rock from the sea,
a satellite map of the strait, and Horsburgh's 1806 China Sea and Pulo Aor
charts. The timeline is letterboxed and frozen.

60 slides, 781.275s. Narration: Kokoro with the OpenVoice clone.
AVATAR: first and last 30s, cartoon with motion.
"""

_U = "https://upload.wikimedia.org/wikipedia/commons"
_C = f"{_U}/thumb"
_A = "/assets/images"

IMAGES = {
    "HERO": f"{_C}/6/62/Horsburgh_Lighthouse_by_John_T_Thomson_2.jpg/1280px-Horsburgh_Lighthouse_by_John_T_Thomson_2.jpg",
    "DANIELL": f"{_U}/f/ff/PedraBranca-Daniell-c1820.jpg",
    "MAP": f"{_C}/d/d7/Pedra_Branca_Map.svg/1280px-Pedra_Branca_Map.svg.png",
    "STONECUT": f"{_U}/3/35/ChineseKayTribeStonecutters-Singapore.jpg",
    "SFP1851": f"{_A}/singapore-free-press-1851-10-06-page-1.jpg",
    "ST1950": f"{_A}/straits-times-1950-05-24-page-6.jpg",
    "PHOTO2017": f"{_C}/6/62/LightHouse.jpg/1280px-LightHouse.jpg",
    "TIMELINE": f"{_A}/horsburgh-timeline-chart.png",
    # Gallery images:
    "SEPIA": f"{_U}/8/82/HorsburghLighthouse-JTThomson-1851-02.jpg",
    "STORM": f"{_U}/2/23/PedraBranca-TRobertson-1882.jpg",
    "GERRITSZ": f"{_U}/0/0d/Hessel_Gerritsz%2C_Map_of_Sumatra_showing_Pedra_Branca_%281620%29.jpg",
    "PLAN": f"{_C}/8/8f/Thomson%27s_topographic_map_of_Pedra_Branca.png/1280px-Thomson%27s_topographic_map_of_Pedra_Branca.png",
    "THOMSON": f"{_U}/0/03/JohnTurnbullThomson.jpg",
    "PEARLS": f"{_U}/6/6a/John_Turnbull_Thomson_-_Singapore_Town_from_Pearl%27s_Hill_Looking_East.jpg",
    "HCHART": f"{_C}/9/93/Strait_of_Malacca_Horsburgh_1806_nla.obj-373089850.jpg/1280px-Strait_of_Malacca_Horsburgh_1806_nla.obj-373089850.jpg",
    "ADM2404": f"{_C}/e/ee/Admiralty_Chart_No_2404_STRAIT_OF_SINGAPORE_Sheet_3_Surveyed_by_JT_Thomson_Esq_Governor_Survr_1846-54_RMG_F1203%2C_Published_1855.tiff/lossy-page1-1280px-Admiralty_Chart_No_2404_STRAIT_OF_SINGAPORE_Sheet_3_Surveyed_by_JT_Thomson_Esq_Governor_Survr_1846-54_RMG_F1203%2C_Published_1855.tiff.jpg",
    "UBIN": f"{_C}/3/33/Convicts_stone-quarrying_at_Pulau_Ubin%2C_Singapore_%28McNair_1899%2C_Plate_XX%29.jpg/1280px-Convicts_stone-quarrying_at_Pulau_Ubin%2C_Singapore_%28McNair_1899%2C_Plate_XX%29.jpg",
    "PEACE": f"{_C}/a/a0/International_Court_of_Justice_HQ_2006.jpg/1280px-International_Court_of_Justice_HQ_2006.jpg",
    "ST1932": f"{_A}/sunday-times-1932-03-06-page-10.jpg",
    "ST1955": f"{_A}/straits-times-1955-12-31-page-9.jpg",
    # Not in this post's captions (credited below):
    "STEVENSON": f"{_U}/8/8b/Alan_Stevenson_Lighthouse_architect.jpg",
    "SELO": f"{_U}/3/33/Pedra_Branca_and_Horsburgh_Lighthouse.jpg",
    "SAT": f"{_U}/8/8f/Pedra_Branca_island.png",
    "CHINASEA": f"{_C}/e/ed/China_Sea_Horsburgh_1806_nla.obj-373118053.jpg/1280px-China_Sea_Horsburgh_1806_nla.obj-373118053.jpg",
    "PULOAOR": f"{_C}/4/47/Pulo_Aor_Horsburgh_1806_nla.obj-373117867.jpg/1280px-Pulo_Aor_Horsburgh_1806_nla.obj-373117867.jpg",
}

# Credits for images not captioned in the post or its gallery.
CREDITS = {
    "TIMELINE": "Timeline by Lesser Known Singapore",
    "STEVENSON": "Unknown author, public domain, via Wikimedia Commons",
    "SELO": "Seloloving, CC BY-SA 4.0, via Wikimedia Commons",
    "SAT": "Public domain, via Wikimedia Commons",
    "CHINASEA": "James Horsburgh, public domain, via Wikimedia Commons",
    "PULOAOR": "James Horsburgh, public domain, via Wikimedia Commons",
}

_E = "ease-in-out"
_IN = {"type": "cover", "zoom": [1.0, 1.06, 1.12], "pan": [(0.5, 0.5)] * 3, "ease": _E}
_OUT = {"type": "cover", "zoom": [1.12, 1.06, 1.0], "pan": [(0.5, 0.5)] * 3, "ease": _E}
# Small paintings, portraits, newspaper pages, maps and charts: letterbox, modest zoom.
_PORT = {"type": "letterbox", "zoom": [1.0, 1.04, 1.08], "pan": [(0.5, 0.5)] * 3, "ease": _E}
_PORT_OUT = {"type": "letterbox", "zoom": [1.08, 1.04, 1.0], "pan": [(0.5, 0.5)] * 3, "ease": _E}
# The timeline: letterbox, frozen.
_GFX = {"type": "letterbox", "zoom": [1, 1, 1], "pan": [(0.5, 0.5)] * 3}

SLIDES = [
    {"img": "HERO", **_IN},            # 0  s0   title
    {"img": "STORM", **_PORT},         # 1  s1   24 May 1850, a steam frigate tows two ships out
    {"img": "SEPIA", **_PORT},         # 2  s2   the Governor, an admiral, the Freemasons
    {"img": "HCHART", **_PORT},        # 3  s3   a lighthouse named for James Horsburgh
    {"img": "THOMSON", **_PORT},       # 4  s4   its architect, John Turnbull Thomson
    {"img": "DANIELL", **_PORT},       # 5  s5   "white rock"; white with droppings (s6)
    {"img": "MAP", **_PORT},           # 6  s7   the eastern entrance, nine miles from Johor
    {"img": "GERRITSZ", **_PORT},      # 7  s8   Portuguese sailing directions from the 1500s
    {"img": "STORM", **_PORT_OUT},     # 8  s9   a dangerous place; the newspaper search (s10)
    {"img": "ADM2404", **_PORT},       # 9  s11  five wrecks, then eleven
    {"img": "PULOAOR", **_PORT},       # 10 s12  the Dourado and its 500,000 dollars
    {"img": "HCHART", **_PORT_OUT},    # 11 s13  Horsburgh's career
    {"img": "CHINASEA", **_PORT},      # 12 s14  his charts and sailing directions
    {"img": "TIMELINE", **_GFX},       # 13 s15  died 1836; the Horsburgh Testimonial
    {"img": "ST1932", **_PORT},        # 14 s16  $9,884 from subscriptions, Jardine Matheson
    {"img": "THOMSON", **_PORT_OUT},   # 15 s17  Thomson's 1844 plans for Peak Rock
    {"img": "SAT", **_PORT},           # 16 s18  June 1847: Pedra Branca instead
    {"img": "PLAN", **_PORT},          # 17 s19  brick test pillars, November 1847
    {"img": "STORM", **_PORT},         # 18 s20  swept away; a tower of granite throughout
    {"img": "PEARLS", **_PORT},        # 19 s21  the directors approve, December 1849
    {"img": "STONECUT", **_PORT},      # 20 s22  the granite cut on Pulau Ubin; nine dollars (s23)
    {"img": "UBIN", **_IN},            # 21 s24  the first party: convicts and blacksmiths
    {"img": "DANIELL", **_PORT_OUT},   # 22 s25  stranded on the rock; hauled off (s26)
    {"img": "SEPIA", **_PORT_OUT},     # 23 s27  everyone on the rock, April 1850
    {"img": "PEARLS", **_PORT_OUT},    # 24 s28  the contractor disappears; daily wages (s29)
    {"img": "UBIN", **_OUT},           # 25 s30  80 to 100 men at the quarries
    {"img": "CHINASEA", **_PORT_OUT},  # 26 s31  piracy; the tower as a strongpoint
    {"img": "ADM2404", **_PORT_OUT},   # 27 s32  two armed gunboats
    {"img": "PULOAOR", **_PORT_OUT},   # 28 s33  three Ubin men killed
    {"img": "ST1955", **_PORT},        # 29 s34  59 feet by October 1850; work resumes (s35)
    {"img": "STEVENSON", **_PORT},     # 30 s36  the lantern by Alan Stevenson
    {"img": "HERO", **_OUT},           # 31 s37  lit for the first time
    {"img": "ST1932", **_PORT_OUT},    # 32 s38  the cost, 23,665 dollars
    {"img": "SFP1851", **_PORT},       # 33 s39  the Notice to Mariners (s40)
    {"img": "SELO", **_PORT},          # 34 s41  revolving light, 95 feet up
    {"img": "SFP1851", **_PORT_OUT},   # 35 s42  every rock and shoal; the Metropolis (s43)
    {"img": "SEPIA", **_PORT},         # 36 s44  the last workmen leave
    {"img": "ST1950", **_PORT},        # 37 s45  life stayed hard; Lane in 1950 (s46)
    {"img": "PHOTO2017", **_IN},       # 38 s47  a crew of seven
    {"img": "STORM", **_PORT_OUT},     # 39 s48  six months of rations; no families (s49)
    {"img": "ST1950", **_PORT_OUT},    # 40 s50  kerosene and Chance Brothers clockwork
    {"img": "SELO", **_PORT_OUT},      # 41 s51  154,500 candle-power; records lost (s52)
    {"img": "PHOTO2017", **_OUT},      # 42 s53  run from Singapore after independence
    {"img": "MAP", **_PORT_OUT},       # 43 s54  the 1979 Malaysian map
    {"img": "TIMELINE", **_GFX},       # 44 s55  Singapore's note, February 1980
    {"img": "PEACE", **_IN},           # 45 s56  talks, then the Special Agreement
    {"img": "GERRITSZ", **_PORT_OUT},  # 46 s57  two readings; Malaysia's argument (s58)
    {"img": "HERO", **_IN},            # 47 s59  Singapore's argument: lawful possession
    {"img": "PEACE", **_OUT},          # 48 s60  judgment, 23 May 2008; original title (s61-62)
    {"img": "TIMELINE", **_GFX},       # 49 s63  the 1953 letter; clear in its meaning (s64)
    {"img": "PHOTO2017", **_IN},       # 50 s65  acts beyond running a lighthouse
    {"img": "MAP", **_PORT},           # 51 s66  sovereignty by 1980; the votes (s67)
    {"img": "PEACE", **_IN},           # 52 s68  back in the news in 2017 (s69)
    {"img": "TIMELINE", **_GFX},       # 53 s70  discontinued, May 2018
    {"img": "SELO", **_PORT},          # 54 s71  MND development works, July 2021
    {"img": "SAT", **_PORT_OUT},       # 55 s72  the Malaysian royal commission
    {"img": "THOMSON", **_PORT},       # 56 s73  the lighthouse Thomson built still stands
    {"img": "DANIELL", **_PORT},       # 57 s74  why it matters: a white rock, a border
    {"img": "PLAN", **_PORT_OUT},      # 58 s75  Thomson's records as evidence
    {"img": "HERO", **_OUT},           # 59 s76  the light still does its job
]

SCHEDULE = [(0.0, 0), (4.35, 1), (15.8, 2), (28.825, 3), (37.825, 4), (55.55, 5), (72.675, 6), (86.1, 7), (93.15, 8), (105.15, 9), (118.275, 10), (124.45, 11), (129.15, 12), (139.9, 13), (150.625, 14), (166.15, 15), (175.975, 16), (188.475, 17), (195.875, 18), (210.925, 19), (217.675, 20), (236.6, 21), (245.95, 22), (264.575, 23), (288.425, 24), (300.95, 25), (308.375, 26), (321.5, 27), (327.775, 28), (341.3, 29), (355.9, 30), (372.4, 31), (384.575, 32), (394.6, 33), (411.825, 34), (424.8, 35), (439.775, 36), (446.0, 37), (462.65, 38), (470.825, 39), (487.025, 40), (495.775, 41), (514.9, 42), (524.775, 43), (541.2, 44), (547.35, 45), (567.1, 46), (584.05, 47), (600.375, 48), (617.075, 49), (638.7, 50), (656.85, 51), (677.95, 52), (698.075, 53), (709.4, 54), (726.35, 55), (739.025, 56), (744.925, 57), (755.675, 58), (773.9, 59)]
TOTAL_DURATION = 781.275
TIMING_JSON = "audio/horsburgh-lighthouse-building-the-light-on-pedra-branca.timing.json"

# The avatar presenter, cartoon with motion: corner bubble for the first and last 30 s.
AVATAR = {"ranges": [(0, 30), (-30, None)], "motion": True}
