"""Video config for the Linggiu Reservoir post.

Four images - a genuinely thin-image topic (no photo of the Linggiu
dam/reservoir itself exists on Wikimedia Commons; confirmed by several
targeted Commons searches, see chat). HERO and MAP carry most of the
runtime; CAUSEWAY and MARINA are reused from the companion Marina
Barrage post's own sourcing, which is expected/documented behaviour
for a thin-image pool (see docs/pronunciation-fixes.md-adjacent
feedback_avoid_image_reuse_when_well_photographed.md - the exception,
not the rule, but this topic qualifies).

  HERO      - the Johor River at Kota Tinggi (Commons)
  MAP       - the hand-annotated OSM map built for this post (local)
  CAUSEWAY  - the Causeway's water pipelines at sunset (Commons, reused
              from the Marina Barrage post)
  MARINA    - Marina Barrage crest gates (local, reused from that
              post) - used specifically on the sentences that
              reference Marina Barrage/the Four Taps pivot by name

MAP uses letterbox (it's a labelled diagram, not a photo - cover would
crop the markers/labels); the rest are landscape photos and use cover.

33 slides, 417.700s.
"""

_U = "https://upload.wikimedia.org/wikipedia/commons"

IMAGES = {
    "HERO": f"{_U}/a/ac/Johor_River.jpg",
    "MAP": "/assets/images/linggiu-map.jpg",
    "CAUSEWAY": f"{_U}/6/6d/Causeway_pipeline.jpg",
    "MARINA": "/assets/images/marina-barrage-crest-gates.jpg",
}

_CVZ = {"type": "cover", "zoom": [1.0, 1.06, 1.12], "pan": [(0.5, 0.5)] * 3, "ease": "ease-in-out"}
_CVZO = {"type": "cover", "zoom": [1.12, 1.06, 1.0], "pan": [(0.5, 0.5)] * 3, "ease": "ease-out"}
_LTB = {"type": "letterbox", "zoom": [1.0, 1.04, 1.08], "pan": [(0.5, 0.5)] * 3, "ease": "ease-in-out"}
_LTBO = {"type": "letterbox", "zoom": [1.08, 1.04, 1.0], "pan": [(0.5, 0.5)] * 3, "ease": "ease-out"}

SLIDES = [
    {"img": "HERO", **_CVZ},        # 0  s0   title
    {"img": "HERO", **_CVZO},       # 1  s1   1962 treaty, 250mgd
    {"img": "HERO", **_CVZ},        # 2  s2   guarantee not enough
    {"img": "HERO", **_CVZO},       # 3  s3   Nov 1990, Singapore pays
    {"img": "MARINA", **_CVZ},      # 4  s4   this blog told part already (Marina Barrage)
    {"img": "HERO", **_CVZO},       # 5  s5   Linggiu, earlier quieter chapter
    {"img": "HERO", **_CVZ},        # 6  s6   1962 Johor River Agreement
    {"img": "HERO", **_CVZO},       # 7  s7   treaty right isn't water that's there
    {"img": "MAP", **_LTB},         # 8  s8   extraction point at Kota Tinggi
    {"img": "MAP", **_LTBO},        # 9  s9   no agreement could stop a river running low
    {"img": "HERO", **_CVZ},        # 10 s10  Singapore's answer: control the river
    {"img": "MAP", **_LTB},         # 11 s11  1989, dam across Sungai Linggiu
    {"img": "HERO", **_CVZO},       # 12 s12  EIA contested
    {"img": "HERO", **_CVZ},        # 13 s13  agreement signed 24 Nov 1990
    {"img": "HERO", **_CVZO},       # 14 s14  Muhyiddin Yassin quote
    {"img": "HERO", **_CVZ},        # 15 s15  Singapore bore full cost
    {"img": "HERO", **_CVZO},       # 16 s16  Goh Chok Tong visit
    {"img": "MAP", **_LTB},         # 17 s17  dam completed April 1993
    {"img": "HERO", **_CVZO},       # 18 s18  draw beyond the cap
    {"img": "HERO", **_CVZ},        # 19 s19  dam's real purpose was defensive
    {"img": "HERO", **_CVZO},       # 20 s20  did its job quietly for two decades
    {"img": "MAP", **_LTBO},        # 21 s21  2015 level fell steadily
    {"img": "CAUSEWAY", **_CVZ},    # 22 s22  Singapore supplies more water to Johor
    {"img": "MAP", **_LTB},         # 23 s23  April 2016 record low 36.9%
    {"img": "HERO", **_CVZO},       # 24 s24  real answer wasn't a bigger dam
    {"img": "MARINA", **_CVZO},     # 25 s25  fourth desalination plant, Marina East
    {"img": "MAP", **_LTBO},        # 26 s26  Linggiu still supplies water today
    {"img": "MAP", **_LTB},         # 27 s27  reservoir Singapore paid S$310m to build
    {"img": "MARINA", **_CVZ},      # 28 s28  why it matters: Marina Barrage/NEWater known
    {"img": "HERO", **_CVZO},       # 29 s29  almost nobody remembers Linggiu
    {"img": "CAUSEWAY", **_CVZO},   # 30 s30  Malaysia still supplies roughly half
    {"img": "MARINA", **_CVZ},      # 31 s31  PUB target ~2060
    {"img": "HERO", **_CVZO},       # 32 s32  never meant to be permanent, closing
]

SCHEDULE = [
    (0.0, 0), (6.8, 1), (20.5, 2), (24.475, 3), (41.75, 4),
    (53.15, 5), (62.35, 6), (84.025, 7), (89.575, 8), (104.875, 9),
    (110.675, 10), (114.8, 11), (134.775, 12), (148.525, 13), (159.025, 14),
    (172.85, 15), (181.575, 16), (199.7, 17), (216.7, 18), (230.65, 19),
    (242.4, 20), (249.1, 21), (259.05, 22), (275.95, 23), (297.45, 24),
    (303.525, 25), (324.975, 26), (335.05, 27), (351.225, 28), (363.7, 29),
    (378.075, 30), (383.525, 31), (402.25, 32),
]
TOTAL_DURATION = 417.700
TIMING_JSON = "audio/linggiu-reservoir-the-dam-singapore-built-inside-another-country-to-secure-its-own-water.timing.json"
