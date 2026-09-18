"""Video config for the "Banana Money" post.

Five banknote scans - the entire post is about the notes themselves, so
the image pool is inherently the denominations sourced for the post and
gallery. HERO and CENT1 are near-square scans (front+back stacked) and
read better letterboxed; DOLLAR1, THOUSAND and HUNDRED are ordinary
landscape note scans and use cover.

  HERO      - $10 note, 1944 (Commons, Smithsonian/Godot13) - the
              banana-tree design that gave the currency its name
  DOLLAR1   - $1 note, 1942 (Commons, Slleong) - an early, low
              denomination from before the inflation took hold
  THOUSAND  - $1,000 note, 1945 (Commons, Makthorpe) - the currency's
              final, absurd top denomination
  HUNDRED   - $100 note, 1944 (Commons, Jacklee; gallery-only in the
              post) - mid-inflation denomination, the egg/rice beats
  CENT1     - 1-cent note, 1942 (Commons, Smithsonian/Godot13;
              gallery-only in the post) - the smallest denomination
              issued

30 slides, 293.65s.
"""

_U = "https://upload.wikimedia.org/wikipedia/commons"

IMAGES = {
    "HERO": f"{_U}/b/ba/MAL-M7c-Malaya-Japanese_Occupation-10_Dollars_ND_%281944%29.jpg",
    "DOLLAR1": f"{_U}/5/5a/One_dollar_note_issued_by_the_Japanese_Government_during_the_occupation_of_Malaya%2C_North_Borneo%2C_Sarawak_and_Brunei_%281942%2C_obverse%29_-_02.jpg",
    "THOUSAND": f"{_U}/f/f2/One_thousand_dollar_note_issued_by_the_Japanese_Government_during_the_occupation_of_Malaya%2C_North_Borneo%2C_Sarawak_and_Brunei_%281944%2C_obverse%29_-_02.jpg",
    "HUNDRED": f"{_U}/9/9d/One_hundred_dollar_note_issued_by_the_Japanese_Government_during_the_occupation_of_Malaya%2C_North_Borneo%2C_Sarawak_and_Brunei_%281944%2C_obverse%29.jpg",
    "CENT1": f"{_U}/a/a8/MAL-M1b-Malaya-Japanese_Occupation-One_Cent_ND_%281942%29.jpg",
}

_CVZ = {"type": "cover", "zoom": [1.0, 1.06, 1.12], "pan": [(0.5, 0.5)] * 3, "ease": "ease-in-out"}
_CVZO = {"type": "cover", "zoom": [1.12, 1.06, 1.0], "pan": [(0.5, 0.5)] * 3, "ease": "ease-out"}
_LTB = {"type": "letterbox", "zoom": [1.0, 1.04, 1.08], "pan": [(0.5, 0.5)] * 3, "ease": "ease-in-out"}
_LTBO = {"type": "letterbox", "zoom": [1.08, 1.04, 1.0], "pan": [(0.5, 0.5)] * 3, "ease": "ease-out"}

SLIDES = [
    {"img": "HERO", **_LTB},          # 0  s0   title
    {"img": "HERO", **_LTBO},         # 1  s1   sells today for a few dollars
    {"img": "HERO", **_LTB},          # 2  s2   note promises pay the bearer
    {"img": "DOLLAR1", **_CVZO},      # 3  s3   it never did
    {"img": "THOUSAND", **_CVZ},      # 4  s4   worth exactly... to worth nothing
    {"img": "DOLLAR1", **_CVZ},       # 5  s5   after Singapore fell, 1942
    {"img": "CENT1", **_LTB},         # 6  s6   earliest notes, anti-counterfeiting
    {"img": "HERO", **_LTBO},         # 7  s7   banana tree design, nickname
    {"img": "CENT1", **_LTBO},        # 8  s8   Malays had their own name
    {"img": "DOLLAR1", **_CVZO},      # 9  s9   problem was never the design
    {"img": "HUNDRED", **_CVZ},       # 10 s10  nothing backed the currency
    {"img": "DOLLAR1", **_CVZ},       # 11 s11  no gold, no silver, no limit
    {"img": "CENT1", **_LTB},         # 12 s12  security features first to go
    {"img": "HUNDRED", **_CVZO},      # 13 s13  new larger denominations
    {"img": "HUNDRED", **_CVZ},       # 14 s14  results were exactly what
    {"img": "HUNDRED", **_CVZO},      # 15 s15  egg 3 cents to $100
    {"img": "HUNDRED", **_CVZ},       # 16 s16  rice $5 to $5,000
    {"img": "THOUSAND", **_CVZO},     # 17 s17  $4,000 million issued
    {"img": "THOUSAND", **_CVZ},      # 18 s18  8 September 1945, no value
    {"img": "THOUSAND", **_CVZO},     # 19 s19  no exchange rate
    {"img": "DOLLAR1", **_CVZO},      # 20 s20  pre-war dollars honoured
    {"img": "THOUSAND", **_CVZ},      # 21 s21  savings only in banana money
    {"img": "HERO", **_LTB},          # 22 s22  Japan never compensated
    {"img": "HUNDRED", **_CVZO},      # 23 s23  what happened to the paper
    {"img": "HUNDRED", **_CVZ},       # 24 s24  400 tons, 20,000 cases
    {"img": "CENT1", **_LTBO},        # 25 s25  repulped into newsprint
    {"img": "HERO", **_LTBO},         # 26 s26  became the paper people read
    {"img": "DOLLAR1", **_CVZ},       # 27 s27  demonetisation, legal mess
    {"img": "HERO", **_LTB},          # 28 s28  why it matters today
    {"img": "HERO", **_LTBO},         # 29 s29  never really money
]

SCHEDULE = [
    (0.0, 0), (4.675, 1), (21.325, 2), (28.0, 3), (29.85, 4),
    (40.25, 5), (54.55, 6), (64.275, 7), (72.725, 8), (80.5, 9),
    (83.7, 10), (97.425, 11), (101.0, 12), (114.2, 13), (128.675, 14),
    (133.225, 15), (140.125, 16), (147.25, 17), (166.225, 18), (181.65, 19),
    (189.55, 20), (198.725, 21), (205.15, 22), (210.275, 23), (215.575, 24),
    (228.4, 25), (234.9, 26), (243.2, 27), (266.6, 28), (278.1, 29),
]
TOTAL_DURATION = 293.65
TIMING_JSON = "audio/banana-money-the-wartime-currency-that-inflated-to-nothing.timing.json"
