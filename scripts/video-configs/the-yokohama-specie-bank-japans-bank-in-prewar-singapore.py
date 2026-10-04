"""Video config for the Yokohama Specie Bank post.

Six whole newspaper pages carry the Singapore story: the 1916 agency notice
(Straits Times), Meyer Chambers on the Straits Budget's 1930 page, and four
Syonan Shimbun pages (the March 1942 reopening notice and change of address,
the 1943 branch advertisement and the 1944 notice No. 52). Each is whole-page
`cover` pushing in on its story (pan/zoom from cover_crop test frames, zoom
capped at 2.4x). Period photos of Collyer Quay, the Hongkong and Shanghai Bank
and Raffles Place, and the bank's own offices in Yokohama, Shanghai, Nagasaki,
Hankou, Honolulu and Jesselton fill the rest.

No portraits: the managers named (Nakamura, Okada, Unagami, Mutoh, Ishii)
have no free photo, so their sentences sit on places or pages.

34 slides, 562.025s. AVATAR: first and last 30s (avatar test #4).
"""

_U = "https://upload.wikimedia.org/wikipedia/commons"
_C = f"{_U}/thumb"
_A = "/assets/images"

IMAGES = {
    "CQ1910": f"{_C}/f/f0/KITLV_-_79887_-_Kleingrothe%2C_C.J._-_Medan_-_Collyer_Quay%2C_Quay_in_Singapore_-_circa_1910.tif/lossy-page1-1920px-KITLV_-_79887_-_Kleingrothe%2C_C.J._-_Medan_-_Collyer_Quay%2C_Quay_in_Singapore_-_circa_1910.tif.jpg",
    "HSBC1900": f"{_U}/8/81/Photographic_Views_of_Singapore_Plate_05_Hongkong_and_Shanghai_Bank.jpg",
    "CQ1900S": f"{_U}/5/53/Collyer_Quay%2C_Singapore_1900s.jpg",
    "HARB1930S": f"{_C}/9/96/KITLV_A1112_-_Haven_van_Singapore%2C_KITLV_142600.tiff/lossy-page1-1920px-KITLV_A1112_-_Haven_van_Singapore%2C_KITLV_142600.tiff.jpg",
    "BONHAM": f"{_U}/a/a1/Bonham_Building_1907.jpg",
    "HQ1923": f"{_U}/e/e5/Yokohama_shokin_bank_Kanto_Daishinsai.jpg",
    "HQTODAY": f"{_C}/5/5b/Kanagawa_Prefectural_Museum_of_Cultural_History_2009.jpg/1920px-Kanagawa_Prefectural_Museum_of_Cultural_History_2009.jpg",
    "SHANGHAI": f"{_U}/c/ce/Yokohama_Specie_Bank_03.jpg",
    "NAGASAKI": f"{_U}/b/b6/Shookin_Bank_Nagasaki.jpg",
    "HANKOU": f"{_C}/e/ea/Wooden_Cash_Box_of_Yokohama_Specie_Bank_Ltd.%2C_Hankow_Branch_in_the_Early_20th_Century.jpg/1920px-Wooden_Cash_Box_of_Yokohama_Specie_Bank_Ltd.%2C_Hankow_Branch_in_the_Early_20th_Century.jpg",
    "HONOLULU": f"{_C}/b/bd/Honolulu-Yokohama-Specie-Bank.JPG/1280px-Honolulu-Yokohama-Specie-Bank.JPG",
    "WARTIME": f"{_U}/2/26/Yokohama_Specie_Bank_during_World_War_II.JPG",
    "JESSELTON": f"{_U}/0/01/Yokohama_Specie_Bank_branch_in_Api_%28Jesselton%29.jpg",
    "NOTE10": f"{_C}/c/c5/Ten_dollar_note_issued_by_the_Japanese_Government_during_the_occupation_of_Malaya%2C_North_Borneo%2C_Sarawak_and_Brunei_%281942%2C_obverse%29.jpg/1920px-Ten_dollar_note_issued_by_the_Japanese_Government_during_the_occupation_of_Malaya%2C_North_Borneo%2C_Sarawak_and_Brunei_%281942%2C_obverse%29.jpg",
    "NOTE1": f"{_C}/1/11/MAL-M5c-Malaya-Japanese_Occupation-One_Dollar_ND_%281942%29.jpg/1280px-MAL-M5c-Malaya-Japanese_Occupation-One_Dollar_ND_%281942%29.jpg",
    "CHART": f"{_A}/yokohama-specie-bank-timeline-chart.png",
    "ST1916": f"{_A}/straits-times-1916-09-05-page-8.jpg",
    "SB1930": f"{_A}/straits-budget-1930-12-04-page-2.jpg",
    "SY420317": f"{_A}/syonan-shimbun-1942-03-17-page-4.jpg",
    "SY420320": f"{_A}/syonan-shimbun-1942-03-20-page-2.jpg",
    "SY430211": f"{_A}/syonan-shimbun-1943-02-11-page-2.jpg",
    "SY440929": f"{_A}/syonan-shimbun-1944-09-29-page-2.jpg",
}

# Credits for images not captioned in the post or its gallery.
CREDITS = {
    "CHART": "Chart by Lesser Known Singapore, data per the post's own Sources list",
    "HONOLULU": "Joel Bradshaw, public domain, via Wikimedia Commons",
}

_E = "ease-in-out"
_IN = {"type": "cover", "zoom": [1.0, 1.06, 1.12], "pan": [(0.5, 0.5)] * 3, "ease": _E}
_OUT = {"type": "cover", "zoom": [1.12, 1.06, 1.0], "pan": [(0.5, 0.5)] * 3, "ease": _E}
_INL = {"type": "cover", "zoom": [1.0, 1.08, 1.16], "pan": [(0.35, 0.45)] * 3, "ease": _E}
_INR = {"type": "cover", "zoom": [1.0, 1.08, 1.16], "pan": [(0.65, 0.45)] * 3, "ease": _E}
# Tall photos (the Shanghai postcard, the wartime interior): letterbox, modest zoom.
_PORT = {"type": "letterbox", "zoom": [1.0, 1.04, 1.08], "pan": [(0.5, 0.5)] * 3, "ease": _E}
# Graphics (the chart): letterbox, frozen.
_GFX = {"type": "letterbox", "zoom": [1, 1, 1], "pan": [(0.5, 0.5)] * 3}


def _c(zoom, pan):
    return {"type": "cover", "zoom": zoom, "pan": pan, "ease": _E}


# Whole-page newspaper push-ins (cover_crop test frames), zoom capped at 2.4x.
_ST1916_N = _c([2.21, 2.3, 2.4], [(0.075, 0.908), (0.089, 0.904), (0.101, 0.9)])
_SB1930 = _c([1.0, 1.04, 1.08], [(0.0, 0.107), (0.0, 0.116), (0.0, 0.123)])
_SB1930_PHOTO = _c([1.5, 1.58, 1.66], [(0.4, 0.14), (0.42, 0.15), (0.44, 0.16)])
_SY0317_N = _c([2.21, 2.3, 2.4], [(1.0, 0.573), (1.0, 0.573), (1.0, 0.572)])
_SY0317_PAGE = _c([1.0, 1.03, 1.06], [(0.5, 0.0), (0.5, 0.03), (0.5, 0.06)])
_SY0320_N = _c([1.2, 1.26, 1.31], [(1.0, 0.425), (1.0, 0.426), (1.0, 0.427)])
_SY0320_NZ = _c([2.0, 2.15, 2.3], [(1.0, 0.42), (1.0, 0.44), (1.0, 0.46)])
_SY0211_AD = _c([2.2, 2.3, 2.4], [(0.76, 0.9), (0.75, 0.92), (0.74, 0.94)])
_SY0929_N = _c([2.15, 2.24, 2.33], [(0.416, 0.081), (0.419, 0.085), (0.421, 0.088)])
_SY0929_N2 = _c([2.21, 2.3, 2.4], [(0.418, 0.223), (0.42, 0.225), (0.423, 0.227)])
# Small or detailed photos: gentle moves only.
_CQ_HSBC = _c([1.25, 1.3, 1.35], [(0.85, 0.4), (0.8, 0.4), (0.75, 0.4)])
_NOTE = _c([1.0, 1.04, 1.08], [(0.4, 0.5), (0.5, 0.5), (0.6, 0.5)])

SLIDES = [
    {"img": "CQ1910", **_IN},             # 0  s0      title
    {"img": "SY420317", **_SY0317_N},     # 1  s1      reopened, 20 March 1942
    {"img": "SB1930", **_SB1930},         # 2  s2      not Meyer Chambers
    {"img": "SY420320", **_SY0320_N},     # 3  s3      "Late Hongkong and Shanghai Banking Corp."
    {"img": "HARB1930S", **_INL},         # 4  s4-5    since 1916, one of the exchange banks
    {"img": "HQ1923", **_IN},             # 5  s6-7    founded 1880; specie
    {"img": "SHANGHAI", **_PORT},         # 6  s8-9    quasi-governmental; 37 offices abroad
    {"img": "ST1916", **_ST1916_N},       # 7  s10     the 1916 agency notice
    {"img": "BONHAM", **_IN},             # 8  s11-12  the Bonham Building; 31-A Chulia Street
    {"img": "NAGASAKI", **_IN},           # 9  s13-14  First World War; trade finance
    {"img": "HONOLULU", **_INR},          # 10 s15-16  managers posted from other offices
    {"img": "CQ1900S", **_IN},            # 11 s17     Unagami's Rotary talk
    {"img": "SB1930", **_SB1930_PHOTO},   # 12 s18     the move to Meyer Chambers
    {"img": "HANKOU", **_IN},             # 13 s19     capital and branches
    {"img": "CQ1910", **_CQ_HSBC},        # 14 s20-21  the 1941 freeze
    {"img": "HSBC1900", **_IN},           # 15 s22     8 December 1941, arrests
    {"img": "HARB1930S", **_INR},         # 16 s23     internment in India
    {"img": "CQ1900S", **_OUT},           # 17 s24     the surrender
    {"img": "SY420317", **_SY0317_PAGE},  # 18 s25     the 17 March announcement
    {"img": "SY420320", **_SY0320_NZ},    # 19 s26-27  the change of addresses
    {"img": "SY430211", **_SY0211_AD},    # 20 s28     21 Collyer Quay; branches of the Southern Regions
    {"img": "JESSELTON", **_IN},          # 21 s29     currency exchange (the Jesselton branch)
    {"img": "NOTE10", **_NOTE},           # 22 s30     banana money
    {"img": "SY440929", **_SY0929_N},     # 23 s31-32  notice No. 52
    {"img": "SY440929", **_SY0929_N2},    # 24 s33-34  who it paid, and how much
    {"img": "CHART", **_GFX},             # 25 s35     the chart
    {"img": "WARTIME", **_PORT},          # 26 s36-37  closed; liquidated 1947
    {"img": "NOTE1", **_PORT},            # 27 s38-39  more than a decade to return
    {"img": "HSBC1900", **_OUT},          # 28 s40     local staff of the prewar branch
    {"img": "CQ1910", **_OUT},            # 29 s41-42  the Bank of Tokyo opens, 1957
    {"img": "HQTODAY", **_IN},            # 30 s43-44  MUFG
    {"img": "HARB1930S", **_OUT},         # 31 s45-46  then and now
    {"img": "BONHAM", **_OUT},            # 32 s47     where it fits
    {"img": "HQ1923", **_OUT},            # 33 s48     the arc
]

SCHEDULE = [
    (0.0, 0), (4.775, 1), (16.45, 2), (20.65, 3), (32.225, 4), (53.925, 5), (70.575, 6),
    (95.725, 7), (114.7, 8), (137.95, 9), (158.05, 10), (179.4, 11), (190.725, 12),
    (205.275, 13), (222.1, 14), (242.4, 15), (254.475, 16), (277.4, 17), (282.5, 18),
    (301.675, 19), (318.625, 20), (341.625, 21), (357.55, 22), (362.675, 23), (382.0, 24),
    (404.35, 25), (411.2, 26), (435.5, 27), (455.925, 28), (468.025, 29), (487.4, 30),
    (506.175, 31), (528.875, 32), (543.55, 33),
]
TOTAL_DURATION = 562.025
TIMING_JSON = "audio/the-yokohama-specie-bank-japans-bank-in-prewar-singapore.timing.json"

# The avatar presenter, Phase 1 test #4: corner bubble for the first and last 30 s.
AVATAR = {"ranges": [(0, 30), (-30, None)]}
