"""Short config for the orang laut post.

The post's opening, sentences 0-7 (0-69.375s, over the 60s TikTok line):
Raffles' landing and the boat people who fled, who the orang laut were, the
families moved off the southern islands, and what the name means. The
Tropenmuseum photos, the Kampong Bahru photochrom, the postcard and
Jackson's long 1823 view are small or wide, so they are letterboxed; the
Pulau Brani village and the Semakau sea are cropped to fill the frame.
"""

_U = "https://upload.wikimedia.org/wikipedia/commons"
_C = f"{_U}/thumb"

WIDTH, HEIGHT = 1080, 1920

IMAGES = {
    "HERO": f"{_C}/5/50/KITLV_-_105809_-_Lambert_%26_Co.%2C_G.R._-_Singapore_-_Malay_village_on_the_island_of_Pulau_Brani_near_Singapore_-_circa_1900.tif/lossy-page1-1280px-KITLV_-_105809_-_Lambert_%26_Co.%2C_G.R._-_Singapore_-_Malay_village_on_the_island_of_Pulau_Brani_near_Singapore_-_circa_1900.tif.jpg",
    "JACKSON": f"{_C}/8/8a/Singapore_from_the_Sea_June_1823_-_Lt._Phillip_Jackson.jpg/1280px-Singapore_from_the_Sea_June_1823_-_Lt._Phillip_Jackson.jpg",
    "HOUSEBOAT": f"{_U}/8/81/COLLECTIE_TROPENMUSEUM_Woonschuit_van_een_Oerang-Laoet_familie_Ka._Toengkal_TMnr_10010488.jpg",
    "SEMAKAU14": f"{_C}/1/16/Pulau_Semakau_14%2C_Nov_06.JPG/1280px-Pulau_Semakau_14%2C_Nov_06.JPG",
    "SAILING": f"{_U}/a/ab/COLLECTIE_TROPENMUSEUM_Woonschuiten_van_de_Orang-Laoets_langs_de_kusten_van_Djambi_en_Riouw_varende_TMnr_10010489.jpg",
    "KBAHRU": f"{_U}/b/b3/Singapore_Scene_in_Kampong_Bahru_LCCN2017657641.jpg",
    "FISHER": f"{_U}/3/3b/COLLECTIE_TROPENMUSEUM_Een_op_zee_levende_visser_van_Orang-Laoet_afkomst_in_de_delta_van_Retih_en_Inderagiri_in_Riouw_Zuid-Sumatra_TMnr_10005469.jpg",
    "MALAYV": f"{_C}/2/28/KITLV_-_1403184_-_Malay_village_-_1900-1906.tif/lossy-page1-1280px-KITLV_-_1403184_-_Malay_village_-_1900-1906.tif.jpg",
}

# Credits for images not captioned in the post or its gallery.
CREDITS = {
    "JACKSON": "Philip Jackson, public domain, via Wikimedia Commons",
    "SEMAKAU14": "Sengkang, free use, via Wikimedia Commons",
}

_E = "ease-in-out"
_LB = {"type": "letterbox", "zoom": [1.0, 1.03, 1.06], "pan": [(0.5, 0.5)] * 3, "ease": _E}


def _v(zoom, pan):
    return {"type": "cover", "zoom": zoom, "pan": pan, "ease": _E}


SLIDES = [
    {"img": "HERO", **_v([1.0, 1.04, 1.08], [(0.5, 0.55)] * 3)},  # s0  title
    {"img": "JACKSON", **_LB},                                     # s1  Raffles and Farquhar come ashore
    {"img": "HOUSEBOAT", **_LB},                                   # s2  these were orang laut
    {"img": "SEMAKAU14", **_v([1.0, 1.04, 1.08], [(0.5, 0.5)] * 3)}, # s3  moved off the southern islands
    {"img": "SAILING", **_LB},                                     # s4  people of the sea
    {"img": "KBAHRU", **_LB},                                      # s5  boats, or houses over the water
    {"img": "FISHER", **_LB},                                      # s6  the Portuguese called them Çelates
    {"img": "MALAYV", **_LB},                                      # s7  each suku, its own waters
]
SCHEDULE = [(0.0, 0), (4.425, 1), (18.1, 2), (27.15, 3), (39.4, 4), (43.05, 5), (57.475, 6), (62.525, 7)]
TOTAL_DURATION = 69.375
TIMING_JSON = "audio/the-orang-laut-the-sea-people-who-kept-singapores-waters.timing.json"

BURN_CAPTIONS = True
CAPTION_FONT_RATIO = 0.032
CAPTION_MAX_WIDTH_FRAC = 0.86
CAPTION_Y_FRAC = 0.70
