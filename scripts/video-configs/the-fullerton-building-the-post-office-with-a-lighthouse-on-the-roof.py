"""Video config for the Fullerton Building post.

Ten images. Everything is an ordinary landscape photo and uses cover
except LANTERN2021 (a portrait night shot), FULLERTON (a portrait
painting) and SHENTON (a grainy portrait, kept in letterbox with only a
mild zoom so the grain isn't magnified), which use letterbox. The
pool of period exteriors is genuinely thin (Commons has one 1920s-30s
view of the finished building), so HERO is repeated on purpose.

  HERO         - 1920-40 harbour postcard of the Fullerton Building
                 (Commons, KITLV 1404891)
  FULLERTON    - Robert Fullerton, first Governor of the Straits
                 Settlements, by George Chinnery (Commons)
  SHENTON      - Sir Shenton Thomas, Governor of the Straits
                 Settlements 1934-42 (Commons, unknown author)
  PO1890       - the old Post Office and Exchange Building on Fullerton
                 Square, c. 1890, Tan Kim Seng fountain at left
                 (Commons, KITLV 103747)
  OIL1942      - smoke from the burning naval base oil tanks over the
                 roofs, early 1942 (Commons, Clifford Bottomley)
  R1973        - the building in 1973/74 with the original Merlion and
                 new towers behind (Commons, Rainer Halama)
  LANTERN2011  - the preserved Fullerton Light lantern at HarbourFront
                 Tower One, 2011 (Commons, Thaejas)
  MODERN2018   - the hotel across the water, 2018 (Commons, gallery)
  CORNER2013   - the columned corner beside Cavenagh Bridge, 2013
                 (Commons, gallery)
  LANTERN2021  - the lantern lit at night at Mapletree Business City,
                 2021 (Commons, gallery)

45 slides, 427.3s.
"""

_U = "https://upload.wikimedia.org/wikipedia/commons"

IMAGES = {
    "HERO": f"{_U}/thumb/1/19/Singapore%2C_KITLV_1404891.tiff/lossy-page1-1280px-Singapore%2C_KITLV_1404891.tiff.jpg",
    "FULLERTON": f"{_U}/4/48/Robert_Fullerton%2C_by_George_Chinnery.jpg",
    "SHENTON": f"{_U}/c/c7/Shenton_Thomas.jpg",
    "PO1890": f"{_U}/thumb/0/0c/KITLV_-_103747_-_Post_and_exchange_office_in_Singapore_-_circa_1890.tif/lossy-page1-1280px-KITLV_-_103747_-_Post_and_exchange_office_in_Singapore_-_circa_1890.tif.jpg",
    "OIL1942": f"{_U}/thumb/4/44/Burning_oil_fields.jpg/1280px-Burning_oil_fields.jpg",
    "R1973": f"{_U}/thumb/e/e4/Singapore-Merlion-1973-74-WUS08176.jpg/1280px-Singapore-Merlion-1973-74-WUS08176.jpg",
    "LANTERN2011": f"{_U}/d/dc/Fullerton_Lighthouse%2C_Singapore_-_20110904.jpg",
    "MODERN2018": f"{_U}/f/f3/Singapore_-_The_Fullerton_Hotel_IMG_9254.jpg",
    "CORNER2013": f"{_U}/7/78/Fullerton_Hotel_-_panoramio_%281%29.jpg",
    "LANTERN2021": f"{_U}/f/f8/Former_Fullerton_Lighthouse_Lantern_at_Mapletree_Business_City%2C_Singapore_2021.jpg",
}

_CVZ = {"type": "cover", "zoom": [1.0, 1.06, 1.12], "pan": [(0.5, 0.5)] * 3, "ease": "ease-in-out"}
_CVZO = {"type": "cover", "zoom": [1.12, 1.06, 1.0], "pan": [(0.5, 0.5)] * 3, "ease": "ease-out"}
_LTB = {"type": "letterbox", "zoom": [1.0, 1.04, 1.08], "pan": [(0.5, 0.5)] * 3, "ease": "ease-in-out"}
_LTBO = {"type": "letterbox", "zoom": [1.08, 1.04, 1.0], "pan": [(0.5, 0.5)] * 3, "ease": "ease-out"}

SLIDES = [
    {"img": "HERO", **_CVZO},             # 0  s0  title
    {"img": "HERO", **_CVZ},              # 1  s1  beacon for twenty years
    {"img": "MODERN2018", **_CVZO},       # 2  s2  many people walk past
    {"img": "FULLERTON", **_LTB},         # 3  s3  site named for Fullerton, the fort
    {"img": "PO1890", **_CVZ},            # 4  s4  1880s Fullerton Square
    {"img": "PO1890", **_CVZO},           # 5  s5  Tan Kim Seng fountain
    {"img": "HERO", **_CVZ},              # 6  s6  1920s GPO on Collyer Quay
    {"img": "PO1890", **_CVZ},            # 7  s7  old buildings cleared
    {"img": "HERO", **_CVZO},             # 8  s8  1920 Keys appointed
    {"img": "HERO", **_CVZ},              # 9  s9  postwar stringency
    {"img": "HERO", **_CVZO},             # 10 s10 tenders, Perry & Co.
    {"img": "CORNER2013", **_CVZ},        # 11 s11 foundation raft
    {"img": "HERO", **_CVZO},             # 12 s12 Clifford opened it, 27 June 1928
    {"img": "HERO", **_CVZ},              # 13 s13 tender and total vote
    {"img": "MODERN2018", **_CVZ},        # 14 s14 most imposing building
    {"img": "CORNER2013", **_CVZO},       # 15 s15 120 ft, colonnade, tenants
    {"img": "R1973", **_CVZO},            # 16 s16 ST described the interior
    {"img": "CORNER2013", **_CVZ},        # 17 s17 300 ft counter
    {"img": "CORNER2013", **_CVZO},       # 18 s18 supervision galleries
    {"img": "HERO", **_CVZ},              # 19 s19 subway to the Post Office pier
    {"img": "HERO", **_CVZO},             # 20 s20 launches loaded mail
    {"img": "PO1890", **_CVZO},           # 21 s21 messengers and baskets
    {"img": "R1973", **_CVZ},             # 22 s22 the quirk: HQ stays in KL
    {"img": "MODERN2018", **_CVZO},       # 23 s23 grandest post office in Malaya
    {"img": "R1973", **_CVZO},            # 24 s24 many tenants, a small town
    {"img": "SHENTON", **_LTBO},          # 25 s25 Feb 1942, makeshift hospital
    {"img": "OIL1942", **_CVZ},           # 26 s26 after the surrender
    {"img": "R1973", **_CVZ},             # 27 s27 in peacetime
    {"img": "R1973", **_CVZO},            # 28 s28 PO, Marine Dept, government offices
    {"img": "LANTERN2011", **_CVZO},      # 29 s29 14 Dec 1958, beacon lit
    {"img": "LANTERN2011", **_CVZ},       # 30 s30 Stone-Chance, Fort Canning light
    {"img": "LANTERN2011", **_CVZO},      # 31 s31 why a light on a post office
    {"img": "R1973", **_CVZ},             # 32 s32 the light did not last
    {"img": "R1973", **_CVZO},            # 33 s33 Fort Canning overtaken, towers
    {"img": "LANTERN2011", **_CVZ},       # 34 s34 Bedok Lighthouse, 1978
    {"img": "LANTERN2021", **_LTBO},      # 35 s35 sources differ, 1978/1979
    {"img": "LANTERN2021", **_LTB},       # 36 s36 the lantern survived
    {"img": "LANTERN2011", **_CVZO},      # 37 s37 Maritime Museum, HarbourFront, Mapletree
    {"img": "MODERN2018", **_CVZ},        # 38 s38 GPO moved out, March 1996
    {"img": "MODERN2018", **_CVZO},       # 39 s39 Sino Land, hotel opens 2001
    {"img": "CORNER2013", **_CVZ},        # 40 s40 national monument, 2015
    {"img": "CORNER2013", **_CVZO},       # 41 s41 counter, subway, beacon gone
    {"img": "HERO", **_CVZ},              # 42 s42 why it matters today
    {"img": "PO1890", **_CVZ},            # 43 s43 far fewer know
    {"img": "HERO", **_CVZO},             # 44 s44 one of several lives
]

SCHEDULE = [
    (0.0, 0), (4.7, 1), (18.6, 2), (26.975, 3), (39.4, 4),
    (48.45, 5), (55.6, 6), (66.575, 7), (75.75, 8), (89.025, 9),
    (93.575, 10), (107.975, 11), (119.25, 12), (131.525, 13), (144.325, 14),
    (149.2, 15), (163.725, 16), (168.0, 17), (183.75, 18), (195.575, 19),
    (202.525, 20), (211.375, 21), (221.525, 22), (226.9, 23), (241.975, 24),
    (248.4, 25), (261.675, 26), (267.625, 27), (272.25, 28), (283.45, 29),
    (289.175, 30), (304.225, 31), (314.525, 32), (318.25, 33), (329.6, 34),
    (341.65, 35), (347.85, 36), (350.675, 37), (363.575, 38), (371.575, 39),
    (383.2, 40), (391.05, 41), (398.275, 42), (406.925, 43), (420.0, 44),
]
TOTAL_DURATION = 427.3
TIMING_JSON = "audio/the-fullerton-building-the-post-office-with-a-lighthouse-on-the-roof.timing.json"
