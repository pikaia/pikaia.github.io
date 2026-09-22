"""Video config for the Lim Peng Siang post.

Five images, a genuinely thin Commons pool (no photographs of Lim
himself beyond the one 1923 book portrait, and none at all of Ho Hong's
mills, ships or banks), so the two landscape harbour photos and the two
portrait-oriented scans repeat with different pans/variants throughout.

  PORTRAIT  - Lim Peng Siang, from Song Ong Siang's 1923 book (Commons,
              CC BY-SA 4.0) - letterbox, small
  COVER     - the 1923 book's own cover (Commons, public domain) -
              letterbox, small
  BOATQUAY  - the Boat Quay, Singapore, c. 1890-1910 (Rijksmuseum,
              CC0, high-res) - cover, three pans
  SHIPYARD  - the Tanjong Rhu shipyard, 1932 (Commons, public domain,
              NLB-watermarked scan) - letterbox, grainy/small
  AMOY      - Amoy town and harbour, 1874 (Wellcome Collection,
              CC BY 4.0) - cover, gallery-only in the post itself,
              used here for variety
  WEEBIN    - Wee Bin, Lim's maternal grandfather, from the same 1923
              book (Commons, CC BY-SA 4.0) - letterbox, small

42 slides, 453.825s.
"""

_U = "https://upload.wikimedia.org/wikipedia/commons"

IMAGES = {
    "PORTRAIT": f"{_U}/1/1c/Lim_Peng_Siang.png",
    "COVER": f"{_U}/1/1f/One_Hundred_Years%27_History_of_the_Chinese_in_Singapore.png",
    "BOATQUAY": f"{_U}/thumb/f/fe/Binnenhaven_van_Singapore_The_boat_quay_Singapore_%28titel_op_object%29%2C_RP-F-00-5018-39.jpg/1920px-Binnenhaven_van_Singapore_The_boat_quay_Singapore_%28titel_op_object%29%2C_RP-F-00-5018-39.jpg",
    "SHIPYARD": f"{_U}/8/85/Tanjong_Rhu_shipyard_in_1932.png",
    "AMOY": f"{_U}/thumb/e/e8/Amoy_town_and_harbour_seen_from_Kalangsu_Wellcome_L0034288.jpg/1920px-Amoy_town_and_harbour_seen_from_Kalangsu_Wellcome_L0034288.jpg",
    "WEEBIN": f"{_U}/e/ee/Wee_Bin.jpg",
}

_LTBA = {"type": "letterbox", "zoom": [1.0, 1.04, 1.08], "pan": [(0.5, 0.5)] * 3, "ease": "ease-in-out"}
_LTBB = {"type": "letterbox", "zoom": [1.08, 1.04, 1.0], "pan": [(0.5, 0.5)] * 3, "ease": "ease-out"}

_CVA = {"type": "cover", "zoom": [1.0, 1.05, 1.1], "pan": [(0.5, 0.42)] * 3, "ease": "ease-in-out"}
_CVB = {"type": "cover", "zoom": [1.12, 1.06, 1.0], "pan": [(0.35, 0.45)] * 3, "ease": "ease-out"}
_CVC = {"type": "cover", "zoom": [1.0, 1.06, 1.12], "pan": [(0.65, 0.45)] * 3, "ease": "ease-in-out"}

SLIDES = [
    {"img": "BOATQUAY", **_CVA}, # s0  title
    {"img": "BOATQUAY", **_CVB}, # s1  1936 greatest magnates
    {"img": "AMOY", **_CVA},     # s2  rice mill and oil mill into a group
    {"img": "COVER", **_LTBA},   # s3  today almost unknown
    {"img": "AMOY", **_CVB},     # s4  born Amoy 1872
    {"img": "WEEBIN", **_LTBA},  # s5  mother daughter of Wee Bin
    {"img": "BOATQUAY", **_CVC}, # s6  family already deep in shipping
    {"img": "PORTRAIT", **_LTBB}, # s7  his own start smaller
    {"img": "PORTRAIT", **_LTBA}, # s8  1904 Ho Hong Co, $50,000 loan
    {"img": "BOATQUAY", **_CVA}, # s9  rice mill / oil mill capacity
    {"img": "AMOY", **_CVA},     # s10 modest industrial beginning
    {"img": "WEEBIN", **_LTBA},  # s11 that name mattered more
    {"img": "WEEBIN", **_LTBB},  # s12 1911 Wee Bin liquidated
    {"img": "WEEBIN", **_LTBA},  # s13 public auction, four steamships
    {"img": "SHIPYARD", **_LTBB}, # s14 Ho Hong Steamship Co, 14 ships by 1926
    {"img": "BOATQUAY", **_CVB}, # s15 buying a bankrupt rival's ships
    {"img": "WEEBIN", **_LTBB},  # s16 founded by his own grandfather
    {"img": "BOATQUAY", **_CVC}, # s17 Ho Hong kept adding pieces
    {"img": "PORTRAIT", **_LTBB}, # s18 Chinese Commercial Bank, Ho Hong Bank
    {"img": "COVER", **_LTBA},   # s19 Ho Hong Bank paid-up capital
    {"img": "AMOY", **_CVB},     # s20 cement works Ulu Pandan
    {"img": "BOATQUAY", **_CVA}, # s21 unusual combination
    {"img": "COVER", **_LTBB},   # s22 2023 study, industrialisation
    {"img": "PORTRAIT", **_LTBA}, # s23 standing grew alongside it
    {"img": "PORTRAIT", **_LTBB}, # s24 Chamber, Advisory Board, Fujian Chamber
    {"img": "COVER", **_LTBA},   # s25 JP, declined Legislative Council
    {"img": "BOATQUAY", **_CVB}, # s26 WWI fighter plane donation
    {"img": "AMOY", **_CVA},     # s27 Malaya No. 6, Choon Guan Peng Siang
    {"img": "PORTRAIT", **_LTBA}, # s28 Sunday paper, 1936
    {"img": "BOATQUAY", **_CVC}, # s29 Depression broke the momentum
    {"img": "SHIPYARD", **_LTBA}, # s30 shipping sold, mills, cement closed
    {"img": "COVER", **_LTBB},   # s31 heavier blow came from banking
    {"img": "COVER", **_LTBA},   # s32 31 Oct 1932, merger into OCBC
    {"img": "AMOY", **_CVB},     # s33 remembered as Tan Ean Kiam, Lee Kong Chian
    {"img": "PORTRAIT", **_LTBB}, # s34 Lim not part of that story
    {"img": "COVER", **_LTBA},   # s35 profiled in 1923 book
    {"img": "COVER", **_LTBB},   # s36 record + 1936 profile
    {"img": "PORTRAIT", **_LTBA}, # s37 less scholarly attention
    {"img": "BOATQUAY", **_CVA}, # s38 died 21 March 1944
    {"img": "SHIPYARD", **_LTBB}, # s39 Peng Siang Quay
    {"img": "BOATQUAY", **_CVB}, # s40 why it matters today
    {"img": "PORTRAIT", **_LTBA}, # s41 nobody today could tell you his name
]

SCHEDULE = [
    (0.0, 0), (4.9, 1), (14.925, 2), (26.925, 3), (34.8, 4),
    (44.85, 5), (58.675, 6), (67.65, 7), (70.975, 8), (82.25, 9),
    (96.7, 10), (105.85, 11), (110.0, 12), (118.3, 13), (131.075, 14),
    (148.25, 15), (158.475, 16), (163.65, 17), (168.1, 18), (187.6, 19),
    (194.5, 20), (206.75, 21), (221.5, 22), (239.225, 23), (243.2, 24),
    (263.975, 25), (272.85, 26), (281.625, 27), (293.475, 28), (304.625, 29),
    (307.6, 30), (326.925, 31), (329.925, 32), (347.35, 33), (359.4, 34),
    (368.375, 35), (380.775, 36), (389.35, 37), (407.025, 38), (415.55, 39),
    (425.55, 40), (443.15, 41),
]
TOTAL_DURATION = 453.825
TIMING_JSON = "audio/lim-peng-siang-the-man-singapore-called-its-greatest-magnate.timing.json"
