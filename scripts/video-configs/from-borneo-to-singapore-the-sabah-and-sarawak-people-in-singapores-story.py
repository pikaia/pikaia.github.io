"""Video config for the Borneo-to-Singapore post.

From Brooke's 1839 voyage to the Kinabalu earthquake of 2015: the Rajah Brooke
steamer, Kuching in 1844 and 1876, the Borneo Company's buildings, Sandakan,
Jesselton and Kudat, the North Borneo Company officers with the Singapore
commissioners, the portraits of Ong Ewe Hai, Hugh Zehnder, Chee Swee Cheng and
Elizabeth Choy, the Straits Times of 1 October 1935 (with Wee Kheng Chiang's
photo), the Cobbold signing, Malaysia Day in Singapore, kolo mee and Sarawak laksa,
Mount Kinabalu, UOB Plaza, Zehnder Road and the timeline.

Named-person rule: Lim Eng Moh, Ong Tiang Swee, Wee Cho Yaw, Siput Sarawak and her
daughters, and the four Sabahan guides have no free photos, so their sentences
show places only; the Kuching racecourse crowd (s25) and the Kuching boatman
(s68) sit under sentences that name no one. Portraits, the newspaper page, the
food and the tall towers are letterboxed with a modest zoom; the timeline is
letterboxed and frozen.

61 slides, 835.975s. Narration: Kokoro with the OpenVoice clone.
AVATAR: first and last 30s, cartoon with motion.
"""

_U = "https://upload.wikimedia.org/wikipedia/commons"
_C = f"{_U}/thumb"

IMAGES = {
    "HERO": f"{_C}/4/44/SS_Rajah_Brooke_leaving_Kuching_for_Singapore_on_22_July_1896.jpg/1280px-SS_Rajah_Brooke_leaving_Kuching_for_Singapore_on_22_July_1896.jpg",
    "WEDDING": f"{_U}/0/03/Elizabeth_Choy%2C_1941.jpg",
    "ZEHNDER": f"{_U}/b/b7/H.R.S._Zehnder.png",
    "ST1935": "/assets/images/straits-times-1935-10-01-page-12.jpg",
    "KUCHPANO": f"{_U}/4/42/Kuching_Waterfront_Panorama.jpg",
    "KUCH1844": f"{_C}/f/fa/Kuching_1844.jpg/1280px-Kuching_1844.jpg",
    "BROOKE": f"{_U}/7/73/Sir_James_Brooke_%281847%29_by_Francis_Grant.jpg",
    "NORTH": f"{_U}/e/e2/Marianne_North_%281830-1890%29_-_View_of_Kuching_and_River%2C_Sarawak%2C_Borneo_-_MN543_-_Marianne_North_Gallery.jpg",
    "ONG": f"{_U}/a/a7/Ong_Ewe_Hai.png",
    "PUBLIC": f"{_C}/2/2d/Kuching%2C_Sarawak%3B_the_Public_Offices._Photograph._Wellcome_V0037395.jpg/1280px-Kuching%2C_Sarawak%3B_the_Public_Offices._Photograph._Wellcome_V0037395.jpg",
    "BORNEOCO": f"{_C}/d/d4/Kuching%2C_Sarawak%3B_the_Borneo_Company%27s_building._Photograph._Wellcome_V0037398.jpg/1280px-Kuching%2C_Sarawak%3B_the_Borneo_Company%27s_building._Photograph._Wellcome_V0037398.jpg",
    "BORNEOCO50": f"{_C}/3/3a/The_Borneo_Company_Limited_building_between_1950-1959.jpg/1280px-The_Borneo_Company_Limited_building_between_1950-1959.jpg",
    "SANDAKAN": f"{_C}/c/cc/Sandakan-Sabah-Sandakan-about1895.PNG/1280px-Sandakan-Sabah-Sandakan-about1895.PNG",
    "OFFICERS": f"{_U}/b/b1/Officers_of_the_British_North_Borneo_Company_and_the_commisioners_from_Singapore%2C_Sandakan%2C_c._1900%E2%80%931920.jpg",
    "RACECOURSE": f"{_C}/7/74/Kuching%2C_Sarawak%3B_view_of_the_racecourse._Photograph._Wellcome_V0037400EL.jpg/1280px-Kuching%2C_Sarawak%3B_view_of_the_racecourse._Photograph._Wellcome_V0037400EL.jpg",
    "OLDPARL": f"{_C}/7/7c/Old_Parliament_House%2C_Singapore%2C_Feb_06.JPG/1280px-Old_Parliament_House%2C_Singapore%2C_Feb_06.JPG",
    "TIGER": f"{_C}/c/c7/Haw_Par_Villa_Tiger_Balm_Gardens_Singapore_1963_02.jpg/1280px-Haw_Par_Villa_Tiger_Balm_Gardens_Singapore_1963_02.jpg",
    "ZROAD": f"{_C}/3/3e/Zehnder_Road%2C_Haw_Par_Villa_%2814790728261%29.jpg/1280px-Zehnder_Road%2C_Haw_Par_Villa_%2814790728261%29.jpg",
    "CHEE": f"{_U}/2/29/Chee_Swee_Cheng.png",
    "SANDTOWN": f"{_U}/7/73/Sandakan_Town_%28AWM_P03008.001%29.JPG",
    "JESSELTON": f"{_U}/8/81/Jesselton%2C_circa_1911.JPG",
    "PLAZA1": f"{_U}/0/0b/United_Overseas_Bank_Plaza_One.jpg",
    "OLDKUDAT": f"{_U}/3/3a/OldKudat-1.gif",
    "CHANGI1936": f"{_C}/3/31/Changi_Prison_in_1936.jpg/1280px-Changi_Prison_in_1936.jpg",
    "CHOY1953": f"{_U}/7/79/Elizabeth_Choy%2C_1953.png",
    "MFP": f"{_C}/0/01/Former_Malay_Film_Productions_Studio_in_Balestier.jpg/1280px-Former_Malay_Film_Productions_Studio_in_Balestier.jpg",
    "MALDAY": f"{_C}/e/e5/Malaysia_Day_in_Singapore_1963.jpg/1280px-Malaysia_Day_in_Singapore_1963.jpg",
    "COBBOLD": f"{_C}/9/9d/Signing-of-the-Cobbold-Report-of-the-Commission-of-Enquiry-North-Borneo-and-Sarawak.jpg/1280px-Signing-of-the-Cobbold-Report-of-the-Commission-of-Enquiry-North-Borneo-and-Sarawak.jpg",
    "PERAHU": f"{_U}/1/1c/Iconic_Sarawak_%27Perahu_Tambang%27_at_Kuching_Waterfront.jpg",
    "TOWERS": f"{_U}/3/38/UOBnOUB.JPG",
    "KOLO": f"{_U}/3/36/Sarawak_Kolo_Mee.jpg",
    "LAKSA": f"{_U}/9/9c/Sarawak_Laksa_01.jpg",
    "KINA": f"{_C}/2/27/Morning_view_of_Mount_Kinabalu_in_Malaysia%2C_with_its_peak_clearly_visible.jpg/1280px-Morning_view_of_Mount_Kinabalu_in_Malaysia%2C_with_its_peak_clearly_visible.jpg",
    "TIMELINE": "/assets/images/borneo-timeline-chart.png",
}

# Credits for images not captioned in the post or its gallery.
CREDITS = {
    "TIMELINE": "Timeline by Lesser Known Singapore",
    "KUCHPANO": "Jin, CC BY 2.0, via Wikimedia Commons",
    "RACECOURSE": "Wellcome Collection, CC BY 4.0, via Wikimedia Commons",
    "OLDPARL": "Sengkang, copyrighted free use, via Wikimedia Commons",
    "TIGER": "Don Christie, CC BY-SA 4.0, via Wikimedia Commons",
    "SANDTOWN": "Australian War Memorial, public domain, via Wikimedia Commons",
    "PLAZA1": "Merlion444, CC BY-SA 4.0, via Wikimedia Commons",
    "CHANGI1936": "The Straits Times, public domain, via Wikimedia Commons",
    "CHOY1953": "Singapore Press Holdings, public domain, via Wikimedia Commons",
    "MFP": "Jnzl's Photos, CC BY 2.0, via Wikimedia Commons",
    "MALDAY": "Don Christie, CC BY-SA 4.0, via Wikimedia Commons",
    "PERAHU": "Tnunong, CC BY-SA 4.0, via Wikimedia Commons",
    "TOWERS": "Terence Ong, CC BY 2.5, via Wikimedia Commons",
}

_E = "ease-in-out"
_IN = {"type": "cover", "zoom": [1.0, 1.06, 1.12], "pan": [(0.5, 0.5)] * 3, "ease": _E}
_OUT = {"type": "cover", "zoom": [1.12, 1.06, 1.0], "pan": [(0.5, 0.5)] * 3, "ease": _E}
# Portraits, the newspaper page, the food and the towers: letterbox, modest zoom.
_PORT = {"type": "letterbox", "zoom": [1.0, 1.04, 1.08], "pan": [(0.5, 0.5)] * 3, "ease": _E}
_PORT_OUT = {"type": "letterbox", "zoom": [1.08, 1.04, 1.0], "pan": [(0.5, 0.5)] * 3, "ease": _E}
# The Cobbold signing: the faces sit a little below the middle.
_COBBOLD = {"type": "cover", "zoom": [1.0, 1.05, 1.1], "pan": [(0.5, 0.55)] * 3, "ease": _E}
# The timeline: letterbox, frozen.
_GFX = {"type": "letterbox", "zoom": [1, 1, 1], "pan": [(0.5, 0.5)] * 3}

SLIDES = [
    {"img": "HERO", **_IN},            # 0  s0  title
    {"img": "WEDDING", **_PORT},       # 1  s1  Elizabeth Choy, born in Kudat
    {"img": "ZEHNDER", **_PORT},       # 2  s2  Hugh Zehnder, born in Sarawak
    {"img": "ST1935", **_PORT},        # 3  s3  Wee Kheng Chiang (his photo is on the page); not exceptions (s4)
    {"img": "KUCHPANO", **_IN},        # 4  s5  a century and a half of people, money and ships
    {"img": "KUCH1844", **_IN},        # 5  s6  a voyage from Singapore
    {"img": "BROOKE", **_PORT},        # 6  s7  James Brooke sails 1839; Rajah by 1841 (s8)
    {"img": "NORTH", **_IN},           # 7  s9  Kuching, a small river port; sago, pepper, gambier (s10)
    {"img": "HERO", **_OUT},           # 8  s11 the first crossings went Singapore to Borneo
    {"img": "ONG", **_PORT},           # 9  s12 Ong Ewe Hai, born in Singapore; his father died (s13)
    {"img": "KUCH1844", **_OUT},       # 10 s14 to Sarawak with Lim Eng Moh, 1846 (no one shown)
    {"img": "ONG", **_PORT_OUT},       # 11 s15 Ewe Hai and Company, 1872
    {"img": "PUBLIC", **_IN},          # 12 s16 Kapitan Cina; Bonnie Grass (s17)
    {"img": "BORNEOCO", **_IN},        # 13 s18 British capital; the Borneo Company, 1856-57 (s19)
    {"img": "BORNEOCO50", **_IN},      # 14 s20 antimony; gold at Bau (s21)
    {"img": "SANDAKAN", **_IN},        # 15 s22 the North Borneo Company, 1881
    {"img": "OFFICERS", **_PORT},      # 16 s23 its officials and Singapore; Labuan 1907-46 (s24)
    {"img": "RACECOURSE", **_IN},      # 17 s25 the traffic in people ran the other way
    {"img": "NORTH", **_OUT},          # 18 s26 Ong Tiang Swee, born in Kuching 1864 (no photo of him)
    {"img": "HERO", **_IN},            # 19 s27 the Sarawak and Singapore Steamship Company
    {"img": "PUBLIC", **_OUT},         # 20 s28 Kapitan Cina from 1889
    {"img": "ZEHNDER", **_PORT},       # 21 s29 Zehnder born 1879
    {"img": "OLDPARL", **_IN},         # 22 s30 called to the bar, 1910 (the old court house)
    {"img": "ZEHNDER", **_PORT_OUT},   # 23 s31 Eurasian Association; Volunteer Corps, OBE (s32)
    {"img": "OLDPARL", **_OUT},        # 24 s33 Legislative Council; Advisory Council, judge (s34)
    {"img": "TIGER", **_PORT},         # 25 s35 Pasir Panjang Hill, beside Haw Par Villa
    {"img": "ZROAD", **_IN},           # 26 s36 died 1963; money moved both ways (s37)
    {"img": "CHEE", **_PORT},          # 27 s38 Chee Swee Cheng, born in Malacca 1866
    {"img": "SANDTOWN", **_PORT},      # 28 s39 the spirit and opium farm in North Borneo
    {"img": "JESSELTON", **_IN},       # 29 s40 5,000 acres: tapioca, rubber, a sawmill
    {"img": "CHEE", **_PORT_OUT},      # 30 s41 Ho Hong Bank, OCBC; died 1938 (s42)
    {"img": "ST1935", **_PORT},        # 31 s43 the two families meet in Wee Kheng Chiang (s44)
    {"img": "ST1935", **_PORT_OUT},    # 32 s45 the United Chinese Bank, opened 1 October 1935 (s46)
    {"img": "BORNEOCO50", **_OUT},     # 33 s47 Wee kept his home in Kuching (no one shown)
    {"img": "PLAZA1", **_PORT},        # 34 s48 Wee Cho Yaw (no photo of him)
    {"img": "OLDKUDAT", **_IN},        # 35 s49 Elizabeth Choy born in Kudat (no one shown)
    {"img": "SANDAKAN", **_OUT},       # 36 s50 school in Kudat and Sandakan; Singapore 1929
    {"img": "WEDDING", **_PORT},       # 37 s51 married Choy Khun Heng, 1941 (her wedding portrait)
    {"img": "CHANGI1936", **_IN},      # 38 s52 the canteen; smuggling to the internees
    {"img": "WEDDING", **_PORT_OUT},   # 39 s53 held by the Kempeitai for 200 days
    {"img": "CHOY1953", **_PORT},      # 40 s54 OBE, Star of Sarawak
    {"img": "CHOY1953", **_PORT_OUT},  # 41 s55 Legislative Council; her own post (s56)
    {"img": "MFP", **_IN},             # 42 s57 the Malay film industry in Singapore
    {"img": "KUCH1844", **_IN},        # 43 s58 an actress from Kuching; Siput Sarawak (s59, no photo of her)
    {"img": "MFP", **_OUT},            # 44 s60 cabarets, first film 1947; about 50 films (s61)
    {"img": "KUCHPANO", **_OUT},       # 45 s62 her daughters; died 1999 (s63, no one shown)
    {"img": "MALDAY", **_IN},          # 46 s64 two years in one country
    {"img": "COBBOLD", **_COBBOLD},    # 47 s65 Lord Cobbold's commission; the report (s66)
    {"img": "MALDAY", **_OUT},         # 48 s67 the Malaysia Agreement; 16 September 1963
    {"img": "PERAHU", **_IN},          # 49 s68 separation 1965; the border (s70)
    {"img": "TOWERS", **_PORT},        # 50 s71 Sabahans and Sarawakians in Singapore's workforce
    {"img": "KOLO", **_PORT},          # 51 s72 food; kolo mee and Sarawak laksa (s73)
    {"img": "LAKSA", **_PORT},         # 52 s74 the Sarikei stall owner in Bedok
    {"img": "JESSELTON", **_OUT},      # 53 s75 Singaporeans travel the other way; Kinabalu climbs (s76)
    {"img": "KINA", **_IN},            # 54 s77 the earthquake, 5 June 2015; ten Singaporeans (s78)
    {"img": "KINA", **_OUT},           # 55 s79 the four Sabahan guides (no photos); remembrance (s80)
    {"img": "PLAZA1", **_PORT_OUT},    # 56 s81 other traces; UOB's headquarters (s82)
    {"img": "ZROAD", **_OUT},          # 57 s83 Zehnder Road and the Heeren
    {"img": "TIMELINE", **_GFX},       # 58 s84 where it fits in the bigger story
    {"img": "BORNEOCO", **_OUT},       # 59 s85 Singapore's hinterland
    {"img": "HERO", **_OUT},           # 60 s86 Choy, Zehnder, Wee (no one shown); others still come (s87)
]

SCHEDULE = [(0.0, 0), (5.85, 1), (15.625, 2), (21.65, 3), (28.625, 4), (44.5, 5), (48.425, 6), (64.825, 7), (79.075, 8), (85.45, 9), (97.375, 10), (108.375, 11), (120.65, 12), (136.375, 13), (157.525, 14), (173.3, 15), (182.6, 16), (208.85, 17), (212.575, 18), (223.875, 19), (237.6, 20), (247.425, 21), (259.35, 22), (271.15, 23), (291.8, 24), (310.525, 25), (321.5, 26), (327.425, 27), (335.825, 28), (347.3, 29), (361.425, 30), (382.425, 31), (402.75, 32), (420.975, 33), (432.75, 34), (438.175, 35), (444.85, 36), (458.925, 37), (466.8, 38), (478.55, 39), (490.95, 40), (498.775, 41), (515.075, 42), (525.5, 43), (543.9, 44), (568.825, 45), (585.1, 46), (590.45, 47), (625.025, 48), (640.15, 49), (659.775, 50), (672.425, 51), (692.025, 52), (703.75, 53), (715.775, 54), (735.55, 55), (764.225, 56), (776.2, 57), (792.025, 58), (804.8, 59), (819.25, 60)]
TOTAL_DURATION = 835.975
TIMING_JSON = "audio/from-borneo-to-singapore-the-sabah-and-sarawak-people-in-singapores-story.timing.json"

# The avatar presenter, cartoon with motion: corner bubble for the first and last 30 s.
AVATAR = {"ranges": [(0, 30), (-30, None)], "motion": True}
