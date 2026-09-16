"""Video config for the Cathay Building post.

Eight images - reorganized 2026-09-16 to fold in three photos added to
the post/gallery after the first pass (THEATRE1945, HARBOUR1945,
NIGHT2013), spreading the wartime section across more than just HERO
repeated (was 9 uses, now 5).

  HERO         - The Cathay Building, 1945 (Commons, Australian War
                 Memorial) - the general period likeness spanning
                 construction through the Occupation
  THEATRE1945  - The Cathay Theatre's street-level entrance, 1945
                 (Commons, AWM) - portrait scan, English-language
                 marquee visible (postwar/liberation era, not
                 mid-Occupation)
  HARBOUR1945  - Allied ships in Singapore harbour, photographed from
                 the Cathay itself, 1945 (Commons, NIGIS) - "not long
                 after the Japanese surrender" per its own caption
  NIGHT        - Cathay Cinema and Hotel by night, 1954 (Commons,
                 Powerhouse Museum) - the neon-lit cinema/hotel era
  DAY          - Cathay Cinema and Hotel by day, 1954 (Commons,
                 Powerhouse Museum) - daytime companion, postwar
                 civilian life
  AERIAL       - Bird's-eye view of Bras Basah Road from the Cathay
                 Building itself, 1976 (Commons, MITA) - a last look
                 from the tower before its interior was gone for good
  MODERN       - The Cathay today, October 2025 (Commons) - present-day
                 facade-in-front-of-a-mall payoff
  NIGHT2013    - The Luxe, Cathay and SOTA at night, 2013 (Commons,
                 Erwin Soo) - wide panorama, the building alive amid
                 its present-day surroundings

HERO and THEATRE1945 are portrait/near-square scans and read better
letterboxed; the rest are ordinary landscape photos (NIGHT2013 is a
wide panorama, cropped by cover the same as any other landscape
source) and use cover.

21 slides, 281.15s.
"""

_U = "https://upload.wikimedia.org/wikipedia/commons"

IMAGES = {
    "HERO": f"{_U}/5/57/The_Cathay_Building_in_Singapore_1945.jpg",
    "THEATRE1945": f"{_U}/c/c9/The_Cathay_Theatre_in_Singapore_1945.jpg",
    "HARBOUR1945": f"{_U}/thumb/4/45/Geallieerde_schepen_in_de_haven_van_Singapore%2C_gefotografeerd_vanaf_de_Cathay%2C_een_van_Singapore_%27s_modernste_gebouwen%2C_dat_door_de_Japanners_als_hoofdkwartier_werd_gebruikt%2C_KITLV_25399.tiff/lossy-page1-1280px-Geallieerde_schepen_in_de_haven_van_Singapore%2C_gefotografeerd_vanaf_de_Cathay%2C_een_van_Singapore_%27s_modernste_gebouwen%2C_dat_door_de_Japanners_als_hoofdkwartier_werd_gebruikt%2C_KITLV_25399.tiff.jpg",
    "NIGHT": f"{_U}/f/f1/Cathay_Cinema_and_Hotel_by_night%2C_Singapore%2C_1954_%284435981577%29.jpg",
    "DAY": f"{_U}/9/96/Cathay_Cinema_and_Hotel_by_day%2C_Singapore%2C_1954_%284435980883%29.jpg",
    "AERIAL": f"{_U}/f/f0/Bird%27s_eye_of_Bras_Basah_Road_from_Cathay_Building%2C_Shaw_Tower_in_the_background.jpg",
    "MODERN": f"{_U}/c/cf/The_Cathay%2C_October_2025.jpg",
    "NIGHT2013": f"{_U}/thumb/d/dd/The_Luxe%2C_Cathay_and_SOTA%2C_2013.jpg/1280px-The_Luxe%2C_Cathay_and_SOTA%2C_2013.jpg",
}

_CVZ = {"type": "cover", "zoom": [1.0, 1.06, 1.12], "pan": [(0.5, 0.5)] * 3, "ease": "ease-in-out"}
_CVZO = {"type": "cover", "zoom": [1.12, 1.06, 1.0], "pan": [(0.5, 0.5)] * 3, "ease": "ease-out"}
_LTB = {"type": "letterbox", "zoom": [1.0, 1.04, 1.08], "pan": [(0.5, 0.5)] * 3, "ease": "ease-in-out"}
_LTBO = {"type": "letterbox", "zoom": [1.08, 1.04, 1.0], "pan": [(0.5, 0.5)] * 3, "ease": "ease-out"}

SLIDES = [
    {"img": "HERO", **_LTB},          # 0  s0   title
    {"img": "MODERN", **_CVZ},        # 1  s1   corner of Handy Road and Dhoby Ghaut
    {"img": "MODERN", **_CVZO},       # 2  s2   most people walking under it
    {"img": "HERO", **_LTBO},         # 3  s3   privately financed, Dato Loke Wan Tho
    {"img": "THEATRE1945", **_LTB},   # 4  s4   Cathay Cinema opened, tallest building
    {"img": "NIGHT", **_CVZ},         # 5  s5   first fully air-conditioned
    {"img": "DAY", **_CVZO},          # 6  s6   complex grew, penthouse
    {"img": "HERO", **_LTBO},         # 7  s7   British military requisitioned, radar
    {"img": "HERO", **_LTB},          # 8  s8   height made it useful to two armies
    {"img": "HARBOUR1945", **_CVZ},   # 9  s9   15 Feb 1942, flag signal
    {"img": "HERO", **_LTB},          # 10 s10  Daitoa Gekijo, Radio Syonan
    {"img": "THEATRE1945", **_LTBO},  # 11 s11  Oct 1943, Subhas Chandra Bose
    {"img": "HARBOUR1945", **_CVZO},  # 12 s12  1945, Mountbatten SEAC HQ
    {"img": "DAY", **_CVZ},           # 13 s13  civilian life came back slowly
    {"img": "NIGHT", **_CVZO},        # 14 s14  Cathay Restaurant, hotel 1954-1970
    {"img": "DAY", **_CVZ},           # 15 s15  1978 renovation, Picturehouse
    {"img": "DAY", **_CVZO},          # 16 s16  1999 rebuild decided, closed 2000
    {"img": "AERIAL", **_LTB},        # 17 s17  demolition 2003, gazetted monument
    {"img": "MODERN", **_CVZ},        # 18 s18  everything behind the facade is new
    {"img": "NIGHT2013", **_CVZO},    # 19 s19  why it matters today
    {"img": "MODERN", **_CVZ},        # 20 s20  monument status, didn't save the building
]

SCHEDULE = [
    (0.0, 0), (3.975, 1), (15.4, 2), (33.525, 3), (54.625, 4),
    (68.825, 5), (80.45, 6), (92.425, 7), (110.575, 8), (117.1, 9),
    (135.0, 10), (147.675, 11), (164.925, 12), (177.4, 13), (180.5, 14),
    (197.625, 15), (208.825, 16), (222.75, 17), (239.675, 18), (251.95, 19),
    (269.15, 20),
]
TOTAL_DURATION = 281.15
TIMING_JSON = "audio/the-cathay-building-singapores-first-skyscraper.timing.json"
