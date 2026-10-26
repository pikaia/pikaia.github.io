"""Video config for the Post Office riot post.

The Post Office and Exchange before 1880, Market Street in the 1920s, the
Straits Times Overland Journal pages of 27 December 1876, John Thomson's
Swatow of around 1869, Amoy around 1870, Singapore and its river around
1870, Ellenborough Market, the Police Court around 1885, Johnston's Pier,
Pickering's 1898 portrait, a Chinese soup seller around 1880, a Pagoda
Street money changer in 2019, the map and the timeline.

Named-person rule: Trotter, Maxwell, Walshe, Douglas, Read and Lim Boon
Keng have no portraits here, so their sentences show places with no
people or a newspaper page; Pickering's sentence shows his portrait. The
soup seller appears only under sentences that name no one. The three
Rijksmuseum album pages are left out of the video (their white mounts).

The newspaper pages, the soup seller, Pickering and the map are
letterboxed; the timeline is fixed.

33 slides, 568.05s. Narration: Kokoro with the OpenVoice clone.
AVATAR: first and last 30s, cartoon with motion.
"""

IMAGES = {
    "GPO": "https://upload.wikimedia.org/wikipedia/commons/thumb/f/f6/KITLV_-_89905_-_Post_office%2C_Exchange_building_and_square_in_Singapore_-_before_1880.tif/lossy-page1-1280px-KITLV_-_89905_-_Post_office%2C_Exchange_building_and_square_in_Singapore_-_before_1880.tif.jpg",
    "MARKET": "https://upload.wikimedia.org/wikipedia/commons/a/a6/Corner_of_Market_St_and_Robinson_Rd_Singapore%2C_1925-1930.jpg",
    "ST2": "/assets/images/straits-times-overland-journal-1876-12-27-page-2.jpg",
    "SOUP": "https://upload.wikimedia.org/wikipedia/commons/thumb/6/62/John_Edmund_Taylor%2C_A_Chinese_Soup_Seller_Trading_in_Singapore_%28c_1880%2C_Wellcome_V0037508%29.jpg/1280px-John_Edmund_Taylor%2C_A_Chinese_Soup_Seller_Trading_in_Singapore_%28c_1880%2C_Wellcome_V0037508%29.jpg",
    "SWJUNK": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/d0/Swatow_MET_DP165628.jpg/1280px-Swatow_MET_DP165628.jpg",
    "SWATOW": "https://upload.wikimedia.org/wikipedia/commons/thumb/b/ba/View_of_Swatow_Harbour_MET_DP165632.jpg/1280px-View_of_Swatow_Harbour_MET_DP165632.jpg",
    "RIVER70": "https://upload.wikimedia.org/wikipedia/commons/thumb/5/52/KITLV_-_106515_-_Harbor_yard_in_Singapore_-_circa_1870.tif/lossy-page1-1280px-KITLV_-_106515_-_Harbor_yard_in_Singapore_-_circa_1870.tif.jpg",
    "AMOY": "https://upload.wikimedia.org/wikipedia/commons/thumb/4/48/Island_of_Koolansoo_and_Amoy_by_Lai_Afong%2C_c1870.jpg/1280px-Island_of_Koolansoo_and_Amoy_by_Lai_Afong%2C_c1870.jpg",
    "SG1870": "https://upload.wikimedia.org/wikipedia/commons/thumb/4/40/KITLV_-_106516_-_Singapore_-_circa_1870.tif/lossy-page1-1280px-KITLV_-_106516_-_Singapore_-_circa_1870.tif.jpg",
    "ST3": "/assets/images/straits-times-overland-journal-1876-12-27-page-3.jpg",
    "ELLEN": "https://upload.wikimedia.org/wikipedia/commons/e/e3/Ellenborough_Market_1910.jpg",
    "MAP": "/assets/images/post-office-riot-map.png",
    "COURT": "https://upload.wikimedia.org/wikipedia/commons/thumb/8/8c/KITLV_-_103754_-_Lambert_%26_Co._-_Court_of_the_police_at_South_Bridge_Road%2C_Singapore_-_circa_1885.tif/lossy-page1-1280px-KITLV_-_103754_-_Lambert_%26_Co._-_Court_of_the_police_at_South_Bridge_Road%2C_Singapore_-_circa_1885.tif.jpg",
    "PIER": "https://upload.wikimedia.org/wikipedia/commons/thumb/5/5e/KITLV_-_103750_-_Johnston%27s_pier_at_Singapore_-_circa_1890.tif/lossy-page1-1280px-KITLV_-_103750_-_Johnston%27s_pier_at_Singapore_-_circa_1890.tif.jpg",
    "PIER2": "https://upload.wikimedia.org/wikipedia/commons/thumb/1/12/KITLV_-_38150_-_Johnston%27s_pier_at_Singapore_-_circa_1890.tif/lossy-page1-1280px-KITLV_-_38150_-_Johnston%27s_pier_at_Singapore_-_circa_1890.tif.jpg",
    "TL": "/assets/images/post-office-riot-timeline-chart.png",
    "PICK": "https://upload.wikimedia.org/wikipedia/commons/thumb/7/71/Portrait_of_Pickering%2C_William_Alexander.jpg/1280px-Portrait_of_Pickering%2C_William_Alexander.jpg",
    "PAGODA": "https://upload.wikimedia.org/wikipedia/commons/thumb/4/4f/Singapore_%28SG%29%2C_China_Town%2C_Pagoda_Street_--_2019_--_4507.jpg/1280px-Singapore_%28SG%29%2C_China_Town%2C_Pagoda_Street_--_2019_--_4507.jpg",
}

# The timeline PNG is the only image not captioned in the post or its gallery.
CREDITS = {
    "TL": "Timeline by Lesser Known Singapore, from Makepeace et al. (1921), Song Ong Siang (1923), the Straits Times Overland Journal and NLB Infopedia",
}

# The channel's 2x2 thumbnail grid, earliest to today: the Post Office
# before 1880, Johnston's Pier around 1890, Market Street in the 1920s and
# a Pagoda Street money changer in 2019.
THUMBNAIL = [
    {"img": "GPO", "pan": (0.5, 0.5)},
    {"img": "PIER", "pan": (0.5, 0.6)},
    {"img": "MARKET", "pan": (0.5, 0.5)},
    {"img": "PAGODA", "pan": (0.5, 0.5)},
]

_E = "ease-in-out"
_IN = {"type": "cover", "zoom": [1.0, 1.06, 1.12], "pan": [(0.5, 0.5)] * 3, "ease": _E}
_OUT = {"type": "cover", "zoom": [1.12, 1.06, 1.0], "pan": [(0.5, 0.5)] * 3, "ease": _E}
# The maps, portrait and small images and the newspaper pages: letterbox, modest zoom.
_PORT = {"type": "letterbox", "zoom": [1.0, 1.04, 1.08], "pan": [(0.5, 0.5)] * 3, "ease": _E}
_PORT_OUT = {"type": "letterbox", "zoom": [1.08, 1.04, 1.0], "pan": [(0.5, 0.5)] * 3, "ease": _E}
# The timeline: letterboxed and still, so its labels stay readable.
_FIX = {"type": "letterbox", "zoom": [1.0, 1.0, 1.0], "pan": [(0.5, 0.5)] * 3, "ease": "linear"}

SLIDES = [
    {"img": "GPO", **_IN},            # 0  s0 title: the Post Office before 1880
    {"img": "MARKET", **_IN},         # 1  s1 81 Market Street; set up for the labourers (s1-2)
    {"img": "ST2", **_PORT},          # 2  s3 wrecked; police fire; three dead
    {"img": "SOUP", **_PORT},         # 3  s4 a labourer sending money home
    {"img": "SWJUNK", **_IN},         # 4  s5 the junks; the earlier post; the Teochew merchants (s5-7)
    {"img": "SWATOW", **_IN},         # 5  s8 1873; talks with London, Peking, Hong Kong (s8-9)
    {"img": "GPO", **_OUT},           # 6  s10 the Gazette notice, 5 December
    {"img": "RIVER70", **_IN},        # 7  s11 Trotter's notice (names him: no people, s11-12)
    {"img": "AMOY", **_IN},           # 8  s13 letters via Swatow and Amoy; fixed charges; compulsory (s13-15)
    {"img": "SG1870", **_IN},         # 9  s16 the merchants; the placards (s16-17)
    {"img": "ST3", **_PORT},          # 10 s18 the placard's words; the reward; the $30 rumour (s18-20)
    {"img": "MARKET", **_OUT},        # 11 s21 assurances; the morning it opened (s21-22)
    {"img": "ST2", **_PORT_OUT},      # 12 s23 8 o'clock; the shop wrecked; Maxwell beaten (names him: no people, s23-25)
    {"img": "ELLEN", **_IN},          # 13 s26 the two police stations; three killed (s26-28)
    {"img": "MAP", **_PORT},          # 14 s29 crowds stay; the Straits Times verdict (s29-31)
    {"img": "ST3", **_PORT_OUT},      # 15 s32 before Captain Walshe (names him: no people)
    {"img": "COURT", **_IN},          # 16 s33 the sentences (s33-35)
    {"img": "ELLEN", **_OUT},         # 17 s36 the market shut; the notice; the towkays' release demanded (s36-39)
    {"img": "PIER", **_IN},           # 18 s40 twelve towkays marched to Johnston's Pier (s40-41)
    {"img": "PIER2", **_IN},          # 19 s42 on the Pluto; 600 marines on Collyer Quay (s42-43)
    {"img": "SG1870", **_OUT},        # 20 s44 Douglas warns the towkays (names him: no people)
    {"img": "RIVER70", **_OUT},       # 21 s45 Read's memory of the monsoon (names him: no people, s45-47)
    {"img": "GPO", **_IN},            # 22 s48 reopened on 18 December (the Postmaster-General: no people)
    {"img": "TL", **_FIX},            # 23 s49 moved into the GPO; 80,000 to 280,000 letters (s49-50)
    {"img": "SWATOW", **_OUT},        # 24 s51 the letter shops supervised; 49 in 1887 (s51-52)
    {"img": "AMOY", **_OUT},          # 25 s53 a new office for the Chinese community
    {"img": "PICK", **_PORT},         # 26 s54 Pickering, Protector of Chinese (names him: his portrait, s54-55)
    {"img": "ST2", **_PORT},          # 27 s56 who was behind it (s56-58)
    {"img": "TL", **_FIX},            # 28 s59 Lim Boon Keng's view (names him: no people)
    {"img": "PAGODA", **_IN},         # 29 s60 money sent home today (s60-61)
    {"img": "SOUP", **_PORT_OUT},     # 30 s62 MAS licensing; the same question as 1876
    {"img": "PIER", **_OUT},          # 31 s63 where it fits (s63-64)
    {"img": "MARKET", **_IN},         # 32 s65 a scheme people did not trust
]

SCHEDULE = [
    (0.0, 0), (3.875, 1), (26.475, 2), (36.175, 3), (43.8, 4), (69.5, 5),
    (90.0, 6), (105.4, 7), (120.5, 8), (144.65, 9), (153.5, 10), (181.7, 11),
    (195.175, 12), (222.725, 13), (237.025, 14), (258.8, 15), (265.825, 16), (289.7, 17),
    (314.05, 18), (336.05, 19), (352.125, 20), (358.95, 21), (380.25, 22), (391.025, 23),
    (415.05, 24), (426.675, 25), (432.75, 26), (462.45, 27), (486.4, 28), (499.15, 29),
    (513.4, 30), (533.35, 31), (560.35, 32),
]
TOTAL_DURATION = 568.05
TIMING_JSON = "audio/the-post-office-riot-of-1876.timing.json"

# The avatar presenter, cartoon with motion: corner bubble for the first and last 30 s.
AVATAR = {"ranges": [(0, 30), (-30, None)], "motion": True}
