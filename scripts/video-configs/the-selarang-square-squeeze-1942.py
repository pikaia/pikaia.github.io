"""Video config for the Selarang Square post.

George Aspinall's secret photographs of the Selarang square in September
1942 (Australian War Memorial, public domain, 640px copies), Changi in 1941
and 1945, Changi Gaol in 1936 and today, the Straits Times trial page of
27 February 1946, the Changi OSM map, Kranji, and the Changi Chapel and
Museum today.

Named-person rule: Fukuye, the four escapees, Hubert, Holmes, Galleghan and
Frith have no photographs here, so their sentences show the map, the
newspaper page, empty barracks, the prison wall, Kranji's headstones or
distant crowds in the square. Aspinall's sentences show his own portrait
(left, with Harry Russell).

The 640px AWM photos, the map, the newspaper page and the narrow or small
photos are letterboxed with a modest zoom.

38 slides, 508.35s. Narration: Kokoro with the OpenVoice clone.
AVATAR: first and last 30s, cartoon with motion.
"""

IMAGES = {
    "HERO": "/assets/images/awm-132937-selarang-square-1942.jpg",
    "SQ03": "/assets/images/awm-132933-selarang-square-1942.jpg",
    "P160": "/assets/images/awm-p02569-160-selarang.jpg",
    "P154": "/assets/images/awm-p02569-154-selarang.jpg",
    "C1941": "https://upload.wikimedia.org/wikipedia/commons/thumb/4/49/Changi_1941_ii.jpg/1280px-Changi_1941_ii.jpg",
    "P169": "/assets/images/awm-p02569-169-selarang.jpg",
    "P153": "/assets/images/awm-p02569-153-selarang.jpg",
    "PRISON36": "https://upload.wikimedia.org/wikipedia/commons/thumb/3/31/Changi_Prison_in_1936.jpg/1280px-Changi_Prison_in_1936.jpg",
    "MAP": "/assets/images/selarang-changi-map.png",
    "ST46": "/assets/images/straits-times-1946-02-27-page-3.jpg",
    "P158": "/assets/images/awm-p02569-158-selarang.jpg",
    "P161": "/assets/images/awm-p02569-161-selarang.jpg",
    "P164": "/assets/images/awm-p02569-164-selarang.jpg",
    "P166": "/assets/images/awm-p02569-166-selarang.jpg",
    "P162": "/assets/images/awm-p02569-162-selarang.jpg",
    "P159": "/assets/images/awm-p02569-159-selarang.jpg",
    "KRANJI": "https://upload.wikimedia.org/wikipedia/commons/8/87/Kranji_War_Memorial_-_Tombs.jpg",
    "P165": "/assets/images/awm-p02569-165-selarang.jpg",
    "P167": "/assets/images/awm-p02569-167-selarang.jpg",
    "P168": "/assets/images/awm-p02569-168-selarang.jpg",
    "PRISONWALL": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/d5/Changi_Prison_Gate_Wall%2C_October_2025.jpg/1280px-Changi_Prison_Gate_Wall%2C_October_2025.jpg",
    "AWM935": "https://upload.wikimedia.org/wikipedia/commons/e/e3/Australian_War_Memorial_132935.JPG",
    "P199": "/assets/images/awm-p02569-199-selarang.jpg",
    "GATE": "https://upload.wikimedia.org/wikipedia/commons/thumb/c/cc/Changi_Museum_gates.jpg/1280px-Changi_Museum_gates.jpg",
    "CMI": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/d9/Changi_chapel_museum.jpg/1280px-Changi_chapel_museum.jpg",
    "REL45": "https://upload.wikimedia.org/wikipedia/commons/c/c7/The_Release_of_Allied_Prisoners_of_War_From_Changi_Prison%2C_1945_CF722.jpg",
}

# Credits for images not captioned in the post or its gallery.
CREDITS = {
    "P159": "George Aspinall, Australian War Memorial P02569.159, public domain",
    "P162": "George Aspinall, Australian War Memorial P02569.162, public domain",
    "P165": "George Aspinall, Australian War Memorial P02569.165, public domain",
    "P167": "George Aspinall, Australian War Memorial P02569.167, public domain",
    "P169": "George Aspinall, Australian War Memorial P02569.169, public domain",
    "PRISONWALL": "GoAheadFan95, CC BY-SA 4.0, via Wikimedia Commons",
    "CMI": "Liaw Xin Ru, CC BY-SA 4.0, via Wikimedia Commons",
}

# The channel's 2x2 thumbnail grid, 1941 to today: the Changi barracks in
# 1941, the Selarang square on 2 September 1942, release from Changi in
# 1945, and the gates of the Changi Chapel and Museum.
THUMBNAIL = [
    {"img": "C1941", "pan": (0.5, 0.5)},
    {"img": "HERO", "pan": (0.5, 0.5)},
    {"img": "REL45", "pan": (0.5, 0.4)},
    {"img": "GATE", "pan": (0.5, 0.5)},
]

_E = "ease-in-out"
_IN = {"type": "cover", "zoom": [1.0, 1.06, 1.12], "pan": [(0.5, 0.5)] * 3, "ease": _E}
_OUT = {"type": "cover", "zoom": [1.12, 1.06, 1.0], "pan": [(0.5, 0.5)] * 3, "ease": _E}
# The 640px AWM photos, the map, the newspaper page and the small photos: letterbox, modest zoom.
_PORT = {"type": "letterbox", "zoom": [1.0, 1.04, 1.08], "pan": [(0.5, 0.5)] * 3, "ease": _E}
_PORT_OUT = {"type": "letterbox", "zoom": [1.08, 1.04, 1.0], "pan": [(0.5, 0.5)] * 3, "ease": _E}
_OUT_LB = {"type": "letterbox", "zoom": [1.06, 1.03, 1.0], "pan": [(0.5, 0.5)] * 3, "ease": _E}

SLIDES = [
    {"img": "HERO", **_PORT},           # 0  s0  title
    {"img": "SQ03", **_PORT},           # 1  s1  15,000-17,000 marched in
    {"img": "P160", **_PORT},           # 2  s2  built for one battalion; four days (s2-3)
    {"img": "P154", **_PORT},           # 3  s4  George Aspinall (him, left)
    {"img": "C1941", **_IN},            # 4  s5  the Changi garrison
    {"img": "P169", **_PORT},           # 5  s6  Selarang Barracks
    {"img": "P153", **_PORT},           # 6  s7  the Gordon Highlanders
    {"img": "C1941", **_OUT},           # 7  s8  surrender; marched to Changi
    {"img": "PRISON36", **_PORT},       # 8  s9  organise themselves; working parties (s9-10)
    {"img": "MAP", **_PORT},            # 9  s11 Fukuye arrives (map only)
    {"img": "P169", **_PORT_OUT},       # 10 s12 the four escapees (empty barracks)
    {"img": "ST46", **_PORT},           # 11 s13 Fukuye's pledge (page only)
    {"img": "P158", **_PORT},           # 12 s14 refused; the duty to escape (s14-15)
    {"img": "MAP", **_PORT_OUT},        # 13 s16 Fukuye's order (map only)
    {"img": "HERO", **_PORT_OUT},       # 14 s17 moving in; Hubert's column (s17-18)
    {"img": "P161", **_PORT},           # 15 s19 blocks full; 1,200 a block (s19-20)
    {"img": "P164", **_PORT},           # 16 s21 water; three taps (s21-22)
    {"img": "P166", **_PORT},           # 17 s23 the latrines
    {"img": "P162", **_PORT},           # 18 s24 firewood; dysentery (s24-25)
    {"img": "P154", **_PORT_OUT},       # 19 s26 Aspinall; the hidden camera (s26-27)
    {"img": "P159", **_PORT},           # 20 s28 from the upper floors
    {"img": "MAP", **_PORT},            # 21 s29 the executions; Holmes and Galleghan (map only, s29-30)
    {"img": "KRANJI", **_PORT},         # 22 s31 Frith; buried at Kranji (no people, s31-32)
    {"img": "P165", **_PORT},           # 23 s33 sick list; Holmes orders signing (s33-34)
    {"img": "P167", **_PORT},           # 24 s35 under duress; Ned Kelly
    {"img": "P168", **_PORT},           # 25 s36 back to the camps; the railway (s36-37)
    {"img": "ST46", **_PORT_OUT},       # 26 s38 the trial; 17,000 (page only, s38-39)
    {"img": "PRISON36", **_PORT_OUT},   # 27 s40 Fukuye's defence (no people)
    {"img": "MAP", **_PORT_OUT},        # 28 s41 sentenced; shot at Changi (map only, s41-42)
    {"img": "PRISONWALL", **_IN},       # 29 s43 negatives hidden in Changi Gaol (no people)
    {"img": "AWM935", **_PORT},         # 30 s44 the water bottle; the AWM (s44-45)
    {"img": "P199", **_PORT},           # 31 s46 after the war; ANZUK (s46-47)
    {"img": "P153", **_PORT_OUT},       # 32 s48 Selarang Camp today
    {"img": "GATE", **_IN},             # 33 s49 the Changi Chapel and Museum
    {"img": "CMI", **_IN},              # 34 s50 revamped, 2021; the hidden camera
    {"img": "REL45", **_PORT},          # 35 s51 where it fits
    {"img": "SQ03", **_PORT_OUT},       # 36 s52 rules as soldiers
    {"img": "HERO", **_OUT_LB},         # 37 s53 close
]

SCHEDULE = [
    (0.0, 0), (3.7, 1), (21.35, 2), (37.15, 3), (48.925, 4), (61.725, 5),
    (68.25, 6), (83.45, 7), (97.075, 8), (114.125, 9), (122.975, 10), (135.25, 11),
    (144.0, 12), (157.875, 13), (166.7, 14), (178.925, 15), (193.15, 16), (205.0, 17),
    (218.2, 18), (231.7, 19), (252.35, 20), (259.5, 21), (281.125, 22), (292.55, 23),
    (310.8, 24), (318.975, 25), (332.775, 26), (359.075, 27), (373.175, 28), (388.875, 29),
    (405.8, 30), (419.775, 31), (442.7, 32), (449.125, 33), (459.15, 34), (470.1, 35),
    (486.3, 36), (497.65, 37),
]
TOTAL_DURATION = 508.35
TIMING_JSON = "audio/the-selarang-square-squeeze-1942.timing.json"

# The avatar presenter, cartoon with motion: corner bubble for the first and last 30 s.
AVATAR = {"ranges": [(0, 30), (-30, None)], "motion": True}
