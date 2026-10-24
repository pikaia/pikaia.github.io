"""Video config for the Chinese Protectorate post.

The 1886 Protectorate building on a postcard, Pickering's portrait and his
1869 photo in Highland dress, the port, piers, streets and coolies of
Singapore around 1890-1900, Shantou coolies landing in Sumatra, the Straits
Times page of 24 August 1887 on the attack, the Protectorate map, and the
1930 building in 2006 and 2025.

Named-person rule: there are no pictures of Chua Ah Siok, the 1873
merchants, Clementi Smith or Pickering's successors, so their sentences
show buildings, the harbour, the newspaper page or the map. Pickering's
sentences show his portrait or the 1869 photo.

The portraits, the small Lambert plates, the album-mounted photos, the
newspaper page and the map are letterboxed.

41 slides, 603.875s. Narration: Kokoro with the OpenVoice clone.
AVATAR: first and last 30s, cartoon with motion.
"""

IMAGES = {
    "HERO": "https://upload.wikimedia.org/wikipedia/commons/thumb/5/53/Chinese_Protectorate%2C_Singapore%2C_KITLV_1404946.tiff/lossy-page1-1280px-Chinese_Protectorate%2C_Singapore%2C_KITLV_1404946.tiff.jpg",
    "PORT90": "https://upload.wikimedia.org/wikipedia/commons/thumb/5/5e/KITLV_-_150813_-_Lambert_%26_Co.%2C_G.R._-_Singapore_-_Port_at_Singapore_-_circa_1890.tif/lossy-page1-1280px-KITLV_-_150813_-_Lambert_%26_Co.%2C_G.R._-_Singapore_-_Port_at_Singapore_-_circa_1890.tif.jpg",
    "PICK": "https://upload.wikimedia.org/wikipedia/commons/thumb/7/71/Portrait_of_Pickering%2C_William_Alexander.jpg/1280px-Portrait_of_Pickering%2C_William_Alexander.jpg",
    "MAP": "/assets/images/chinese-protectorate-map.png",
    "ST87": "/assets/images/straits-times-1887-08-24-page-2.jpg",
    "FC06": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/d5/Family_court_singapore.jpg/1280px-Family_court_singapore.jpg",
    "MOL25": "https://upload.wikimedia.org/wikipedia/commons/thumb/a/a3/Former_Ministry_of_Labour_Building%2C_October_2025.jpg/1280px-Former_Ministry_of_Labour_Building%2C_October_2025.jpg",
    "HIGH": "https://upload.wikimedia.org/wikipedia/commons/thumb/a/ab/British_Library_digitised_image_from_page_299_of_%22Pioneering_in_Formosa%2C_etc%22.jpg/1280px-British_Library_digitised_image_from_page_299_of_%22Pioneering_in_Formosa%2C_etc%22.jpg",
    "COOL": "https://upload.wikimedia.org/wikipedia/commons/1/13/Photographic_Views_of_Singapore_Plate_13_Group_of_Coolies.jpg",
    "COAL": "https://upload.wikimedia.org/wikipedia/commons/thumb/7/73/Woningen_van_de_kolensjouwers_van_de_Tanjong_Pagar_Dock_Co._Ltd._in_Singapore_Coal_coolies_quarters_%28titel_op_object%29%2C_RP-F-F01140-AC.jpg/1280px-Woningen_van_de_kolensjouwers_van_de_Tanjong_Pagar_Dock_Co._Ltd._in_Singapore_Coal_coolies_quarters_%28titel_op_object%29%2C_RP-F-F01140-AC.jpg",
    "PIER": "https://upload.wikimedia.org/wikipedia/commons/thumb/3/38/KITLV_-_402631_-_Pier_in_Singapore_-_circa_1890.tif/lossy-page1-1280px-KITLV_-_402631_-_Pier_in_Singapore_-_circa_1890.tif.jpg",
    "SHANTOU": "https://upload.wikimedia.org/wikipedia/commons/d/db/COLLECTIE_TROPENMUSEUM_Chinese_koelies_uit_Shantou_verlaten_het_schip_%27s_Jacob_in_de_haven_van_Belawan_Sumatra_om_in_de_tabakcultuur_te_gaan_werken_TMnr_10001445.jpg",
    "SHOPS": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/d3/KITLV_-_29179_-_Lambert_%26_Co.%2C_G.R._-_Singapore_-_Small_Chinese_shops_in_Singapore_-_1897.tif/lossy-page1-1280px-KITLV_-_29179_-_Lambert_%26_Co.%2C_G.R._-_Singapore_-_Small_Chinese_shops_in_Singapore_-_1897.tif.jpg",
    "STREET": "https://upload.wikimedia.org/wikipedia/commons/f/fe/Photographic_Views_of_Singapore_Plate_23_Street_Scene.jpg",
    "NBR": "https://upload.wikimedia.org/wikipedia/commons/thumb/8/80/KITLV_-_43317_-_Lambert_%26_Co.%2C_G.R._-_Singapore_-_The_North_Bridge_Road%2C_Singapore_-_circa_1900.tiff/lossy-page1-1280px-KITLV_-_43317_-_Lambert_%26_Co.%2C_G.R._-_Singapore_-_The_North_Bridge_Road%2C_Singapore_-_circa_1900.tiff.jpg",
    "RICK": "https://upload.wikimedia.org/wikipedia/commons/thumb/5/55/KITLV_-_50189_-_Lambert_%26_Co.%2C_G.R._-_Singapore_-_Chinese_rickshaw_at_Singapore_-_circa_1900.tif/lossy-page1-1280px-KITLV_-_50189_-_Lambert_%26_Co.%2C_G.R._-_Singapore_-_Chinese_rickshaw_at_Singapore_-_circa_1900.tif.jpg",
    "FJC06": "https://upload.wikimedia.org/wikipedia/commons/thumb/8/80/Subordinate_Courts%2C_Family_and_Juvenile_Court%2C_Mar_06.JPG/1280px-Subordinate_Courts%2C_Family_and_Juvenile_Court%2C_Mar_06.JPG",
    "FJC25": "https://upload.wikimedia.org/wikipedia/commons/thumb/4/46/Family_Justice_Courts%2C_October_2025.jpg/1280px-Family_Justice_Courts%2C_October_2025.jpg",
    "PST06": "https://upload.wikimedia.org/wikipedia/commons/thumb/2/2d/Pickering_Street%2C_Oct_06.JPG/1280px-Pickering_Street%2C_Oct_06.JPG",
}

# Every image is captioned in the post or its gallery.
CREDITS = {}

# The channel's 2x2 thumbnail grid, 1890s to today: Pickering in his 1898
# book, coolies at a pier around 1900, the 1886 Protectorate building on a
# postcard, and the 1930 building in 2025.
THUMBNAIL = [
    {"img": "PICK", "pan": (0.5, 0.4)},
    {"img": "COOL", "pan": (0.5, 0.5)},
    {"img": "HERO", "pan": (0.5, 0.5)},
    {"img": "MOL25", "pan": (0.5, 0.5)},
]

_E = "ease-in-out"
_IN = {"type": "cover", "zoom": [1.0, 1.06, 1.12], "pan": [(0.5, 0.5)] * 3, "ease": _E}
_OUT = {"type": "cover", "zoom": [1.12, 1.06, 1.0], "pan": [(0.5, 0.5)] * 3, "ease": _E}
# Portraits, small plates, album-mounted photos, the newspaper page and the map: letterbox, modest zoom.
_PORT = {"type": "letterbox", "zoom": [1.0, 1.04, 1.08], "pan": [(0.5, 0.5)] * 3, "ease": _E}
_PORT_OUT = {"type": "letterbox", "zoom": [1.08, 1.04, 1.0], "pan": [(0.5, 0.5)] * 3, "ease": _E}

SLIDES = [
    {"img": "HERO", **_IN},           # 0  s0 title; Chua Ah Siok at the office (building only, s0-1)
    {"img": "PICK", **_PORT},         # 1  s2 Pickering struck (s2-3)
    {"img": "NBR", **_IN},            # 2  s4 a secret society; ten years
    {"img": "PORT90", **_IN},         # 3  s5 Chinese migrants, the 1870s
    {"img": "SHANTOU", **_PORT},      # 4  s6 the credit-ticket system (s6-7)
    {"img": "COAL", **_PORT},         # 5  s8 held in a hold or a depot
    {"img": "COOL", **_PORT},         # 6  s9 open to abuse
    {"img": "PIER", **_IN},           # 7  s10 the 1873 merchants (no people)
    {"img": "SHANTOU", **_PORT_OUT},  # 8  s11 shipped to the Sumatra estates
    {"img": "SHOPS", **_PORT},        # 9  s12 the 1871 petition
    {"img": "HIGH", **_PORT},         # 10 s13 Pickering: Nottinghamshire, Formosa (s13-14)
    {"img": "PICK", **_PORT_OUT},     # 11 s15 interpreter, 1872; five dialects (s15-16)
    {"img": "HIGH", **_PORT_OUT},     # 12 s17 first Protector, 1877
    {"img": "PORT90", **_OUT},        # 13 s18 the 1877 ordinances
    {"img": "MAP", **_PORT},          # 14 s19 North Canal Road; boarding officer (s19-20)
    {"img": "COOL", **_PORT_OUT},     # 15 s21 handbills; licensed brokers (s21-22)
    {"img": "PICK", **_PORT},         # 16 s23 registration, not a ban (s23-24)
    {"img": "STREET", **_PORT},       # 17 s25 disputes brought to the Protectorate
    {"img": "MAP", **_PORT_OUT},      # 18 s26 outgrew its first office
    {"img": "PST06", **_IN},          # 19 s27 Upper Macao Street, now Pickering Street
    {"img": "RICK", **_PORT},         # 20 s28 overwhelmingly men (s28-29)
    {"img": "NBR", **_OUT},           # 21 s30 brothels registered; Hong Kong Po Leung Kuk (s30-31)
    {"img": "SHOPS", **_PORT_OUT},    # 22 s32 the committee; the 1888 ordinance (no people, s32-33)
    {"img": "MAP", **_PORT},          # 23 s34 mui tsai; Kandang Kerbau, York Hill (s34-35)
    {"img": "HERO", **_OUT},          # 24 s36 the League of Nations, 1931
    {"img": "STREET", **_PORT_OUT},   # 25 s37 one of them struck back
    {"img": "ST87", **_PORT},         # 26 s38 Chua Ah Siok; the trial (page only, s38-40)
    {"img": "HIGH", **_PORT},         # 27 s41 never recovered; retired (s41-42)
    {"img": "PIER", **_OUT},          # 28 s43 Clementi Smith's ban (no people)
    {"img": "PICK", **_PORT_OUT},     # 29 s44 died at San Remo, 1907
    {"img": "FJC06", **_IN},          # 30 s45 later heads (no people, s45-46)
    {"img": "FC06", **_IN},           # 31 s47 the 1930 building (s47-48)
    {"img": "MOL25", **_IN},          # 32 s49 the Chinese Secretariat
    {"img": "MAP", **_PORT_OUT},      # 33 s50 the Poh Leung Kuk dissolved
    {"img": "FJC06", **_OUT},         # 34 s51 the courts from 1990
    {"img": "FC06", **_OUT},          # 35 s52 national monument, 1998
    {"img": "FJC25", **_IN},          # 36 s53 Family Justice Courts move, 2024
    {"img": "MOL25", **_OUT},         # 37 s54 present-day echoes; the 2015 Act (s54-55)
    {"img": "COOL", **_PORT},         # 38 s56 settling-in programme
    {"img": "HERO", **_IN},           # 39 s57 where it fits (s57-58)
    {"img": "PST06", **_OUT},         # 40 s59 close
]

SCHEDULE = [
    (0.0, 0), (18.7, 1), (29.025, 2), (42.725, 3), (56.3, 4), (69.725, 5),
    (80.15, 6), (86.925, 7), (105.225, 8), (118.425, 9), (130.025, 10), (149.425, 11),
    (175.25, 12), (189.25, 13), (199.275, 14), (213.55, 15), (233.225, 16), (250.425, 17),
    (262.85, 18), (266.5, 19), (279.5, 20), (297.35, 21), (315.75, 22), (336.125, 23),
    (360.8, 24), (371.575, 25), (380.325, 26), (412.25, 27), (423.625, 28), (437.4, 29),
    (442.775, 30), (453.775, 31), (474.0, 32), (486.675, 33), (498.3, 34), (509.65, 35),
    (516.275, 36), (523.95, 37), (544.3, 38), (565.775, 39), (594.025, 40),
]
TOTAL_DURATION = 603.875
TIMING_JSON = "audio/the-chinese-protectorate-pickering-the-poh-leung-kuk-and-the-coolie-trade.timing.json"

# The avatar presenter, cartoon with motion: corner bubble for the first and last 30 s.
AVATAR = {"ranges": [(0, 30), (-30, None)], "motion": True}
