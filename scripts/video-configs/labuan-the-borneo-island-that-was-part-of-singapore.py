"""Video config for the Labuan post.

From the 1848 Phlegethon engraving and the cession of 1846 to the offshore
centre today: the flag-raising and treaty engravings, Brooke (two portraits),
Hugh Low, the old maps and charts (1848, 1872, 1888, 1913 and Singapore's own
1930 map), the Chimney, St Andrew's Cathedral, the 1906 overprinted stamp,
Clifford and Shenton Thomas, the Government Offices, both Straits Times pages
(2 January 1907 and 16 July 1946), the memorial stones, the 1942 and 1945
landings, the ruins of Victoria, the surrenders on Labuan and in Singapore, the
war cemetery, and present-day Labuan.

Named-person rule: William Napier and E. B. Maundrell have no free portraits,
so their sentences show places only; the governors' list (s30) shows Shenton
Thomas, the last of them. Portraits, maps, newspaper pages, stones and small
wartime photos are letterboxed with a modest zoom; the timeline is frozen.

53 slides, 745.95s. Narration: Kokoro with the OpenVoice clone.
AVATAR: first and last 30s, cartoon with motion.
"""

_U = "https://upload.wikimedia.org/wikipedia/commons"
_C = f"{_U}/thumb"

IMAGES = {
    "HERO": f"{_C}/9/9e/H.C._steamer_Phlegethon_at_Labuan%2C_August_1848.jpg/1280px-H.C._steamer_Phlegethon_at_Labuan%2C_August_1848.jpg",
    "MAP1930": f"{_C}/c/c3/Labuan_1930_img0035_AccNo128_1.jpg/1280px-Labuan_1930_img0035_AccNo128_1.jpg",
    "STAMP": f"{_U}/0/07/1906straitssettlements2c.jpg",
    "FINPARK": f"{_C}/6/61/Labuan_Financial_Park_-_01.JPG/1280px-Labuan_Financial_Park_-_01.JPG",
    "CHART1848": f"{_C}/6/6c/Admiralty_Chart_No_1844_Labuan_Island%2C_Published_1848%2C_Large_Corrections_1902.jpg/1280px-Admiralty_Chart_No_1844_Labuan_Island%2C_Published_1848%2C_Large_Corrections_1902.jpg",
    "FLAG": f"{_U}/0/06/Ceremony_of_Hoisting_the_British_Flag_on_the_island_of_Labuan%2C_N._W._Coast_of_Borneo.jpg",
    "BROOKE": f"{_U}/5/50/Sir-James-Brooke.jpg",
    "TREATY": f"{_U}/3/31/Treaty_of_Labuan1846.jpg",
    "LOW": f"{_U}/c/c0/Hugh_Low.png",
    "BROOKE2": f"{_U}/5/58/Rajah_Brooke_%28OAW%29.png",
    "FULLARTON": f"{_U}/5/5a/Fullarton%27s_Labuan_island_map_%281872%29.png",
    "CHIMNEY": f"{_C}/f/f4/Labuan_Malaysia_Chimney-01.jpg/1280px-Labuan_Malaysia_Chimney-01.jpg",
    "CHIMNEY2": f"{_U}/0/05/Labuan-Chimney.jpg",
    "CATHEDRAL": f"{_C}/7/7a/KITLV_-_1404966_-_Ribeiro_%26_Co.%2C_stationers%2C_printers_%26_stampdealers_-_Singapore_-_St._Andrews_Cathedral_-_1895-1908.tif/lossy-page1-1280px-KITLV_-_1404966_-_Ribeiro_%26_Co.%2C_stationers%2C_printers_%26_stampdealers_-_Singapore_-_St._Andrews_Cathedral_-_1895-1908.tif.jpg",
    "MAP1888": f"{_U}/f/fb/Map_of_Labuan_%281888%29.jpg",
    "CHART1913": f"{_C}/1/1c/Admiralty_Chart_No_947_Victoria_Harbour%2C_Published_1913.jpg/1280px-Admiralty_Chart_No_947_Victoria_Harbour%2C_Published_1913.jpg",
    "CLIFFORD": f"{_U}/7/78/Hugh_Charles_Clifford_%28The_Straits_Times%2C_15_October_1929%29.jpg",
    "GOVOFF": f"{_U}/2/2f/Labuan_Government_Offices.jpg",
    "ST1907": "/assets/images/straits-times-1907-01-02-page-6.jpg",
    "CESSION": f"{_C}/7/7f/Labuan-MemorialStone-from-1846-12-24.jpg/1280px-Labuan-MemorialStone-from-1846-12-24.jpg",
    "SHENTON": f"{_C}/9/97/Shenton_Thomas_1936.jpg/1280px-Shenton_Thomas_1936.jpg",
    "ISLAND": f"{_U}/1/16/Labuan_Island.jpg",
    "POWSTONE": f"{_C}/d/d7/Labuan_Malaysia_Memorial-Stone-Visit-Prince-of-Wales-01.jpg/1280px-Labuan_Malaysia_Memorial-Stone-Visit-Prince-of-Wales-01.jpg",
    "JPLAND": f"{_U}/d/df/Japanese_landing_off_the_west_coast_of_British_North_Borneo%2C_Labuan.jpg",
    "MAEDA": f"{_C}/d/d5/Labuan_Malaysia_Memorial-Stone-GENERAL-MAIDA-01.jpg/1280px-Labuan_Malaysia_Memorial-Stone-GENERAL-MAIDA-01.jpg",
    "AUSLAND": f"{_U}/0/00/Australian_troops_landing_on_Labuan%2C_1945.JPG",
    "REMNANTS": f"{_U}/8/86/Remnants_of_Victoria_town_in_Labuan_on_10_June_1945_following_the_Allied_bombardment.jpg",
    "SURRENDER": f"{_U}/5/5f/Japanese_Surrender%2C_Labuan_%28AWM_115989%29.JPG",
    "SURRPOINT": f"{_C}/5/5b/Labuan_Malaysia_Surrender-Point-Memorial-01.jpg/1280px-Labuan_Malaysia_Surrender-Point-Memorial-01.jpg",
    "SGSURR": f"{_U}/b/ba/Signing_of_the_Japanese_Surrender_at_Singapore%2C_1945_CF719.jpg",
    "CEMOPEN": f"{_U}/2/26/Labuan_War_Cemetery_Opening%2C_1945.JPG",
    "CEM2025": f"{_C}/b/bc/Labuan_War_Cemetery%2C_April_2025_09.jpg/1280px-Labuan_War_Cemetery%2C_April_2025_09.jpg",
    "CEMCROSS": f"{_C}/c/c7/Labuan_Malaysia_War-Cemetery-01.jpg/1280px-Labuan_Malaysia_War-Cemetery-01.jpg",
    "BABA": f"{_U}/5/5d/MasaoBaba_Labuan01.jpg",
    "ST1946": "/assets/images/straits-times-1946-07-16-page-1.jpg",
    "JESSELTON": f"{_U}/8/81/Jesselton%2C_circa_1911.JPG",
    "FERRY": f"{_C}/6/69/Labuan_Express_Ferry_Arriving_In_Kota_Kinabalu.jpg/1280px-Labuan_Express_Ferry_Arriving_In_Kota_Kinabalu.jpg",
    "DOWNTOWN": f"{_C}/7/74/View_Of_Downtown_Labuan.jpg/1280px-View_Of_Downtown_Labuan.jpg",
    "TIMELINE": "/assets/images/labuan-timeline-chart.png",
}

# Credits for images not captioned in the post or its gallery.
CREDITS = {
    "TIMELINE": "Timeline by Lesser Known Singapore",
    "CHART1848": "United Kingdom Hydrographic Office, public domain, via Wikimedia Commons",
    "LOW": "Unknown author, public domain, via Wikimedia Commons",
    "BROOKE2": "Joseph Swain, after Thomas Woolner, public domain, via Wikimedia Commons",
    "FULLARTON": "A. Fullarton and Co., public domain, via Wikimedia Commons",
    "CHIMNEY2": "CEphoto, Uwe Aranas, CC BY-SA 3.0, via Wikimedia Commons",
    "CATHEDRAL": "Ribeiro and Co., KITLV, public domain, via Wikimedia Commons",
    "CESSION": "CEphoto, Uwe Aranas, CC BY-SA 3.0, via Wikimedia Commons",
    "SHENTON": "Unknown author, public domain, via Wikimedia Commons",
    "ISLAND": "rizuan.j, CC BY 2.0, via Wikimedia Commons",
    "AUSLAND": "Unknown author, Australian War Memorial, public domain, via Wikimedia Commons",
    "REMNANTS": "Jack Band, Australian War Memorial, public domain, via Wikimedia Commons",
    "SGSURR": "Flying Officer Ashley, Royal Air Force official photographer, public domain, via Wikimedia Commons",
    "CEMOPEN": "Pleass, Australian War Memorial, public domain, via Wikimedia Commons",
    "CEMCROSS": "CEphoto, Uwe Aranas, CC BY-SA 3.0, via Wikimedia Commons",
    "JESSELTON": "Unknown author, public domain, via Wikimedia Commons",
    "FERRY": "Jason Thien, CC BY 2.0, via Wikimedia Commons",
    "DOWNTOWN": "Jason Thien, CC BY 2.0, via Wikimedia Commons",
}

# The channel's 2x2 thumbnail grid, 1846 to today: the flag-raising, the 1906
# Straits Settlements stamp, the 1945 surrender, the Financial Park.
THUMBNAIL = [
    {"img": "FLAG", "pan": (0.5, 0.4)},
    {"img": "STAMP", "pan": (0.5, 0.22)},
    {"img": "SURRENDER", "pan": (0.5, 0.45)},
    "FINPARK",
]

_E = "ease-in-out"
_IN = {"type": "cover", "zoom": [1.0, 1.06, 1.12], "pan": [(0.5, 0.5)] * 3, "ease": _E}
_OUT = {"type": "cover", "zoom": [1.12, 1.06, 1.0], "pan": [(0.5, 0.5)] * 3, "ease": _E}
# Portraits, maps, newspaper pages, stones and small wartime photos: letterbox, modest zoom.
_PORT = {"type": "letterbox", "zoom": [1.0, 1.04, 1.08], "pan": [(0.5, 0.5)] * 3, "ease": _E}
_PORT_OUT = {"type": "letterbox", "zoom": [1.08, 1.04, 1.0], "pan": [(0.5, 0.5)] * 3, "ease": _E}
# The timeline: letterbox, frozen.
_GFX = {"type": "letterbox", "zoom": [1, 1, 1], "pan": [(0.5, 0.5)] * 3}

SLIDES = [
    {"img": "HERO", **_IN},           # 0  s0  title
    {"img": "MAP1930", **_PORT},      # 1  s1  almost forty years governed from Singapore (Singapore's own 1930 map)
    {"img": "STAMP", **_PORT},        # 2  s2  part of the Settlement of Singapore, then a settlement of its own
    {"img": "FINPARK", **_IN},        # 3  s3  a federal territory and offshore centre today
    {"img": "CHART1848", **_IN},      # 4  s4  coal and a sheltered harbour on the China route
    {"img": "FLAG", **_IN},           # 5  s5  labuhan, an anchorage
    {"img": "BROOKE", **_PORT},       # 6  s6  James Brooke presses London
    {"img": "TREATY", **_PORT},       # 7  s7  the treaty of 18 December 1846; Mundy negotiates with the Brunei court
    {"img": "BROOKE", **_PORT_OUT},   # 8  s8  Crown Colony 1848, Brooke Governor
    {"img": "HERO", **_OUT},          # 9  s9  William Napier (no portrait of him)
    {"img": "LOW", **_PORT},          # 10 s10  Hugh Low, Napier's secretary
    {"img": "BROOKE2", **_PORT},      # 11 s11  Napier invests Brooke in Singapore
    {"img": "FULLARTON", **_PORT},    # 12 s12  gloomy predictions in Singapore; came to nothing (s13)
    {"img": "CHIMNEY", **_PORT},      # 13 s14  the coal companies; malaria and accidents (s15)
    {"img": "BROOKE2", **_PORT_OUT},  # 14 s16  Brooke's 1854 inquiry in Singapore
    {"img": "CHIMNEY2", **_PORT},     # 15 s17  the Chimney
    {"img": "CATHEDRAL", **_IN},      # 16 s18  the shared diocese; St Andrew's its cathedral (s19-20)
    {"img": "MAP1888", **_PORT},      # 17 s21  debt; North Borneo Company from 1890
    {"img": "CHART1913", **_PORT},    # 18 s22  the 1894 cable
    {"img": "CLIFFORD", **_PORT},     # 19 s23  Hugh Clifford, governor 1900-01
    {"img": "GOVOFF", **_IN},         # 20 s24  Britain takes it back, 1906
    {"img": "STAMP", **_PORT_OUT},    # 21 s25  Letters Patent; part of the Settlement of Singapore (s26)
    {"img": "ST1907", **_PORT},       # 22 s27  the Labuan Bill passes the Legislative Council
    {"img": "CESSION", **_PORT},      # 23 s28  a separate settlement, 1912; same Governor (s29)
    {"img": "SHENTON", **_PORT},      # 24 s30  the governors, ending with Shenton Thomas (shown)
    {"img": "GOVOFF", **_OUT},        # 25 s31  a Resident on the island
    {"img": "CLIFFORD", **_PORT_OUT}, # 26 s32  Clifford back as Governor, 1927-30 (s33)
    {"img": "CHIMNEY2", **_PORT_OUT}, # 27 s34  a quiet posting; the mines close (s35)
    {"img": "ISLAND", **_PORT},       # 28 s36  Maundrell shot, 1916 (no photo of him)
    {"img": "POWSTONE", **_PORT},     # 29 s37  the Prince of Wales lands, 17 May 1922
    {"img": "MAP1930", **_PORT_OUT},  # 30 s38  the 1930 map; 9,000 people (s39)
    {"img": "JPLAND", **_PORT},       # 31 s40  Japanese landing, January 1942; the airfield (s41)
    {"img": "MAEDA", **_IN},          # 32 s42  General Maeda; Maeda Island
    {"img": "AUSLAND", **_PORT},      # 33 s43  Australian landing, 10 June 1945 (s44)
    {"img": "REMNANTS", **_PORT},     # 34 s45  casualties; Victoria in ruins
    {"img": "SURRENDER", **_PORT},    # 35 s46  Baba surrenders to Wootten, 10 September 1945
    {"img": "SURRPOINT", **_IN},      # 36 s47  Surrender Point
    {"img": "SGSURR", **_PORT},       # 37 s48  the surrender in Singapore, 12 September
    {"img": "CEMOPEN", **_PORT},      # 38 s49  the war cemetery (s50)
    {"img": "CEM2025", **_IN},        # 39 s51  sent from Singapore; B and E Force (s52)
    {"img": "CEMCROSS", **_PORT},     # 40 s53  graves moved; unnamed graves
    {"img": "BABA", **_PORT},         # 41 s54  Baba tried and hanged
    {"img": "ST1946", **_PORT},       # 42 s55  the Straits Settlements dissolved; Labuan still under Singapore
    {"img": "JESSELTON", **_IN},      # 43 s56  joined to North Borneo, 15 July 1946
    {"img": "ST1946", **_PORT_OUT},   # 44 s57  the Straits Times front page
    {"img": "FERRY", **_IN},          # 45 s58  Malaysia 1963; federal territory 1984 (s59)
    {"img": "FINPARK", **_OUT},       # 46 s60  the offshore centre; 2024 figures (s61)
    {"img": "DOWNTOWN", **_IN},       # 47 s62  a free port; ferries
    {"img": "SURRPOINT", **_OUT},     # 48 s63  where its history is kept
    {"img": "CATHEDRAL", **_OUT},     # 49 s64  almost no trace in Singapore (s65)
    {"img": "TIMELINE", **_GFX},      # 50 s66  where it fits in the bigger story
    {"img": "FULLARTON", **_PORT_OUT},# 51 s67  Christmas Island and the Cocos; one scattered colony
    {"img": "HERO", **_OUT},          # 52 s68  never the rival port; the men who left Changi
]

SCHEDULE = [(0.0, 0), (4.075, 1), (16.3, 2), (31.7, 3), (41.75, 4), (55.925, 5), (61.825, 6), (67.575, 7), (85.45, 8), (92.975, 9), (104.75, 10), (115.5, 11), (125.225, 12), (141.775, 13), (161.875, 14), (175.6, 15), (187.025, 16), (213.675, 17), (228.675, 18), (236.85, 19), (246.625, 20), (255.1, 21), (274.125, 22), (289.95, 23), (306.8, 24), (318.05, 25), (328.475, 26), (348.275, 27), (360.925, 28), (373.275, 29), (390.475, 30), (409.875, 31), (421.65, 32), (441.65, 33), (459.775, 34), (471.9, 35), (491.025, 36), (494.55, 37), (504.1, 38), (520.675, 39), (542.775, 40), (555.225, 41), (564.125, 42), (576.875, 43), (587.475, 44), (606.275, 45), (622.8, 46), (651.3, 47), (657.95, 48), (683.825, 49), (702.375, 50), (708.525, 51), (724.95, 52)]
TOTAL_DURATION = 745.95
TIMING_JSON = "audio/labuan-the-borneo-island-that-was-part-of-singapore.timing.json"

# The avatar presenter, cartoon with motion: corner bubble for the first and last 30 s.
AVATAR = {"ranges": [(0, 30), (-30, None)], "motion": True}
