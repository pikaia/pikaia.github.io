"""Video config for the Song Ong Siang post.

Nine images, all portrait-oriented scans or portraits, so every slide is
letterbox. The pool is thin (Commons has almost nothing beyond a few
portraits from the 1923 book), so images repeat on purpose; COUPLE and
CROP are the same 1923 photograph, full and cropped, for variety. The
1936 Wentscher oil portrait is deliberately not used (the painter died
in 1961, so Commons' public-domain tag is doubtful).

  COUPLE   - Song Ong Siang in academic dress with his wife Helen Yeo,
             frontispiece of the 1923 book (Commons)
  CROP     - the same photo cropped to Song alone (Commons)
  LBK      - Lim Boon Keng, 1930s (Commons, Lee Brothers Studio)
  HOOT     - Song Hoot Kiam, the author's father, plate from the book
  TKC      - Tan Kim Ching, plate from the book
  SEAH     - Seah Eu Chin, plate from the book
  WBT      - Wee Boon Teck, plate from the book
  ST36     - The Straits Times, 7 Jan 1936, page 10 (whole page, local
             scan, NewspaperSG / SPH, public domain by age)
  ST41     - The Straits Times, 30 Sept 1941, page 10 (same basis)

48 slides, 472.575s.
"""

_U = "https://upload.wikimedia.org/wikipedia/commons"

IMAGES = {
    "COUPLE": f"{_U}/e/e1/Mr_and_Mrs_Song_Ong_Siang%2C_1923.png",
    "CROP": f"{_U}/4/4c/Sir_Song_Ong_Siang%2C_1923_%28cropped%29.png",
    "LBK": f"{_U}/c/c7/Lim_Boon_Keng%2C_1930s.jpg",
    "HOOT": f"{_U}/thumb/3/3c/Song_Hoot_Kiam.jpg/1280px-Song_Hoot_Kiam.jpg",
    "TKC": f"{_U}/thumb/c/cc/Tan_Kim_Ching.jpg/1280px-Tan_Kim_Ching.jpg",
    "SEAH": f"{_U}/thumb/6/64/Seah_Eu_Chin.jpg/1280px-Seah_Eu_Chin.jpg",
    "WBT": f"{_U}/thumb/2/2a/Wee_Boon_Teck.jpg/1280px-Wee_Boon_Teck.jpg",
    "ST36": "/assets/images/straits-times-1936-01-07-page-10.jpg",
    "ST41": "/assets/images/straits-times-1941-09-30-page-10.jpg",
}

_LTB = {"type": "letterbox", "zoom": [1.0, 1.04, 1.08], "pan": [(0.5, 0.5)] * 3, "ease": "ease-in-out"}
_LTBO = {"type": "letterbox", "zoom": [1.08, 1.04, 1.0], "pan": [(0.5, 0.5)] * 3, "ease": "ease-out"}

SLIDES = [
    {"img": "COUPLE", **_LTB},        # 0  s0  title
    {"img": "TKC", **_LTB},           # 1  s1  the 602-page book
    {"img": "COUPLE", **_LTBO},       # 2  s2  the author, few know his name
    {"img": "CROP", **_LTB},          # 3  s3  born 14 June 1871
    {"img": "HOOT", **_LTB},          # 4  s4  father Song Hoot Kiam
    {"img": "CROP", **_LTBO},         # 5  s5  Raffles Institution, Guthrie
    {"img": "COUPLE", **_LTB},        # 6  s6  the Queen's Scholarship
    {"img": "COUPLE", **_LTBO},       # 7  s7  first in 1886 and 1887, too young
    {"img": "LBK", **_LTB},           # 8  s8  Lim Boon Keng won 1887
    {"img": "CROP", **_LTB},          # 9  s9  Song took it in 1888
    {"img": "CROP", **_LTBO},         # 10 s10 Middle Temple, Cambridge
    {"img": "COUPLE", **_LTB},        # 11 s11 English Bar, then Singapore Bar 1894
    {"img": "CROP", **_LTB},          # 12 s12 Aitken & Ong Siang
    {"img": "ST36", **_LTB},          # 13 s13 1936 tribute, chamber work
    {"img": "CROP", **_LTBO},         # 14 s14 public life
    {"img": "COUPLE", **_LTBO},       # 15 s15 Bintang Timor
    {"img": "LBK", **_LTBO},          # 16 s16 Straits Chinese Magazine
    {"img": "LBK", **_LTB},           # 17 s17 girls' school, SCBA
    {"img": "CROP", **_LTB},          # 18 s18 a soldier of sorts
    {"img": "COUPLE", **_LTB},        # 19 s19 SVI Chinese company, coronation 1902
    {"img": "CROP", **_LTBO},         # 20 s20 captain in 1915
    {"img": "COUPLE", **_LTBO},       # 21 s21 Legislative Council, marriage committee
    {"img": "TKC", **_LTBO},          # 22 s22 the book began small
    {"img": "LBK", **_LTBO},          # 23 s23 1919 centenary, Lim declined
    {"img": "SEAH", **_LTB},          # 24 s24 grew into a history
    {"img": "WBT", **_LTB},           # 25 s25 two assistants, three years
    {"img": "TKC", **_LTB},           # 26 s26 finished 1922
    {"img": "SEAH", **_LTBO},         # 27 s27 John Murray, GBP12
    {"img": "WBT", **_LTBO},          # 28 s28 subscriptions, William Murray letter
    {"img": "HOOT", **_LTBO},         # 29 s29 the dedication
    {"img": "TKC", **_LTBO},          # 30 s30 Times Literary Supplement
    {"img": "SEAH", **_LTB},          # 31 s31 portraits and biographies
    {"img": "WBT", **_LTB},           # 32 s32 this blog has leaned on it
    {"img": "ST36", **_LTBO},         # 33 s33 knighted 1936
    {"img": "ST36", **_LTB},          # 34 s34 L.C.L. tribute
    {"img": "COUPLE", **_LTB},        # 35 s35 the King's Chinese
    {"img": "CROP", **_LTB},          # 36 s36 ill health
    {"img": "ST41", **_LTB},          # 37 s37 died 29 Sept 1941, editorial
    {"img": "ST41", **_LTBO},         # 38 s38 funeral, gun carriage
    {"img": "ST41", **_LTB},          # 39 s39 firm dissolved, invasion
    {"img": "TKC", **_LTB},           # 40 s40 scholars differ
    {"img": "SEAH", **_LTBO},         # 41 s41 Wheatley
    {"img": "WBT", **_LTBO},          # 42 s42 Warren
    {"img": "TKC", **_LTBO},          # 43 s43 both views
    {"img": "CROP", **_LTBO},         # 44 s44 no single explanation
    {"img": "COUPLE", **_LTBO},       # 45 s45 a lifetime building institutions
    {"img": "HOOT", **_LTB},          # 46 s46 why it matters today
    {"img": "COUPLE", **_LTB},        # 47 s47 history compiled by particular people
]

SCHEDULE = [
    (0.0, 0), (5.45, 1), (17.8, 2), (28.375, 3), (41.425, 4),
    (50.175, 5), (59.45, 6), (66.625, 7), (77.375, 8), (85.85, 9),
    (94.475, 10), (104.225, 11), (116.35, 12), (128.55, 13), (140.725, 14),
    (144.775, 15), (151.825, 16), (164.125, 17), (179.375, 18), (182.275, 19),
    (199.575, 20), (203.4, 21), (223.275, 22), (225.625, 23), (240.625, 24),
    (244.85, 25), (257.725, 26), (263.375, 27), (275.475, 28), (283.625, 29),
    (294.6, 30), (299.45, 31), (310.15, 32), (318.8, 33), (329.0, 34),
    (344.95, 35), (357.25, 36), (361.9, 37), (376.775, 38), (385.75, 39),
    (394.225, 40), (397.325, 41), (410.325, 42), (419.55, 43), (426.075, 44),
    (432.925, 45), (446.325, 46), (458.075, 47),
]
TOTAL_DURATION = 472.575
TIMING_JSON = "audio/song-ong-siang-the-chronicler-who-became-singapores-first-chinese-knight.timing.json"
