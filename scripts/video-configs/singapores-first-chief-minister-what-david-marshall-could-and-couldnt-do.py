"""Video config for the David Marshall post.

Most of the visual pool is Straits Times pages (1955-56), each zoomed to a
different region: headlines, photos, columns. The delegation photo (London,
1956) is the only landscape photograph and is reused with different pans and
zooms. The portraits (Marshall as a lawyer, a volunteer, a prisoner of war, at
the Victoria Memorial Hall, in London) are small or portrait-format, so they are
frozen letterbox, as is the seats chart. The one bloodied photograph on the
13 May 1955 front page is never in frame (the window stays on its left side).

  CHART - scripts/render_marshall_seats_chart.py
  S0403/S0404/S0513/S0516/S0608/S0608P2/S0608P8 - The Straits Times, whole pages

59 slides; sentences 8, 11, 13, 21, 29, 33 (short) continue the slide before.
"""

IMAGES = {
    "B30": "https://upload.wikimedia.org/wikipedia/commons/9/98/David_Saul_Marshall%2C_1930s_%28cropped%29.jpg",
    "BCO": "https://upload.wikimedia.org/wikipedia/commons/9/9b/David_Marshall_with_%22B%22_Company_during_WWII.jpg",
    "CHART": "/assets/images/marshall-1955-seats-chart.png",
    "DEL": "https://thumb.wikimedia.org/wikipedia/commons/thumb/0/0c/Singaporean_delegation_at_the_1956_constitutional_talks.png/1920px-Singaporean_delegation_at_the_1956_constitutional_talks.png",
    "NIC": "https://upload.wikimedia.org/wikipedia/commons/e/e6/David_Marshall%2C_1952.jpg",
    "POW": "https://upload.wikimedia.org/wikipedia/commons/d/d0/David_Marshall_as_a_prisoner-of-war%2C_1944.png",
    "S0403": "/assets/images/straits-times-1955-04-03-page-1.jpg",
    "S0404": "/assets/images/straits-times-1955-04-04-page-1.jpg",
    "S0513": "/assets/images/straits-times-1955-05-13-page-1.jpg",
    "S0516": "/assets/images/straits-times-1956-05-16-page-1.jpg",
    "S0608": "/assets/images/straits-times-1956-06-08-page-1.jpg",
    "S0608P2": "/assets/images/straits-times-1956-06-08-page-2.jpg",
    "S0608P8": "/assets/images/straits-times-1956-06-08-page-8.jpg",
    "T20": "https://upload.wikimedia.org/wikipedia/commons/9/91/David_Marshall%2C_1920s.png",
    "TALK": "https://upload.wikimedia.org/wikipedia/commons/0/09/David_Marshall%2C_1956_%28cropped%29.png",
}

CREDITS = {
    "CHART": "Chart by Lesser Known Singapore, figures per The Sunday Times, 3 April 1955",
}

_P0 = {"type": "cover", "zoom": [1.0, 1.05, 1.1], "pan": [(0.25, 0.5), (0.5, 0.5), (0.75, 0.5)], "ease": "ease-in-out"}
_P1 = {"type": "cover", "zoom": [2.00, 2.05, 2.10], "pan": [(0.0, 0.017), (0.256, 0.02), (0.5, 0.023)], "ease": "ease-in-out"}
_P2 = {"type": "cover", "zoom": [1.15, 1.18, 1.21], "pan": [(0.5, 0.039), (0.5, 0.068), (0.5, 0.095)], "ease": "ease-in-out"}
_P3 = {"type": "cover", "zoom": [2.00, 2.05, 2.10], "pan": [(0.16, 0.0), (0.217, 0.0), (0.271, 0.0)], "ease": "ease-in-out"}
_P4 = {"type": "cover", "zoom": [1.1, 1.05, 1.0], "pan": [(0.75, 0.5), (0.5, 0.5), (0.25, 0.5)], "ease": "ease-in-out"}
_P5 = {"type": "letterbox", "zoom": [1.0, 1.0, 1.0], "pan": [(0.5, 0.5)] * 3, "ease": "linear"}
_P6 = {"type": "cover", "zoom": [1.30, 1.33, 1.37], "pan": [(0.717, 0.293), (0.7, 0.317), (0.687, 0.341)], "ease": "ease-in-out"}
_P7 = {"type": "cover", "zoom": [1.15, 1.18, 1.21], "pan": [(0.5, 0.0), (0.5, 0.02), (0.5, 0.047)], "ease": "ease-in-out"}
_P8 = {"type": "cover", "zoom": [2.20, 2.25, 2.31], "pan": [(0.133, 0.246), (0.141, 0.265), (0.147, 0.285)], "ease": "ease-in-out"}
_P9 = {"type": "cover", "zoom": [1.25, 1.28, 1.31], "pan": [(0.5, 0.0), (0.5, 0.024), (0.5, 0.049)], "ease": "ease-in-out"}
_P10 = {"type": "cover", "zoom": [1.20, 1.23, 1.26], "pan": [(0.5, 0.0), (0.5, 0.0), (0.5, 0.0)], "ease": "ease-in-out"}
_P11 = {"type": "cover", "zoom": [1.30, 1.33, 1.37], "pan": [(0.717, 0.293), (0.7, 0.339), (0.687, 0.384)], "ease": "ease-in-out"}
_P12 = {"type": "cover", "zoom": [1.80, 1.84, 1.89], "pan": [(1.0, 0.67), (1.0, 0.688), (1.0, 0.706)], "ease": "ease-in-out"}
_P13 = {"type": "cover", "zoom": [1.70, 1.74, 1.78], "pan": [(0.257, 0.0), (0.265, 0.014), (0.273, 0.038)], "ease": "ease-in-out"}
_P14 = {"type": "cover", "zoom": [1.90, 1.95, 1.99], "pan": [(0.078, 0.241), (0.109, 0.262), (0.139, 0.283)], "ease": "ease-in-out"}
_P15 = {"type": "cover", "zoom": [1.70, 1.74, 1.78], "pan": [(0.063, 0.0), (0.218, 0.0), (0.364, 0.0)], "ease": "ease-in-out"}
_P16 = {"type": "cover", "zoom": [1.90, 1.95, 1.99], "pan": [(0.183, 0.927), (0.192, 0.944), (0.199, 0.96)], "ease": "ease-in-out"}
_P17 = {"type": "cover", "zoom": [1.60, 1.64, 1.68], "pan": [(0.233, 0.144), (0.244, 0.167), (0.253, 0.19)], "ease": "ease-in-out"}
_P18 = {"type": "cover", "zoom": [2.00, 2.05, 2.10], "pan": [(0.54, 0.628), (0.539, 0.646), (0.538, 0.664)], "ease": "ease-in-out"}
_P19 = {"type": "cover", "zoom": [2.00, 2.05, 2.10], "pan": [(0.0, 0.653), (0.0, 0.671), (0.0, 0.689)], "ease": "ease-in-out"}
_P20 = {"type": "cover", "zoom": [2.40, 2.46, 2.52], "pan": [(1.0, 0.621), (1.0, 0.639), (1.0, 0.656)], "ease": "ease-in-out"}
_P21 = {"type": "cover", "zoom": [1.3, 1.35, 1.4], "pan": [(0.45, 0.55), (0.5, 0.5), (0.55, 0.5)], "ease": "ease-in-out"}
_P22 = {"type": "cover", "zoom": [2.00, 2.05, 2.10], "pan": [(0.0, 0.73), (0.012, 0.747), (0.023, 0.764)], "ease": "ease-in-out"}
_P23 = {"type": "cover", "zoom": [1.90, 1.95, 1.99], "pan": [(0.036, 0.565), (0.048, 0.584), (0.059, 0.602)], "ease": "ease-in-out"}
_P24 = {"type": "cover", "zoom": [1.45, 1.4, 1.35], "pan": [(0.75, 0.5), (0.65, 0.55), (0.55, 0.6)], "ease": "ease-in-out"}
_P25 = {"type": "cover", "zoom": [2.60, 2.67, 2.73], "pan": [(0.988, 1.0), (0.98, 1.0), (0.973, 1.0)], "ease": "ease-in-out"}
_P26 = {"type": "cover", "zoom": [2.00, 2.05, 2.10], "pan": [(0.94, 0.225), (0.93, 0.245), (0.92, 0.265)], "ease": "ease-in-out"}
_P27 = {"type": "cover", "zoom": [2.00, 2.05, 2.10], "pan": [(0.94, 0.437), (0.93, 0.456), (0.92, 0.475)], "ease": "ease-in-out"}
_P28 = {"type": "cover", "zoom": [2.00, 2.05, 2.10], "pan": [(0.94, 0.3), (0.93, 0.32), (0.92, 0.339)], "ease": "ease-in-out"}
_P29 = {"type": "cover", "zoom": [2.40, 2.46, 2.52], "pan": [(1.0, 0.56), (1.0, 0.578), (1.0, 0.595)], "ease": "ease-in-out"}
_P30 = {"type": "cover", "zoom": [1.30, 1.33, 1.37], "pan": [(0.5, 0.0), (0.5, 0.0), (0.5, 0.0)], "ease": "ease-in-out"}
_P31 = {"type": "cover", "zoom": [2.40, 2.46, 2.52], "pan": [(0.0, 0.163), (0.0, 0.183), (0.0, 0.202)], "ease": "ease-in-out"}
_P32 = {"type": "cover", "zoom": [2.60, 2.67, 2.73], "pan": [(0.0, 0.228), (0.0, 0.247), (0.0, 0.265)], "ease": "ease-in-out"}
_P33 = {"type": "cover", "zoom": [2.40, 2.46, 2.52], "pan": [(0.174, 0.259), (0.18, 0.279), (0.185, 0.297)], "ease": "ease-in-out"}
_P34 = {"type": "cover", "zoom": [2.40, 2.46, 2.52], "pan": [(0.174, 0.356), (0.18, 0.374), (0.185, 0.393)], "ease": "ease-in-out"}
_P35 = {"type": "cover", "zoom": [2.40, 2.46, 2.52], "pan": [(0.26, 0.692), (0.264, 0.709), (0.268, 0.726)], "ease": "ease-in-out"}
_P36 = {"type": "cover", "zoom": [1.60, 1.64, 1.68], "pan": [(1.0, 0.018), (1.0, 0.042), (1.0, 0.065)], "ease": "ease-in-out"}
_P37 = {"type": "cover", "zoom": [1.35, 1.4, 1.45], "pan": [(0.15, 0.6), (0.2, 0.55), (0.3, 0.5)], "ease": "ease-in-out"}
_P38 = {"type": "cover", "zoom": [2.00, 2.05, 2.10], "pan": [(0.6, 0.017), (0.354, 0.02), (0.118, 0.023)], "ease": "ease-in-out"}

SLIDES = [
    {"img": "DEL", **_P0},  # s0 Singapore's First Chief Minister: What David
    {"img": "S0608", **_P1},  # s1 At 5 p.m. on the 7th of June 1956, David Mar
    {"img": "S0516", **_P2},  # s2 He had said he would resign if he could not 
    {"img": "S0608", **_P3},  # s3 The Straits Times of the following morning p
    {"img": "DEL", **_P4},  # s4 The story of those fourteen months is as muc
    {"img": "B30", **_P5},  # s5 David Marshall was born in Singapore on the 
    {"img": "BCO", **_P5},  # s6 He joined the Singapore Volunteer Corps that
    {"img": "POW", **_P5},  # s7 After the fall of Singapore he was marched t
    {"img": "B30", **_P5},  # s8 After the war he became one of Singapore's b
    {"img": "S0404", **_P6},  # s9 In August 1954 he founded the Labour Front w
    {"img": "S0403", **_P7},  # s10 The election of the 2nd of April 1955 was th
    {"img": "NIC", **_P5},  # s11 The British kept defence, external affairs a
    {"img": "S0403", **_P8},  # s12 There were more than 300,000 registered vote
    {"img": "S0403", **_P9},  # s13 The Sunday Times of the 3rd of April ran the
    {"img": "CHART", **_P5},  # s14 The Labour Front had won ten seats, the most
    {"img": "S0404", **_P10},  # s15 The Straits Times of the next day headed its
    {"img": "S0404", **_P11},  # s16 Marshall nevertheless formed a minority gove
    {"img": "S0404", **_P12},  # s17 Three colonial officials, the Chief Secretar
    {"img": "S0513", **_P13},  # s18 His government was barely a month old when t
    {"img": "S0513", **_P14},  # s19 The dispute began when the bus company dismi
    {"img": "S0513", **_P15},  # s20 On the 12th of May 1955 riots broke out alon
    {"img": "S0513", **_P16},  # s21 Four people died, among them two police offi
    {"img": "S0513", **_P17},  # s22 The Straits Times of the 13th of May carried
    {"img": "S0513", **_P18},  # s23 An agreement to end the strike was reached o
    {"img": "S0513", **_P19},  # s24 After students staged sit-ins at several Chi
    {"img": "NIC", **_P5},  # s25 The second test was over the limits of the o
    {"img": "S0404", **_P20},  # s26 In July 1955 Marshall asked for four junior 
    {"img": "DEL", **_P21},  # s27 He threatened to resign, and the dispute was
    {"img": "DEL", **_P0},  # s28 Marshall's government passed a good deal in 
    {"img": "S0513", **_P22},  # s29 The Emergency Regulations were replaced by s
    {"img": "S0513", **_P23},  # s30 The all-party committee on education produce
    {"img": "DEL", **_P24},  # s31 A Malayanisation Commission, set up in Augus
    {"img": "DEL", **_P21},  # s32 The Central Provident Fund was amended in Ma
    {"img": "S0608P2", **_P10},  # s33 In February 1956 the Assembly voted unanimou
    {"img": "DEL", **_P4},  # s34 A Free Legal Aid Bill was still under discus
    {"img": "DEL", **_P0},  # s35 The all-party delegation, thirteen strong, l
    {"img": "TALK", **_P5},  # s36 Marshall asked for full self-government by A
    {"img": "S0516", **_P25},  # s37 The sticking point was the council that woul
    {"img": "S0516", **_P26},  # s38 The British proposed equal numbers from Brit
    {"img": "S0516", **_P27},  # s39 Marshall proposed a chairman born in Singapo
    {"img": "S0516", **_P28},  # s40 The British rejected both proposals, citing 
    {"img": "S0516", **_P2},  # s41 The Straits Times of the 16th of May, in a s
    {"img": "S0516", **_P29},  # s42 Marshall made a last attempt to restart the 
    {"img": "S0608P2", **_P30},  # s43 On the 7th of June Marshall moved a motion i
    {"img": "S0608P2", **_P31},  # s44 The Liberal Socialist Party proposed an amen
    {"img": "S0608P2", **_P32},  # s45 The amendment found a single supporter outsi
    {"img": "S0608P8", **_P33},  # s46 Two hours after the Assembly rose, he submit
    {"img": "S0608P8", **_P34},  # s47 The Straits Times editorial the next day sai
    {"img": "S0608", **_P35},  # s48 On the same front page, the paper reported t
    {"img": "S0608P8", **_P36},  # s49 Lim Yew Hock became Chief Minister on the 8t
    {"img": "DEL", **_P37},  # s50 Lim Yew Hock led a delegation to London in M
    {"img": "DEL", **_P24},  # s51 The State of Singapore Act received royal as
    {"img": "B30", **_P5},  # s52 Marshall stayed in the Assembly as a backben
    {"img": "NIC", **_P5},  # s53 He lost his Cairnhill seat in 1959, won the 
    {"img": "TALK", **_P5},  # s54 From 1978 to 1993 he served as Singapore's a
    {"img": "T20", **_P5},  # s55 He died on the 12th of December 1995.
    {"img": "DEL", **_P21},  # s56 Where it fits in the bigger story: Singapore
    {"img": "DEL", **_P4},  # s57 The fourteen months before them show a first
    {"img": "S0608", **_P38},  # s58 The internal security council that failed in
]

SCHEDULE = [
    (0.0, 0), (8.35, 1), (24.725, 2), (31.8, 3), (43.575, 4),
    (51.7, 5), (63.1, 6), (70.3, 7), (90.075, 8), (102.2, 9),
    (118.375, 10), (135.85, 11), (144.6, 12), (157.025, 13), (167.1, 14),
    (173.85, 15), (183.2, 16), (189.725, 17), (206.575, 18), (212.2, 19),
    (222.25, 20), (228.55, 21), (238.125, 22), (246.4, 23), (258.4, 24),
    (275.425, 25), (279.875, 26), (287.1, 27), (301.425, 28), (305.95, 29),
    (318.475, 30), (328.0, 31), (342.475, 32), (347.75, 33), (366.125, 34),
    (376.75, 35), (387.475, 36), (397.375, 37), (402.875, 38), (411.65, 39),
    (421.425, 40), (432.675, 41), (443.925, 42), (453.65, 43), (463.975, 44),
    (476.025, 45), (486.725, 46), (492.65, 47), (507.025, 48), (515.5, 49),
    (519.85, 50), (543.55, 51), (556.625, 52), (565.1, 53), (579.7, 54),
    (588.875, 55), (593.175, 56), (602.15, 57), (617.025, 58),
]
TOTAL_DURATION = 632.6
TIMING_JSON = "audio/singapores-first-chief-minister-what-david-marshall-could-and-couldnt-do.timing.json"
