"""Video config for the newspapers post ("Who Pays for the News?").

Photo pool is thin (the Raffles Place views, the Straits Times office c.1900 at
Finlayson Green, and Mediacorp's campus today), so photos repeat with different
pans; two self-rendered timeline charts carry the dated sentences.

  HERO/R1890/R1910/R1910K/PV03 - Raffles Place views, 1885-1910 (Commons, public domain)
  STOFF   - Finlayson Green with the Straits Times office, c.1900 (Commons, public domain)
  MC      - Mediacorp Campus today (Commons, CC0)
  CH1     - scripts/render_newspapers_charts.py (1824-1846 timeline)
  CH2     - same script (2005-2025 timeline)

43 slides, one per sentence.
"""

IMAGES = {
    "HERO": "https://upload.wikimedia.org/wikipedia/commons/thumb/9/9f/KITLV_-_103746_-_Lambert_%26_Co._-_Raffles_Place_in_Singapore_-_circa_1885.tif/lossy-page1-1280px-KITLV_-_103746_-_Lambert_%26_Co._-_Raffles_Place_in_Singapore_-_circa_1885.tif.jpg",
    "R1910": "https://upload.wikimedia.org/wikipedia/commons/thumb/c/c7/KITLV_-_79892_-_Kleingrothe%2C_C.J._-_Medan_-_Raffles_Place%2C_Singapore_-_circa_1910.tif/lossy-page1-1280px-KITLV_-_79892_-_Kleingrothe%2C_C.J._-_Medan_-_Raffles_Place%2C_Singapore_-_circa_1910.tif.jpg",
    "R1890": "https://upload.wikimedia.org/wikipedia/commons/thumb/8/8d/KITLV_-_103753_-_Raffles_Place%2C_Singapore_-_circa_1890.tif/lossy-page1-1280px-KITLV_-_103753_-_Raffles_Place%2C_Singapore_-_circa_1890.tif.jpg",
    "PV03": "https://upload.wikimedia.org/wikipedia/commons/4/44/Photographic_Views_of_Singapore_Plate_03_Raffles%27_Square.jpg",
    "R1910K": "https://upload.wikimedia.org/wikipedia/commons/thumb/8/85/KITLV_-_79893_-_Kleingrothe%2C_C.J._-_Medan_-_Raffles_Place_and_King_Street_in_Singapore_-_circa_1910.tif/lossy-page1-1280px-KITLV_-_79893_-_Kleingrothe%2C_C.J._-_Medan_-_Raffles_Place_and_King_Street_in_Singapore_-_circa_1910.tif.jpg",
    "STOFF": "https://upload.wikimedia.org/wikipedia/commons/thumb/9/97/KITLV_-_50209_-_Lambert_%26_Co.%2C_G.R._-_Singapore_-_Finlayson_Green_with_the_office_of_the_Dutch_East_India_Commercial_Bank%2C_the_Straits_Times_and_the_Royal_Packet_Company_in_Singapore_-_circa_1900.jpg/1280px-KITLV_-_50209_-_Lambert_%26_Co.%2C_G.R._-_Singapore_-_Finlayson_Green_with_the_office_of_the_Dutch_East_India_Commercial_Bank%2C_the_Straits_Times_and_the_Royal_Packet_Company_in_Singapore_-_circa_1900.jpg",
    "MC": "https://upload.wikimedia.org/wikipedia/commons/9/94/224_Mediacorp_Campus_Building.jpg",
    "CH1": "/assets/images/newspapers-1824-1846-chart.png",
    "CH2": "/assets/images/newspapers-2005-2025-chart.png",
}

CREDITS = {
    "CH1": "Chart by Lesser Known Singapore, dates per the post's own Sources list",
    "CH2": "Chart by Lesser Known Singapore, figures per the post's own Sources list",
}

_PA = {"type": "cover", "zoom": [1.0, 1.05, 1.1], "pan": [(0.5, 0.4), (0.5, 0.5), (0.5, 0.6)], "ease": "ease-in-out"}
_PB = {"type": "cover", "zoom": [1.1, 1.05, 1.0], "pan": [(0.5, 0.6), (0.5, 0.5), (0.5, 0.4)], "ease": "ease-in-out"}
_STA = {"type": "cover", "zoom": [1.1, 1.15, 1.2], "pan": [(0.55, 0.5), (0.64, 0.5), (0.72, 0.5)], "ease": "ease-in-out"}
_STB = {"type": "cover", "zoom": [1.2, 1.15, 1.1], "pan": [(0.72, 0.5), (0.64, 0.5), (0.55, 0.5)], "ease": "ease-in-out"}
_CHART = {"type": "letterbox", "zoom": [1.0, 1.0, 1.0], "pan": [(0.5, 0.5)] * 3, "ease": "linear"}

SLIDES = [
    {"img": "HERO", **_PA},  # s0 Who Pays for the News?
    {"img": "HERO", **_PB},  # s1 Singapore Has Been Asking Since 1824
    {"img": "R1890", **_PA},  # s2 Singapore's first newspaper was printed on rough
    {"img": "PV03", **_PB},  # s3 It got through its first five years on a governm
    {"img": "HERO", **_PB},  # s4 Nearly two centuries later, the question that de
    {"img": "CH1", **_CHART},  # s5 The Singapore Chronicle's first issue appeared o
    {"img": "R1890", **_PB},  # s6 The British Resident, John Crawfurd, had applied
    {"img": "HERO", **_PA},  # s7 It was printed at first by the Mission Press and
    {"img": "PV03", **_PA},  # s8 It was a paper for the port.
    {"img": "R1910K", **_PB},  # s9 The Chronicle carried official notifications, ad
    {"img": "CH1", **_CHART},  # s10 A year's subscription cost 18 Spanish dollars an
    {"img": "CH1", **_CHART},  # s11 But subscriptions did not cover its costs.
    {"img": "CH1", **_CHART},  # s12 The editor also received a fixed government subs
    {"img": "CH1", **_CHART},  # s13 The larger change came in 1835, when restriction
    {"img": "CH1", **_CHART},  # s14 That October, the Singapore Free Press and Merca
    {"img": "R1890", **_PA},  # s15 Its founders included William Napier and Edward 
    {"img": "CH1", **_CHART},  # s16 The older paper, now facing a rival edited by it
    {"img": "STOFF", **_STA},  # s17 The Straits Times and Singapore Journal of Comme
    {"img": "R1910", **_PA},  # s18 It was the work of an editor from Bombay, Robert
    {"img": "CH1", **_CHART},  # s19 The first issue ran to eight folio pages, printe
    {"img": "HERO", **_PB},  # s20 It began as a Tuesday weekly and went to twice w
    {"img": "R1910K", **_PA},  # s21 Woods had struggled to convince Moses that the p
    {"img": "CH1", **_CHART},  # s22 By September 1846, only fourteen months after la
    {"img": "STOFF", **_STB},  # s23 The same question is now being asked of a much l
    {"img": "CH2", **_CHART},  # s24 The publisher of the Straits Times, Lianhe Zaoba
    {"img": "CH2", **_CHART},  # s25 On the 16th of February 2022 the government anno
    {"img": "CH2", **_CHART},  # s26 The Ministry of Digital Development and Informat
    {"img": "CH2", **_CHART},  # s27 The trust also disclosed in 2023 that its report
    {"img": "MC", **_PA},  # s28 Television is on a similar footing.
    {"img": "CH2", **_CHART},  # s29 Mediacorp, owned by the state investment company
    {"img": "MC", **_PB},  # s30 She set that against the roughly 780 million Sin
    {"img": "MC", **_PA},  # s31 The government, she added, now measures reach ac
    {"img": "R1910K", **_PB},  # s32 The figures for online audiences are of a differ
    {"img": "MC", **_PB},  # s33 CNA, Mediacorp's news brand, reported nearly 12 
    {"img": "STOFF", **_STA},  # s34 The Straits Times put its website online in 1994
    {"img": "CH2", **_CHART},  # s35 Visitors, subscribers and printed copies are not
    {"img": "R1910", **_PB},  # s36 The stated rationale for that support is about t
    {"img": "R1890", **_PB},  # s37 Minister Teo has said that "no one gains if thes
    {"img": "PV03", **_PA},  # s38 Research for the Reuters Institute for the Study
    {"img": "HERO", **_PA},  # s39 Whether public funding preserves a local view of
    {"img": "CH1", **_CHART},  # s40 Where it fits in the bigger story: In 1824, a co
    {"img": "STOFF", **_STB},  # s41 In 1846 the paper nobody would buy was the one t
    {"img": "HERO", **_PB},  # s42 Small markets have always struggled to pay for t
]

SCHEDULE = [
    (0.0, 0), (2.375, 1), (6.525, 2), (16.875, 3), (29.725, 4),
    (43.225, 5), (49.825, 6), (70.275, 7), (87.3, 8), (89.9, 9),
    (102.6, 10), (113.95, 11), (117.4, 12), (128.3, 13), (134.675, 14),
    (143.575, 15), (153.55, 16), (163.9, 17), (175.775, 18), (193.925, 19),
    (202.625, 20), (209.675, 21), (214.725, 22), (222.975, 23), (230.975, 24),
    (246.75, 25), (267.275, 26), (288.3, 27), (305.65, 28), (309.0, 29),
    (326.325, 30), (347.125, 31), (356.7, 32), (361.325, 33), (374.575, 34),
    (382.4, 35), (399.7, 36), (405.975, 37), (413.825, 38), (434.55, 39),
    (445.6, 40), (462.425, 41), (468.275, 42),
]
TOTAL_DURATION = 482.025
TIMING_JSON = "audio/who-pays-for-the-news-singapore-has-been-asking-since-1824.timing.json"
