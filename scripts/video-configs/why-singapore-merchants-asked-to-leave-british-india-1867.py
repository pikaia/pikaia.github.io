"""Video config for the 1867 transfer post.

The Town Hall photo of the 1860s opens and closes the ceremony; the 1860
harbour panorama is swept in three different stretches for the free port and
the trade figures; the coins (letterbox) carry the currency quarrel; the
Straits Times of 23 December 1856 is pushed in on its report of the port dues
meeting; the timeline (letterbox, frozen) takes the forty years under India and
the Act. Portraits only under sentences naming that person: Ord, Keppel,
Cavenagh, Canning, Seah Eu Chin, Whampoa. Buckley, W. H. Read, Lord Bury and
the Earl of Albemarle have no portraits here, so their sentences show places
or coins. Small portraits and coins are letterboxed, not zoomed.

44 slides, 606.25s. AVATAR: first and last 30s, cartoon with motion.
"""

_U = "https://upload.wikimedia.org/wikipedia/commons"
_C = f"{_U}/thumb"
_A = "/assets/images"

IMAGES = {
    "TOWNHALL": f"{_U}/6/66/Town_Hall%2C_Singapore_-_1860s.jpg",
    "ORD": f"{_U}/3/3c/Sir_Harry_Ord.jpg",
    "ORD2": f"{_U}/7/7f/HarryStGeorgeOrd-1867-1873.jpg",
    "KEPPEL": f"{_U}/9/95/Admiral_of_the_Fleet_Sir_Henry_Keppel.jpg",
    "CANNING": f"{_U}/7/7c/Charles_Canning%2C_1st_Earl_Canning.jpg",
    "CAVENAGH": f"{_U}/0/00/Sir_Orfeur_Cavenagh.jpg",
    "SEAH": f"{_C}/6/64/Seah_Eu_Chin.jpg/1280px-Seah_Eu_Chin.jpg",
    "WHAMPOA": f"{_C}/7/7b/The_Hon._Hoh-Ah-Kay_Whampoa%2C_C.M.G.%2C_M.L.C.%2C_and_Consul_for_Wellcome_V0037527.jpg/1280px-The_Hon._Hoh-Ah-Kay_Whampoa%2C_C.M.G.%2C_M.L.C.%2C_and_Consul_for_Wellcome_V0037527.jpg",
    "RUPEE_O": f"{_U}/6/6d/East_India_Company%2C_One_Rupee%2C_1840_-_obverse.jpg",
    "RUPEE_R": f"{_U}/3/32/East_India_Company%2C_One_Rupee%2C_1840_-_reverse.jpg",
    "MEXDOLLAR": f"{_C}/3/33/1888_M%C3%A9xico_8_Reals_Trade_Coin_Silver.jpg/1280px-1888_M%C3%A9xico_8_Reals_Trade_Coin_Silver.jpg",
    "SPANISH": f"{_C}/0/09/SPANISH_PIECE_OF_EIGHT%2C_CARLOS_IV_MEXICO_MINT_1805_-8_REALES_b_-_Flickr_-_woody1778a.jpg/1280px-SPANISH_PIECE_OF_EIGHT%2C_CARLOS_IV_MEXICO_MINT_1805_-8_REALES_b_-_Flickr_-_woody1778a.jpg",
    "CENT_R": f"{_C}/4/4e/India_Straits%2C_One_Cent%2C_1862_-_reverse.jpg/1280px-India_Straits%2C_One_Cent%2C_1862_-_reverse.jpg",
    "CENT_O": f"{_C}/b/b4/India_Straits%2C_One_Cent%2C_1862_-_obverse.jpg/1280px-India_Straits%2C_One_Cent%2C_1862_-_obverse.jpg",
    "GOVHOUSE": f"{_C}/5/56/Government_House%2C_Singapore%2C_approaching_completion%2C_1869_%28McNair_1899%2C_Plate_XVIII%29.jpg/1280px-Government_House%2C_Singapore%2C_approaching_completion%2C_1869_%28McNair_1899%2C_Plate_XVIII%29.jpg",
    "HARBOUR": f"{_C}/7/79/KITLV_-_29175_-_View_of_the_harbor_of_Singapore_-_1860.tif/lossy-page1-1920px-KITLV_-_29175_-_View_of_the_harbor_of_Singapore_-_1860.tif.jpg",
    "PROMENADE": f"{_C}/c/cd/KITLV_-_29170_-_Promenade_in_Singapore_-_1860.tif/lossy-page1-1280px-KITLV_-_29170_-_Promenade_in_Singapore_-_1860.tif.jpg",
    "ESPLANADE": f"{_C}/d/d4/Gezicht_op_de_Esplanade_te_Singapore%2C_RP-F-F01025-BH.jpg/1280px-Gezicht_op_de_Esplanade_te_Singapore%2C_RP-F-F01025-BH.jpg",
    "TOWN": f"{_C}/1/16/Gezicht_op_Singapore%2C_RP-F-F01025-AZ.jpg/1280px-Gezicht_op_Singapore%2C_RP-F-F01025-AZ.jpg",
    "MAP": f"{_C}/e/e5/Map_of_Singapore_from_A_Sailor%27s_Life_under_Four_Sovereigns_%281899%29.jpg/1280px-Map_of_Singapore_from_A_Sailor%27s_Life_under_Four_Sovereigns_%281899%29.jpg",
    "CHINESE1867": f"{_C}/2/2c/Chinese_in_Singapore%2C_Aleksei_Vysheslavtsev%2C_page_121_%281867%29.jpg/1280px-Chinese_in_Singapore%2C_Aleksei_Vysheslavtsev%2C_page_121_%281867%29.jpg",
    "ST1856": f"{_A}/straits-times-1856-12-23-page-4.jpg",
    "TIMELINE": f"{_A}/straits-transfer-timeline-chart.png",
    # From earlier posts, or not in this post's captions (credited below):
    "TOWN2": f"{_C}/5/5f/Gezicht_op_Singapore%2C_RP-F-F01025-BR.jpg/1280px-Gezicht_op_Singapore%2C_RP-F-F01025-BR.jpg",
    "MUSTER": f"{_C}/1/16/General_monthly_muster_of_the_convicts%2C_Singapore_Jail_%28McNair_1899%2C_frontispiece%29.jpg/1280px-General_monthly_muster_of_the_convicts%2C_Singapore_Jail_%28McNair_1899%2C_frontispiece%29.jpg",
    "STANDREWS": f"{_C}/d/d4/KITLV_-_29163_-_St._Andrew%27s_Cathedral%2C_belonging_to_the_Anglican_Church%2C_Singapore_-_1860.tif/lossy-page1-1280px-KITLV_-_29163_-_St._Andrew%27s_Cathedral%2C_belonging_to_the_Anglican_Church%2C_Singapore_-_1860.tif.jpg",
    "SHIP": f"{_C}/e/e6/Maersk_Huacho_container_ship_at_Pasir_Panjang_Container_Terminal.jpg/1280px-Maersk_Huacho_container_ship_at_Pasir_Panjang_Container_Terminal.jpg",
    "PORT": f"{_C}/7/7f/Pasir_Panjang_Container_Terminal%2C_Singapore_-_20110227-01.jpg/1280px-Pasir_Panjang_Container_Terminal%2C_Singapore_-_20110227-01.jpg",
}

# Credits for images not captioned in the post or its gallery.
CREDITS = {
    "TIMELINE": "Timeline by Lesser Known Singapore, dates from Buckley (1902), Hansard and The Straits Times",
    "ORD2": "Harry Ord as Governor of the Straits Settlements, 1867-73, G. R. Lambert, public domain, via Wikimedia Commons",
    "RUPEE_O": "East India Company rupee, 1840, obverse, 5snake5, CC0, via Wikimedia Commons",
    "CENT_O": "India Straits one cent, 1862, obverse, 5snake5, CC0, via Wikimedia Commons",
    "TOWN2": "A view of Singapore, between 1867 and 1880, Rijksmuseum, CC0, via Wikimedia Commons",
    "MUSTER": "The general monthly muster of the convicts, Singapore jail, J. F. A. McNair and W. D. Bayliss, Prisoners Their Own Warders (1899), public domain, via Wikimedia Commons",
    "STANDREWS": "St Andrew's Church, Singapore, 1860, unknown photographer, KITLV, public domain, via Wikimedia Commons",
    "SHIP": "A container ship at Pasir Panjang Container Terminal, 2021, Wzhkevin, CC BY-SA 4.0, via Wikimedia Commons",
    "PORT": "Pasir Panjang Container Terminal, 2011, Jacklee, CC BY-SA 3.0, via Wikimedia Commons",
}

_E = "ease-in-out"
_IN = {"type": "cover", "zoom": [1.0, 1.06, 1.12], "pan": [(0.5, 0.5)] * 3, "ease": _E}
_OUT = {"type": "cover", "zoom": [1.12, 1.06, 1.0], "pan": [(0.5, 0.5)] * 3, "ease": _E}
# Small portraits, coins and tall pictures: letterbox, modest zoom (no zoom on grainy photos).
_PORT = {"type": "letterbox", "zoom": [1.0, 1.04, 1.08], "pan": [(0.5, 0.5)] * 3, "ease": _E}
# The timeline and the map: letterbox, frozen.
_GFX = {"type": "letterbox", "zoom": [1, 1, 1], "pan": [(0.5, 0.5)] * 3}


def _c(zoom, pan):
    return {"type": "cover", "zoom": zoom, "pan": pan, "ease": _E}


# The Rijksmuseum views are cartes de visite in album mounts: zoom past the card.
_CARD_IN = _c([1.52, 1.57, 1.62], [(0.5, 0.5)] * 3)
_CARD_OUT = _c([1.62, 1.57, 1.52], [(0.5, 0.5)] * 3)
# The 1860 harbour panorama is nearly five times wider than tall, so each
# cover slide sweeps a different stretch of it.
_HARB_L = _c([1.0, 1.02, 1.04], [(0.05, 0.5), (0.15, 0.5), (0.25, 0.5)])
_HARB_M = _c([1.0, 1.02, 1.04], [(0.4, 0.5), (0.5, 0.5), (0.6, 0.5)])
_HARB_R = _c([1.0, 1.02, 1.04], [(0.75, 0.5), (0.85, 0.5), (0.95, 0.5)])
# Whole-page newspaper push-ins (1600x2500 page), zoom capped at 2.4x.
_ST_PAGE = _c([1.0, 1.04, 1.08], [(0.5, 0.15), (0.5, 0.2), (0.5, 0.25)])
_ST_REPORT = _c([2.0, 2.1, 2.2], [(0.77, 0.354), (0.758, 0.367), (0.748, 0.38)])     # the meeting report, centre column
_ST_DEEPER = _c([2.2, 2.3, 2.4], [(0.748, 0.428), (0.739, 0.453), (0.731, 0.476)])   # down to the resolutions

SLIDES = [
    {"img": "TOWNHALL", **_IN},         # 0  s0      title
    {"img": "TOWNHALL", **_c([1.15, 1.22, 1.3], [(0.5, 0.45)] * 3)},  # 1  s1  noon, 1 April 1867, the salute
    {"img": "ESPLANADE", **_CARD_IN},        # 2  s2      a crowd outside; the Order read
    {"img": "HARBOUR", **_HARB_L},      # 3  s3-4    forty years under India; now London
    {"img": "TOWN", **_CARD_IN},             # 4  s5-6    a campaign by Singapore's merchants
    {"img": "TOWNHALL", **_OUT},        # 5  s7      Buckley's account; Colonel Man arrives
    {"img": "ORD", **_PORT},            # 6  s8      Ord keeps his hat on
    {"img": "ORD2", **_PORT},           # 7  s9      "was never removed"
    {"img": "KEPPEL", **_PORT},         # 8  s10     Keppel takes an ordinary chair
    {"img": "TOWN2", **_CARD_IN},            # 9  s11-12  documents read; council sworn
    {"img": "PROMENADE", **_IN},        # 10 s13-14  W. H. Read (no portrait); a seat on the council
    {"img": "TIMELINE", **_GFX},        # 11 s15-16  1826, 1830, 1851
    {"img": "MAP", **_GFX},             # 12 s17     laws made in Calcutta
    {"img": "HARBOUR", **_HARB_M},      # 13 s18-19  growing fast; £4m to £15m (Lord Bury, no portrait)
    {"img": "TOWN", **_CARD_OUT},            # 14 s20     Europe-China trade, not India
    {"img": "SPANISH", **_PORT},        # 15 s21-22  Spanish and Mexican silver dollars
    {"img": "RUPEE_O", **_PORT},        # 16 s23     one currency; the rupee laws
    {"img": "RUPEE_R", **_PORT},        # 17 s24     220 rupees to 100 dollars
    {"img": "MEXDOLLAR", **_PORT},      # 18 s25-26  traders would not accept it; protests
    {"img": "RUPEE_O", **{**_PORT, "zoom": [1.1, 1.15, 1.2]}},  # 19 s27  "most barbarous and inconvenient coin"
    {"img": "CENT_R", **_PORT},         # 20 s28     the bill fails; the dollar stays
    {"img": "HARBOUR", **_HARB_R},      # 21 s29-30  the free port
    {"img": "ST1856", **_ST_PAGE},      # 22 s31     tonnage dues proposed
    {"img": "ST1856", **_ST_REPORT},    # 23 s32-33  about 8,000 rupees a year
    {"img": "ST1856", **_ST_DEEPER},    # 24 s34     "an unwarrantable attack"
    {"img": "PROMENADE", **_OUT},       # 25 s35     London forbids the dues
    {"img": "CAVENAGH", **_PORT},       # 26 s36     Cavenagh opposes them in 1863
    {"img": "MUSTER", **_IN},           # 27 s37-38  convicts from across India
    {"img": "STANDREWS", **_IN},        # 28 s39     the uprising; public works halted
    {"img": "CHINESE1867", **_PORT},    # 29 s40-41  the income tax fight
    {"img": "ESPLANADE", **_CARD_OUT},       # 30 s42-43  the meetings and the petition
    {"img": "HARBOUR", **_HARB_M},      # 31 s44     Bury presents it (no portrait)
    {"img": "CANNING", **_PORT},        # 32 s45-46  Canning agrees
    {"img": "TOWN2", **_CARD_OUT},           # 33 s47     into the 1860s
    {"img": "SEAH", **_PORT},           # 34 s48     Seah Eu Chin at the 1863 meeting
    {"img": "TIMELINE", **_GFX},        # 35 s49-50  the wait; the Act of 1866
    {"img": "TOWNHALL", **_IN},         # 36 s51     the new colony's councils
    {"img": "WHAMPOA", **_PORT},        # 37 s52     Whampoa, first Chinese member
    {"img": "GOVHOUSE", **_IN},         # 38 s53-54  a colony in its own right
    {"img": "ORD", **{**_PORT, "zoom": [1.08, 1.04, 1.0]}},     # 39 s55  Ord at odds with the merchants
    {"img": "CENT_O", **_PORT},         # 40 s56-57  the dollar and the free port survive
    {"img": "SHIP", **_IN},             # 41 s58-59  four kinds of dutiable goods today
    {"img": "PORT", **_IN},             # 42 s60-61  everything else duty-free
    {"img": "HARBOUR", **_HARB_L},      # 43 s62     why it matters
]

SCHEDULE = [
    (0.0, 0), (7.2, 1), (19.7, 2), (28.3, 3), (43.1, 4), (59.1, 5), (74.9, 6), (85.275, 7),
    (89.825, 8), (102.9, 9), (111.675, 10), (126.575, 11), (147.55, 12), (156.525, 13), (176.05, 14),
    (188.575, 15), (207.475, 16), (221.95, 17), (232.475, 18), (251.0, 19), (264.775, 20),
    (273.375, 21), (289.05, 22), (297.2, 23), (313.9, 24), (329.825, 25), (335.65, 26), (346.975, 27),
    (370.625, 28), (385.225, 29), (401.4, 30), (429.225, 31), (434.925, 32), (458.35, 33),
    (462.425, 34), (476.55, 35), (504.075, 36), (516.475, 37), (523.625, 38), (535.2, 39),
    (544.025, 40), (553.075, 41), (571.3, 42), (587.8, 43),
]
TOTAL_DURATION = 606.25
TIMING_JSON = "audio/why-singapore-merchants-asked-to-leave-british-india-1867.timing.json"

# The avatar presenter, cartoon with motion: corner bubble for the first and last 30 s.
AVATAR = {"ranges": [(0, 30), (-30, None)], "motion": True}
