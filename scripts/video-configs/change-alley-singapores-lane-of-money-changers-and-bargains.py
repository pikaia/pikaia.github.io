"""Video config for the Change Alley post.

Three whole newspaper pages carry the alley itself: The Malayan Saturday Post
of 16 April 1932 (page 30; its two alley photographs at the bottom, pushed in
one at a time), the Singapore Free Press of 25 February 1931 (page 10; the
"Heart of the Lion City" column, top right) and The Sunday Times of
12 February 1939 (page 32; the "Bargain Mart" back page and its photographs).
The 1965 street-sign photo opens and closes. Raffles Place (1910-1971) and the
Collyer Quay waterfront fill the business-district sentences; Clifford Pier in
1971 takes the landing. The timeline (letterbox, frozen) takes the closure.
The 2005 arcade, bridge and Hitachi Tower photos and OUE Link take today.
No named person appears, so no portraits are needed.

37 slides, 568.925s. AVATAR: first and last 30s, cartoon with motion.
"""

_U = "https://upload.wikimedia.org/wikipedia/commons"
_C = f"{_U}/thumb"
_A = "/assets/images"

IMAGES = {
    "HERO": f"{_C}/f/f2/Change_Alley_Singapore_street_sign_January_1965.jpg/1280px-Change_Alley_Singapore_street_sign_January_1965.jpg",
    "MSP1932": f"{_A}/malayan-saturday-post-1932-04-16-page-30.jpg",
    "ST1939": f"{_A}/sunday-times-1939-02-12-page-32.jpg",
    "SFP1931": f"{_A}/singapore-free-press-1931-02-25-page-10.jpg",
    "TIMELINE": f"{_A}/change-alley-timeline-chart.png",
    "CLIFFORD71": f"{_C}/9/9d/545a_Singapore_1971_%2851316139004%29.jpg/1280px-545a_Singapore_1971_%2851316139004%29.jpg",
    "BRIDGE05": f"{_C}/b/b9/Change_Alley_Overhead_Bridge%2C_Dec_05.JPG/1280px-Change_Alley_Overhead_Bridge%2C_Dec_05.JPG",
    "RP1910A": f"{_C}/d/da/KITLV_-_79891_-_Kleingrothe%2C_C.J._-_Medan_-_Raffles_Place%2C_Singapore_-_circa_1910.tif/lossy-page1-1280px-KITLV_-_79891_-_Kleingrothe%2C_C.J._-_Medan_-_Raffles_Place%2C_Singapore_-_circa_1910.tif.jpg",
    "RP1910B": f"{_C}/8/85/KITLV_-_79893_-_Kleingrothe%2C_C.J._-_Medan_-_Raffles_Place_and_King_Street_in_Singapore_-_circa_1910.tif/lossy-page1-1280px-KITLV_-_79893_-_Kleingrothe%2C_C.J._-_Medan_-_Raffles_Place_and_King_Street_in_Singapore_-_circa_1910.tif.jpg",
    "RP1920": f"{_U}/a/a4/Raffles_Place_c._1920.jpg",
    "RPCARS": f"{_C}/7/7c/KITLV_A723_-_Raffles_Place_te_Singapore%2C_KITLV_87929.tiff/lossy-page1-1280px-KITLV_A723_-_Raffles_Place_te_Singapore%2C_KITLV_87929.tiff.jpg",
    "COLLYER1910": f"{_C}/4/4b/Collyer_Quay%2C_Singapore_postcard.jpg/1280px-Collyer_Quay%2C_Singapore_postcard.jpg",
    "KADE": f"{_C}/9/9a/Kade_te_Singapore%2C_KITLV_104787.tiff/lossy-page1-1280px-Kade_te_Singapore%2C_KITLV_104787.tiff.jpg",
    "HAVEN": f"{_C}/9/96/KITLV_A1112_-_Haven_van_Singapore%2C_KITLV_142600.tiff/lossy-page1-1280px-KITLV_A1112_-_Haven_van_Singapore%2C_KITLV_142600.tiff.jpg",
    "RP1963": f"{_C}/b/bf/SG_Singapore_Raffles_Square_-_1963_%28W63-K27-15%29.jpg/1280px-SG_Singapore_Raffles_Square_-_1963_%28W63-K27-15%29.jpg",
    "RP71G": f"{_C}/d/dc/71-610_Raffles_Place_Singapore_1971_%2851252222815%29.jpg/1280px-71-610_Raffles_Place_Singapore_1971_%2851252222815%29.jpg",
    "RP71B": f"{_C}/0/01/71-610a_Raffles_Place_Singapore_1971_%2851251176861%29.jpg/1280px-71-610a_Raffles_Place_Singapore_1971_%2851251176861%29.jpg",
    "CB71": f"{_C}/2/28/522a_Singapore_1971_%2851316419105%29.jpg/1280px-522a_Singapore_1971_%2851316419105%29.jpg",
    "AERIAL05": f"{_U}/1/1b/Change_Alley_Aerial_Plaza%2C_Dec_05.JPG",
    "ARCADE05": f"{_U}/e/e0/Change_Alley%2C_Dec_05.JPG",
    "OUELINK": f"{_C}/a/a1/OUE_Link_Entrance.jpg/1280px-OUE_Link_Entrance.jpg",
    # Not in this post's captions (credited below):
    "MAP1890": f"{_C}/b/b9/Map_of_Raffles_Place_from_The_Stranger%27s_Guide_to_Singapore_%281890%29.jpg/1280px-Map_of_Raffles_Place_from_The_Stranger%27s_Guide_to_Singapore_%281890%29.jpg",
    "LONDON": f"{_U}/b/b8/Change_Alley_-_geograph.org.uk_-_1759761.jpg",
    "HITACHI05": f"{_U}/9/97/Hitachi_Tower%2C_Dec_05.JPG",
}

# Credits for images not captioned in the post or its gallery.
CREDITS = {
    "TIMELINE": "Timeline by Lesser Known Singapore, from the Daily Advertiser (1890), Singapore Free Press (1931), Sunday Times (1939) and NLB Infopedia",
    "MAP1890": "Map of Raffles Place from The Stranger's Guide to Singapore, 1890, B. D. d'Aranjo, public domain, via Wikimedia Commons",
    "LONDON": "Change Alley, City of London, 2010, Basher Eyre, CC BY-SA 2.0, via Wikimedia Commons",
    "HITACHI05": "Hitachi Tower, Singapore, December 2005, Mailer diablo, copyrighted free use, via Wikimedia Commons",
}

_E = "ease-in-out"
_IN = {"type": "cover", "zoom": [1.0, 1.06, 1.12], "pan": [(0.5, 0.5)] * 3, "ease": _E}
_OUT = {"type": "cover", "zoom": [1.12, 1.06, 1.0], "pan": [(0.5, 0.5)] * 3, "ease": _E}
# Tall photos, small scans and the map: letterbox, modest zoom (no zoom on grainy photos).
_PORT = {"type": "letterbox", "zoom": [1.0, 1.04, 1.08], "pan": [(0.5, 0.5)] * 3, "ease": _E}
_PORT_OUT = {"type": "letterbox", "zoom": [1.08, 1.04, 1.0], "pan": [(0.5, 0.5)] * 3, "ease": _E}
_STILL = {"type": "letterbox", "zoom": [1, 1, 1], "pan": [(0.5, 0.5)] * 3}
# The timeline: letterbox, frozen.
_GFX = {"type": "letterbox", "zoom": [1, 1, 1], "pan": [(0.5, 0.5)] * 3}


def _c(zoom, pan):
    return {"type": "cover", "zoom": zoom, "pan": pan, "ease": _E}


# The 1965 photo: the street sign high in the frame, then the stall at bottom left.
_HERO_SIGN = _c([1.0, 1.04, 1.08], [(0.5, 0.2)] * 3)
_HERO_STALL = _c([1.4, 1.45, 1.5], [(0.0, 0.95)] * 3)
# Clifford Pier, 1971: pushed in on the pier building.
_PIER = _c([1.5, 1.55, 1.6], [(0.26, 0.6)] * 3)

# Whole-page newspaper push-ins, zoom capped at 2.4x.
# Malayan Saturday Post, 1932 (1600x2403): the alley photographs at the bottom.
_MSP_BOTTOM = _c([1.0, 1.05, 1.1], [(0.5, 1.0), (0.5, 0.98), (0.5, 0.96)])
_MSP_BUSY = _c([2.0, 2.05, 2.1], [(0.08, 0.84)] * 3)     # "during business hours", left
_MSP_QUIET = _c([2.0, 2.05, 2.1], [(0.98, 0.845)] * 3)   # "after business hours", right
# Singapore Free Press, 1931 (1600x2066): the column at top right.
_SFP_HEAD = _c([2.2, 2.3, 2.4], [(0.944, 0.0), (0.944, 0.01), (0.944, 0.02)])
_SFP_HAWKERS = _c([2.4, 2.4, 2.4], [(0.944, 0.34), (0.944, 0.36), (0.944, 0.38)])
_SFP_EXCHANGE = _c([2.4, 2.4, 2.4], [(0.944, 0.58), (0.944, 0.6), (0.944, 0.62)])
# The Sunday Times, 1939 (1600x2206).
_ST_HEAD = _c([1.6, 1.65, 1.7], [(0.66, 0.19), (0.66, 0.2), (0.66, 0.21)])     # headline and the shop photo
_ST_PAGE = _c([1.0, 1.04, 1.08], [(0.5, 0.0), (0.5, 0.04), (0.5, 0.08)])
_ST_SHOP = _c([2.0, 2.05, 2.1], [(0.62, 0.22)] * 3)      # the shop counter, top centre
_ST_LANE = _c([2.0, 2.05, 2.1], [(0.0, 0.26)] * 3)       # the lane and its awnings, top left
_ST_MID = _c([1.8, 1.85, 1.9], [(0.635, 0.746)] * 3)     # the two middle photographs
_ST_CROWD = _c([1.8, 1.85, 1.9], [(0.635, 0.965)] * 3)   # the crowd, bottom

SLIDES = [
    {"img": "HERO", **_HERO_SIGN},      # 0  s0      title
    {"img": "CLIFFORD71", **_IN},       # 1  s1      from the sea to the business district
    {"img": "COLLYER1910", **_IN},      # 2  s2      Collyer Quay to Raffles Place
    {"img": "ST1939", **_ST_HEAD},      # 3  s3      money-changers and bazaar
    {"img": "ARCADE05", **_PORT},       # 4  s4      closed 1989; the arcade now
    {"img": "MAP1890", **_PORT},        # 5  s5-6    named in 1890
    {"img": "LONDON", **_STILL},        # 6  s7      London's Exchange Alley
    {"img": "MSP1932", **_MSP_BUSY},    # 7  s8      the money-changers who worked there
    {"img": "RP1910A", **_IN},          # 8  s9      a short cut to Raffles Place
    {"img": "KADE", **_IN},             # 9  s10-11  Winchester House; landing at the waterfront
    {"img": "MSP1932", **_MSP_BOTTOM},  # 10 s12     mostly Indian, in their own shops
    {"img": "RP1920", **_IN},           # 11 s13-14  the 1920s; the 1929 burglary
    {"img": "HAVEN", **_IN},            # 12 s15     ships' crews and passengers
    {"img": "HERO", **_HERO_STALL},     # 13 s16-17  changers at the entrances
    {"img": "MSP1932", **_MSP_QUIET},   # 14 s18     1932: busy by day, eerie after hours
    {"img": "SFP1931", **_SFP_HEAD},    # 15 s19     the 1931 walk
    {"img": "RP1910B", **_IN},          # 16 s20-21  Mincing Lane, Petticoat Lane
    {"img": "SFP1931", **_SFP_EXCHANGE},  # 17 s22-23  the produce exchange
    {"img": "RPCARS", **_IN},           # 18 s24-26  business moves to offices and telephones
    {"img": "SFP1931", **_SFP_HAWKERS},  # 19 s27-28  the hawkers' calls
    {"img": "ST1939", **_ST_MID},       # 20 s29-31  shops by the dozen
    {"img": "ST1939", **_ST_PAGE},      # 21 s32-33  the Sunday Times back page
    {"img": "ST1939", **_ST_SHOP},      # 22 s34-36  bargaining at the counter
    {"img": "ST1939", **_ST_CROWD},     # 23 s37-40  after the war
    {"img": "CLIFFORD71", **_PIER},     # 24 s41-43  landing at Clifford Pier
    {"img": "RP1963", **_IN},           # 25 s44     phrases in four languages
    {"img": "RP71B", **_IN},            # 26 s45-46  the office workers
    {"img": "ST1939", **_ST_LANE},      # 27 s47-48  "if you don't bargain"
    {"img": "AERIAL05", **_PORT},       # 28 s49     the Aerial Plaza, 1973
    {"img": "CB71", **_IN},             # 29 s50-52  losing customers
    {"img": "TIMELINE", **_GFX},        # 30 s53-54  the last day, 30 April 1989
    {"img": "COLLYER1910", **_OUT},     # 31 s55-56  the stallholders; the end buildings demolished
    {"img": "RP71G", **_OUT},           # 32 s57-59  Chris's aside
    {"img": "HITACHI05", **_PORT},      # 33 s60     Caltex House and Hitachi Tower, 1993
    {"img": "BRIDGE05", **_IN},         # 34 s61     the arcade and its bridge
    {"img": "OUELINK", **_PORT_OUT},    # 35 s62-63  office workers again
    {"img": "HERO", **_OUT},            # 36 s64     why it matters
]

SCHEDULE = [
    (0.0, 0), (4.6, 1), (14.325, 2), (24.325, 3), (42.65, 4), (51.375, 5), (64.95, 6), (73.05, 7),
    (80.175, 8), (84.0, 9), (101.85, 10), (110.65, 11), (126.575, 12), (137.825, 13), (156.225, 14),
    (174.15, 15), (183.225, 16), (197.675, 17), (218.4, 18), (245.3, 19), (262.35, 20), (287.975, 21),
    (308.95, 22), (333.05, 23), (361.75, 24), (379.4, 25), (385.85, 26), (404.55, 27), (417.5, 28),
    (429.65, 29), (450.625, 30), (468.325, 31), (487.65, 32), (508.75, 33), (521.225, 34), (531.6, 35),
    (551.625, 36),
]
TOTAL_DURATION = 568.925
TIMING_JSON = "audio/change-alley-singapores-lane-of-money-changers-and-bargains.timing.json"

# The avatar presenter, cartoon with motion: corner bubble for the first and last 30 s.
AVATAR = {"ranges": [(0, 30), (-30, None)], "motion": True}
