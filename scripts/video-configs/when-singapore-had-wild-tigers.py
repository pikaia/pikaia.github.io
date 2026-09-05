"""Video config for the wild-tigers post's Watch widget / main video.

The historical half of the narration (roughly the first five minutes -
the menace, the bounty, the 1928 and 1930 hunts) has no tiger
photography available: the two 1930 Choa Chu Kang photos are held by
NLB and pending a permission reply, and nothing else clears. So that
stretch leans on three graphics that carry it honestly - the OSM
locations map (MAP), the dated-event timeline (TIMELINE), and the one
period photograph we have, a c.1900 gambier-and-pepper plantation shed
(GAMBIER) - cycled with varied push/pull framing. If the NLB photos
come through later this section can be re-cut around them.

The present-day half is well covered: the CBD otter road sign
(OTTERSIGN, portrait -> letterbox), a wild otter family, an Oriental
Pied Hornbill, wild boars on Pulau Ubin, and the Eco-Link@BKE bridge.

Graphics (MAP, TIMELINE) are letterbox and near-frozen, per
docs/production-pipeline.md ss3 - cover would crop their labels.
Everything else is centred zoom, no horizontal pan (the pan read JERKY
on the pineapple-kings post's large scans).

29 slides, 537.95s.
"""

_C = "https://upload.wikimedia.org/wikipedia/commons"

IMAGES = {
    "GAMBIER": f"{_C}/0/0d/ChineseGambierSingapore.jpg",                                    # 624x486
    "OTTERSIGN": f"{_C}/5/52/%27Watch_out_for_otters_crossing%27_sign_on_Robertson_Quay_near_Kim_Seng_Park%2C_Singapore.jpg",  # 3072x4080 (portrait)
    "OTTERFAMILY": f"{_C}/b/bf/Smooth-coated_otters_%28Lutrogale_perspicillata%29%2C_Sungei_Serangoon%2C_Singapore_-_20130518.jpg",  # landscape
    "HORNBILL": f"{_C}/2/2c/Anthracoceros_albirostris_%28Oriential_Pied_Hornbill%29.jpg",   # 4238x2848
    "BOAR": f"{_C}/a/ab/Singapore_Wildschweine_auf_Pulau_Ubin_1.jpg",                       # 4592x2576
    "ECOLINK": f"{_C}/d/d8/Eco-link_%40_BKE_%2823337731653%29.jpg",                         # 3456x2304
    "MAP": "/assets/images/when-singapore-had-wild-tigers-map.png",                         # 1600x1280, OSM-based, committed locally
    "TIMELINE": "/assets/images/when-singapore-had-wild-tigers-timeline.png",               # 1280x720, committed locally
}

CREDITS = {
    "MAP": "Map by Lesser Known Singapore; base map data © OpenStreetMap contributors",
    "TIMELINE": "Timeline by Lesser Known Singapore",
}

_LBI = {"type": "letterbox", "zoom": [1.0, 1.04, 1.08], "pan": [(0.5, 0.5)] * 3, "ease": "ease-in-out"}
_LBW = {"type": "letterbox", "zoom": [1.0, 1.05, 1.10], "pan": [(0.5, 0.5)] * 3, "ease": "ease-in-out"}
_CVZ = {"type": "cover", "zoom": [1.0, 1.06, 1.12], "pan": [(0.5, 0.5)] * 3, "ease": "ease-in-out"}
_CVZO = {"type": "cover", "zoom": [1.12, 1.06, 1.0], "pan": [(0.5, 0.5)] * 3, "ease": "ease-out"}
_MAPMOVE = {"type": "letterbox", "zoom": [1.0, 1.03, 1.05], "pan": [(0.5, 0.5)] * 3, "ease": "linear"}
_CHART = {"type": "letterbox", "zoom": [1.0, 1.0, 1.0], "pan": [(0.5, 0.5)] * 3, "ease": "linear"}
# The hornbill photo is 3:2 and the bird runs top (raised beak) to bottom
# (long tail) - cover-cropping to 16:9 clips both ends, so it stays letterbox.
_LBN = {"type": "letterbox", "zoom": [1.0, 1.03, 1.06], "pan": [(0.5, 0.5)] * 3, "ease": "ease-in"}

SLIDES = [
    {"img": "GAMBIER", **_CVZ},      # 0  s0-1   title; "rumoured a death a day"
    {"img": "MAP", **_MAPMOVE},      # 1  s2-3   Butterworth's 200/year; last tiger 1930
    {"img": "OTTERFAMILY", **_CVZ},  # 2  s4     "wild animals got smaller"
    {"img": "OTTERSIGN", **_LBI},    # 3  s5     the otter road sign in the CBD
    {"img": "GAMBIER", **_CVZO},     # 4  s6-7   swam from Malaya; virgin jungle
    {"img": "MAP", **_MAPMOVE},      # 5  s8-9   earliest reports; 1839 Rangong Road
    {"img": "GAMBIER", **_CVZ},      # 6  s10-11 gambier & pepper; cultivation spreads
    {"img": "GAMBIER", **_CVZO},     # 7  s12-13 coolies as targets; a death a day
    {"img": "TIMELINE", **_CHART},   # 8  s14    Butterworth's House of Commons estimate
    {"img": "MAP", **_MAPMOVE},      # 9  s15-16 Bukit Timah village abandoned; underreporting
    {"img": "GAMBIER", **_CVZ},      # 10 s17-18 the bounty; the reward climbs
    {"img": "GAMBIER", **_CVZO},     # 11 s19-20 camouflaged pits; hunting as sport
    {"img": "MAP", **_MAPMOVE},      # 12 s21-22 McNair's convict patrols; "did their work"
    {"img": "TIMELINE", **_CHART},   # 13 s23-24 Thomson Road 1890, Bukit Timah 1896, 1902
    {"img": "GAMBIER", **_CVZ},      # 14 s25-26 the circus tiger; "the story most people know"
    {"img": "MAP", **_MAPMOVE},      # 15 s27-29 the 1928 hunt; the family aside
    {"img": "GAMBIER", **_CVZO},     # 16 s30-32 the NAS record; jungle at the tenth milestone
    {"img": "TIMELINE", **_CHART},   # 17 s33-34 the same party, two years later; 1930
    {"img": "MAP", **_MAPMOVE},      # 18 s35-36 the last wild tiger; the photo survives
    {"img": "OTTERFAMILY", **_CVZ},  # 19 s37    "a century later, wild animals again"
    {"img": "OTTERSIGN", **_LBW},    # 20 s38    otters colonised the waterways
    {"img": "HORNBILL", **_LBI},     # 21 s39    the Oriental Pied Hornbill's comeback
    {"img": "BOAR", **_CVZ},         # 22 s40-41 not every comeback welcome; Pulau Ubin
    {"img": "BOAR", **_CVZO},        # 23 s42    relocate vs cull; the Punggol boar
    {"img": "MAP", **_MAPMOVE},      # 24 s43-44 crocodiles case-by-case; Marina East 2023
    {"img": "ECOLINK", **_CVZ},      # 25 s45    the Sentosa crocodiles
    {"img": "ECOLINK", **_CVZO},     # 26 s46-47 the Eco-Link@BKE bridge
    {"img": "MAP", **_MAPMOVE},      # 27 s48    "a century clearing the jungle"
    {"img": "HORNBILL", **_LBN},     # 28 s49    the forest patches; seniors' hikes
]

SCHEDULE = [
    (0.0, 0), (9.975, 1), (29.9, 2), (36.875, 3), (44.425, 4),
    (62.825, 5), (86.475, 6), (103.475, 7), (119.275, 8), (129.925, 9),
    (152.8, 10), (167.675, 11), (190.625, 12), (210.225, 13), (233.975, 14),
    (252.15, 15), (280.6, 16), (307.425, 17), (324.825, 18), (339.35, 19),
    (346.75, 20), (371.675, 21), (387.975, 22), (411.975, 23), (430.15, 24),
    (453.1, 25), (469.675, 26), (497.75, 27), (513.9, 28),
]
TOTAL_DURATION = 537.95
TIMING_JSON = "audio/when-singapore-had-wild-tigers.timing.json"
