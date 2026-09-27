"""Video config for the early banks post.

Photos: Battery Road c.1910, Johnston's Pier and the Hongkong and Shanghai Bank
(a postcard, zoomed 1.4+ to stay inside the printed photo, and the same view as
a plate), the HSBC building c.1900, the Chartered Bank on Raffles Place, the
1885 Oriental Bank note and the Sri Thendayuthapani Temple. The two silver
dollars (borrowed from the Spanish dollar post) are frozen letterbox. The
Straits Times of 5 August 1845 (page 7) is zoomed to the note on the planned
Oriental Bank branch and the Union Bank of Calcutta.

31 slides, one per sentence.
"""

IMAGES = {
    "BATTERY": "https://upload.wikimedia.org/wikipedia/commons/thumb/8/89/KITLV_-_79890_-_Kleingrothe%2C_C.J._-_Medan_-_Battery_Road_at_Singapore_-_circa_1910.tif/lossy-page1-1920px-KITLV_-_79890_-_Kleingrothe%2C_C.J._-_Medan_-_Battery_Road_at_Singapore_-_circa_1910.tif.jpg",
    "CHARTERED": "https://upload.wikimedia.org/wikipedia/commons/thumb/5/59/The_Chartered_Bank_aan_Raffles_Place_te_Singapore%2C_KITLV_104795.tiff/lossy-page1-1920px-The_Chartered_Bank_aan_Raffles_Place_te_Singapore%2C_KITLV_104795.tiff.jpg",
    "COINSG": "https://upload.wikimedia.org/wikipedia/commons/3/33/1789_Charles_IV_Spanish_dollar_countermarked_with_Chinese_words_meaning_%22Singapore%22.jpg",
    "HSBC": "https://upload.wikimedia.org/wikipedia/commons/thumb/1/13/KITLV_-_50198_-_Lambert_%26_Co.%2C_G.R._-_Singapore_-_Building_of_the_Hong_Kong_and_Shanghai_Bank_in_Singapore_-_circa_1900.tif/lossy-page1-1920px-KITLV_-_50198_-_Lambert_%26_Co.%2C_G.R._-_Singapore_-_Building_of_the_Hong_Kong_and_Shanghai_Bank_in_Singapore_-_circa_1900.tif.jpg",
    "HSBC05": "https://upload.wikimedia.org/wikipedia/commons/8/81/Photographic_Views_of_Singapore_Plate_05_Hongkong_and_Shanghai_Bank.jpg",
    "NOTE": "https://upload.wikimedia.org/wikipedia/commons/thumb/a/a1/10_dollar_note%2C_Oriental_Bank_Corporation%2C_Singapore%2C_1885._On_display_at_the_British_Museum_in_London.jpg/1920px-10_dollar_note%2C_Oriental_Bank_Corporation%2C_Singapore%2C_1885._On_display_at_the_British_Museum_in_London.jpg",
    "PIER": "https://upload.wikimedia.org/wikipedia/commons/thumb/1/1e/KITLV_-_1404900_-_Johnston%27s_Pier_and_H._M._Bank._Singapore_-_1895-1906.tif/lossy-page1-1920px-KITLV_-_1404900_-_Johnston%27s_Pier_and_H._M._Bank._Singapore_-_1895-1906.tif.jpg",
    "PILLAR": "https://upload.wikimedia.org/wikipedia/commons/thumb/f/f9/Mexico_Carlos_III_Pillar_Dollar_of_8_Reales_1771.jpg/1920px-Mexico_Carlos_III_Pillar_Dollar_of_8_Reales_1771.jpg",
    "ST45": "/assets/images/straits-times-1845-08-05-page-7.jpg",
    "TEMPLE": "https://upload.wikimedia.org/wikipedia/commons/thumb/1/19/Singapore._Sri_Thendayuthapani_Temple._2013-10-09_15-10-07.jpg/1920px-Singapore._Sri_Thendayuthapani_Temple._2013-10-09_15-10-07.jpg",
}

_P0 = {"type": "cover", "zoom": [1.0, 1.05, 1.1], "pan": [(0.3, 0.5), (0.5, 0.5), (0.7, 0.5)], "ease": "ease-in-out"}
_P1 = {"type": "cover", "zoom": [1.4, 1.45, 1.5], "pan": [(0.25, 0.3), (0.3, 0.3), (0.35, 0.3)], "ease": "ease-in-out"}
_P2 = {"type": "cover", "zoom": [1.1, 1.05, 1.0], "pan": [(0.7, 0.5), (0.5, 0.5), (0.3, 0.5)], "ease": "ease-in-out"}
_P3 = {"type": "cover", "zoom": [1.5, 1.45, 1.4], "pan": [(0.35, 0.3), (0.3, 0.3), (0.25, 0.3)], "ease": "ease-in-out"}
_P4 = {"type": "cover", "zoom": [1.5, 1.55, 1.6], "pan": [(0.15, 0.6), (0.2, 0.6), (0.25, 0.6)], "ease": "ease-in-out"}
_P5 = {"type": "letterbox", "zoom": [1.0, 1.0, 1.0], "pan": [(0.5, 0.5)] * 3, "ease": "linear"}
_P6 = {"type": "cover", "zoom": [3.00, 3.07, 3.15], "pan": [(0.0, 0.374), (0.0, 0.386), (0.002, 0.398)], "ease": "ease-in-out"}
_P7 = {"type": "cover", "zoom": [1.4, 1.45, 1.5], "pan": [(0.5, 0.55), (0.5, 0.55), (0.5, 0.55)], "ease": "ease-in-out"}
_P8 = {"type": "cover", "zoom": [1.8, 1.85, 1.9], "pan": [(0.35, 0.25), (0.35, 0.25), (0.35, 0.25)], "ease": "ease-in-out"}
_P9 = {"type": "cover", "zoom": [2.60, 2.67, 2.73], "pan": [(0.0, 0.336), (0.0, 0.348), (0.0, 0.361)], "ease": "ease-in-out"}
_P10 = {"type": "cover", "zoom": [2.80, 2.87, 2.94], "pan": [(0.0, 0.407), (0.0, 0.419), (0.0, 0.431)], "ease": "ease-in-out"}

SLIDES = [
    {"img": "BATTERY", **_P0},  # s0 Before the Banks: How Singapore's Merchants 
    {"img": "PIER", **_P1},  # s1 For its first twenty-one years, Singapore wa
    {"img": "HSBC05", **_P0},  # s2 Its merchants still borrowed, lent, paid and
    {"img": "BATTERY", **_P2},  # s3 When the first bank finally opened a branch 
    {"img": "PIER", **_P3},  # s4 In the port's early years, the work that a b
    {"img": "HSBC05", **_P2},  # s5 They held money for their clients, advanced 
    {"img": "BATTERY", **_P4},  # s6 According to the National Library Board's hi
    {"img": "COINSG", **_P5},  # s7 Trade itself ran on silver coins, mostly the
    {"img": "PILLAR", **_P5},  # s8 Goods changed hands on the promise of paymen
    {"img": "ST45", **_P6},  # s9 The first bank in Singapore was a branch of 
    {"img": "BATTERY", **_P7},  # s10 It offered merchants advances on goods to be
    {"img": "CHARTERED", **_P0},  # s11 It also issued the first banknotes with the 
    {"img": "PIER", **_P8},  # s12 Its parent bank in Calcutta collapsed in 184
    {"img": "ST45", **_P9},  # s13 A year before the Oriental Bank opened, The 
    {"img": "ST45", **_P10},  # s14 Other banks followed, each based elsewhere a
    {"img": "NOTE", **_P0},  # s15 The Oriental Bank came in 1846, the Mercanti
    {"img": "HSBC", **_P0},  # s16 The Hongkong and Shanghai Bank did business 
    {"img": "CHARTERED", **_P2},  # s17 These were European banks, and most of their
    {"img": "HSBC", **_P2},  # s18 The comprador vouched for the customers he b
    {"img": "TEMPLE", **_P0},  # s19 Alongside the banks, many borrowers who coul
    {"img": "HSBC05", **_P7},  # s20 The National Library Board's account describ
    {"img": "CHARTERED", **_P7},  # s21 The banks found the arrangement safe enough,
    {"img": "NOTE", **_P7},  # s22 The Chettiars' terms could be expensive for 
    {"img": "TEMPLE", **_P2},  # s23 The community's standing in the town shows i
    {"img": "TEMPLE", **_P7},  # s24 The Sri Thendayuthapani Temple on Tank Road,
    {"img": "BATTERY", **_P0},  # s25 The foreign banks gave Singapore's trade acc
    {"img": "PIER", **_P1},  # s26 But they did not replace the older ways of k
    {"img": "HSBC05", **_P0},  # s27 The agency houses, the compradors and the Ch
    {"img": "CHARTERED", **_P0},  # s28 Where it fits in the bigger story: Singapore
    {"img": "COINSG", **_P5},  # s29 For the first two decades there were none, a
    {"img": "HSBC", **_P0},  # s30 When the banks came, from 1840, they settled
]

SCHEDULE = [
    (0.0, 0), (4.325, 1), (11.85, 2), (24.35, 3), (32.05, 4),
    (45.525, 5), (53.625, 6), (65.2, 7), (72.025, 8), (81.575, 9),
    (89.05, 10), (102.15, 11), (107.65, 12), (112.55, 13), (128.625, 14),
    (136.45, 15), (154.325, 16), (168.225, 17), (185.45, 18), (192.85, 19),
    (201.85, 20), (215.375, 21), (223.0, 22), (239.25, 23), (244.1, 24),
    (255.7, 25), (270.275, 26), (275.3, 27), (288.55, 28), (298.125, 29),
    (307.075, 30),
]
TOTAL_DURATION = 320.575
TIMING_JSON = "audio/before-the-banks-how-singapores-merchants-kept-their-money.timing.json"
