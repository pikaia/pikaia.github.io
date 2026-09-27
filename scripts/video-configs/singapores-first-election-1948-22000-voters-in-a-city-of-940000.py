"""Video config for the 1948 election post.

Visuals: the Victoria Theatre (where the votes were counted; the KITLV print and
a 1930s postcard, cover), portraits of C. C. Tan and Governor Gimson (frozen
letterbox), the registered-voters chart (scripts/render_election_voters_chart.py,
frozen), and the front pages of 20 and 21 March 1948 zoomed to the headlines,
the voter-registration reports and the results by constituency.

30 slides, one per sentence.
"""

IMAGES = {
    "CCTAN": "https://upload.wikimedia.org/wikipedia/commons/b/b6/Tan_Chye_Cheng.png",
    "CHART": "/assets/images/election-1948-registered-voters-chart.png",
    "GIMSON": "https://upload.wikimedia.org/wikipedia/commons/d/dd/Sir_Franklin_Gimson_in_1951.png",
    "ST20": "/assets/images/straits-times-1948-03-20-page-1.jpg",
    "ST21": "/assets/images/straits-times-1948-03-21-page-1.jpg",
    "VT": "https://upload.wikimedia.org/wikipedia/commons/thumb/a/a2/KITLV_A887_-_Victoria_Theatre_en_Memorial_Hall_te_Singapore%2C_KITLV_107516.tiff/lossy-page1-1280px-KITLV_A887_-_Victoria_Theatre_en_Memorial_Hall_te_Singapore%2C_KITLV_107516.tiff.jpg",
    "VT30": "https://upload.wikimedia.org/wikipedia/commons/e/e6/Victoria_Theatre_and_Victoria_Memorial_Hall_-_c_1930.jpg",
}

_P0 = {"type": "cover", "zoom": [1.0, 1.05, 1.1], "pan": [(0.35, 0.5), (0.5, 0.5), (0.65, 0.5)], "ease": "ease-in-out"}
_P1 = {"type": "cover", "zoom": [1.30, 1.33, 1.37], "pan": [(0.067, 0.0), (0.099, 0.0), (0.126, 0.0)], "ease": "ease-in-out"}
_P2 = {"type": "cover", "zoom": [2.20, 2.25, 2.31], "pan": [(0.372, 0.139), (0.374, 0.154), (0.377, 0.168)], "ease": "ease-in-out"}
_P3 = {"type": "cover", "zoom": [1.40, 1.43, 1.47], "pan": [(0.0, 0.0), (0.005, 0.0), (0.031, 0.019)], "ease": "ease-in-out"}
_P4 = {"type": "letterbox", "zoom": [1.0, 1.0, 1.0], "pan": [(0.5, 0.5)] * 3, "ease": "linear"}
_P5 = {"type": "cover", "zoom": [1.1, 1.05, 1.0], "pan": [(0.65, 0.5), (0.5, 0.5), (0.35, 0.5)], "ease": "ease-in-out"}
_P6 = {"type": "cover", "zoom": [2.40, 2.46, 2.52], "pan": [(0.38, 0.183), (0.382, 0.197), (0.384, 0.21)], "ease": "ease-in-out"}
_P7 = {"type": "cover", "zoom": [2.60, 2.67, 2.73], "pan": [(0.297, 0.404), (0.3, 0.416), (0.303, 0.429)], "ease": "ease-in-out"}
_P8 = {"type": "cover", "zoom": [2.40, 2.46, 2.52], "pan": [(0.0, 0.476), (0.0, 0.488), (0.0, 0.5)], "ease": "ease-in-out"}
_P9 = {"type": "cover", "zoom": [2.60, 2.67, 2.73], "pan": [(0.0, 0.548), (0.0, 0.56), (0.0, 0.571)], "ease": "ease-in-out"}
_P10 = {"type": "cover", "zoom": [1.3, 1.35, 1.4], "pan": [(0.55, 0.3), (0.55, 0.3), (0.55, 0.3)], "ease": "ease-in-out"}
_P11 = {"type": "cover", "zoom": [2.40, 2.46, 2.52], "pan": [(0.209, 0.622), (0.214, 0.633), (0.218, 0.645)], "ease": "ease-in-out"}
_P12 = {"type": "cover", "zoom": [2.60, 2.67, 2.73], "pan": [(0.224, 0.692), (0.228, 0.703), (0.232, 0.714)], "ease": "ease-in-out"}
_P13 = {"type": "cover", "zoom": [2.40, 2.46, 2.52], "pan": [(0.569, 0.671), (0.567, 0.682), (0.566, 0.693)], "ease": "ease-in-out"}
_P14 = {"type": "cover", "zoom": [1.30, 1.33, 1.37], "pan": [(0.0, 0.0), (0.0, 0.0), (0.0, 0.003)], "ease": "ease-in-out"}
_P15 = {"type": "cover", "zoom": [2.40, 2.46, 2.52], "pan": [(0.191, 0.317), (0.197, 0.33), (0.202, 0.343)], "ease": "ease-in-out"}
_P16 = {"type": "cover", "zoom": [2.40, 2.46, 2.52], "pan": [(0.106, 0.22), (0.112, 0.233), (0.119, 0.247)], "ease": "ease-in-out"}
_P17 = {"type": "cover", "zoom": [2.60, 2.67, 2.73], "pan": [(0.403, 0.428), (0.404, 0.44), (0.405, 0.453)], "ease": "ease-in-out"}
_P18 = {"type": "cover", "zoom": [1.80, 1.84, 1.89], "pan": [(0.0, 0.132), (0.0, 0.148), (0.0, 0.163)], "ease": "ease-in-out"}

SLIDES = [
    {"img": "VT", **_P0},  # s0 Singapore's First Election, 1948: 22,000 Vot
    {"img": "ST20", **_P1},  # s1 On the 20th of March 1948 Singapore held its
    {"img": "ST20", **_P2},  # s2 Six seats on a Legislative Council of twenty
    {"img": "ST21", **_P3},  # s3 The Sunday Times the next morning reported t
    {"img": "CHART", **_P4},  # s4 Eleven years later, at the 1959 election, 58
    {"img": "VT30", **_P0},  # s5 After the Japanese occupation the Straits Se
    {"img": "GIMSON", **_P4},  # s6 Its new Legislative Council had 22 members.
    {"img": "VT", **_P5},  # s7 Thirteen were officials, three were nominate
    {"img": "ST20", **_P6},  # s8 On the morning of the vote the Straits Times
    {"img": "ST20", **_P7},  # s9 The vote was open to British subjects aged 2
    {"img": "VT30", **_P5},  # s10 Registration was voluntary, and many people 
    {"img": "ST20", **_P8},  # s11 The same front page carried a warning from T
    {"img": "ST20", **_P9},  # s12 He said that only about 5,300 of the Chinese
    {"img": "VT", **_P10},  # s13 Many other residents, including most of thos
    {"img": "ST20", **_P11},  # s14 The Malayan Democratic Union and several oth
    {"img": "ST20", **_P12},  # s15 Candidates for the Progressive Party replied
    {"img": "ST20", **_P13},  # s16 On the eve of the vote, the Supervisor of El
    {"img": "ST21", **_P14},  # s17 Fifteen candidates stood.
    {"img": "ST21", **_P15},  # s18 The Sunday Times of the 21st of March report
    {"img": "ST21", **_P16},  # s19 The six elected members were Sardon bin Haji
    {"img": "CCTAN", **_P4},  # s20 Three belonged to the Progressive Party and 
    {"img": "ST21", **_P17},  # s21 C. C. Tan, the Progressive Party's president
    {"img": "VT30", **_P0},  # s22 The electorate stayed small for several year
    {"img": "CHART", **_P4},  # s23 At the next election, on the 10th of April 1
    {"img": "CHART", **_P4},  # s24 The large change came in 1955, under the Ren
    {"img": "CCTAN", **_P4},  # s25 That election made David Marshall Singapore'
    {"img": "CHART", **_P4},  # s26 At the 1959 election, the first under full i
    {"img": "VT", **_P0},  # s27 Where it fits in the bigger story: Singapore
    {"img": "ST21", **_P18},  # s28 The first election, eleven years earlier, wa
    {"img": "VT", **_P5},  # s29 The growth from 22,334 voters in 1948 to 586
]

SCHEDULE = [
    (0.0, 0), (8.45, 1), (14.2, 2), (28.0, 3), (35.025, 4),
    (45.375, 5), (55.35, 6), (59.525, 7), (71.825, 8), (84.6, 9),
    (93.525, 10), (99.575, 11), (114.225, 12), (129.125, 13), (136.8, 14),
    (151.5, 15), (157.875, 16), (167.95, 17), (170.525, 18), (188.95, 19),
    (198.175, 20), (204.575, 21), (217.425, 22), (221.05, 23), (233.275, 24),
    (251.975, 25), (257.0, 26), (272.2, 27), (281.825, 28), (295.225, 29),
]
TOTAL_DURATION = 311.55
TIMING_JSON = "audio/singapores-first-election-1948-22000-voters-in-a-city-of-940000.timing.json"
