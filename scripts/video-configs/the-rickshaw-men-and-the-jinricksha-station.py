"""Video config for the rickshaw-men post's Watch widget / main video.

Good image coverage for once: period KITLV photographs of pullers, a
c.1930 Chinatown rickshaw rank, studio and street scenes, the rise-and-
fall chart, and two present-day views of the conserved Jinrikisha
Station.

  PULLER1890  - a puller between the shafts with a passenger, c.1890 (hero)
  PORTRAIT1900 - "Rikisha puller", G.R. Lambert & Co., c.1900 (portrait -> letterbox)
  RANK1930    - a Chinatown rickshaw stand, c.1930
  STUDIO1909  - a European party posed round a rickshaw, the puller at the edge
  CHILDREN    - a puller with two European children, c.1910s
  TEUTONIA    - a rickshaw at the Teutonia Club drive, c.1910
  FINLAYSON   - Finlayson Green junction, c.1910 (wide -> cover, centre crop)
  CHART       - "Rickshaws registered in Singapore, 1883-1947" (letterbox, frozen)
  STATION_FACADE - the Jinrikisha Station's long arcaded facade today
  STATION_TOWER  - the station's corner tower and octagonal cupola today
  TRISHAW     - a modern tourist trishaw on Trengganu Street, 2013

Graphics (CHART) are letterbox and near-frozen, per
docs/production-pipeline.md s3 - cover would crop the labels. Everything
else is centred zoom, no horizontal pan.

30 slides, 494.175s.
"""

_C = "https://upload.wikimedia.org/wikipedia/commons/thumb"

IMAGES = {
    "PULLER1890": f"{_C}/0/09/KITLV_-_377462_-_Bengal_man_in_a_Chinese_rickshaw_at_Singapore_-_circa_1890.tif/lossy-page1-1280px-KITLV_-_377462_-_Bengal_man_in_a_Chinese_rickshaw_at_Singapore_-_circa_1890.tif.jpg",
    "PORTRAIT1900": f"{_C}/5/55/KITLV_-_50189_-_Lambert_%26_Co.%2C_G.R._-_Singapore_-_Chinese_rickshaw_at_Singapore_-_circa_1900.tif/lossy-page1-1280px-KITLV_-_50189_-_Lambert_%26_Co.%2C_G.R._-_Singapore_-_Chinese_rickshaw_at_Singapore_-_circa_1900.tif.jpg",
    "RANK1930": f"{_C}/3/3b/Jinricksha_Station_aan_Neil_Road_te_Singapore%2C_KITLV_104799.tiff/lossy-page1-1280px-Jinricksha_Station_aan_Neil_Road_te_Singapore%2C_KITLV_104799.tiff.jpg",
    "STUDIO1909": f"{_C}/a/a4/Europees_gezelschap_in_en_naast_een_riksja_in_een_fotostudio_te_Singapore%2C_KITLV_10712.tiff/lossy-page1-1280px-Europees_gezelschap_in_en_naast_een_riksja_in_een_fotostudio_te_Singapore%2C_KITLV_10712.tiff.jpg",
    "CHILDREN": f"{_C}/0/0d/Twee_meisjes_in_een_rickshaw%2C_vermoedelijk_in_Singapore%2C_KITLV_43535.tiff/lossy-page1-1280px-Twee_meisjes_in_een_rickshaw%2C_vermoedelijk_in_Singapore%2C_KITLV_43535.tiff.jpg",
    "TEUTONIA": f"{_C}/4/4d/KITLV_-_79905_-_Kleingrothe%2C_C.J._-_Medan_-_Teutonia_Club_in_Singapore_-_circa_1910.tif/lossy-page1-1280px-KITLV_-_79905_-_Kleingrothe%2C_C.J._-_Medan_-_Teutonia_Club_in_Singapore_-_circa_1910.tif.jpg",
    "FINLAYSON": f"{_C}/8/84/KITLV_-_79924_-_Kleingrothe%2C_C.J._-_Medan_-_Cecil_Street%2C_Singapore_-_circa_1910.tif/lossy-page1-1280px-KITLV_-_79924_-_Kleingrothe%2C_C.J._-_Medan_-_Cecil_Street%2C_Singapore_-_circa_1910.tif.jpg",
    "CHART": "/assets/images/rickshaw-registered.png",
    "STATION_FACADE": f"{_C}/1/1e/Jinrikisha_Station_%2812848777624%29.jpg/1280px-Jinrikisha_Station_%2812848777624%29.jpg",
    "STATION_TOWER": f"{_C}/e/e5/Jinrikisha_Station_Singapore.jpg/1280px-Jinrikisha_Station_Singapore.jpg",
    "TRISHAW": f"{_C}/8/8f/Rickshaw_in_Trengganu_Street_20130210.jpg/1280px-Rickshaw_in_Trengganu_Street_20130210.jpg",
}

CREDITS = {
    "CHART": "Chart by Lesser Known Singapore; data from municipal reports and J.F. Warren",
}

_LBI = {"type": "letterbox", "zoom": [1.0, 1.04, 1.08], "pan": [(0.5, 0.5)] * 3, "ease": "ease-in-out"}
_LBW = {"type": "letterbox", "zoom": [1.0, 1.05, 1.10], "pan": [(0.5, 0.5)] * 3, "ease": "ease-in-out"}
_LBN = {"type": "letterbox", "zoom": [1.0, 1.03, 1.06], "pan": [(0.5, 0.5)] * 3, "ease": "ease-in"}
_CVZ = {"type": "cover", "zoom": [1.0, 1.06, 1.12], "pan": [(0.5, 0.5)] * 3, "ease": "ease-in-out"}
_CVZO = {"type": "cover", "zoom": [1.12, 1.06, 1.0], "pan": [(0.5, 0.5)] * 3, "ease": "ease-out"}
_CHART = {"type": "letterbox", "zoom": [1.0, 1.0, 1.0], "pan": [(0.5, 0.5)] * 3, "ease": "linear"}

# Top-favoured pan overrides (see docs/production-pipeline.md s3): when the
# subject of a photo sits high in the frame - heads in a group portrait, a
# building's tower - a centred cover crop clips it. A lower pan y keeps the
# top in view. Merge after the cover preset so this pan wins.
_TOP = {"pan": [(0.5, 0.15)] * 3}    # group portraits, heads at the very top
_TOPM = {"pan": [(0.5, 0.33)] * 3}   # a single standing figure, a tower/cupola

SLIDES = [
    {"img": "STATION_FACADE", **_CVZ},            # 0  s0     title
    {"img": "STATION_TOWER", **_CVZO, **_TOPM},   # 1  s1-2   the corner today; a wine bar now
    {"img": "RANK1930", **_CVZ},                  # 2  s3-4   built 1903 to register every rickshaw; the peak
    {"img": "PULLER1890", **_CVZ, **_TOPM},       # 3  s5-6   the building was preserved; the men left nothing
    {"img": "FINLAYSON", **_CVZO},                # 4  s7-8   rickshaws arrive 1880; they see off the gharries
    {"img": "STATION_FACADE", **_CVZO},           # 5  s9-10  1888 Jinrikisha Department; the rented offices
    {"img": "STATION_FACADE", **_CVZ},            # 6  s11-12 1898 the land bought; Tomlinson and Craik
    {"img": "STATION_TOWER", **_CVZ, **_TOPM},    # 7  s13    the triangular site, the tower, the crest
    {"img": "RANK1930", **_CVZO},                 # 8  s14-15 clerks registered and inspected; 22,629 by 1902
    {"img": "PORTRAIT1900", **_LBI},              # 9  s16    Hokchew and Henghua, from coastal Fujian
    {"img": "PORTRAIT1900", **_LBW},              # 10 s17-18 illiterate peasants; the coolie trade; no skill
    {"img": "CHILDREN", **_CVZ, **_TOPM},         # 11 s19-20 none owned the rickshaw; hired by the shift
    {"img": "RANK1930", **_CVZ},                  # 12 s21-22 the owner's cut; the coolie keng and the opium lamp
    {"img": "PULLER1890", **_CVZO, **_TOPM},      # 13 s23    25-40 km a day at a jog, barefoot, on opium
    {"img": "PORTRAIT1900", **_LBI},              # 14 s24    "the deadliest occupation in the East"
    {"img": "STUDIO1909", **_CVZ, **_TOP},        # 15 s25-26 Warren, the coroner's files; Sago Lane's death houses
    {"img": "FINLAYSON", **_CVZ},                 # 16 s27-29 not silent; the strikes of 1919, 1920, 1938
    {"img": "TRISHAW", **_CVZ},                   # 17 s30-31 the trishaw licensed 1914; the motor car
    {"img": "CHART", **_CHART},                   # 18 s32-33 licences cut from the late 1920s; 3,693 by 1940
    {"img": "TRISHAW", **_CVZO},                  # 19 s34-35 the 1947 ban; the men move to trishaws
    {"img": "STATION_FACADE", **_CVZ},            # 20 s36    a family-planning clinic; then a health centre
    {"img": "STATION_FACADE", **_CVZO},           # 21 s37    1987: the Tanjong Pagar conservation area
    {"img": "STATION_TOWER", **_CVZ, **_TOPM},    # 22 s38-39 1989 L&B; 2007 Jackie Chan; "1 Neil Road"
    {"img": "STUDIO1909", **_CVZO, **_TOP},       # 23 s40-41 worth keeping; the trade left no monument
    {"img": "STATION_TOWER", **_CVZO, **_TOPM},   # 24 s42-43 the conservation is of the architecture
    {"img": "RANK1930", **_CVZ},                  # 25 s44    Sago Lane, a temple and shops now
    {"img": "TEUTONIA", **_CVZ},                  # 26 s45    the merchants get statues, street names, foundations
    {"img": "PORTRAIT1900", **_LBN},              # 27 s46    the pullers survive as background
    {"img": "PULLER1890", **_CVZ, **_TOPM},       # 28 s47    early Singapore ran on imported muscle
    {"img": "STATION_FACADE", **_CVZO},           # 29 s48-49 the building that processed them; the closing line
]

SCHEDULE = [
    (0.0, 0), (3.325, 1), (24.325, 2), (44.3, 3), (49.725, 4),
    (68.925, 5), (97.375, 6), (120.125, 7), (137.825, 8), (156.125, 9),
    (166.325, 10), (183.1, 11), (195.175, 12), (219.65, 13), (233.075, 14),
    (242.975, 15), (263.0, 16), (291.925, 17), (302.75, 18), (331.65, 19),
    (345.775, 20), (354.85, 21), (369.675, 22), (391.25, 23), (412.35, 24),
    (427.275, 25), (439.025, 26), (450.2, 27), (462.25, 28), (480.175, 29),
]
TOTAL_DURATION = 494.175
TIMING_JSON = "audio/the-rickshaw-men-and-the-jinricksha-station.timing.json"
