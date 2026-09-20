"""Video config for the 1915 Singapore Mutiny post.

Eight images. The pool is genuinely thin (Commons has almost nothing
from the mutiny itself), so images repeat on purpose. OTOWA, MONTCALM and
TABLET are ordinary landscape photos/illustrations and use cover; the
rest are portrait scans, a captioned news illustration, a grainy print
or newspaper pages, and use letterbox. The grainy execution line-up
photo from the gallery is deliberately NOT used in the video (sober
choice for an autoplaying format).

  SAILORS   - "Review of Japanese sailors after the mutiny at Singapore,"
              H. W. Wilson, The Great War, 1916 (Commons)
  HAV       - Lovett watercolour of a Musalman Rajput havildar of the
              5th Light Infantry (Commons, National Army Museum)
  ST17      - The Straits Times, 17 Feb 1915, page 10 (whole page, local
              scan, NewspaperSG / SPH, public domain by age)
  ST26      - The Straits Times, 26 Mar 1915, page 7 (whole page, local
              scan, same basis)
  OTOWA     - Japanese cruiser Otowa (Commons)
  MONTCALM  - French cruiser Montcalm, Page's Magazine 1902 (Commons)
  OUTRAM    - Outram (Pearl's Hill) Prison, 1850s (Commons)
  TABLET    - 1915 mutiny memorial tablet, Victoria Concert Hall, 2014
              (Commons, Smuconlaw)

52 slides, 445.375s.
"""

_U = "https://upload.wikimedia.org/wikipedia/commons"

IMAGES = {
    "SAILORS": f"{_U}/thumb/4/46/REVIEW_OF_JAPANESE_SAILORS_ALTER_THE_MUTINY_AT_SINGAPORE%2C_1915.png/1280px-REVIEW_OF_JAPANESE_SAILORS_ALTER_THE_MUTINY_AT_SINGAPORE%2C_1915.png",
    "HAV": f"{_U}/7/7b/A_Musalman_Rajput_Havildar_of_the_5th_light_infantry_and_a_Jat_Havildar_of_the_6th_Jat_light_infantry.jpg",
    "ST17": "/assets/images/straits-times-1915-02-17-page-10.jpg",
    "ST26": "/assets/images/straits-times-1915-03-26-page-7.jpg",
    "OTOWA": f"{_U}/thumb/c/c7/Japanese_cruiser_Otowa.jpg/1280px-Japanese_cruiser_Otowa.jpg",
    "MONTCALM": f"{_U}/thumb/6/6d/Cruiser_Montcalm_-_Page%27s_Magazine_1902.png/1280px-Cruiser_Montcalm_-_Page%27s_Magazine_1902.png",
    "OUTRAM": f"{_U}/thumb/5/54/Photograph_of_Outram_Prison_%28Pearl%E2%80%99s_Hill_Prison%29_in_the_1850%27s.jpg/1280px-Photograph_of_Outram_Prison_%28Pearl%E2%80%99s_Hill_Prison%29_in_the_1850%27s.jpg",
    "TABLET": f"{_U}/thumb/a/ad/1915_Singapore_Mutiny_memorial_tablet%2C_Victoria_Concert_Hall%2C_Singapore_-_20140926.jpg/1280px-1915_Singapore_Mutiny_memorial_tablet%2C_Victoria_Concert_Hall%2C_Singapore_-_20140926.jpg",
}

_CVZ = {"type": "cover", "zoom": [1.0, 1.06, 1.12], "pan": [(0.5, 0.5)] * 3, "ease": "ease-in-out"}
_CVZO = {"type": "cover", "zoom": [1.12, 1.06, 1.0], "pan": [(0.5, 0.5)] * 3, "ease": "ease-out"}
_LTB = {"type": "letterbox", "zoom": [1.0, 1.04, 1.08], "pan": [(0.5, 0.5)] * 3, "ease": "ease-in-out"}
_LTBO = {"type": "letterbox", "zoom": [1.08, 1.04, 1.0], "pan": [(0.5, 0.5)] * 3, "ease": "ease-out"}

SLIDES = [
    {"img": "SAILORS", **_LTB},       # 0  s0  title
    {"img": "HAV", **_LTB},           # 1  s1  afternoon of 15 Feb, Alexandra Barracks
    {"img": "HAV", **_LTBO},          # 2  s2  by evening turned their rifles
    {"img": "SAILORS", **_LTBO},      # 3  s3  warships from Japan, France, Russia
    {"img": "HAV", **_LTB},           # 4  s4  a Muslim regiment of the Indian Army
    {"img": "HAV", **_LTBO},          # 5  s5  reached Singapore Oct 1914
    {"img": "HAV", **_LTB},           # 6  s6  told they would go to Hong Kong
    {"img": "HAV", **_LTBO},          # 7  s7  rumours of the Ottoman front
    {"img": "HAV", **_LTB},           # 8  s8  court of inquiry, causes
    {"img": "HAV", **_LTBO},          # 9  s9  historians still argue
    {"img": "HAV", **_LTB},           # 10 s10 3.30 pm, four companies rose
    {"img": "TABLET", **_CVZ},        # 11 s11 Boyce and Elliott killed
    {"img": "HAV", **_LTBO},          # 12 s12 Tanglin camp attacked
    {"img": "HAV", **_LTB},           # 13 s13 35 Germans escaped
    {"img": "TABLET", **_CVZO},       # 14 s14 civilians among the dead
    {"img": "HAV", **_LTBO},          # 15 s15 siege of the bungalow
    {"img": "ST17", **_LTB},          # 16 s16 martial law
    {"img": "ST17", **_LTBO},         # 17 s17 funeral at Bidadari
    {"img": "ST17", **_LTB},          # 18 s18 two lorries and a hearse
    {"img": "ST17", **_LTBO},         # 19 s19 list covered civilians only
    {"img": "ST17", **_LTB},          # 20 s20 toll between 36 and 44
    {"img": "SAILORS", **_LTB},       # 21 s21 help came from outside
    {"img": "MONTCALM", **_CVZ},      # 22 s22 ships arrived
    {"img": "OTOWA", **_CVZ},         # 23 s23 landing parties
    {"img": "SAILORS", **_LTBO},      # 24 s24 432 captured by evening
    {"img": "SAILORS", **_LTB},       # 25 s25 Shropshires arrived 20 Feb
    {"img": "HAV", **_LTB},           # 26 s26 fled into Johor
    {"img": "OTOWA", **_CVZO},        # 27 s27 largely over within a week
    {"img": "OUTRAM", **_LTB},        # 28 s28 over 200 court-martialled
    {"img": "OUTRAM", **_LTBO},       # 29 s29 47 executed, 64 transported
    {"img": "OUTRAM", **_LTB},        # 30 s30 outside Outram Road Prison
    {"img": "ST26", **_LTB},          # 31 s31 ST described the largest batch
    {"img": "ST26", **_LTBO},         # 32 s32 25 March sentences read
    {"img": "ST26", **_LTB},          # 33 s33 crowd of 15,000
    {"img": "ST26", **_LTBO},         # 34 s34 firing party of 110
    {"img": "OUTRAM", **_LTBO},       # 35 s35 other accounts, disputed
    {"img": "OUTRAM", **_LTB},        # 36 s36 records sealed 50 years
    {"img": "HAV", **_LTBO},          # 37 s37 regiment left, disbanded 1922
    {"img": "HAV", **_LTB},           # 38 s38 Criminal Intelligence Department
    {"img": "TABLET", **_CVZ},        # 39 s39 few marks on the city
    {"img": "TABLET", **_CVZO},       # 40 s40 memorial tablets
    {"img": "OUTRAM", **_LTBO},       # 41 s41 no memorial to the executed
    {"img": "TABLET", **_CVZ},        # 42 s42 historians frame it differently
    {"img": "TABLET", **_CVZO},       # 43 s43 law and tension
    {"img": "HAV", **_LTBO},          # 44 s44 Sedition Act repealed, new Act
    {"img": "TABLET", **_CVZ},        # 45 s45 housing and electoral rules
    {"img": "HAV", **_LTB},           # 46 s46 state cites 1964 and 1969
    {"img": "TABLET", **_CVZO},       # 47 s47 critics, free expression
    {"img": "HAV", **_LTBO},          # 48 s48 no official speech cites 1915
    {"img": "TABLET", **_CVZ},        # 49 s49 an earlier episode
    {"img": "SAILORS", **_LTBO},      # 50 s50 why it matters today
    {"img": "TABLET", **_CVZO},       # 51 s51 lessons still argued
]

SCHEDULE = [
    (0.0, 0), (6.375, 1), (23.875, 2), (30.1, 3), (36.65, 4),
    (45.025, 5), (57.5, 6), (63.325, 7), (74.975, 8), (91.45, 9),
    (103.675, 10), (108.725, 11), (114.85, 12), (124.925, 13), (130.2, 14),
    (133.1, 15), (138.775, 16), (142.3, 17), (153.8, 18), (158.1, 19),
    (164.4, 20), (172.375, 21), (175.25, 22), (185.35, 23), (202.425, 24),
    (209.025, 25), (214.55, 26), (220.2, 27), (227.65, 28), (231.2, 29),
    (241.325, 30), (250.725, 31), (254.4, 32), (267.225, 33), (273.775, 34),
    (285.575, 35), (292.625, 36), (297.025, 37), (305.075, 38), (317.15, 39),
    (320.525, 40), (333.55, 41), (338.85, 42), (351.275, 43), (357.725, 44),
    (380.65, 45), (385.85, 46), (400.45, 47), (409.075, 48), (414.55, 49),
    (423.625, 50), (435.75, 51),
]
TOTAL_DURATION = 445.375
TIMING_JSON = "audio/the-1915-singapore-mutiny-the-week-a-regiment-rose-on-chinese-new-year.timing.json"
