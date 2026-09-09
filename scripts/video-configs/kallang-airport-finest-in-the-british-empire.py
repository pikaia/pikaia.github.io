"""Video config for the Kallang Airport post's Watch widget / main video.

Thin period coverage: one hero (freed POWs at the terminal, Sept 1945),
Wearne's aircraft in front of the new terminal (1937), Brewster Buffalos
at the RAF station (1941), a KLM DC-3 at Singapore (1939), a post-war RAF
Liberator on the apron, abandoned Japanese fighters (1945), one 1945
aerial of the whole airfield, the OSM locator map, the terminal in its
People's Association years (2006) and empty today (2021), and the
Straits Settlements crest on the gate.

  HERO_POW     - freed British/Allied POWs walking past the terminal, 8 Sep 1945 (hero)
  TERMINAL2021 - the empty streamline terminal head-on, 2021 (workhorse "today")
  MAP          - OSM locator: terminal, runway line, Sports Hub, Stadium/Dakota MRT
  WEARNE       - Wearne's "Governor Raffles" in front of the new terminal, c.1937
  BUFFALO      - Brewster Buffalo fighters at the Kallang hangar, 1941
  DEREIGER     - KLM Douglas DC-3 "De Reiger" on the Singapore apron, 1939
  LIBERATOR    - RAF B-24 Liberator on the apron, terminal behind, Sep 1945
  KI45         - abandoned Japanese Kawasaki Ki-45 fighters at Kallang, Sep 1945
  PA_HQ_2006   - the terminal as the People's Association headquarters, 2006
  CREST        - the "lion against a coconut tree" crest on the airport gate
  AERIAL1945   - the whole airfield from the air, Sep 1945 (450px source - used sparingly)

MAP is a graphic: letterbox + frozen zoom, per docs/production-pipeline.md
s3 (cover would crop the legend and labels). Everything else is centred
cover zoom, no horizontal pan. TERMINAL2021 is wider than 16:9 so a
centred cover keeps full height (tower stays in frame); PA_HQ_2006 and
HERO_POW are taller than 16:9, so they get a raised crop (_TOPM) to keep
the control tower.

36 slides, 554.65s.
"""

_U = "https://upload.wikimedia.org/wikipedia/commons"
_C = f"{_U}/thumb"

IMAGES = {
    "HERO_POW": f"{_U}/a/a0/Evacuation_of_British_POWs%2C_Kallang_Airport%2C_Singapore_-_19450908.jpg",
    "TERMINAL2021": f"{_C}/f/f3/Kallang_Airport_Terminal.jpg/1280px-Kallang_Airport_Terminal.jpg",
    "MAP": "/assets/images/kallang-airport-map.png",
    "WEARNE": f"{_U}/6/64/Wearne%27s_Air_Service%2C_Rapide.jpg",
    "BUFFALO": f"{_C}/7/72/Kallang_1941.jpg/1280px-Kallang_1941.jpg",
    "DEREIGER": f"{_C}/3/36/KITLV_A782_-_De_Reiger_van_het_type_DC-3_van_de_Koninklijke_Luchtvaart_Maatschappij_onderweg_naar_Nederland_op_het_vliegveld_te_Singapore_02.tif/lossy-page1-1280px-KITLV_A782_-_De_Reiger_van_het_type_DC-3_van_de_Koninklijke_Luchtvaart_Maatschappij_onderweg_naar_Nederland_op_het_vliegveld_te_Singapore_02.tif.jpg",
    "LIBERATOR": f"{_U}/5/57/RAF_Liberator_aircraft_at_Kallang_Airport%2C_Singapore_-_194509.jpg",
    "KI45": f"{_U}/4/40/Japanese_Kawasaki_Ki-45_Toryu_aircraft_at_Kallang_Airport%2C_Singapore_-_194509.jpg",
    "PA_HQ_2006": f"{_U}/a/af/Former_People%27s_Association_headquarters_at_old_Kallang_Airport%2C_Singapore.jpg",
    "CREST": f"{_C}/e/ef/Charge_of_the_Settlement_of_Singapore_on_the_gate_of_Kallang_Airport%2C_Singapore_-_20110501.jpg/960px-Charge_of_the_Settlement_of_Singapore_on_the_gate_of_Kallang_Airport%2C_Singapore_-_20110501.jpg",
    "AERIAL1945": f"{_U}/d/d4/Kallang_Airport_aerial_photo_1945.jpg",
}

CREDITS = {
    "MAP": "Map by Lesser Known Singapore; base map © OpenStreetMap contributors",
}

_CVZ = {"type": "cover", "zoom": [1.0, 1.06, 1.12], "pan": [(0.5, 0.5)] * 3, "ease": "ease-in-out"}
_CVZO = {"type": "cover", "zoom": [1.12, 1.06, 1.0], "pan": [(0.5, 0.5)] * 3, "ease": "ease-out"}
_MAP = {"type": "letterbox", "zoom": [1.0, 1.0, 1.0], "pan": [(0.5, 0.5)] * 3, "ease": "linear"}

# Raised crop for a source taller than 16:9 whose subject (the control
# tower) sits high - a centred cover crop would clip it. Merge after the
# cover preset so this pan wins. See docs/production-pipeline.md s3.
_TOPM = {"pan": [(0.5, 0.33)] * 3}

SLIDES = [
    {"img": "TERMINAL2021", **_CVZ},                 # 0  s0     title
    {"img": "MAP", **_MAP},                          # 1  s1-2   north bank, across from the Sports Hub; 9 Stadium Link
    {"img": "TERMINAL2021", **_CVZO},                # 2  s3     tens of thousands pass it, no idea what it is
    {"img": "HERO_POW", **_CVZ, **_TOPM},            # 3  s4-5   18 years; finest in the Empire; "miracle of the East"; closed 1955
    {"img": "TERMINAL2021", **_CVZ},                 # 4  s6     still there, still empty
    {"img": "BUFFALO", **_CVZ},                      # 5  s7     before Kallang: the RAF fields at Seletar and Sembawang
    {"img": "DEREIGER", **_CVZ},                     # 6  s8     civil aviation growing; the colony wanted its own airport
    {"img": "AERIAL1945", **_CVZ},                   # 7  s9     Clementi's 1931 announcement; "the best site is the Kallang Basin"
    {"img": "MAP", **_MAP},                          # 8  s10    a tidal swamp, Malay villages on stilts
    {"img": "AERIAL1945", **_CVZO},                  # 9  s11    300 acres reclaimed; the resettlement to Kampung Melayu
    {"img": "WEARNE", **_CVZ},                       # 10 s12-13 the work ran through the 1930s; opened 12 June 1937
    {"img": "DEREIGER", **_CVZO},                    # 11 s14-15 two jobs at once: a grass field and the flying-boat basin
    {"img": "LIBERATOR", **_CVZ},                    # 12 s16-17 the Britain-Australia Empire route; a scheduled halt
    {"img": "WEARNE", **_CVZO},                      # 13 s18    smaller operators: Wearne's, and KNILM to Batavia
    {"img": "TERMINAL2021", **_CVZ},                 # 14 s19    the terminal by Frank Dorrington Ward
    {"img": "PA_HQ_2006", **_CVZ, **_TOPM},          # 15 s20    streamline Moderne; the tower; the rooftop viewing gallery
    {"img": "HERO_POW", **_CVZO, **_TOPM},           # 16 s21-22 it drew visitors; Earhart, "an aviation miracle of the East"
    {"img": "BUFFALO", **_CVZ},                      # 17 s23-24 a short life, spent at war; RAF Station Kallang, 1941
    {"img": "KI45", **_CVZ},                         # 18 s25    the Buffalos outmatched; the Hurricanes too few
    {"img": "BUFFALO", **_CVZO},                     # 19 s26    9 Feb 1942: the surviving Hurricanes withdrawn to Sumatra
    {"img": "KI45", **_CVZO},                        # 20 s27    the occupation; the Japanese lay a concrete runway
    {"img": "LIBERATOR", **_CVZ},                    # 21 s28    civil flights resume 1949; second-busiest in the Far East
    {"img": "MAP", **_MAP},                          # 22 s29-30 lengthened for the Comet, but hemmed in by sea and city
    {"img": "DEREIGER", **_CVZ},                     # 23 s31    13 March 1954: the Constellation short of the runway
    {"img": "LIBERATOR", **_CVZO},                   # 24 s32    the inquiry: a fatigued crew, and the fire service
    {"img": "HERO_POW", **_CVZ, **_TOPM},            # 25 s33    18 March 1956: the merdeka rally that became a riot
    {"img": "MAP", **_MAP},                          # 26 s34-35 no room to grow; Paya Lebar opens, Kallang closes, 1955
    {"img": "DEREIGER", **_CVZO},                    # 27 s36    the name lingers: Old Airport Road, Dakota MRT
    {"img": "HERO_POW", **_CVZO, **_TOPM},           # 28 s37-38 the ground never went back to small; Nicoll Highway, 1956
    {"img": "PA_HQ_2006", **_CVZ, **_TOPM},          # 29 s39    Youth Sports Council; PA headquarters 1960-2009; the CMPB
    {"img": "MAP", **_MAP},                          # 30 s40-41 1973: the National Stadium on the runway; then the Sports Hub
    {"img": "CREST", **_CVZ},                        # 31 s42    restored 1994: the green windows, the lion-and-coconut crest
    {"img": "TERMINAL2021", **_CVZ},                 # 32 s43    gazetted for conservation, 2008; a Biennale venue, 2011
    {"img": "PA_HQ_2006", **_CVZO, **_TOPM},         # 33 s44-45 empty since 2009; the "Old Airport Square" plan; a listed building
    {"img": "HERO_POW", **_CVZ, **_TOPM},            # 34 s46    the shell kept, the purpose lost
    {"img": "TERMINAL2021", **_CVZO},               # 35 s47    a conserved facade, on ground known for football, not flight
]

SCHEDULE = [
    (0.0, 0), (4.325, 1), (21.675, 2), (31.975, 3), (51.6, 4),
    (58.25, 5), (69.325, 6), (76.175, 7), (93.725, 8), (103.95, 9),
    (121.375, 10), (135.0, 11), (154.875, 12), (172.75, 13), (182.725, 14),
    (193.65, 15), (209.975, 16), (232.925, 17), (250.925, 18), (261.175, 19),
    (274.375, 20), (288.4, 21), (309.05, 22), (327.9, 23), (344.35, 24),
    (357.95, 25), (378.05, 26), (398.325, 27), (413.95, 28), (424.775, 29),
    (449.2, 30), (472.65, 31), (492.725, 32), (503.2, 33), (528.75, 34),
    (536.75, 35),
]
TOTAL_DURATION = 554.65
TIMING_JSON = "audio/kallang-airport-finest-in-the-british-empire.timing.json"
