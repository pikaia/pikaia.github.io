"""Video config for the Wee Bin post.

The fifteen-picture pool: Lambert's port at Singapore about 1890 (the
scene hero), the harbour in 1860 and the river port about 1870, the
steamship Brisbane in dry dock in 1860, Boat Quay in a Rijksmuseum
photograph and in a postcard of about 1900, Chinese tongkangs, ships
and rowing boats in the harbour, Taylor's 1879 watercolour of the
harbour, Johnston's Pier about 1900, and Collyer Quay and the Tanjong
Pagar harbour about 1910 - plus the three portraits the story turns
on: Wee Bin, Lim Ho Puah and Lim Peng Siang.

Named-person rule: a portrait appears only under sentences naming
that person. Wee Boon Teck, Wee Siang Tat, Kiong Kong Tuan and Oei
Tiong Ham have no portraits in the pool, so their sentences show
harbour and quay scenes. The closing sentence names both the founder
and his grandson, so it closes on the harbour, not a portrait. The
Wee Bin portrait is a tall full-frame photograph, mostly black robe;
its slides pan high (0.5, 0.28) so the face, not the robe, fills the
frame. A head-and-shoulders crop of the portrait is prepared and
awaits Chris's word; if he approves it, the WEEBIN entry below and
the post's image change together before the step-4 widget build.

49 slides, 667.65s. Narration: Kokoro with the OpenVoice clone.
AVATAR: first and last 30s, cartoon with motion.
"""

IMAGES = {
    "PORT": "https://upload.wikimedia.org/wikipedia/commons/thumb/5/5e/KITLV_-_150813_-_Lambert_%26_Co.%2C_G.R._-_Singapore_-_Port_at_Singapore_-_circa_1890.tif/lossy-page1-1280px-KITLV_-_150813_-_Lambert_%26_Co.%2C_G.R._-_Singapore_-_Port_at_Singapore_-_circa_1890.tif.jpg",
    "DOCK": "https://upload.wikimedia.org/wikipedia/commons/thumb/c/c1/KITLV_-_29164_-_The_steamship_Brisbane_in_dry_dock_in_Singapore_-_1860.tif/lossy-page1-1280px-KITLV_-_29164_-_The_steamship_Brisbane_in_dry_dock_in_Singapore_-_1860.tif.jpg",
    "WEEBIN": "https://upload.wikimedia.org/wikipedia/commons/e/ee/Wee_Bin.jpg",
    "HOPUAH": "https://upload.wikimedia.org/wikipedia/commons/2/21/Lim_Ho_Puah.png",
    "QUAY": "https://upload.wikimedia.org/wikipedia/commons/f/fe/Binnenhaven_van_Singapore_The_boat_quay_Singapore_%28titel_op_object%29%2C_RP-F-00-5018-39.jpg",
    "PENGSIANG": "https://upload.wikimedia.org/wikipedia/commons/1/1c/Lim_Peng_Siang.png",
    "PIER": "https://upload.wikimedia.org/wikipedia/commons/5/5c/KITLV_-_50211_-_Lambert_%26_Co.%2C_G.R._-_Singapore_-_Johnston%27s_Pier_Singapore_-_circa_1900.jpg",
    "HARB1860": "https://upload.wikimedia.org/wikipedia/commons/thumb/7/79/KITLV_-_29175_-_View_of_the_harbor_of_Singapore_-_1860.tif/lossy-page1-1280px-KITLV_-_29175_-_View_of_the_harbor_of_Singapore_-_1860.tif.jpg",
    "RIVER1870": "https://upload.wikimedia.org/wikipedia/commons/thumb/a/a2/KITLV_-_106514_-_Port_on_the_river_in_Singapore_-_circa_1870.tif/lossy-page1-1280px-KITLV_-_106514_-_Port_on_the_river_in_Singapore_-_circa_1870.tif.jpg",
    "TONGKANG": "https://upload.wikimedia.org/wikipedia/commons/thumb/9/95/Chinese_schepen_%28tongkans%29_in_haven_van_Singapore%2C_RP-F-F01149-FY.jpg/1280px-Chinese_schepen_%28tongkans%29_in_haven_van_Singapore%2C_RP-F-F01149-FY.jpg",
    "ROWBOATS": "https://upload.wikimedia.org/wikipedia/commons/thumb/1/1b/Schepen_en_roeiboten_in_de_haven_van_Singapore_Harbour%2C_S.pore_%28titel_op_object%29%2C_RP-F-F01197-AE.jpg/1280px-Schepen_en_roeiboten_in_de_haven_van_Singapore_Harbour%2C_S.pore_%28titel_op_object%29%2C_RP-F-F01197-AE.jpg",
    "NBQ1900": "https://upload.wikimedia.org/wikipedia/commons/b/b6/Singapore_Boat_Quay_ca._1900.jpg",
    "COLLYER": "https://upload.wikimedia.org/wikipedia/commons/thumb/f/f0/KITLV_-_79887_-_Kleingrothe%2C_C.J._-_Medan_-_Collyer_Quay%2C_Quay_in_Singapore_-_circa_1910.tif/lossy-page1-1280px-KITLV_-_79887_-_Kleingrothe%2C_C.J._-_Medan_-_Collyer_Quay%2C_Quay_in_Singapore_-_circa_1910.tif.jpg",
    "TANJONGP": "https://upload.wikimedia.org/wikipedia/commons/thumb/a/a0/KITLV_-_79886_-_Kleingrothe%2C_C.J._-_Medan_-_Tanjong_Pagar%2C_harbor_in_Singapore_-_circa_1910.tif/lossy-page1-1280px-KITLV_-_79886_-_Kleingrothe%2C_C.J._-_Medan_-_Tanjong_Pagar%2C_harbor_in_Singapore_-_circa_1910.tif.jpg",
    "TAYLOR": "https://upload.wikimedia.org/wikipedia/commons/4/47/John_Edmund_Taylor%2C_The_Harbour%2C_Singapore_%281879%2C_Wellcome_V0037490%29.jpg"
}

# Every image is captioned in the post or its gallery.
CREDITS = {}

# The channel's 2x2 thumbnail grid, in story order: the port at its
# height, the founder, the steam fleet in dry dock, and the modern
# quay that succeeded his world. The portrait cell pans high, to the
# face.
THUMBNAIL = [
    {"img": "PORT", "pan": (0.5, 0.5)},
    {"img": "WEEBIN", "pan": (0.5, 0.25)},
    {"img": "DOCK", "pan": (0.5, 0.5)},
    {"img": "COLLYER", "pan": (0.5, 0.5)},
]

_E = "ease-in-out"
_IN = {"type": "cover", "zoom": [1.0, 1.06, 1.12], "pan": [(0.5, 0.5)] * 3, "ease": _E}
_OUT = {"type": "cover", "zoom": [1.12, 1.06, 1.0], "pan": [(0.5, 0.5)] * 3, "ease": _E}
# The tall Wee Bin portrait: same zooms, panned up to the face.
_INP = {"type": "cover", "zoom": [1.0, 1.06, 1.12], "pan": [(0.5, 0.28)] * 3, "ease": _E}
_OUTP = {"type": "cover", "zoom": [1.12, 1.06, 1.0], "pan": [(0.5, 0.28)] * 3, "ease": _E}

SLIDES = [
    {"img": "PORT", **_IN},  # 0  s0 title: the port at Singapore, c. 1890 (4.8s)
    {"img": "NBQ1900", **_OUT},  # 1  s1-2 March 1911: the Straits Times announces the end (14.8s)
    {"img": "QUAY", **_IN},  # 2  s3 106 Market St.; the steamers sold by auction (11.8s)
    {"img": "WEEBIN", **_INP},  # 3  s4-5 the date on the founder's grave: died 1868 (names him: his portrait) (10.6s)
    {"img": "PORT", **_OUT},  # 4  s6 at its height the largest Chinese shipping business in Singapore (20.3s)
    {"img": "RIVER1870", **_IN},  # 5  s7 a Hokkien, born 1823 in Longxi county (8.0s)
    {"img": "HARB1860", **_OUT},  # 6  s8-9 arrival unrecorded; by 1856 he founds his house (19.5s)
    {"img": "DOCK", **_IN},  # 7  s10-11 Western business practices; the Dutch East Indies trade (10.1s)
    {"img": "TONGKANG", **_OUT},  # 8  s12-13 Bali produce, earthenware, sago, merchant banking (16.3s)
    {"img": "ROWBOATS", **_IN},  # 9  s14 a fleet of over twenty vessels (11.1s)
    {"img": "TAYLOR", **_OUT},  # 10  s15 the 1866 survey: 56 of 178 vessels Chinese-owned (12.1s)
    {"img": "QUAY", **_IN},  # 11  s16 his standing in the small print: executor of Wee Lim Seng's estate (19.8s)
    {"img": "WEEBIN", **_OUTP},  # 12  s17-18 married twice; a daughter of Kiong Kong Tuan (names him: his portrait) (22.8s)
    {"img": "PORT", **_IN},  # 13  s19-21 he died in 1868; the firm did not die with him (16.2s)
    {"img": "RIVER1870", **_OUT},  # 14  s22 Boon Teck grows into the business (names him: no portrait; the river port) (9.1s)
    {"img": "NBQ1900", **_IN},  # 15  s23 the hospital and Po Leung Kuk committees; the $4,000 ward gift (22.5s)
    {"img": "DOCK", **_OUT},  # 16  s24 Boon Teck dies in 1888, the second towkay to die in office (8.8s)
    {"img": "TONGKANG", **_IN},  # 17  s25 Siang Tat becomes a partner in 1900 (names him: no portrait) (7.6s)
    {"img": "ROWBOATS", **_OUT},  # 18  s26 no head for business; the Philomathic Society's violinist (14.1s)
    {"img": "QUAY", **_IN},  # 19  s27-28 Siang Tat dies in 1901; survival rests on the son-in-law (12.2s)
    {"img": "HOPUAH", **_OUT},  # 20  s29 Lim Ho Puah: born in Amoy, entered the firm in the kitchen (names him: his portrait) (14.5s)
    {"img": "PIER", **_IN},  # 21  s30-31 bookkeeper; executor after 1888, running the fleet (17.5s)
    {"img": "PORT", **_OUT},  # 22  s32-34 the kitchen boy now senior partner; the China passenger trade, 1891 (14.3s)
    {"img": "ROWBOATS", **_IN},  # 23  s35-36 Hong Leong, 1894; the Glenfalloch, largest in the trade (14.4s)
    {"img": "DOCK", **_OUT},  # 24  s37 the Hong Moh, a two-funnelled steamer (7.8s)
    {"img": "COLLYER", **_IN},  # 25  s38 the weekly service: Rangoon, Penang, Singapore, Hong Kong, Swatow, Amoy (17.2s)
    {"img": "TANJONGP", **_OUT},  # 26  s39 a director of the Tanjong Pagar Dock Company (the harbour it ran) (13.3s)
    {"img": "HOPUAH", **_IN},  # 27  s40 sole surviving partner after 1901 (names him: his portrait) (13.0s)
    {"img": "NBQ1900", **_OUT},  # 28  s41-42 the widow Ho Shiok Chui Neo; her remarriage in 1909 (15.0s)
    {"img": "QUAY", **_IN},  # 29  s43-44 ninety-seven lots under the hammer, 1910; the firm to be wound up (13.2s)
    {"img": "HARB1860", **_OUT},  # 30  s45-47 what the liquidation was not: no bankruptcy, no failure (17.3s)
    {"img": "PORT", **_IN},  # 31  s48-50 'well-known and long-established'; Powell & Co. sell the steamers (16.4s)
    {"img": "TAYLOR", **_OUT},  # 32  s51 the Pinang Gazette prices: Glenfalloch $60,000, Hong Wan I $85,000 (8.3s)
    {"img": "ROWBOATS", **_IN},  # 33  s52 two smaller ships to Oei Tiong Ham's agent (names him: no portrait) (8.4s)
    {"img": "PENGSIANG", **_OUT},  # 34  s53-54 the large steamers bought by Lim Peng Siang (names him: his portrait) (16.3s)
    {"img": "COLLYER", **_IN},  # 35  s55-56 1904: Ho Hong founded on a $50,000 loan (names him: the new age's quay) (16.9s)
    {"img": "QUAY", **_OUT},  # 36  s57 Ho Hong: 'Ho' from Lim Ho Puah, 'Hong' from Hong Guan (10.4s)
    {"img": "COLLYER", **_IN},  # 37  s58 the steamers become Ho Hong's shipping department, 1913 (15.1s)
    {"img": "TONGKANG", **_OUT},  # 38  s59 Glenfalloch, Hong Bee and Hong Wan I transferred into Ho Hong (17.2s)
    {"img": "HOPUAH", **_IN},  # 39  s60-61 the man who held the firm together dies, February 1914 (names him: his portrait) (11.7s)
    {"img": "PIER", **_OUT},  # 40  s62 the funeral procession, the longest ever seen in Singapore (14.2s)
    {"img": "NBQ1900", **_IN},  # 41  s63 the silken coffin cover stolen on the way (11.3s)
    {"img": "QUAY", **_OUT},  # 42  s64 'The Coffin Cover' - the Free Press reports the conviction (13.6s)
    {"img": "WEEBIN", **_INP},  # 43  s65-66 nothing on Market Street today; the name survives in one portrait (names him: the portrait itself) (12.9s)
    {"img": "PORT", **_IN},  # 44  s67 the trade itself never stopped: ships and routes into Ho Hong (14.8s)
    {"img": "HARB1860", **_OUT},  # 45  s68-69 outlived its founder by forty-three years; then outlived itself (8.2s)
    {"img": "TAYLOR", **_IN},  # 46  s70 where it fits: one of the first great Chinese shipping houses (18.9s)
    {"img": "COLLYER", **_OUT},  # 47  s71 settlement, not collapse; Ho Hong grows into banks and industry (14.5s)
    {"img": "PORT", **_IN},  # 48  s72 the family prequel to the Lim Peng Siang post (names both men: the harbour closes) (9.1s)
]

SCHEDULE = [
    (0, 0), (4.75, 1), (19.575, 2), (31.35, 3), (41.925, 4), (62.25, 5),
    (70.275, 6), (89.725, 7), (99.825, 8), (116.075, 9), (127.15, 10), (139.275, 11),
    (159.025, 12), (181.8, 13), (197.975, 14), (207.1, 15), (229.6, 16), (238.4, 17),
    (245.95, 18), (260.05, 19), (272.2, 20), (286.725, 21), (304.25, 22), (318.55, 23),
    (332.925, 24), (340.7, 25), (357.9, 26), (371.225, 27), (384.2, 28), (399.225, 29),
    (412.475, 30), (429.8, 31), (446.15, 32), (454.4, 33), (462.775, 34), (479.075, 35),
    (496.0, 36), (506.35, 37), (521.45, 38), (538.675, 39), (550.375, 40), (564.525, 41),
    (575.825, 42), (589.45, 43), (602.325, 44), (617.15, 45), (625.3, 46), (644.15, 47),
    (658.6, 48)
]
TOTAL_DURATION = 667.65
TIMING_JSON = "audio/wee-bin-the-shipping-magnate-whose-firm-outlived-its-own-name.timing.json"

# The avatar presenter, cartoon with motion: corner bubble for the first and last 30 s.
AVATAR = {"ranges": [(0, 30), (-30, None)], "motion": True}
