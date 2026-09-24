"""Video config for the Straits Trading Company post.

A thin Commons pool (no founder portraits, no ingot photos), so the smelter
hero repeats with different pans, alternating with the two Pulau Brani views,
the Rendezvous hotel for the "today" section, and a self-rendered timeline.

  SMELTER   - "View of Pulo Brani Tin Smelting Works", c.1890-1905
              (Rijksmuseum, CC0) - cover; an album page, so zoomed in to
              crop the page margins (zoom >= 1.5 needed: the photo spans only
              ~68% of the page width) and centred on the photo itself
  VILLAGE   - Malay village on Pulau Brani, c.1900 (KITLV, public domain)
  BRANI1910 - Pulau Brani across the water, c.1910 (KITLV, public domain)
  HOTEL     - Rendezvous Grand Hotel, Bras Basah Road (CC BY 2.0)
  TIMELINE  - rendered by scripts/render_straits_trading_timeline_chart.py

34 slides, one per sentence.
"""

_U = "https://upload.wikimedia.org/wikipedia/commons"

IMAGES = {
    "SMELTER": f"{_U}/thumb/5/56/Gezicht_op_de_tinsmelterijen_op_het_eiland_Pulau_Brani_bij_Singapore_View_of_Pulo_Brani_tin_smelting_works_%28titel_op_object%29%2C_RP-F-F01140-AH.jpg/1920px-Gezicht_op_de_tinsmelterijen_op_het_eiland_Pulau_Brani_bij_Singapore_View_of_Pulo_Brani_tin_smelting_works_%28titel_op_object%29%2C_RP-F-F01140-AH.jpg",
    "VILLAGE": f"{_U}/thumb/5/50/KITLV_-_105809_-_Lambert_%26_Co.%2C_G.R._-_Singapore_-_Malay_village_on_the_island_of_Pulau_Brani_near_Singapore_-_circa_1900.tif/lossy-page1-1920px-KITLV_-_105809_-_Lambert_%26_Co.%2C_G.R._-_Singapore_-_Malay_village_on_the_island_of_Pulau_Brani_near_Singapore_-_circa_1900.tif.jpg",
    "BRANI1910": f"{_U}/thumb/a/ad/KITLV_-_79928_-_Kleingrothe%2C_C.J._-_Medan_-_Tin_industry_at_the_island_of_Pulau_Brani%2C_Singapore_-_circa_1910.tif/lossy-page1-1920px-KITLV_-_79928_-_Kleingrothe%2C_C.J._-_Medan_-_Tin_industry_at_the_island_of_Pulau_Brani%2C_Singapore_-_circa_1910.tif.jpg",
    "HOTEL": f"{_U}/thumb/1/1f/Rendezvous_Grand_Hotel_%288645381320%29.jpg/1920px-Rendezvous_Grand_Hotel_%288645381320%29.jpg",
    "TIMELINE": "/assets/images/straits-trading-timeline-chart.png",
}

CREDITS = {
    "TIMELINE": "Chart by Lesser Known Singapore, dates per the post's own Sources list",
}

_SMA = {"type": "cover", "zoom": [1.5, 1.55, 1.6], "pan": [(0.55, 0.5)] * 3, "ease": "ease-in-out"}
_SMB = {"type": "cover", "zoom": [1.7, 1.65, 1.6], "pan": [(0.62, 0.5)] * 3, "ease": "ease-out"}
_SMC = {"type": "cover", "zoom": [1.6, 1.7, 1.8], "pan": [(0.47, 0.55)] * 3, "ease": "ease-in-out"}

_VLA = {"type": "cover", "zoom": [1.0, 1.05, 1.1], "pan": [(0.5, 0.68)] * 3, "ease": "ease-in-out"}
_VLB = {"type": "cover", "zoom": [1.1, 1.05, 1.0], "pan": [(0.3, 0.7)] * 3, "ease": "ease-out"}
_VLC = {"type": "cover", "zoom": [1.0, 1.06, 1.12], "pan": [(0.7, 0.7)] * 3, "ease": "ease-in-out"}

_BRA = {"type": "cover", "zoom": [1.0, 1.05, 1.1], "pan": [(0.6, 0.6)] * 3, "ease": "ease-in-out"}
_BRB = {"type": "cover", "zoom": [1.1, 1.05, 1.0], "pan": [(0.4, 0.6)] * 3, "ease": "ease-out"}
_BRC = {"type": "cover", "zoom": [1.0, 1.06, 1.12], "pan": [(0.8, 0.55)] * 3, "ease": "ease-in-out"}

_HTA = {"type": "cover", "zoom": [1.0, 1.05, 1.1], "pan": [(0.5, 0.5)] * 3, "ease": "ease-in-out"}
_HTB = {"type": "cover", "zoom": [1.1, 1.05, 1.0], "pan": [(0.35, 0.55)] * 3, "ease": "ease-out"}
_HTC = {"type": "cover", "zoom": [1.0, 1.06, 1.12], "pan": [(0.65, 0.55)] * 3, "ease": "ease-in-out"}

_CHART = {"type": "letterbox", "zoom": [1.0, 1.0, 1.0], "pan": [(0.5, 0.5)] * 3, "ease": "linear"}

SLIDES = [
    {"img": "SMELTER", **_SMA},  # s0  title
    {"img": "SMELTER", **_SMB},  # s1  1912 third of world's tin
    {"img": "SMELTER", **_SMC},  # s2  ingots Straits Tin purest
    {"img": "VILLAGE", **_VLA},  # s3  smelter gone, island naval base
    {"img": "BRANI1910", **_BRA},  # s4  still around, still listed
    {"img": "SMELTER", **_SMA},  # s5  1887 founders, five vessels
    {"img": "VILLAGE", **_VLB},  # s6  1890 pivot to Pulau Brani
    {"img": "SMELTER", **_SMB},  # s7  centralise smelting
    {"img": "SMELTER", **_SMC},  # s8  It worked
    {"img": "BRANI1910", **_BRB},  # s9  furnaces at scale
    {"img": "SMELTER", **_SMA},  # s10 1902 Butterworth
    {"img": "SMELTER", **_SMB},  # s11 Straits Tin ingots
    {"img": "TIMELINE", **_CHART},  # s12 1912 half world's tin
    {"img": "TIMELINE", **_CHART},  # s13 single firm two plants
    {"img": "SMELTER", **_SMC},  # s14 biggest disruption
    {"img": "SMELTER", **_SMA},  # s15 came from the British
    {"img": "BRANI1910", **_BRC},  # s16 1941 destroyed
    {"img": "SMELTER", **_SMB},  # s17 scorched earth
    {"img": "VILLAGE", **_VLA},  # s18 staff return Dec 1945
    {"img": "SMELTER", **_SMC},  # s19 smelting resumed
    {"img": "VILLAGE", **_VLB},  # s20 outlasted war two decades
    {"img": "BRANI1910", **_BRB},  # s21 late 1960s naval base
    {"img": "VILLAGE", **_VLC},  # s22 gone for good
    {"img": "TIMELINE", **_CHART},  # s23 Butterworth kept going
    {"img": "TIMELINE", **_CHART},  # s24 1982 Malaysia Smelting Corp
    {"img": "TIMELINE", **_CHART},  # s25 no longer smelting in Singapore
    {"img": "HOTEL", **_HTA},  # s26 what replaced tin
    {"img": "HOTEL", **_HTB},  # s27 diversified, 1997 hotels
    {"img": "HOTEL", **_HTC},  # s28 2008 Tecity
    {"img": "HOTEL", **_HTA},  # s29 three divisions
    {"img": "HOTEL", **_HTB},  # s30 SGX-listed, S$218.4m
    {"img": "TIMELINE", **_CHART},  # s31 bigger story
    {"img": "SMELTER", **_SMA},  # s32 survived demolition
    {"img": "SMELTER", **_SMB},  # s33 few firms still trading
]

SCHEDULE = [
    (0.0, 0), (3.95, 1), (15.125, 2), (22.35, 3), (33.075, 4),
    (42.775, 5), (70.2, 6), (82.875, 7), (100.525, 8), (101.975, 9),
    (110.625, 10), (118.25, 11), (134.4, 12), (145.375, 13), (156.15, 14),
    (162.025, 15), (164.85, 16), (181.225, 17), (185.35, 18), (202.75, 19),
    (220.725, 20), (226.05, 21), (238.925, 22), (248.8, 23), (252.85, 24),
    (264.825, 25), (276.325, 26), (280.225, 27), (295.25, 28), (306.375, 29),
    (329.3, 30), (343.125, 31), (364.525, 32), (382.35, 33),
]
TOTAL_DURATION = 392.125
TIMING_JSON = "audio/the-company-that-outlived-its-own-tin-smelter.timing.json"
