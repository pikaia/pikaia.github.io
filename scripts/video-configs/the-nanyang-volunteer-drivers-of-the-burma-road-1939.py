"""Video config for the Nanyang volunteers post.

The pool is thin on the volunteers themselves, so the road carries the middle:
the 1940-41 Chinese photos of lorries on the road and the crash, the US Army
convoy and landslide photos, the OpenStreetMap route map and the Hump map
(both letterbox, frozen). The two Nanyang Siang Pau pages are pushed in on
their stories: the 18 February 1939 headline and the 20 February report on
how the first group organised itself. Singapore sentences sit on the 1930s
harbour photos and Raffles Place; Tan Kah Kee's sentences on his own 1911 and
1946 photos; the Sook Ching on the Civilian War Memorial. Small scans are
letterboxed, not zoomed.

41 slides, 549.675s. AVATAR: first and last 30s (avatar test #7, cartoon).
"""

_U = "https://upload.wikimedia.org/wikipedia/commons"
_C = f"{_U}/thumb"
_A = "/assets/images"

IMAGES = {
    "HERO": f"{_U}/6/6c/%E6%BB%87%E7%BC%85%E5%85%AC%E8%B7%AF01.jpg",
    "CRASH": f"{_U}/e/e6/%E6%BB%87%E7%BC%85%E5%85%AC%E8%B7%AF%E8%BF%90%E8%BE%93%E6%83%85%E5%86%B501.jpg",
    "BULLDOZER": f"{_U}/3/30/%E6%BB%87%E7%BC%85%E5%85%AC%E8%B7%AF-%E6%8E%A8%E5%9C%9F%E6%9C%BA.jpg",
    "ABMAC": f"{_C}/7/79/ABMAC_trucks_on_Burma_Road_-_DPLA_-_5753369dd3963972687f72522b10540f.jpg/1920px-ABMAC_trucks_on_Burma_Road_-_DPLA_-_5753369dd3963972687f72522b10540f.jpg",
    "CONVOY": f"{_U}/7/7a/China-bound_convoy_travels_Burma_Road.jpg",
    "AERIAL": f"{_U}/b/b8/Aerial_view_of_Burma_Road.jpg",
    "JAPTRUCK": f"{_U}/8/8c/Japanese_truck_and_tankette_in_Burma_Road.jpg",
    "CUIHU": f"{_U}/1/14/Kumming%27s_Cuihu_from_the_east%2C_circa_1940s.jpg",
    "DIANCHI": f"{_U}/2/2f/Dianchi_boats_1940s.jpg",
    "TKK1946": f"{_U}/a/a6/Tan_Kah_Kee%2C_Lee_Kong_Chian%2C_and_Tan_Lark_Sye%2C_1946.png",
    "TKKSUN": f"{_U}/0/03/Tan_Kah_Kee_and_Sun_Yat-sen.jpg",
    "CHS": f"{_U}/f/ff/View_from_the_Bell_tower_in_the_50s.JPG",
    "HUMPMAP": f"{_U}/9/97/The_Hump_and_Burma_Road.png",
    "MAP": f"{_A}/burma-road-map.png",
    "NYSP18": f"{_A}/nanyang-siang-pau-1939-02-18-page-6.jpg",
    "NYSP20": f"{_A}/nanyang-siang-pau-1939-02-20-page-8.jpg",
    "CWM": f"{_C}/a/a2/Singapore_Civilian-War-Memorial-01.jpg/1920px-Singapore_Civilian-War-Memorial-01.jpg",
    "CWM2": f"{_C}/7/72/Civilian_War_Memorial%2C_Singapore_-_20131117.jpg/1920px-Civilian_War_Memorial%2C_Singapore_-_20131117.jpg",
    "SCULPT": f"{_U}/9/9b/%E5%8D%97%E4%BE%A8%E6%9C%BA%E5%B7%A5%E7%BA%AA%E5%BF%B5%E9%9B%95%E5%A1%91.jpg",
    "HALL": f"{_C}/8/83/Sun_Yat_Sen_Nanyang_Memorial_Hall%2C_July_2022.jpg/1920px-Sun_Yat_Sen_Nanyang_Memorial_Hall%2C_July_2022.jpg",
    "HARB": f"{_C}/3/37/Haven_van_Singapore%2C_KITLV_104789.tiff/lossy-page1-1920px-Haven_van_Singapore%2C_KITLV_104789.tiff.jpg",
    "HARBPAN": f"{_C}/0/0e/De_haven_van_Singapore%2C_KITLV_29185.tiff/lossy-page1-1920px-De_haven_van_Singapore%2C_KITLV_29185.tiff.jpg",
    "WHARF": f"{_C}/d/dc/KITLV_A1041_-_Haven_van_Singapore%2C_KITLV_140424.tiff/lossy-page1-1920px-KITLV_A1041_-_Haven_van_Singapore%2C_KITLV_140424.tiff.jpg",
    "CHARTERED": f"{_C}/5/59/The_Chartered_Bank_aan_Raffles_Place_te_Singapore%2C_KITLV_104795.tiff/lossy-page1-1920px-The_Chartered_Bank_aan_Raffles_Place_te_Singapore%2C_KITLV_104795.tiff.jpg",
    "RAFFLES1963": f"{_C}/b/bf/SG_Singapore_Raffles_Square_-_1963_%28W63-K27-15%29.jpg/1920px-SG_Singapore_Raffles_Square_-_1963_%28W63-K27-15%29.jpg",
    "SURRENDER": f"{_U}/9/9e/Japanese_surrender_at_Singapore%2C_1945.jpg",
}

# Credits for images not captioned in the post or its gallery.
CREDITS = {
    "HARB": "The harbour of Singapore, KITLV 104789, unknown photographer, CC BY 4.0, via Wikimedia Commons",
    "HARBPAN": "The harbour of Singapore, KITLV 29185, unknown photographer, CC BY 4.0, via Wikimedia Commons",
    "WHARF": "The harbour of Singapore, KITLV 140424, unknown photographer, CC BY 4.0, via Wikimedia Commons",
    "CHARTERED": "The Chartered Bank at Raffles Place, KITLV 104795, unknown photographer, CC BY 4.0, via Wikimedia Commons",
    "RAFFLES1963": "Raffles Place in about 1963, David Pirmann, CC BY 2.0, via Wikimedia Commons",
    "SURRENDER": "The Japanese surrender at Singapore, 12 September 1945, Royal Navy official photographer, public domain, via Wikimedia Commons",
    "CWM2": "The Civilian War Memorial, Singapore, 2013, Clay Gilliland, CC BY-SA 2.0, via Wikimedia Commons",
}

_E = "ease-in-out"
_IN = {"type": "cover", "zoom": [1.0, 1.06, 1.12], "pan": [(0.5, 0.5)] * 3, "ease": _E}
_OUT = {"type": "cover", "zoom": [1.12, 1.06, 1.0], "pan": [(0.5, 0.5)] * 3, "ease": _E}
_INL = {"type": "cover", "zoom": [1.0, 1.08, 1.16], "pan": [(0.35, 0.45)] * 3, "ease": _E}
_INR = {"type": "cover", "zoom": [1.0, 1.08, 1.16], "pan": [(0.65, 0.45)] * 3, "ease": _E}
# Small scans and tall photos: letterbox, modest zoom (no zoom on grainy photos).
_PORT = {"type": "letterbox", "zoom": [1.0, 1.04, 1.08], "pan": [(0.5, 0.5)] * 3, "ease": _E}
# Maps: letterbox, frozen.
_GFX = {"type": "letterbox", "zoom": [1, 1, 1], "pan": [(0.5, 0.5)] * 3}


def _c(zoom, pan):
    return {"type": "cover", "zoom": zoom, "pan": pan, "ease": _E}


# Whole-page newspaper push-ins, zoom capped at 2.4x.
_NY18_HEAD = _c([2.0, 2.1, 2.2], [(1.0, 0.06), (1.0, 0.07), (1.0, 0.08)])       # the headline, top right
_NY18_PAGE = _c([1.0, 1.04, 1.08], [(0.5, 0.0), (0.5, 0.03), (0.5, 0.06)])      # the page from the top
_NY20_FIRST = _c([2.2, 2.3, 2.4], [(0.82, 0.59), (0.83, 0.6), (0.84, 0.61)])    # the first group's organisation
_NY20_PAGE = _c([1.0, 1.04, 1.08], [(0.5, 0.06), (0.5, 0.09), (0.5, 0.12)])

SLIDES = [
    {"img": "HERO", **_IN},             # 0  s0      title
    {"img": "NYSP18", **_NY18_HEAD},    # 1  s1      "to return to the homeland and serve"
    {"img": "HARBPAN", **_IN},          # 2  s2      the first 80 of 3,200
    {"img": "CRASH", **_IN},            # 3  s3-5    a third died; loyalty; home
    {"img": "TKKSUN", **_PORT},         # 4  s6      the Nanyang responds with money
    {"img": "TKK1946", **_PORT},        # 5  s7      Tan Kah Kee's relief fund
    {"img": "HARB", **_INL},            # 6  s8      rich and poor gave
    {"img": "CHS", **_PORT},            # 7  s9      the Chinese High School, October 1938
    {"img": "HUMPMAP", **_GFX},         # 8  s10-11  China's coast lost
    {"img": "MAP", **_GFX},             # 9  s12-13  the Burma Road, Lashio to Kunming
    {"img": "ABMAC", **_IN},            # 10 s14     drivers and mechanics needed
    {"img": "WHARF", **_IN},            # 11 s15-16  the appeal; the first group leaves
    {"img": "NYSP20", **_NY20_PAGE},    # 12 s17-19  batches; nine in ten from Malaya
    {"img": "CONVOY", **_IN},           # 13 s20     women and non-Chinese volunteers
    {"img": "NYSP18", **_NY18_PAGE},    # 14 s21-22  the paper reports the departure
    {"img": "NYSP20", **_NY20_FIRST},   # 15 s23     the first group's own organisation
    {"img": "BULLDOZER", **_IN},        # 16 s24-25  training; mountain passes, landslides
    {"img": "HERO", **_OUT},            # 17 s26     malaria and bombing
    {"img": "ABMAC", **_OUT},           # 18 s27     20,000 tons a month
    {"img": "CRASH", **_OUT},           # 19 s28-30  how many died
    {"img": "JAPTRUCK", **_PORT},       # 20 s31     the road cut, May 1942
    {"img": "HUMPMAP", **_GFX},         # 21 s32     the airlift from India
    {"img": "CUIHU", **_IN},            # 22 s33     a third stayed in China
    {"img": "CHARTERED", **_IN},        # 23 s34     the war reaches Malaya
    {"img": "TKK1946", **_PORT},        # 24 s35     the Mobilisation Council; Dalforce
    {"img": "WHARF", **_OUT},           # 25 s36     2,000 to 4,000 volunteers
    {"img": "HARBPAN", **_OUT},         # 26 s37     Dalforce in position
    {"img": "CWM", **_PORT},            # 27 s38-39  the Sook Ching
    {"img": "CWM2", **_PORT},           # 28 s40-41  many thousands killed
    {"img": "TKKSUN", **_PORT},         # 29 s42     Tan Kah Kee in hiding in Java
    {"img": "SURRENDER", **_IN},        # 30 s43     after the war
    {"img": "TKK1946", **_PORT},        # 31 s44-46  back to China; refused re-entry
    {"img": "RAFFLES1963", **_IN},      # 32 s47-48  families chose to stay; citizenship
    {"img": "CHARTERED", **_OUT},       # 33 s49     320,000 registered
    {"img": "RAFFLES1963", **_OUT},     # 34 s50     community leaders took it up
    {"img": "DIANCHI", **_IN},          # 35 s51-52  forgotten, then rediscovered
    {"img": "NYSP18", **_NY18_PAGE},    # 36 s53     the 2009 exhibition
    {"img": "HALL", **_IN},             # 37 s54     the Sun Yat Sen Nanyang Memorial Hall
    {"img": "SCULPT", **_IN},           # 38 s55     where it fits
    {"img": "MAP", **_GFX},             # 39 s56     a generation's sense of belonging
    {"img": "SCULPT", **_OUT},          # 40 s57     they belong to that history
]

SCHEDULE = [
    (0.0, 0), (5.525, 1), (17.8, 2), (37.0, 3), (51.075, 4), (62.6, 5), (74.15, 6), (90.05, 7),
    (103.325, 8), (115.625, 9), (138.425, 10), (146.3, 11), (162.875, 12), (183.325, 13),
    (200.5, 14), (219.95, 15), (231.0, 16), (252.85, 17), (259.65, 18), (270.425, 19),
    (288.325, 20), (293.75, 21), (302.7, 22), (315.775, 23), (322.4, 24), (337.0, 25),
    (352.45, 26), (366.3, 27), (392.675, 28), (398.8, 29), (405.8, 30), (410.55, 31),
    (429.275, 32), (447.325, 33), (459.125, 34), (471.375, 35), (489.125, 36), (507.275, 37),
    (519.95, 38), (527.125, 39), (542.35, 40),
]
TOTAL_DURATION = 549.675
TIMING_JSON = "audio/the-nanyang-volunteer-drivers-of-the-burma-road-1939.timing.json"

# The avatar presenter, cartoon, test #7: corner bubble for the first and last 30 s.
AVATAR = {"ranges": [(0, 30), (-30, None)]}
