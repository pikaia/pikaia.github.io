"""Video config for the Straits dollar post.

The Straits Times of 30 January 1906 (page 5) is pushed in on its "EXCHANGE"
report, top left, for the opening and again for the £100,000 episode. The
coins and notes (letterbox) carry the money itself: the 1903, 1904 and 1907
dollars, the British trade dollar, the Mexican dollar it replaced, the gold
sovereign and three Straits notes. The value chart (letterbox, frozen) takes
the fall of silver. The 1900s waterfront of banks fills the merchants'
argument. Portraits only under sentences naming that person: Anderson and Lim
Kim San. Tan Keong Saik, Tan Jiak Kim and Sir David Barbour have no free
photos here, so their sentences show places or coins.

34 slides, 557.175s. AVATAR: first and last 30s, cartoon with motion.
"""

_U = "https://upload.wikimedia.org/wikipedia/commons"
_C = f"{_U}/thumb"
_A = "/assets/images"

IMAGES = {
    "HERO": f"{_C}/e/ee/1_dollar_of_Straits_Settlements%2C_Edward_VII_-_1903_B.png/1280px-1_dollar_of_Straits_Settlements%2C_Edward_VII_-_1903_B.png",
    "D1903B": f"{_U}/e/ef/Straits_settlements-1Dollar-1903.jpg",
    "D1904R": f"{_C}/6/69/Straits_Settlements%2C_One_Dollar%2C_Edward_VII%2C_1904%2C_-_reverse.jpg/1280px-Straits_Settlements%2C_One_Dollar%2C_Edward_VII%2C_1904%2C_-_reverse.jpg",
    "D1907": f"{_C}/b/b8/1_dollar_of_Straits_Settlements_-_Edward_VII_1907.png/1280px-1_dollar_of_Straits_Settlements_-_Edward_VII_1907.png",
    "TRADE": f"{_U}/5/59/Great_Britain_Trade_Dollar_1895.jpg",
    "MEX": f"{_C}/3/33/1888_M%C3%A9xico_8_Reals_Trade_Coin_Silver.jpg/1280px-1888_M%C3%A9xico_8_Reals_Trade_Coin_Silver.jpg",
    "SOV": f"{_C}/b/b1/Edward_VII_sovereign_MET_DP100405.jpg/1280px-Edward_VII_sovereign_MET_DP100405.jpg",
    "NOTE50": f"{_U}/0/02/Straits_Setlements_-_1911_-_%2450_banknote.jpg",
    "NOTE10": f"{_U}/3/33/Straits_Settlements_-_1927_-_%2410_banknote.jpg",
    "NOTE1": f"{_U}/a/aa/Straits_Settlements_-_1935_-_%241_banknote_%28obverse%29.jpg",
    "SWETT": f"{_U}/1/1c/Sir_Frank_Swettenham_by_John_Singer_Sargent_1904.jpg",
    "ANDERSON": f"{_U}/4/4a/Sir_john_anderson.gif",
    "COLLYER": f"{_U}/5/53/Collyer_Quay%2C_Singapore_1900s.jpg",
    "HSBC": f"{_C}/1/13/KITLV_-_50198_-_Lambert_%26_Co.%2C_G.R._-_Singapore_-_Building_of_the_Hong_Kong_and_Shanghai_Bank_in_Singapore_-_circa_1900.tif/lossy-page1-1920px-KITLV_-_50198_-_Lambert_%26_Co.%2C_G.R._-_Singapore_-_Building_of_the_Hong_Kong_and_Shanghai_Bank_in_Singapore_-_circa_1900.tif.jpg",
    "JOHNSTON": f"{_C}/1/1e/KITLV_-_1404900_-_Johnston%27s_Pier_and_H._M._Bank._Singapore_-_1895-1906.tif/lossy-page1-1920px-KITLV_-_1404900_-_Johnston%27s_Pier_and_H._M._Bank._Singapore_-_1895-1906.tif.jpg",
    "RAFFLESSQ": f"{_U}/4/44/Photographic_Views_of_Singapore_Plate_03_Raffles%27_Square.jpg",
    "ST1906": f"{_A}/straits-times-1906-01-30-page-5.jpg",
    "CHART": f"{_A}/straits-dollar-value-chart.png",
    # Not in this post's captions (credited below):
    "HSBCPLATE": f"{_U}/8/81/Photographic_Views_of_Singapore_Plate_05_Hongkong_and_Shanghai_Bank.jpg",
    "LIM": f"{_U}/b/b8/Lim_Kim_San_in_the_1940s.jpg",
    "MAS": f"{_U}/0/09/MASBuilding-Singapore-20090914.jpg",
}

# Credits for images not captioned in the post or its gallery.
CREDITS = {
    "CHART": "Chart by Lesser Known Singapore, figures from One Hundred Years of Singapore (1921)",
    "HSBCPLATE": "The Hongkong and Shanghai Bank by the Singapore River, about 1900, G. R. Lambert and Co., public domain, via Wikimedia Commons",
    "LIM": "Lim Kim San in the 1940s, National Archives of Singapore, public domain, via Wikimedia Commons",
    "MAS": "The MAS Building, Singapore, 2009, Nicolas Lannuzel, CC BY-SA 2.0, via Wikimedia Commons",
}

_E = "ease-in-out"
_IN = {"type": "cover", "zoom": [1.0, 1.06, 1.12], "pan": [(0.5, 0.5)] * 3, "ease": _E}
_OUT = {"type": "cover", "zoom": [1.12, 1.06, 1.0], "pan": [(0.5, 0.5)] * 3, "ease": _E}
# Coins, notes, small scans and tall portraits: letterbox, modest zoom (no zoom on grainy photos).
_PORT = {"type": "letterbox", "zoom": [1.0, 1.04, 1.08], "pan": [(0.5, 0.5)] * 3, "ease": _E}
_PORT_OUT = {"type": "letterbox", "zoom": [1.08, 1.04, 1.0], "pan": [(0.5, 0.5)] * 3, "ease": _E}
# The chart: letterbox, frozen.
_GFX = {"type": "letterbox", "zoom": [1, 1, 1], "pan": [(0.5, 0.5)] * 3}


def _c(zoom, pan):
    return {"type": "cover", "zoom": zoom, "pan": pan, "ease": _E}


# Whole-page newspaper push-ins (1600x2121 page), zoom capped at 2.4x.
_ST_HEAD = _c([2.0, 2.1, 2.2], [(0.0, 0.018), (0.0, 0.03), (0.0, 0.042)])     # EXCHANGE and the headline, top left
_ST_COL = _c([2.2, 2.3, 2.4], [(0.0, 0.227), (0.0, 0.255), (0.0, 0.281)])     # the report on the £100,000
_ST_PAGE = _c([1.0, 1.04, 1.08], [(0.5, 0.0), (0.5, 0.04), (0.5, 0.08)])

SLIDES = [
    {"img": "HERO", **_PORT},           # 0  s0      title
    {"img": "ST1906", **_ST_HEAD},      # 1  s1      29 January 1906: fixed at 2s 4d
    {"img": "ST1906", **_ST_COL},       # 2  s2      the headline; "a most painful sensation"
    {"img": "ST1906", **_ST_PAGE},      # 3  s3      what the day settled
    {"img": "D1903B", **_PORT},         # 4  s4      a dollar of its own
    {"img": "MEX", **_PORT},            # 5  s5-6    Spanish, then Mexican dollars
    {"img": "TRADE", **_PORT},          # 6  s7      the 1895 British trade dollar
    {"img": "HSBC", **_IN},             # 7  s8      banks' own notes
    {"img": "SOV", **_PORT},            # 8  s9-10   silver against gold
    {"img": "CHART", **_GFX},           # 9  s11-12  4s 6d, 2s 7d, 1s 6d
    {"img": "COLLYER", **_IN},          # 10 s13     paid in dollars, owing in sterling
    {"img": "RAFFLESSQ", **_IN},        # 11 s14-16  the Chamber of Commerce
    {"img": "JOHNSTON", **_IN},         # 12 s17-18  the counter-petition
    {"img": "CHART", **_GFX},           # 13 s19     "cheap dollars"
    {"img": "HSBCPLATE", **_IN},        # 14 s20-21  Tan Keong Saik (no photo); minds changed
    {"img": "NOTE50", **_PORT},         # 15 s22-23  the currency board and its notes
    {"img": "D1904R", **_PORT},         # 16 s24-25  the Barbour committee's new dollar (no photo of Barbour)
    {"img": "SWETT", **_PORT},          # 17 s26     the plan adopted, 29 May 1903
    {"img": "COLLYER", **_OUT},         # 18 s27     Tan Jiak Kim's pledge (no photo)
    {"img": "HERO", **_PORT_OUT},       # 19 s28-29  the new dollars arrive; counterfeits
    {"img": "MEX", **_PORT_OUT},        # 20 s30-31  recoinage; the old dollars demonetised
    {"img": "ANDERSON", **_PORT},       # 21 s32-33  fixed under Governor Anderson
    {"img": "ST1906", **_ST_COL},       # 22 s34-35  the £100,000 episode
    {"img": "SOV", **_PORT_OUT},        # 23 s36-37  $60 in notes for £7 in gold
    {"img": "NOTE10", **_PORT},         # 24 s38-39  the reserves behind the notes
    {"img": "D1907", **_PORT},          # 25 s40-42  silver rises; the smaller dollar
    {"img": "HSBC", **_OUT},            # 26 s43     a run on the Currency Commissioners
    {"img": "JOHNSTON", **_OUT},        # 27 s44-45  was 2s 4d too high?
    {"img": "NOTE1", **_PORT},          # 28 s46     to the Malayan dollar
    {"img": "LIM", **_PORT},            # 29 s47     Singapore's own board, 1967, Lim Kim San
    {"img": "RAFFLESSQ", **_OUT},       # 30 s48-49  the old principle kept
    {"img": "MAS", **_PORT},            # 31 s50-51  merged into MAS, 2002
    {"img": "HSBCPLATE", **_OUT},       # 32 s52-54  interchangeable with Brunei; the promise kept
    {"img": "HERO", **{**_PORT, "zoom": [1.0, 1.06, 1.12]}},  # 33 s55  why it matters
]

SCHEDULE = [
    (0.0, 0), (5.05, 1), (17.625, 2), (34.7, 3), (38.75, 4), (54.675, 5), (72.2, 6), (84.7, 7),
    (89.55, 8), (104.125, 9), (126.725, 10), (141.15, 11), (165.15, 12), (185.4, 13), (200.075, 14),
    (216.6, 15), (236.6, 16), (258.35, 17), (268.3, 18), (282.075, 19), (293.725, 20), (308.6, 21),
    (324.275, 22), (347.025, 23), (369.025, 24), (388.55, 25), (410.675, 26), (419.775, 27),
    (438.9, 28), (450.775, 29), (465.275, 30), (484.9, 31), (508.05, 32), (537.6, 33),
]
TOTAL_DURATION = 557.175
TIMING_JSON = "audio/the-straits-dollar-singapores-first-money-of-its-own-1903.timing.json"

# The avatar presenter, cartoon with motion: corner bubble for the first and last 30 s.
AVATAR = {"ranges": [(0, 30), (-30, None)], "motion": True}
