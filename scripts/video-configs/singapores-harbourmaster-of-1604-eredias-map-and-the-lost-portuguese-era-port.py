"""Video config for the Erédia post.

Erédia's 1604 sketch (the hero) is only 496px wide, so it is always
letterboxed with a modest zoom, never cropped (no zoom on small scans); it
returns under each sentence that reads from it. His self-portrait takes the
sentences that name him; Matelief's and Heemskerck's portraits take theirs.
There is no image of Coutre, Grotius's sentences get the 1609 title page,
and Raffles appears only under the closing line that names him. The shore
the Xabandaria stood on gets today's Kallang Basin and Tanjong Rhu
(video-only); Malacca gets Erédia's plan, Bocarro's fortress, the 1753 view
and the Porta de Santiago; the wars get the 1606 siege prints and an 1892
painting of Matelief's sea battle (video-only); the cargo gets three kraak
dishes (one video-only). The timeline is letterboxed and frozen.

49 slides, 599.925s. AVATAR: first and last 30s, cartoon with motion.
"""

_U = "https://upload.wikimedia.org/wikipedia/commons"
_C = f"{_U}/thumb"
_A = "/assets/images"

IMAGES = {
    "HERO": f"{_U}/f/f6/Map_of_Singapura_by_Godinho_de_Er%C3%A9dia_1604.jpg",
    "MALACA": f"{_U}/2/28/Malaca_%28manuel_godinho_de_eredia_1604%29.jpg",
    "PORTRAIT": f"{_C}/7/77/Manuel_Godinho_de_Er%C3%A9dia_self_portrait.jpg/1280px-Manuel_Godinho_de_Er%C3%A9dia_self_portrait.jpg",
    "MATELIEF": f"{_C}/7/76/Cornelis_Matelieff_de_Jonge_%281570-1632%29%2C_gekozen_in_1602%2C_SK-A-4491.jpg/1280px-Cornelis_Matelieff_de_Jonge_%281570-1632%29%2C_gekozen_in_1602%2C_SK-A-4491.jpg",
    "HEEMS": f"{_C}/4/4e/Portret_van_Jacob_van_Heemskerck%2C_RP-P-OB-48.603.jpg/1280px-Portret_van_Jacob_van_Heemskerck%2C_RP-P-OB-48.603.jpg",
    "KRAAK": f"{_C}/1/15/Kraak_dish._Porcelain_decorated_with_underglaze_blue._From_1591-1613_CE._From_Jingdezhen%2C_China._Victoria_and_Albert_Museum%2C_London%2C_UK.jpg/1280px-Kraak_dish._Porcelain_decorated_with_underglaze_blue._From_1591-1613_CE._From_Jingdezhen%2C_China._Victoria_and_Albert_Museum%2C_London%2C_UK.jpg",
    "LIBERUM": f"{_C}/0/0b/001_-_Mare_Liberum_-_KW_893_G_6_-_frontpage_%28cropped%29.jpg/1280px-001_-_Mare_Liberum_-_KW_893_G_6_-_frontpage_%28cropped%29.jpg",
    "EMPRESS": f"{_C}/4/4a/Empress_Place_Building%2C_Singapore_-_20140723.jpg/1280px-Empress_Place_Building%2C_Singapore_-_20140723.jpg",
    "REGION": f"{_C}/0/02/Exacta_et_Accurata_Delineatio_1595.jpg/1280px-Exacta_et_Accurata_Delineatio_1595.jpg",
    "TIMELINE": f"{_A}/eredia-timeline-chart.png",
    # Gallery images:
    "SIEGE1614": f"{_C}/1/12/AMH-6471-KB_Battle_near_Malacca_waged_by_Cornelis_Matelief%2C_1606.jpg/1280px-AMH-6471-KB_Battle_near_Malacca_waged_by_Cornelis_Matelief%2C_1606.jpg",
    "SIEGE1683": f"{_C}/a/ac/Melaka_onder_leiding_van_Cornelis_Matelief_de_Jonge_belegerd%2C_1606%2C_RP-P-1896-A-19368-399.jpg/1280px-Melaka_onder_leiding_van_Cornelis_Matelief_de_Jonge_belegerd%2C_1606%2C_RP-P-1896-A-19368-399.jpg",
    "BOCARRO": f"{_U}/8/8f/Malacca_1630.jpg",
    "VIEW1753": f"{_C}/a/a7/AMH-8010-KB_View_of_Malacca.jpg/1280px-AMH-8010-KB_View_of_Malacca.jpg",
    "FAMOSA": f"{_C}/7/76/KITLV_-_101099_-_Kleingrothe%2C_C.J._-_Medan_-_Porta_de_Santiago_of_the_destroyed_fortress_A_Famosa_at_Malacca_%28Melaka%29_in_Malaysia_-_circa_1905.tif/lossy-page1-1280px-KITLV_-_101099_-_Kleingrothe%2C_C.J._-_Medan_-_Porta_de_Santiago_of_the_destroyed_fortress_A_Famosa_at_Malacca_%28Melaka%29_in_Malaysia_-_circa_1905.tif.jpg",
    "JONG": f"{_U}/a/a2/Figure_2_Jong_by_Manuel_Godinho_de_Eredia_circa_1613.jpg",
    "CARRACKS": f"{_C}/4/40/Portuguese_Carracks_off_a_Rocky_Coast.jpg/1280px-Portuguese_Carracks_off_a_Rocky_Coast.jpg",
    "KRAAKG": f"{_C}/c/c3/Kraak_porcelain_dish_-_Ming_dynasty_-_Guimet_museum_-_Accesion_number_MA_4801.jpg/1280px-Kraak_porcelain_dish_-_Ming_dynasty_-_Guimet_museum_-_Accesion_number_MA_4801.jpg",
    "JLMUSEUM": f"{_C}/7/70/Kota_Johor_Lama_Museum.JPG/1280px-Kota_Johor_Lama_Museum.JPG",
    "KALLANG": f"{_C}/5/5f/Kallang_Basin_from_Centennial_Tower%2C_2024046%2C_RSKY.jpg/1280px-Kallang_Basin_from_Centennial_Tower%2C_2024046%2C_RSKY.jpg",
    # Not in this post's captions (credited below):
    "SULA": f"{_U}/2/2d/Excerpt_from_the_Sulalatus_Salatin_manuscript%2C_copied_in_the_year_1808%2C_chapter_on_the_Death_of_Hang_Tuah.jpg",
    "DEBRY": f"{_U}/6/66/DeBry_People_of_Malacca.jpg",
    "SEABATTLE": f"{_U}/d/db/Cornelis_Matelief_verslaat_de_Spaans_Portugese_vloot_voor_Malakka%2C_22_oktober_1606.jpg",
    "KRAAK3": f"{_C}/3/37/Kraak_porcelain_plate_with_birds_and_floral_Chinese_motifs.jpg/1280px-Kraak_porcelain_plate_with_birds_and_floral_Chinese_motifs.jpg",
    "TRHU": f"{_U}/1/17/Tanjong_Rhu_Suspension_Bridge.jpg",
    "JOHORLAMA": f"{_C}/1/12/Johor_Lama.JPG/1280px-Johor_Lama.JPG",
    "JACKSON": f"{_C}/8/8a/Singapore_from_the_Sea_June_1823_-_Lt._Phillip_Jackson.jpg/1280px-Singapore_from_the_Sea_June_1823_-_Lt._Phillip_Jackson.jpg",
    "RAFFLES": f"{_U}/a/a0/George_Francis_Joseph_-_Sir_Thomas_Stamford_Bingley_Raffles.jpg",
}

# Credits for images not captioned in the post or its gallery.
CREDITS = {
    "TIMELINE": "Timeline by Lesser Known Singapore",
    "SULA": "Osman bin Kuri bin Amat Utat, the copyist, CC0, via Wikimedia Commons",
    "DEBRY": "Johann Theodor and Johann Israel de Bry, about 1599, public domain, via Wikimedia Commons",
    "SEABATTLE": "W. A. Terwogt, 1892, public domain, via Wikimedia Commons",
    "KRAAK3": "Gniam Jin Hong, CC BY 4.0, via Wikimedia Commons",
    "TRHU": "William Cho, CC BY-SA 2.0, via Wikimedia Commons",
    "JOHORLAMA": "Chongkian, CC BY-SA 4.0, via Wikimedia Commons",
    "JACKSON": "Philip Jackson, public domain, via Wikimedia Commons",
    "RAFFLES": "George Francis Joseph, public domain, via Wikimedia Commons",
}

_E = "ease-in-out"
_IN = {"type": "cover", "zoom": [1.0, 1.06, 1.12], "pan": [(0.5, 0.5)] * 3, "ease": _E}
_IN2 = {"type": "cover", "zoom": [1.1, 1.16, 1.22], "pan": [(0.4, 0.5), (0.5, 0.5), (0.6, 0.5)], "ease": _E}
_OUT = {"type": "cover", "zoom": [1.12, 1.06, 1.0], "pan": [(0.5, 0.5)] * 3, "ease": _E}
# Portraits, maps, pages and small scans (the 496px hero above all): letterbox, modest zoom.
_PORT = {"type": "letterbox", "zoom": [1.0, 1.04, 1.08], "pan": [(0.5, 0.5)] * 3, "ease": _E}
_PORT_OUT = {"type": "letterbox", "zoom": [1.08, 1.04, 1.0], "pan": [(0.5, 0.5)] * 3, "ease": _E}
# The timeline: letterbox, frozen.
_GFX = {"type": "letterbox", "zoom": [1, 1, 1], "pan": [(0.5, 0.5)] * 3}


def _c(zoom, pan):
    return {"type": "cover", "zoom": zoom, "pan": pan, "ease": _E}


# Jackson's 1823 view: the drawing sits in a band across the paper.
_SHORE = _c([1.4, 1.5, 1.6], [(0.3, 0.58), (0.4, 0.58), (0.5, 0.58)])
# The 1540s carracks painting is long and low: drift along it.
_CARRACK_R = _c([1.0, 1.04, 1.08], [(0.3, 0.5), (0.5, 0.5), (0.7, 0.5)])

SLIDES = [
    {"img": "HERO", **_PORT},         # 0  s0   title
    {"img": "PORTRAIT", **_PORT},     # 1  s1   Erédia drew a sketch map in 1604
    {"img": "HERO", **_PORT_OUT},     # 2  s2   the place names; Xabandaria
    {"img": "SULA", **_PORT},         # 3  s3   two hundred years after Singapura
    {"img": "HERO", **_PORT},         # 4  s4   the map's title
    {"img": "MALACA", **_PORT},       # 5  s5   the Description of Malacca
    {"img": "PORTRAIT", **_PORT_OUT}, # 6  s6   the manuscript in Brussels
    {"img": "REGION", **_IN},         # 7  s7   an island in the mouth of the Johor River
    {"img": "HERO", **_PORT},         # 8  s8   the Old and New Straits
    {"img": "TRHU", **_IN},           # 9  s9   Tanah Merah, Bedok, Tanjong Rhu
    {"img": "KALLANG", **_IN},        # 10 s10  its exact spot is uncertain
    {"img": "PORTRAIT", **_PORT},     # 11 s12  born in Malacca, 1563
    {"img": "MALACA", **_PORT_OUT},   # 12 s13  his father and mother
    {"img": "REGION", **_OUT},        # 13 s14  Goa; a career in Portuguese India
    {"img": "CARRACKS", **_CARRACK_R},# 14 s16  the search for Meridional India
    {"img": "HERO", **_PORT_OUT},     # 15 s18  the 1604 squadron
    {"img": "BOCARRO", **_PORT},      # 16 s19  back to Goa; died 1623
    {"img": "DEBRY", **_PORT},        # 17 s21  the word shahbandar
    {"img": "VIEW1753", **_IN},       # 18 s23  the laws of Melaka
    {"img": "JONG", **_PORT},         # 19 s24  the merchants and their ships
    {"img": "FAMOSA", **_IN},         # 20 s25  the Portuguese take Melaka, 1511
    {"img": "JLMUSEUM", **_IN},       # 21 s26  Johor's outposts
    {"img": "KALLANG", **_OUT},       # 22 s27  a shahbandar on the island
    {"img": "MATELIEF", **_PORT},     # 23 s28  Matelief and the shahbandar
    {"img": "SEABATTLE", **_IN},      # 24 s30  the Johor-Dutch alliance
    {"img": "HERO", **_PORT},         # 25 s31  the island of the old shahbandar's quarters
    {"img": "SIEGE1614", **_IN},      # 26 s32  a war zone
    {"img": "JOHORLAMA", **_IN},      # 27 s33  Johor Lama destroyed, 1587
    {"img": "REGION", **_IN2},        # 28 s34  the Dutch arrive
    {"img": "BOCARRO", **_PORT_OUT},  # 29 s35  the blockade of the Johor River
    {"img": "HEEMS", **_PORT},        # 30 s36  Heemskerck takes the Santa Catarina
    {"img": "CARRACKS", **_OUT},      # 31 s37  a 1,500-ton carrack
    {"img": "KRAAK", **_IN},          # 32 s38  silk and porcelain; kraak
    {"img": "KRAAKG", **_IN},         # 33 s39  the Company's capital
    {"img": "LIBERUM", **_PORT},      # 34 s40  Grotius and Mare Liberum
    {"img": "TIMELINE", **_GFX},      # 35 s43  not the only evidence
    {"img": "EMPRESS", **_IN},        # 36 s44  Empress Place, 1998
    {"img": "KRAAK3", **_IN},         # 37 s46  Ming porcelain
    {"img": "EMPRESS", **_OUT},       # 38 s47  the harbourmaster's site
    {"img": "SIEGE1683", **_PORT},    # 39 s48  the port did not survive
    {"img": "REGION", **_OUT},        # 40 s49  Aceh's fleet, 1613
    {"img": "JLMUSEUM", **_OUT},      # 41 s51  Singapura burned
    {"img": "FAMOSA", **_OUT},        # 42 s52  older histories blame the Portuguese
    {"img": "HERO", **_PORT_OUT},     # 43 s54  the name lingered
    {"img": "KALLANG", **_IN2},       # 44 s56  two centuries of near-silence
    {"img": "JACKSON", **_SHORE},     # 45 s57  the Temenggong's village
    {"img": "RAFFLES", **_PORT},      # 46 s58  why it matters
    {"img": "TIMELINE", **_GFX},      # 47 s59  the harbourmaster's job today
    {"img": "HERO", **_PORT},         # 48 s60  two words on a small sketch
]

SCHEDULE = [(0.0, 0), (6.9, 1), (17.125, 2), (32.6, 3), (44.0, 4), (53.725, 5), (62.825, 6), (73.0, 7), (81.275, 8), (91.9, 9), (104.025, 10), (123.85, 11), (129.575, 12), (143.35, 13), (160.8, 14), (176.075, 15), (192.225, 16), (204.9, 17), (215.6, 18), (224.25, 19), (231.225, 20), (242.825, 21), (248.375, 22), (257.375, 23), (273.05, 24), (279.0, 25), (297.575, 26), (303.35, 27), (317.85, 28), (328.025, 29), (337.9, 30), (350.15, 31), (362.925, 32), (379.825, 33), (386.0, 34), (413.975, 35), (419.45, 36), (442.65, 37), (456.3, 38), (472.6, 39), (476.1, 40), (495.875, 41), (504.175, 42), (518.925, 43), (530.55, 44), (541.95, 45), (556.875, 46), (580.45, 47), (593.025, 48)]
TOTAL_DURATION = 599.925
TIMING_JSON = "audio/singapores-harbourmaster-of-1604-eredias-map-and-the-lost-portuguese-era-port.timing.json"

# The avatar presenter, cartoon with motion: corner bubble for the first and last 30 s.
AVATAR = {"ranges": [(0, 30), (-30, None)], "motion": True}
