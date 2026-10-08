"""Video config for the Endau settlement post.

There are no photos of the wartime settlement itself, so the two Syonan
Shimbun pages carry it: 2 February 1944 pushed in on "First Batch Of Settlers
Leave For New Syonan" (top centre) and then down its column, and 14 December
1944 pushed in on the first-anniversary report (left). Endau is shown in 1964
and on the 1976 ferry photos; the map and the two charts (letterbox, frozen)
take the plan, the rations and today's targets. Shinozaki, Huang Qiuhong, Wan
Leong Gay and Tan Ean Teck have no free photos, so their sentences show no
person. The close moves to today's container port and a local farm. Small
scans and square photos are letterboxed, not zoomed.

43 slides, 593.8s. AVATAR: first and last 30s (avatar test #9, cartoon).
"""

_U = "https://upload.wikimedia.org/wikipedia/commons"
_C = f"{_U}/thumb"
_A = "/assets/images"

IMAGES = {
    "HERO": f"{_C}/b/bb/Endau_Malaya_February_1964.jpg/1280px-Endau_Malaya_February_1964.jpg",
    "FEB2": f"{_A}/syonan-shimbun-1944-02-02-page-2.jpg",
    "DEC14": f"{_A}/syonan-shimbun-1944-12-14-page-2.jpg",
    "MAP": f"{_A}/endau-bahau-map.png",
    "RICE": f"{_A}/endau-rice-ration-chart.png",
    "FOOD": f"{_A}/singapore-local-food-share-chart.png",
    "LBK30": f"{_U}/c/c7/Lim_Boon_Keng%2C_1930s.jpg",
    "LBK29": f"{_U}/c/cd/%E6%9E%97%E6%96%87%E6%85%B6.jpg",
    "MPAJA": f"{_U}/8/81/The_British_Reoccupation_of_Malaya_SE5878.jpg",
    "MPAJA3": f"{_U}/5/5d/The_British_Reoccupation_of_Malaya_SE5883.jpg",
    "DOWNTOWN": f"{_C}/5/58/Downtown_Singapore_%28Syonan%29%2C_Djawa_Baroe%2C_Vol._1%2C_Iss._4_%281943-02-15%29%2C_p18.jpg/1280px-Downtown_Singapore_%28Syonan%29%2C_Djawa_Baroe%2C_Vol._1%2C_Iss._4_%281943-02-15%29%2C_p18.jpg",
    "CAUSEWAY": f"{_C}/c/c4/Djohor_Baru_Bridge_in_Singapore_%28Syonan%29%2C_Djawa_Baroe%2C_Vol._1%2C_Iss._4_%281943-02-15%29%2C_pp18-19.jpg/1280px-Djohor_Baru_Bridge_in_Singapore_%28Syonan%29%2C_Djawa_Baroe%2C_Vol._1%2C_Iss._4_%281943-02-15%29%2C_pp18-19.jpg",
    "JBROAD": f"{_C}/8/86/KITLV_A1363_-_Weg_van_Djohor_Bahru_naar_Singapore%2C_KITLV_78456.tiff/lossy-page1-1280px-KITLV_A1363_-_Weg_van_Djohor_Bahru_naar_Singapore%2C_KITLV_78456.tiff.jpg",
    "CASSAVA": f"{_U}/0/01/Cassava_harvesting.jpg",
    "FERRY1": f"{_C}/1/17/Endau_River-02-Faehre-1976-gje.jpg/1280px-Endau_River-02-Faehre-1976-gje.jpg",
    "FERRY2": f"{_C}/b/b1/Endau_River-04-Faehre-Landeplatz-1976-gje.jpg/1280px-Endau_River-04-Faehre-Landeplatz-1976-gje.jpg",
    "FERRY3": f"{_C}/3/3e/Endau_River-06-Faehre-Warteschlange-1976-gje.jpg/1280px-Endau_River-06-Faehre-Warteschlange-1976-gje.jpg",
    "SURR": f"{_U}/4/40/Japanese_Surrender_in_Malaya%2C_1945_IND4845.jpg",
    "LIBERATION": f"{_U}/9/93/Liberation_banner.jpg",
    # From earlier posts or not in this post's captions (credited below):
    "SYOMAP": f"{_C}/4/4a/SyonanSingapore.jpg/1920px-SyonanSingapore.jpg",
    "CHAMBER": f"{_U}/e/e7/Singapore_Chinese_Chamber_of_Commerce_%26_Industry_Building%2C_Aug_06.JPG",
    "SHIP": f"{_C}/e/e6/Maersk_Huacho_container_ship_at_Pasir_Panjang_Container_Terminal.jpg/1280px-Maersk_Huacho_container_ship_at_Pasir_Panjang_Container_Terminal.jpg",
    "PORT": f"{_C}/7/7f/Pasir_Panjang_Container_Terminal%2C_Singapore_-_20110227-01.jpg/1280px-Pasir_Panjang_Container_Terminal%2C_Singapore_-_20110227-01.jpg",
    "FARM": f"{_C}/c/cf/Kok_Fah_Technology_Farm.jpg/1280px-Kok_Fah_Technology_Farm.jpg",
}

# Credits for images not captioned in the post or its gallery.
CREDITS = {
    "RICE": "Chart by Lesser Known Singapore, from BiblioAsia (2019) and a National Archives of Singapore oral history",
    "FOOD": "Chart by Lesser Known Singapore, figures from the Singapore Food Agency's Singapore Food Statistics 2025",
    "SYOMAP": "A Japanese map of Syonan-to, 1942, Magyer Lohasa, CC BY-SA 4.0, via Wikimedia Commons",
    "CHAMBER": "The Singapore Chinese Chamber of Commerce and Industry, Hill Street, 2006, Sengkang, copyrighted free use, via Wikimedia Commons",
    "SHIP": "A container ship at Pasir Panjang Container Terminal, 2021, Wzhkevin, CC BY-SA 4.0, via Wikimedia Commons",
    "PORT": "Pasir Panjang Container Terminal, 2011, Jacklee, CC BY-SA 3.0, via Wikimedia Commons",
    "FARM": "Kok Fah Technology Farm, 2020, Kok Fah Technology Farm, CC BY-SA 4.0, via Wikimedia Commons",
}

_E = "ease-in-out"
_IN = {"type": "cover", "zoom": [1.0, 1.06, 1.12], "pan": [(0.5, 0.5)] * 3, "ease": _E}
_OUT = {"type": "cover", "zoom": [1.12, 1.06, 1.0], "pan": [(0.5, 0.5)] * 3, "ease": _E}
# Small scans, square and tall photos: letterbox, modest zoom (no zoom on grainy photos).
_PORT = {"type": "letterbox", "zoom": [1.0, 1.04, 1.08], "pan": [(0.5, 0.5)] * 3, "ease": _E}
# The map and charts: letterbox, frozen.
_GFX = {"type": "letterbox", "zoom": [1, 1, 1], "pan": [(0.5, 0.5)] * 3}


def _c(zoom, pan):
    return {"type": "cover", "zoom": zoom, "pan": pan, "ease": _E}


# Whole-page newspaper push-ins (1600px-wide pages), zoom capped at 2.4x.
_FEB2_HEAD = _c([2.0, 2.1, 2.2], [(0.38, 0.0), (0.385, 0.0), (0.39, 0.0)])                # headline, top centre
_FEB2_COL = _c([2.2, 2.3, 2.4], [(0.289, 0.047), (0.297, 0.089), (0.303, 0.13)])       # down the story's column
_FEB2_PAGE = _c([1.0, 1.04, 1.08], [(0.5, 0.0), (0.5, 0.03), (0.5, 0.06)])
_DEC14_HEAD = _c([2.0, 2.1, 2.2], [(0.06, 0.294), (0.08, 0.296), (0.097, 0.298)])        # the anniversary report, left
_DEC14_COL = _c([1.8, 1.85, 1.9], [(0.005, 0.376), (0.021, 0.401), (0.036, 0.426)])
_DEC14_PAGE = _c([1.0, 1.04, 1.08], [(0.5, 0.2), (0.5, 0.25), (0.5, 0.3)])

SLIDES = [
    {"img": "HERO", **_IN},             # 0  s0      title
    {"img": "FEB2", **_FEB2_HEAD},      # 1  s1      1 February 1944: the first party leaves
    {"img": "FEB2", **_FEB2_PAGE},      # 2  s2      "pioneers in every sense of the word"
    {"img": "CAUSEWAY", **_IN},         # 3  s3      families, Po Leung Kok girls, labourers
    {"img": "DEC14", **_DEC14_HEAD},    # 4  s4      7,000 settlers within a year
    {"img": "DOWNTOWN", **_PORT},       # 5  s5      Syonan did not have enough to eat
    {"img": "SYOMAP", **_IN},           # 6  s6-7    imported rice; the shipping lost
    {"img": "RICE", **_GFX},            # 7  s8-9    the ration, 20 katis down to 8, 6, 4
    {"img": "CASSAVA", **_PORT},        # 8  s10-11  Grow More Food; tapioca on the Padang
    {"img": "MAP", **_GFX},             # 9  s12-13  the plan to move people out
    {"img": "CHAMBER", **_IN},          # 10 s14     Shinozaki and the association (no photo of him)
    {"img": "MAP", **_GFX},             # 11 s15-16  two sites: Endau and Bahau
    {"img": "LBK30", **_PORT},          # 12 s17     $2 million; Lim Boon Keng
    {"img": "FERRY1", **_IN},           # 13 s18     inspection parties; the flag raised
    {"img": "CHAMBER", **_OUT},         # 14 s19     the promises
    {"img": "LBK29", **_PORT},          # 15 s20     run by the Chinese themselves
    {"img": "FERRY2", **_IN},           # 16 s21     free to come and go (Huang; no photo)
    {"img": "FEB2", **_FEB2_COL},       # 17 s22-23  the send-off; lorry loads of rice
    {"img": "JBROAD", **_IN},           # 18 s24     city people, few farmers
    {"img": "FERRY3", **_IN},           # 19 s25-26  longhouses; three acres a family
    {"img": "CASSAVA", **_PORT},        # 20 s27     what they grew
    {"img": "HERO", **_OUT},            # 21 s28     the hospital; quinine
    {"img": "RICE", **_GFX},            # 22 s29-30  18 katis, then 4 or 5
    {"img": "FERRY1", **_OUT},          # 23 s31     trade with Malay villages
    {"img": "DEC14", **_DEC14_HEAD},    # 24 s32-33  the first-anniversary report
    {"img": "DEC14", **_DEC14_COL},     # 25 s34-35  buildings, acres, "in abundance"
    {"img": "RICE", **_GFX},            # 26 s36-37  the shrinking ration; 12,000
    {"img": "MPAJA", **_PORT},          # 27 s38-39  the guerrillas; convoys ambushed
    {"img": "MPAJA3", **_PORT},         # 28 s40-41  19 April 1944 (no photo of Tan Ean Teck)
    {"img": "FERRY2", **_OUT},          # 29 s42     killings inside the settlement
    {"img": "SYOMAP", **_OUT},          # 30 s43     Shinozaki's truce (no photo of him)
    {"img": "MAP", **_GFX},             # 31 s44-46  Bahau, a month earlier; it fared worse
    {"img": "JBROAD", **_OUT},          # 32 s47     the deaths at Bahau
    {"img": "HERO", **_IN},             # 33 s48-49  Endau fared better
    {"img": "SURR", **_PORT},           # 34 s50     Japan surrenders
    {"img": "LIBERATION", **_PORT},     # 35 s50     the settlers return to Singapore
    {"img": "SHIP", **_IN},             # 36 s51-52  more than 90% imported
    {"img": "PORT", **_IN},             # 37 s53-54  "30 by 30", then Singapore Food Story 2
    {"img": "FOOD", **_GFX},            # 38 s55     20% fibre, 30% protein by 2035
    {"img": "FARM", **_IN},             # 39 s56     four measures
    {"img": "FEB2", **_FEB2_HEAD},      # 40 s57-58  the wartime answer: move people out
    {"img": "SHIP", **_OUT},            # 41 s59     today: no single source can fail
    {"img": "DEC14", **_DEC14_PAGE},    # 42 s60     why it matters
]

SCHEDULE = [
    (0, 0), (4.3, 1), (19.625, 2), (24.675, 3), (39.325, 4), (44.625, 5), (52.025, 6), (70.825, 7),
    (94.175, 8), (113.975, 9), (134.4, 10), (150.75, 11), (173.5, 12), (182.75, 13), (196.625, 14),
    (208.8, 15), (212.775, 16), (226.95, 17), (244.925, 18), (251.75, 19), (268.825, 20),
    (276.375, 21), (286.075, 22), (304.375, 23), (313.175, 24), (332.05, 25), (350.2, 26),
    (369.775, 27), (385.425, 28), (407, 29), (413.325, 30), (427, 31), (449.625, 32),
    (461.675, 33), (474.075, 34), (478.725, 35), (483.45, 36), (501.55, 37), (525.475, 38),
    (540.5, 39), (550.3, 40), (563, 41), (574.3, 42),
]
TOTAL_DURATION = 593.8
TIMING_JSON = "audio/new-syonan-the-endau-settlement-1943.timing.json"

# The avatar presenter, cartoon, test #9: corner bubble for the first and last 30 s.
AVATAR = {"ranges": [(0, 30), (-30, None)]}
