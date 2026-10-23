"""Video config for the Chek Jawa post.

From Pulau Ubin's quarries and village to the boardwalk today: the OSM
locator map (twice, for the island and for the 1992 plan), Singapore's
land-area chart (reused from the Telok Ayer post), House No. 1 in 2007
and 2015, and the shore, mangroves and boardwalk in August 2007 (a month
after the reopening) and November 2015.

Named-person rule: Joseph Lai, Tan Koh Siang, Langdon Williams, Lee Thor
Seng, Mah Bow Tan and Eric Lin have no free photographs, so their
sentences show the shore, the house and the map only, never people. The
photos with visitors in them (the mudflats, the back mangrove, the
visitor centre) go under sentences about crowds and visitors.

The map, the chart and the portrait-shaped photos are letterboxed.

42 slides, 614.775s. Narration: Kokoro with the OpenVoice clone.
AVATAR: first and last 30s, cartoon with motion.
"""

IMAGES = {
    "HERO": "https://upload.wikimedia.org/wikipedia/commons/thumb/3/36/Chek_Jawa_35%2C_Aug_07.JPG/1280px-Chek_Jawa_35%2C_Aug_07.JPG",
    "ROCKS09": "https://upload.wikimedia.org/wikipedia/commons/a/a8/Chek_Jawa%2C_Singapore_%283940295137%29.jpg",
    "CJ25": "https://upload.wikimedia.org/wikipedia/commons/thumb/5/5e/Chek_Jawa_25%2C_Aug_07.JPG/1280px-Chek_Jawa_25%2C_Aug_07.JPG",
    "CJ40": "https://upload.wikimedia.org/wikipedia/commons/thumb/3/35/Singapore_Pulau_Ubin_Chek_Jawa_40.jpg/1280px-Singapore_Pulau_Ubin_Chek_Jawa_40.jpg",
    "JETTY07": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/dd/Chek_Jawa_30%2C_Aug_07.JPG/1280px-Chek_Jawa_30%2C_Aug_07.JPG",
    "COASTBW": "https://upload.wikimedia.org/wikipedia/commons/thumb/f/f7/Chek_Jawa_15%2C_Aug_07.JPG/1280px-Chek_Jawa_15%2C_Aug_07.JPG",
    "MAP": "/assets/images/chek-jawa-map.png",
    "QUARRY": "https://upload.wikimedia.org/wikipedia/commons/thumb/8/8b/Abandoned_quarry_on_Pulau_Ubin.jpg/1280px-Abandoned_quarry_on_Pulau_Ubin.jpg",
    "KAMPONG": "https://upload.wikimedia.org/wikipedia/commons/thumb/4/45/Pulau_Ubin_kampong_house.jpg/1280px-Pulau_Ubin_kampong_house.jpg",
    "BOULD15": "https://upload.wikimedia.org/wikipedia/commons/thumb/0/0f/Singapore_Pulau_Ubin_Chek_Jawa_20.jpg/1280px-Singapore_Pulau_Ubin_Chek_Jawa_20.jpg",
    "CJ50": "https://upload.wikimedia.org/wikipedia/commons/thumb/b/b2/Singapore_Pulau_Ubin_Chek_Jawa_50.jpg/1280px-Singapore_Pulau_Ubin_Chek_Jawa_50.jpg",
    "HOUSE15": "https://upload.wikimedia.org/wikipedia/commons/thumb/8/85/Singapore_Pulau_Ubin_Chek_Jawa_23.jpg/1280px-Singapore_Pulau_Ubin_Chek_Jawa_23.jpg",
    "HOUSE07": "https://upload.wikimedia.org/wikipedia/commons/thumb/c/c0/Chek_Jawa%2C_Aug_07.JPG/1280px-Chek_Jawa%2C_Aug_07.JPG",
    "HOUSE07B": "https://upload.wikimedia.org/wikipedia/commons/thumb/b/b8/Chek_Jawa_2%2C_Aug_07.JPG/1280px-Chek_Jawa_2%2C_Aug_07.JPG",
    "CHART": "/assets/images/singapore-land-area-chart.png",
    "UBINJETTY": "https://upload.wikimedia.org/wikipedia/commons/thumb/7/7a/Pulau_Ubin_Jetty_and_Settlement.jpg/1280px-Pulau_Ubin_Jetty_and_Settlement.jpg",
    "ROOTS": "https://upload.wikimedia.org/wikipedia/commons/a/a6/Chek_Jawa_21%2C_Aug_07.JPG",
    "CJ18": "https://upload.wikimedia.org/wikipedia/commons/2/2a/Chek_Jawa_18%2C_Aug_07.JPG",
    "JETTY15": "https://upload.wikimedia.org/wikipedia/commons/thumb/5/51/Singapore_Pulau_Ubin_Chek_Jawa_01.jpg/1280px-Singapore_Pulau_Ubin_Chek_Jawa_01.jpg",
    "CJ60": "https://upload.wikimedia.org/wikipedia/commons/thumb/4/41/Singapore_Pulau_Ubin_Chek_Jawa_60.jpg/1280px-Singapore_Pulau_Ubin_Chek_Jawa_60.jpg",
    "MANG15": "https://upload.wikimedia.org/wikipedia/commons/thumb/5/55/Singapore_Pulau_Ubin_Chek_Jawa_70.jpg/1280px-Singapore_Pulau_Ubin_Chek_Jawa_70.jpg",
    "MUD": "https://upload.wikimedia.org/wikipedia/commons/thumb/f/f6/Chek_Jawa_12%2C_Aug_07.JPG/1280px-Chek_Jawa_12%2C_Aug_07.JPG",
    "CJ7": "https://upload.wikimedia.org/wikipedia/commons/9/9e/Chek_Jawa_7%2C_Aug_07.JPG",
    "LANDSCAPE": "https://upload.wikimedia.org/wikipedia/commons/thumb/1/1d/Chek_Jawa_landscape.jpg/1280px-Chek_Jawa_landscape.jpg",
    "BACKMANG": "https://upload.wikimedia.org/wikipedia/commons/thumb/6/66/Chek_Jawa_9%2C_Aug_07.JPG/1280px-Chek_Jawa_9%2C_Aug_07.JPG",
    "VCIN": "https://upload.wikimedia.org/wikipedia/commons/thumb/c/c0/Chek_Jawa_3%2C_Aug_07.JPG/1280px-Chek_Jawa_3%2C_Aug_07.JPG",
    "TOWER": "https://upload.wikimedia.org/wikipedia/commons/2/24/Chek_Jawa_5%2C_Aug_07.JPG",
    "VC09": "https://upload.wikimedia.org/wikipedia/commons/0/01/Chek_Jawa_Visitor_Centre%2C_Pulau_Ubin_%E2%80%93_Singapore_%283817430741%29.jpg",
    "BUMBOATS": "https://upload.wikimedia.org/wikipedia/commons/thumb/4/4d/SINGAPOREAN_BUMBOATS.jpg/1280px-SINGAPOREAN_BUMBOATS.jpg",
}

# Credits for images not captioned in the post or its gallery.
CREDITS = {
    "CJ25": "Sengkang, CC BY-SA 3.0, via Wikimedia Commons",
    "CJ40": "Zairon, CC BY-SA 4.0, via Wikimedia Commons",
    "CJ50": "Zairon, CC BY-SA 4.0, via Wikimedia Commons",
    "HOUSE07B": "Sengkang, CC BY-SA 3.0, via Wikimedia Commons",
    "CHART": "Chart by Lesser Known Singapore, figures from the Singapore Land Authority via data.gov.sg",
    "CJ18": "Sengkang, CC BY-SA 3.0, via Wikimedia Commons",
    "CJ60": "Zairon, CC BY-SA 4.0, via Wikimedia Commons",
    "CJ7": "Sengkang, CC BY-SA 3.0, via Wikimedia Commons",
    "LANDSCAPE": "Alyarish, CC BY-SA 4.0, via Wikimedia Commons",
}

# The channel's 2x2 thumbnail grid, 1930s to today: House No. 1 (built in
# the 1930s), visitors above the mudflats and the boardwalk in August 2007,
# and the boulders off the point in 2015.
THUMBNAIL = [
    {"img": "HOUSE07", "pan": (0.5, 0.45)},
    {"img": "MUD", "pan": (0.5, 0.5)},
    {"img": "HERO", "pan": (0.5, 0.5)},
    {"img": "BOULD15", "pan": (0.5, 0.5)},
]

_E = "ease-in-out"
_IN = {"type": "cover", "zoom": [1.0, 1.06, 1.12], "pan": [(0.5, 0.5)] * 3, "ease": _E}
_OUT = {"type": "cover", "zoom": [1.12, 1.06, 1.0], "pan": [(0.5, 0.5)] * 3, "ease": _E}
# The map, the chart and portrait-shaped photos: letterbox, modest zoom.
_PORT = {"type": "letterbox", "zoom": [1.0, 1.04, 1.08], "pan": [(0.5, 0.5)] * 3, "ease": _E}
_PORT_OUT = {"type": "letterbox", "zoom": [1.08, 1.04, 1.0], "pan": [(0.5, 0.5)] * 3, "ease": _E}

SLIDES = [
    {"img": "HERO", **_IN},               # 0  s0  title
    {"img": "ROCKS09", **_IN},            # 1  s1  Lai at Chek Jawa, December 2000 (no people)
    {"img": "CJ25", **_IN},               # 2  s2  the flats alive
    {"img": "CJ40", **_IN},               # 3  s3  due to be reclaimed
    {"img": "JETTY07", **_IN},            # 4  s4  a year of visitors; the deferral
    {"img": "COASTBW", **_IN},            # 5  s5  still there today
    {"img": "MAP", **_PORT},              # 6  s6  Pulau Ubin off Changi
    {"img": "QUARRY", **_IN},             # 7  s7  squared stone; the quarries
    {"img": "KAMPONG", **_IN},            # 8  s8  2,000 residents; fewer than 200 (s8-9)
    {"img": "BOULD15", **_IN},            # 9  s10 the point; six habitats (s10-11)
    {"img": "CJ50", **_IN},               # 10 s12 Tan Koh Siang (no people)
    {"img": "HOUSE15", **_IN},            # 11 s13 House No. 1; Langdon Williams (s13-14)
    {"img": "HOUSE07", **_IN},            # 12 s15 a weekend home
    {"img": "HOUSE07B", **_IN},           # 13 s16 Lee Thor Seng; acquired in the 1990s
    {"img": "CHART", **_PORT},            # 14 s17 land area 1960-2025 (s17-18)
    {"img": "UBINJETTY", **_IN},          # 15 s19 the Telok Ayer post
    {"img": "MAP", **_PORT_OUT},          # 16 s20 the 1992 plan; reserve land (s20-22)
    {"img": "ROOTS", **_PORT},            # 17 s23 the salvage survey (s23-24)
    {"img": "CJ18", **_PORT},             # 18 s25 the URA forum; letters (s25-27)
    {"img": "JETTY15", **_PORT},          # 19 s28 the URA's reply (s28-29)
    {"img": "CJ60", **_IN},               # 20 s30 seagrass and dugongs
    {"img": "MANG15", **_IN},             # 21 s31 the volunteers carry on (s31-32)
    {"img": "MUD", **_IN},                # 22 s33 more than a thousand turn up
    {"img": "CJ7", **_PORT},              # 23 s34 Remember Chek Jawa
    {"img": "ROCKS09", **_OUT},           # 24 s35 field data and reports
    {"img": "LANDSCAPE", **_PORT},        # 25 s36 Mah Bow Tan meets the groups (s36-37)
    {"img": "BOULD15", **_OUT},           # 26 s38 the press release (s38-39)
    {"img": "CJ25", **_OUT},              # 27 s40 consultations; "no urgent need" (s40-41)
    {"img": "CJ40", **_OUT},              # 28 s42 14 January 2002 (s42-43)
    {"img": "JETTY07", **_OUT},           # 29 s44 not cost-effective; the committee (s44-45)
    {"img": "BACKMANG", **_IN},           # 30 s46 the crowds; the rules (s46-47)
    {"img": "VCIN", **_IN},               # 31 s48 20,000 on the guided walks
    {"img": "ROOTS", **_PORT_OUT},        # 32 s49 the floods; tours suspended (s49-51)
    {"img": "TOWER", **_PORT},            # 33 s52 the 2007 reopening
    {"img": "VC09", **_IN},               # 34 s53 the heritage award
    {"img": "COASTBW", **_OUT},           # 35 s54 no guide needed
    {"img": "JETTY15", **_PORT_OUT},      # 36 s55 the 2010 oil spill
    {"img": "MANG15", **_OUT},            # 37 s56 Parks and Trees Act; not a reserve (s56-57)
    {"img": "UBINJETTY", **_OUT},         # 38 s58 the 2013 land-use plans
    {"img": "BUMBOATS", **_IN},           # 39 s59 a bumboat from Changi
    {"img": "HOUSE07", **_OUT},           # 40 s60 where it fits (s60-61)
    {"img": "HERO", **_OUT},              # 41 s62 close
]

SCHEDULE = [
    (0.0, 0), (3.65, 1), (15.525, 2), (22.55, 3), (27.075, 4), (44.75, 5),
    (53.75, 6), (64.475, 7), (73.575, 8), (85.175, 9), (106.0, 10), (117.425, 11),
    (138.35, 12), (143.275, 13), (150.825, 14), (176.325, 15), (183.7, 16), (212.575, 17),
    (235.175, 18), (264.85, 19), (282.9, 20), (301.425, 21), (314.15, 22), (319.975, 23),
    (326.85, 24), (339.3, 25), (355.3, 26), (375.6, 27), (398.625, 28), (411.8, 29),
    (437.7, 30), (451.6, 31), (458.55, 32), (479.85, 33), (503.675, 34), (510.15, 35),
    (514.525, 36), (529.675, 37), (551.7, 38), (565.9, 39), (576.6, 40), (603.975, 41),
]
TOTAL_DURATION = 614.775
TIMING_JSON = "audio/chek-jawa-the-shore-that-was-saved-by-a-survey.timing.json"

# The avatar presenter, cartoon with motion: corner bubble for the first and last 30 s.
AVATAR = {"ranges": [(0, 30), (-30, None)], "motion": True}
