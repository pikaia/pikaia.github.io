"""Video config for the $50 million "gift" post.

The two Syonan Times pages carry the story: 26 June 1942 pushed in on the
"$50 Million Gift By Chinese" headline and the photo of Yamashita taking the
cheque from Lim Boon Keng (top right), and 23 June pushed in on the notice to
contributors (centre). The chart (letterbox, frozen) returns for the demand,
the shortfall and the scale. The occupation banknotes run under the currency
sentences, in order of issue. Shinozaki has no free photo, so his sentences
sit on the 1942 map and the trials photo, never another man's portrait. Lim
Boon Keng's sentences are on his own portraits and grave. Small scans and tall
portraits are letterboxed, not zoomed.

43 slides, 519.475s. AVATAR: first and last 30s (avatar test #8, cartoon).
"""

_U = "https://upload.wikimedia.org/wikipedia/commons"
_C = f"{_U}/thumb"
_A = "/assets/images"

IMAGES = {
    "HERO": f"{_U}/2/21/Yamashita_e_Suzuki.jpg",
    "ST26": f"{_A}/syonan-shimbun-1942-06-26-page-2.jpg",
    "ST23": f"{_A}/syonan-shimbun-1942-06-23-page-3.jpg",
    "CHART": f"{_A}/fifty-million-gift-chart.png",
    "LBK30": f"{_U}/c/c7/Lim_Boon_Keng%2C_1930s.jpg",
    "LBK29": f"{_U}/c/cd/%E6%9E%97%E6%96%87%E6%85%B6.jpg",
    "GRAVE": f"{_C}/7/77/Gravestone_of_Lim_Boon_Keng_and_Grace_Pek_Ha_Yin%2C_Bidadari_Garden%2C_Singapore_-_20121008.jpg/1920px-Gravestone_of_Lim_Boon_Keng_and_Grace_Pek_Ha_Yin%2C_Bidadari_Garden%2C_Singapore_-_20121008.jpg",
    "CHAMBER": f"{_U}/e/e7/Singapore_Chinese_Chamber_of_Commerce_%26_Industry_Building%2C_Aug_06.JPG",
    "YAMA": f"{_U}/f/f5/Yamashita_Tomoyuki.jpg",
    "STAMPS": f"{_U}/f/f0/1942_Fall_of_Singapore_for_Japanese_stamps.JPG",
    "SYOMAP": f"{_C}/4/4a/SyonanSingapore.jpg/1920px-SyonanSingapore.jpg",
    "DJ1": f"{_U}/8/8d/%27Celebration%27_of_Japanese_victory_in_Singapore_%28Syonan%29%2C_Djawa_Baroe%2C_Vol._1%2C_Iss._7_%281943-04-01%29%2C_p28.jpg",
    "DJ2": f"{_U}/f/ff/Commemoration_of_anniversary_of_occupation_in_Asia_Raya_theatre%2C_Singapore_%28Syonan%29%2C_Djawa_Baroe%2C_Vol._1%2C_Iss._5_%281943-03-01%29%2C_p31.jpg",
    "N1": f"{_C}/1/11/MAL-M5c-Malaya-Japanese_Occupation-One_Dollar_ND_%281942%29.jpg/1920px-MAL-M5c-Malaya-Japanese_Occupation-One_Dollar_ND_%281942%29.jpg",
    "N5": f"{_C}/5/51/MAL-M6c-Malaya-Japanese_Occupation-Five_Dollars_ND_%281942%29.jpg/1920px-MAL-M6c-Malaya-Japanese_Occupation-Five_Dollars_ND_%281942%29.jpg",
    "N100": f"{_C}/d/d2/MAL-M8b-Malaya-Japanese_Occupation-100_Dollars_ND_%281944%29.jpg/1920px-MAL-M8b-Malaya-Japanese_Occupation-100_Dollars_ND_%281944%29.jpg",
    "N1000": f"{_C}/d/d6/MAL-M10b-Malaya-Japanese_Occupation-1000_Dollars_ND_%281945%29.jpg/1920px-MAL-M10b-Malaya-Japanese_Occupation-1000_Dollars_ND_%281945%29.jpg",
    "TRIALS": f"{_U}/5/5f/War_crimes_trials_at_Singapore.jpg",
    "CWM": f"{_C}/a/a2/Singapore_Civilian-War-Memorial-01.jpg/1920px-Singapore_Civilian-War-Memorial-01.jpg",
    # From earlier posts (credited below):
    "TKK1946": f"{_U}/a/a6/Tan_Kah_Kee%2C_Lee_Kong_Chian%2C_and_Tan_Lark_Sye%2C_1946.png",
    "BURMA": f"{_U}/6/6c/%E6%BB%87%E7%BC%85%E5%85%AC%E8%B7%AF01.jpg",
    "MARCH": f"{_U}/1/15/JapaneseMarchSgpCity.jpg",
    "ITEMS": f"{_U}/a/a4/Items_found_in_mass_graves_due_to_the_Sook_Ching_massacre_of_1942_by_the_Japanese.jpg",
    "WARTIME": f"{_U}/2/26/Yokohama_Specie_Bank_during_World_War_II.JPG",
    "SURRENDER": f"{_U}/9/9e/Japanese_surrender_at_Singapore%2C_1945.jpg",
    "CWM3": f"{_U}/2/27/Civilian_War_Memorial%2C_Singapore-3276.jpg",
    "CWM2": f"{_C}/7/72/Civilian_War_Memorial%2C_Singapore_-_20131117.jpg/1920px-Civilian_War_Memorial%2C_Singapore_-_20131117.jpg",
}

# Credits for images not captioned in the post or its gallery.
CREDITS = {
    "TKK1946": "Tan Kah Kee, Lee Kong Chian and Tan Lark Sye in about 1946, Tan Kah Kee Memorial Museum, public domain, via Wikimedia Commons",
    "BURMA": "Lorries on the Yunnan-Burma Road in 1940, Xiao Qian and Kuang Guang, public domain, via Wikimedia Commons",
    "MARCH": "Japanese troops marching through Singapore's city centre, February 1942, Imperial War Museums, public domain, via Wikimedia Commons",
    "ITEMS": "Personal items recovered from Sook Ching mass graves, on display at the National Museum of Singapore, Wombatjpw, CC BY-SA 4.0, via Wikimedia Commons",
    "WARTIME": "Inside the Yokohama Specie Bank in Japan, 25 May 1944, unknown photographer, public domain, via Wikimedia Commons",
    "SURRENDER": "The Japanese surrender at Singapore, 12 September 1945, Royal Navy official photographer, public domain, via Wikimedia Commons",
    "CWM3": "The Civilian War Memorial, Beach Road, Bijay Chaurasia, CC BY-SA 4.0, via Wikimedia Commons",
    "CWM2": "The Civilian War Memorial, Singapore, 2013, Clay Gilliland, CC BY-SA 2.0, via Wikimedia Commons",
}

_E = "ease-in-out"
_IN = {"type": "cover", "zoom": [1.0, 1.06, 1.12], "pan": [(0.5, 0.5)] * 3, "ease": _E}
_OUT = {"type": "cover", "zoom": [1.12, 1.06, 1.0], "pan": [(0.5, 0.5)] * 3, "ease": _E}
# Small scans, banknotes and tall photos: letterbox, modest zoom (no zoom on grainy photos).
_PORT = {"type": "letterbox", "zoom": [1.0, 1.04, 1.08], "pan": [(0.5, 0.5)] * 3, "ease": _E}
# The chart: letterbox, frozen.
_GFX = {"type": "letterbox", "zoom": [1, 1, 1], "pan": [(0.5, 0.5)] * 3}


def _c(zoom, pan):
    return {"type": "cover", "zoom": zoom, "pan": pan, "ease": _E}


# Whole-page newspaper push-ins (1600x2046 pages), zoom capped at 2.4x.
_ST26_HEAD = _c([2.2, 2.3, 2.4], [(1.0, 0.075), (1.0, 0.08), (1.0, 0.084)])       # headline + cheque photo, top right
_ST26_PAGE = _c([1.0, 1.04, 1.08], [(0.5, 0.0), (0.5, 0.03), (0.5, 0.06)])        # the page from the top
_ST23_NOTE = _c([2.2, 2.3, 2.4], [(0.482, 0.687), (0.482, 0.685), (0.483, 0.684)])  # the contributors' notice
_ST23_PAGE = _c([1.0, 1.04, 1.08], [(0.5, 0.25), (0.5, 0.3), (0.5, 0.35)])

SLIDES = [
    {"img": "HERO", **_IN},             # 0  s0      title
    {"img": "ST26", **_ST26_HEAD},      # 1  s1      Lim Boon Keng hands Yamashita the cheque
    {"img": "ST26", **_ST26_PAGE},      # 2  s2      "voluntary gift"
    {"img": "DJ2", **_IN},              # 3  s3      demanded; half borrowed
    {"img": "TKK1946", **_PORT},        # 4  s4-5    prewar relief funds, Tan Kah Kee
    {"img": "BURMA", **_IN},            # 5  s5      the Burma Road volunteers
    {"img": "MARCH", **_IN},            # 6  s6      Singapore falls; the Chinese treated as hostile
    {"img": "ITEMS", **_PORT},          # 7  s7      the Sook Ching
    {"img": "SYOMAP", **_IN},           # 8  s8      Shinozaki gathers the leaders (no photo of him)
    {"img": "CHAMBER", **_IN},          # 9  s9      formed at the Chinese Chamber, Hill Street
    {"img": "LBK29", **_PORT},          # 10 s10     Lim Boon Keng, chairman
    {"img": "CHAMBER", **_OUT},         # 11 s11-12  a body to speak for the community
    {"img": "CHART", **_GFX},           # 12 s13     $50 million: $10m and $40m
    {"img": "DJ1", **_IN},              # 13 s14     the deadlines
    {"img": "STAMPS", **_PORT},         # 14 s15     the levy rates
    {"img": "LBK30", **_PORT},          # 15 s16     Lim Boon Keng's own $2,200
    {"img": "DJ2", **_OUT},             # 16 s17     the Malaya-wide body
    {"img": "CHART", **_GFX},           # 17 s18-19  $28 million raised
    {"img": "ST23", **_ST23_NOTE},      # 18 s20     the notice of 23 June
    {"img": "WARTIME", **_PORT},        # 19 s21     the loan from the Yokohama Specie Bank
    {"img": "N1", **_PORT},             # 20 s22-23  6 per cent; owed with interest
    {"img": "HERO", **_OUT},            # 21 s24     the cheque handed over
    {"img": "ST26", **_ST26_HEAD},      # 22 s25     the report and photograph
    {"img": "ST26", **_ST26_PAGE},      # 23 s26-27  said nothing of the levy or the loan
    {"img": "CHART", **_GFX},           # 24 s28-29  against $220 million
    {"img": "N5", **_PORT},             # 25 s30     the occupation currency
    {"img": "N100", **_PORT},           # 26 s31     its value collapsed
    {"img": "N1000", **_PORT},          # 27 s32     a heavy sum in 1942
    {"img": "WARTIME", **_PORT},        # 28 s33     the loan's fate unrecorded
    {"img": "SURRENDER", **_IN},        # 29 s34     the bank closed after the surrender
    {"img": "DJ1", **_OUT},             # 30 s35-36  how the community judged it
    {"img": "LBK30", **_PORT},          # 31 s37     Lim Boon Keng in the Occupation
    {"img": "GRAVE", **_IN},            # 32 s38     died 1 January 1957
    {"img": "ST23", **_ST23_PAGE},      # 33 s39     Tan Yeok Seong's account (no photo of him)
    {"img": "TRIALS", **_PORT},         # 34 s40     Shinozaki a witness at the trials
    {"img": "SYOMAP", **_OUT},          # 35 s41-42  his memoir
    {"img": "ITEMS", **_PORT},          # 36 s43-44  the mass graves; the blood debt
    {"img": "CWM2", **_PORT},           # 37 s45     the 1966 settlement
    {"img": "CWM", **_PORT},            # 38 s46     the memorial
    {"img": "CHART", **_GFX},           # 39 s47     two sums alike in size
    {"img": "YAMA", **_PORT},           # 40 s48     set by an occupying army
    {"img": "CWM3", **_PORT},           # 41 s49     agreed between two governments
    {"img": "ST26", **_ST26_PAGE},      # 42 s50     why it matters
]

SCHEDULE = [
    (0.0, 0), (4.45, 1), (25.675, 2), (35.65, 3), (49.675, 4), (68.5, 5), (77.6, 6), (86.725, 7),
    (93.7, 8), (103.25, 9), (113.4, 10), (126.9, 11), (137.85, 12), (153.075, 13), (161.375, 14),
    (176.675, 15), (186.575, 16), (197.6, 17), (212.95, 18), (225.725, 19), (245.0, 20),
    (264.375, 21), (268.4, 22), (281.5, 23), (290.425, 24), (312.275, 25), (322.65, 26),
    (332.775, 27), (341.525, 28), (349.65, 29), (361.025, 30), (380.7, 31), (391.175, 32),
    (398.325, 33), (409.65, 34), (418.025, 35), (440.55, 36), (455.625, 37), (470.975, 38),
    (479.3, 39), (484.775, 40), (493.175, 41), (498.55, 42),
]
TOTAL_DURATION = 519.475
TIMING_JSON = "audio/the-50-million-gift-of-1942.timing.json"

# The avatar presenter, cartoon, test #8: corner bubble for the first and last 30 s.
AVATAR = {"ranges": [(0, 30), (-30, None)]}
