"""Video config for the Southern Special Students post.

From the Syonan Shimbun's reports of 1943 and 1944 to Hiroshima University
and the Peace Memorial Park today: eleven whole Syonan Shimbun pages on the
scheme (the plan, the Woodsville trainees, the arrivals in Tokyo, the 1944
selection, the Johor students' return), Tokyo and Waseda then and now, the
Hiroshima University of Literature and Science before and after the bombing,
the two clouds of 6 August 1945, and the cenotaph.

Named-person rule: Bostam, Kasmani, Abdul Razak, Nik Yusof, Syed Omar,
Kazuo Aoki, Meiko Kurihara, Dr Hamajima and the Sonobes have no free
photographs, so their sentences show newspaper pages, buildings and ruins
only, never a crowd. Ungku Aziz, Pengiran Yusuf and Marquis Tokugawa get
their own portraits. The 1938 Nijubashi photo was passed over because it
shows a crowd of Hitler Youth, and the Kyoto University Hospital photo
because the sources say only "a hospital in Kyoto".

Newspaper pages and portraits are letterboxed with a modest zoom.

45 slides, 944.9s. Narration: Kokoro with the OpenVoice clone.
AVATAR: first and last 30s, cartoon with motion.
"""

_U = "https://upload.wikimedia.org/wikipedia/commons"
_C = f"{_U}/thumb"
_SS = "/assets/images/syonan-shimbun-"

IMAGES = {
    "HERO": f"{_C}/c/cc/Ruins_of_Hiroshima_University_of_Literature_and_Science.jpg/1280px-Ruins_of_Hiroshima_University_of_Literature_and_Science.jpg",
    "SS430413": f"{_SS}1943-04-13-page-1.jpg",
    "SS430604": f"{_SS}1943-06-04-page-1.jpg",
    "SS430702": f"{_SS}1943-07-02-page-1.jpg",
    "SS430726": f"{_SS}1943-07-26-page-2.jpg",
    "SS430807": f"{_SS}1943-08-07-page-2.jpg",
    "SS440131": f"{_SS}1944-01-31-page-2.jpg",
    "SS440203": f"{_SS}1944-02-03-page-1.jpg",
    "SS440422": f"{_SS}1944-04-22-page-2.jpg",
    "SS440612": f"{_SS}1944-06-12-page-1.jpg",
    "SS440704": f"{_SS}1944-07-04-page-1.jpg",
    "SS450420": f"{_SS}1945-04-20-page-2.jpg",
    "WOODS": f"{_C}/7/72/Upp_Serangoon_Rd_bef_Woodsville_Flyover_20060409.jpg/1280px-Upp_Serangoon_Rd_bef_Woodsville_Flyover_20060409.jpg",
    "CLOUDK": f"{_U}/6/65/Atomic_cloud_over_Hiroshima_from_the_Kure_Naval_Arsenal.jpg",
    "CLOUDC": f"{_C}/b/b7/Atomic_cloud_over_Hiroshima.jpg/1280px-Atomic_cloud_over_Hiroshima.jpg",
    "OKUMA1927": f"{_U}/8/83/Waseda_University_-_Okuma_Auditorium_inauguration.jpg",
    "OKUMA2010": f"{_C}/5/56/Waseda_University_-_Okuma_auditorium_and_Okuma_tower.JPG/1280px-Waseda_University_-_Okuma_auditorium_and_Okuma_tower.JPG",
    "TOKYOSTN": f"{_C}/d/d0/Devastated_Tokyo_station_building_from_platform.jpg/1280px-Devastated_Tokyo_station_building_from_platform.jpg",
    "TOKUGAWA": f"{_U}/1/1f/Tokugawa_Yoshichika_01.jpg",
    "TOKYO1945": f"{_U}/2/20/Tokyo_kushu_1945-4.jpg",
    "GATE": f"{_C}/c/cb/Hiroshima_Bunrika_University-old1.jpg/1280px-Hiroshima_Bunrika_University-old1.jpg",
    "REMAINS": f"{_C}/6/6b/Fire-_and_blast-damaged_remains_of_Hiroshima_University_of_Literature_and_Science.jpg/1280px-Fire-_and_blast-damaged_remains_of_Hiroshima_University_of_Literature_and_Science.jpg",
    "ATOMIC": f"{_C}/2/2c/AtomicEffects-Hiroshima.jpg/1280px-AtomicEffects-Hiroshima.jpg",
    "MUSEUM": f"{_C}/a/a3/Blast-damaged_ruins_of_Hiroshima_University_Museum.jpg/1280px-Blast-damaged_ruins_of_Hiroshima_University_Museum.jpg",
    "REDCROSS": f"{_U}/1/11/Hiroshima_red_cross_hospital_october_1945.jpg",
    "LAB": f"{_C}/4/4f/Fire-damaged_chemical_lab%2C_Hiroshima_University_of_Literature_and_Science.jpg/1280px-Fire-damaged_chemical_lab%2C_Hiroshima_University_of_Literature_and_Science.jpg",
    "BOOKS": f"{_C}/b/b4/Fire-damaged_interior_with_books_reduced_to_ashes%2C_Hiroshima_University_of_Literature_and_Science.jpg/1280px-Fire-damaged_interior_with_books_reduced_to_ashes%2C_Hiroshima_University_of_Literature_and_Science.jpg",
    "UNGKU": f"{_U}/c/cf/Ungku_Abdul_Aziz.jpg",
    "YUSUF65": f"{_U}/b/b8/Pengiran_Muhammad_Yusuf_bin_Abdul_Rahim.jpg",
    "OLDBLDG": f"{_C}/d/dc/Hiroshima_Bunrika_Daigaku_02.JPG/1280px-Hiroshima_Bunrika_Daigaku_02.JPG",
    "OLDBLDG2": f"{_C}/a/a9/Hiroshima_University_Former_School_Building_01.jpg/1280px-Hiroshima_University_Former_School_Building_01.jpg",
    "HUCAMPUS": f"{_C}/c/cf/Hiroshima_University_Higashi_Hiroshima_Campus_01.jpg/1280px-Hiroshima_University_Higashi_Hiroshima_Campus_01.jpg",
    "HU1955": f"{_C}/b/bd/Hiroshima_University_1955.jpg/1280px-Hiroshima_University_1955.jpg",
    "ABOMB": f"{_U}/5/51/A-Bomb_Dome.jpg",
    "CENOTAPH": f"{_C}/d/d8/Hiroshima_Peace_Memorial_Park_cenotaph.jpg/1280px-Hiroshima_Peace_Memorial_Park_cenotaph.jpg",
    "YASUDA": f"{_C}/d/de/Yasuda_Auditorium.jpg/1280px-Yasuda_Auditorium.jpg",
    "PEACEPARK": f"{_C}/1/11/Hiroshima_Peace_Memorial_Park%2C_20240817_1032_4210.jpg/1280px-Hiroshima_Peace_Memorial_Park%2C_20240817_1032_4210.jpg",
}

_NSG = "The Syonan Shimbun, via NewspaperSG, National Library Board Singapore, public domain"

# Credits for images not captioned in the post or its gallery.
CREDITS = {
    "SS440131": _NSG,
    "SS440203": _NSG,
    "SS440704": _NSG,
    "OKUMA1927": "Unknown author, public domain, via Wikimedia Commons",
    "OKUMA2010": "XIIIfromTOKYO, CC BY-SA 3.0, via Wikimedia Commons",
    "TOKUGAWA": "Unknown author, public domain, via Wikimedia Commons",
    "TOKYO1945": "Ishikawa Koyo, public domain, via Wikimedia Commons",
    "ATOMIC": "United States Government, public domain, via Wikimedia Commons",
    "REDCROSS": "Shunkichi Kikuchi, public domain, via Wikimedia Commons",
    "UNGKU": "Victor Pogadaev, CC BY-SA 4.0, via Wikimedia Commons",
    "OLDBLDG2": "Taisyo, CC BY 3.0, via Wikimedia Commons",
    "ABOMB": "Dan Smith, CC BY-SA 2.5, via Wikimedia Commons",
    "YASUDA": "Wiiii, CC BY-SA 3.0, via Wikimedia Commons",
    "PEACEPARK": "Jakub Halun, CC BY 4.0, via Wikimedia Commons",
}

# The channel's 2x2 thumbnail grid, 1943 to today: the 4 June 1943 report
# naming the two Syonan trainees (zoomed to its headline), the cloud over
# Hiroshima, the university's ruins in November 1945, and the cenotaph.
THUMBNAIL = [
    {"img": "SS430604", "zoom": 3.0, "pan": (0.40, 0.74)},
    {"img": "CLOUDK", "pan": (0.5, 0.35)},
    {"img": "HERO", "pan": (0.5, 0.5)},
    {"img": "CENOTAPH", "pan": (0.5, 0.5)},
]

_E = "ease-in-out"
_IN = {"type": "cover", "zoom": [1.0, 1.06, 1.12], "pan": [(0.5, 0.5)] * 3, "ease": _E}
_OUT = {"type": "cover", "zoom": [1.12, 1.06, 1.0], "pan": [(0.5, 0.5)] * 3, "ease": _E}
# Newspaper pages, portraits and small photos: letterbox, modest zoom.
_PORT = {"type": "letterbox", "zoom": [1.0, 1.04, 1.08], "pan": [(0.5, 0.5)] * 3, "ease": _E}
_PORT_OUT = {"type": "letterbox", "zoom": [1.08, 1.04, 1.0], "pan": [(0.5, 0.5)] * 3, "ease": _E}

SLIDES = [
    {"img": "HERO", **_IN},               # 0  s0  title
    {"img": "SS430604", **_PORT},         # 1  s1  33 trainees at Woodsville
    {"img": "WOODS", **_IN},              # 2  s2  fifteen best to Japan
    {"img": "SS430604", **_PORT_OUT},     # 3  s3  Bostam and Kasmani
    {"img": "SS430807", **_PORT},         # 4  s4  about 200 Southern Special Students
    {"img": "CLOUDK", **_PORT},           # 5  s5  Hiroshima, 6 August 1945
    {"img": "SS430413", **_PORT},         # 6  s6  the plan, 13 April 1943 (s6-9)
    {"img": "OKUMA1927", **_PORT},        # 7  s10 the terms (s10-13)
    {"img": "SS440203", **_PORT},         # 8  s14 Aoki's aims (s14-16)
    {"img": "SS430726", **_PORT},         # 9  s17 the Ryugakusei Kunrenjo course (s17-20)
    {"img": "SS430702", **_PORT},         # 10 s21 the fifteen leave
    {"img": "TOKYOSTN", **_IN},           # 11 s22 Tokyo Station, Imperial Palace (s22-23)
    {"img": "SS430726", **_PORT_OUT},     # 12 s24 the 18 left behind (s24-25)
    {"img": "OKUMA2010", **_IN},          # 13 s26 Waseda (s26-27)
    {"img": "TOKUGAWA", **_PORT},         # 14 s28 the Tokugawa mansion
    {"img": "SS430807", **_PORT_OUT},     # 15 s29 20 Malayans in Japan
    {"img": "SS440131", **_PORT},         # 16 s30 the 1944 selection (s30-31)
    {"img": "SS440422", **_PORT},         # 17 s32 the four of 1944
    {"img": "SS440612", **_PORT},         # 18 s33 the second group of 89
    {"img": "SS440422", **_PORT_OUT},     # 19 s34 Abdul Razak, Nik Yusof, Syed Omar (s34-36)
    {"img": "SS440704", **_PORT},         # 20 s37 life in Japan (s37-38)
    {"img": "TOKYO1945", **_IN},          # 21 s39 the war turns; raids on Tokyo (s39-40)
    {"img": "GATE", **_PORT},             # 22 s41 nine at Hiroshima; Konan dormitory (s41-43)
    {"img": "CLOUDC", **_PORT},           # 23 s44 the bomb (s44-45)
    {"img": "REMAINS", **_IN},            # 24 s46 Abdul Razak in the lecture room (s46-47)
    {"img": "ATOMIC", **_IN},             # 25 s48 Nik Yusof, towards Itsukaichi (s48-49)
    {"img": "MUSEUM", **_PORT},           # 26 s50 the urn at Kozenji
    {"img": "REDCROSS", **_PORT},         # 27 s51 sleeping in the open; Kurihara (s51-52)
    {"img": "LAB", **_IN},                # 28 s53 Syed Omar's fever
    {"img": "BOOKS", **_IN},              # 29 s54 the journey home; Kyoto (s54-57)
    {"img": "CLOUDK", **_PORT_OUT},       # 30 s58 his death; Razak's postcard (s58-59)
    {"img": "SS450420", **_PORT},         # 31 s60 the Johor students home (s60-62)
    {"img": "UNGKU", **_PORT},            # 32 s63 Ungku Abdul Aziz
    {"img": "YUSUF65", **_PORT},          # 33 s64 Pengiran Muhammad Yusuf (s64-65)
    {"img": "OLDBLDG2", **_IN},           # 34 s66 Abdul Razak's life (s66-68)
    {"img": "HUCAMPUS", **_IN},           # 35 s69 honorary doctorate
    {"img": "HU1955", **_IN},             # 36 s70 leaders of independent countries (s70-71)
    {"img": "ABOMB", **_IN},              # 37 s72 remembered by strangers; the graves (s72-76)
    {"img": "OLDBLDG", **_IN},            # 38 s77 the university's part
    {"img": "CENOTAPH", **_IN},           # 39 s78 the register (s78-80)
    {"img": "YASUDA", **_IN},             # 40 s81 government scholarships (s81-83)
    {"img": "OKUMA2010", **_OUT},         # 41 s84 AOTS, 1986 (s84-85)
    {"img": "WOODS", **_OUT},             # 42 s86 forty years after Woodsville
    {"img": "PEACEPARK", **_IN},          # 43 s87 where it fits (s87-88)
    {"img": "HERO", **_OUT},              # 44 s89 close
]

SCHEDULE = [
    (0.0, 0), (7.65, 1), (25.325, 2), (31.4, 3), (38.35, 4), (50.55, 5),
    (62.5, 6), (106.125, 7), (142.675, 8), (174.8, 9), (213.875, 10), (218.15, 11),
    (244.175, 12), (266.6, 13), (289.975, 14), (297.75, 15), (305.0, 16), (328.525, 17),
    (349.675, 18), (359.55, 19), (397.175, 20), (423.15, 21), (432.9, 22), (464.5, 23),
    (479.425, 24), (492.675, 25), (505.75, 26), (513.625, 27), (532.425, 28), (543.55, 29),
    (569.2, 30), (590.175, 31), (619.675, 32), (636.75, 33), (668.075, 34), (703.625, 35),
    (715.975, 36), (731.25, 37), (786.225, 38), (804.35, 39), (833.15, 40), (859.475, 41),
    (890.175, 42), (902.925, 43), (931.225, 44),
]
TOTAL_DURATION = 944.9
TIMING_JSON = "audio/the-southern-special-students-malayan-youths-sent-to-japan-1943-45.timing.json"

# The avatar presenter, cartoon with motion: corner bubble for the first and last 30 s.
AVATAR = {"ranges": [(0, 30), (-30, None)], "motion": True}
