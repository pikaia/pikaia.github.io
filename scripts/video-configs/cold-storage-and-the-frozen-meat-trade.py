"""Video config for the Cold Storage post.

Three images - a genuinely thin-image topic (no archival photo of the
1900s-1930s Cold Storage building or the Bukit Timah dairy farm itself
turned up on Wikimedia Commons; confirmed by several targeted Commons
searches, see chat). HERO carries most of the runtime.

  HERO       - Centrepoint shopping centre, Orchard Road (Commons) -
               the mall Cold Storage itself built and moved into in 1983
  QUARRY     - Singapore Quarry in Dairy Farm Nature Park (Commons) -
               the present-day site of the old Bukit Timah dairy farm
  FAIRPRICE  - an NTUC FairPrice checkout (Commons) - used on the
               present-day "still competing against NTUC FairPrice and
               Sheng Siong" beat

QUARRY is a landscape/nature photo but reads better letterboxed here
(it's specifically illustrating a place, not just decorative); HERO and
FAIRPRICE are ordinary landscape photos and use cover.

28 slides, 341.600s.
"""

_U = "https://upload.wikimedia.org/wikipedia/commons"

IMAGES = {
    "HERO": f"{_U}/2/29/Centrepoint_Shopping_Centre%2C_Singapore_-_20060212.jpg",
    "QUARRY": f"{_U}/a/a0/Singapore_Quarry_in_Dairy_Farm_Nature_Park%2C_with_viewing_platform_visible_in_foreground.jpg",
    "FAIRPRICE": f"{_U}/6/6a/FairPrice_Supermarket%2C_Nex%2C_Singapore_-_20140216.jpg",
}

_CVZ = {"type": "cover", "zoom": [1.0, 1.06, 1.12], "pan": [(0.5, 0.5)] * 3, "ease": "ease-in-out"}
_CVZO = {"type": "cover", "zoom": [1.12, 1.06, 1.0], "pan": [(0.5, 0.5)] * 3, "ease": "ease-out"}
_LTB = {"type": "letterbox", "zoom": [1.0, 1.04, 1.08], "pan": [(0.5, 0.5)] * 3, "ease": "ease-in-out"}
_LTBO = {"type": "letterbox", "zoom": [1.08, 1.04, 1.0], "pan": [(0.5, 0.5)] * 3, "ease": "ease-out"}

SLIDES = [
    {"img": "HERO", **_CVZ},        # 0  s0   title
    {"img": "HERO", **_CVZO},       # 1  s1   8 June 1903, registered
    {"img": "HERO", **_CVZ},        # 2  s2   everything grew out of that need
    {"img": "HERO", **_CVZO},       # 3  s3   first cargo, chilled meat/poultry/dairy
    {"img": "HERO", **_CVZ},        # 4  s4   first retail shop, 1905
    {"img": "HERO", **_CVZO},       # 5  s5   did not do well: servants avoided it
    {"img": "HERO", **_CVZ},        # 6  s6   recovered from 1909
    {"img": "HERO", **_CVZO},       # 7  s7   kept building on the same idea
    {"img": "HERO", **_CVZ},        # 8  s8   1923 ice cream factory, Paradise
    {"img": "QUARRY", **_LTB},      # 9  s9   1937 Fred Heron, tropical dairy farm
    {"img": "QUARRY", **_LTBO},     # 10 s10  Paradise relaunched as Magnolia
    {"img": "HERO", **_CVZ},        # 11 s11  1959 first self-service supermarket
    {"img": "HERO", **_CVZO},       # 12 s12  early 1980s, property developer
    {"img": "HERO", **_CVZ},        # 13 s13  Nov 1983, opened Centrepoint
    {"img": "HERO", **_CVZO},       # 14 s14  "the Cold Storage at Centrepoint"
    {"img": "HERO", **_CVZ},        # 15 s15  my own family, typical Chinese household
    {"img": "HERO", **_CVZO},       # 16 s16  after I married my wife
    {"img": "HERO", **_CVZ},        # 17 s17  every year before Christmas, behind Centrepoint
    {"img": "HERO", **_CVZO},       # 18 s18  pineapple and honey ham, such a hit
    {"img": "HERO", **_CVZ},        # 19 s19  ownership changed more than once
    {"img": "HERO", **_CVZO},       # 20 s20  1992, Dairy Farm International/Jardine Matheson
    {"img": "HERO", **_CVZ},        # 21 s21  March 2025, sold to Macrovalue
    {"img": "FAIRPRICE", **_CVZ},   # 22 s22  Macrovalue promised lower prices
    {"img": "FAIRPRICE", **_CVZO},  # 23 s23  alongside NTUC FairPrice and Sheng Siong
    {"img": "HERO", **_CVZ},        # 24 s24  visit back to Singapore, stayed in Joo Chiat
    {"img": "FAIRPRICE", **_CVZ},   # 25 s25  pricier than other chains, still there
    {"img": "HERO", **_CVZO},       # 26 s26  why it matters today
    {"img": "QUARRY", **_LTB},      # 27 s27  400-tonne shed, dairy farm with 800 cows
]

SCHEDULE = [
    (0.0, 0), (3.375, 1), (19.05, 2), (30.25, 3), (43.375, 4),
    (52.775, 5), (70.75, 6), (75.875, 7), (83.6, 8), (91.55, 9),
    (112.775, 10), (126.4, 11), (140.4, 12), (148.125, 13), (159.875, 14),
    (169.375, 15), (179.8, 16), (192.475, 17), (200.675, 18), (217.875, 19),
    (222.125, 20), (234.575, 21), (257.925, 22), (268.1, 23), (286.35, 24),
    (305.575, 25), (309.9, 26), (323.525, 27),
]
TOTAL_DURATION = 341.600
TIMING_JSON = "audio/cold-storage-and-the-frozen-meat-trade.timing.json"
