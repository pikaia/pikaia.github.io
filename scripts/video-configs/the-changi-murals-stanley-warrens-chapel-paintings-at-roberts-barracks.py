"""Video config for the Changi Murals post.

There are no free photos of the murals themselves (still in copyright; a
permission request to the Changi Chapel and Museum is pending), so the video
uses Leslie Cole's 1945 painting of a Changi ward and his cookhouse, the 1942
Selarang square, RAF Changi in 1958 and from a 1963 satellite, the Changi Air
Base (West) entrance, the museum in 2006, 2016 and 2023, its display, the
replica prison chapel, the Changi chapel rebuilt at Duntroon, the Changi map
and the murals timeline.

Named-person rule: there are no photos of Stanley Warren, the chaplains,
Ronald Searle, Wally Hammond, Charles Morris or Denis Healey, so every
sentence naming them shows a picture with no people in it: the museum, the
chapels, the air base entrance, the satellite image, the map or the timeline.

The map is letterboxed; the timeline is shown fixed.

35 slides, 499.175s. Narration: Kokoro with the OpenVoice clone.
AVATAR: first and last 30s, cartoon with motion.
"""

IMAGES = {
    "MUS06": "https://upload.wikimedia.org/wikipedia/commons/6/69/Changi_Museum.jpg",
    "REPLICA": "https://upload.wikimedia.org/wikipedia/commons/thumb/1/15/POW_chapel_at_Changi_Prison.jpg/1280px-POW_chapel_at_Changi_Prison.jpg",
    "MUS23": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/d9/Changi_chapel_museum.jpg/1280px-Changi_chapel_museum.jpg",
    "ENTR": "https://upload.wikimedia.org/wikipedia/commons/thumb/c/cf/Changi_Air_Base_West_entrance.JPG/1280px-Changi_Air_Base_West_entrance.JPG",
    "AWM": "https://upload.wikimedia.org/wikipedia/commons/e/e3/Australian_War_Memorial_132935.JPG",
    "COLE": "https://upload.wikimedia.org/wikipedia/commons/thumb/a/a9/Orderly_on_His_Rounds_in_X_Ward%2C_Changi_Gaol%2C_Singapore%2C_With_Pow%27s_Suffering_from_Starvation_and_Beri-beri_Art.IWMARTLD5618.jpg/1280px-Orderly_on_His_Rounds_in_X_Ward%2C_Changi_Gaol%2C_Singapore%2C_With_Pow%27s_Suffering_from_Starvation_and_Beri-beri_Art.IWMARTLD5618.jpg",
    "MAP": "/assets/images/changi-murals-map.png",
    "DUNTROON": "https://upload.wikimedia.org/wikipedia/commons/thumb/2/2d/Changi_Chapel_March_2013_2.jpg/1280px-Changi_Chapel_March_2013_2.jpg",
    "TL": "/assets/images/changi-murals-timeline-chart.png",
    "MUS16": "https://upload.wikimedia.org/wikipedia/commons/thumb/c/cc/Changi_Museum_gates.jpg/1280px-Changi_Museum_gates.jpg",
    "DISPLAY": "https://upload.wikimedia.org/wikipedia/commons/1/1f/Changi_Museum_Display.jpg",
    "COOK": "https://upload.wikimedia.org/wikipedia/commons/thumb/0/06/Singapore-_the_cookhouse%2C_Changi_Gaol._British_Pow%27s_prepare_their_main_meal_of_rice._Art.IWMARTLD5825.jpg/1280px-Singapore-_the_cookhouse%2C_Changi_Gaol._British_Pow%27s_prepare_their_main_meal_of_rice._Art.IWMARTLD5825.jpg",
    "CORONA": "https://upload.wikimedia.org/wikipedia/commons/0/0d/Satellite_image_of_RAF_Changi%2C_Singapore_%28Corona%2C_KH-4%2C_mission_9053%29_-_19630401.jpg",
    "RAF58": "https://upload.wikimedia.org/wikipedia/commons/0/06/Changi_Air_Base_1958.jpg",
}

# The timeline PNG is the only image not captioned in the post or its gallery.
CREDITS = {
    "TL": "Timeline by Lesser Known Singapore, from Wikipedia, Roots.gov.sg, the RAF Changi Association and The Straits Times",
}

# The channel's 2x2 thumbnail grid, 1942 to today: Selarang square in
# September 1942, Leslie Cole's 1945 Changi ward, RAF Changi in 1958, and the
# replica prison chapel at the museum.
THUMBNAIL = [
    {"img": "AWM", "pan": (0.5, 0.5)},
    {"img": "COLE", "pan": (0.5, 0.5)},
    {"img": "RAF58", "pan": (0.5, 0.45)},
    {"img": "REPLICA", "pan": (0.5, 0.5)},
]

_E = "ease-in-out"
_IN = {"type": "cover", "zoom": [1.0, 1.06, 1.12], "pan": [(0.5, 0.5)] * 3, "ease": _E}
_OUT = {"type": "cover", "zoom": [1.12, 1.06, 1.0], "pan": [(0.5, 0.5)] * 3, "ease": _E}
# The map: letterbox, modest zoom.
_PORT = {"type": "letterbox", "zoom": [1.0, 1.04, 1.08], "pan": [(0.5, 0.5)] * 3, "ease": _E}
_PORT_OUT = {"type": "letterbox", "zoom": [1.08, 1.04, 1.0], "pan": [(0.5, 0.5)] * 3, "ease": _E}
# The timeline: letterboxed and still, so its labels stay readable.
_FIX = {"type": "letterbox", "zoom": [1.0, 1.0, 1.0], "pan": [(0.5, 0.5)] * 3, "ease": "linear"}

SLIDES = [
    {"img": "MUS06", **_IN},          # 0  s0 title (names Warren: no people)
    {"img": "DUNTROON", **_IN},       # 1  s1 Warren begins painting a chapel; so ill (no people, s1-2)
    {"img": "MUS23", **_IN},          # 2  s3 the murals vanish; Warren goes home (no people)
    {"img": "ENTR", **_IN},           # 3  s4 inside an air force camp
    {"img": "AWM", **_IN},            # 4  s5 the prisoners marched to Changi
    {"img": "COLE", **_IN},           # 5  s6 Roberts Barracks becomes a hospital
    {"img": "MAP", **_PORT},          # 6  s7 Warren's regiment; Block 151 (no people, s7-8)
    {"img": "DISPLAY", **_IN},        # 7  s9 the chapel of St Luke; Warren had painted before (no people, s9-10)
    {"img": "MUS16", **_IN},          # 8  s11 Bukit Batok; Chambers and Payne; the choir (no people, s11-13)
    {"img": "AWM", **_OUT},           # 9  s14 the Selarang incident (s14-15)
    {"img": "TL", **_FIX},            # 10 s16 Warren begins; a colonel steps in (no people, s16-17)
    {"img": "MUS06", **_OUT},         # 11 s18 five murals (no people, s18-19)
    {"img": "COLE", **_OUT},          # 12 s20 the Nativity by Christmas 1942
    {"img": "COOK", **_IN},           # 13 s21 fellow prisoners find him paint
    {"img": "DUNTROON", **_OUT},      # 14 s22 broad strokes; a gift to God (no people, s22-23)
    {"img": "CORONA", **_IN},         # 15 s24 a store for the airfield; the doorway (s24-25)
    {"img": "ENTR", **_OUT},          # 16 s26 Kranji; Warren goes home (no people, s26-27)
    {"img": "RAF58", **_IN},          # 17 s28 RAF Changi; the airmen (s28-29)
    {"img": "CORONA", **_OUT},        # 18 s30 accounts differ (s30-31)
    {"img": "MUS23", **_OUT},         # 19 s32 the Sunday Times appeal
    {"img": "DISPLAY", **_OUT},       # 20 s33 Ronald Searle; his wife (no people, s33-34)
    {"img": "MAP", **_PORT_OUT},      # 21 s35 the book; the Daily Mirror finds Warren (no people, s35-36)
    {"img": "MUS16", **_OUT},         # 22 s37 four murals; the RAF asks Warren (no people, s37-38)
    {"img": "TL", **_FIX},            # 23 s39 three trips; a man with a mission (no people, s39-40)
    {"img": "MUS06", **_IN},          # 24 s41 1982, the SAF Boys' School (no people)
    {"img": "DUNTROON", **_IN},       # 25 s42 St Luke never restored; Wally Hammond (no people, s42-43)
    {"img": "MUS23", **_IN},          # 26 s44 the small picture (no people)
    {"img": "ENTR", **_IN},           # 27 s45 Warren dies, 1992 (no people)
    {"img": "TL", **_FIX},            # 28 s46 Charles Morris, Denis Healey; MINDEF 1969 (no people)
    {"img": "CORONA", **_IN},         # 29 s47 historic site; the camp is restricted (s47-48)
    {"img": "REPLICA", **_IN},        # 30 s49 visitors see the replicas (two visitors in shot; no named person, s49-50)
    {"img": "MUS16", **_IN},          # 31 s51 the copy at Larkhill
    {"img": "COOK", **_OUT},          # 32 s52 where it fits: a sick prisoner
    {"img": "DISPLAY", **_IN},        # 33 s53 the man who painted them (no people)
    {"img": "MAP", **_PORT_OUT},      # 34 s54 close: the camp and the museum down the road
]

SCHEDULE = [
    (0.0, 0), (5.25, 1), (29.6, 2), (38.15, 3), (44.7, 4), (58.025, 5),
    (66.375, 6), (92.075, 7), (105.1, 8), (130.55, 9), (153.625, 10), (167.975, 11),
    (180.125, 12), (184.825, 13), (196.125, 14), (207.375, 15), (226.45, 16), (243.525, 17),
    (257.425, 18), (269.3, 19), (282.9, 20), (296.575, 21), (320.175, 22), (333.275, 23),
    (351.95, 24), (361.375, 25), (380.55, 26), (390.8, 27), (399.725, 28), (418.125, 29),
    (440.1, 30), (459.2, 31), (466.05, 32), (481.025, 33), (488.5, 34),
]
TOTAL_DURATION = 499.175
TIMING_JSON = "audio/the-changi-murals-stanley-warrens-chapel-paintings-at-roberts-barracks.timing.json"

# The avatar presenter, cartoon with motion: corner bubble for the first and last 30 s.
AVATAR = {"ranges": [(0, 30), (-30, None)], "motion": True}
