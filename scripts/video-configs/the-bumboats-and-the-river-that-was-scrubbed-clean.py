"""Video config for the bumboats/river clean-up post.

Seven images: a genuine 1960 photo of the working river, a surviving
1950s godown, two bronze river-trade sculptures for the labour
sections, present-day tourist bumboats, the CBD skyline reflected in
the now-clean river at night, and Boat Quay's restaurant strip at
night for the closing "name survives, trade doesn't" beat.

  HERO         - twakows at Boat Quay, September 1960 (hero)
  MOONSTONE    - surviving 1950s godown, Moonstone Lane
  RIVER_MERCH  - "The River Merchants" (2003), coolies loading a cart
  RIVER_SCULPT - the other "People of the River" sculpture, bullock cart
  CBD_NIGHT    - CBD skyline reflected in the river at night, present day
  BOATQUAY_NIGHT - Boat Quay restaurant strip at night, present day
  BUMBOAT_TODAY - present-day tourist bumboats on the river

Landscape photos use centred cover zoom; BOATQUAY_NIGHT is portrait and
uses letterbox instead (cover would crop it to a narrow sliver - see
docs/production-pipeline.md §3).

45 slides, 471.425s.
"""

_U = "https://upload.wikimedia.org/wikipedia/commons"
_C = f"{_U}/thumb"

IMAGES = {
    "HERO": f"{_U}/f/f6/SingaporeRiver-bumboats-196009.jpg",
    "MOONSTONE": f"{_C}/4/49/Warehouse_at_Moonstone_Lane.jpg/1280px-Warehouse_at_Moonstone_Lane.jpg",
    "RIVER_MERCH": f"{_C}/6/68/The_River_Merchants_%282003%29_by_Aw_Tee_Hong%2C_Cavenagh_Bridge%2C_Singapore_-_20051203.jpg/1280px-The_River_Merchants_%282003%29_by_Aw_Tee_Hong%2C_Cavenagh_Bridge%2C_Singapore_-_20051203.jpg",
    "RIVER_SCULPT": f"{_C}/6/62/The_River_Merchant_Sculpture._Singapore._%288069678494%29.jpg/1280px-The_River_Merchant_Sculpture._Singapore._%288069678494%29.jpg",
    "CBD_NIGHT": f"{_C}/8/87/BoatQuay-CentralBusinessDistrict-20090903.jpg/1280px-BoatQuay-CentralBusinessDistrict-20090903.jpg",
    "BOATQUAY_NIGHT": f"{_C}/5/51/BoatQuay%27sGastronomicDelights_16.jpg/1280px-BoatQuay%27sGastronomicDelights_16.jpg",
    "BUMBOAT_TODAY": f"{_U}/c/c0/Bumboats_in_front_of_Boat_Quay_on_the_Singapore_River_-_20060717.jpg",
}

_CVZ = {"type": "cover", "zoom": [1.0, 1.06, 1.12], "pan": [(0.5, 0.5)] * 3, "ease": "ease-in-out"}
_CVZO = {"type": "cover", "zoom": [1.12, 1.06, 1.0], "pan": [(0.5, 0.5)] * 3, "ease": "ease-out"}
_LTB = {"type": "letterbox", "zoom": [1.0, 1.04, 1.08], "pan": [(0.5, 0.5)] * 3, "ease": "ease-in-out"}
_LTBO = {"type": "letterbox", "zoom": [1.08, 1.04, 1.0], "pan": [(0.5, 0.5)] * 3, "ease": "ease-out"}

SLIDES = [
    {"img": "HERO", **_CVZ},            # 0  s0   title
    {"img": "HERO", **_CVZO},           # 1  s1   main cargo terminal, no proper dock
    {"img": "MOONSTONE", **_CVZ},       # 2  s2   bumboats twakows tongkangs ferried to godowns
    {"img": "HERO", **_CVZ},            # 3  s3   harbour deep enough, river shallow and narrow
    {"img": "MOONSTONE", **_CVZO},      # 4  s4   ships at anchor, ship to godown, godown to ship
    {"img": "RIVER_SCULPT", **_CVZ},    # 5  s5   Chulia lightermen, the tongkang
    {"img": "RIVER_MERCH", **_CVZO},    # 6  s6   Chinese crews, the twakow design
    {"img": "RIVER_MERCH", **_CVZ},     # 7  s7   a twakow crew was small, the towkay
    {"img": "RIVER_MERCH", **_CVZO},    # 8  s8   the work was exactly as hard as it looked
    {"img": "RIVER_SCULPT", **_CVZ},    # 9  s9   24 hours straight, sleeping in snatches
    {"img": "CBD_NIGHT", **_CVZO},      # 10 s10  by 1983, 800 lighters; office towers no memory
    {"img": "MOONSTONE", **_CVZ},       # 11 s11  I never worked on the river myself
    {"img": "MOONSTONE", **_CVZO},      # 12 s12  FX trader, Bank of America, founding banks
    {"img": "MOONSTONE", **_CVZ},       # 13 s13  couldn't say for certain, riverside godowns
    {"img": "MOONSTONE", **_CVZO},      # 14 s14  shown to me, the bank's roots
    {"img": "HERO", **_CVZ},            # 15 s15  1970s, river and Kallang Basin, the runoff
    {"img": "HERO", **_CVZO},           # 16 s16  government count of pollution sources
    {"img": "HERO", **_CVZ},            # 17 s17  800 bumboats, 64 boatyards
    {"img": "HERO", **_CVZO},           # 18 s18  the river was an open drain
    {"img": "CBD_NIGHT", **_CVZ},       # 19 s19  27 February 1977, Upper Peirce Reservoir
    {"img": "HERO", **_CVZ},            # 20 s20  in ten years let us have fishing
    {"img": "HERO", **_CVZO},           # 21 s21  it can be done
    {"img": "BOATQUAY_NIGHT", **_LTB},  # 22 s22  the Straits Times covered the same speech
    {"img": "MOONSTONE", **_CVZ},       # 23 s23  a genuinely multi-agency campaign
    {"img": "MOONSTONE", **_CVZO},      # 24 s24  squatters, backyard trades, farmers resettled
    {"img": "RIVER_MERCH", **_CVZ},     # 25 s25  street hawkers moved to food centres
    {"img": "RIVER_SCULPT", **_CVZO},   # 26 s26  vegetable wholesalers to Pasir Panjang
    {"img": "RIVER_SCULPT", **_CVZ},    # 27 s27  boatyards, charcoal trade, Lorong Halus
    {"img": "HERO", **_CVZ},            # 28 s28  the bumboats, all 800, moved to Pasir Panjang
    {"img": "BUMBOAT_TODAY", **_CVZO},  # 29 s29  September 1983, lighterage ceased
    {"img": "MOONSTONE", **_CVZ},       # 30 s30  nightsoil bucket phased out, January 1987
    {"img": "CBD_NIGHT", **_CVZO},      # 31 s31  1987, Lee marked the campaign's completion
    {"img": "CBD_NIGHT", **_CVZ},       # 32 s32  a triumph, diverted sewers, resettled
    {"img": "CBD_NIGHT", **_CVZO},      # 33 s33  we now have pleasant riverscapes
    {"img": "BUMBOAT_TODAY", **_CVZ},   # 34 s34  walk the river, fish or boat, ski and swim
    {"img": "BOATQUAY_NIGHT", **_LTBO}, # 35 s35  fish returned, regattas, dragon boats, bars
    {"img": "BOATQUAY_NIGHT", **_LTB},  # 36 s36  I worked in one of those towers, HSBC
    {"img": "BOATQUAY_NIGHT", **_LTBO}, # 37 s37  mee pok from a food centre on lunch break
    {"img": "BUMBOAT_TODAY", **_CVZO},  # 38 s38  an expat trader's bet to swim across
    {"img": "CBD_NIGHT", **_CVZ},       # 39 s39  everyone knew, still felt revulsion
    {"img": "BUMBOAT_TODAY", **_CVZ},   # 40 s40  he made it across unharmed
    {"img": "CBD_NIGHT", **_CVZO},      # 41 s41  succeeded on paper before in anyone's head
    {"img": "BOATQUAY_NIGHT", **_LTB},  # 42 s42  why it matters today
    {"img": "HERO", **_CVZ},            # 43 s43  a hard, unglamorous, decade-long effort
    {"img": "BUMBOAT_TODAY", **_CVZO},  # 44 s44  the bumboats are gone, only the name survives
]

SCHEDULE = [
    (0.0, 0), (3.800, 1), (11.450, 2), (25.700, 3), (36.600, 4),
    (46.475, 5), (55.025, 6), (71.950, 7), (85.725, 8), (98.975, 9),
    (107.500, 10), (122.350, 11), (128.700, 12), (145.600, 13), (155.550, 14),
    (164.750, 15), (177.975, 16), (213.200, 17), (224.350, 18), (230.450, 19),
    (249.775, 20), (256.100, 21), (257.900, 22), (268.975, 23), (276.575, 24),
    (288.650, 25), (295.650, 26), (300.500, 27), (306.475, 28), (321.775, 29),
    (328.725, 30), (335.800, 31), (351.950, 32), (361.700, 33), (364.425, 34),
    (372.100, 35), (382.475, 36), (391.300, 37), (397.300, 38), (403.150, 39),
    (414.825, 40), (417.475, 41), (423.775, 42), (439.950, 43), (454.900, 44),
]
TOTAL_DURATION = 471.425
TIMING_JSON = "audio/the-bumboats-and-the-river-that-was-scrubbed-clean.timing.json"
