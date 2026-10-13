"""Video config for the Syonan Syoken post.

The museum's Konan Saiken tickets (the 1st, 4th, 6th, 9th, 16th and 21st
draws) carry the lottery sentences; the 9th-draw ticket, whose two sides name
its causes, is letterboxed so both sides stay in frame. The six whole
newspaper pages (the post's four, plus the 26 June 1942 gift page and the
17 March 1942 bank-reopening page from the earlier posts, video-only) are
always letterboxed, never cropped to one story. The first prize winner,
S. P. Letchuman Chettiar, is named only under the 13 September 1942 page that
carries his photograph; Mr Hara and Mr Nakahira have no image, so their
sentences get the hall and the old Victoria Memorial Hall. The banknotes are
letterboxed. Video-only: the two newspaper pages, the Hongkong and Shanghai
Bank around 1900 (where the Yokohama Specie Bank reopened in 1942), the
Victoria Memorial Hall, a 1944 Syonan Shimbun front page, a set of the notes,
a 50-cent note, a 1944 $10 note and Singapore Pools' head office today. The
chart and timeline are letterboxed and frozen.

51 slides, 641.525s. AVATAR: first and last 30s, cartoon with motion.
"""

_U = "https://upload.wikimedia.org/wikipedia/commons"
_C = f"{_U}/thumb"
_A = "/assets/images"

IMAGES = {
    "HERO": f"{_C}/6/66/JapLotteryTicket-SIN-Occupation_SINMuseum_20171213_02.jpg/1280px-JapLotteryTicket-SIN-Occupation_SINMuseum_20171213_02.jpg",
    "SY0911": f"{_A}/syonan-shimbun-1942-09-11-page-1.jpg",
    "SY0623": f"{_A}/syonan-shimbun-1942-06-23-page-3.jpg",
    "VICT": f"{_U}/e/e6/Victoria_Theatre_and_Victoria_Memorial_Hall_-_c_1930.jpg",
    "SY0913": f"{_A}/syonan-shimbun-1942-09-13-page-1.jpg",
    "T9": f"{_C}/a/a8/JapLotteryTicket-SIN-Occupation_SINMuseum_20171213_04.jpg/1280px-JapLotteryTicket-SIN-Occupation_SINMuseum_20171213_04.jpg",
    "NOTE10": f"{_C}/c/c5/Ten_dollar_note_issued_by_the_Japanese_Government_during_the_occupation_of_Malaya%2C_North_Borneo%2C_Sarawak_and_Brunei_%281942%2C_obverse%29.jpg/1280px-Ten_dollar_note_issued_by_the_Japanese_Government_during_the_occupation_of_Malaya%2C_North_Borneo%2C_Sarawak_and_Brunei_%281942%2C_obverse%29.jpg",
    "SY0802": f"{_A}/syonan-shimbun-1945-08-02-page-2.jpg",
    "CHART": f"{_A}/syoken-dollar-chart.png",
    "TIMELINE": f"{_A}/syoken-timeline-chart.png",
    # Gallery images:
    "T1": f"{_C}/9/9f/JapLotteryTicket-SIN-Occupation_SINMuseum_20171213_05.jpg/1280px-JapLotteryTicket-SIN-Occupation_SINMuseum_20171213_05.jpg",
    "T4": f"{_C}/b/be/JapLotteryTicket-SIN-Occupation_SINMuseum_20171213_08.jpg/1280px-JapLotteryTicket-SIN-Occupation_SINMuseum_20171213_08.jpg",
    "T6": f"{_C}/0/0a/JapLotteryTicket-SIN-Occupation_SINMuseum_20171213_09.jpg/1280px-JapLotteryTicket-SIN-Occupation_SINMuseum_20171213_09.jpg",
    "T16": f"{_C}/c/c6/JapLotteryTicket-SIN-Occupation_SINMuseum_20171213_03.jpg/1280px-JapLotteryTicket-SIN-Occupation_SINMuseum_20171213_03.jpg",
    "NOTE1": f"{_C}/2/27/One_dollar_note_issued_by_the_Japanese_Government_during_the_occupation_of_Malaya%2C_North_Borneo%2C_Sarawak_and_Brunei_%281942%2C_obverse%29.jpg/1280px-One_dollar_note_issued_by_the_Japanese_Government_during_the_occupation_of_Malaya%2C_North_Borneo%2C_Sarawak_and_Brunei_%281942%2C_obverse%29.jpg",
    "NOTE100": f"{_C}/9/9d/One_hundred_dollar_note_issued_by_the_Japanese_Government_during_the_occupation_of_Malaya%2C_North_Borneo%2C_Sarawak_and_Brunei_%281944%2C_obverse%29.jpg/1280px-One_hundred_dollar_note_issued_by_the_Japanese_Government_during_the_occupation_of_Malaya%2C_North_Borneo%2C_Sarawak_and_Brunei_%281944%2C_obverse%29.jpg",
    "NOTE1000": f"{_C}/d/d6/MAL-M10b-Malaya-Japanese_Occupation-1000_Dollars_ND_%281945%29.jpg/1280px-MAL-M10b-Malaya-Japanese_Occupation-1000_Dollars_ND_%281945%29.jpg",
    "RATION": f"{_C}/f/fd/RationBook_SIN_1942_20171213.jpg/1280px-RationBook_SIN_1942_20171213.jpg",
    "SY1943": f"{_C}/9/9c/ST3February1943.jpg/1280px-ST3February1943.jpg",
    "STREET": f"{_U}/f/fc/Street_in_Shonan.JPG",
    "MAP": f"{_C}/4/4a/SyonanSingapore.jpg/1280px-SyonanSingapore.jpg",
    # Not in this post's captions (credited below):
    "SY0626": f"{_A}/syonan-shimbun-1942-06-26-page-2.jpg",
    "SY0317": f"{_A}/syonan-shimbun-1942-03-17-page-4.jpg",
    "HSBC1900": f"{_U}/8/81/Photographic_Views_of_Singapore_Plate_05_Hongkong_and_Shanghai_Bank.jpg",
    "VMH": f"{_C}/d/d8/Victoria_Memorial_Hall_te_Singapore%2C_KITLV_33210.tiff/lossy-page1-1280px-Victoria_Memorial_Hall_te_Singapore%2C_KITLV_33210.tiff.jpg",
    "SY1944": f"{_C}/3/32/ST3April1944.jpg/1280px-ST3April1944.jpg",
    "NOTES": f"{_C}/c/c2/Notes_issued_by_the_Japanese_Government_during_the_occupation_of_Malaya%2C_North_Borneo%2C_Sarawak_and_Brunei%2C_used_in_Batu_Lintang_camp%2C_Sarawak_%281942%E2%80%931945%2C_obverse%29.jpg/1280px-thumbnail.jpg",
    "NOTE50": f"{_C}/0/06/Fifty_cent_note_issued_by_the_Japanese_Government_during_the_occupation_of_Malaya%2C_North_Borneo%2C_Sarawak_and_Brunei_%281942%2C_reverse%29.jpg/1280px-Fifty_cent_note_issued_by_the_Japanese_Government_during_the_occupation_of_Malaya%2C_North_Borneo%2C_Sarawak_and_Brunei_%281942%2C_reverse%29.jpg",
    "NOTE10B": f"{_C}/b/ba/MAL-M7c-Malaya-Japanese_Occupation-10_Dollars_ND_%281944%29.jpg/1280px-MAL-M7c-Malaya-Japanese_Occupation-10_Dollars_ND_%281944%29.jpg",
    "POOLS": f"{_C}/6/6f/Sede_de_Singapore_Pools%2C_Middle_Road%2C_Singapur%2C_2023-08-16%2C_DD_02.jpg/1280px-Sede_de_Singapore_Pools%2C_Middle_Road%2C_Singapur%2C_2023-08-16%2C_DD_02.jpg",
    "POOLS2": f"{_C}/3/3d/Singapore_Pools_Head_Office_20210503_125649.jpg/1280px-Singapore_Pools_Head_Office_20210503_125649.jpg",
}

# Credits for images not captioned in the post or its gallery.
CREDITS = {
    "CHART": "Chart by Lesser Known Singapore",
    "TIMELINE": "Timeline by Lesser Known Singapore",
    "SY0626": "Singapore Press Holdings, via NewspaperSG, National Library Board Singapore, public domain",
    "SY0317": "Singapore Press Holdings, via NewspaperSG, National Library Board Singapore, public domain",
    "HSBC1900": "G. R. Lambert & Co., public domain, via Wikimedia Commons",
    "VMH": "M. S. Nakajima, KITLV, CC BY 4.0, via Wikimedia Commons",
    "SY1944": "The Straits Times, public domain, via Wikimedia Commons",
    "NOTES": "Government of Imperial Japan, public domain, via Wikimedia Commons",
    "NOTE50": "Scanned by Jacklee, public domain, via Wikimedia Commons",
    "NOTE10B": "National Museum of American History, public domain, via Wikimedia Commons",
    "POOLS": "Diego Delso, CC BY-SA 4.0, via Wikimedia Commons",
    "POOLS2": "ZKang123, CC BY-SA 4.0, via Wikimedia Commons",
}

_E = "ease-in-out"
_IN = {"type": "cover", "zoom": [1.0, 1.06, 1.12], "pan": [(0.5, 0.5)] * 3, "ease": _E}
_IN2 = {"type": "cover", "zoom": [1.1, 1.16, 1.22], "pan": [(0.4, 0.5), (0.5, 0.5), (0.6, 0.5)], "ease": _E}
_OUT = {"type": "cover", "zoom": [1.12, 1.06, 1.0], "pan": [(0.5, 0.5)] * 3, "ease": _E}
# Newspaper pages, banknotes, small scans and tall photos: letterbox, modest zoom.
_PORT = {"type": "letterbox", "zoom": [1.0, 1.04, 1.08], "pan": [(0.5, 0.5)] * 3, "ease": _E}
_PORT_OUT = {"type": "letterbox", "zoom": [1.08, 1.04, 1.0], "pan": [(0.5, 0.5)] * 3, "ease": _E}
# The chart and timeline: letterbox, frozen.
_GFX = {"type": "letterbox", "zoom": [1, 1, 1], "pan": [(0.5, 0.5)] * 3}

SLIDES = [
    {"img": "HERO", **_IN},           # 0  s0   title
    {"img": "VICT", **_PORT},         # 1  s1   the draw at the old Victoria Theatre
    {"img": "SY0911", **_PORT},       # 2  s2   women turn the drums; 62 winners
    {"img": "SY0913", **_PORT},       # 3  s3   the $100,000 first prize, 223 tickets
    {"img": "T1", **_IN},             # 4  s4   the first of more than thirty lotteries
    {"img": "MAP", **_IN},            # 5  s5   announced 29 May 1942
    {"img": "NOTE1", **_PORT},        # 6  s6   a $1,000,000 lottery, "dual purpose"
    {"img": "HSBC1900", **_PORT},     # 7  s7   City Hall, Yokohama Specie Bank, Bank of Taiwan
    {"img": "STREET", **_PORT},       # 8  s8   its reasons: spending money, speculation
    {"img": "RATION", **_IN},         # 9  s10  a hard moment for the city's money
    {"img": "SY0626", **_PORT},       # 10 s11  the $50 million "gift"
    {"img": "SY0317", **_PORT},       # 11 s12  the same bank pays the winners
    {"img": "NOTE10", **_PORT},       # 12 s13  banana money
    {"img": "NOTES", **_PORT},        # 13 s14  drawing some of that money back
    {"img": "SY0623", **_PORT},       # 14 s15  Syonan Syoken; the notice and the advertisement
    {"img": "SY0911", **_PORT_OUT},   # 15 s18  62 prizes, $300,000
    {"img": "HSBC1900", **_PORT_OUT}, # 16 s19  no tax; cash at the Yokohama Specie Bank
    {"img": "VMH", **_PORT},          # 17 s20  the draw moved to 10 September
    {"img": "VICT", **_PORT_OUT},     # 18 s21  Mr Hara: a million tickets in two months
    {"img": "RATION", **_OUT},        # 19 s22  "relief of distressed people"
    {"img": "SY0913", **_PORT_OUT},   # 20 s23  the winners; Letchuman Chettiar
    {"img": "NOTE50", **_PORT},       # 21 s25  a Sikh constable in Negri Sembilan
    {"img": "MAP", **_OUT},           # 22 s26  a dhoby shop on Exeter Road
    {"img": "CHART", **_GFX},         # 23 s27  the $700,000 left over
    {"img": "VMH", **_PORT_OUT},      # 24 s29  Mr Nakahira: "any further lotteries"
    {"img": "T4", **_IN},             # 25 s30  further lotteries, every month
    {"img": "HERO", **_OUT},          # 26 s31  Konan Saiken
    {"img": "T6", **_IN},             # 27 s32  sold out within days
    {"img": "SY1943", **_PORT},       # 28 s33  400,000 tickets from August 1943
    {"img": "T9", **_PORT},           # 29 s34  health facilities, refugee relief
    {"img": "T16", **_IN},            # 30 s35  winners giving some away
    {"img": "NOTE1", **_PORT_OUT},    # 31 s36  the Malacca winner; the Red Cross gift
    {"img": "VICT", **_PORT},         # 32 s37  loudspeakers outside the hall
    {"img": "NOTE10B", **_PORT},      # 33 s38  a fixed sum in a falling currency
    {"img": "NOTES", **_PORT_OUT},    # 34 s39  some $4,000 million issued
    {"img": "STREET", **_PORT_OUT},   # 35 s40  an egg for $100
    {"img": "NOTE100", **_PORT},      # 36 s41  a fortune in 1942
    {"img": "NOTE1000", **_PORT},     # 37 s42  $100 and $1,000 notes
    {"img": "SY1944", **_PORT},       # 38 s43  the lotteries went on to the end
    {"img": "HERO", **_IN2},          # 39 s44  the 25th issue, June 1945
    {"img": "MAP", **_IN2},           # 40 s45  Engo Saiken at $5
    {"img": "SY0802", **_PORT},       # 41 s46  the 27th issue, drawing set for 5 September
    {"img": "TIMELINE", **_GFX},      # 42 s48  the surrender; the British return
    {"img": "NOTE10", **_PORT_OUT},   # 43 s49  banana money declared worthless
    {"img": "T4", **_OUT},            # 44 s50  the museum's tickets
    {"img": "T16", **_OUT},           # 45 s51  neither account can be checked
    {"img": "HERO", **_OUT},          # 46 s52  why it matters
    {"img": "T9", **_PORT_OUT},       # 47 s53  its good causes printed on every ticket
    {"img": "POOLS", **_IN},          # 48 s54  Singapore Pools, 1968
    {"img": "POOLS2", **_IN},         # 49 s55  the Tote Board
    {"img": "T1", **_OUT},            # 50 s56  public accounting
]

SCHEDULE = [(0.0, 0), (7.2, 1), (20.35, 2), (30.575, 3), (40.6, 4), (54.95, 5), (60.55, 6), (76.95, 7), (86.625, 8), (106.425, 9), (110.525, 10), (127.4, 11), (132.775, 12), (143.975, 13), (152.95, 14), (179.225, 15), (193.25, 16), (204.2, 17), (215.2, 18), (225.05, 19), (250.575, 20), (272.9, 21), (278.65, 22), (289.8, 23), (311.0, 24), (326.9, 25), (330.775, 26), (341.275, 27), (355.6, 28), (373.1, 29), (385.2, 30), (389.6, 31), (408.75, 32), (420.1, 33), (425.725, 34), (444.35, 35), (463.15, 36), (469.475, 37), (481.4, 38), (484.35, 39), (499.4, 40), (512.925, 41), (540.05, 42), (550.475, 43), (562.425, 44), (576.275, 45), (587.575, 46), (598.8, 47), (613.65, 48), (621.625, 49), (632.175, 50)]
TOTAL_DURATION = 641.525
TIMING_JSON = "audio/syonan-syoken-the-occupations-government-lottery-1942-45.timing.json"

# The avatar presenter, cartoon with motion: corner bubble for the first and last 30 s.
AVATAR = {"ranges": [(0, 30), (-30, None)], "motion": True}
