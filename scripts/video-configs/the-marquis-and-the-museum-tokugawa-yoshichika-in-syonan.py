"""Video config for the Marquis post.

From the Raffles Museum and the Botanic Gardens before the war to the Lee
Kong Chian Natural History Museum and Holttum Hall today: the Syonan Times
and Syonan Shimbun pages of 1942-44 (Tanakadate's museum, the Marquis's
appointment, Raffles's statue moved, the scholarships, Koriba's arrival,
the visitor numbers, Koriba's 1944 lecture), the Straits Times page of
1946 on the forestry manual printed under the occupation, three photos of
the Marquis (1913, 1929 and his statue at Komakiyama), and the peerage.

Named-person rule: Tanakadate, Holttum, Corner, Koriba, Desch, Haneda,
Nakata, Mrs Reyes and Archey have no free photographs, so their sentences
show buildings, gardens and newspaper pages only, never people. The
doctors' group in front of Raffles's statue (in the gallery) is passed
over for the statue alone, and the 1943 photo of Allied prisoners on the
Burma railway because the sentence is about the Gardens' Indian and Malay
workers. The Marquis and Ungku Aziz get their own portraits.

Newspaper pages and portraits are letterboxed with a modest zoom.

50 slides, 819.2s. Narration: Kokoro with the OpenVoice clone.
AVATAR: first and last 30s, cartoon with motion.
"""

IMAGES = {
    "HERO": "https://upload.wikimedia.org/wikipedia/commons/thumb/f/f5/KITLV_-_105738_-_Raffles_Museum_in_Singapore_-_circa_1900.tif/lossy-page1-1280px-KITLV_-_105738_-_Raffles_Museum_in_Singapore_-_circa_1900.tif.jpg",
    "SS420905": "/assets/images/syonan-shimbun-1942-09-05-page-4.jpg",
    "GARDLAKE": "https://upload.wikimedia.org/wikipedia/commons/thumb/4/4e/924._Lake%2C_Botanical_Garden_Singapore.%2C_KITLV_1404931.tiff/lossy-page1-1280px-924._Lake%2C_Botanical_Garden_Singapore.%2C_KITLV_1404931.tiff.jpg",
    "GARD1910": "https://upload.wikimedia.org/wikipedia/commons/thumb/b/b3/KITLV_-_79909_-_Kleingrothe%2C_C.J._-_Medan_-_Botanical_Gardens%2C_Singapore_-_circa_1910.tif/lossy-page1-1280px-KITLV_-_79909_-_Kleingrothe%2C_C.J._-_Medan_-_Botanical_Gardens%2C_Singapore_-_circa_1910.tif.jpg",
    "LKC2026": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/d9/Lee_Kong_Chian_Natural_History_Museum_Jul2026_01.jpg/1280px-Lee_Kong_Chian_Natural_History_Museum_Jul2026_01.jpg",
    "MUS1910": "https://upload.wikimedia.org/wikipedia/commons/thumb/7/75/KITLV_-_79901_-_Kleingrothe%2C_C.J._-_Medan_-_Raffles_Museum_in_Singapore_-_circa_1910.tif/lossy-page1-1280px-KITLV_-_79901_-_Kleingrothe%2C_C.J._-_Medan_-_Raffles_Museum_in_Singapore_-_circa_1910.tif.jpg",
    "MUSA1338": "https://upload.wikimedia.org/wikipedia/commons/thumb/9/9f/KITLV_A1338_-_Raffles_Museum_te_Singapore%2C_KITLV_58725.tiff/lossy-page1-1280px-KITLV_A1338_-_Raffles_Museum_te_Singapore%2C_KITLV_58725.tiff.jpg",
    "GARDENT": "https://upload.wikimedia.org/wikipedia/commons/thumb/b/bb/Entrance_to_the_Botanical_Gardens_-_Singapore%2C_KITLV_1404768.tiff/lossy-page1-1280px-Entrance_to_the_Botanical_Gardens_-_Singapore%2C_KITLV_1404768.tiff.jpg",
    "PLATE1": "https://upload.wikimedia.org/wikipedia/commons/thumb/c/c9/Guide_to_the_zoological_collections_of_the_Raffles_Museum%2C_Singapore_%28PLATE_I%29_BHL47142049.jpg/1280px-Guide_to_the_zoological_collections_of_the_Raffles_Museum%2C_Singapore_%28PLATE_I%29_BHL47142049.jpg",
    "SS420627": "/assets/images/syonan-shimbun-1942-06-27-page-4.jpg",
    "PLATE2": "https://upload.wikimedia.org/wikipedia/commons/thumb/9/9a/Guide_to_the_zoological_collections_of_the_Raffles_Museum%2C_Singapore_%28PLATE_II%29_BHL47142032.jpg/1280px-Guide_to_the_zoological_collections_of_the_Raffles_Museum%2C_Singapore_%28PLATE_II%29_BHL47142032.jpg",
    "TOK1913": "https://upload.wikimedia.org/wikipedia/commons/1/13/Yoshichika_Tokugawa_01.jpg",
    "PEERS": "https://upload.wikimedia.org/wikipedia/commons/0/08/Japanese_House_of_Peers.jpg",
    "DIET1905": "https://upload.wikimedia.org/wikipedia/commons/9/94/Japanese_Houses_of_Parliament%2C_1905.jpg",
    "TOK1929": "https://upload.wikimedia.org/wikipedia/commons/1/1f/Tokugawa_Yoshichika_01.jpg",
    "TOKART2005": "https://upload.wikimedia.org/wikipedia/commons/c/c0/Tokugawa_Art_Museum.jpg",
    "MUS1880": "https://upload.wikimedia.org/wikipedia/commons/thumb/4/43/KITLV_-_89911_-_Raffles_Library_and_Museum_in_Singapore_-_before_1880.tif/lossy-page1-1280px-KITLV_-_89911_-_Raffles_Library_and_Museum_in_Singapore_-_before_1880.tif.jpg",
    "SS430126": "/assets/images/syonan-shimbun-1943-01-26-page-1.jpg",
    "GARD1900": "https://upload.wikimedia.org/wikipedia/commons/thumb/c/cf/KITLV_-_50216_-_Botanical_Gardens_in_Singapore_-_circa_1900.tif/lossy-page1-1280px-KITLV_-_50216_-_Botanical_Gardens_in_Singapore_-_circa_1900.tif.jpg",
    "VICREGIA": "https://upload.wikimedia.org/wikipedia/commons/thumb/4/4a/KITLV_-_53177_-_Lambert_%26_Co.%2C_G.R._-_Singapore_-_Victoria_Regia_-_circa_1895.tif/lossy-page1-1280px-KITLV_-_53177_-_Lambert_%26_Co.%2C_G.R._-_Singapore_-_Victoria_Regia_-_circa_1895.tif.jpg",
    "STAT1890": "https://upload.wikimedia.org/wikipedia/commons/thumb/5/56/KITLV_-_377458_-_Statue_of_Sir_Thomas_Stamford_Raffles_in_Singapore_-_circa_1890.tif/lossy-page1-1280px-KITLV_-_377458_-_Statue_of_Sir_Thomas_Stamford_Raffles_in_Singapore_-_circa_1890.tif.jpg",
    "SS420913": "/assets/images/syonan-shimbun-1942-09-13-page-4.jpg",
    "SS421216": "/assets/images/syonan-shimbun-1942-12-16-page-1.jpg",
    "UNGKU": "https://upload.wikimedia.org/wikipedia/commons/c/cf/Ungku_Abdul_Aziz.jpg",
    "ST460828": "/assets/images/straits-times-1946-08-28-page-3.jpg",
    "CHANGI": "https://upload.wikimedia.org/wikipedia/commons/thumb/3/31/Changi_Prison_in_1936.jpg/1280px-Changi_Prison_in_1936.jpg",
    "SS430125": "/assets/images/syonan-shimbun-1943-01-25-page-2.jpg",
    "ADIANT": "https://upload.wikimedia.org/wikipedia/commons/thumb/6/6a/Adiantums_Plant_House_Singapore_%2C_mogelijk_in_de_botanische_tuin%2C_KITLV_1404770.tiff/lossy-page1-1280px-Adiantums_Plant_House_Singapore_%2C_mogelijk_in_de_botanische_tuin%2C_KITLV_1404770.tiff.jpg",
    "SS440826": "/assets/images/syonan-shimbun-1944-08-26-page-2.jpg",
    "TOKYO1945": "https://upload.wikimedia.org/wikipedia/commons/2/20/Tokyo_kushu_1945-4.jpg",
    "BURKILL": "https://upload.wikimedia.org/wikipedia/commons/thumb/2/21/Burkill_Hall_in_Singapore_Botanic_Gardens.jpg/1280px-Burkill_Hall_in_Singapore_Botanic_Gardens.jpg",
    "TOKSTATUE": "https://upload.wikimedia.org/wikipedia/commons/5/5a/Tokugawa_Yoshichika.JPG",
    "NMS": "https://upload.wikimedia.org/wikipedia/commons/thumb/1/10/National_Museum_of_Singapore_-_Joy_of_Museums_-_External.jpg/1280px-National_Museum_of_Singapore_-_Joy_of_Museums_-_External.jpg",
    "LKC2015": "https://upload.wikimedia.org/wikipedia/commons/thumb/f/f0/Lee_Kong_Chian_Natural_History_Museum%2C_National_University_of_Singapore_-_20150808-01.jpg/1280px-Lee_Kong_Chian_Natural_History_Museum%2C_National_University_of_Singapore_-_20150808-01.jpg",
    "HOLTTUMHALL": "https://upload.wikimedia.org/wikipedia/commons/thumb/f/ff/Singapore_Botanic_Gardens_Heritage_Museum.jpg/1280px-Singapore_Botanic_Gardens_Heritage_Museum.jpg",
    "TOKART2023": "https://upload.wikimedia.org/wikipedia/commons/thumb/5/5f/Tokugawa_Art_Museum_Original_Hall%2C_Tokugawa-cho_Higashi_Ward_Nagoya_City_2023.jpg/1280px-Tokugawa_Art_Museum_Original_Hall%2C_Tokugawa-cho_Higashi_Ward_Nagoya_City_2023.jpg",
}

_NSG = "The Syonan Shimbun, via NewspaperSG, National Library Board Singapore, public domain"

# Credits for images not captioned in the post or its gallery.
CREDITS = {
    "GARDLAKE": "Unknown author, CC BY 4.0, via Wikimedia Commons",
    "GARD1910": "C. J. Kleingrothe, public domain, via Wikimedia Commons",
    "MUSA1338": "Unknown author, CC BY 4.0, via Wikimedia Commons",
    "PLATE1": "R. Hanitsch, Raffles Museum, public domain, via Wikimedia Commons",
    "PEERS": "Unknown author, public domain, via Wikimedia Commons",
    "DIET1905": "Unknown author, public domain, via Wikimedia Commons",
    "TOKART2005": "Gnsin, CC BY-SA 3.0, via Wikimedia Commons",
    "MUS1880": "Unknown author, public domain, via Wikimedia Commons",
    "GARD1900": "Unknown author, public domain, via Wikimedia Commons",
    "VICREGIA": "G. R. Lambert & Co., public domain, via Wikimedia Commons",
    "STAT1890": "Unknown author, public domain, via Wikimedia Commons",
    "UNGKU": "Victor Pogadaev, CC BY-SA 4.0, via Wikimedia Commons",
    "CHANGI": "The Straits Times, public domain, via Wikimedia Commons",
    "ADIANT": "G. R. Lambert & Co., CC BY 4.0, via Wikimedia Commons",
    "TOKYO1945": "Ishikawa Kōyō, public domain, via Wikimedia Commons",
    "BURKILL": "alantankenghoe, CC BY 2.0, via Wikimedia Commons",
    "NMS": "GordonMakryllos, CC BY-SA 4.0, via Wikimedia Commons",
    "LKC2015": "Jacklee, CC BY-SA 4.0, via Wikimedia Commons",
}

# The channel's 2x2 thumbnail grid, 1900 to today: the Raffles Museum around
# 1900, the Marquis in 1929, the 5 September 1942 report of his appointment
# (zoomed to its headline), and the Lee Kong Chian museum in 2026.
THUMBNAIL = [
    {"img": "HERO", "pan": (0.5, 0.5)},
    {"img": "TOK1929", "pan": (0.6, 0.1)},
    {"img": "SS420905", "zoom": 3.2, "pan": (0.62, 0.69)},
    {"img": "LKC2026", "pan": (0.5, 0.5)},
]

_E = "ease-in-out"
_IN = {"type": "cover", "zoom": [1.0, 1.06, 1.12], "pan": [(0.5, 0.5)] * 3, "ease": _E}
_OUT = {"type": "cover", "zoom": [1.12, 1.06, 1.0], "pan": [(0.5, 0.5)] * 3, "ease": _E}
# Newspaper pages, portraits and small photos: letterbox, modest zoom.
_PORT = {"type": "letterbox", "zoom": [1.0, 1.04, 1.08], "pan": [(0.5, 0.5)] * 3, "ease": _E}
_PORT_OUT = {"type": "letterbox", "zoom": [1.08, 1.04, 1.0], "pan": [(0.5, 0.5)] * 3, "ease": _E}

SLIDES = [
    {"img": "HERO", **_IN},               # 0  s0  title
    {"img": "SS420905", **_PORT},         # 1  s1  the 5 Sep 1942 report (s1-3)
    {"img": "GARDLAKE", **_IN},           # 2  s4  a nobleman who once hunted tigers
    {"img": "GARD1910", **_IN},           # 3  s5  Holttum and Corner (no faces)
    {"img": "LKC2026", **_IN},            # 4  s6  their descendants today
    {"img": "MUS1910", **_IN},            # 5  s7  the surrender
    {"img": "MUSA1338", **_IN},           # 6  s8  Tanakadate and the notices (s8-9)
    {"img": "GARDENT", **_IN},            # 7  s10 the Gardens' 1947 report (s10-11)
    {"img": "PLATE1", **_IN},             # 8  s12 one department, head office at the museum
    {"img": "SS420627", **_PORT},         # 9  s13 the June 1942 report
    {"img": "PLATE2", **_PORT},           # 10 s14 the elephant's bath
    {"img": "TOK1913", **_PORT},          # 11 s15 a marquis in 1942
    {"img": "PEERS", **_PORT},            # 12 s16 the kazoku (s16-17)
    {"img": "DIET1905", **_IN},           # 13 s18 abolished 1947
    {"img": "TOK1913", **_PORT_OUT},      # 14 s19 born 1886, Owari, biology (s19-21)
    {"img": "TOK1929", **_PORT},          # 15 s22 Malaya and the tiger hunt (s22-24)
    {"img": "TOKART2005", **_IN},         # 16 s25 Malay; the art museum (s25-26)
    {"img": "DIET1905", **_OUT},          # 17 s27 the March Incident
    {"img": "MUS1880", **_IN},            # 18 s28 reached Syonan, 5 March 1942
    {"img": "SS420905", **_PORT_OUT},     # 19 s29 greatly enlarged; Honorary President (s29-30)
    {"img": "SS430126", **_PORT},         # 20 s31 Koriba arrives
    {"img": "GARD1900", **_PORT},         # 21 s32 not interned; the monkey bite; permission (s32-34)
    {"img": "VICREGIA", **_IN},           # 22 s35 fungi, ferns, orchids (s35-36)
    {"img": "STAT1890", **_PORT},         # 23 s37 the libraries; Raffles's statue
    {"img": "SS420913", **_PORT},         # 24 s38 "a mark of respect" (s38-39)
    {"img": "SS421216", **_PORT},         # 25 s40 the five scholarships
    {"img": "UNGKU", **_PORT},            # 26 s41 Ungku Aziz
    {"img": "ST460828", **_PORT},         # 27 s42 the 1946 find (s42-43)
    {"img": "CHANGI", **_PORT},           # 28 s44 Desch released from Changi
    {"img": "ST460828", **_PORT_OUT},     # 29 s45 the printing costs
    {"img": "MUSA1338", **_OUT},          # 30 s46 proofs into the camp; published 1943 (s46-47)
    {"img": "SS430125", **_PORT},         # 31 s48 600 a day; "do away with English" (s48-50)
    {"img": "PLATE2", **_PORT_OUT},       # 32 s51 books stolen from the library
    {"img": "ADIANT", **_IN},             # 33 s52 the railway (s52-53)
    {"img": "GARDENT", **_OUT},           # 34 s54 Tyersall; prices (s54-55)
    {"img": "GARD1910", **_OUT},          # 35 s56 Corner called a collaborator (s56-57)
    {"img": "ADIANT", **_OUT},            # 36 s58 the two men's own account
    {"img": "SS440826", **_PORT},         # 37 s59 August 1944; "I love Malaya" (s59-60)
    {"img": "TOKYO1945", **_IN},          # 38 s61 Tanakadate's books lost in an air raid
    {"img": "CHANGI", **_PORT_OUT},       # 39 s62 Koriba declines release (s62-63)
    {"img": "BURKILL", **_PORT},          # 40 s64 herbarium intact; Holttum returns (s64-65)
    {"img": "TOKSTATUE", **_PORT},        # 41 s66 the Marquis after the war (s66-68)
    {"img": "PLATE1", **_OUT},            # 42 s69 Corner's book; the 1982 review (s69-70)
    {"img": "NMS", **_IN},                # 43 s71 the National Museum
    {"img": "LKC2015", **_IN},            # 44 s72 the natural history collections
    {"img": "LKC2026", **_OUT},           # 45 s73 the Lee Kong Chian museum
    {"img": "HOLTTUMHALL", **_IN},        # 46 s74 UNESCO; Holttum Hall (s74-75)
    {"img": "TOKART2023", **_IN},         # 47 s76 the Tokugawa Art Museum
    {"img": "VICREGIA", **_OUT},          # 48 s77 where it fits
    {"img": "HERO", **_OUT},              # 49 s78 close (s78-79)
]

SCHEDULE = [
    (0.0, 0), (7.975, 1), (36.85, 2), (47.475, 3), (55.175, 4), (62.325, 5),
    (67.425, 6), (94.8, 7), (117.55, 8), (127.125, 9), (146.7, 10), (154.45, 11),
    (162.325, 12), (188.1, 13), (195.05, 14), (229.475, 15), (256.45, 16), (270.55, 17),
    (281.825, 18), (293.975, 19), (324.2, 20), (334.75, 21), (359.6, 22), (372.9, 23),
    (391.45, 24), (399.075, 25), (411.725, 26), (420.175, 27), (442.375, 28), (457.975, 29),
    (468.525, 30), (485.6, 31), (512.2, 32), (527.025, 33), (547.7, 34), (566.375, 35),
    (580.025, 36), (603.075, 37), (616.975, 38), (628.925, 39), (645.275, 40), (671.4, 41),
    (694.725, 42), (711.675, 43), (718.85, 44), (732.825, 45), (752.675, 46), (773.575, 47),
    (780.725, 48), (794.85, 49),
]
TOTAL_DURATION = 819.2
TIMING_JSON = "audio/the-marquis-and-the-museum-tokugawa-yoshichika-in-syonan.timing.json"

# The avatar presenter, cartoon with motion: corner bubble for the first and last 30 s.
AVATAR = {"ranges": [(0, 30), (-30, None)], "motion": True}
