"""Video config for the Lien Ying Chow post.

There is no free photo of Lien himself, so his sentences sit on places and
pages (the named-person rule): the harbour he left in 1942, Fremantle, Hong
Kong and Robinson Road, wartime Chongqing, Raffles Place and Meyer Chambers,
the Mandarin and the OUB Centre. The two 1949 newspaper pages carry the
opening: the Straits Times announcement (pushed in on its board list) and the
Sunday Times front page ("People's Bank Opened"). Named people get their own
portraits: Chiang Kai-shek, Aw Boon Haw, Tan Lark Sye, Loke Wan Tho. Small
Commons scans (the Chongqing photos, the portraits) are letterboxed, not
zoomed. The timeline chart is letterbox, frozen.

47 slides, 716.85s. AVATAR: first and last 30s (avatar test #6).
"""

_U = "https://upload.wikimedia.org/wikipedia/commons"
_C = f"{_U}/thumb"
_A = "/assets/images"

IMAGES = {
    "RAFFLES1963": f"{_C}/b/bf/SG_Singapore_Raffles_Square_-_1963_%28W63-K27-15%29.jpg/1920px-SG_Singapore_Raffles_Square_-_1963_%28W63-K27-15%29.jpg",
    "WHARF": f"{_C}/d/dc/KITLV_A1041_-_Haven_van_Singapore%2C_KITLV_140424.tiff/lossy-page1-1920px-KITLV_A1041_-_Haven_van_Singapore%2C_KITLV_140424.tiff.jpg",
    "HARB": f"{_C}/3/37/Haven_van_Singapore%2C_KITLV_104789.tiff/lossy-page1-1920px-Haven_van_Singapore%2C_KITLV_104789.tiff.jpg",
    "HARBPAN": f"{_C}/0/0e/De_haven_van_Singapore%2C_KITLV_29185.tiff/lossy-page1-1920px-De_haven_van_Singapore%2C_KITLV_29185.tiff.jpg",
    "FREMANTLE": f"{_U}/8/8a/Fremantle_Harbour%2C_WW2.PNG",
    "DAPU": f"{_C}/3/31/Dapu_County_DSC_2199_%284129932675%29.jpg/1920px-Dapu_County_DSC_2199_%284129932675%29.jpg",
    "HK1920": f"{_U}/c/cc/Hong_Kong_Connaught_Road_1920s.jpg",
    "ROBINSON": f"{_U}/1/14/Robinson_Road-sg.JPG",
    "CQ1900S": f"{_U}/5/53/Collyer_Quay%2C_Singapore_1900s.jpg",
    "CQ1910": f"{_C}/f/f0/KITLV_-_79887_-_Kleingrothe%2C_C.J._-_Medan_-_Collyer_Quay%2C_Quay_in_Singapore_-_circa_1910.tif/lossy-page1-1920px-KITLV_-_79887_-_Kleingrothe%2C_C.J._-_Medan_-_Collyer_Quay%2C_Quay_in_Singapore_-_circa_1910.tif.jpg",
    "CHARTERED": f"{_C}/5/59/The_Chartered_Bank_aan_Raffles_Place_te_Singapore%2C_KITLV_104795.tiff/lossy-page1-1920px-The_Chartered_Bank_aan_Raffles_Place_te_Singapore%2C_KITLV_104795.tiff.jpg",
    "RP1920S": f"{_C}/7/7c/KITLV_A723_-_Raffles_Place_te_Singapore%2C_KITLV_87929.tiff/lossy-page1-1280px-KITLV_A723_-_Raffles_Place_te_Singapore%2C_KITLV_87929.tiff.jpg",
    "CHAMBER": f"{_U}/e/e7/Singapore_Chinese_Chamber_of_Commerce_%26_Industry_Building%2C_Aug_06.JPG",
    "CHIANG": f"{_U}/d/d0/Chiang_Kai-shek_in_the_40s.jpg",
    "CQBOMB": f"{_U}/8/8e/Chongqing_bomb.jpg",
    "CQMAP": f"{_U}/7/71/Bombing_of_Chongqing.png",
    "CQWALL": f"{_U}/9/95/%E9%87%8D%E6%85%B6%E5%9F%8E%E5%A2%BB1940s.jpg",
    "CQVOL": f"{_U}/4/48/Chungking_bomb6.jpg",
    "CQALLEY": f"{_U}/4/4f/Korean_Provisional_Government_%28%EB%8C%80%ED%95%9C%EB%AF%BC%EA%B5%AD_%EC%9E%84%EC%8B%9C%EC%A0%95%EB%B6%80%2C_%E5%A4%A7%E9%9F%A9%E6%B0%91%E5%9B%BD_%E8%87%A8%E6%99%82%E6%94%BF%E5%BA%9C%29_Third_Office_in_Chongqing%2C_1941-1945.jpg",
    "SURRENDER": f"{_U}/9/9e/Japanese_surrender_at_Singapore%2C_1945.jpg",
    "ST1949": f"{_A}/straits-times-1949-02-05-page-4.jpg",
    "SUN1949": f"{_A}/sunday-times-1949-02-06-page-1.jpg",
    "SB1930": f"{_A}/straits-budget-1930-12-04-page-2.jpg",
    "AW": f"{_U}/8/87/Hu_Wenhu.jpg",
    "TLS": f"{_U}/d/dd/Tan_Lark_Sye%2C_1950.jpg",
    "LOKE": f"{_U}/1/12/Loke_Wan_Tho%2C_1947_%28cropped%29.jpg",
    "MANDVIEW": f"{_C}/f/f6/Singapore-Mandarin_Hotel-1973-74-WUS08139.jpg/1920px-Singapore-Mandarin_Hotel-1973-74-WUS08139.jpg",
    "MANDORCH": f"{_C}/8/87/Singapore-Orchard_Road-Mandarin_Hotel-1973-74-WUS08142.jpg/1920px-Singapore-Orchard_Road-Mandarin_Hotel-1973-74-WUS08142.jpg",
    "OUBSKY": f"{_U}/d/d2/OUB_Centre_Skyward.JPG",
    "OUBDEC": f"{_U}/b/b4/OUB_Centre%2C_Dec_05.JPG",
    "SCULPT": f"{_U}/5/54/Yang_Ying_Feng%2C_Progress_and_Advancement_%281988%2C_detail%29%2C_Raffles_Place%2C_Singapore_-_20090908.jpg",
    "UOB2001": f"{_U}/a/a8/Evening_view_of_UOB_Plaza%2C_OUB_Centre_and_OCBC_Centre_near_the_Singapore_River_-_20010608.jpg",
    "MAS": f"{_U}/8/8e/MAS_Building%2C_Springleaf_Tower.JPG",
    "MBFC": f"{_C}/c/c1/2016_Singapur%2C_Downtown_Core%2C_Marina_Bay_Financial_Centre.jpg/1280px-2016_Singapur%2C_Downtown_Core%2C_Marina_Bay_Financial_Centre.jpg",
    "TIMELINE": f"{_A}/lien-ying-chow-timeline-chart.png",
}

# Credits for images not captioned in the post or its gallery.
CREDITS = {
    "WHARF": "The harbour of Singapore, KITLV 140424, unknown photographer, CC BY 4.0, via Wikimedia Commons",
    "HARB": "The harbour of Singapore, KITLV 104789, unknown photographer, CC BY 4.0, via Wikimedia Commons",
    "HARBPAN": "The harbour of Singapore, KITLV 29185, unknown photographer, CC BY 4.0, via Wikimedia Commons",
    "DAPU": "Sunset over Dapu County, 2009, Aaron Lai, CC BY 2.0, via Wikimedia Commons",
    "ROBINSON": "Robinson Road, Singapore, 2006, Terence Ong, CC BY 2.5, via Wikimedia Commons",
    "CQ1900S": "Collyer Quay in the 1900s, unknown photographer, public domain, via Wikimedia Commons",
    "CQ1910": "Collyer Quay, about 1910, C. J. Kleingrothe, KITLV 79887, public domain, via Wikimedia Commons",
    "CHARTERED": "The Chartered Bank at Raffles Place, KITLV 104795, unknown photographer, CC BY 4.0, via Wikimedia Commons",
    "RP1920S": "Raffles Place, KITLV 87929, unknown photographer, CC BY 4.0, via Wikimedia Commons",
    "CQMAP": "Map of the bombing of Chongqing, SY, CC BY-SA 4.0, via Wikimedia Commons",
    "OUBDEC": "The OUB Centre, December 2005, Mailer diablo, copyrighted free use, via Wikimedia Commons",
    "SCULPT": "Yang Ying Feng, Progress and Advancement (1988, detail), Raffles Place, photograph CC BY 2.0, via Wikimedia Commons",
    "UOB2001": "UOB Plaza, the OUB Centre and the OCBC Centre, 8 June 2001, Steven Byles, CC BY-SA 2.0, via Wikimedia Commons",
    "MAS": "The MAS Building, 2006, Terence Ong, CC BY 2.5, via Wikimedia Commons",
    "MBFC": "Marina Bay Financial Centre, 2016, Marcin Konsek, CC BY-SA 4.0, via Wikimedia Commons",
    "TIMELINE": "Chart by Lesser Known Singapore, dates per the post's own Sources list",
}

_E = "ease-in-out"
_IN = {"type": "cover", "zoom": [1.0, 1.06, 1.12], "pan": [(0.5, 0.5)] * 3, "ease": _E}
_OUT = {"type": "cover", "zoom": [1.12, 1.06, 1.0], "pan": [(0.5, 0.5)] * 3, "ease": _E}
_INL = {"type": "cover", "zoom": [1.0, 1.08, 1.16], "pan": [(0.35, 0.45)] * 3, "ease": _E}
_INR = {"type": "cover", "zoom": [1.0, 1.08, 1.16], "pan": [(0.65, 0.45)] * 3, "ease": _E}
# Portraits, tall towers and small scans: letterbox, modest zoom (no zoom on grainy photos).
_PORT = {"type": "letterbox", "zoom": [1.0, 1.04, 1.08], "pan": [(0.5, 0.5)] * 3, "ease": _E}
# Graphics (the timeline, the map): letterbox, frozen.
_GFX = {"type": "letterbox", "zoom": [1, 1, 1], "pan": [(0.5, 0.5)] * 3}


def _c(zoom, pan):
    return {"type": "cover", "zoom": zoom, "pan": pan, "ease": _E}


# Whole-page newspaper push-ins, zoom capped at 2.4x.
_ST49_AD = _c([2.0, 2.1, 2.2], [(0.0, 0.02), (0.0, 0.025), (0.0, 0.03)])        # the opening announcement
_ST49_BOARD = _c([2.2, 2.3, 2.4], [(0.0, 0.12), (0.0, 0.14), (0.0, 0.16)])    # its board list
_SUN49_TOP = _c([1.0, 1.04, 1.08], [(0.5, 0.0), (0.5, 0.0), (0.5, 0.0)])        # the front page, masthead
_SUN49_BANK = _c([2.2, 2.3, 2.4], [(0.18, 0.72), (0.185, 0.728), (0.19, 0.736)])  # "People's Bank Opened"
_SB30_PHOTO = _c([1.5, 1.58, 1.66], [(0.4, 0.14), (0.42, 0.15), (0.44, 0.16)])  # Meyer Chambers

SLIDES = [
    {"img": "RAFFLES1963", **_IN},    # 0  s0      title
    {"img": "WHARF", **_IN},          # 1  s1      the Gorgon leaves the harbour
    {"img": "HARBPAN", **_IN},        # 2  s2      cash and two diamonds
    {"img": "FREMANTLE", **_IN},      # 3  s3      reached Fremantle
    {"img": "ST1949", **_ST49_AD},    # 4  s4      the first new bank of postwar Singapore
    {"img": "DAPU", **_IN},           # 5  s5-7    born in Dapu; orphaned
    {"img": "HK1920", **_IN},         # 6  s8      Hong Kong; HK$10
    {"img": "HARB", **_INL},          # 7  s9      arrives in Singapore
    {"img": "ROBINSON", **_IN},       # 8  s10-12  Kian Thye, Robinson Road
    {"img": "CQ1900S", **_IN},        # 9  s13-14  his own chandlery; Wah Hin
    {"img": "CHARTERED", **_IN},      # 10 s15     supplies the British forces
    {"img": "CHAMBER", **_PORT},      # 11 s16     Chamber president, 1941
    {"img": "WHARF", **_OUT},         # 12 s17-18  bombing; leaves on the Gorgon
    {"img": "FREMANTLE", **_OUT},     # 13 s19     the passenger list at Fremantle
    {"img": "CHIANG", **_PORT},       # 14 s20     Chongqing under Chiang Kai-shek
    {"img": "CQBOMB", **_IN},         # 15 s21     the bombing of Chongqing
    {"img": "CQWALL", **_PORT},       # 16 s22     the wartime political council
    {"img": "CQVOL", **_PORT},        # 17 s23     back into business
    {"img": "CQALLEY", **_PORT},      # 18 s24-25  the Overseas Chinese Union Bank
    {"img": "CQMAP", **_GFX},         # 19 s26-27  branches; closed after the war
    {"img": "SURRENDER", **_IN},      # 20 s28     back in Singapore, October 1945
    {"img": "SUN1949", **_SUN49_TOP}, # 21 s29     opened 5 February 1949
    {"img": "SB1930", **_SB30_PHOTO}, # 22 s30     Meyer Chambers, the Yokohama Specie Bank's floor
    {"img": "ST1949", **_ST49_BOARD}, # 23 s31-34  capital, staff, board, chairman
    {"img": "AW", **_PORT},           # 24 s35     Aw Boon Haw
    {"img": "TLS", **_PORT},          # 25 s35     Tan Lark Sye
    {"img": "LOKE", **_PORT},         # 26 s35     Loke Wan Tho
    {"img": "RP1920S", **_IN},        # 27 s36     Raffles Place, the preserve of European banks
    {"img": "SUN1949", **_SUN49_BANK},# 28 s37-38  "People's Bank Opened"
    {"img": "HARB", **_OUT},          # 29 s39-42  the rice trade; the dividend
    {"img": "CQ1910", **_IN},         # 30 s43-44  branches; 32 branches by 1968
    {"img": "RAFFLES1963", **_OUT},   # 31 s45-46  New York; one of the big four
    {"img": "MANDVIEW", **_IN},       # 32 s47-49  the hotel plan
    {"img": "MANDORCH", **_INR},      # 33 s50     the Mandarin opens, 1971
    {"img": "OUBSKY", **_PORT},       # 34 s51-52  land bought plot by plot
    {"img": "OUBDEC", **_PORT},       # 35 s53-54  the OUB Centre
    {"img": "TIMELINE", **_GFX},      # 36 s55-57  public roles
    {"img": "SCULPT", **_IN},         # 37 s58-59  monuments board; the Lien Foundation
    {"img": "RP1920S", **_OUT},       # 38 s60-61  retires; the smallest of the four
    {"img": "UOB2001", **_IN},        # 39 s62-63  the 2001 bids
    {"img": "TIMELINE", **_GFX},      # 40 s64-65  sold to UOB; the name gone
    {"img": "OUBSKY", **_PORT},       # 41 s66-67  the tower still stands
    {"img": "HARBPAN", **_OUT},       # 42 s68-69  savings carried out in his clothes
    {"img": "MAS", **_PORT},          # 43 s70-71  deposit insurance
    {"img": "MBFC", **_IN},           # 44 s72-73  91 per cent of depositors
    {"img": "SUN1949", **_SUN49_TOP}, # 45 s74-75  where it fits
    {"img": "CQWALL", **_PORT},       # 46 s76     a refugee bank in Chongqing
]

SCHEDULE = [
    (0.0, 0), (3.85, 1), (18.6, 2), (31.55, 3), (38.775, 4), (50.4, 5), (71.4, 6), (84.275, 7),
    (99.775, 8), (124.625, 9), (142.95, 10), (157.8, 11), (166.275, 12), (189.9, 13), (201.35, 14),
    (211.725, 15), (224.575, 16), (235.4, 17), (238.25, 18), (259.35, 19), (272.05, 20),
    (283.825, 21), (297.025, 22), (307.225, 23), (337.525, 24), (340.6, 25), (343.6, 26),
    (346.625, 27), (359.725, 28), (378.375, 29), (404.125, 30), (423.175, 31), (441.725, 32),
    (460.7, 33), (465.125, 34), (481.3, 35), (507.225, 36), (534.925, 37), (550.875, 38),
    (572.3, 39), (592.225, 40), (610.25, 41), (625.6, 42), (642.05, 43), (668.55, 44),
    (689.65, 45), (705.35, 46),
]
TOTAL_DURATION = 716.85
TIMING_JSON = "audio/lien-ying-chow-the-banker-who-escaped-to-chongqing.timing.json"

# The avatar presenter, Phase 1 test #6: corner bubble for the first and last 30 s.
AVATAR = {"ranges": [(0, 30), (-30, None)]}
