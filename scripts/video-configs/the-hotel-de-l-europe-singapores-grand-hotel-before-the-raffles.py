"""Video config for the Hotel de l'Europe post.

The ten-picture pool: the rebuilt hotel in its own 1914 souvenir album
(the hero plate) and the Bird Cage dining room from the same album, the
Padang in 1914, the old hotel in 1897 and about 1890, carriages along
the front, High Street in a colour photochrom, the hotel in its
grounds, and the site today as the former Supreme Court and as
National Gallery Singapore. A thin pool for twelve minutes, so images
recur at new story beats; no map (Chris's call, 2026-10-31: the
hotel's three addresses carry the story).

Named-person rule: the pool holds no portrait of Kipling, Dutronquoy,
Esperanza, Casteleyns, Hjelmstrom, Becker, the Alkaffs, Tomlinson,
Adis, Oliveiro or Ward, so every sentence naming a person shows the
hotel or a street or place with no portrayed person. The grounds
photograph's one anonymous figure appears only under sentences that
name nobody.

43 slides, 740.80s. Narration: Kokoro with the OpenVoice clone.
AVATAR: first and last 30s, cartoon with motion.
"""

IMAGES = {
    "HERO": "https://upload.wikimedia.org/wikipedia/commons/5/57/Souvenir_of_Singapore%2C_1914_-_Plate_03_-_Europe_Hotel.jpg",
    "OLD97": "https://upload.wikimedia.org/wikipedia/commons/thumb/2/2a/KITLV_-_29176_-_Lambert_%26_Co.%2C_G.R._-_Singapore_-_Hotel_de_l%27Europe_at_Singapore_-_1897.tif/lossy-page1-1280px-KITLV_-_29176_-_Lambert_%26_Co.%2C_G.R._-_Singapore_-_Hotel_de_l%27Europe_at_Singapore_-_1897.tif.jpg",
    "G1890": "https://upload.wikimedia.org/wikipedia/commons/thumb/7/72/KITLV_-_377459_-_Hotel_d%27Europe_at_Singapore_-_circa_1890.tif/lossy-page1-1280px-KITLV_-_377459_-_Hotel_d%27Europe_at_Singapore_-_circa_1890.tif.jpg",
    "CARR": "https://upload.wikimedia.org/wikipedia/commons/thumb/9/9b/Koetsen_voor_het_Hotel_de_l%27Europe_in_Singapore%2C_SFA002022355.jpg/1280px-Koetsen_voor_het_Hotel_de_l%27Europe_in_Singapore%2C_SFA002022355.jpg",
    "HIGH": "https://upload.wikimedia.org/wikipedia/commons/2/26/Singapore._High_Street_with_Hotel_Europe_LCCN2017657652.jpg",
    "GRND": "https://upload.wikimedia.org/wikipedia/commons/thumb/9/91/KITLV_A1225_-_Hotel_d_%27Europe_te_Singapore%2C_KITLV_142885.tiff/lossy-page1-1280px-KITLV_A1225_-_Hotel_d_%27Europe_te_Singapore%2C_KITLV_142885.tiff.jpg",
    "BIRD": "https://upload.wikimedia.org/wikipedia/commons/9/96/Souvenir_of_Singapore%2C_1914_-_Plate_02_-_Dining_Room.jpg",
    "PAD14": "https://upload.wikimedia.org/wikipedia/commons/4/41/Souvenir_of_Singapore%2C_1914_-_Plate_12_-_Singapore_Cricket_Club%2C_Town_Hall%2C_Supreme_Court_and_Europe_Hotel.jpg",
    "COURT": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/d4/Former_Supreme_Court_Singapore.jpg/1280px-Former_Supreme_Court_Singapore.jpg",
    "GAL": "https://upload.wikimedia.org/wikipedia/commons/thumb/5/5e/National_Gallery_Singapore_1.jpg/1280px-National_Gallery_Singapore_1.jpg"
}

# Every image is captioned in the post or its gallery.
CREDITS = {}

# The channel's 2x2 thumbnail grid, in story order: the old hotel
# across the Esplanade about 1890, High Street in colour in the 1890s,
# the rebuilt hotel in 1914, and the site today under the Gallery dome.
THUMBNAIL = [
    {"img": "G1890", "pan": (0.5, 0.5)},
    {"img": "HIGH", "pan": (0.5, 0.5)},
    {"img": "HERO", "pan": (0.5, 0.5)},
    {"img": "GAL", "pan": (0.5, 0.5)},
]

_E = "ease-in-out"
_IN = {"type": "cover", "zoom": [1.0, 1.06, 1.12], "pan": [(0.5, 0.5)] * 3, "ease": _E}
_OUT = {"type": "cover", "zoom": [1.12, 1.06, 1.0], "pan": [(0.5, 0.5)] * 3, "ease": _E}

SLIDES = [
    {"img": "HERO", **_IN},  # 0  s0 title: the rebuilt hotel, 1914 plate (4.9s)
    {"img": "OLD97", **_OUT},  # 1  s1 Kipling (names him: no portrait exists; the old hotel) (14.0s)
    {"img": "PAD14", **_IN},  # 2  s2 the Raffles managers borrow the line (9.9s)
    {"img": "G1890", **_OUT},  # 3  s3 across the Padang to the great rival (17.6s)
    {"img": "COURT", **_IN},  # 4  s4-5 the site today: the former Supreme Court (12.0s)
    {"img": "GAL", **_OUT},  # 5  s6 the domed Gallery wing on the footprint (14.1s)
    {"img": "PAD14", **_IN},  # 6  s7-8 the Esplanade and the Padang; the best seat (16.3s)
    {"img": "CARR", **_OUT},  # 7  s9-10 it did not begin grandly (11.2s)
    {"img": "HIGH", **_IN},  # 8  s11-12 Dutronquoy's London Hotel, High Street corner (names him: street scene) (24.3s)
    {"img": "G1890", **_OUT},  # 9  s13 Madame Esperanza takes over (names her: the hotel across the Esplanade) (10.4s)
    {"img": "OLD97", **_IN},  # 10  s14-15 Casteleyns starts the Hotel d'Europe on Hill Street (names him: the old hotel) (13.0s)
    {"img": "G1890", **_OUT},  # 11  s16-17 the moves; arrived on the Padang (16.7s)
    {"img": "GRND", **_IN},  # 12  s18 comfortable, not magnificent: thirty rooms in the grounds (13.9s)
    {"img": "CARR", **_OUT},  # 13  s19 the 1870s visitor: bar-room, billiard room, reading room (19.6s)
    {"img": "HIGH", **_IN},  # 14  s20 Hjelmstrom and Becker, proprietors (names them: High Street frontage) (17.4s)
    {"img": "PAD14", **_OUT},  # 15  s21-22 the Raffles opens; a two-hotel town (18.7s)
    {"img": "HERO", **_IN},  # 16  s23 glamour and travellers vs the residents' hotel (11.2s)
    {"img": "OLD97", **_OUT},  # 17  s24 the Alkaff ownership years (names them: the old buildings) (21.2s)
    {"img": "CARR", **_IN},  # 18  s25 what the archives record (15.0s)
    {"img": "G1890", **_OUT},  # 19  s26-27 investors, not managers; three parties, three roles (24.7s)
    {"img": "OLD97", **_IN},  # 20  s28-29 the old buildings show their age; 'barn-like erection' (18.2s)
    {"img": "HIGH", **_OUT},  # 21  s30-32 grander called for; the Tomlinson syndicate (names them: street scene) (25.4s)
    {"img": "CARR", **_IN},  # 22  s33 November 1905: Adis takes over the financing (names him: the hotel front) (15.9s)
    {"img": "G1890", **_OUT},  # 23  s34-36 Adis's own story: Howrah, Hong Kong (names him: the hotel he would rebuild) (25.0s)
    {"img": "HERO", **_IN},  # 24  s37-38 arrived with very little; the Adis Building (28.1s)
    {"img": "BIRD", **_OUT},  # 25  s39-40 built to impress; part opens, 1906-07 (13.8s)
    {"img": "HERO", **_IN},  # 26  s41 the Renaissance palace described (22.3s)
    {"img": "BIRD", **_OUT},  # 27  s42 120 bedrooms, each with balcony and bathroom (16.6s)
    {"img": "CARR", **_IN},  # 28  s43-44 its own carriages to Tanjong Pagar; a million dollars (10.2s)
    {"img": "BIRD", **_OUT},  # 29  s45-46 the Bird Cage dining room; roof garden and ladies' lounge (17.8s)
    {"img": "PAD14", **_IN},  # 30  s47-48 Oliveiro's dinner music (names him: the Padang frontage); the 1924 rate (21.5s)
    {"img": "OLD97", **_OUT},  # 31  s49-50 February 1915: the mutiny; fortress and sanctuary (20.2s)
    {"img": "PAD14", **_IN},  # 32  s51 parades on the Padang again (11.2s)
    {"img": "G1890", **_OUT},  # 33  s52-53 the end begins: behind the times (17.0s)
    {"img": "HIGH", **_IN},  # 34  s54-55 the Peninsula plan; The Europe Hotel Ltd (22.0s)
    {"img": "CARR", **_OUT},  # 35  s56 liquidation; 'The Europe Hotel Closes' (13.4s)
    {"img": "BIRD", **_IN},  # 36  s57-58 dancing almost to the last: the dinner dances (20.2s)
    {"img": "OLD97", **_OUT},  # 37  s59-60 empty; demolition decided (18.2s)
    {"img": "COURT", **_IN},  # 38  s61-62 the government acquires; Ward's Supreme Court rises (26.6s)
    {"img": "GAL", **_OUT},  # 39  s63 the last classical building; the Gallery wing since 2015 (18.3s)
    {"img": "PAD14", **_IN},  # 40  s64-65 the Europe never left the Padang; sleep in an art gallery (21.3s)
    {"img": "GAL", **_OUT},  # 41  s66 where it fits: the other pole of Singapore's social world (17.8s)
    {"img": "HERO", **_IN},  # 42  s67 the million-dollar fortunes that built the civic district (13.6s)
]

SCHEDULE = [
    (0, 0), (4.925, 1), (18.95, 2), (28.825, 3), (46.4, 4), (58.35, 5),
    (72.475, 6), (88.775, 7), (99.975, 8), (124.3, 9), (134.65, 10), (147.625, 11),
    (164.325, 12), (178.175, 13), (197.775, 14), (215.225, 15), (233.925, 16), (245.1, 17),
    (266.325, 18), (281.325, 19), (306.025, 20), (324.225, 21), (349.6, 22), (365.5, 23),
    (390.5, 24), (418.575, 25), (432.35, 26), (454.675, 27), (471.275, 28), (481.5, 29),
    (499.325, 30), (520.8, 31), (541.05, 32), (552.275, 33), (569.25, 34), (591.3, 35),
    (604.725, 36), (624.9, 37), (643.1, 38), (669.75, 39), (688.05, 40), (709.325, 41),
    (727.175, 42)
]
TOTAL_DURATION = 740.8
TIMING_JSON = "audio/the-hotel-de-l-europe-singapores-grand-hotel-before-the-raffles.timing.json"

# The avatar presenter, cartoon with motion: corner bubble for the first and last 30 s.
AVATAR = {"ranges": [(0, 30), (-30, None)], "motion": True}
