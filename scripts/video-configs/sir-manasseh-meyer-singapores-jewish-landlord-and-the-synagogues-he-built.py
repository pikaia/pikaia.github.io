"""Video config for the Sir Manasseh Meyer post.

His life from Calcutta to Belle Vue, told through his 1921 portrait, photographs
of Raffles Place, Collyer Quay and North Bridge Road from the 1880s to the 1920s,
the Adelphi Hotel, Crescent Flats and the Sea View Hotel, both synagogues inside
and out, the 1929, 1930 and 1949 Straits Times pages, the two-stage property map,
the timeline, and present-day photos of the Manasseh Meyer Building, Peninsula
Plaza and the school named after him. Meyer appears only as himself (his portrait
and the two pages that carry it); Joshua Raphael Joshua, Thomas Braddell, R. A. J.
Bidwell and his sons are named over places, never over someone else's face, and
Einstein (s37) is shown with his own 1921 portrait.
Portrait-shaped images, the newspaper pages and Peninsula Plaza are letterboxed
with a modest zoom; the maps and timeline are letterboxed and frozen.
Video-only: Chesed-El from 2023, from the side and a column detail, Maghain Aboth
in 2025 and 2011, Raffles Place around 1910 and in a Kelly & Walsh view,
Johnston's Pier, North Bridge Road, Peninsula Plaza and a second Manasseh Meyer
Building view.

47 slides, 683.325s. Narration: Kokoro with the OpenVoice clone.
AVATAR: first and last 30s, cartoon with motion.
"""

IMAGES = {
    "HERO": "https://upload.wikimedia.org/wikipedia/commons/thumb/2/21/Chesed-El_Synagogue%2C_Singapore_-_20060529.jpg/1280px-Chesed-El_Synagogue%2C_Singapore_-_20060529.jpg",
    "MEYER": "https://upload.wikimedia.org/wikipedia/commons/4/4b/Manasseh_Meyer.jpg",
    "RP1890": "https://upload.wikimedia.org/wikipedia/commons/thumb/8/8d/KITLV_-_103753_-_Raffles_Place%2C_Singapore_-_circa_1890.tif/lossy-page1-1280px-KITLV_-_103753_-_Raffles_Place%2C_Singapore_-_circa_1890.tif.jpg",
    "ADELPHI": "https://upload.wikimedia.org/wikipedia/commons/thumb/2/2b/Adelphi_Hotel_Singapore%2C_KITLV_1404749.tiff/lossy-page1-1280px-Adelphi_Hotel_Singapore%2C_KITLV_1404749.tiff.jpg",
    "MAGHAIN": "https://upload.wikimedia.org/wikipedia/commons/thumb/2/27/Maghain_Aboth_Synagogue_-_Singapore_%282023%29_img_01.jpg/1280px-Maghain_Aboth_Synagogue_-_Singapore_%282023%29_img_01.jpg",
    "CHINT": "https://upload.wikimedia.org/wikipedia/commons/thumb/b/be/Interior_of_Chesed-El_Synagogue%2C_Singapore_-_20100815-01.jpg/1280px-Interior_of_Chesed-El_Synagogue%2C_Singapore_-_20100815-01.jpg",
    "MMB": "https://upload.wikimedia.org/wikipedia/commons/thumb/f/f4/Manasseh_Meyer_Building%2C_National_University_of_Singapore_Bukit_Timah_Campus%2C_October_2025.jpg/1280px-Manasseh_Meyer_Building%2C_National_University_of_Singapore_Bukit_Timah_Campus%2C_October_2025.jpg",
    "ST1929": "/assets/images/straits-times-1929-03-01-page-11.jpg",
    "ST1930": "/assets/images/straits-times-1930-07-01-page-13.jpg",
    "ST1949": "/assets/images/straits-times-1949-12-02-page-4.jpg",
    "MAP0": "/assets/images/meyer-map-0.png",
    "MAP1": "/assets/images/meyer-map-1.png",
    "TIMELINE": "/assets/images/meyer-timeline-chart.png",
    "PLAQUE": "https://upload.wikimedia.org/wikipedia/commons/thumb/8/87/Memorial_plaque_to_Menasseh_Meyer%2C_Chesed-El_Synagogue%2C_Singapore_-_20100815.jpg/1280px-Memorial_plaque_to_Menasseh_Meyer%2C_Chesed-El_Synagogue%2C_Singapore_-_20100815.jpg",
    "MAINT": "https://upload.wikimedia.org/wikipedia/commons/2/28/Interior_of_Maghain_Aboth_Synagogue.jpg",
    "RP1885": "https://upload.wikimedia.org/wikipedia/commons/thumb/9/9f/KITLV_-_103746_-_Lambert_%26_Co._-_Raffles_Place_in_Singapore_-_circa_1885.tif/lossy-page1-1280px-KITLV_-_103746_-_Lambert_%26_Co._-_Raffles_Place_in_Singapore_-_circa_1885.tif.jpg",
    "RP1920": "https://upload.wikimedia.org/wikipedia/commons/a/a4/Raffles_Place_c._1920.jpg",
    "COLLYER": "https://upload.wikimedia.org/wikipedia/commons/thumb/5/50/KITLV_-_103744_-_Collyer_Quay_in_Singapore_-_circa_1890.tif/lossy-page1-1280px-KITLV_-_103744_-_Collyer_Quay_in_Singapore_-_circa_1890.tif.jpg",
    "ADELPHI2": "https://upload.wikimedia.org/wikipedia/commons/thumb/7/7d/Adelphi_Hotel_te_Singapore%2C_KITLV_34127.tiff/lossy-page1-1280px-Adelphi_Hotel_te_Singapore%2C_KITLV_34127.tiff.jpg",
    "CRESCENT": "https://upload.wikimedia.org/wikipedia/commons/thumb/8/8d/Crescent_flats_Tanjong_Katon%2C_Singapore%2C_KITLV_1404949.tiff/lossy-page1-1280px-Crescent_flats_Tanjong_Katon%2C_Singapore%2C_KITLV_1404949.tiff.jpg",
    "SEAVIEW": "https://upload.wikimedia.org/wikipedia/commons/thumb/4/4b/Sea_View_Hotel_te_Singapore%2C_KITLV_104797.tiff/lossy-page1-1280px-Sea_View_Hotel_te_Singapore%2C_KITLV_104797.tiff.jpg",
    "EINSTEIN": "https://upload.wikimedia.org/wikipedia/commons/1/11/Albert_Einstein_photo_1921.jpg",
    "SMMIS": "https://upload.wikimedia.org/wikipedia/commons/thumb/4/49/SMMIS_outside.jpg/1280px-SMMIS_outside.jpg",
    "CH2023": "https://upload.wikimedia.org/wikipedia/commons/thumb/b/b9/Chesed-El_Synagogue%2C_2023_%2801%29.jpg/1280px-Chesed-El_Synagogue%2C_2023_%2801%29.jpg",
    "CHSIDE": "https://upload.wikimedia.org/wikipedia/commons/thumb/3/34/Chesed_El_from_the_side_%288119264099%29.jpg/1280px-Chesed_El_from_the_side_%288119264099%29.jpg",
    "CHCOL": "https://upload.wikimedia.org/wikipedia/commons/thumb/c/c3/Chesed-El_Synagogue%2C_Singapore_-_20100815-05.jpg/1280px-Chesed-El_Synagogue%2C_Singapore_-_20100815-05.jpg",
    "MAGH2025": "https://upload.wikimedia.org/wikipedia/commons/thumb/8/8e/Maghain_Aboth_Synagogue%2C_October_2025.jpg/1280px-Maghain_Aboth_Synagogue%2C_October_2025.jpg",
    "MAGHMA": "https://upload.wikimedia.org/wikipedia/commons/thumb/3/31/Synagoga_Magen_Avot.jpg/1280px-Synagoga_Magen_Avot.jpg",
    "RP1910": "https://upload.wikimedia.org/wikipedia/commons/thumb/c/c7/KITLV_-_79892_-_Kleingrothe%2C_C.J._-_Medan_-_Raffles_Place%2C_Singapore_-_circa_1910.tif/lossy-page1-1280px-KITLV_-_79892_-_Kleingrothe%2C_C.J._-_Medan_-_Raffles_Place%2C_Singapore_-_circa_1910.tif.jpg",
    "RPKW": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/d9/KITLV_A887_-_Raffle_%27s_Place_te_Singapore%2C_KITLV_107519.tiff/lossy-page1-1280px-KITLV_A887_-_Raffle_%27s_Place_te_Singapore%2C_KITLV_107519.tiff.jpg",
    "JOHNSTON": "https://upload.wikimedia.org/wikipedia/commons/thumb/3/30/KITLV_-_1404880_-_Singapore._Johnstons_Pier_and_Collyer_Quay_-_1895-1908.tif/lossy-page1-1280px-KITLV_-_1404880_-_Singapore._Johnstons_Pier_and_Collyer_Quay_-_1895-1908.tif.jpg",
    "NBR": "https://upload.wikimedia.org/wikipedia/commons/thumb/8/80/KITLV_-_43317_-_Lambert_%26_Co.%2C_G.R._-_Singapore_-_The_North_Bridge_Road%2C_Singapore_-_circa_1900.tiff/lossy-page1-1280px-KITLV_-_43317_-_Lambert_%26_Co.%2C_G.R._-_Singapore_-_The_North_Bridge_Road%2C_Singapore_-_circa_1900.tiff.jpg",
    "PENINSULA": "https://upload.wikimedia.org/wikipedia/commons/thumb/5/53/Peninsula_Plaza_from_cathedral_grounds_2016.jpg/1280px-Peninsula_Plaza_from_cathedral_grounds_2016.jpg",
    "MMB2": "https://upload.wikimedia.org/wikipedia/commons/thumb/3/3a/Manasseh_Meyer_Building%2C_October_2025.jpg/1280px-Manasseh_Meyer_Building%2C_October_2025.jpg",
}

# Credits for images not captioned in the post or its gallery.
CREDITS = {
    "TIMELINE": "Timeline by Lesser Known Singapore",
    "MAP0": "Map by Lesser Known Singapore; map data © OpenStreetMap contributors",
    "MAP1": "Map by Lesser Known Singapore; map data © OpenStreetMap contributors",
    "CH2023": "Bahnfrend, CC BY-SA 4.0, via Wikimedia Commons",
    "CHSIDE": "Sam Litvin, CC BY 2.0, via Wikimedia Commons",
    "CHCOL": "Smuconlaw, CC BY-SA 3.0, via Wikimedia Commons",
    "MAGH2025": "GoAheadFan95, CC BY-SA 4.0, via Wikimedia Commons",
    "MAGHMA": "Ondrej Zvacek, CC BY 2.5, via Wikimedia Commons",
    "RP1910": "C. J. Kleingrothe, KITLV, public domain, via Wikimedia Commons",
    "RPKW": "Kelly & Walsh, KITLV, public domain, via Wikimedia Commons",
    "JOHNSTON": "Unknown photographer, KITLV, public domain, via Wikimedia Commons",
    "NBR": "G. R. Lambert & Co., KITLV, CC BY-SA 4.0, via Wikimedia Commons",
    "PENINSULA": "Orderinchaos, CC BY-SA 4.0, via Wikimedia Commons",
    "MMB2": "GoAheadFan95, CC BY-SA 4.0, via Wikimedia Commons",
}

_E = "ease-in-out"
_IN = {"type": "cover", "zoom": [1.0, 1.06, 1.12], "pan": [(0.5, 0.5)] * 3, "ease": _E}
_OUT = {"type": "cover", "zoom": [1.12, 1.06, 1.0], "pan": [(0.5, 0.5)] * 3, "ease": _E}
# Portrait-shaped images and the newspaper pages: letterbox, modest zoom.
_PORT = {"type": "letterbox", "zoom": [1.0, 1.04, 1.08], "pan": [(0.5, 0.5)] * 3, "ease": _E}
_PORT_OUT = {"type": "letterbox", "zoom": [1.08, 1.04, 1.0], "pan": [(0.5, 0.5)] * 3, "ease": _E}
# The maps and the timeline: letterbox, frozen.
_GFX = {"type": "letterbox", "zoom": [1, 1, 1], "pan": [(0.5, 0.5)] * 3}

SLIDES = [
    {"img": "HERO", **_IN},               # 0  s0  title
    {"img": "MEYER", **_PORT},            # 1  s1  arrived 1861, died 1930 (names him)
    {"img": "RP1890", **_IN},             # 2  s2  trading firm, property, synagogues
    {"img": "ADELPHI", **_IN},            # 3  s3  hotels, flats and shophouses gone
    {"img": "MEYER", **_PORT_OUT},        # 4  s4  born in Baghdad (names him)
    {"img": "RP1885", **_IN},             # 5  s5  uncle Joshua, Joshua Brothers (no portrait)
    {"img": "NBR", **_IN},                # 6  s6  St Joseph's; back to Calcutta (s7)
    {"img": "JOHNSTON", **_IN},           # 7  s8  Rangoon, six years
    {"img": "COLLYER", **_IN},            # 8  s9  Meyer Brothers, India trade (s10)
    {"img": "RP1910", **_IN},             # 9  s11  opium, a legal trade
    {"img": "TIMELINE", **_GFX},          # 10  s12  buying property from 1885
    {"img": "MAP0", **_GFX},              # 11  s13  Killiney House becomes Belle Vue (s14)
    {"img": "RP1890", **_OUT},            # 12  s15  Raffles Place and Collyer Quay (s16)
    {"img": "ADELPHI2", **_IN},           # 13  s17  the Adelphi Hotel and Meyer Mansions
    {"img": "CRESCENT", **_IN},           # 14  s18  the Sea View Hotel and Crescent Flats
    {"img": "SEAVIEW", **_IN},            # 15  s19  Meyer Road, 1921
    {"img": "RP1920", **_IN},             # 16  s20  the Municipal Commission
    {"img": "RPKW", **_IN},               # 17  s21  the 1911 protest; currency committee (s22)
    {"img": "NBR", **_OUT},               # 18  s23  the first synagogue, Synagogue Street
    {"img": "MAGH2025", **_IN},           # 19  s24  Braddell agrees (no portrait)
    {"img": "MAGHAIN", **_IN},            # 20  s25  Maghain Aboth, 1878; galleries (s26)
    {"img": "MAINT", **_IN},              # 21  s27  crowded; disagreements (s28)
    {"img": "CHSIDE", **_IN},             # 22  s29  a private synagogue at Belle Vue
    {"img": "CH2023", **_IN},             # 23  s30  Chesed-El, designed by Bidwell (no portrait)
    {"img": "CHCOL", **_IN},              # 24  s31  the M for Meyer; his chair (s32)
    {"img": "CHINT", **_IN},              # 25  s33  the minyan; the Hebrew school (s34)
    {"img": "MMB2", **_IN},               # 26  s35  gifts; Raffles College (s36)
    {"img": "EINSTEIN", **_PORT},         # 27  s37  Einstein at Belle Vue, 1922
    {"img": "RP1910", **_OUT},            # 28  s38  the promised concert-hall organ
    {"img": "ST1929", **_PORT},           # 29  s39  Malaya's New Knight, 1929 (s40-41)
    {"img": "ST1930", **_PORT},           # 30  s42  his death, 1930 (s43-44)
    {"img": "PLAQUE", **_PORT},           # 31  s45  the will; sons named (no portraits)
    {"img": "CHSIDE", **_OUT},            # 32  s47  Chesed-El in the Occupation (s48)
    {"img": "MAGHMA", **_IN},             # 33  s49  the community before and after the war (s50)
    {"img": "ST1949", **_PORT},           # 34  s51  the estate wound up; 1947 sale list (s52)
    {"img": "RP1885", **_OUT},            # 35  s53  1949 tender
    {"img": "CRESCENT", **_OUT},          # 36  s54  1950 auction; Crescent Flats withdrawn
    {"img": "MAP1", **_GFX},              # 37  s55  the Belle Vue dispute, 1956 (s56)
    {"img": "CH2023", **_OUT},            # 38  s57  the house no longer stands (s58)
    {"img": "PENINSULA", **_PORT},        # 39  s59  Meyer Mansions -> Peninsula Plaza
    {"img": "MAGHAIN", **_OUT},           # 40  s60  the synagogues survived; monuments (s61)
    {"img": "MAGH2025", **_OUT},          # 41  s62  Jacob Ballas Centre; museum
    {"img": "MMB", **_IN},                # 42  s63  the Manasseh Meyer Building (s64)
    {"img": "SMMIS", **_IN},              # 43  s65  the trust; the school (s66)
    {"img": "TIMELINE", **_GFX},          # 44  s67  the community today
    {"img": "MEYER", **_PORT},            # 45  s68  why it matters (names him)
    {"img": "HERO", **_OUT},              # 46  s69  what lasted
]

SCHEDULE = [(0.0, 0), (5.425, 1), (20.7, 2), (32.95, 3), (41.9, 4), (52.525, 5), (61.35, 6), (77.925, 7), (85.7, 8), (102.325, 9), (116.2, 10), (125.3, 11), (140.725, 12), (154.3, 13), (161.425, 14), (172.275, 15), (182.525, 16), (197.825, 17), (209.55, 18), (219.1, 19), (232.325, 20), (247.6, 21), (264.8, 22), (275.35, 23), (291.125, 24), (306.55, 25), (320.3, 26), (339.625, 27), (356.975, 28), (369.6, 29), (397.3, 30), (416.825, 31), (439.1, 32), (452.175, 33), (471.5, 34), (493.525, 35), (509.425, 36), (525.525, 37), (537.9, 38), (555.025, 39), (572.025, 40), (588.475, 41), (598.75, 42), (620.75, 43), (642.425, 44), (654.85, 45), (666.35, 46)]
TOTAL_DURATION = 683.325
TIMING_JSON = "audio/sir-manasseh-meyer-singapores-jewish-landlord-and-the-synagogues-he-built.timing.json"

# The avatar presenter, cartoon with motion: corner bubble for the first and last 30 s.
AVATAR = {"ranges": [(0, 30), (-30, None)], "motion": True}
