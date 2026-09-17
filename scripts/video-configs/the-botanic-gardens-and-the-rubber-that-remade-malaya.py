"""Video config for the Botanic Gardens/rubber post.

Six images - all portrait-oriented scans/photos (old portraits, a
vertical garden shot, a tall museum bust, a personal photo), so every
slide is letterbox; no cover slides needed for this post.

  HERO         - Henry Nicholas Ridley beside a tapped rubber tree,
                 circa 1900 (Commons, Singapore MND) - shows the man,
                 the herringbone cut, and a live tree all at once
  WICKHAM      - Henry Wickham beside an old rubber tree (Commons,
                 Biblioteca Nacional Digital Brasil) - the 1876
                 seed-smuggling origin story
  TANCHAYYAN   - Portrait of Tan Chay Yan (Commons, from Song Ong
                 Siang's 1923 history) - the planter whose 1896 estate
                 proved rubber could make money
  STATUE       - Bronze bust of Ridley, Muzium Negara KL (Commons) -
                 hands cupped as if still offering seeds; used for the
                 "never made a cent"/legacy beat
  MODERN       - The Botanic Gardens bandstand today (Commons) -
                 present-day UNESCO payoff
  ORCHID       - Dendrobium Barack and Michelle Obama, photographed by
                 Chris on a visit of his own in 2018 - the personal
                 aside paragraph added 2026-09-17

32 slides, 319.725s.
"""

_U = "https://upload.wikimedia.org/wikipedia/commons"

IMAGES = {
    "HERO": f"{_U}/2/21/Henry_Nicholas_Ridley%2C_Botanist_%281855-1956%29.jpg",
    "WICKHAM": f"{_U}/0/03/%E2%80%9CHenry_Wickham%2C_who_in_1876_directed_an_operation_smuggling_70%2C000_rubber_tree_seeds%E2%80%9D.jpg",
    "TANCHAYYAN": f"{_U}/7/70/Tan_Chay_Yan.png",
    "STATUE": f"{_U}/c/ce/Statue_of_Sir_Henry_Nicholas_Ridley_%28DSCF0927%29.jpg",
    "MODERN": f"{_U}/9/93/UNESCO_HERITAGE_AT_BOTANIC_GARDEN_1859.jpg",
    "ORCHID": "/assets/images/botanic-gardens-named-orchid.jpg",
}

_LTB = {"type": "letterbox", "zoom": [1.0, 1.04, 1.08], "pan": [(0.5, 0.5)] * 3, "ease": "ease-in-out"}
_LTBO = {"type": "letterbox", "zoom": [1.08, 1.04, 1.0], "pan": [(0.5, 0.5)] * 3, "ease": "ease-out"}

SLIDES = [
    {"img": "HERO", **_LTB},          # 0  s0   title
    {"img": "MODERN", **_LTBO},       # 1  s1   joggers, wedding photographers
    {"img": "MODERN", **_LTB},        # 2  s2   UNESCO World Heritage Site since 2015
    {"img": "MODERN", **_LTBO},       # 3  s3   doesn't look like the place that decided
    {"img": "WICKHAM", **_LTB},       # 4  s4   the rubber itself came from a theft
    {"img": "WICKHAM", **_LTBO},      # 5  s5   1876, Wickham smuggled seeds
    {"img": "WICKHAM", **_LTB},       # 6  s6   2,700 seeds at Kew, most to Ceylon
    {"img": "HERO", **_LTBO},         # 7  s7   22 seedlings sent from Kew 1877
    {"img": "HERO", **_LTB},          # 8  s8   for over a decade, end of story
    {"img": "HERO", **_LTBO},         # 9  s9   nobody wanted to grow rubber
    {"img": "HERO", **_LTB},          # 10 s10  coffee and gambier
    {"img": "HERO", **_LTBO},         # 11 s11  Ridley arrived 1888
    {"img": "HERO", **_LTB},          # 12 s12  pestering, pockets, Mad Ridley
    {"img": "HERO", **_LTBO},         # 13 s13  wild tapping killed the tree
    {"img": "HERO", **_LTB},          # 14 s14  1895, herringbone cut
    {"img": "WICKHAM", **_LTBO},      # 15 s15  same method used today
    {"img": "TANCHAYYAN", **_LTB},    # 16 s16  planters only started listening
    {"img": "TANCHAYYAN", **_LTBO},   # 17 s17  coffee-leaf disease
    {"img": "TANCHAYYAN", **_LTB},    # 18 s18  1896, Tan Chay Yan's estate
    {"img": "TANCHAYYAN", **_LTBO},   # 19 s19  it worked
    {"img": "TANCHAYYAN", **_LTB},    # 20 s20  1898 expanded, 1906 largest in world
    {"img": "STATUE", **_LTBO},       # 21 s21  then the automobile arrived
    {"img": "STATUE", **_LTB},        # 22 s22  demand for tyres, rubber boom 1910
    {"img": "HERO", **_LTBO},         # 23 s23  345 to 2.3 million acres
    {"img": "HERO", **_LTB},          # 24 s24  half the world's rubber by 1920s
    {"img": "STATUE", **_LTBO},       # 25 s25  Ridley never made a cent
    {"img": "STATUE", **_LTB},        # 26 s26  left 1911, died 1956 at 101
    {"img": "HERO", **_LTBO},         # 27 s27  made millions, never a penny
    {"img": "ORCHID", **_LTB},        # 28 s28  I've visited the Gardens myself
    {"img": "ORCHID", **_LTBO},       # 29 s29  one of dozens of orchids named for heads of state
    {"img": "MODERN", **_LTB},        # 30 s30  why it matters today
    {"img": "MODERN", **_LTBO},       # 31 s31  trees gone, tapping method still used
]

SCHEDULE = [
    (0.0, 0), (4.25, 1), (19.775, 2), (31.45, 3), (39.775, 4),
    (42.825, 5), (59.625, 6), (67.45, 7), (79.7, 8), (83.7, 9),
    (86.6, 10), (95.8, 11), (109.5, 12), (124.425, 13), (138.4, 14),
    (148.425, 15), (153.225, 16), (157.825, 17), (167.35, 18), (182.125, 19),
    (183.575, 20), (200.7, 21), (203.35, 22), (216.15, 23), (227.075, 24),
    (233.5, 25), (237.525, 26), (252.45, 27), (259.625, 28), (277.1, 29),
    (290.925, 30), (309.55, 31),
]
TOTAL_DURATION = 319.725
TIMING_JSON = "audio/the-botanic-gardens-and-the-rubber-that-remade-malaya.timing.json"
