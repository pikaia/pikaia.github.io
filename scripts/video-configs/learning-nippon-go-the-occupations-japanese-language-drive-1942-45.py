"""Video config for the Learning Nippon-go post.

The story is told mostly through whole Syonan Times / Syonan Shimbun pages
(always letterboxed, never cropped to one story) and the Belajarlah poster.
Named people get their own photograph or none: Ibuse Masuji (s4, s13) and
Jinbo Kotaro (s29). The author's Yokohama aside (s53-57) gets a Yokohama view
and the lesson pages, no other person. Street in Shonan, the Cathay Building
and the shrine are small, so they are letterboxed with a modest zoom.
Video-only: the British surrender photograph, the 1942 Syonan-to map, the
Hiroshima aerial view (for Black Rain), the shrine in Syonan (for the bowing
rule), an Occupation ten-dollar note (for the allowances) and Minato Mirai
from Osanbashi Pier (Yokohama, a present-day stand-in). The timeline is
letterboxed and frozen.

48 slides, 642.075s. Narration: Kokoro with the OpenVoice clone.
AVATAR: first and last 30s, cartoon with motion.
"""

_U = "https://upload.wikimedia.org/wikipedia/commons"
_C = f"{_U}/thumb"
_A = "/assets/images"

IMAGES = {
    "HERO": f"{_U}/f/f2/Belajarlah_Pakailah_Bahasa_Nippon.jpg",
    "FEB21": f"{_A}/syonan-shimbun-1942-02-21-page-4.jpg",
    "JUL1": f"{_A}/syonan-shimbun-1942-07-01-page-4.jpg",
    "JUN4": f"{_A}/syonan-shimbun-1942-06-04-page-1.jpg",
    "NOV13": f"{_A}/syonan-shimbun-1943-11-13-page-1.jpg",
    "JUN20": f"{_A}/syonan-shimbun-1945-06-20-page-6.jpg",
    "JUN23": f"{_A}/syonan-shimbun-1942-06-23-page-3.jpg",
    "TIMELINE": f"{_A}/nippongo-timeline-chart.png",
    # Gallery images:
    "STREET": f"{_U}/f/fc/Street_in_Shonan.JPG",
    "QUEEN": f"{_C}/f/f6/%27Queen_Street._Singapore.%2C_KITLV_1404750.tiff/lossy-page1-1280px-%27Queen_Street._Singapore.%2C_KITLV_1404750.tiff.jpg",
    "CATHAY": f"{_U}/5/57/The_Cathay_Building_in_Singapore_1945.jpg",
    "IBUSE": f"{_U}/b/b1/Masuji_Ibuse_01.jpg",
    "JINBO": f"{_C}/0/00/Jimbo_Kotaro.jpg/1280px-Jimbo_Kotaro.jpg",
    "DOWNTOWN": f"{_C}/5/58/Downtown_Singapore_%28Syonan%29%2C_Djawa_Baroe%2C_Vol._1%2C_Iss._4_%281943-02-15%29%2C_p18.jpg/1280px-Downtown_Singapore_%28Syonan%29%2C_Djawa_Baroe%2C_Vol._1%2C_Iss._4_%281943-02-15%29%2C_p18.jpg",
    "FEB26": f"{_A}/syonan-shimbun-1942-02-26-page-4.jpg",
    "MAR20": f"{_A}/syonan-shimbun-1942-03-20-page-2.jpg",
    "AUG1": f"{_A}/syonan-shimbun-1942-08-01-page-4.jpg",
    "OCT8": f"{_A}/syonan-shimbun-1942-10-08-page-4.jpg",
    "NOV11": f"{_A}/syonan-shimbun-1943-11-11-page-1.jpg",
    "FEB44": f"{_A}/syonan-shimbun-1944-02-02-page-2.jpg",
    # Not in this post's captions (credited below):
    "SURRENDER": f"{_C}/2/22/BritishSurrender.jpg/1280px-BritishSurrender.jpg",
    "MAP": f"{_C}/4/4a/SyonanSingapore.jpg/1280px-SyonanSingapore.jpg",
    "HIROSHIMA": f"{_C}/4/41/Hiroshima_aerial_view_after_atomic_bomb_8-1945.jpeg/1280px-Hiroshima_aerial_view_after_atomic_bomb_8-1945.jpeg",
    "SHRINE": f"{_U}/8/80/Shinto_shrine_in_Shonan_%28Singapore%29_-_194210.jpg",
    "NOTE10": f"{_C}/b/ba/MAL-M7c-Malaya-Japanese_Occupation-10_Dollars_ND_%281944%29.jpg/1280px-MAL-M7c-Malaya-Japanese_Occupation-10_Dollars_ND_%281944%29.jpg",
    "YOKOHAMA": f"{_U}/e/e2/Minato_Mirai_21_views_from_Osanbashi_Pier.jpg",
}

# Credits for images not captioned in the post or its gallery.
CREDITS = {
    "TIMELINE": "Timeline by Lesser Known Singapore",
    "SURRENDER": "Japanese official photographer, public domain, via Wikimedia Commons",
    "MAP": "Magyer Lohasa, CC BY-SA 4.0, via Wikimedia Commons",
    "HIROSHIMA": "U.S. Navy, public domain, via Wikimedia Commons",
    "SHRINE": "Unknown author, public domain, via Wikimedia Commons",
    "NOTE10": "National Museum of American History, public domain, via Wikimedia Commons",
    "YOKOHAMA": "Dandy1022, CC BY-SA 3.0, via Wikimedia Commons",
}

_E = "ease-in-out"
_IN = {"type": "cover", "zoom": [1.0, 1.06, 1.12], "pan": [(0.5, 0.5)] * 3, "ease": _E}
_OUT = {"type": "cover", "zoom": [1.12, 1.06, 1.0], "pan": [(0.5, 0.5)] * 3, "ease": _E}
# Portraits, newspaper pages, the poster, the map and small photos: letterbox, modest zoom.
_PORT = {"type": "letterbox", "zoom": [1.0, 1.04, 1.08], "pan": [(0.5, 0.5)] * 3, "ease": _E}
_PORT_OUT = {"type": "letterbox", "zoom": [1.08, 1.04, 1.0], "pan": [(0.5, 0.5)] * 3, "ease": _E}
# The timeline: letterbox, frozen.
_GFX = {"type": "letterbox", "zoom": [1, 1, 1], "pan": [(0.5, 0.5)] * 3}

SLIDES = [
    {"img": "HERO", **_PORT},          # 0  s0   title
    {"img": "SURRENDER", **_IN},       # 1  s1   six days after the British surrender
    {"img": "FEB21", **_PORT},         # 2  s2   the first Nippon Lesson, page 4
    {"img": "IBUSE", **_PORT},         # 3  s4   printer and publisher: Ibuse Masuji
    {"img": "MAP", **_PORT},           # 4  s6   three and a half years; Singapore and Malaya
    {"img": "STREET", **_PORT},        # 5  s7   the lessons appeared almost every day
    {"img": "MAR20", **_PORT},         # 6  s8   Lesson 24, kurisumasu
    {"img": "FEB26", **_PORT},         # 7  s9   "Nippon Lessons Appreciated"
    {"img": "DOWNTOWN", **_PORT},      # 8  s10  the children calling "Ikaga desu ka?"
    {"img": "FEB26", **_PORT_OUT},     # 9  s11  the father: good jobs
    {"img": "IBUSE", **_PORT_OUT},     # 10 s13  Ibuse conscripted into the propaganda unit
    {"img": "HIROSHIMA", **_PORT},     # 11 s14  Black Rain, the bombing of Hiroshima
    {"img": "TIMELINE", **_GFX},       # 12 s15  the policy set in Tokyo
    {"img": "QUEEN", **_IN},           # 13 s17  English, the language of the old colonial government
    {"img": "JUN4", **_PORT},          # 14 s18  "Manabe Tukae Nippon-go"
    {"img": "HERO", **_PORT_OUT},      # 15 s19  the poster in three languages
    {"img": "JUL1", **_PORT},          # 16 s20  the 1 July 1942 schools report
    {"img": "MAP", **_PORT_OUT},       # 17 s22  Malay, English, Chinese and Indian schools
    {"img": "JUL1", **_PORT_OUT},      # 18 s23  "English has been discarded"
    {"img": "DOWNTOWN", **_PORT_OUT},  # 19 s24  parents keeping children home; teachers dismissed
    {"img": "FEB44", **_PORT},         # 20 s26  radio lessons printed in the paper
    {"img": "SHRINE", **_PORT},        # 21 s27  bowing towards the Imperial Palace
    {"img": "QUEEN", **_OUT},          # 22 s28  the Syonan Nippon Gakuen
    {"img": "JINBO", **_PORT},         # 23 s29  opened under the poet Jinbo Kotaro
    {"img": "JUN4", **_PORT_OUT},      # 24 s30  about 100 boys and girls
    {"img": "CATHAY", **_PORT},        # 25 s31  graduation at the former Cathay Theatre
    {"img": "AUG1", **_PORT},          # 26 s32  short and popular courses
    {"img": "OCT8", **_PORT},          # 27 s33  234 of 734 applicants
    {"img": "STREET", **_PORT_OUT},    # 28 s34  renamed Gunseikanbu Kokugo Gakko; Queen Street, 1944
    {"img": "NOV11", **_PORT},         # 29 s35  paid to learn; the allowances report
    {"img": "NOTE10", **_PORT},        # 30 s37  $50, $30, $10 and $5 a month
    {"img": "TIMELINE", **_GFX},       # 31 s38  graded examinations, February 1945
    {"img": "NOV13", **_PORT},         # 32 s40  two Nippon-go Weeks
    {"img": "FEB44", **_PORT_OUT},     # 33 s43  "five Nippon-Go words daily"
    {"img": "NOV11", **_PORT_OUT},     # 34 s45  "Speak Nippon-Go" notices
    {"img": "JUN20", **_PORT},         # 35 s46  claiming success
    {"img": "DOWNTOWN", **_PORT},      # 36 s47  younger people in Japanese firms and offices
    {"img": "JUN20", **_PORT_OUT},     # 37 s48  "a very small percentage"
    {"img": "MAP", **_PORT},           # 38 s49  a short time to change a city's language
    {"img": "CATHAY", **_PORT_OUT},    # 39 s50  the last issue; British forces arrive
    {"img": "JUN23", **_PORT},         # 40 s51  the lessons reach grammar
    {"img": "YOKOHAMA", **_IN},        # 41 s53  the AOTS scholarship, Yokohama
    {"img": "FEB21", **_PORT_OUT},     # 42 s55  intensive teaching, no word on structure
    {"img": "JUN23", **_PORT_OUT},     # 43 s56  subject, object, verb
    {"img": "YOKOHAMA", **_OUT},       # 44 s57  a smattering; a wasted opportunity
    {"img": "HERO", **_PORT},          # 45 s58  why it matters: by order
    {"img": "MAR20", **_PORT_OUT},     # 46 s59  Japanese taught by choice since 1978
    {"img": "HERO", **_PORT_OUT},      # 47 s60  made to learn, or choosing to
]

SCHEDULE = [(0.0, 0), (7.8, 1), (18.65, 2), (30.65, 3), (43.625, 4), (60.75, 5), (65.7, 6), (84.0, 7), (101.625, 8), (109.075, 9), (119.75, 10), (133.625, 11), (143.575, 12), (164.525, 13), (171.125, 14), (182.975, 15), (194.075, 16), (213.175, 17), (229.6, 18), (243.025, 19), (255.575, 20), (269.0, 21), (281.025, 22), (288.875, 23), (299.125, 24), (304.9, 25), (322.625, 26), (325.75, 27), (340.4, 28), (358.025, 29), (383.85, 30), (404.9, 31), (421.025, 32), (454.775, 33), (466.55, 34), (473.525, 35), (477.775, 36), (491.975, 37), (506.275, 38), (518.65, 39), (528.8, 40), (547.625, 41), (572.15, 42), (578.225, 43), (592.425, 44), (600.225, 45), (617.325, 46), (633.8, 47)]
TOTAL_DURATION = 642.075
TIMING_JSON = "audio/learning-nippon-go-the-occupations-japanese-language-drive-1942-45.timing.json"

# The avatar presenter, cartoon with motion: corner bubble for the first and last 30 s.
AVATAR = {"ranges": [(0, 30), (-30, None)], "motion": True}
