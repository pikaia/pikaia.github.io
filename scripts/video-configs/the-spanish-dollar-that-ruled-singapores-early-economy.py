"""Video config for the Spanish dollar post.

Coin and banknote photos plus two self-rendered chart PNGs. The coins are square-ish
or very wide against a 16:9 frame; a slow zoom on a *letterboxed* foreground
showed real held-frame jerkiness (checked with --check-only), so the coin slides
use cover with slow pans across the coin instead (cover is supersampled and
smooth). The two small banknote scans and the charts are frozen letterbox.

  COINSG   - 1789 Charles IV dollar countermarked "Singapore" (Commons, CC BY 2.5 ES)
  PILLAR   - 1771 Mexican pillar dollar, both faces (Commons, Heritage Auctions)
  S1904O/R - 1904 Straits Settlements dollar, obverse/reverse (Commons, CC0)
  NOTE1911 - 1911 $50 Straits note (Commons, public domain) - small, frozen
  NOTE1935 - 1935 $1 Straits note (Commons, public domain) - small, frozen
  SGCHART  - scripts/render_spanish_dollar_charts.py (Singapore's own money)
  RESCHART - same script (reserve-currency baton)

35 slides, one per sentence.
"""

_U = "https://upload.wikimedia.org/wikipedia/commons"

IMAGES = {
    "COINSG": f"{_U}/3/33/1789_Charles_IV_Spanish_dollar_countermarked_with_Chinese_words_meaning_%22Singapore%22.jpg",
    "PILLAR": f"{_U}/f/f9/Mexico_Carlos_III_Pillar_Dollar_of_8_Reales_1771.jpg",
    "S1904O": f"{_U}/4/49/Straits_Settlements%2C_One_Dollar%2C_Edward_VII%2C_1904_-_obverse.jpg",
    "S1904R": f"{_U}/6/69/Straits_Settlements%2C_One_Dollar%2C_Edward_VII%2C_1904%2C_-_reverse.jpg",
    "NOTE1911": f"{_U}/0/02/Straits_Setlements_-_1911_-_%2450_banknote.jpg",
    "NOTE1935": f"{_U}/a/aa/Straits_Settlements_-_1935_-_%241_banknote_%28obverse%29.jpg",
    "SGCHART": "/assets/images/spanish-dollar-singapore-money-chart.png",
    "RESCHART": "/assets/images/spanish-dollar-reserve-currencies-chart.png",
}

CREDITS = {
    "SGCHART": "Chart by Lesser Known Singapore, dates per the post's own Sources list",
    "RESCHART": "Chart by Lesser Known Singapore, data: Wikipedia (Reserve currency, Spanish dollar)",
}

_CNA = {"type": "cover", "zoom": [1.0, 1.05, 1.1], "pan": [(0.5, 0.35), (0.5, 0.5), (0.5, 0.62)], "ease": "ease-in-out"}
_CNB = {"type": "cover", "zoom": [1.1, 1.05, 1.0], "pan": [(0.5, 0.62), (0.5, 0.5), (0.5, 0.38)], "ease": "ease-in-out"}
# PILLAR is two coin faces side by side (aspect ~2:1): zoom in so one face fills the
# frame, and pan across from one face to the other.
_PLA = {"type": "cover", "zoom": [1.55, 1.55, 1.55], "pan": [(0.12, 0.5), (0.5, 0.5), (0.88, 0.5)], "ease": "ease-in-out"}
_PLB = {"type": "cover", "zoom": [1.55, 1.55, 1.55], "pan": [(0.88, 0.5), (0.5, 0.5), (0.12, 0.5)], "ease": "ease-in-out"}
_S4A = {"type": "cover", "zoom": [1.0, 1.05, 1.1], "pan": [(0.5, 0.35), (0.5, 0.5), (0.5, 0.62)], "ease": "ease-in-out"}
_S4B = {"type": "cover", "zoom": [1.1, 1.05, 1.0], "pan": [(0.5, 0.62), (0.5, 0.5), (0.5, 0.38)], "ease": "ease-in-out"}
_S4C = {"type": "cover", "zoom": [1.0, 1.05, 1.1], "pan": [(0.5, 0.35), (0.5, 0.5), (0.5, 0.62)], "ease": "ease-in-out"}
_S4D = {"type": "cover", "zoom": [1.1, 1.05, 1.0], "pan": [(0.5, 0.62), (0.5, 0.5), (0.5, 0.38)], "ease": "ease-in-out"}
_NOTE = {"type": "letterbox", "zoom": [1.0, 1.0, 1.0], "pan": [(0.5, 0.5)] * 3, "ease": "linear"}
_CHART = {"type": "letterbox", "zoom": [1.0, 1.0, 1.0], "pan": [(0.5, 0.5)] * 3, "ease": "linear"}

SLIDES = [
    {"img": "COINSG", **_CNA},  # s0  title
    {"img": "COINSG", **_CNB},  # s1  1824 finished buying Singapore
    {"img": "PILLAR", **_PLA},  # s2  33,200 Spanish dollars
    {"img": "PILLAR", **_PLB},  # s3  struck in Mexico and Peru
    {"img": "PILLAR", **_PLA},  # s4  piece of eight, 1497
    {"img": "COINSG", **_CNA},  # s5  uniformity
    {"img": "PILLAR", **_PLB},  # s6  Manila galleons
    {"img": "COINSG", **_CNB},  # s7  chopmarks
    {"img": "PILLAR", **_PLA},  # s8  1819 already using it
    {"img": "PILLAR", **_PLB},  # s9  mix of currencies, 1823
    {"img": "COINSG", **_CNA},  # s10 MAS: silver dollar, copper for bazaar
    {"img": "SGCHART", **_CHART},  # s11 Company's preference
    {"img": "SGCHART", **_CHART},  # s12 1826 rupee pushed
    {"img": "SGCHART", **_CHART},  # s13 market did not follow
    {"img": "PILLAR", **_PLA},  # s14 Mexican dollar
    {"img": "COINSG", **_CNB},  # s15 1840 first Singapore banknote
    {"img": "SGCHART", **_CHART},  # s16 1867 London takes over
    {"img": "SGCHART", **_CHART},  # s17 five dollars legal tender
    {"img": "COINSG", **_CNA},  # s18 whatever silver merchants trusted
    {"img": "S1904O", **_S4A},  # s19 supply of good dollars held up
    {"img": "S1904O", **_S4B},  # s20 1895 trade dollar, 1897 board
    {"img": "S1904O", **_S4A},  # s21 1903 Straits dollar, 1904 demonetised
    {"img": "S1904R", **_S4C},  # s22 value was its silver
    {"img": "SGCHART", **_CHART},  # s23 1906 gold peg 2s4d
    {"img": "S1904R", **_S4D},  # s24 smaller dollar 1907
    {"img": "NOTE1911", **_NOTE},  # s25 1931 sterling, 1939 Malayan
    {"img": "RESCHART", **_CHART},  # s26 baton of world money
    {"img": "RESCHART", **_CHART},  # s27 Spanish dollar first global
    {"img": "RESCHART", **_CHART},  # s28 Dutch guilder
    {"img": "RESCHART", **_CHART},  # s29 pound sterling
    {"img": "RESCHART", **_CHART},  # s30 Bretton Woods 1944
    {"img": "RESCHART", **_CHART},  # s31 1950s sterling 55 percent
    {"img": "PILLAR", **_PLA},  # s32 US dollar based on Spanish weight
    {"img": "COINSG", **_CNA},  # s33 bigger story
    {"img": "NOTE1935", **_NOTE},  # s34 pound then American dollar
]

SCHEDULE = [
    (0.0, 0), (4.425, 1), (14.725, 2), (28.925, 3), (40.65, 4),
    (53.275, 5), (65.375, 6), (78.25, 7), (85.575, 8), (92.175, 9),
    (110.025, 10), (122.1, 11), (125.5, 12), (137.25, 13), (139.8, 14),
    (154.125, 15), (165.85, 16), (172.625, 17), (183.3, 18), (189.35, 19),
    (194.275, 20), (210.125, 21), (224.825, 22), (234.225, 23), (246.1, 24),
    (261.55, 25), (274.3, 26), (286.0, 27), (297.225, 28), (308.575, 29),
    (319.225, 30), (330.375, 31), (341.025, 32), (357.55, 33), (372.125, 34),
]
TOTAL_DURATION = 391.525
TIMING_JSON = "audio/the-spanish-dollar-that-ruled-singapores-early-economy.timing.json"
