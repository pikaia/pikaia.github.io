"""Video config for the Coney Island post's Watch widget / main video.

The image set is modest: seven sources for ~6 minutes. There is no
photography of the Aw-era villa or the 1950s "Singapore Coney Island"
resort that clears licensing, and the island itself is only lightly
photographed on Commons. So the video leans on a few repeated images
with varied push/pull framing -

  NYLUNA     - "Night in Luna Park, Coney Island" (Detroit Publishing
               Co., 1905, public domain) - the New York namesake, for
               the opening two sentences only
  GATE       - the modern "Coney Island" entrance gate (landscape -> cover)
  MAP        - the OSM locator, island off Punggol (letterbox, near-frozen)
  PANO2022   - the author's wide view of the wooded island across
               Serangoon Reservoir (a 3.8:1 panorama -> cover, centre crop)
  AWBH       - Aw Boon Haw, portrait from Who's Who in China (1931,
               public domain; a small scan -> letterbox, gentle zoom)
  GROUP1979  - the author's group on the island, 1979 (letterbox; a 4:3
               print, and "UNITY" sits on the left edge, so cover would
               crop it)
  OTTERS     - present-day wildlife (portrait -> letterbox)

Graphics (MAP) are letterbox and near-frozen, per
docs/production-pipeline.md s3 - cover would crop the labels. Everything
else is centred zoom, no horizontal pan (the pan read JERKY on the
pineapple-kings post's large scans - so PANO2022 takes a fixed centre
crop rather than a pan reveal).

28 slides, 369.825s.
"""

_C = "https://upload.wikimedia.org/wikipedia/commons"

IMAGES = {
    "NYLUNA": f"{_C}/8/82/Night_in_Luna_Park%2C_Coney_Island_%281905%29.jpg",  # 5885x4768
    "GATE": f"{_C}/8/87/Coney_Island_Gate.jpg",                              # 3456x2304
    "MAP": "/assets/images/coney-island-before-it-was-a-nature-park-map.png",  # 1600x1280, OSM-based, committed locally
    "PANO2022": "/assets/images/coney-island-2022.jpg",                     # 2000x528 panorama, committed locally
    "AWBH": f"{_C}/f/f9/Hu_Wenhu2.jpg",                                     # 343x531 portrait scan
    "GROUP1979": "/assets/images/coney-island-1979.jpg",                    # 692x514, committed locally
    "OTTERS": f"{_C}/b/bd/Pair_of_Smooth-coated_otters.jpg",                # 922x1247 (portrait)
}

CREDITS = {
    "MAP": "Map by Lesser Known Singapore; base map data © OpenStreetMap contributors",
    "PANO2022": "Photograph: Lesser Known Singapore",
    "GROUP1979": "From Paul Kang's collection",
}

_LBI = {"type": "letterbox", "zoom": [1.0, 1.04, 1.08], "pan": [(0.5, 0.5)] * 3, "ease": "ease-in-out"}
_LBW = {"type": "letterbox", "zoom": [1.0, 1.05, 1.10], "pan": [(0.5, 0.5)] * 3, "ease": "ease-in-out"}
_LBN = {"type": "letterbox", "zoom": [1.0, 1.03, 1.06], "pan": [(0.5, 0.5)] * 3, "ease": "ease-in"}
_CVZ = {"type": "cover", "zoom": [1.0, 1.06, 1.12], "pan": [(0.5, 0.5)] * 3, "ease": "ease-in-out"}
_CVZO = {"type": "cover", "zoom": [1.12, 1.06, 1.0], "pan": [(0.5, 0.5)] * 3, "ease": "ease-out"}
_MAPMOVE = {"type": "letterbox", "zoom": [1.0, 1.03, 1.05], "pan": [(0.5, 0.5)] * 3, "ease": "linear"}

SLIDES = [
    {"img": "NYLUNA", **_CVZ},      # 0  s0     title (New York's Luna Park, 1905)
    {"img": "NYLUNA", **_CVZO},     # 1  s1     New York: a switchback railway, a Ferris wheel, a million visitors
    {"img": "GATE", **_CVZ},        # 2  s2     Singapore: a locked gate and a gravel track
    {"img": "MAP", **_MAPMOVE},     # 3  s3     the name arrives in 1950; a small island off Punggol
    {"img": "PANO2022", **_CVZ},    # 4  s4-5   the plan failed; the opposite of a resort
    {"img": "MAP", **_MAPMOVE},     # 5  s6     Pulau Serangoon, a thin wooded strip off Punggol
    {"img": "AWBH", **_LBN},        # 6  s7     1937: Aw Boon Haw bought it
    {"img": "PANO2022", **_CVZ},    # 7  s8     the Tiger Balm fortune; a beach villa on the island
    {"img": "MAP", **_MAPMOVE},     # 8  s9-10  attributed to Ho Kwong Yew; "Haw Par Island"
    {"img": "PANO2022", **_CVZO},   # 9  s11-12 the villa didn't last; Occupation; sold on
    {"img": "GATE", **_CVZO},       # 10 s13-14 the buyer, Ghulam Mahmood; a mass-market resort
    {"img": "PANO2022", **_CVZ},    # 11 s15-16 renamed Coney Island; launches, the Coney Island Band
    {"img": "MAP", **_MAPMOVE},     # 12 s17-19 it didn't take; auction; a run of owners
    {"img": "GROUP1979", **_LBN},   # 13 s20-21 the national-service visit, around 1979
    {"img": "GROUP1979", **_LBI},   # 14 s22-23 overgrown and quiet; nobody to stop us
    {"img": "MAP", **_MAPMOVE},     # 15 s24-25 government acquires it, 1972; PSA reclamation
    {"img": "PANO2022", **_CVZO},   # 16 s26-28 the 1990s fill; the 1980s plan to join it on
    {"img": "GATE", **_CVZ},        # 17 s29-30 simply shut; fenced off; grazing cattle
    {"img": "GATE", **_CVZO},       # 18 s31    Coney Island Park opens, 10 October 2015
    {"img": "PANO2022", **_CVZ},    # 19 s32-33 deliberately spare; beaches A to E; boardwalks
    {"img": "PANO2022", **_CVZO},   # 20 s34-35 nothing to buy; casuarina; eighty bird species
    {"img": "GATE", **_CVZ},        # 21 s36-37 the Brahman bull; its 2016 obituary
    {"img": "PANO2022", **_CVZ},    # 22 s38    the Haw Par villa, roofless among the trees
    {"img": "OTTERS", **_LBI},      # 23 s39    the otters, pigs and birds arrived on their own
    {"img": "OTTERS", **_LBW},      # 24 s40-41 the irony; sixty years of selling it as fun
    {"img": "GATE", **_CVZO},       # 25 s42    the version that stuck sells nothing
    {"img": "MAP", **_MAPMOVE},     # 26 s43-44 closing; larger than it was born, tied to the shore
    {"img": "GATE", **_CVZ},        # 27 s45    the rough edges are a decision
]

SCHEDULE = [
    (0.0, 0), (3.65, 1), (11.25, 2), (19.625, 3), (30.55, 4),
    (42.525, 5), (53.25, 6), (58.075, 7), (77.3, 8), (92.3, 9),
    (105.425, 10), (128.525, 11), (145.075, 12), (166.475, 13), (179.325, 14),
    (192.45, 15), (212.15, 16), (241.55, 17), (252.0, 18), (260.975, 19),
    (274.05, 20), (291.675, 21), (313.4, 22), (320.4, 23), (324.825, 24),
    (337.375, 25), (344.425, 26), (365.775, 27),
]
TOTAL_DURATION = 369.825
TIMING_JSON = "audio/coney-island-before-it-was-a-nature-park.timing.json"
