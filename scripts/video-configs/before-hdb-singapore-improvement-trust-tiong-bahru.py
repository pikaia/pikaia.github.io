"""Video config for the Tiong Bahru / SIT post.

Nine images for a topic where the estate's built fabric survives better
than any archival photography of it - one 1930s-look corner block
(the post's own hero), one architectural detail shot (the vertical fins
at 82 Tiong Poh Road), the Trust's own crest, present-day street/transit
shots standing in for "the estate today," and the rebuilt market
(exterior + courtyard) carrying the gentrification/heritage beats.

  HERO      - SIT corner block, Streamline Moderne facade (hero)
  FIN82     - 82 Tiong Poh Road, vertical brick-and-render fins
  LOGO      - the Singapore Improvement Trust's own crest
  ROAD      - Tiong Bahru Road today, 2024
  FLATS     - another SIT-era block, 2006
  CANAL     - footpath alongside the canal (SIT drainage infrastructure)
  MRT       - Tiong Bahru MRT Station, 2024
  MARKET    - Tiong Bahru Market, exterior
  COURTYARD - Tiong Bahru Market's courtyard garden

Photos are landscape and use centred cover zoom; the crest and the
three portrait-oriented photos (FIN82, MARKET, COURTYARD) use letterbox
instead - a portrait image cover-fit into this landscape frame crops to
a narrow sliver regardless of zoom (see docs/production-pipeline.md §3).

39 slides, 482.375s.
"""

_U = "https://upload.wikimedia.org/wikipedia/commons"
_C = f"{_U}/thumb"

IMAGES = {
    "HERO": f"{_C}/1/12/Tiong_Bahru_8%2C_Jul_06.JPG/1280px-Tiong_Bahru_8%2C_Jul_06.JPG",
    "FIN82": f"{_U}/a/ae/Tiong_Bahru_13%2C_Jul_06.JPG",
    "LOGO": f"{_U}/e/ed/Singapore_Improvement_Trust_logo.png",
    "ROAD": f"{_C}/8/8f/Tiong_Bahru_Road_2.jpg/1280px-Tiong_Bahru_Road_2.jpg",
    "FLATS": f"{_C}/a/ac/Tiong_Bahru_10%2C_Jul_06.JPG/1280px-Tiong_Bahru_10%2C_Jul_06.JPG",
    "CANAL": f"{_C}/1/1a/Footpath_running_alongside_canal_between_Tiong_Bahru_Road_and_Boon_Tiong_Road.jpg/1280px-Footpath_running_alongside_canal_between_Tiong_Bahru_Road_and_Boon_Tiong_Road.jpg",
    "MRT": f"{_C}/a/a8/Tiong_Bahru_MRT_Station_202407_3.jpg/1280px-Tiong_Bahru_MRT_Station_202407_3.jpg",
    "MARKET": f"{_C}/1/1b/Tiong_Bahru_Market%2C_exterior.jpg/1280px-Tiong_Bahru_Market%2C_exterior.jpg",
    "COURTYARD": f"{_C}/9/9b/Tiong_Bahru_Market%2C_courtyard_garden.jpg/1280px-Tiong_Bahru_Market%2C_courtyard_garden.jpg",
}

_CVZ = {"type": "cover", "zoom": [1.0, 1.06, 1.12], "pan": [(0.5, 0.5)] * 3, "ease": "ease-in-out"}
_CVZO = {"type": "cover", "zoom": [1.12, 1.06, 1.0], "pan": [(0.5, 0.5)] * 3, "ease": "ease-out"}
_LTB = {"type": "letterbox", "zoom": [1.0, 1.04, 1.08], "pan": [(0.5, 0.5)] * 3, "ease": "ease-in-out"}
_LTBO = {"type": "letterbox", "zoom": [1.08, 1.04, 1.0], "pan": [(0.5, 0.5)] * 3, "ease": "ease-out"}

SLIDES = [
    {"img": "HERO", **_CVZ},        # 0  s0     title
    {"img": "ROAD", **_CVZO},       # 1  s1     Tiong Bahru today, heritage flex, Art Deco pocket
    {"img": "HERO", **_CVZ},        # 2  s2     almost none of it was built to be charming
    {"img": "FLATS", **_CVZO},      # 3  s3     Singapore's first public housing, colonial body, slum
    {"img": "FLATS", **_CVZ},       # 4  s4     the ground that would become Tiong Bahru, a byword
    {"img": "CANAL", **_CVZ},       # 5  s5     General Hospital, mangrove swamp, poor drainage
    {"img": "CANAL", **_CVZO},      # 6  s6     bred mosquitoes and disease
    {"img": "ROAD", **_CVZ},        # 7  s7     Chinatown, 1907 report, 1918 commission
    {"img": "FLATS", **_CVZO},      # 8  s8     P. S. Hunter's study of congestion
    {"img": "LOGO", **_LTB},        # 9  s9     the Singapore Improvement Trust, established 1927
    {"img": "HERO", **_CVZ},        # 10 s10    Tiong Bahru was its proving ground
    {"img": "CANAL", **_CVZO},      # 11 s11    clearance 1925, land acquired 1926, infrastructure
    {"img": "FLATS", **_CVZ},       # 12 s12    construction began 1936, first block that December
    {"img": "FLATS", **_CVZO},      # 13 s13    784 flats housing more than 6,000 people
    {"img": "FIN82", **_LTB},       # 14 s14    the architects, Streamline Moderne
    {"img": "HERO", **_CVZO},       # 15 s15    puay kee chu, "aeroplane houses"
    {"img": "FLATS", **_CVZ},       # 16 s16    a step up from a shophouse cubicle
    {"img": "ROAD", **_CVZO},       # 17 s17    mei ren wo, "den of beauties"
    {"img": "FLATS", **_CVZ},       # 18 s18    the "Hollywood of Singapore"
    {"img": "ROAD", **_CVZ},        # 19 s19    the flats themselves didn't discriminate
    {"img": "FLATS", **_CVZO},      # 20 s20    Japanese Occupation damaged rooftops
    {"img": "ROAD", **_CVZ},        # 21 s21    the community that formed there kept growing
    {"img": "LOGO", **_LTBO},       # 22 s22    the Trust was on borrowed time
    {"img": "LOGO", **_LTB},        # 23 s23    1 February 1960, SIT dissolved, HDB
    {"img": "CANAL", **_CVZ},       # 24 s24    the 1952-58 Master Plan
    {"img": "HERO", **_CVZO},       # 25 s25    the prototype for everything HDB did next
    {"img": "FLATS", **_CVZO},      # 26 s26    for a while, Tiong Bahru just aged
    {"img": "ROAD", **_CVZ},        # 27 s27    rental to sales, ageing population
    {"img": "FLATS", **_CVZ},       # 28 s28    reversed - not need, but heritage
    {"img": "COURTYARD", **_LTB},   # 29 s29    2003 conservation, gallery owners, boutique operators
    {"img": "MRT", **_CVZ},         # 30 s30    property prices climbed with them
    {"img": "MARKET", **_LTBO},     # 31 s31    highest resale/rental prices, boutique hotels
    {"img": "ROAD", **_CVZO},       # 32 s32    prewar leases from 1967, postwar from 1973
    {"img": "FLATS", **_CVZ},       # 33 s33    conservation forecloses en-bloc redevelopment
    {"img": "COURTYARD", **_LTBO},  # 34 s34    a genuine exception, not just a high price
    {"img": "HERO", **_CVZ},        # 35 s35    priced out of reach of the household it was built for
    {"img": "HERO", **_CVZO},       # 36 s36    why it matters today
    {"img": "LOGO", **_LTB},        # 37 s37    tested and refined by a colonial trust
    {"img": "COURTYARD", **_LTB},   # 38 s38    the estate's second life
]

SCHEDULE = [
    (0.0, 0), (5.050, 1), (20.975, 2), (24.425, 3), (38.350, 4),
    (49.875, 5), (69.400, 6), (74.075, 7), (95.725, 8), (104.875, 9),
    (119.450, 10), (122.675, 11), (142.750, 12), (155.525, 13), (163.500, 14),
    (186.175, 15), (202.025, 16), (212.750, 17), (229.425, 18), (235.175, 19),
    (246.025, 20), (262.775, 21), (276.000, 22), (280.225, 23), (295.500, 24),
    (309.450, 25), (316.750, 26), (319.650, 27), (341.275, 28), (346.875, 29),
    (365.075, 30), (368.100, 31), (387.575, 32), (408.750, 33), (424.025, 34),
    (438.575, 35), (446.675, 36), (455.550, 37), (472.750, 38),
]
TOTAL_DURATION = 482.375
TIMING_JSON = "audio/before-hdb-singapore-improvement-trust-tiong-bahru.timing.json"
