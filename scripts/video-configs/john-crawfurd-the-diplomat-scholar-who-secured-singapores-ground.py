"""Video config for the John Crawfurd post.

Eight images. HERO/BRIDGE/ISTANA are ordinary landscape photos and use
cover; FARQUHAR/CRAWFURD are portrait-oriented scans and use letterbox;
MAP1825/SETTLEMENT1828/CHRONICLE are period maps/plans/a newspaper
page with small text labels that cover would clip in the Watch
widget's variable-aspect display, so all three use letterbox too
(same rule as charts/OSM maps).

  HERO         - "View of the Town and Roads of Singapore from the
                 Government Hill," published 1828 in Crawfurd's own
                 account of his Siam/Cochinchina embassy (Commons,
                 Robert Elliot) - a period panorama of the settlement
  FARQUHAR     - Portrait of William Farquhar, c. 1830 (Commons) -
                 Singapore's first Resident, 1819-1823
  CRAWFURD     - John Crawfurd, photographed late 1850s (Commons, NPG
                 London) - the man himself
  MAP1825      - Hand-drawn survey of Singapore, 18 June 1825, less
                 than a year after the treaty (Commons, British
                 Library India Office Records)
  BRIDGE       - Crawford Bridge today, spanning the Rochor River
                 (Commons) - the misspelled present-day payoff
  ISTANA       - Istana Kampong Glam / Malay Heritage Centre today
                 (Commons) - the Sultan's compound, present day
  SETTLEMENT1828 - "Plan of the British Settlement of Singapore,"
                 published 1828 in Crawfurd's own book (Commons) -
                 the whole island plus the town plan
  CHRONICLE    - Front page of the Singapore Chronicle and Commercial
                 Register, 30 September 1837 (Commons, NLB) - a later
                 issue of the paper Crawfurd edited and part-financed,
                 added 2026-09-19 at Chris's request; swapped in for
                 slide 29 (was HERO), no re-sync needed (image-only
                 change, no narration/timing change)

40 slides, 475.325s.
"""

_U = "https://upload.wikimedia.org/wikipedia/commons"

IMAGES = {
    "HERO": f"{_U}/8/84/View_of_the_town_and_roads_of_Singapore_from_the_government_hill_published_1828.jpg",
    "FARQUHAR": f"{_U}/f/f9/Portrait_of_William_Farquhar_%28c._1830%29.jpg",
    "CRAWFURD": f"{_U}/3/32/John_Crawfurd.jpg",
    "MAP1825": f"{_U}/9/9f/Part_of_Singapore_Island_%28British_Library_India_Office_Records%2C_1825%2C_detail%29.jpg",
    "BRIDGE": f"{_U}/c/c9/Crawford_Bridge_-_2022-08-13.jpg",
    "ISTANA": f"{_U}/f/fe/Istana_kampong_glam_malay_heritage_centre_june_2009.jpg",
    "SETTLEMENT1828": f"{_U}/4/44/Plan_of_the_British_settlement_of_Singapore_published_1828.jpg",
    "CHRONICLE": f"{_U}/4/40/Singapore_Chronicle_and_Commercial_Register%2C_30_September_1837.png",
}

_CVZ = {"type": "cover", "zoom": [1.0, 1.06, 1.12], "pan": [(0.5, 0.5)] * 3, "ease": "ease-in-out"}
_CVZO = {"type": "cover", "zoom": [1.12, 1.06, 1.0], "pan": [(0.5, 0.5)] * 3, "ease": "ease-out"}
_LTB = {"type": "letterbox", "zoom": [1.0, 1.04, 1.08], "pan": [(0.5, 0.5)] * 3, "ease": "ease-in-out"}
_LTBO = {"type": "letterbox", "zoom": [1.08, 1.04, 1.0], "pan": [(0.5, 0.5)] * 3, "ease": "ease-out"}

SLIDES = [
    {"img": "HERO", **_CVZ},            # 0  s0   title
    {"img": "HERO", **_CVZO},           # 1  s1   Raffles's name stamped across Singapore
    {"img": "BRIDGE", **_CVZ},          # 2  s2   all three spell his name wrong
    {"img": "HERO", **_CVZ},            # 3  s3   what Raffles obtained 1819, a factory
    {"img": "ISTANA", **_CVZO},         # 4  s4   Sultan Hussein installed as rival
    {"img": "ISTANA", **_CVZ},          # 5  s5   the Temenggong who co-signed
    {"img": "SETTLEMENT1828", **_LTB},  # 6  s6   Dutch objected, not obviously legal
    {"img": "FARQUHAR", **_LTB},        # 7  s7   the man who ran the settlement, "Resident"
    {"img": "FARQUHAR", **_LTBO},       # 8  s8   Raffles based in Bencoolen, distant superior
    {"img": "FARQUHAR", **_LTB},        # 9  s9   Farquhar held the post 4.5 years, dismissed
    {"img": "FARQUHAR", **_LTBO},       # 10 s10  what matters is simpler, still unresolved
    {"img": "CRAWFURD", **_LTB},        # 11 s11  his replacement, an unusual choice
    {"img": "CRAWFURD", **_LTBO},       # 12 s12  born 1783 Islay, Edinburgh, surgeon
    {"img": "CRAWFURD", **_LTB},        # 13 s13  Penang 1808, Malay scholar, met Raffles
    {"img": "CRAWFURD", **_LTBO},       # 14 s14  followed Raffles to Java, Yogyakarta
    {"img": "CRAWFURD", **_LTB},        # 15 s15  History of the Indian Archipelago, 1816
    {"img": "CRAWFURD", **_LTBO},       # 16 s16  1821 Siam and Cochinchina mission
    {"img": "CRAWFURD", **_LTB},        # 17 s17  arrived second Resident, 9 June 1823
    {"img": "HERO", **_CVZO},           # 18 s18  two things happened in 1824
    {"img": "SETTLEMENT1828", **_LTBO}, # 19 s19  March, Anglo-Dutch Treaty of London
    {"img": "SETTLEMENT1828", **_LTB},  # 20 s20  resolved the international dispute
    {"img": "MAP1825", **_LTB},         # 21 s21  did nothing to resolve the local one
    {"img": "CRAWFURD", **_LTBO},       # 22 s22  Crawfurd closed that gap, 2 August 1824
    {"img": "MAP1825", **_LTBO},        # 23 s23  ceded in full sovereignty and property
    {"img": "MAP1825", **_LTB},         # 24 s24  a separate article abrogated
    {"img": "ISTANA", **_CVZO},         # 25 s25  Sultan received 33,200 dollars, Temenggong
    {"img": "SETTLEMENT1828", **_LTBO}, # 26 s26  Lord Amherst ratified it that November
    {"img": "MAP1825", **_LTB},         # 27 s27  a dry legal document next to Raffles's landing
    {"img": "HERO", **_CVZ},            # 28 s28  Crawfurd's instructions, reclamation work
    {"img": "CHRONICLE", **_LTB},       # 29 s29  Singapore Chronicle, the first newspaper
    {"img": "ISTANA", **_CVZ},          # 30 s30  moved against slavery, freed the women
    {"img": "HERO", **_CVZ},            # 31 s31  trade and population kept climbing
    {"img": "CRAWFURD", **_LTBO},       # 32 s32  left Singapore, 14 August 1826
    {"img": "BRIDGE", **_CVZO},         # 33 s33  Crawford Street, Lane, Bridge and Park
    {"img": "CRAWFURD", **_LTB},        # 34 s34  long second career, free trade
    {"img": "HERO", **_CVZO},           # 35 s35  why it matters today, Raffles picked the site
    {"img": "FARQUHAR", **_LTB},        # 36 s36  Farquhar spent 4.5 years actually building
    {"img": "MAP1825", **_LTBO},        # 37 s37  Crawfurd sat down with them a second time
    {"img": "HERO", **_CVZ},            # 38 s38  Singapore remembers the first two names
    {"img": "BRIDGE", **_CVZ},          # 39 s39  the one that closed the deal, misspelled
]

SCHEDULE = [
    (0.0, 0), (5.575, 1), (31.4, 2), (34.2, 3), (45.1, 4),
    (62.725, 5), (75.125, 6), (82.55, 7), (103.45, 8), (113.35, 9),
    (125.55, 10), (136.45, 11), (142.25, 12), (154.725, 13), (167.175, 14),
    (182.55, 15), (198.025, 16), (216.7, 17), (231.975, 18), (238.625, 19),
    (256.875, 20), (260.3, 21), (274.375, 22), (279.475, 23), (303.7, 24),
    (309.925, 25), (329.625, 26), (335.05, 27), (348.2, 28), (359.025, 29),
    (371.825, 30), (394.575, 31), (403.4, 32), (415.725, 33), (425.8, 34),
    (438.625, 35), (445.425, 36), (451.775, 37), (467.175, 38), (470.875, 39),
]
TOTAL_DURATION = 475.325
TIMING_JSON = "audio/john-crawfurd-the-diplomat-scholar-who-secured-singapores-ground.timing.json"
