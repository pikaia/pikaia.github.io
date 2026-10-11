"""Video config for the Munshi Abdullah post.

There is no portrait of Abdullah, so no slide claims to show him: under his
own lines the slides show his book (the 1849 first edition, the 1843
manuscript, his signature), Malacca, Malay manuscripts and the 2019 statue,
the one image that does depict him. Farquhar's two portraits and Raffles's
three take the sentences that name them; a kris (video-only) takes the
attack; Sultan Hussein's seal takes the Sultan; Jackson's 1823 sketch (the
hero, cropped four ways), the 1822 plan, the 1825 survey and the 1830 view
carry the town; the stone's drawings and photos carry the stone; the Bugis
prau carries the slave boats; an Admiralty chart of Jeddah takes his death.
The timeline is letterboxed and frozen.

51 slides, 873.775s. AVATAR: first and last 30s, cartoon with motion.
"""

_U = "https://upload.wikimedia.org/wikipedia/commons"
_C = f"{_U}/thumb"
_A = "/assets/images"

IMAGES = {
    "HERO": f"{_C}/8/8a/Singapore_from_the_Sea_June_1823_-_Lt._Phillip_Jackson.jpg/1280px-Singapore_from_the_Sea_June_1823_-_Lt._Phillip_Jackson.jpg",
    "FARQ": f"{_U}/f/f9/Portrait_of_William_Farquhar_%28c._1830%29.jpg",
    "HIK1849": f"{_U}/a/af/AbdullahbinAbdulKadir-HikayatAbdullah-1849.jpg",
    "PLAN": f"{_U}/6/60/Plan_of_the_Town_of_Singapore_%281822%29_by_Lieutenant_Philip_Jackson.jpg",
    "RAFFLES": f"{_U}/a/a0/George_Francis_Joseph_-_Sir_Thomas_Stamford_Bingley_Raffles.jpg",
    "STONE09": f"{_C}/0/08/SingaporeStone-NationalMuseumofSingapore-20090712.jpg/1280px-SingaporeStone-NationalMuseumofSingapore-20090712.jpg",
    "BUGIS": f"{_U}/3/3b/Bugis-Makassan_prauw_William_Westall_1803.jpg",
    "STATUES": f"{_C}/a/af/Statues_of_Singaporean_Pioneers_at_the_Raffles%27_Landing_Site_-_three-quarter_front_view.jpg/1280px-Statues_of_Singaporean_Pioneers_at_the_Raffles%27_Landing_Site_-_three-quarter_front_view.jpg",
    "TIMELINE": f"{_A}/abdullah-timeline-chart.png",
    # Gallery images:
    "BLAND": f"{_C}/a/a1/1837-SingaporeStone-WBlanddrawing.jpg/1280px-1837-SingaporeStone-WBlanddrawing.jpg",
    "STONE12": f"{_C}/5/59/Singapore_Stone_-_20121019.jpg/1280px-Singapore_Stone_-_20121019.jpg",
    "MAP1825": f"{_C}/9/9f/Part_of_Singapore_Island_%28British_Library_India_Office_Records%2C_1825%2C_detail%29.jpg/1280px-Part_of_Singapore_Island_%28British_Library_India_Office_Records%2C_1825%2C_detail%29.jpg",
    "VIEW1830": f"{_C}/4/41/View_of_Singapore_1830_Sophia_Raffles%27_memoir_of_Stamford_Raffles.jpg/1280px-View_of_Singapore_1830_Sophia_Raffles%27_memoir_of_Stamford_Raffles.jpg",
    "HIK1843": f"{_U}/7/7b/AbdullahbinAbdulKadir-HikayatAbdullah-1843.jpg",
    "SIG": f"{_C}/6/69/Signature_of_Munshi_Abdullah.jpg/1280px-Signature_of_Munshi_Abdullah.jpg",
    "LONSDALE": f"{_U}/a/a6/James_Lonsdale_%281777-1839%29_-_Sir_Thomas_Stamford_Raffles_%281781%E2%80%931826%29_-_ART10000042_-_Zoological_Society_of_London.jpg",
    "FARQK": f"{_C}/8/8c/Schilderij_van_kolonel_William_Farquhar%2C_de_eerste_Britse_resident_van_Singapore_tussen_1819_en_1823%2C_KITLV_16311.tiff/lossy-page1-960px-Schilderij_van_kolonel_William_Farquhar%2C_de_eerste_Britse_resident_van_Singapore_tussen_1819_en_1823%2C_KITLV_16311.tiff.jpg",
    "SEAL": f"{_U}/2/21/The_Seal_of_the_Sultan_Hussein_Shah_of_Johor_and_Singapore.jpg",
    "TAJ": f"{_C}/f/fe/Initial_pages_of_the_Taj_al-Salatin%2C_%E2%80%98The_Crown_of_Kings%E2%80%99%2C_a_Malay_%E2%80%98mirror_for_princes%E2%80%99.jpg/1280px-Initial_pages_of_the_Taj_al-Salatin%2C_%E2%80%98The_Crown_of_Kings%E2%80%99%2C_a_Malay_%E2%80%98mirror_for_princes%E2%80%99.jpg",
    "STADT": f"{_C}/a/af/Malakka_Stadhuis.jpg/1280px-Malakka_Stadhuis.jpg",
    # Not in this post's captions (credited below):
    "KRIS": f"{_C}/0/08/Kris_with_Sheath_MET_DT11927.jpg/1280px-Kris_with_Sheath_MET_DT11927.jpg",
    "MINI": f"{_C}/2/2f/Miniature_portrait_of_Sir_Stamford_Raffles.jpg/1280px-Miniature_portrait_of_Sir_Stamford_Raffles.jpg",
    "WAX": f"{_U}/0/0e/Wax_seals_of_Sir_Stamford_Raffles.jpg",
    "FARQCOLL": f"{_C}/0/0c/Drawings_from_the_William_Farquhar_Collection_of_Natural_History_Drawings%2C_Singapore_History_Gallery%2C_National_Museum_of_Singapore_-_20121019.jpg/1280px-Drawings_from_the_William_Farquhar_Collection_of_Natural_History_Drawings%2C_Singapore_History_Gallery%2C_National_Museum_of_Singapore_-_20121019.jpg",
    "STADT2": f"{_C}/0/07/Malacca_stadhuys1.jpg/1280px-Malacca_stadhuys1.jpg",
    "RIVER": f"{_C}/9/93/Mouth_of_Singapore_River.jpg/1280px-Mouth_of_Singapore_River.jpg",
    "JIDDA": f"{_C}/e/e5/Admiralty_Chart_No_2599_Jidda_with_its_Approaches_Surveyed_by_Commander_W.J.L._Wharton%2C_R.N._and_the_Officers_of_H.M.S._%22Fawn%2C%22_1876%2C_Published_1927.jpg/1280px-Admiralty_Chart_No_2599_Jidda_with_its_Approaches_Surveyed_by_Commander_W.J.L._Wharton%2C_R.N._and_the_Officers_of_H.M.S._%22Fawn%2C%22_1876%2C_Published_1927.jpg",
}

# Credits for images not captioned in the post or its gallery.
CREDITS = {
    "TIMELINE": "Timeline by Lesser Known Singapore, dates from NLB Infopedia and the Hikayat Abdullah",
    "KRIS": "Kris with sheath, 18th to 19th century, The Metropolitan Museum of Art, CC0, via Wikimedia Commons",
    "MINI": "Miniature portrait of Sir Stamford Raffles, about 1817, photographed by Ng.yisheng, CC BY-SA 4.0, via Wikimedia Commons",
    "WAX": "Wax seals of Sir Stamford Raffles, early 19th century, National Museum of Singapore, public domain, via Wikimedia Commons",
    "FARQCOLL": "Drawings from the William Farquhar Collection, National Museum of Singapore, 2012, Bryn Pinzgauer, CC BY 2.0, via Wikimedia Commons",
    "STADT2": "The Stadthuys, Malacca, 2007, Slleong (Wikivoyage), CC BY 1.0, via Wikimedia Commons",
    "RIVER": "The mouth of the Singapore River, 2010, Jukkabrother, CC BY-SA 4.0, via Wikimedia Commons",
    "JIDDA": "Admiralty Chart No. 2599, Jidda with its Approaches, surveyed 1876, United Kingdom Hydrographic Office, public domain, via Wikimedia Commons",
}

_E = "ease-in-out"
_IN = {"type": "cover", "zoom": [1.0, 1.06, 1.12], "pan": [(0.5, 0.5)] * 3, "ease": _E}
_IN2 = {"type": "cover", "zoom": [1.1, 1.16, 1.22], "pan": [(0.3, 0.5), (0.4, 0.5), (0.5, 0.5)], "ease": _E}
_OUT = {"type": "cover", "zoom": [1.12, 1.06, 1.0], "pan": [(0.5, 0.5)] * 3, "ease": _E}
# Portraits, tall photos and small scans: letterbox, modest zoom (no zoom on grainy photos).
_PORT = {"type": "letterbox", "zoom": [1.0, 1.04, 1.08], "pan": [(0.5, 0.5)] * 3, "ease": _E}
_PORT_OUT = {"type": "letterbox", "zoom": [1.08, 1.04, 1.0], "pan": [(0.5, 0.5)] * 3, "ease": _E}
# The timeline and the Jeddah chart: letterbox, frozen.
_GFX = {"type": "letterbox", "zoom": [1, 1, 1], "pan": [(0.5, 0.5)] * 3}


def _c(zoom, pan):
    return {"type": "cover", "zoom": zoom, "pan": pan, "ease": _E}


# Jackson's 1823 sketch: the drawing sits in a band across the paper, so the
# close crops zoom past the blank sky onto the shoreline.
_HERO_SHORE = _c([1.5, 1.6, 1.7], [(0.3, 0.6), (0.35, 0.6), (0.4, 0.6)])
_HERO_TOWN = _c([1.4, 1.55, 1.7], [(0.55, 0.58), (0.6, 0.58), (0.65, 0.58)])
_HERO_SEA = _c([1.3, 1.4, 1.5], [(0.8, 0.6), (0.75, 0.6), (0.7, 0.6)])
# The wide 1830 view: drift across it.
_VIEW_R = _c([1.0, 1.04, 1.08], [(0.2, 0.5), (0.5, 0.5), (0.8, 0.5)])
_VIEW_L = _c([1.0, 1.04, 1.08], [(0.8, 0.5), (0.5, 0.5), (0.2, 0.5)])
_VIEW_R2 = _c([1.1, 1.14, 1.18], [(0.3, 0.55), (0.45, 0.55), (0.6, 0.55)])
# The 1825 survey: a slow pan, and a push in on Rocky Point at the river mouth.
_MAP_PAN = _c([1.1, 1.15, 1.2], [(0.35, 0.5), (0.45, 0.5), (0.55, 0.5)])
_MAP_POINT = _c([1.2, 1.4, 1.6], [(0.55, 0.5), (0.6, 0.52), (0.65, 0.55)])
# The Jeddah chart is tall: crop onto the harbour plan at the top.
_JIDDA = _c([1.0, 1.06, 1.12], [(0.45, 0.12), (0.45, 0.14), (0.45, 0.16)])
# The 2019 statues: keep Abdullah (second from the left) in frame.
_STATUES = _c([1.0, 1.06, 1.12], [(0.35, 0.5), (0.33, 0.5), (0.31, 0.5)])

SLIDES = [
    {"img": "HERO", **_IN},       # 0  s0   title
    {"img": "FARQ", **_PORT},     # 1  s1   March 1823: the teacher meets Farquhar
    {"img": "KRIS", **_PORT},     # 2  s2   a man run amok; Farquhar collapses
    {"img": "HIK1849", **_PORT},  # 3  s4   Abdullah and the Hikayat
    {"img": "BUGIS", **_PORT},    # 4  s5   the debt: traders from Pahang and Palembang
    {"img": "FARQK", **_PORT},    # 5  s8   Farquhar hears the case; the hidden kris
    {"img": "PLAN", **_PORT},     # 6  s10  the evening visit; the peon killed
    {"img": "KRIS", **_PORT_OUT}, # 7  s13  the search, the stick, the stab
    {"img": "FARQ", **_PORT_OUT}, # 8  s17  Andrew's sword; the shallow wound
    {"img": "HERO", **_HERO_SHORE},# 9  s20  uproar; cannon at the Temenggong's compound
    {"img": "RAFFLES", **_PORT},  # 10 s22  Raffles arrives
    {"img": "HIK1843", **_PORT},  # 11 s24  'if Farquhar dies, I shall hang you'
    {"img": "SEAL", **_PORT},     # 12 s26  Sultan Hussein and Malay custom
    {"img": "MAP1825", **_MAP_PAN},# 13 s28  the body in the cage at Tanjong Malang
    {"img": "STADT", **_IN},      # 14 s31  born in Malacca, 1797; his father
    {"img": "TAJ", **_IN},        # 15 s33  teaching the garrison; 'munshi'
    {"img": "LONSDALE", **_PORT}, # 16 s35  Raffles hires him, 1810; Java
    {"img": "STADT2", **_IN},     # 17 s37  the missionaries; to Singapore with Thomsen
    {"img": "SIG", **_PORT},      # 18 s38  Raffles's secretary and interpreter
    {"img": "HERO", **_HERO_TOWN},# 19 s39  a town cut out of forest; the rats and the cat
    {"img": "PLAN", **_PORT_OUT}, # 20 s43  Farquhar's bounty
    {"img": "FARQK", **_PORT_OUT},# 21 s45  five duit; the trench; centipedes
    {"img": "VIEW1830", **_VIEW_R},# 22 s47  the crocodile, Rochor and Bras Basah
    {"img": "MINI", **_PORT},     # 23 s48  Raffles as Abdullah saw him
    {"img": "RAFFLES", **_PORT_OUT},# 24 s51  writing at night
    {"img": "FARQCOLL", **_IN},   # 25 s53  the collectors
    {"img": "TAJ", **_OUT},       # 26 s54  Malacca's manuscripts nearly used up
    {"img": "MAP1825", **_MAP_POINT},# 27 s55  the stone at the point
    {"img": "BLAND", **_PORT},    # 28 s58  Raffles, Thomsen and the moulds
    {"img": "RIVER", **_IN},      # 29 s60  blown up in 1843
    {"img": "STONE09", **_IN},    # 30 s62  fragments; Calcutta; the National Museum
    {"img": "BUGIS", **_PORT_OUT},# 31 s64  the Bugis season; slaves for sale
    {"img": "HERO", **_HERO_SEA}, # 32 s67  rowing out to the boat
    {"img": "WAX", **_PORT},      # 33 s70  Raffles: 'every slave a free man'
    {"img": "LONSDALE", **_PORT_OUT},# 34 s72  Raffles leaves, June 1823
    {"img": "HERO", **_OUT},      # 35 s75  Lady Raffles; the wave from the window
    {"img": "VIEW1830", **_VIEW_L},# 36 s78  Farquhar goes; the fire
    {"img": "TIMELINE", **_GFX},  # 37 s80  writing in 1840-43
    {"img": "HIK1843", **_PORT_OUT},# 38 s81  the 1819 landing, second-hand
    {"img": "STONE12", **_IN},    # 39 s82  blaming Coleman
    {"img": "SEAL", **_PORT_OUT}, # 40 s83  fond of Raffles, critical of the rulers
    {"img": "HIK1849", **_PORT_OUT},# 41 s85  the translations
    {"img": "FARQK", **_PORT},    # 42 s88  checked against the attack on Farquhar
    {"img": "VIEW1830", **_VIEW_R2},# 43 s89  petition-writer, teacher
    {"img": "TAJ", **_IN2},       # 44 s91  North and Keasberry; printing
    {"img": "TIMELINE", **_GFX},  # 45 s92  the Hikayat, 1840-1849; Kelantan
    {"img": "JIDDA", **_JIDDA},   # 46 s94  the pilgrimage; Jeddah, 1854
    {"img": "SIG", **_PORT_OUT},  # 47 s97  father of modern Malay literature
    {"img": "STATUES", **_STATUES},# 48 s99  Munshi Abdullah Avenue; statue; $20 note
    {"img": "STONE09", **_OUT},   # 49 s100 why it matters
    {"img": "HERO", **_OUT},      # 50 s102 read with care
]

SCHEDULE = [(0.0, 0), (4.475, 1), (19.925, 2), (34.6, 3), (49.55, 4), (65.975, 5), (80.575, 6), (104.575, 7), (124.3, 8), (142.125, 9), (157.625, 10), (169.725, 11), (189.7, 12), (207.9, 13), (231.625, 14), (255.75, 15), (268.65, 16), (290.8, 17), (305.425, 18), (311.475, 19), (336.325, 20), (351.15, 21), (373.425, 22), (387.025, 23), (415.525, 24), (436.175, 25), (447.05, 26), (455.2, 27), (478.25, 28), (496.725, 29), (511.275, 30), (528.7, 31), (556.35, 32), (576.325, 33), (596.7, 34), (621.475, 35), (642.525, 36), (659.725, 37), (671.775, 38), (684.8, 39), (694.8, 40), (708.625, 41), (733.0, 42), (740.3, 43), (757.325, 44), (767.9, 45), (788.275, 46), (804.675, 47), (823.975, 48), (841.075, 49), (858.3, 50)]
TOTAL_DURATION = 873.775
TIMING_JSON = "audio/munshi-abdullah-the-scribe-who-watched-singapore-begin.timing.json"

# The avatar presenter, cartoon with motion: corner bubble for the first and last 30 s.
AVATAR = {"ranges": [(0, 30), (-30, None)], "motion": True}
