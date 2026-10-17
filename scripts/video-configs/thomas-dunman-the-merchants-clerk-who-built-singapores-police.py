"""Video config for the Thomas Dunman post.

Dunman's police are told through the buildings and streets of the town: the
police court and Central Police Station on South Bridge Road, the square
behind the court, the Tanjong Pagar station and its constables, and prints and
photographs of the town (Grosse 1866, Shopping 1860, the Bras Basah jail).
Named people get their own picture or none: Dunman's portrait (s2, s12-13,
s18-19, s50-51, s54, s78), Farquhar (s4-5, s73), Thomson (s9-10, s17),
Butterworth (s46, s49) and Cavenagh (s56); Buckley, Bernard, Pickering,
Tan Tock Seng (the hospital instead) and Cheang Hong Lim (the park) get a
building or a scene with no portrait. The small photographs, portraits and the
certificate are letterboxed with a modest zoom; the timeline is letterboxed
and frozen.
Video-only: Farquhar's portrait from the Farquhar posts, Thomson's portrait
from the Thomson post and the Pearl's Hill hospital from the Tan Tock Seng
post.

54 slides, 782.7s. Narration: Kokoro with the OpenVoice clone.
AVATAR: first and last 30s, cartoon with motion.
"""

_U = "https://upload.wikimedia.org/wikipedia/commons"
_C = f"{_U}/thumb"
_A = "/assets/images"

IMAGES = {
    "HERO": f"{_C}/8/8c/KITLV_-_103754_-_Lambert_%26_Co._-_Court_of_the_police_at_South_Bridge_Road%2C_Singapore_-_circa_1885.tif/lossy-page1-1280px-KITLV_-_103754_-_Lambert_%26_Co._-_Court_of_the_police_at_South_Bridge_Road%2C_Singapore_-_circa_1885.tif.jpg",
    "DUNMAN": f"{_U}/2/2d/Thomas_Dunman.jpg",
    "TPAGAR": f"{_C}/c/c0/Politieagenten_voor_het_politiebureau_van_Tanjong_Pagar_in_Singapore_Tanjong_Pagar_police_station_%28titel_op_object%29%2C_RP-F-F01140-AQ.jpg/1280px-Politieagenten_voor_het_politiebureau_van_Tanjong_Pagar_in_Singapore_Tanjong_Pagar_police_station_%28titel_op_object%29%2C_RP-F-F01140-AQ.jpg",
    "GHEEHIN": f"{_U}/2/2d/Membership_certificate_of_the_Ghee_Hin_Kongsi_from_William_Stirling_Collection.jpg",
    "BUTTER": f"{_U}/2/2f/William_J_Butterworth.jpg",
    "TAYLOR": f"{_C}/d/d9/John_Edmund_Taylor%2C_Under_the_Cocoa_Nut_Trees._The_Bungalows._Tanjong_Katong%2C_Singapore._%281879%2C_Wellcome_V0037492%29.jpg/1280px-John_Edmund_Taylor%2C_Under_the_Cocoa_Nut_Trees._The_Bungalows._Tanjong_Katong%2C_Singapore._%281879%2C_Wellcome_V0037492%29.jpg",
    "PLAQUE": f"{_U}/9/9c/OrchardRoadPresbyterianChurch-DunmanPlaque-20091220.jpg",
    "DROAD": f"{_C}/6/6d/Dunman_Road_-_Singapura_%2814_Julai_%2724%29.jpg/1280px-Dunman_Road_-_Singapura_%2814_Julai_%2724%29.jpg",
    "TIMELINE": f"{_A}/dunman-timeline-chart.png",
    # Gallery images:
    "CPS1880": f"{_U}/2/2f/Central_Police_Station_and_Magistrates_Courts_on_South_Bridge_Road%2C_Singapore_c._1880s.jpg",
    "PCOURT": f"{_C}/f/f4/The_Police_Court_Singapore%2C_KITLV_1404912.tiff/lossy-page1-1280px-The_Police_Court_Singapore%2C_KITLV_1404912.tiff.jpg",
    "BACK": f"{_C}/e/e2/Gezicht_op_een_plein_achter_een_gerechtsgebouw_in_Singapore_View_at_back_of_Police_Court._S.pore_%28titel_op_object%29%2C_RP-F-F01197-AH.jpg/1280px-Gezicht_op_een_plein_achter_een_gerechtsgebouw_in_Singapore_View_at_back_of_Police_Court._S.pore_%28titel_op_object%29%2C_RP-F-F01197-AH.jpg",
    "CPS1911": f"{_U}/7/7b/Central_Police_Station_Singapore_1911.jpg",
    "SHOP": f"{_C}/8/83/KITLV_-_29167_-_Shopping_in_Singapore_-_1860.tif/lossy-page1-1280px-KITLV_-_29167_-_Shopping_in_Singapore_-_1860.tif.jpg",
    "GROSSE": f"{_C}/0/07/Singapore_January_20_1866_Frederick_Grosse.jpg/1280px-Singapore_January_20_1866_Frederick_Grosse.jpg",
    "JAIL": f"{_C}/c/c5/Main_gate_of_Singapore_Jail%2C_Bras_Basah_%28McNair_1899%2C_Plate_XI%29.jpg/1280px-Main_gate_of_Singapore_Jail%2C_Bras_Basah_%28McNair_1899%2C_Plate_XI%29.jpg",
    "CAVENAGH": f"{_U}/0/00/Sir_Orfeur_Cavenagh.jpg",
    "SIKH": f"{_U}/b/b0/Sikh_Contingent_member%2C_Straits_Settlements_Police.jpg",
    "KATONG": f"{_C}/d/d4/Tandjong_Katong%2C_Singapore%2C_KITLV_1407451.tiff/lossy-page1-1280px-Tandjong_Katong%2C_Singapore%2C_KITLV_1407451.tiff.jpg",
    "TANGLIN": f"{_C}/f/f1/KITLV_-_79904_-_Kleingrothe%2C_C.J._-_Medan_-_Tanglin_Club_in_Singapore_-_circa_1910.tif/lossy-page1-1280px-KITLV_-_79904_-_Kleingrothe%2C_C.J._-_Medan_-_Tanglin_Club_in_Singapore_-_circa_1910.tif.jpg",
    "HONGLIM": f"{_C}/6/65/Hong_Lim_Park_2%2C_Mar_06.JPG/1280px-Hong_Lim_Park_2%2C_Mar_06.JPG",
    # Not in this post's captions (credited below):
    "FARQ": f"{_U}/f/f9/Portrait_of_William_Farquhar_%28c._1830%29.jpg",
    "THOMSON": f"{_U}/0/03/JohnTurnbullThomson.jpg",
    "TTSH": f"{_U}/c/c3/Tan_Tock_Seng_Hospital_circa_1844-1856.jpg",
}

# Credits for images not captioned in the post or its gallery.
CREDITS = {
    "TIMELINE": "Timeline by Lesser Known Singapore",
    "FARQ": "Unknown artist, public domain, via Wikimedia Commons",
    "THOMSON": "Cyclopedia Company Limited, CC BY-SA 3.0, via Wikimedia Commons",
    "TTSH": "Unknown author, public domain, via Wikimedia Commons",
}

_E = "ease-in-out"
_IN = {"type": "cover", "zoom": [1.0, 1.06, 1.12], "pan": [(0.5, 0.5)] * 3, "ease": _E}
_OUT = {"type": "cover", "zoom": [1.12, 1.06, 1.0], "pan": [(0.5, 0.5)] * 3, "ease": _E}
# Small photographs, portraits and the certificate: letterbox, modest zoom.
_PORT = {"type": "letterbox", "zoom": [1.0, 1.04, 1.08], "pan": [(0.5, 0.5)] * 3, "ease": _E}
_PORT_OUT = {"type": "letterbox", "zoom": [1.08, 1.04, 1.0], "pan": [(0.5, 0.5)] * 3, "ease": _E}
# The timeline: letterbox, frozen.
_GFX = {"type": "letterbox", "zoom": [1, 1, 1], "pan": [(0.5, 0.5)] * 3}

SLIDES = [
    {"img": "HERO", **_IN},            # 0  s0   title
    {"img": "DROAD", **_IN},           # 1  s1   Dunman Road, Dunman High School
    {"img": "DUNMAN", **_PORT},        # 2  s2   1843: the force handed to a merchant's clerk
    {"img": "TIMELINE", **_GFX},       # 3  s3   28 years, retired 1871
    {"img": "FARQ", **_PORT},          # 4  s4   a tiny first force; Farquhar's twelve men (s5)
    {"img": "GROSSE", **_IN},          # 5  s6   the Night Watch Fund, 1821
    {"img": "SHOP", **_IN},            # 6  s7   18 men in 1831; the town outgrew it (s8)
    {"img": "THOMSON", **_PORT},       # 7  s9   Thomson: £60 a year; gang robberies (s10)
    {"img": "PCOURT", **_IN},          # 8  s11  the public meeting, February 1843
    {"img": "DUNMAN", **_PORT_OUT},    # 9  s12  born 1814, Martin Dyce & Co.; the Free Press (s13)
    {"img": "GROSSE", **_OUT},         # 10 s14  an unusual appointment; covenanted officers (s15-16)
    {"img": "THOMSON", **_PORT_OUT},   # 11 s17  only the deputy title, a quarter of the pay
    {"img": "DUNMAN", **_PORT},        # 12 s18  amateur actor, "Mr. Johnson" (s19)
    {"img": "SHOP", **_OUT},           # 13 s20  the stage and the night watch
    {"img": "CPS1880", **_PORT},       # 14 s21  personal methods; never in uniform (s22)
    {"img": "BACK", **_IN},            # 15 s23  out at all hours; no lights on Orchard Road (s24)
    {"img": "GHEEHIN", **_PORT},       # 16 s25  trusted by the secret societies
    {"img": "HERO", **_OUT},           # 17 s26  the first rules, beats and uniform (s27)
    {"img": "TPAGAR", **_PORT},        # 18 s28  the constables' uniforms
    {"img": "TIMELINE", **_GFX},       # 19 s29  night classes; the force in 1848 (s30)
    {"img": "JAIL", **_IN},            # 20 s31  problems beyond him; the gambling houses (s32)
    {"img": "TPAGAR", **_PORT_OUT},    # 21 s33  no common language; low pay (s34)
    {"img": "TTSH", **_PORT},          # 22 s35  the Pauper Hospital; the cockfight birds (s36-37)
    {"img": "GHEEHIN", **_PORT_OUT},   # 23 s38  the secret societies
    {"img": "GROSSE", **_IN},          # 24 s39  the 1846 funeral procession (s40)
    {"img": "SHOP", **_IN},            # 25 s41  the interpreter rescued; troops in the streets (s42)
    {"img": "TIMELINE", **_GFX},       # 26 s43  May 1854: the rice quarrel (s44)
    {"img": "BACK", **_OUT},           # 27 s45  400 or more dead
    {"img": "BUTTER", **_PORT},        # 28 s46  Butterworth pelted, then the troops
    {"img": "PCOURT", **_OUT},         # 29 s47  special constables; the Riot Act
    {"img": "TPAGAR", **_PORT},        # 30 s48  "in good order"
    {"img": "BUTTER", **_PORT_OUT},    # 31 s49  the sword of honour
    {"img": "DUNMAN", **_PORT_OUT},    # 32 s50  Superintendent, 1851; magistrate and tax (s51)
    {"img": "CPS1880", **_PORT_OUT},   # 33 s52  the grand jury; the Police Act of 1856 (s53)
    {"img": "DUNMAN", **_PORT},        # 34 s54  first full-time Commissioner, 1857
    {"img": "GROSSE", **_OUT},         # 35 s55  coastal stations, Marine Police, detectives
    {"img": "CAVENAGH", **_PORT},      # 36 s56  the Muharram ban, 1865
    {"img": "TIMELINE", **_GFX},       # 37 s57  retired 1871
    {"img": "KATONG", **_IN},          # 38 s58  the Tanjong Katong coconut estate (s59)
    {"img": "TAYLOR", **_IN},          # 39 s60  the seaside bungalows
    {"img": "BACK", **_IN},            # 40 s61  Dunman's Green
    {"img": "TANGLIN", **_IN},         # 41 s62  the Presbyterian church; the Tanglin Club
    {"img": "TIMELINE", **_GFX},       # 42 s63  England 1875; Bournemouth 1887 (s64)
    {"img": "HONGLIM", **_IN},         # 43 s65  Hong Lim Green, now Hong Lim Park
    {"img": "SIKH", **_PORT},          # 44 s66  the force kept changing; the 1871 Ordinance (s67)
    {"img": "CPS1911", **_PORT},       # 45 s68  the Chinese Protectorate, 1879 inquiry, 1881
    {"img": "PCOURT", **_IN},          # 46 s69  Buckley in 1902
    {"img": "DROAD", **_OUT},          # 47 s70  Neighbourhood Police Posts, 1983 (s71-72)
    {"img": "FARQ", **_PORT_OUT},      # 48 s73  SPF200: Farquhar's first twelve men
    {"img": "DROAD", **_IN},           # 49 s74  Dunman Road, the food centre; the schools (s75)
    {"img": "PLAQUE", **_PORT},        # 50 s76  the church plaque
    {"img": "HERO", **_OUT},           # 51 s77  why it matters: a safe city
    {"img": "DUNMAN", **_PORT},        # 52 s78  a merchant's clerk who knew the town
    {"img": "TPAGAR", **_PORT_OUT},    # 53 s79  the story of the force he built
]

SCHEDULE = [(0.0, 0), (4.775, 1), (13.5, 2), (30.575, 3), (40.275, 4), (57.175, 5), (65.475, 6), (83.7, 7), (106.05, 8), (118.5, 9), (147.0, 10), (163.675, 11), (177.95, 12), (194.05, 13), (203.175, 14), (212.525, 15), (235.75, 16), (244.8, 17), (258.8, 18), (270.575, 19), (292.6, 20), (307.875, 21), (329.45, 22), (356.1, 23), (364.475, 24), (383.925, 25), (401.35, 26), (418.9, 27), (424.6, 28), (437.925, 29), (453.2, 30), (463.225, 31), (473.175, 32), (490.4, 33), (514.925, 34), (529.125, 35), (540.675, 36), (557.3, 37), (563.975, 38), (577.85, 39), (589.0, 40), (598.3, 41), (609.5, 42), (624.45, 43), (636.75, 44), (652.075, 45), (671.325, 46), (686.65, 47), (714.875, 48), (722.175, 49), (741.875, 50), (750.65, 51), (760.7, 52), (774.45, 53)]
TOTAL_DURATION = 782.7
TIMING_JSON = "audio/thomas-dunman-the-merchants-clerk-who-built-singapores-police.timing.json"

# The avatar presenter, cartoon with motion: corner bubble for the first and last 30 s.
AVATAR = {"ranges": [(0, 30), (-30, None)], "motion": True}
