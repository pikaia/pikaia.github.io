"""Video config for the P.S. Hunter post.

Six images: the Tiong Bahru flat that resulted from his 1925
recommendation, two newspaper clippings Chris retrieved via NLB (the
1939 Middleton Hospital farewell group photo, and the 1952 father-son
reunion photo - the clearest surviving likeness of Hunter himself), a
c.1900 photo of the hospital where he died, a 1901 scientific
illustration of Anopheles mosquito anatomy for the malaria section,
and a modern Aedes aegypti photo for the present-day dengue/Wolbachia
closing beat.

  HERO       - Art Deco SIT corner flat, Tiong Poh Road, Tiong Bahru
  MIDDLETON  - "Middleton Hospital Farewell To Dr. Hunter" clipping, 1939
  SGH        - Singapore General Hospital, circa 1900
  FATHERSON  - father-son reunion photo, The Straits Budget, 1952
  ANOPHELES  - Anopheles mosquito anatomy, Journal of Hygiene, 1901
  AEDES      - Aedes aegypti mosquito, modern photo

The two newspaper clippings and the label-heavy 1901 diagram use
letterbox (cover would crop their printed text); the rest are
landscape photos and use cover.

Sentence 40 (the "mosquito fight never stopped" / malaria-to-dengue
sentence, 35s alone) is split across two slides mid-sentence - a plain
single slide there tripped the 30s long-hold check.

43 slides, 520.725s.
"""

_U = "https://upload.wikimedia.org/wikipedia/commons"
_C = f"{_U}/thumb"

IMAGES = {
    "HERO": f"{_U}/8/8d/Tiong_Bahru_11%2C_Jul_06.JPG",
    "MIDDLETON": "/assets/images/middleton-hospital-farewell-hunter-1939.jpg",
    "SGH": f"{_U}/6/6b/KITLV_-_50201_-_Lambert_%26_Co.%2C_G.R._-_Singapore_-_General_Hospital_in_Singapore_-_circa_1900.jpg",
    "FATHERSON": "/assets/images/ps-hunter-father-son-1952.jpg",
    "ANOPHELES": f"{_C}/b/b2/Life_cycle_%26_anatomy_of_Anopheles_mosquito%2C_1901_Wellcome_L0037512.jpg/1280px-Life_cycle_%26_anatomy_of_Anopheles_mosquito%2C_1901_Wellcome_L0037512.jpg",
    "AEDES": f"{_U}/2/2c/Aedes_aegypti_CDC-Gathany.jpg",
}

_CVZ = {"type": "cover", "zoom": [1.0, 1.06, 1.12], "pan": [(0.5, 0.5)] * 3, "ease": "ease-in-out"}
_CVZO = {"type": "cover", "zoom": [1.12, 1.06, 1.0], "pan": [(0.5, 0.5)] * 3, "ease": "ease-out"}
_LTB = {"type": "letterbox", "zoom": [1.0, 1.04, 1.08], "pan": [(0.5, 0.5)] * 3, "ease": "ease-in-out"}
_LTBO = {"type": "letterbox", "zoom": [1.08, 1.04, 1.0], "pan": [(0.5, 0.5)] * 3, "ease": "ease-out"}

SLIDES = [
    {"img": "HERO", **_CVZ},        # 0  s0   title
    {"img": "HERO", **_CVZO},       # 1  s1   Tiong Bahru Art Deco description
    {"img": "HERO", **_CVZ},        # 2  s2   name barely survives
    {"img": "HERO", **_CVZO},       # 3  s3   actual name confirmed
    {"img": "HERO", **_CVZ},        # 4  s4   joined health service 1913
    {"img": "MIDDLETON", **_LTB},   # 5  s5   bacteriologist at Middleton
    {"img": "HERO", **_CVZO},       # 6  s6   SVC commission, 1914
    {"img": "HERO", **_CVZ},        # 7  s7   son born 1915, Leonie Hill Road
    {"img": "HERO", **_CVZO},       # 8  s8   mid-1920s, Municipal Health Officer
    {"img": "HERO", **_CVZ},        # 9  s9   Chinatown overcrowding
    {"img": "HERO", **_CVZO},       # 10 s10  1925, recommended a suburb
    {"img": "HERO", **_CVZ},        # 11 s11  the recommendation had consequences
    {"img": "HERO", **_CVZO},       # 12 s12  SIT established, 1927
    {"img": "HERO", **_CVZ},        # 13 s13  Dec 1936, flats occupied
    {"img": "HERO", **_CVZO},       # 14 s14  template for public housing
    {"img": "ANOPHELES", **_LTB},   # 15 s15  housing wasn't Hunter's only fight
    {"img": "ANOPHELES", **_LTBO},  # 16 s16  anti-malaria campaign, 1911, Watson
    {"img": "ANOPHELES", **_LTB},   # 17 s17  1930s, Hunter's own job
    {"img": "ANOPHELES", **_LTBO},  # 18 s18  Dec 1935, the ludlowi mosquito
    {"img": "ANOPHELES", **_LTB},   # 19 s19  Hunter reassuring readers
    {"img": "ANOPHELES", **_LTBO},  # 20 s20  May 1936, on leave
    {"img": "ANOPHELES", **_LTB},   # 21 s21  annual report, thanked the press
    {"img": "ANOPHELES", **_LTBO},  # 22 s22  Malaya free of recurrence since 1911
    {"img": "HERO", **_CVZ},        # 23 s23  1937 Coronation Honours
    {"img": "HERO", **_CVZO},       # 24 s24  1948, Turf Club, C.B.E.
    {"img": "HERO", **_CVZ},        # 25 s25  retired, 10 March 1939
    {"img": "MIDDLETON", **_LTB},   # 26 s26  the send-off was substantial
    {"img": "MIDDLETON", **_LTBO},  # 27 s27  the Middleton Hospital visit
    {"img": "MIDDLETON", **_LTB},   # 28 s28  a group photograph was taken
    {"img": "HERO", **_CVZO},       # 29 s29  farewell dinner at Mr. N. A. Sen's
    {"img": "HERO", **_CVZ},        # 30 s30  the farewell interview
    {"img": "HERO", **_CVZO},       # 31 s31  retirement didn't mean leaving
    {"img": "HERO", **_CVZ},        # 32 s32  stayed on, chaired the Turf Club
    {"img": "FATHERSON", **_LTB},   # 33 s33  March 1952, his son's visit
    {"img": "FATHERSON", **_LTBO},  # 34 s34  three papers ran the reunion photo
    {"img": "SGH", **_CVZ},         # 35 s35  died, Singapore General Hospital, 1954
    {"img": "SGH", **_CVZO},        # 36 s36  the obituary
    {"img": "HERO", **_CVZ},        # 37 s37  why it matters today - a stretch
    {"img": "HERO", **_CVZO},       # 38 s38  but the direction was set here
    {"img": "HERO", **_CVZ},        # 39 s39  Hunter's own office, institutional ancestor
    {"img": "AEDES", **_CVZ},       # 40 s40a mosquito fight never stopped / malaria-to-dengue
    {"img": "AEDES", **_CVZO},      # 41 s40b ...Project Wolbachia, sterilising the population
    {"img": "HERO", **_CVZO},       # 42 s41  Tiong Bahru still stands, closing
]

SCHEDULE = [
    (0.000, 0), (5.400, 1), (23.025, 2), (34.475, 3), (45.600, 4),
    (57.075, 5), (70.825, 6), (85.525, 7), (100.550, 8), (112.250, 9),
    (120.450, 10), (137.625, 11), (141.525, 12), (158.475, 13), (173.475, 14),
    (181.975, 15), (185.225, 16), (202.900, 17), (211.875, 18), (226.350, 19),
    (240.025, 20), (251.800, 21), (265.950, 22), (277.375, 23), (289.250, 24),
    (298.875, 25), (306.250, 26), (309.000, 27), (328.250, 28), (331.750, 29),
    (337.425, 30), (358.500, 31), (361.250, 32), (378.300, 33), (398.150, 34),
    (408.075, 35), (417.075, 36), (434.150, 37), (452.850, 38), (455.550, 39),
    (471.900, 40), (485.130, 41), (506.925, 42),
]
TOTAL_DURATION = 520.725
TIMING_JSON = "audio/peter-sinclair-hunter-the-health-officer-whose-one-report-built-tiong-bahru.timing.json"
