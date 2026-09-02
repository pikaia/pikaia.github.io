"""Video config for "The Three Days Singapore's Stock Market Closed" -
Watch widget and main video (the 1985 Pan-Electric collapse).

A 1985 financial-scandal story with almost no freely-licensed
photography - no trading floor, no Pan-Electric, no Tan Koon Swan - so
the visual backbone is four explanatory graphics rather than photo
stand-ins:

  FORWARD   how a forward contract propped up the share price
  MONEY     the crisis by the scale of the money (four bars)
  TIMELINE  the shutdown through to the CLOB freeze
  MAP       the exchange floor and the rescue banks, a few blocks apart

Each is a static PNG the site renders itself (render_three_days_*.py),
shown frozen (zoom held at 1.0) while the narration walks it; TIMELINE
runs twice. Five recognisable financial-district photos (hero + Clifford
Centre + 1971 Raffles Place + two skyline shots) carry the rest, reused
with slow zooms.

The graphics are letterbox + frozen, never cover: cover scales an image
to fill the frame and clips whatever overflows, which cropped the
diagram labels off the edges in the Watch widget. Letterbox contains the
whole PNG (blurred bars fill any aspect gap) so every label stays on
screen.

Only the hero skyline is wide enough for cover (3840x2400), and it takes
a centred push-in (_CVZ); a horizontal pan across it reads JERKY on the
smoothness check. Every other photo is portrait or near-square, so
letterbox, cycling push-in / pull-out. Letterbox + zero pan and a frozen
graphic both read JERKY in --check-only - the documented false positives
(pipeline section 5); the five cover slides (0, 12, 30, 35, 37) all pass.
No slide held past ~30s; gap report clean.

38 slides, 537.575s.
"""

_C = "https://upload.wikimedia.org/wikipedia/commons"

IMAGES = {
    "SKYLINE": f"{_C}/1/1e/Singapore_Skyline_Raffles_Place.jpg",
    "CLIFFORD": f"{_C}/b/b8/Clifford_Centre.JPG",
    "RP1971": f"{_C}/d/dc/71-610_Raffles_Place_Singapore_1971_%2851252222815%29.jpg",
    "RIVER": f"{_C}/3/36/Singapore_skyline.JPG",
    "DUSK": f"{_C}/a/a8/Evening_view_of_UOB_Plaza%2C_OUB_Centre_and_OCBC_Centre_near_the_Singapore_River_-_20010608.jpg",
    "FORWARD": "/assets/images/three-days-stock-exchange-shut-1985-forward.png",
    "MONEY": "/assets/images/three-days-stock-exchange-shut-1985-money.png",
    "TIMELINE": "/assets/images/three-days-stock-exchange-shut-1985-timeline.png",
    "MAP": "/assets/images/three-days-stock-exchange-shut-1985-map.png",
}

CREDITS = {
    "FORWARD": "Diagram by Lesser Known Singapore",
    "MONEY": "Chart by Lesser Known Singapore",
    "TIMELINE": "Chart by Lesser Known Singapore",
    "MAP": "Map by Lesser Known Singapore; base map data © OpenStreetMap contributors",
}

_LBI = {"type": "letterbox", "zoom": [1, 1.05, 1.10], "pan": [(0.5, 0.5)] * 3, "ease": "ease-in-out"}
_LBO = {"type": "letterbox", "zoom": [1.10, 1.05, 1], "pan": [(0.5, 0.5)] * 3, "ease": "ease-out"}
_LBW = {"type": "letterbox", "zoom": [1, 1.06, 1.12], "pan": [(0.5, 0.5)] * 3, "ease": "ease-in-out"}
_CVZ = {"type": "cover", "zoom": [1.0, 1.06, 1.12], "pan": [(0.5, 0.5)] * 3, "ease": "ease-in-out"}
# Graphics are shown whole - letterbox (never cover, which crops labels off
# the edges) and frozen (no zoom). The blurred bars fill any aspect gap.
_CHART = {"type": "letterbox", "zoom": [1.0, 1.0, 1.0], "pan": [(0.5, 0.5)] * 3, "ease": "linear"}

SLIDES = [
    {"img": "SKYLINE", **_CVZ},     # 0
    {"img": "CLIFFORD", **_LBI},    # 1
    {"img": "RP1971", **_LBW},      # 2
    {"img": "DUSK", **_LBI},        # 3
    {"img": "RP1971", **_LBI},      # 4
    {"img": "RIVER", **_LBW},       # 5
    {"img": "DUSK", **_LBO},        # 6
    {"img": "RP1971", **_LBI},      # 7
    {"img": "RIVER", **_LBI},       # 8
    {"img": "CLIFFORD", **_LBW},    # 9
    {"img": "DUSK", **_LBI},        # 10
    {"img": "RIVER", **_LBO},       # 11
    {"img": "SKYLINE", **_CVZ},     # 12
    {"img": "FORWARD", **_CHART},   # 13
    {"img": "CLIFFORD", **_LBI},    # 14
    {"img": "MONEY", **_CHART},     # 15
    {"img": "RP1971", **_LBI},      # 16
    {"img": "CLIFFORD", **_LBW},    # 17
    {"img": "DUSK", **_LBO},        # 18
    {"img": "RIVER", **_LBI},       # 19
    {"img": "TIMELINE", **_CHART},  # 20
    {"img": "MAP", **_CHART},       # 21
    {"img": "CLIFFORD", **_LBW},    # 22
    {"img": "DUSK", **_LBI},        # 23
    {"img": "RIVER", **_LBW},       # 24
    {"img": "RP1971", **_LBI},      # 25
    {"img": "CLIFFORD", **_LBI},    # 26
    {"img": "DUSK", **_LBW},        # 27
    {"img": "RIVER", **_LBI},       # 28
    {"img": "CLIFFORD", **_LBO},    # 29
    {"img": "SKYLINE", **_CVZ},     # 30
    {"img": "RP1971", **_LBW},      # 31
    {"img": "TIMELINE", **_CHART},  # 32
    {"img": "DUSK", **_LBI},        # 33
    {"img": "TIMELINE", **_CHART},  # 34
    {"img": "SKYLINE", **_CVZ},     # 35
    {"img": "RIVER", **_LBW},       # 36
    {"img": "SKYLINE", **_CVZ},     # 37
]

# Real values from audio/three-days-stock-exchange-shut-1985.timing.json.
# Every point is a real sentence start; slide index runs 0..37 in order.
#   0  s0-1   title; Mon 2 Dec 1985, the Stock Exchange of Singapore did
#             not open
#   1  s2-3   neither did Kuala Lumpur; both shut three days - the only
#             time the market has ever closed completely
#   2  s4     what forced it: Pan-Electric, a fridge maker turned
#             conglomerate, and a web of undisclosed contracts
#   3  s5     Tan Koon Swan, elected leader of Malaysia's main Chinese
#             party three weeks earlier
#   4  s6     Pan-Electric began 1956 as Climate Engineering, importing
#             French Frimatic refrigerators
#   5  s7     founder Ernest Kahlenberg; pioneer-industry scheme, renamed
#             1961, factory at Kampong Arang Road 1965
#   6  s8     by 1967 the largest fridge plant in Southeast Asia; listed
#             August 1968
#   7  s9     from the mid-1970s: Selco salvage, Vanguard Realty, the 1981
#             Acma merger, hotels
#   8  s10    by 1985 around sixty subsidiaries
#   9  s11    Peter Tham joined the board 1982; Kahlenberg gone by 1983
#   10 s12    Tan Koon Swan: a Malaysian, his fortune made in Singapore's
#             market, a golden-touch reputation
#   11 s13    his interest held through Sigma International and Grand United
#   12 s14    November 1985 - elected president of the MCA, a partner in
#             Malaysia's ruling coalition
#   13 s15-17 FORWARD: the share price was propped up with forward
#             contracts - how one works, and why it was accepted practice
#   14 s18    what made this dangerous: large, undisclosed, and the market
#             fell instead of rising
#   15 s19-21 MONEY: Tan's ~S$140m, market-wide ~S$600m, and the ~S$29m he
#             moved out of company accounts
#   16 s22-23 27 Sep 1985 a S$64m rights issue; 18 Nov a missed loan
#             payment
#   17 s24    21 Nov - S$453 million owed to thirty-five banks, mostly
#             unsecured
#   18 s25    the banks stopped lending, to Pan-Electric and to the brokers
#             tied to it
#   19 s26    30 November - receivership
#   20 s27-30 TIMELINE: the danger of a chain reaction; on Monday 2
#             December both exchanges suspend trading, closed through
#             Wednesday
#   21 s31-32 MAP: behind closed doors, the four big banks are asked for a
#             credit line, first S$150m, settled at S$180m
#   22 s33    Chan Sek Keong, later Chief Justice, helped the MAS draft it
#   23 s34    Richard Hu: not there to save reckless brokers, and anything
#             drawn would be repaid with interest
#   24 s35-36 about six broking firms did not survive; the market reopened
#             Friday 5 December
#   25 s37-38 Pan-Electric wound up October 1986; shares worthless,
#             thousands of shareholders and creditors carried the loss
#   26 s39    Tan Koon Swan arrested January 1986
#   27 s40    pleaded guilty, fifteen charges cut to one, two years' jail
#             and a fine
#   28 s41    resigned the MCA presidency; the conviction ended his
#             political career
#   29 s42-43 Peter Tham eight years for forgery; decades later some,
#             including the lead prosecutor, call the conviction wrong
#   30 s44-45 the lasting change was the rules - the Securities Industry
#             Act of 1986
#   31 s46-47 the crisis exposed how entangled the two exchanges were; at
#             the end of 1989 they delisted each other's companies
#   32 s48-49 TIMELINE: Singapore opened CLOB International, January 1990;
#             it ran quietly for eight years
#   33 s50    September 1998 - Malaysia freezes it: ~S$4 billion, about
#             172,000 investors, almost all Singaporean
#   34 s51-52 TIMELINE: released in stages in early 2000; the untangling
#             took fifteen years and a second crisis
#   35 s53-54 where it fits: the shape is familiar - it begins with a
#             scheme that bends convention without breaking the law
#   36 s55-56 it runs long because the name at the centre is trusted; then
#             something unforeseen turns the bet the wrong way
#   37 s57-58 Pan-Electric was the first time that pattern closed a
#             Singapore exchange; it was not the last
SCHEDULE = [
    (0.0, 0), (11.65, 1), (22.075, 2), (35.725, 3), (46.325, 4),
    (55.425, 5), (72.175, 6), (83.7, 7), (100.775, 8), (106.975, 9),
    (113.725, 10), (124.45, 11), (133.275, 12), (149.25, 13), (172.0, 14),
    (189.1, 15), (218.825, 16), (234.1, 17), (244.875, 18), (250.925, 19),
    (255.925, 20), (283.7, 21), (311.65, 22), (319.85, 23), (334.625, 24),
    (343.275, 25), (354.45, 26), (359.6, 27), (370.675, 28), (378.525, 29),
    (398.55, 30), (419.3, 31), (433.125, 32), (447.1, 33), (466.675, 34),
    (482.7, 35), (501.25, 36), (528.5, 37),
]
TOTAL_DURATION = 537.575
TIMING_JSON = "audio/three-days-stock-exchange-shut-1985.timing.json"
