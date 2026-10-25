"""Video config for the Ghee Hin post.

The old Chinese town and its people from the 1860s to about 1910 (KITLV and
Lambert photographs of North Bridge Road, South Bridge Road, Cecil Street,
Thian Hock Keng and street sellers), a Ghee Hin membership certificate, the
Chinese Protectorate, the 1846 and 1854 Straits Times pages, the 1854 riots
map and the timeline, Clementi Smith's Vanity Fair caricature and bust, and
Thian Hock Keng and the Ying Fo Fui Kun clan hall today.

Named-person rule: the sentence naming Ho Ah Yam shows the 1846 page, the
sentences naming Buckley the 1854 page, and those naming Pickering or Wynne
the timeline or the certificate; Clementi Smith's sentences show his
caricature or his bust. Street and crowd photographs go only on sentences
that name no one.

The certificate, the newspaper pages, the map, South Bridge Road, the
street vendor and the bust are letterboxed; the timeline and the small
caricature are shown fixed.

38 slides, 568.625s. Narration: Kokoro with the OpenVoice clone.
AVATAR: first and last 30s, cartoon with motion.
"""

IMAGES = {
    "NBR": "https://upload.wikimedia.org/wikipedia/commons/thumb/8/80/KITLV_-_43317_-_Lambert_%26_Co.%2C_G.R._-_Singapore_-_The_North_Bridge_Road%2C_Singapore_-_circa_1900.tiff/lossy-page1-1280px-KITLV_-_43317_-_Lambert_%26_Co.%2C_G.R._-_Singapore_-_The_North_Bridge_Road%2C_Singapore_-_circa_1900.tiff.jpg",
    "CERT": "https://upload.wikimedia.org/wikipedia/commons/2/2d/Membership_certificate_of_the_Ghee_Hin_Kongsi_from_William_Stirling_Collection.jpg",
    "PROT": "https://upload.wikimedia.org/wikipedia/commons/thumb/5/53/Chinese_Protectorate%2C_Singapore%2C_KITLV_1404946.tiff/lossy-page1-1280px-Chinese_Protectorate%2C_Singapore%2C_KITLV_1404946.tiff.jpg",
    "THK1890": "https://upload.wikimedia.org/wikipedia/commons/thumb/8/81/KITLV_-_103742_-_Lambert_%26_Co._-_Thian_Hock_Keng_Temple_in_Singapore_-_circa_1890.tif/lossy-page1-1280px-KITLV_-_103742_-_Lambert_%26_Co._-_Thian_Hock_Keng_Temple_in_Singapore_-_circa_1890.tif.jpg",
    "SBR": "https://upload.wikimedia.org/wikipedia/commons/c/cf/Photographic_Views_of_Singapore_Plate_02_South_Bridge_Road.jpg",
    "STREET1860": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/d0/KITLV_-_29169_-_Chinese_street_in_Singapore%2C_completely_decorated_on_the_occasion_of_the_visit_of_Prince_Albert_of_Saxe-Coburg_-_Gotha%2C_husband_of_Queen_Victoria_-_1860.tif/lossy-page1-1280px-KITLV_-_29169_-_Chinese_street_in_Singapore%2C_completely_decorated_on_the_occasion_of_the_visit_of_Prince_Albert_of_Saxe-Coburg_-_Gotha%2C_husband_of_Queen_Victoria_-_1860.tif.jpg",
    "VENDOR": "https://upload.wikimedia.org/wikipedia/commons/thumb/1/10/KITLV_-_103776_-_Chinese_street_vendor_in_Singapore_-_circa_1890.tif/lossy-page1-1280px-KITLV_-_103776_-_Chinese_street_vendor_in_Singapore_-_circa_1890.tif.jpg",
    "CECIL": "https://upload.wikimedia.org/wikipedia/commons/thumb/8/84/KITLV_-_79924_-_Kleingrothe%2C_C.J._-_Medan_-_Cecil_Street%2C_Singapore_-_circa_1910.tif/lossy-page1-1280px-KITLV_-_79924_-_Kleingrothe%2C_C.J._-_Medan_-_Cecil_Street%2C_Singapore_-_circa_1910.tif.jpg",
    "CAKE": "https://upload.wikimedia.org/wikipedia/commons/thumb/f/fa/KITLV_-_50188_-_Lambert_%26_Co.%2C_G.R._-_Singapore_-_Chinese_cookie_sellers_in_Singapore_-_circa_1900.tif/lossy-page1-1280px-KITLV_-_50188_-_Lambert_%26_Co.%2C_G.R._-_Singapore_-_Chinese_cookie_sellers_in_Singapore_-_circa_1900.tif.jpg",
    "ST1846": "/assets/images/straits-times-1846-03-18-page-2.jpg",
    "MAP": "/assets/images/ghee-hin-1854-riots-map.png",
    "ST1854": "/assets/images/straits-times-1854-06-13-page-4.jpg",
    "TL": "/assets/images/ghee-hin-timeline-chart.png",
    "CLEM": "https://upload.wikimedia.org/wikipedia/commons/1/1b/Cecil_Clementi_Smith_Vanity_Fair_1892-01-23.jpg",
    "BUST": "https://upload.wikimedia.org/wikipedia/commons/thumb/b/b2/Bust_of_Sir_Cecil_Clementi_Smith%2C_Victoria_Concert_Hall%2C_Singapore_-_20141101-01.JPG/1280px-Bust_of_Sir_Cecil_Clementi_Smith%2C_Victoria_Concert_Hall%2C_Singapore_-_20141101-01.JPG",
    "YING": "https://upload.wikimedia.org/wikipedia/commons/thumb/8/8c/Ying_Fo_Fui_Kun%2C_Telok_Ayer_Street%2C_October_2025.jpg/1280px-Ying_Fo_Fui_Kun%2C_Telok_Ayer_Street%2C_October_2025.jpg",
    "THK2023": "https://upload.wikimedia.org/wikipedia/commons/thumb/5/52/Thian_Hock_Keng_Temple%2C_20230630.jpg/1280px-Thian_Hock_Keng_Temple%2C_20230630.jpg",
}

# The timeline PNG is the only image not captioned in the post or its gallery.
CREDITS = {
    "TL": "Timeline by Lesser Known Singapore, from BiblioAsia, Cheng Siok-Hwa (1972), C. B. Buckley (1902) and the National Library Board",
}

# The channel's 2x2 thumbnail grid, 1860s to today: a decorated Chinese street of the 1860s,
# Thian Hock Keng around 1890, North Bridge Road around 1900 and the Ying Fo
# Fui Kun clan hall in 2025.
THUMBNAIL = [
    {"img": "STREET1860", "pan": (0.5, 0.5)},
    {"img": "THK1890", "pan": (0.5, 0.5)},
    {"img": "NBR", "pan": (0.5, 0.5)},
    {"img": "YING", "pan": (0.5, 0.5)},
]

_E = "ease-in-out"
_IN = {"type": "cover", "zoom": [1.0, 1.06, 1.12], "pan": [(0.5, 0.5)] * 3, "ease": _E}
_OUT = {"type": "cover", "zoom": [1.12, 1.06, 1.0], "pan": [(0.5, 0.5)] * 3, "ease": _E}
# The certificate, the newspaper pages, the map and the small or portrait images: letterbox, modest zoom.
_PORT = {"type": "letterbox", "zoom": [1.0, 1.04, 1.08], "pan": [(0.5, 0.5)] * 3, "ease": _E}
_PORT_OUT = {"type": "letterbox", "zoom": [1.08, 1.04, 1.0], "pan": [(0.5, 0.5)] * 3, "ease": _E}
# The timeline and the small caricature: letterboxed and still.
_FIX = {"type": "letterbox", "zoom": [1.0, 1.0, 1.0], "pan": [(0.5, 0.5)] * 3, "ease": "linear"}

SLIDES = [
    {"img": "NBR", **_IN},            # 0  s0 title
    {"img": "CERT", **_PORT},         # 1  s1 the 1890 law; sixty years of the societies (s1-2)
    {"img": "PROT", **_IN},           # 2  s3 the headmen hand in seals, flags and books
    {"img": "THK1890", **_IN},        # 3  s4 the Tiandihui; Qing and Ming (s4-5)
    {"img": "CERT", **_PORT_OUT},     # 4  s6 initiation; secret signs
    {"img": "SBR", **_PORT},          # 5  s7 the Ghee Hin, 1820s, Rochor Road (s7-8)
    {"img": "STREET1860", **_IN},     # 6  s9 mutual aid; rival societies (s9-10)
    {"img": "NBR", **_OUT},           # 7  s11 the Chinese population (s11-13)
    {"img": "VENDOR", **_PORT},       # 8  s14 met off the ships, found work
    {"img": "CECIL", **_IN},          # 9  s15 few ways to reach them; a tiny police force (s15-16)
    {"img": "CAKE", **_IN},           # 10 s17 the trades they controlled; opium revenue (s17-18)
    {"img": "STREET1860", **_OUT},    # 11 s19 rivalry turns violent
    {"img": "ST1846", **_PORT},       # 12 s20 Ho Ah Yam's funeral, 1846 (names him: the 1846 page, s20-21)
    {"img": "THK1890", **_OUT},       # 13 s22 February 1851
    {"img": "MAP", **_PORT},          # 14 s23 May 1854; the rice quarrel (s23-24)
    {"img": "ST1854", **_PORT},       # 15 s25 Buckley's account (names him: the 1854 page, s25-26)
    {"img": "MAP", **_PORT_OUT},      # 16 s27 400 dead; the special criminal session (s27-28)
    {"img": "SBR", **_PORT_OUT},      # 17 s29 the 1876 post office riot (s29-30)
    {"img": "TL", **_FIX},            # 18 s31 registration, 1869 (s31-32)
    {"img": "CERT", **_PORT},         # 19 s33 the registers faked (s33-34)
    {"img": "TL", **_FIX},            # 20 s35 the Protectorate; Pickering (names him: no people, s35-36)
    {"img": "CECIL", **_OUT},         # 21 s37 1882 and 1885; 49,000 to 65,000 (s37-38)
    {"img": "TL", **_FIX},            # 22 s39 Pickering attacked, 1887 (names him: no people)
    {"img": "CLEM", **_FIX},          # 23 s40 Clementi Smith becomes Governor (shows him, s40-41)
    {"img": "CERT", **_PORT_OUT},     # 24 s42 Pickering and the police chief oppose the bill (no people)
    {"img": "BUST", **_PORT},         # 25 s43 the Legislative Council vote
    {"img": "PROT", **_IN},           # 26 s44 the ordinance in force; its rules (s44-45)
    {"img": "CLEM", **_FIX},          # 27 s46 the Governor reports the hand-over (shows him)
    {"img": "CERT", **_PORT},         # 28 s47 seals and certificates to the museum
    {"img": "PROT", **_OUT},          # 29 s48 the Chinese Advisory Boards (s48-49)
    {"img": "NBR", **_IN},            # 30 s50 the ban did not end the societies (s50-51)
    {"img": "YING", **_IN},           # 31 s52 the clan and dialect associations
    {"img": "TL", **_FIX},            # 32 s53 Wynne's dilemma (names him: no people)
    {"img": "THK2023", **_IN},        # 33 s54 gangs; the 1950s crackdown
    {"img": "YING", **_OUT},          # 34 s55 the Societies Act today (s55-56)
    {"img": "CAKE", **_OUT},          # 35 s57 where it fits
    {"img": "TL", **_FIX},            # 36 s58 a turning point
    {"img": "THK2023", **_OUT},       # 37 s59 the rule that outlasted the colony
]

SCHEDULE = [
    (0.0, 0), (5.05, 1), (33.125, 2), (42.025, 3), (63.85, 4), (74.85, 5),
    (91.05, 6), (113.275, 7), (136.625, 8), (147.875, 9), (166.525, 10), (185.125, 11),
    (189.65, 12), (207.95, 13), (218.2, 14), (232.8, 15), (258.65, 16), (269.525, 17),
    (288.0, 18), (306.35, 19), (317.95, 20), (340.55, 21), (358.125, 22), (365.775, 23),
    (381.7, 24), (386.05, 25), (397.975, 26), (424.425, 27), (435.325, 28), (445.8, 29),
    (469.85, 30), (480.5, 31), (490.6, 32), (504.3, 33), (516.3, 34), (535.175, 35),
    (548.4, 36), (563.55, 37),
]
TOTAL_DURATION = 568.625
TIMING_JSON = "audio/the-ghee-hin-and-the-1890-ban-on-the-secret-societies.timing.json"

# The avatar presenter, cartoon with motion: corner bubble for the first and last 30 s.
AVATAR = {"ranges": [(0, 30), (-30, None)], "motion": True}
