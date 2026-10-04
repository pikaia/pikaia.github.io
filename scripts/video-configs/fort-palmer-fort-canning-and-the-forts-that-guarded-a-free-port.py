"""Video config for the forts post.

Period photos carry most of it: the foot of Mount Palmer, Fort Canning above
the river (a carte-de-visite, 1867-80), its signal battery around 1860, the town
and harbour from the 1860s to the 1900s, New Harbour's entrance, the Tanjong
Pagar docks and the 1891 Admiralty chart. Three whole Straits Times pages
(14 Oct 1891, 14 Mar 1891, 10 Jan 1895) push in on their stories; the four stage
maps (scripts/render_fort_map.py) are letterboxed. Album prints are cropped
inside their mounts (pan/zoom from cover_crop test frames), zoom capped at 2.4x.

No portraits: the people named (Raffles, Farquhar, Lake, Fullerton, Canning,
Robinson, Anderson, Tan Keong Saik, Lee Keng Yan) sit on places or pages.

49 slides, 881.075s. AVATAR: first and last 30s (avatar test #3).
"""

_U = "https://upload.wikimedia.org/wikipedia/commons"
_C = f"{_U}/thumb"
_A = "/assets/images"

IMAGES = {
    "MP": f"{_C}/1/13/Strand_en_badgasten_aan_de_voet_van_Mount_Palmer_%28Mount_Parsee%2C_Parsee_Hill%29_bij_Singapore_Foot_of_Mount_Palmer._S.pore_%28titel_op_object%29%2C_RP-F-F01104-Z.jpg/1920px-Strand_en_badgasten_aan_de_voet_van_Mount_Palmer_%28Mount_Parsee%2C_Parsee_Hill%29_bij_Singapore_Foot_of_Mount_Palmer._S.pore_%28titel_op_object%29%2C_RP-F-F01104-Z.jpg",
    "CANBATT": f"{_C}/6/69/KITLV_-_29173_-_Singapore_city_and_harbor%2C_at_the_right_the_battery_for_the_day_and_evening_shot_-_circa_1860.tif/lossy-page1-3840px-KITLV_-_29173_-_Singapore_city_and_harbor%2C_at_the_right_the_battery_for_the_day_and_evening_shot_-_circa_1860.tif.jpg",
    "GATE": f"{_U}/5/5e/Fort_Gate%2C_Fort_Canning%2C_Singapore_-_20090103.jpg",
    "CDV": f"{_U}/9/9a/Gezicht_op_Fort_Canning_met_de_Singapore_River%2C_RP-F-F01025-BS.jpg",
    "HARB1860": f"{_C}/7/79/KITLV_-_29175_-_View_of_the_harbor_of_Singapore_-_1860.tif/lossy-page1-3840px-KITLV_-_29175_-_View_of_the_harbor_of_Singapore_-_1860.tif.jpg",
    "TOWN1870": f"{_C}/4/40/KITLV_-_106516_-_Singapore_-_circa_1870.tif/lossy-page1-1920px-KITLV_-_106516_-_Singapore_-_circa_1870.tif.jpg",
    "VIEWFC": f"{_C}/1/18/KITLV_-_1404879_-_Ludwig%2C_Deutsche_Buchhandlung_Max_-_Singapore_-_View_from_Fort_Canning%2C_Singapore_-_1895-1903.tif/lossy-page1-1920px-KITLV_-_1404879_-_Ludwig%2C_Deutsche_Buchhandlung_Max_-_Singapore_-_View_from_Fort_Canning%2C_Singapore_-_1895-1903.tif.jpg",
    "JPIER": f"{_C}/9/98/KITLV_-_150812_-_Lambert_%26_Co.%2C_G.R._-_Singapore_-_Johnston%27s_pier_in_the_harbor_at_Singapore_-_circa_1890.tif/lossy-page1-1920px-KITLV_-_150812_-_Lambert_%26_Co.%2C_G.R._-_Singapore_-_Johnston%27s_pier_in_the_harbor_at_Singapore_-_circa_1890.tif.jpg",
    "TOWNHALL": f"{_C}/7/7d/KITLV_A740_-_Stadhuis_te_Singapore%2C_KITLV_90268.tiff/lossy-page1-1920px-KITLV_A740_-_Stadhuis_te_Singapore%2C_KITLV_90268.tiff.jpg",
    "NHENTR": f"{_C}/7/78/Gezicht_op_de_ingang_van_de_nieuwe_haven_te_Singapore_Entrance_to_New-harbour._S.pore_%28titel_op_object%29%2C_RP-F-F01104-X.jpg/1920px-Gezicht_op_de_ingang_van_de_nieuwe_haven_te_Singapore_Entrance_to_New-harbour._S.pore_%28titel_op_object%29%2C_RP-F-F01104-X.jpg",
    "NHPOST": f"{_C}/d/d4/KITLV_-_1404881_-_Singapore._Entrance_at_New_harbor._-_1895-1908.tif/lossy-page1-1920px-KITLV_-_1404881_-_Singapore._Entrance_at_New_harbor._-_1895-1908.tif.jpg",
    "TPD": f"{_C}/9/98/Gezicht_op_de_gebouwen_en_dokken_van_de_Tanjong_Pagar_Dock_Co._Ltd._in_Singapore_Panorama_of_six_sheets_taken_from_clock_tower_%28titel_op_object%29%2C_RP-F-F01140-S.jpg/3840px-thumbnail.jpg",
    "CHART1891": f"{_C}/6/6f/Admiralty_Chart_No_2023_Keppel_Harbor%2C_Singapore%2C_Published_1893.jpg/3840px-Admiralty_Chart_No_2023_Keppel_Harbor%2C_Singapore%2C_Published_1893.jpg",
    "LABTUN": f"{_U}/1/12/Labrador_tunnel_1_entrance_20060419.jpg",
    "SILOSO": f"{_C}/e/e0/Casemates%2C_Fort_Siloso_Square_%28171549%29.jpg/1920px-Casemates%2C_Fort_Siloso_Square_%28171549%29.jpg",
    "CANNON": f"{_C}/5/51/9-pound_cannon_at_Fort_Canning%2C_Singapore.jpg/1920px-9-pound_cannon_at_Fort_Canning%2C_Singapore.jpg",
    "HABIBNOH": f"{_C}/1/11/Keramat_Habib_Noh_and_remains_of_former_Mount_Palmer.jpg/1920px-Keramat_Habib_Noh_and_remains_of_former_Mount_Palmer.jpg",
    "OCT1891": f"{_A}/straits-times-1891-10-14-page-2.jpg",
    "MAR1891": f"{_A}/straits-times-1891-03-14-page-3.jpg",
    "JAN1895": f"{_A}/straits-times-1895-01-10-page-3.jpg",
    "MAP0": f"{_A}/fort-map-0.png", "MAP1": f"{_A}/fort-map-1.png",
    "MAP2": f"{_A}/fort-map-2.png", "MAP3": f"{_A}/fort-map-3.png",
}

# Credits for images not captioned in the post or its gallery (the stage maps).
_OSM = "Map by Lesser Known Singapore. Map data (c) OpenStreetMap contributors"
CREDITS = {"MAP0": _OSM, "MAP1": _OSM, "MAP2": _OSM, "MAP3": _OSM}

_E = "ease-in-out"
_IN = {"type": "cover", "zoom": [1.0, 1.06, 1.12], "pan": [(0.5, 0.5)] * 3, "ease": _E}
_OUT = {"type": "cover", "zoom": [1.12, 1.06, 1.0], "pan": [(0.5, 0.5)] * 3, "ease": _E}
_INL = {"type": "cover", "zoom": [1.0, 1.08, 1.16], "pan": [(0.35, 0.45)] * 3, "ease": _E}
_INR = {"type": "cover", "zoom": [1.0, 1.08, 1.16], "pan": [(0.65, 0.45)] * 3, "ease": _E}
# Graphics (the stage maps): letterbox, frozen.
_GFX = {"type": "letterbox", "zoom": [1, 1, 1], "pan": [(0.5, 0.5)] * 3}


def _c(zoom, pan):
    return {"type": "cover", "zoom": zoom, "pan": pan, "ease": _E}


# Album prints, cropped inside their mounts.
_MP_FULL = _c([1.2, 1.24, 1.28], [(0.45, 0.5)] * 3)
_MP_FULL_OUT = _c([1.28, 1.24, 1.2], [(0.5, 0.45)] * 3)
_MP_HILL = _c([1.31, 1.36, 1.42], [(0.58, 0.186), (0.6, 0.202), (0.62, 0.217)])
_NHENTR = _c([1.2, 1.25, 1.3], [(0.45, 0.5)] * 3)
_NHENTR_R = _c([1.3, 1.25, 1.2], [(0.6, 0.45)] * 3)
_CDV = _c([1.45, 1.5, 1.55], [(0.53, 0.2), (0.53, 0.205), (0.53, 0.21)])
_CDV_OUT = _c([1.55, 1.5, 1.45], [(0.53, 0.21), (0.53, 0.205), (0.53, 0.2)])
_CANBATT = _c([1.89, 1.98, 2.06], [(1.0, 1.0)] * 3)
_CANBATT_TOWN = _c([1.9, 1.98, 2.06], [(0.0, 0.9), (0.03, 0.9), (0.06, 0.9)])
_TOWN = _c([1.0, 1.04, 1.08], [(0.5, 1.0)] * 3)
_TOWN_R = _c([1.25, 1.3, 1.35], [(0.85, 1.0), (0.8, 1.0), (0.75, 1.0)])
_TPD = _c([1.61, 1.68, 1.75], [(0.513, 0.536), (0.512, 0.529), (0.512, 0.524)])
_TPD_R = _c([1.9, 1.95, 2.0], [(0.62, 0.5), (0.6, 0.5), (0.58, 0.5)])
_VIEWFC = _c([1.1, 1.15, 1.2], [(0.4, 0.15), (0.5, 0.15), (0.6, 0.15)])
_VIEWFC_OUT = _c([1.2, 1.15, 1.1], [(0.6, 0.15), (0.5, 0.15), (0.4, 0.15)])
_NHPOST = _c([1.0, 1.04, 1.08], [(0.5, 0.0)] * 3)
_NHPOST_L = _c([1.25, 1.3, 1.35], [(0.0, 0.0), (0.05, 0.0), (0.1, 0.0)])
_HARB_LR = _c([1.0, 1.0, 1.0], [(0.0, 0.5), (0.5, 0.5), (1.0, 0.5)])
_HARB_RL = _c([1.05, 1.05, 1.05], [(1.0, 0.5), (0.5, 0.5), (0.0, 0.5)])
_CHART = _c([1.24, 1.29, 1.35], [(0.0, 0.003), (0.0, 0.039), (0.0, 0.073)])
_CHART_ENT = _c([1.9, 2.0, 2.1], [(0.05, 0.25), (0.08, 0.27), (0.11, 0.29)])
# Whole-page newspaper push-ins.
_OCT_HEAD = _c([1.0, 1.04, 1.08], [(0.5, 0.0)] * 3)
_OCT_ART1 = _c([2.2, 2.3, 2.4], [(1.0, 0.005), (1.0, 0.011), (1.0, 0.016)])
_OCT_ART2 = _c([2.0, 2.1, 2.2], [(1.0, 0.239), (1.0, 0.242), (1.0, 0.245)])
_MAR_HEAD = _c([2.21, 2.3, 2.4], [(0.0, 0.0)] * 3)
_MAR_PAGE = _c([1.0, 1.03, 1.06], [(0.5, 0.0)] * 3)
_MAR_COL2 = _c([1.26, 1.32, 1.37], [(0.0, 0.009), (0.0, 0.02), (0.0, 0.027)])
_JAN_HEAD = _c([2.21, 2.3, 2.4], [(0.468, 0.378), (0.469, 0.379), (0.47, 0.38)])
_JAN_AMT = _c([1.87, 1.95, 2.03], [(0.462, 0.766), (0.464, 0.763), (0.466, 0.761)])
_JAN_LOW = _c([1.87, 1.95, 2.03], [(0.462, 0.86), (0.464, 0.88), (0.466, 0.9)])

SLIDES = [
    {"img": "MP", **_MP_FULL},            # 0  s0      title
    {"img": "NHENTR", **_NHENTR},         # 1  s1      the party on Mount Wallich above the docks
    {"img": "CHART1891", **_CHART},       # 2  s2      the guns fire out to sea
    {"img": "MAR1891", **_MAR_HEAD},      # 3  s3      seven months earlier, the meeting
    {"img": "HARB1860", **_HARB_LR},      # 4  s4      a port with no duties still needed forts
    {"img": "OCT1891", **_OCT_HEAD},      # 5  s5      the Straits Times next morning
    {"img": "OCT1891", **_OCT_ART1},      # 6  s6-8    "The New 10-Inch Guns"
    {"img": "NHPOST", **_NHPOST},         # 7  s9-10   the target tongkang
    {"img": "OCT1891", **_OCT_ART2},      # 8  s11-12  the second shot
    {"img": "CHART1891", **_CHART_ENT},   # 9  s13     range and penetration
    {"img": "HABIBNOH", **_IN},           # 10 s14-15  the Parsee Lodge made uninhabitable
    {"img": "TOWN1870", **_TOWN},         # 11 s16-18  modest beginnings
    {"img": "HARB1860", **_HARB_RL},      # 12 s19-20  the free port and its revenue
    {"img": "MAP0", **_GFX},              # 13 s21-22  Lake's survey, Mount Palmer and Pearl's Hill
    {"img": "JPIER", **_IN},              # 14 s23-24  Fort Fullerton, enlarged to Johnston's Pier
    {"img": "CANNON", **_IN},             # 15 s25-27  the merchants' complaints
    {"img": "MP", **_MP_HILL},            # 16 s28     Fort Palmer by 1864
    {"img": "CDV", **_CDV},               # 17 s29-30  Government House pulled down
    {"img": "VIEWFC", **_VIEWFC},         # 18 s31-32  Fort Canning finished, 1861
    {"img": "CANBATT", **_CANBATT},       # 19 s33-34  guns; no water; out of range
    {"img": "MAP1", **_GFX},              # 20 s35-37  the morning gun; Pearl's Hill cut down
    {"img": "TOWN1870", **_TOWN_R},       # 21 s38-39  governed from India; Fullerton dismantled
    {"img": "JPIER", **_OUT},             # 22 s40-41  the 1872 editorial; the Post Office
    {"img": "TPD", **_TPD},               # 23 s42-43  docks and coal at New Harbour
    {"img": "NHENTR", **_NHENTR_R},       # 24 s44     forts either side of the western entrance
    {"img": "MAP2", **_GFX},              # 25 s45-47  Mount Palmer rebuilt; the Dock Company deal
    {"img": "CANBATT", **_CANBATT_TOWN},  # 26 s48-49  the garrison; the 1890 demand
    {"img": "MAR1891", **_MAR_PAGE},      # 27 s50-51  the meeting called; a whole page
    {"img": "TOWNHALL", **_IN},           # 28 s52-53  crowds at the Town Hall
    {"img": "MAR1891", **_MAR_COL2},      # 29 s54-56  the resolutions and speakers
    {"img": "JAN1895", **_JAN_HEAD},      # 30 s57-59  silver falls
    {"img": "JAN1895", **_JAN_AMT},       # 31 s60     London's rising scale
    {"img": "JAN1895", **_JAN_LOW},       # 32 s61-62  resignations; 20 per cent
    {"img": "TPD", **_TPD_R},             # 33 s63-64  1914, opium revenue
    {"img": "MAP2", **_GFX},              # 34 s65-66  the map
    {"img": "MAP3", **_GFX},              # 35 s67-68  Fort Fullerton gone; the Fullerton Hotel
    {"img": "MP", **_MP_FULL_OUT},        # 36 s69-70  Mount Palmer dug away
    {"img": "HABIBNOH", **_OUT},          # 37 s71     the knoll and Habib Noh's shrine
    {"img": "VIEWFC", **_VIEWFC_OUT},     # 38 s72-73  Fort Canning demolished; the Battlebox
    {"img": "GATE", **_IN},               # 39 s74     the gateway and cannons
    {"img": "LABTUN", **_IN},             # 40 s75-76  Fort Pasir Panjang enlarged
    {"img": "NHPOST", **_NHPOST_L},       # 41 s77     February 1942
    {"img": "SILOSO", **_INL},            # 42 s78     Siloso's guns turned inland
    {"img": "LABTUN", **_OUT},            # 43 s79     the Labrador tunnels found
    {"img": "SILOSO", **_INR},            # 44 s80     Siloso today
    {"img": "CANNON", **_OUT},            # 45 s81-82  who should pay
    {"img": "MAP3", **_GFX},              # 46 s83-84  steady spending today
    {"img": "CDV", **_CDV_OUT},           # 47 s85     where it fits
    {"img": "TOWNHALL", **_OUT},          # 48 s86-87  the harder fight was over the bill
]

SCHEDULE = [
    (0.0, 0), (4.7, 1), (17.7, 2), (35.15, 3), (50.375, 4), (62.675, 5), (66.875, 6),
    (94.95, 7), (109.15, 8), (131.1, 9), (140.275, 10), (157.325, 11), (175.325, 12),
    (201.575, 13), (222.9, 14), (251.95, 15), (277.05, 16), (285.8, 17), (305.85, 18),
    (319.875, 19), (347.2, 20), (373.975, 21), (391.3, 22), (412.6, 23), (431.35, 24),
    (451.45, 25), (472.45, 26), (498.975, 27), (514.725, 28), (540.25, 29), (569.8, 30),
    (596.625, 31), (616.45, 32), (636.9, 33), (655.075, 34), (667.65, 35), (686.4, 36),
    (706.125, 37), (718.7, 38), (741.025, 39), (748.7, 40), (765.675, 41), (782.5, 42),
    (790.275, 43), (801.7, 44), (809.575, 45), (822.55, 46), (846.575, 47), (866.4, 48),
]
TOTAL_DURATION = 881.075
TIMING_JSON = "audio/fort-palmer-fort-canning-and-the-forts-that-guarded-a-free-port.timing.json"

# The avatar presenter, Phase 1 test #3: corner bubble for the first and last 30 s.
AVATAR = {"ranges": [(0, 30), (-30, None)]}
