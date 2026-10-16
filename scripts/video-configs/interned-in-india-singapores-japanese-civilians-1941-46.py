"""Video config for the Interned in India post.

The journey is told through places (Changi, Port Swettenham, St John's Island,
Bombay, Calcutta, the Purana Qila) and the seven whole newspaper pages (always
letterboxed, never cropped to one story); Deoli, which has no photographs on
Commons, gets the people chart and the timeline instead. Named people get
their own picture or none: Fukuda only ever gets the 1955 Singapore Standard
page that carries his photograph (s4, s27, s52, s80-81); s82 gets the timeline; Inge (s16),
Kusalasaya (s40), George Sakai (s44) and Rajagopalachari (s77, over the 1951
page reporting his statement) get no portrait. The Syonan Shimbun page
(Japanese propaganda) sits under Japan's protests about the camp (s45-47).
Video-only: W. H. Jackson's 1895 lantern slide of Sher Shah's ruins in Delhi
and the British Red Cross photo of the 1949 Geneva Conventions signing.
The charts are letterboxed and frozen; small or portrait photos (Changi's wide
1936 view, the Kidderpore dock, the memorial stones, the lake view, the map)
are letterboxed with a modest zoom.

59 slides, 939.075s. Narration: Kokoro with the OpenVoice clone.
AVATAR: the whole video, cartoon with motion (the Phase 2 test).
"""

_U = "https://upload.wikimedia.org/wikipedia/commons"
_C = f"{_U}/thumb"
_A = "/assets/images"

IMAGES = {
    "HERO": f"{_C}/b/b5/Purana_Qila_ramparts%2C_Delhi.jpg/1280px-Purana_Qila_ramparts%2C_Delhi.jpg",
    "CHANGI": f"{_C}/3/31/Changi_Prison_in_1936.jpg/1280px-Changi_Prison_in_1936.jpg",
    "ST1941": f"{_A}/straits-times-1941-12-08-page-8.jpg",
    "SYONAN": f"{_A}/syonan-shimbun-1942-12-15-page-1.jpg",
    "MT1946": f"{_A}/malaya-tribune-1946-03-26-page-1.jpg",
    "SUN1946": f"{_A}/sunday-tribune-1946-01-27-page-4.jpg",
    "ST1951": f"{_A}/straits-times-1951-09-19-page-4.jpg",
    "SS1955": f"{_A}/singapore-standard-1955-11-08-page-10.jpg",
    "PEOPLE": f"{_A}/interned-in-india-people-chart.png",
    "TIMELINE": f"{_A}/interned-in-india-timeline-chart.png",
    # Gallery images:
    "GATE": f"{_C}/c/cf/Old_Fort%28purana_qila%29_Delhi.jpg/1280px-Old_Fort%28purana_qila%29_Delhi.jpg",
    "SHER": f"{_C}/f/f3/Purana_Qila%2C_Delhi_2.jpg/1280px-Purana_Qila%2C_Delhi_2.jpg",
    "LAKE": f"{_C}/7/79/Purana_Qila_in_Delhi_03-2016_img1.jpg/1280px-Purana_Qila_in_Delhi_03-2016_img1.jpg",
    "STJ1879": f"{_C}/5/59/John_Edmund_Taylor%2C_St._John%27s_Island_%26_the_Sisters._From_Tanjong_Katong_Singapore_%281879%2C_Wellcome_V0037483%29.jpg/1280px-John_Edmund_Taylor%2C_St._John%27s_Island_%26_the_Sisters._From_Tanjong_Katong_Singapore_%281879%2C_Wellcome_V0037483%29.jpg",
    "STJ2019": f"{_C}/c/c0/St._John%27s_Island_%28Singapore%29.jpg/1280px-St._John%27s_Island_%28Singapore%29.jpg",
    "PSWET": f"{_U}/6/6e/Port_Swettenham_And_Vicinity.jpg",
    "BOMBAY": f"{_C}/f/f6/006_1940_-_Bombay_Harbour%2C_India.jpg/1280px-006_1940_-_Bombay_Harbour%2C_India.jpg",
    "KIDDER": f"{_U}/b/bc/Kidderpore_dock_No._1_in_1885_-_looking_towards_river%2C_showing_temporary_railway_lines_for_removal_of_spoil.jpg",
    "LAMBERT": f"{_C}/e/e5/KITLV_-_103764_-_Lambert_%26_Co._-_Japanese_women_in_Singapore_-_circa_1890.tif/lossy-page1-1280px-KITLV_-_103764_-_Lambert_%26_Co._-_Japanese_women_in_Singapore_-_circa_1890.tif.jpg",
    "CEMETERY": f"{_C}/6/6c/Japanese_Cemetery_Park.jpg/1280px-Japanese_Cemetery_Park.jpg",
    "MEMORIAL": f"{_U}/e/ea/Japanese_war_memorial%2C_Japanese_Cemetery_Park%2C_Singapore_-_20070526.jpg",
    "STMAY": f"{_A}/straits-times-1951-05-08-page-8.jpg",
    # Not in this post's captions (credited below):
    "JACKSON": f"{_U}/3/39/Delhi_-_ruins_of_Shershak_LCCN2004707758.jpg",
    "GENEVA": f"{_U}/2/2f/Geneva_Conventions_-_signing_in_1949.jpg",
}

# Credits for images not captioned in the post or its gallery.
CREDITS = {
    "PEOPLE": "Chart by Lesser Known Singapore",
    "TIMELINE": "Timeline by Lesser Known Singapore",
    "JACKSON": "William Henry Jackson, 1895, public domain, via Wikimedia Commons",
    "GENEVA": "British Red Cross, CC BY 2.0, via Wikimedia Commons",
}

_E = "ease-in-out"
_IN = {"type": "cover", "zoom": [1.0, 1.06, 1.12], "pan": [(0.5, 0.5)] * 3, "ease": _E}
_OUT = {"type": "cover", "zoom": [1.12, 1.06, 1.0], "pan": [(0.5, 0.5)] * 3, "ease": _E}
# Small or portrait photos, newspaper pages and maps: letterbox, modest zoom.
_PORT = {"type": "letterbox", "zoom": [1.0, 1.04, 1.08], "pan": [(0.5, 0.5)] * 3, "ease": _E}
_PORT_OUT = {"type": "letterbox", "zoom": [1.08, 1.04, 1.0], "pan": [(0.5, 0.5)] * 3, "ease": _E}
# The charts: letterbox, frozen.
_GFX = {"type": "letterbox", "zoom": [1, 1, 1], "pan": [(0.5, 0.5)] * 3}

SLIDES = [
    {"img": "HERO", **_IN},            # 0  s0   title
    {"img": "LAMBERT", **_PORT},       # 1  s1   8 December 1941, the police round up the Japanese
    {"img": "GATE", **_IN},            # 2  s2   shopkeepers to fishermen, shipped to India; few home (s3)
    {"img": "SS1955", **_PORT},        # 3  s4   Fukuda at Echigoya from 1916; manager by 1941 (s5)
    {"img": "CHANGI", **_PORT},        # 4  s6   planned to leave; raids at 3.15, arrested at 6 (s7-8)
    {"img": "ST1941", **_PORT},        # 5  s9   the Straits Times reported it; 400 at the depot (s10-11)
    {"img": "TIMELINE", **_GFX},       # 6  s12  planned since 1940; India asked in September 1941
    {"img": "PSWET", **_PORT},         # 7  s13  the SS Klang to Port Swettenham
    {"img": "CHANGI", **_PORT_OUT},    # 8  s14  brought back to Changi
    {"img": "STJ2019", **_IN},         # 9  s15  women and children on St John's Island
    {"img": "STJ1879", **_PORT},       # 10 s16  Norah Inge guards them (no portrait)
    {"img": "ST1941", **_PORT_OUT},    # 11 s17  Japanese by nationality; no citizenship until 1957 (s18)
    {"img": "PEOPLE", **_GFX},         # 12 s19  Taiwanese and Koreans; the May 1943 count (s20)
    {"img": "LAMBERT", **_PORT_OUT},   # 13 s21  the Malays mostly women; long-term residents (s22)
    {"img": "MEMORIAL", **_PORT},      # 14 s23  about 3,600 in Malaya in 1941
    {"img": "CEMETERY", **_IN},        # 15 s24  studios, chemists, hotels; Little Japan
    {"img": "STJ1879", **_PORT_OUT},   # 16 s25  400 Okinawan fishermen
    {"img": "MEMORIAL", **_PORT_OUT},  # 17 s26  the bank and trading-house managers
    {"img": "SS1955", **_PORT_OUT},    # 18 s27  Fukuda at the Anglo-Chinese School
    {"img": "CEMETERY", **_OUT},       # 19 s28  new generations born here
    {"img": "CHANGI", **_PORT},        # 20 s29  7 January 1942, a steamer from Changi
    {"img": "BOMBAY", **_IN},          # 21 s30  Bombay, then north by rail to Delhi
    {"img": "KIDDER", **_PORT},        # 22 s31  the women sail separately; Calcutta (s32-33)
    {"img": "HERO", **_OUT},           # 23 s34  joined from India, Burma, Ceylon, Iran
    {"img": "LAKE", **_PORT},          # 24 s35  the consuls kept under house arrest
    {"img": "JACKSON", **_PORT},       # 25 s36  a transit camp: 300 army tents
    {"img": "SHER", **_IN},            # 26 s37  councils, wing leaders, night patrols
    {"img": "GATE", **_OUT},           # 27 s38  the baseball season
    {"img": "HERO", **_IN},            # 28 s39  the weather; Kusalasaya (no portrait); 46 degrees (s40-41)
    {"img": "JACKSON", **_PORT_OUT},   # 29 s42  dysentery, malaria, beriberi; 106 deaths (s43)
    {"img": "LAKE", **_PORT_OUT},      # 30 s44  George Sakai (no portrait)
    {"img": "SYONAN", **_PORT},        # 31 s45  Japan protests through Switzerland
    {"img": "SHER", **_OUT},           # 32 s46  India's answer; barley and medical care (s47)
    {"img": "TIMELINE", **_GFX},       # 33 s48  the 1942 exchange at Lourenço Marques
    {"img": "BOMBAY", **_OUT},         # 34 s50  who was chosen
    {"img": "SS1955", **_PORT},        # 35 s52  Fukuda number 480; no fishermen (s53)
    {"img": "HERO", **_OUT},           # 36 s54  those left behind attack the committee
    {"img": "STJ2019", **_OUT},        # 37 s55  back to Syonan, September 1942
    {"img": "PEOPLE", **_GFX},         # 38 s56  moved to Deoli, about 2,100 people
    {"img": "SHER", **_IN},            # 39 s58  conditions better; hospital and school (s59)
    {"img": "LAKE", **_PORT},          # 40 s60  230 rock gardens
    {"img": "TIMELINE", **_GFX},       # 41 s61  a second exchange; the surrender (s62)
    {"img": "MT1946", **_PORT},        # 42 s63  the camp splits; kachi-gumi and make-gumi
    {"img": "GATE", **_IN},            # 43 s66  80 ask for protection; the wing revolts (s67)
    {"img": "MT1946", **_PORT_OUT},    # 44 s68  troops open fire; Reuters, 15 killed (s69)
    {"img": "MEMORIAL", **_PORT},      # 45 s70  19 dead in later accounts
    {"img": "HERO", **_OUT},           # 46 s71  the Emperor's broadcast via Sweden
    {"img": "SUN1946", **_PORT},       # 47 s72  left Deoli May 1946; not allowed home (s73-74)
    {"img": "STJ2019", **_IN},         # 48 s75  held at Jurong and Bukit Timah, then shipped on
    {"img": "STMAY", **_PORT},         # 49 s76  the bill; Rajagopalachari in Parliament (s77)
    {"img": "ST1951", **_PORT},        # 50 s78  Singapore's $4,644,972
    {"img": "TIMELINE", **_GFX},       # 51 s79  three-fifths for Singapore
    {"img": "SS1955", **_PORT},        # 52 s80  Fukuda reopens Echigoya, November 1955 (s81)
    {"img": "TIMELINE", **_GFX},       # 53 s82  first Japanese firm with local capital
    {"img": "CEMETERY", **_OUT},       # 54 s83  closed in 1977
    {"img": "HERO", **_IN},            # 55 s84  why it matters: forgotten in three countries
    {"img": "GATE", **_OUT},           # 56 s85  the 1929 Convention applied by analogy
    {"img": "GENEVA", **_PORT},        # 57 s86  the Fourth Geneva Convention, 1949
    {"img": "HERO", **_OUT},           # 58 s87  the gap those rules close
]

SCHEDULE = [(0.0, 0), (7.2, 1), (21.075, 2), (48.45, 3), (64.0, 4), (86.0, 5), (114.4, 6), (135.975, 7), (149.625, 8), (159.5, 9), (168.7, 10), (173.325, 11), (190.8, 12), (220.95, 13), (231.125, 14), (242.975, 15), (260.0, 16), (272.1, 17), (279.5, 18), (291.775, 19), (303.1, 20), (311.475, 21), (325.35, 22), (342.75, 23), (360.7, 24), (370.25, 25), (385.225, 26), (397.1, 27), (409.05, 28), (432.5, 29), (453.35, 30), (462.425, 31), (472.0, 32), (491.95, 33), (518.525, 34), (538.5, 35), (548.35, 36), (562.1, 37), (571.875, 38), (597.875, 39), (615.85, 40), (626.275, 41), (643.175, 42), (663.55, 43), (680.5, 44), (697.525, 45), (709.05, 46), (722.55, 47), (752.625, 48), (765.9, 49), (788.6, 50), (807.55, 51), (831.125, 52), (853.325, 53), (871.975, 54), (876.575, 55), (895.7, 56), (917.65, 57), (932.025, 58)]
TOTAL_DURATION = 939.075
TIMING_JSON = "audio/interned-in-india-singapores-japanese-civilians-1941-46.timing.json"

# The avatar presenter, cartoon with motion: the whole video (Phase 2 test).
AVATAR = {"ranges": [(0, None)], "motion": True}
