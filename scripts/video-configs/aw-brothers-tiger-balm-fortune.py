"""Video config for "The Ointment Outlasted the Empire It Paid For" -
Watch widget and main video.

Three diagrams as near-static slides with CREDITS lines: the OSM
headquarters-and-park map (render_aw_brothers_hq_park_map.py), the
empire timeline chart (render_aw_brothers_timeline_chart.py) and the
FY2025 income-streams chart (render_aw_brothers_money_chart.py). The two
charts mirror the post's inline SVGs; compose_chart_frame() only
animates a calendar-year line, so they are pre-rendered PNGs shown
static (zoom held at 1.0 so nothing is cropped) while the narration
walks through them.

This is a person-and-fortune story with little freely-licensed
photography, so the two Aw Boon Haw portraits, the 1971 Tiger Balm
shots, the Neil Road building and the Haw Par Villa images each recur
several times, re-triggering a fresh slow zoom. 14 image assets
(3 captioned in the post, 8 in the gallery, 3 originals with CREDITS),
so stage_youtube_text.py resolves every credit.

Chart slides are cover + zoom [1,1,1] (deliberately frozen); the rest
mix cover pans and letterbox zooms. Letterbox + zero pan and a held
chart both read JERKY in --check-only - the documented false positives
(pipeline section 5). Longest hold ~25s (a single 25s narration
sentence); gap report clean.

43 slides, 554.8s.
"""

_C = "https://upload.wikimedia.org/wikipedia/commons"

IMAGES = {
    "HELL": f"{_C}/c/c2/Entrance_to_the_Ten_Courts_of_Hell_%EF%BC%88%E5%8D%81%E6%AE%BF%E9%98%8E%E7%BD%97%EF%BC%89%2C_Haw_Par_Villa_%2814791602374%29.jpg",
    "HELL8": f"{_C}/0/0b/Eighth_Court_of_Hell_%E2%80%93_Yama_King_Dushi%2C_Haw_Par_Villa_%2814793981305%29.jpg",
    "HPV2004": f"{_C}/0/05/Haw_Par_Villa%2C_Singapore_%283327855083%29.jpg",
    "HPVOLD": f"{_C}/thumb/b/b6/D_100_View_of_Haw_Par_Villa._S_%27pore.%2C_KITLV_1404806.tiff/lossy-page1-1280px-D_100_View_of_Haw_Par_Villa._S_%27pore.%2C_KITLV_1404806.tiff.jpg",
    "GARDEN71": f"{_C}/f/fd/161a_Tiger_Balm_Garden_Singapore_1971_%2851253058784%29.jpg",
    "SIGN71": f"{_C}/f/fb/71-528a_Tiger_Balm%2C_Singapore_1971_%2851251929204%29.jpg",
    "ENGAUNTONG": f"{_C}/b/bf/89_Neil_Road%2C_Singapore_%282025%29_-_img_04.jpg",
    "PORTRAIT": f"{_C}/8/87/Hu_Wenhu.jpg",
    "PORTRAIT2": f"{_C}/f/f9/Hu_Wenhu2.jpg",
    "TIGERCAR": f"{_C}/3/3b/TigerCar-HawParVilla-Singapore-20081115.jpg",
    "SINCHEW": f"{_C}/c/c2/Sin_Chew_Jit_Poh_1.JPG",
    "MAP": "/assets/images/aw-brothers-hq-park-map.png",
    "TIMELINE": "/assets/images/aw-brothers-timeline-chart.png",
    "MONEY": "/assets/images/aw-brothers-money-chart.png",
}

CREDITS = {
    "MAP": "Map by Lesser Known Singapore; base map data © OpenStreetMap contributors",
    "TIMELINE": "Chart by Lesser Known Singapore",
    "MONEY": "Chart by Lesser Known Singapore",
}

_LBI = {"type": "letterbox", "zoom": [1, 1.05, 1.10], "pan": [(0.5, 0.5)] * 3, "ease": "ease-in-out"}
_LBO = {"type": "letterbox", "zoom": [1.10, 1.05, 1], "pan": [(0.5, 0.5)] * 3, "ease": "ease-out"}
_LBW = {"type": "letterbox", "zoom": [1, 1.06, 1.12], "pan": [(0.5, 0.5)] * 3, "ease": "ease-in-out"}
_MAPMOVE = {"type": "letterbox", "zoom": [1, 1.03, 1.05], "pan": [(0.5, 0.5)] * 3, "ease": "linear"}
_CVL = {"type": "cover", "zoom": [1.06, 1.06, 1.06], "pan": [(0.15, 0.5), (0.5, 0.5), (0.85, 0.5)], "ease": "ease-in-out"}
_CVR = {"type": "cover", "zoom": [1.06, 1.06, 1.06], "pan": [(0.85, 0.5), (0.5, 0.5), (0.15, 0.5)], "ease": "ease-in-out"}
_CVZ = {"type": "cover", "zoom": [1.0, 1.06, 1.12], "pan": [(0.5, 0.5)] * 3, "ease": "ease-in-out"}
_CHART = {"type": "cover", "zoom": [1.0, 1.0, 1.0], "pan": [(0.5, 0.5)] * 3, "ease": "linear"}

SLIDES = [
    {"img": "HELL", **_CVZ},          # 0
    {"img": "SIGN71", **_LBI},        # 1
    {"img": "HPV2004", **_LBI},       # 2
    {"img": "PORTRAIT2", **_LBI},     # 3
    {"img": "PORTRAIT", **_LBW},      # 4
    {"img": "PORTRAIT2", **_LBO},     # 5
    {"img": "SIGN71", **_LBW},        # 6
    {"img": "PORTRAIT", **_LBI},      # 7
    {"img": "PORTRAIT2", **_LBW},     # 8
    {"img": "MAP", **_MAPMOVE},       # 9
    {"img": "ENGAUNTONG", **_LBI},    # 10
    {"img": "SIGN71", **_LBO},        # 11
    {"img": "TIGERCAR", **_LBI},      # 12
    {"img": "TIGERCAR", **_LBW},      # 13
    {"img": "SINCHEW", **_LBI},       # 14
    {"img": "SINCHEW", **_LBW},       # 15
    {"img": "ENGAUNTONG", **_LBW},    # 16
    {"img": "GARDEN71", **_CVL},      # 17
    {"img": "PORTRAIT", **_LBI},      # 18
    {"img": "PORTRAIT2", **_LBI},     # 19
    {"img": "PORTRAIT2", **_LBW},     # 20
    {"img": "PORTRAIT", **_LBO},      # 21
    {"img": "MAP", **_MAPMOVE},       # 22
    {"img": "HPVOLD", **_CVZ},        # 23
    {"img": "HPV2004", **_LBI},       # 24
    {"img": "HELL8", **_CVL},         # 25
    {"img": "HELL", **_CVR},          # 26
    {"img": "HPVOLD", **_CVR},        # 27
    {"img": "PORTRAIT", **_LBI},      # 28
    {"img": "PORTRAIT2", **_LBW},     # 29
    {"img": "TIMELINE", **_CHART},    # 30
    {"img": "TIMELINE", **_CHART},    # 31
    {"img": "TIMELINE", **_CHART},    # 32
    {"img": "TIMELINE", **_CHART},    # 33
    {"img": "TIMELINE", **_CHART},    # 34
    {"img": "SINCHEW", **_LBI},       # 35
    {"img": "ENGAUNTONG", **_LBO},    # 36
    {"img": "HPV2004", **_LBW},       # 37
    {"img": "MONEY", **_CHART},       # 38
    {"img": "MONEY", **_CHART},       # 39
    {"img": "MONEY", **_CHART},       # 40
    {"img": "MAP", **_MAPMOVE},       # 41
    {"img": "HELL", **_CVZ},          # 42
]

# Real values from audio/aw-brothers-tiger-balm-fortune.timing.json.
# Every point is a real sentence start; slide index runs 0..42 in order.
#   0  s0-1   title; the leaping-tiger jar in your home / at the pharmacy
#   1  s2     sold in 100+ countries, at a US drugstore as at a Singapore shop
#   2  s3     the last everyday trace of a fortune that ran papers and a bank
#   3  s4     Rangoon; Aw Chu Kin, Eng Aun Tong, ~1870
#   4  s5     two sons - Boon Haw (1882), Boon Par (1888)
#   5  s6     father dies 1908; they inherit the shop and the recipes
#   6  s7     refined the ointment, the hexagonal jars, named it Tiger Balm
#   7  s8-9   the division of labour; Boon Par the quiet one, the factory
#   8  s10-11 Boon Haw the salesman; by 1920 among the richest in Rangoon
#   9  s12    1926 - HQ and factory move to Singapore, eye on China
#   10 s13-14 the Neil Road plant, 10x Rangoon; the building still stands
#   11 s15-16 what set it apart was advertising - bought space, free samples
#   12 s17    the "tiger cars" - stripes, a tiger's head, a roaring horn
#   13 s18    the leaping-tiger trademark on every jar, wall, masthead
#   14 s19    the ointment threw off enough cash for a conglomerate
#   15 s20    1929 Sin Chew Jit Poh; ~17 papers to 1951; Sing Tao, Tiger Standard
#   16 s21    1950 - Chung Khiaw Bank, Robinson Road, Boon Haw first chairman
#   17 s22    rubber, property, and for a time Coney Island
#   18 s23-24 serious philanthropy - >$1m, schools, hospitals, China war relief
#   19 s25    his Occupation record is more contested
#   20 s26    the war in Hong Kong, meetings, later accusations; and defenders
#   21 s27    both readings argued ever since
#   22 s28    1935 - a seafront hill on Pasir Panjang Road, away from town
#   23 s29    Ho Kwong Yew's Art Deco villa, 1937, for the homesick brother
#   24 s30    the free garden - painted statues, folklore, morality
#   25 s31    the set piece: the Ten Courts of Hell
#   26 s32    sister gardens in Hong Kong and Fujian
#   27 s33-34 the war on the hill - a lookout, the villa bombed then demolished
#   28 s35    Boon Par back to Rangoon, died 1944
#   29 s36-37 Boon Haw kept adding until his death in Honolulu, 1954; he was 72
#   30 s38-39 how a fortune comes apart; 1969 - the listed company
#   31 s40    within two years, sold to Slater Walker; Aw Cheng Chye dies
#   32 s41    Slater Walker breaks it up - Chung Khiaw to UOB, papers sold, Jurong
#   33 s42    1975 - the share-rigging allegations, the failed extradition
#   34 s43-44 Wee Cho Yaw chairman from 1978; now Haw Par Corporation
#   35 s45-46 the other pieces - Sin Chew's last issue 1983, into Lianhe Zaobao
#   36 s47    the Neil Road building conserved, 1992
#   37 s48    Haw Par Villa - state takeover, Dragon World's losses, free again 1998
#   38 s49-50 Haw Par Corp today - Tiger Balm nearly all revenue, 100+ countries
#   39 s51-52 but most profit is UOB/UOL dividends on decades-old shareholdings
#   40 s53    in effect, an ointment brand wrapped around a bank shareholding
#   41 s54    where it fits - built and run from Singapore, then scattered
#   42 s55    three fragments still in plain sight - jar, masthead, the demons
SCHEDULE = [
    (0.0, 0), (14.65, 1), (25.02, 2), (41.23, 3), (57.15, 4),
    (68.65, 5), (82.45, 6), (91.80, 7), (101.65, 8), (116.00, 9),
    (125.72, 10), (145.38, 11), (159.50, 12), (177.03, 13), (186.57, 14),
    (190.90, 15), (211.70, 16), (218.68, 17), (225.18, 18), (243.60, 19),
    (249.38, 20), (269.02, 21), (272.52, 22), (283.40, 23), (292.77, 24),
    (305.48, 25), (313.07, 26), (319.65, 27), (333.68, 28), (339.48, 29),
    (353.20, 30), (366.60, 31), (380.65, 32), (399.00, 33), (415.57, 34),
    (428.73, 35), (446.62, 36), (453.32, 37), (478.45, 38), (498.77, 39),
    (518.95, 40), (526.35, 41), (540.45, 42),
]
TOTAL_DURATION = 554.8
TIMING_JSON = "audio/aw-brothers-tiger-balm-fortune.timing.json"
