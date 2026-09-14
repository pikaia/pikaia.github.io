"""Video config for the Marina Barrage post.

Eleven images: mostly Chris's own photography across several visits
(2018-2025), plus one Commons shot of the Causeway water pipelines for
the historical section.

  HERO           - crest gates + pump housings, daytime close-up
  CAUSEWAY       - the Causeway's water pipelines at sunset (Commons)
  SUNSET         - Flyer/skyline reflected in the reservoir at sunset
  DUSK_VISITOR   - visitor centre + rooftop lawn crowd, dusk
  ROOFTOP        - crowd on the rooftop lawn, sail structure, daytime
  DOCK           - visitor centre signage + boat dock, daytime
  WALKWAY        - joggers/cyclists on the crest walkway (portrait)
  PANORAMA       - crest panorama: reservoir/skyline one side, open sea
                   the other, in a single frame (very wide source)
  MORNING_PANO   - wide morning panorama from the crest
  DUSK_PANO      - wide dusk panorama from the crest

Most sources are normal landscape photos and use cover; WALKWAY is
portrait and uses letterbox. The three panorama sources (PANORAMA,
MORNING_PANO, DUSK_PANO) are far wider than the 16:9 frame, so instead
of a static cover crop (which would lose most of the image) they get a
slow pan sweep across the frame at fixed zoom - see docs/production-
pipeline.md §3 for the standard letterbox-vs-cover reasoning; this is
the same idea applied to an extreme-aspect source instead.

41 slides, 486.050s.
"""

_U = "https://upload.wikimedia.org/wikipedia/commons"

IMAGES = {
    "HERO": "/assets/images/marina-barrage-crest-gates.jpg",
    "CAUSEWAY": f"{_U}/6/6d/Causeway_pipeline.jpg",
    "SUNSET": "/assets/images/marina-barrage-sunset-reflection.jpg",
    "DUSK_VISITOR": "/assets/images/marina-barrage-dusk-visitor-centre.jpg",
    "ROOFTOP": "/assets/images/marina-barrage-rooftop-lawn.jpg",
    "DOCK": "/assets/images/marina-barrage-visitor-centre-dock.jpg",
    "WALKWAY": "/assets/images/marina-barrage-crest-walkway.jpg",
    "PANORAMA": "/assets/images/marina-barrage-panorama-both-sides.jpg",
    "MORNING_PANO": "/assets/images/marina-barrage-morning-panorama.jpg",
    "DUSK_PANO": "/assets/images/marina-barrage-dusk-panorama.jpg",
    "NIGHT": "/assets/images/marina-barrage-night.jpg",
}

_CVZ = {"type": "cover", "zoom": [1.0, 1.06, 1.12], "pan": [(0.5, 0.5)] * 3, "ease": "ease-in-out"}
_CVZO = {"type": "cover", "zoom": [1.12, 1.06, 1.0], "pan": [(0.5, 0.5)] * 3, "ease": "ease-out"}
_LTB = {"type": "letterbox", "zoom": [1.0, 1.04, 1.08], "pan": [(0.5, 0.5)] * 3, "ease": "ease-in-out"}
_LTBO = {"type": "letterbox", "zoom": [1.08, 1.04, 1.0], "pan": [(0.5, 0.5)] * 3, "ease": "ease-out"}
# Slow pan sweep at fixed zoom, for sources much wider than the 16:9 frame.
_PANL2R = {"type": "cover", "zoom": [1.15, 1.15, 1.15], "pan": [(0.08, 0.5), (0.5, 0.5), (0.92, 0.5)], "ease": "ease-in-out"}
_PANR2L = {"type": "cover", "zoom": [1.15, 1.15, 1.15], "pan": [(0.92, 0.5), (0.5, 0.5), (0.08, 0.5)], "ease": "ease-in-out"}

SLIDES = [
    {"img": "HERO", **_CVZ},          # 0  s0   title
    {"img": "HERO", **_CVZO},         # 1  s1   350m dam, nine gates, seven pumps
    {"img": "PANORAMA", **_PANL2R},   # 2  s2   finished 2008, 15th reservoir, largest
    {"img": "HERO", **_CVZ},          # 3  s3   nine 30m gates, 70 tonnes
    {"img": "HERO", **_CVZO},         # 4  s4   seven pumps, 280 cubic metres/sec
    {"img": "DOCK", **_CVZ},          # 5  s5   gates stay shut, level constant
    {"img": "WALKWAY", **_LTB},       # 6  s6   rains hard low tide, gates open
    {"img": "WALKWAY", **_LTBO},      # 7  s7   rains hard high tide, pumps take over
    {"img": "DUSK_VISITOR", **_CVZ},  # 8  s8   flood relief, Chinatown/Jalan Besar/Geylang
    {"img": "HERO", **_CVZ},          # 9  s9   dam, floodgate, pumping station
    {"img": "CAUSEWAY", **_CVZ},      # 10 s10  fresh water crossed a border
    {"img": "CAUSEWAY", **_CVZO},     # 11 s11  1942 invasion, pipeline demolished
    {"img": "CAUSEWAY", **_CVZ},      # 12 s12  Tebrau/Scudai and Johor River agreements
    {"img": "CAUSEWAY", **_CVZO},     # 13 s13  1961 agreement expired 2011
    {"img": "CAUSEWAY", **_CVZ},      # 14 s14  1962 agreement runs to 2061
    {"img": "SUNSET", **_CVZO},       # 15 s15  dependency not just engineering
    {"img": "SUNSET", **_CVZ},        # 16 s16  1965, Tunku's threat
    {"img": "DUSK_PANO", **_PANR2L},  # 17 s17  threat never carried out, LKY's reaction
    {"img": "DUSK_PANO", **_PANL2R},  # 18 s18  water security became sovereignty
    {"img": "HERO", **_CVZ},          # 19 s19  LKY conceived the barrage, 1987
    {"img": "DOCK", **_CVZO},         # 20 s20  "bend at the knees for water survival"
    {"img": "MORNING_PANO", **_PANL2R}, # 21 s21 Four National Taps strategy
    {"img": "MORNING_PANO", **_PANR2L}, # 22 s22 each tap expanded or shrunk
    {"img": "PANORAMA", **_PANL2R},   # 23 s23  damming off the Kallang Basin
    {"img": "PANORAMA", **_PANR2L},   # 24 s24  Punggol/Serangoon, a sixth of the land
    {"img": "HERO", **_CVZ},          # 25 s25  construction 2005-2008, S$226m
    {"img": "HERO", **_CVZO},         # 26 s26  gates closed, Marina Reservoir 240ha
    {"img": "DUSK_VISITOR", **_CVZ},  # 27 s27  dragon boats, kayaking, NDP fireworks
    {"img": "DUSK_VISITOR", **_CVZO}, # 28 s28  none of that was the reason it was built
    {"img": "ROOFTOP", **_CVZ},       # 29 s29  ask most Singaporeans, rooftop lawn
    {"img": "ROOFTOP", **_CVZO},      # 30 s30  landscaped over the pumping station
    {"img": "WALKWAY", **_LTB},       # 31 s31  enjoying exactly what they think
    {"img": "SUNSET", **_CVZ},        # 32 s32  I remember the first time I saw it
    {"img": "SUNSET", **_CVZO},       # 33 s33  pride in the accomplishment
    {"img": "MORNING_PANO", **_PANR2L}, # 34 s34 not a small thing to feel
    {"img": "NIGHT", **_CVZ},         # 35 s35  one of the most beautiful spots after dark
    {"img": "NIGHT", **_CVZO},        # 36 s36  gates light up, reservoir still and black
    {"img": "NIGHT", **_CVZ},         # 37 s37  been back a few times since
    {"img": "DUSK_PANO", **_PANR2L},  # 38 s38  why it matters today
    {"img": "HERO", **_CVZ},          # 39 s39  anxiety stopped being purely defensive
    {"img": "NIGHT", **_CVZO},        # 40 s40  closing
]

SCHEDULE = [
    (0.000, 0), (5.550, 1), (17.200, 2), (32.050, 3), (38.750, 4),
    (47.025, 5), (53.025, 6), (60.750, 7), (69.425, 8), (83.200, 9),
    (91.925, 10), (99.425, 11), (119.400, 12), (145.475, 13), (151.950, 14),
    (156.950, 15), (161.650, 16), (182.375, 17), (196.375, 18), (204.800, 19),
    (225.700, 20), (238.575, 21), (252.325, 22), (262.900, 23), (279.975, 24),
    (290.400, 25), (313.475, 26), (329.875, 27), (344.725, 28), (352.575, 29),
    (372.375, 30), (386.000, 31), (396.575, 32), (403.475, 33), (420.450, 34),
    (425.225, 35), (431.325, 36), (445.125, 37), (451.825, 38), (468.325, 39),
    (474.075, 40),
]
TOTAL_DURATION = 486.050
TIMING_JSON = "audio/marina-barrage-and-the-end-of-singapores-water-dependency-anxiety.timing.json"
