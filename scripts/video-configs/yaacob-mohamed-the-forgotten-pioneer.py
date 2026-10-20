"""Video config for the Ya'acob Mohamed post.

No freely licensed portrait of Ya'acob exists, so his own sentences show the
places of his story: the Blakang Mati ferry, the Old Parliament House, the
island villages of Pulau Brani and Blakang Mati, Johor Bahru, the Kampong Ubi
community centre, the 1959 election map and seat diagram, a CIA map of the
islands and the life timeline. Named people other than Ya'acob get their own
picture or none: Lee Kuan Yew (s49, not s1), Marcos (s62), Nasser (s67);
Ahmad Jabri, Yong Nyuk Lin, Hasmah and the biographers get no portrait. The
Tanjong Malim college group (s8-9, s53-54) shows former students, not him.
Portraits, the postcard, the maps and the small Plate 12 are letterboxed with a
modest zoom; the timeline, election map and seat diagram are letterboxed and
frozen.
Video-only: a second Old Parliament House view, Lambert's Plate 12 of Pulau
Brani, and the 1959 results map and seat diagram.

51 slides, 746.75s. Narration: Kokoro with the OpenVoice clone.
AVATAR: first and last 30s, cartoon with motion.
"""

_U = "https://upload.wikimedia.org/wikipedia/commons"
_C = f"{_U}/thumb"
_A = "/assets/images"

IMAGES = {
    "FERRY": f"{_C}/f/f8/Blakang_Mati_Ferry_1951.jpg/1280px-Blakang_Mati_Ferry_1951.jpg",
    "SITC": f"{_C}/4/4e/Some_of_the_Brunei_Malay_teachers_%28former_students_of_Sultan_Idris_Training_College%2C_Tanjong_Malim%2C_Perak%2C_from_1932_to_1948%29.jpg/1280px-Some_of_the_Brunei_Malay_teachers_%28former_students_of_Sultan_Idris_Training_College%2C_Tanjong_Malim%2C_Perak%2C_from_1932_to_1948%29.jpg",
    "OPH": f"{_C}/7/7c/Old_Parliament_House%2C_Singapore%2C_Feb_06.JPG/1280px-Old_Parliament_House%2C_Singapore%2C_Feb_06.JPG",
    "WATER": f"{_C}/f/f0/Singapore%3B_a_view_across_part_of_Blakang_Mati_Island._Waterc_Wellcome_V0037528.jpg/1280px-Singapore%3B_a_view_across_part_of_Blakang_Mati_Island._Waterc_Wellcome_V0037528.jpg",
    "BRANI": f"{_C}/5/50/KITLV_-_105809_-_Lambert_%26_Co.%2C_G.R._-_Singapore_-_Malay_village_on_the_island_of_Pulau_Brani_near_Singapore_-_circa_1900.tif/lossy-page1-1280px-KITLV_-_105809_-_Lambert_%26_Co.%2C_G.R._-_Singapore_-_Malay_village_on_the_island_of_Pulau_Brani_near_Singapore_-_circa_1900.tif.jpg",
    "MARCOS": f"{_C}/e/e2/Ferdinand_Marcos%27_official_portrait_during_his_second_term_%281969%29.jpg/1280px-Ferdinand_Marcos%27_official_portrait_during_his_second_term_%281969%29.jpg",
    "UBI": f"{_C}/a/a8/Kampong_Ubi_Community_Centre_%282025%29_-_img_01.jpg/1280px-Kampong_Ubi_Community_Centre_%282025%29_-_img_01.jpg",
    "TIMELINE": f"{_A}/yaacob-timeline-chart.png",
    # Gallery images:
    "NYPL": f"{_C}/0/06/Malay_-_village_Pulo_Brani_Singapore_%28NYPL_Hades-2359734-4044499%29.jpg/1280px-Malay_-_village_Pulo_Brani_Singapore_%28NYPL_Hades-2359734-4044499%29.jpg",
    "JB": f"{_U}/0/04/Johor_Bahru_town_in_the_1920s.jpg",
    "LKY": f"{_U}/1/13/Lee_Kuan_Yew%2C_1965_%28cropped%29.jpg",
    "NASSER": f"{_C}/d/db/Gamal_Abdel_Nasser_Portrait_1962_%283x4_cropped%29.jpg/1280px-Gamal_Abdel_Nasser_Portrait_1962_%283x4_cropped%29.jpg",
    "AZHAR": f"{_U}/f/f1/V.M._Doroshevich-East_and_War-Arab_University_in_Cairo_enhaced.jpg",
    "CIAMAP": f"{_C}/f/f8/Singapore_-_DPLA_-_2c6cbbcc6e4ff6930e06b68da922e07e.jpg/1280px-Singapore_-_DPLA_-_2c6cbbcc6e4ff6930e06b68da922e07e.jpg",
    "BRANI06": f"{_C}/d/d0/Pulau_Brani%2C_Aug_06.JPG/1280px-Pulau_Brani%2C_Aug_06.JPG",
    "BUKOM": f"{_C}/f/f5/Pulau_Bukom_from_Sentosa.JPG/1280px-Pulau_Bukom_from_Sentosa.JPG",
    "SEBAROK": f"{_C}/4/4b/Pulau_Sebarok%2C_Nov_06.jpg/1280px-Pulau_Sebarok%2C_Nov_06.jpg",
    "SEMAKAU": f"{_C}/4/40/Pulau_Semakau%2C_panorama%2C_Nov_06.jpg/1280px-Pulau_Semakau%2C_panorama%2C_Nov_06.jpg",
    # Not in this post's captions (credited below):
    "OPH4": f"{_C}/1/13/Old_Parliament_House_4%2C_Singapore%2C_Jan_06.JPG/1280px-Old_Parliament_House_4%2C_Singapore%2C_Jan_06.JPG",
    "PLATE12": f"{_U}/a/ab/Photographic_Views_of_Singapore_Plate_12_Malay_Village%2C_Pulau_Brani.jpg",
    "MAP1959": f"{_C}/2/29/Map_of_the_results_of_the_1959_Singaporean_general_election.svg/1280px-Map_of_the_results_of_the_1959_Singaporean_general_election.svg.png",
    "ASSEMBLY": f"{_C}/c/c9/Singapore_Legislative_Assembly_1959.svg/1280px-Singapore_Legislative_Assembly_1959.svg.png",
}

# Credits for images not captioned in the post or its gallery.
CREDITS = {
    "TIMELINE": "Timeline by Lesser Known Singapore",
    "OPH4": "User:Sengkang, copyrighted free use, via Wikimedia Commons",
    "PLATE12": "G. R. Lambert & Co., public domain, via Wikimedia Commons",
    "MAP1959": "FelipeRev, CC BY-SA 4.0, via Wikimedia Commons",
    "ASSEMBLY": "FelipeRev, CC BY-SA 4.0, via Wikimedia Commons",
}

_E = "ease-in-out"
_IN = {"type": "cover", "zoom": [1.0, 1.06, 1.12], "pan": [(0.5, 0.5)] * 3, "ease": _E}
_OUT = {"type": "cover", "zoom": [1.12, 1.06, 1.0], "pan": [(0.5, 0.5)] * 3, "ease": _E}
# Portraits, the postcard, the maps and the small Plate 12: letterbox, modest zoom.
_PORT = {"type": "letterbox", "zoom": [1.0, 1.04, 1.08], "pan": [(0.5, 0.5)] * 3, "ease": _E}
_PORT_OUT = {"type": "letterbox", "zoom": [1.08, 1.04, 1.0], "pan": [(0.5, 0.5)] * 3, "ease": _E}
# The timeline, the election map and the seat diagram: letterbox, frozen.
_GFX = {"type": "letterbox", "zoom": [1, 1, 1], "pan": [(0.5, 0.5)] * 3}

SLIDES = [
    {"img": "FERRY", **_IN},          # 0  s0  title
    {"img": "OPH", **_IN},            # 1  s1  Lee Kuan Yew's tribute, 1980 (no portrait under a sentence about Ya'acob)
    {"img": "TIMELINE", **_GFX},      # 2  s2  UMNO to PAP, minister, envoy
    {"img": "BRANI", **_IN},          # 3  s3  the Southern Islands
    {"img": "JB", **_IN},             # 4  s4  born in Kelantan, raised in Johor (s5-7)
    {"img": "SITC", **_IN},           # 5  s8  the Johor teachers' exam; Tanjong Malim (s9)
    {"img": "CIAMAP", **_PORT},       # 6  s10  to Singapore; the Madrasah Khairiyah (s11)
    {"img": "JB", **_OUT},            # 7  s12  the Malay Nationalist Party and API in Johor
    {"img": "TIMELINE", **_GFX},      # 8  s13  UMNO in Singapore, 1949
    {"img": "OPH4", **_IN},           # 9  s14  the PAP founded, 1954; he declines (s15-16)
    {"img": "TIMELINE", **_GFX},      # 10 s17  the switch to the PAP, 1958 (s18)
    {"img": "OPH", **_OUT},           # 11 s19  31 leaders overnight; called traitors (s20)
    {"img": "CIAMAP", **_PORT_OUT},   # 12 s21  chairman of the Bukit Panjang branch
    {"img": "MAP1959", **_GFX},       # 13 s22  Bukit Timah, May 1959 (s23)
    {"img": "ASSEMBLY", **_GFX},      # 14 s24  43 of 51 seats
    {"img": "WATER", **_IN},          # 15 s25  Southern Islands, September 1963
    {"img": "PLATE12", **_PORT},      # 16 s26  Ahmad Jabri's seat; 55.4 per cent (s27)
    {"img": "BRANI", **_OUT},         # 17 s28  the island kampongs
    {"img": "FERRY", **_OUT},         # 18 s29  Blakang Mati's villages; water (s30)
    {"img": "NYPL", **_PORT},         # 19 s31  assemblyman; three primary schools (s32)
    {"img": "WATER", **_OUT},         # 20 s33  the 1964 integrated school
    {"img": "SEBAROK", **_IN},        # 21 s34  the Pulau Sebarok mosque
    {"img": "BRANI06", **_IN},        # 22 s35  Sentosa, the move to Telok Blangah (s36-37)
    {"img": "BUKOM", **_IN},          # 23 s38  cleared for industry
    {"img": "SEMAKAU", **_PORT},      # 24 s39  Pulau Seking demolished, 1993
    {"img": "TIMELINE", **_GFX},      # 25 s40  the merger years; the DSO (s41)
    {"img": "NYPL", **_PORT_OUT},     # 26 s42  Malay leaders branded traitors
    {"img": "OPH", **_IN},            # 27 s43  "have patience"; the riots (s44)
    {"img": "BRANI", **_IN},          # 28 s45  separation; "the rice has turned into porridge" (s46)
    {"img": "OPH4", **_OUT},          # 29 s47  "We Malays have never migrated" (s48)
    {"img": "LKY", **_PORT},          # 30 s49  Lee Kuan Yew's broadcast request
    {"img": "OPH", **_OUT},           # 31 s50  Parliamentary Secretary, Minister of State
    {"img": "UBI", **_IN},            # 32 s51  Kampong Ubi, 1968, 1972, 1976 (s52)
    {"img": "SITC", **_OUT},          # 33 s53  advocate for the Malay community (s54)
    {"img": "TIMELINE", **_GFX},      # 34 s55  "least advanced in Singapore"
    {"img": "CIAMAP", **_PORT},       # 35 s56  Sang Nila Utama Secondary School (s57)
    {"img": "UBI", **_OUT},           # 36 s58  pre-university and English streams (s59)
    {"img": "OPH4", **_IN},           # 37 s60  the end of the pre-university classes
    {"img": "CIAMAP", **_PORT_OUT},   # 38 s61  Bidadari and Sang Nila Utama Road
    {"img": "MARCOS", **_PORT},       # 39 s62  the Philippines; the Order of Sikatuna
    {"img": "TIMELINE", **_GFX},      # 40 s63  India, Egypt
    {"img": "AZHAR", **_PORT},        # 41 s64  Al-Azhar students; resigns 1986 (s65-66)
    {"img": "NASSER", **_PORT},       # 42 s67  Nasser's Order of the United Arab Republic
    {"img": "OPH", **_IN},            # 43 s68  the NUS honorary doctorate
    {"img": "FERRY", **_IN},          # 44 s69  after Parliament; "To compromise is not to give in" (s70-71)
    {"img": "BRANI", **_OUT},         # 45 s72  sepak takraw, silat, the scholarship fund
    {"img": "TIMELINE", **_GFX},      # 46 s73  heart attack, death 1989 (s74)
    {"img": "UBI", **_IN},            # 47 s75  his family; the biography; the Kampong Ubi scholarship (s76)
    {"img": "WATER", **_IN},          # 48 s77  why it matters
    {"img": "OPH", **_OUT},           # 49 s78  merger and separation
    {"img": "BRANI", **_IN},          # 50 s79  the school and the villages gone
]

SCHEDULE = [(0.0, 0), (3.45, 1), (18.05, 2), (31.975, 3), (44.375, 4), (69.475, 5), (85.025, 6), (98.45, 7), (107.225, 8), (121.825, 9), (141.375, 10), (155.325, 11), (170.075, 12), (181.7, 13), (203.575, 14), (213.125, 15), (228.525, 16), (244.775, 17), (251.925, 18), (276.25, 19), (294.55, 20), (313.5, 21), (321.575, 22), (348.25, 23), (358.575, 24), (362.725, 25), (381.575, 26), (388.7, 27), (403.275, 28), (419.8, 29), (432.5, 30), (438.475, 31), (447.925, 32), (476.075, 33), (494.55, 34), (506.775, 35), (527.075, 36), (541.4, 37), (559.525, 38), (570.85, 39), (584.1, 40), (593.7, 41), (612.525, 42), (620.675, 43), (632.025, 44), (655.675, 45), (676.05, 46), (693.725, 47), (713.475, 48), (724.95, 49), (737.175, 50)]
TOTAL_DURATION = 749.625
TIMING_JSON = "audio/yaacob-mohamed-the-forgotten-pioneer.timing.json"

# The avatar presenter, cartoon with motion: corner bubble for the first and last 30 s.
AVATAR = {"ranges": [(0, 30), (-30, None)], "motion": True}
