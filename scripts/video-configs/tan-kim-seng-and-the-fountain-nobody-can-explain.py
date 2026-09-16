"""Video config for the Tan Kim Seng post.

Six images - a workable but not richly-photographed topic (no
contemporary 1850s-1880s photo of Tan Kim Seng himself survives; the
only period likeness is a mid-19th-century ancestor portrait).

  PORTRAIT  - Ancestor portrait of Tan Kim Seng, Asian Civilisations
              Museum (Commons) - the only period likeness of the man
  FULLERTON - The fountain at its original site, Fullerton Square,
              circa 1900 (Commons, G.R. Lambert & Co.) - its first home
  MODERN    - The fountain today, at Esplanade Park (Commons, 2026) -
              carries most of the runtime as the "present-day landmark"
  ALTAR     - Tan Kim Seng's own ancestral altar, Peranakan Museum
              (Commons) - family/legacy beat
  BRIDGE    - Tan Kim Seng Bridge over the Melaka River, Malacca
              (Commons) - his son's own philanthropy, back in Malacca
  JIAKKIM   - Portrait of his grandson Tan Jiak Kim, 1900 (Commons) -
              the King Edward VII College of Medicine beat

PORTRAIT and JIAKKIM are period portraits and read better letterboxed
(faces near the frame edge shouldn't be cropped by cover); FULLERTON,
MODERN, ALTAR and BRIDGE are ordinary landscape photos and use cover.

26 slides, 346.575s.
"""

_U = "https://upload.wikimedia.org/wikipedia/commons"

IMAGES = {
    "PORTRAIT": f"{_U}/a/a1/Qu_Chiqing%2C_Ancestor_portrait_of_Tan_Kim_Seng%2C_Mid_19th_century%2C_Oil_on_canvas%2C_98_x_78_cm%2C_Asian_Civilisations_Museum.png",
    "FULLERTON": f"{_U}/1/16/Photographic_Views_of_Singapore_Plate_08_Street_Scenery.jpg",
    "MODERN": f"{_U}/c/c9/Tan_Kim_Seng_Fountain%2C_2026_01.jpg",
    "ALTAR": f"{_U}/9/9d/Ancestral_altar_of_Tan_Kim_Seng_ca_1860_IMG_9773_singapore_peranakan_museum.jpg",
    "BRIDGE": f"{_U}/5/55/Tan_Kim_Seng_Bridge_1.jpg",
    "JIAKKIM": f"{_U}/2/23/Tan_Jiak_Kim.jpg",
}

_CVZ = {"type": "cover", "zoom": [1.0, 1.06, 1.12], "pan": [(0.5, 0.5)] * 3, "ease": "ease-in-out"}
_CVZO = {"type": "cover", "zoom": [1.12, 1.06, 1.0], "pan": [(0.5, 0.5)] * 3, "ease": "ease-out"}
_LTB = {"type": "letterbox", "zoom": [1.0, 1.04, 1.08], "pan": [(0.5, 0.5)] * 3, "ease": "ease-in-out"}
_LTBO = {"type": "letterbox", "zoom": [1.08, 1.04, 1.0], "pan": [(0.5, 0.5)] * 3, "ease": "ease-out"}

SLIDES = [
    {"img": "PORTRAIT", **_LTB},     # 0  s0   title
    {"img": "MODERN", **_CVZ},       # 1  s1   ornate fountain has stood
    {"img": "MODERN", **_CVZO},      # 2  s2   joggers and tourists pass it
    {"img": "MODERN", **_CVZ},       # 3  s3   almost none stop to read
    {"img": "PORTRAIT", **_LTBO},    # 4  s4   born 1805, Dutch Malacca
    {"img": "PORTRAIT", **_LTB},     # 5  s5   Kim Seng & Company, 1840
    {"img": "PORTRAIT", **_LTBO},    # 6  s6   JP 1850, Municipal Commission
    {"img": "PORTRAIT", **_LTB},     # 7  s7   1854 Hokkien-Teochew riots
    {"img": "ALTAR", **_CVZO},       # 8  s8   Chong Wen Ge, Tan Tock Seng Hospital
    {"img": "MODERN", **_CVZ},       # 9  s9   none of that put his name on a fountain
    {"img": "MODERN", **_CVZO},      # 10 s10  18 Nov 1857, $13,000 offer
    {"img": "MODERN", **_CVZ},       # 11 s11  government bungled it
    {"img": "MODERN", **_CVZO},      # 12 s12  earthenware pipes, Kandang Kerbau
    {"img": "PORTRAIT", **_LTB},     # 13 s13  waterworks 1877, Tan died 1864
    {"img": "FULLERTON", **_CVZO},   # 14 s14  Municipal Commissioners built fountain 1882
    {"img": "FULLERTON", **_CVZ},    # 15 s15  Andrew Handyside & Co.
    {"img": "FULLERTON", **_CVZO},   # 16 s16  stayed until Fullerton Square redeveloped
    {"img": "MODERN", **_CVZ},       # 17 s17  1929 removal, rebuilt at Esplanade Park
    {"img": "MODERN", **_CVZO},      # 18 s18  gazetted 2010, restored twice
    {"img": "ALTAR", **_CVZ},        # 19 s19  his own philanthropy didn't end with him
    {"img": "BRIDGE", **_CVZO},      # 20 s20  son Tan Beng Swee, Malacca
    {"img": "JIAKKIM", **_LTB},      # 21 s21  grandson Tan Jiak Kim, King Edward VII College
    {"img": "MODERN", **_CVZ},       # 22 s22  three generations, the fountain most people photograph
    {"img": "MODERN", **_CVZO},      # 23 s23  why it matters today
    {"img": "JIAKKIM", **_LTBO},     # 24 s24  lasting result: civic institutions
    {"img": "MODERN", **_CVZ},       # 25 s25  Marina Barrage and Linggiu finished telling
]

SCHEDULE = [
    (0.0, 0), (4.0, 1), (27.925, 2), (32.175, 3), (39.15, 4),
    (47.325, 5), (61.725, 6), (79.625, 7), (102.975, 8), (118.925, 9),
    (122.95, 10), (140.15, 11), (146.625, 12), (162.075, 13), (177.6, 14),
    (185.075, 15), (202.475, 16), (210.95, 17), (229.9, 18), (253.475, 19),
    (258.1, 20), (267.875, 21), (289.175, 22), (304.925, 23), (319.025, 24),
    (337.05, 25),
]
TOTAL_DURATION = 346.575
TIMING_JSON = "audio/tan-kim-seng-and-the-fountain-nobody-can-explain.timing.json"
