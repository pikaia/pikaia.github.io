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
  HOHONGBANK - Ho Hong Bank's own building, its name visible over the
              door, in the background of a 1929 street-paving photo in
              Batavia (Commons, public domain, Chris's own find) -
              letterbox, the sign is small in frame
  CCBANK    - The Singapore Free Press, 1 July 1929, page 4 (whole
              page, local scan, NewspaperSG / SPH, public domain by
              age), reporting the Chinese Commercial Bank's Chulia
              Street rebuild alongside the Oversea-Chinese Bank -
              letterbox

44 slides, 488.75s.
"""

_U = "https://upload.wikimedia.org/wikipedia/commons"

IMAGES = {
    "PORTRAIT": f"{_U}/1/1c/Lim_Peng_Siang.png",
    "COVER": f"{_U}/1/1f/One_Hundred_Years%27_History_of_the_Chinese_in_Singapore.png",
    "BOATQUAY": f"{_U}/thumb/f/fe/Binnenhaven_van_Singapore_The_boat_quay_Singapore_%28titel_op_object%29%2C_RP-F-00-5018-39.jpg/1920px-Binnenhaven_van_Singapore_The_boat_quay_Singapore_%28titel_op_object%29%2C_RP-F-00-5018-39.jpg",
    "SHIPYARD": f"{_U}/8/85/Tanjong_Rhu_shipyard_in_1932.png",
    "AMOY": f"{_U}/thumb/e/e8/Amoy_town_and_harbour_seen_from_Kalangsu_Wellcome_L0034288.jpg/1920px-Amoy_town_and_harbour_seen_from_Kalangsu_Wellcome_L0034288.jpg",
    "WEEBIN": f"{_U}/e/ee/Wee_Bin.jpg",
    "HOHONGBANK": f"{_U}/8/85/Collectie_NMvWereldculturen%2C_TM-60032202%2C_Foto%2C_%27Asfaltering_van_het_stationsplein_bij_het_in_aanbouw_zijnde_spoorwegstation_Kota%2C_Batavia%27%2C_fotograaf_onbekend%2C_1929.jpg",
    "CCBANK": "/assets/images/singapore-free-press-1929-07-01-page-4.jpg",
}

_LTBA = {"type": "letterbox", "zoom": [1.0, 1.04, 1.08], "pan": [(0.5, 0.5)] * 3, "ease": "ease-in-out"}
_LTBB = {"type": "letterbox", "zoom": [1.08, 1.04, 1.0], "pan": [(0.5, 0.5)] * 3, "ease": "ease-out"}

_CVA = {"type": "cover", "zoom": [1.0, 1.05, 1.1], "pan": [(0.5, 0.42)] * 3, "ease": "ease-in-out"}
_CVB = {"type": "cover", "zoom": [1.12, 1.06, 1.0], "pan": [(0.35, 0.45)] * 3, "ease": "ease-out"}
_CVC = {"type": "cover", "zoom": [1.0, 1.06, 1.12], "pan": [(0.65, 0.45)] * 3, "ease": "ease-in-out"}

# CCBANK is the one whole-page ST/SFP scan in this post. A whole page shown
# via letterbox (the usual choice for a portrait scan) is too small to read
# at all, and the point of a whole-page image is compliance for the hosted
# asset, not that every part of the page must stay visible on screen - so
# these two slides use "cover" instead, with a real pan/zoom that reveals
# the actual "New Bank Building" article over the two slides' combined
# dwell time (checked by rendering test frames with cover_crop() directly,
# not guessed from pixel math). The source file in assets/images/ is still
# the untouched whole page.
#
# zoom=1.4, pan=(1.0, 0.08) is the target framing (Chris, 2026-09-22): the
# headline text and the full building illustration both fit in frame
# together at that zoom/pan, with the masthead's blank margin above the
# headline cropped off. Tighter zoom (~2.4) can show either the headline
# or the illustration well but not both - the article's own proportions
# (tall and narrow) don't fit a 16:9 frame at a legible tight crop.
_CCBANK1 = {"type": "cover", "zoom": [1.15, 1.3, 1.4], "pan": [(0.65, 0.15), (0.9, 0.1), (1.0, 0.08)], "ease": "ease-in-out"}
_CCBANK2 = {"type": "cover", "zoom": [1.4, 1.45, 1.5], "pan": [(1.0, 0.08), (1.0, 0.15), (1.0, 0.22)], "ease": "ease-in-out"}

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
    {"img": "HOHONGBANK", **_LTBA}, # s18 Chinese Commercial Bank, Ho Hong Bank
    {"img": "HOHONGBANK", **_LTBB}, # s19 Ho Hong Bank paid-up capital, Batavia/Palembang
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
    {"img": "CCBANK", **_CCBANK1}, # s32 1929 Chulia Street rebuild
    {"img": "CCBANK", **_CCBANK2}, # s33 modernising for the same future
    {"img": "COVER", **_LTBA},   # s34 31 Oct 1932, merger into OCBC
    {"img": "AMOY", **_CVB},     # s35 remembered as Tan Ean Kiam, Lee Kong Chian
    {"img": "PORTRAIT", **_LTBB}, # s36 Lim not part of that story
    {"img": "COVER", **_LTBA},   # s37 profiled in 1923 book
    {"img": "COVER", **_LTBB},   # s38 record + 1936 profile
    {"img": "PORTRAIT", **_LTBA}, # s39 less scholarly attention
    {"img": "BOATQUAY", **_CVA}, # s40 died 21 March 1944
    {"img": "SHIPYARD", **_LTBB}, # s41 Peng Siang Quay
    {"img": "BOATQUAY", **_CVB}, # s42 why it matters today
    {"img": "PORTRAIT", **_LTBA}, # s43 nobody today could tell you his name
]

SCHEDULE = [
    (0.0, 0), (4.9, 1), (14.925, 2), (26.925, 3), (34.8, 4),
    (44.85, 5), (58.675, 6), (67.65, 7), (70.975, 8), (82.25, 9),
    (96.7, 10), (105.85, 11), (110.0, 12), (118.3, 13), (131.075, 14),
    (148.25, 15), (158.475, 16), (163.65, 17), (168.1, 18), (187.6, 19),
    (203.45, 20), (215.7, 21), (230.45, 22), (248.175, 23), (252.15, 24),
    (272.925, 25), (281.8, 26), (290.575, 27), (302.425, 28), (313.575, 29),
    (316.55, 30), (335.875, 31), (338.875, 32), (356.275, 33), (364.85, 34),
    (382.275, 35), (394.325, 36), (403.3, 37), (415.7, 38), (424.275, 39),
    (441.95, 40), (450.475, 41), (460.475, 42), (478.075, 43),
]
TOTAL_DURATION = 488.75
TIMING_JSON = "audio/lim-peng-siang-the-man-singapore-called-its-greatest-magnate.timing.json"
