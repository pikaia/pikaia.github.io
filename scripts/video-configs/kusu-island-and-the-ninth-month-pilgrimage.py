"""Video config for the Kusu Island post.

Kusu from the air (2016 and undated), the temple in 2006, 2010, 2011 and
2023, the keramat steps in 2020, the tortoises, the wishing well, the pier,
the fertility tree, a 2024 ferry, the Straits Times front page of 18
October 1948 and the Sunday Times page of 24 October 1948, the crossing
map and the 2019-2025 visitors chart.

Named-person rule: there are no photos of Syed Abdul Rahman, William
Gibson, Cheang Hong Lim, Ishak Samsudin, Seet Seng Huat or Hoo Tiang Lai,
so their sentences show the island, the temple or the keramat with no
people. Chik bin Embee's sentence shows the 1948 page that carries his
photograph.

The newspaper pages, the map and the portrait-format keramat steps are
letterboxed; the chart is shown fixed.

42 slides, 630.4s. Narration: Kokoro with the OpenVoice clone.
AVATAR: first and last 30s, cartoon with motion.
"""

IMAGES = {
    "AERIAL": "https://upload.wikimedia.org/wikipedia/commons/thumb/1/19/Aerial_perspective_of_Kusu_Island%2C_Singapore._Shot_in_2016.jpg/1280px-Aerial_perspective_of_Kusu_Island%2C_Singapore._Shot_in_2016.jpg",
    "AERIAL2": "https://upload.wikimedia.org/wikipedia/commons/thumb/f/fb/KUSU_island_from_the_sky_-_panoramio.jpg/1280px-KUSU_island_from_the_sky_-_panoramio.jpg",
    "ST48A": "/assets/images/straits-times-1948-10-18-page-1.jpg",
    "ST48B": "/assets/images/straits-times-1948-10-24-page-4.jpg",
    "MAP": "/assets/images/kusu-island-map.png",
    "CHART": "/assets/images/kusu-pilgrimage-visitors-chart.png",
    "TEMPLE23": "https://upload.wikimedia.org/wikipedia/commons/thumb/5/58/Kusu_Island_Tua_Pek_Kong_Temple_Photo.jpg/1280px-Kusu_Island_Tua_Pek_Kong_Temple_Photo.jpg",
    "KERAMAT": "https://upload.wikimedia.org/wikipedia/commons/thumb/3/38/Keramat_Kusu%2C_Kusu_Island_%2870917%29.jpg/1280px-Keramat_Kusu%2C_Kusu_Island_%2870917%29.jpg",
    "FERRY": "https://upload.wikimedia.org/wikipedia/commons/thumb/b/bc/SP1471A_Singapore_Island_Cruise_Marina_South_Pier_to_Saint_John%27s_Island_and_Kusu_Island_17-05-2024%287%29.jpg/1280px-SP1471A_Singapore_Island_Cruise_Marina_South_Pier_to_Saint_John%27s_Island_and_Kusu_Island_17-05-2024%287%29.jpg",
    "TEMPLE06": "https://upload.wikimedia.org/wikipedia/commons/8/85/KusuIsland01.JPG",
    "SEA11": "https://upload.wikimedia.org/wikipedia/commons/thumb/8/8a/Kusu_Island%2C_Singapore_-_20110227-01.jpg/1280px-Kusu_Island%2C_Singapore_-_20110227-01.jpg",
    "BOAT11": "https://upload.wikimedia.org/wikipedia/commons/thumb/4/4c/Kusu_Island%2C_Singapore_-_20110227-03.jpg/1280px-Kusu_Island%2C_Singapore_-_20110227-03.jpg",
    "TEMPLESEA": "https://upload.wikimedia.org/wikipedia/commons/thumb/4/45/Kusu_Island_Chinese_Temple%2C_Singapore_-_20110227.jpg/1280px-Kusu_Island_Chinese_Temple%2C_Singapore_-_20110227.jpg",
    "DABOGONG": "https://upload.wikimedia.org/wikipedia/commons/thumb/9/98/Da_Bogong_Temple_Kusu_Island.JPG/1280px-Da_Bogong_Temple_Kusu_Island.JPG",
    "TORT": "https://upload.wikimedia.org/wikipedia/commons/thumb/f/f7/Marble_Tortoise_Kusu_Island.JPG/1280px-Marble_Tortoise_Kusu_Island.JPG",
    "SHELTER": "https://upload.wikimedia.org/wikipedia/commons/thumb/c/cf/Tortoise_shelter_on_Kusu_island%2CSingapore_SF0001.jpg/1280px-Tortoise_shelter_on_Kusu_island%2CSingapore_SF0001.jpg",
    "WELL": "https://upload.wikimedia.org/wikipedia/commons/thumb/9/93/Wishing_Well_Kusu_Island.JPG/1280px-Wishing_Well_Kusu_Island.JPG",
    "PIER": "https://upload.wikimedia.org/wikipedia/commons/thumb/1/11/Welcome_to_Kusu_Island_-_The_Pier_%284815257760%29.jpg/1280px-Welcome_to_Kusu_Island_-_The_Pier_%284815257760%29.jpg",
    "FERT": "https://upload.wikimedia.org/wikipedia/commons/thumb/7/75/Fertility_Tree.jpg/1280px-Fertility_Tree.jpg",
    "STAIRS": "https://upload.wikimedia.org/wikipedia/commons/thumb/a/ae/Keramat_Kusu%2C_Kusu_Island_%2824732%29.jpg/1280px-Keramat_Kusu%2C_Kusu_Island_%2824732%29.jpg",
}

# The chart PNG is the only image not captioned in the post or its gallery.
CREDITS = {
    "CHART": "Chart by Lesser Known Singapore, Singapore Land Authority figures reported by CNA",
}

# The channel's 2x2 thumbnail grid, 1948 to today: the Straits Times front
# page of 18 October 1948, the temple in 2006, the island from the air in
# 2016, and the temple in its centenary year, 2023.
THUMBNAIL = [
    {"img": "ST48A", "pan": (0.5, 0.3)},
    {"img": "TEMPLE06", "pan": (0.5, 0.5)},
    {"img": "AERIAL", "pan": (0.5, 0.5)},
    {"img": "TEMPLE23", "pan": (0.5, 0.5)},
]

_E = "ease-in-out"
_IN = {"type": "cover", "zoom": [1.0, 1.06, 1.12], "pan": [(0.5, 0.5)] * 3, "ease": _E}
_OUT = {"type": "cover", "zoom": [1.12, 1.06, 1.0], "pan": [(0.5, 0.5)] * 3, "ease": _E}
# The newspaper pages, the map and the portrait-format steps: letterbox, modest zoom.
_PORT = {"type": "letterbox", "zoom": [1.0, 1.04, 1.08], "pan": [(0.5, 0.5)] * 3, "ease": _E}
_PORT_OUT = {"type": "letterbox", "zoom": [1.08, 1.04, 1.0], "pan": [(0.5, 0.5)] * 3, "ease": _E}
# The chart: letterboxed and still, so its labels stay readable.
_FIX = {"type": "letterbox", "zoom": [1.0, 1.0, 1.0], "pan": [(0.5, 0.5)] * 3, "ease": "linear"}

SLIDES = [
    {"img": "AERIAL", **_IN},         # 0  s0 title
    {"img": "ST48A", **_PORT},        # 1  s1 5,000 cross, 17 October 1948 (s1-2)
    {"img": "KERAMAT", **_IN},        # 2  s3 the shrine on the hill
    {"img": "FERRY", **_IN},          # 3  s4 this year's season
    {"img": "ST48A", **_PORT_OUT},    # 4  s5 the front page; 60 boats (s5-6)
    {"img": "TEMPLE06", **_IN},       # 5  s7 the offerings and mementoes
    {"img": "TEMPLESEA", **_IN},      # 6  s8 temple, then Syed Abdul Rahman's shrine (no people)
    {"img": "STAIRS", **_PORT},       # 7  s9 122 steps; hawkers (s9-10)
    {"img": "MAP", **_PORT},          # 8  s11 5.6 km south
    {"img": "AERIAL2", **_IN},        # 9  s12 two mounds, the turtle's head (s12-13)
    {"img": "SEA11", **_IN},          # 10 s14 Pulau Tembakul; Signal and Peak Island (s14-15)
    {"img": "TORT", **_IN},           # 11 s16 the turtle legend
    {"img": "SEA11", **_OUT},         # 12 s17 Gibson's versions (no people, s17-19)
    {"img": "TORT", **_OUT},          # 13 s20 the two holy men; no written records (s20-21)
    {"img": "DABOGONG", **_IN},       # 14 s22 Cheang Hong Lim's 1875 letter (no people, s22-23)
    {"img": "BOAT11", **_IN},         # 15 s24 Bintang Timor, 1894
    {"img": "STAIRS", **_PORT_OUT},   # 16 s25 the 1917 and 1921 plaques
    {"img": "TEMPLE23", **_IN},       # 17 s26 the temple, 1923 (s26-27)
    {"img": "DABOGONG", **_OUT},      # 18 s28 Tua Pek Kong; Guan Yin (s28-29)
    {"img": "ST48B", **_PORT},        # 19 s30 Two Faiths Share Holy Island (s30-31)
    {"img": "TEMPLESEA", **_OUT},     # 20 s32 pork and fowl, yellow rice
    {"img": "ST48B", **_PORT_OUT},    # 21 s33 Chik bin Embee (the page carries his photo)
    {"img": "FERT", **_IN},           # 22 s34 vows; stones on a tree (s34-35)
    {"img": "WELL", **_IN},           # 23 s36 yellow cotton; no pork
    {"img": "KERAMAT", **_OUT},       # 24 s37 the keramat's fame among the Chinese
    {"img": "STAIRS", **_PORT},       # 25 s38 three people; 152 steps (s38-39)
    {"img": "BOAT11", **_OUT},        # 26 s40 hired boats; boatmen prey (s40-41)
    {"img": "MAP", **_PORT_OUT},      # 27 s42 bumboats from Clifford Pier
    {"img": "AERIAL", **_OUT},        # 28 s43 the SDC; the 1975 rock bund (s43-44)
    {"img": "AERIAL2", **_OUT},       # 29 s45 1.2 to 8.5 hectares
    {"img": "PIER", **_IN},           # 30 s46 jetty and beaches; the 1983 levy (s46-47)
    {"img": "TEMPLE06", **_OUT},      # 31 s48 60,000 in 1984; 200,000 in 1996
    {"img": "FERRY", **_OUT},         # 32 s49 the SLA; one ferry operator
    {"img": "SHELTER", **_IN},        # 33 s50 500 a day, 2021
    {"img": "KERAMAT", **_IN},        # 34 s51 the 2022 fire; Ishak Samsudin (no people, s51-52)
    {"img": "TEMPLE23", **_OUT},      # 35 s53 Seet Seng Huat (no people)
    {"img": "CHART", **_FIX},         # 36 s54 the crowds have thinned (s54-56)
    {"img": "WELL", **_OUT},          # 37 s57 fewer stalls; ageing pilgrims (s57-58)
    {"img": "SHELTER", **_OUT},       # 38 s59 Hoo Tiang Lai (no people)
    {"img": "DABOGONG", **_IN},       # 39 s60 heritage inventory; Nanyin (s60-61)
    {"img": "AERIAL2", **_IN},        # 40 s62 where it fits (s62-63)
    {"img": "AERIAL", **_OUT},        # 41 s64 close
]

SCHEDULE = [
    (0.0, 0), (3.575, 1), (25.775, 2), (33.925, 3), (42.15, 4), (58.025, 5),
    (72.875, 6), (86.35, 7), (95.025, 8), (101.05, 9), (117.225, 10), (137.775, 11),
    (150.475, 12), (175.075, 13), (194.025, 14), (214.875, 15), (229.275, 16), (237.025, 17),
    (262.45, 18), (282.35, 19), (302.55, 20), (309.05, 21), (317.075, 22), (332.025, 23),
    (346.75, 24), (357.425, 25), (379.575, 26), (391.975, 27), (403.075, 28), (420.35, 29),
    (434.175, 30), (455.75, 31), (469.225, 32), (480.7, 33), (487.3, 34), (507.6, 35),
    (513.8, 36), (540.675, 37), (558.775, 38), (568.35, 39), (590.375, 40), (617.175, 41),
]
TOTAL_DURATION = 630.4
TIMING_JSON = "audio/kusu-island-and-the-ninth-month-pilgrimage.timing.json"

# The avatar presenter, cartoon with motion: corner bubble for the first and last 30 s.
AVATAR = {"ranges": [(0, 30), (-30, None)], "motion": True}
