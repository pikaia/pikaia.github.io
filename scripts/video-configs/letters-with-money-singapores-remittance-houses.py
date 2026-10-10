"""Video config for the remittance-houses post.

The two qiaopi (the hero letter and the envelope from 石叻, Singapore) carry
the letters themselves; the Shanghai street letter-writer takes the
letter-writers. The Straits Times of 16 December 1876 (page 5) is pushed in
on its riot report for the 1876 Post Office riot. Junks, Amoy harbour and a
1900 plan of Swatow take the journey home; Singapore's Chinese streets and
river (1860-1900) take the remittance houses; the letters chart (letterbox,
frozen) takes the growth of the trade. Portraits only under sentences naming
that person: Seah Eu Chin and Governor Jervois. Trotter, the Ongs, Maxwell,
Lim Ah Tye, Harris and Zhang Huimei have no free photos here, so their
sentences show places or the newspaper page.

44 slides, 756.4s. AVATAR: first and last 30s, cartoon with motion.
"""

_U = "https://upload.wikimedia.org/wikipedia/commons"
_C = f"{_U}/thumb"
_A = "/assets/images"

IMAGES = {
    "HERO": f"{_C}/3/32/%E4%BE%A8%E6%89%B91.jpg/1280px-%E4%BE%A8%E6%89%B91.jpg",
    "ENV": f"{_C}/0/02/%E4%BE%A8%E6%89%B92.jpg/1280px-%E4%BE%A8%E6%89%B92.jpg",
    "WRITER": f"{_C}/6/64/A_man_working_as_a_combination_letter-writer_and_fortune-teller_and_a_man_working_as_a_barber_in_the_same_street%2C_Shanghai%2C_Shanghai_Shi%2C_China%2C_ca.1900-1919_%28IMP-YDS-RG008-358-0008-0056%29.jpg/1280px-thumbnail.jpg",
    "ST1876": f"{_A}/straits-times-1876-12-16-page-5.jpg",
    "CHART": f"{_A}/qiaopi-letters-chart.png",
    "MUSEUM": f"{_C}/1/16/Shantou_Qiaopi_Museum.jpg/1280px-Shantou_Qiaopi_Museum.jpg",
    "SEAH": f"{_C}/6/64/Seah_Eu_Chin.jpg/1280px-Seah_Eu_Chin.jpg",
    "JERVOIS": f"{_C}/0/07/Portrait_of_Governor_Jervois%28GN02384%29.jpg/1280px-Portrait_of_Governor_Jervois%28GN02384%29.jpg",
    "SQUALL": f"{_C}/e/e2/John_Edmund_Taylor%2C_Chinese_Junks_in_a_Squall._Singapore._%281879%2C_Wellcome_V0037495%29.jpg/1280px-John_Edmund_Taylor%2C_Chinese_Junks_in_a_Squall._Singapore._%281879%2C_Wellcome_V0037495%29.jpg",
    "JUNK": f"{_C}/6/6a/566._Chinese_Junk_caring_Firewood%2C_Tanjong_Katon%2C_Singapore%2C_KITLV_1404877.tiff/lossy-page1-1280px-566._Chinese_Junk_caring_Firewood%2C_Tanjong_Katon%2C_Singapore%2C_KITLV_1404877.tiff.jpg",
    "AMOY69": f"{_C}/2/2e/Amoy_Harbour_MET_DP165636.jpg/1280px-Amoy_Harbour_MET_DP165636.jpg",
    "AMOY74": f"{_C}/e/e8/Amoy_town_and_harbour_seen_from_Kalangsu_Wellcome_L0034288.jpg/1280px-Amoy_town_and_harbour_seen_from_Kalangsu_Wellcome_L0034288.jpg",
    "AMOYJUNK": f"{_C}/4/49/Amoy_-_D%C5%BEunka_ulazi_u_luku_Amoy_~_1898..jpg/1280px-Amoy_-_D%C5%BEunka_ulazi_u_luku_Amoy_~_1898..jpg",
    "SHANTOU": f"{_U}/d/db/COLLECTIE_TROPENMUSEUM_Chinese_koelies_uit_Shantou_verlaten_het_schip_%27s_Jacob_in_de_haven_van_Belawan_Sumatra_om_in_de_tabakcultuur_te_gaan_werken_TMnr_10001445.jpg",
    "STREET1860": f"{_C}/d/d0/KITLV_-_29169_-_Chinese_street_in_Singapore%2C_completely_decorated_on_the_occasion_of_the_visit_of_Prince_Albert_of_Saxe-Coburg_-_Gotha%2C_husband_of_Queen_Victoria_-_1860.tif/lossy-page1-1280px-thumbnail.tif.jpg",
    "THK1890": f"{_C}/8/81/KITLV_-_103742_-_Lambert_%26_Co._-_Thian_Hock_Keng_Temple_in_Singapore_-_circa_1890.tif/lossy-page1-1280px-KITLV_-_103742_-_Lambert_%26_Co._-_Thian_Hock_Keng_Temple_in_Singapore_-_circa_1890.tif.jpg",
    "VENDOR": f"{_C}/1/10/KITLV_-_103776_-_Chinese_street_vendor_in_Singapore_-_circa_1890.tif/lossy-page1-1280px-KITLV_-_103776_-_Chinese_street_vendor_in_Singapore_-_circa_1890.tif.jpg",
    "NBR1900": f"{_C}/8/80/KITLV_-_43317_-_Lambert_%26_Co.%2C_G.R._-_Singapore_-_The_North_Bridge_Road%2C_Singapore_-_circa_1900.tiff/lossy-page1-1280px-KITLV_-_43317_-_Lambert_%26_Co.%2C_G.R._-_Singapore_-_The_North_Bridge_Road%2C_Singapore_-_circa_1900.tiff.jpg",
    "BOATQ": f"{_U}/3/37/Photographic_Views_of_Singapore_Plate_09_Boat_Quay.jpg",
    "BOATQPC": f"{_U}/b/b6/Singapore_Boat_Quay_ca._1900.jpg",
    "PORT1900": f"{_C}/3/36/KITLV_-_50215_-_Lambert_%26_Co.%2C_G.R._-_Singapore_-_Port_in_Singapore_-_circa_1900.jpg/1280px-KITLV_-_50215_-_Lambert_%26_Co.%2C_G.R._-_Singapore_-_Port_in_Singapore_-_circa_1900.jpg",
    "GPO1900": f"{_U}/5/57/General_Post_Office_Singapore_1900.jpg",
    "LIYUAN": f"{_C}/1/1b/20260606-%E5%88%A9%E6%BA%90%E4%BE%A8%E6%89%B9%E5%B1%80%E6%97%A7%E5%9D%80.jpg/1280px-20260606-%E5%88%A9%E6%BA%90%E4%BE%A8%E6%89%B9%E5%B1%80%E6%97%A7%E5%9D%80.jpg",
    "YONGAN": f"{_C}/f/f4/%E4%B8%AD%E5%B1%B1%E6%B0%B8%E5%AE%89%E4%BE%A8%E6%89%B9%E5%B1%80%E6%97%A7%E5%9D%80.jpg/1280px-%E4%B8%AD%E5%B1%B1%E6%B0%B8%E5%AE%89%E4%BE%A8%E6%89%B9%E5%B1%80%E6%97%A7%E5%9D%80.jpg",
    "PURVIS": f"{_C}/9/94/Purvis_Street%2C_Dec_05.JPG/1280px-Purvis_Street%2C_Dec_05.JPG",
    # Not in this post's captions (credited below):
    "SWATOWMAP": f"{_C}/2/26/Plan_of_the_port_of_Swatow_-_btv1b525087105_%281_of_2%29.jpg/1280px-Plan_of_the_port_of_Swatow_-_btv1b525087105_%281_of_2%29.jpg",
}

# Credits for images not captioned in the post or its gallery.
CREDITS = {
    "CHART": "Chart by Lesser Known Singapore, figures from One Hundred Years of Singapore (1921)",
    "SWATOWMAP": "Plan of the port of Swatow, about 1900, Bibliotheque nationale de France, public domain, via Wikimedia Commons",
}

_E = "ease-in-out"
_IN = {"type": "cover", "zoom": [1.0, 1.06, 1.12], "pan": [(0.5, 0.5)] * 3, "ease": _E}
_OUT = {"type": "cover", "zoom": [1.12, 1.06, 1.0], "pan": [(0.5, 0.5)] * 3, "ease": _E}
# Portraits, tall photos, small scans and the map: letterbox, modest zoom (no zoom on grainy photos).
_PORT = {"type": "letterbox", "zoom": [1.0, 1.04, 1.08], "pan": [(0.5, 0.5)] * 3, "ease": _E}
_PORT_OUT = {"type": "letterbox", "zoom": [1.08, 1.04, 1.0], "pan": [(0.5, 0.5)] * 3, "ease": _E}
# The chart: letterbox, frozen.
_GFX = {"type": "letterbox", "zoom": [1, 1, 1], "pan": [(0.5, 0.5)] * 3}


def _c(zoom, pan):
    return {"type": "cover", "zoom": zoom, "pan": pan, "ease": _E}


# The street letter-writer, pushed in on his table (right of centre).
_WRITER_CLOSE = _c([1.4, 1.5, 1.6], [(0.72, 0.5), (0.74, 0.5), (0.76, 0.5)])
# The hero letter, pushed in on its columns.
_HERO_CLOSE = _c([1.4, 1.5, 1.6], [(0.4, 0.45), (0.45, 0.45), (0.5, 0.45)])

# Whole-page newspaper push-ins (1600x2294 page). Long holds get at least a
# 0.2 zoom change and a pan drift, or they step (Change Alley post, 2026-10-10).
_ST_PAGE = _c([1.0, 1.1, 1.2], [(0.5, 0.0), (0.5, 0.04), (0.5, 0.08)])
_ST_PAGE_OUT = _c([1.2, 1.1, 1.0], [(0.5, 0.1), (0.5, 0.05), (0.5, 0.0)])
_ST_RIOT = _c([2.0, 2.1, 2.2], [(0.44, 0.06), (0.44, 0.08), (0.44, 0.1)])     # "the effects of yesterday's riots"
_ST_MAXWELL = _c([2.2, 2.3, 2.4], [(0.44, 0.12), (0.44, 0.14), (0.44, 0.16)])  # Maxwell beaten at the Market Street police office
_ST_COUNCIL = _c([2.0, 2.1, 2.2], [(0.44, 0.36), (0.44, 0.38), (0.44, 0.4)])  # the arrest of "about twenty towkays"

SLIDES = [
    {"img": "HERO", **_IN},             # 0  s0      title
    {"img": "VENDOR", **_PORT},         # 1  s1      a labourer sending wages home
    {"img": "BOATQPC", **_IN},          # 2  s2      a remittance house near the river
    {"img": "ENV", **_PORT},            # 3  s3      the qiaopi; Singapore the hub
    {"img": "ST1876", **_ST_PAGE},      # 4  s4      the 1876 riot
    {"img": "AMOY69", **_IN},           # 5  s5      from Fujian and Guangdong
    {"img": "SEAH", **_PORT},           # 6  s6      Seah Eu Chin, 1847
    {"img": "SQUALL", **_IN},           # 7  s7      when the junks sailed
    {"img": "JUNK", **_IN},             # 8  s8-9    the courier and his commission
    {"img": "AMOYJUNK", **_IN},         # 9  s10     30,000 to 70,000 dollars a year
    {"img": "AMOY74", **_IN},           # 10 s11     the shuike
    {"img": "WRITER", **_IN},           # 11 s12-14  the letter-writers
    {"img": "WRITER", **_WRITER_CLOSE},  # 12 s15     three to six cents a letter
    {"img": "STREET1860", **_IN},       # 13 s16-17  the first remittance houses
    {"img": "NBR1900", **_IN},          # 14 s18-19  each house served its own people
    {"img": "SWATOWMAP", **_PORT},      # 15 s20-21  branches near the home villages
    {"img": "ENV", **_PORT_OUT},        # 16 s22-23  the clubbed packet and the huipi
    {"img": "PORT1900", **_IN},         # 17 s24-25  round trips; holding the money
    {"img": "BOATQ", **_PORT},          # 18 s26-27  Harris on how the houses made money
    {"img": "GPO1900", **_PORT},        # 19 s28-29  Trotter and the postal monopoly
    {"img": "THK1890", **_IN},          # 20 s30     the Ongs' offer
    {"img": "JERVOIS", **_PORT},        # 21 s31-32  Governor Jervois's sub-post office
    {"img": "STREET1860", **_OUT},      # 22 s33-34  the placards go up around the town
    {"img": "ST1876", **_ST_RIOT},      # 23 s35-36  15 December: the office wrecked
    {"img": "ST1876", **_ST_MAXWELL},   # 24 s37-38  the police station; Maxwell
    {"img": "PORT1900", **_OUT},        # 25 s39-40  arrests; the towkays on the Pluto
    {"img": "ST1876", **_ST_COUNCIL},   # 26 s41-42  the shops close; the towkays return
    {"img": "ST1876", **_ST_PAGE_OUT},  # 27 s43-45  the office reopens; who was behind it
    {"img": "GPO1900", **_PORT_OUT},    # 28 s46-48  into the General Post Office
    {"img": "CHART", **_GFX},           # 29 s49-51  the letters climb; 49 offices in 1887
    {"img": "NBR1900", **_OUT},         # 30 s52-53  houses that failed
    {"img": "SHANTOU", **_PORT},        # 31 s54     about 200 houses, the regional hub
    {"img": "VENDOR", **_PORT_OUT},     # 32 s55     Hokkien and Teochew houses by 1937
    {"img": "AMOY69", **_OUT},          # 33 s56-58  the war cuts the link
    {"img": "BOATQ", **_PORT_OUT},      # 34 s59-61  the golden years
    {"img": "HERO", **_HERO_CLOSE},     # 35 s62-63  exchange control; $45 a month
    {"img": "JUNK", **_OUT},            # 36 s64     licensing from 1948
    {"img": "YONGAN", **_PORT},         # 37 s65-66  after 1949
    {"img": "PURVIS", **_IN},           # 38 s67-69  a changing population; decline
    {"img": "LIYUAN", **_IN},           # 39 s70     the letters survive
    {"img": "MUSEUM", **_PORT},         # 40 s71     UNESCO, 2013
    {"img": "ENV", **_PORT},            # 41 s72-73  the Koh Seow Chuan collection; Dear You
    {"img": "SQUALL", **_OUT},          # 42 s74-75  remittances today
    {"img": "HERO", **_OUT},            # 43 s76     why it matters
]

SCHEDULE = [
    (0.0, 0), (6.1, 1), (15.775, 2), (31.425, 3), (45.3, 4), (54.475, 5), (65.625, 6), (74.9, 7),
    (89.075, 8), (111.4, 9), (125.325, 10), (134.35, 11), (160.0, 12), (167.425, 13), (187.3, 14),
    (206.85, 15), (222.225, 16), (243.375, 17), (253.625, 18), (279.875, 19), (297.95, 20),
    (307.425, 21), (334.5, 22), (356.0, 23), (370.35, 24), (385.65, 25), (403.3, 26), (422.275, 27),
    (446.925, 28), (474.875, 29), (492.8, 30), (509.975, 31), (526.825, 32), (539.2, 33),
    (564.65, 34), (591.125, 35), (607.475, 36), (622.2, 37), (643.3, 38), (666.9, 39), (676.35, 40),
    (691.45, 41), (716.8, 42), (737.65, 43),
]
TOTAL_DURATION = 756.4
TIMING_JSON = "audio/letters-with-money-singapores-remittance-houses.timing.json"

# The avatar presenter, cartoon with motion: corner bubble for the first and last 30 s.
AVATAR = {"ranges": [(0, 30), (-30, None)], "motion": True}
