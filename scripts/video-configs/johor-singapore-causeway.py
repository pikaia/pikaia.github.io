"""Video config for the Johor-Singapore Causeway post.

Decent coverage this time - a mix of period and present-day: the eerie
empty Causeway from the 2020 lockdown (hero / bookend), a ~1950 KITLV
photo of a car crossing, a 1943 occupation-magazine shot of the breach
being repaired, the pipelines in 1973, present-day crossings and
checkpoints, the passport "chop", the airport-style automated gates, a
Johor Bahru mall, and the RTS station going up at Bukit Chagar.

  HERO_EMPTY   - the Causeway empty at night, March 2020 lockdown (hero)
  BUSQUEUE     - the bus queue at Woodlands Checkpoint, Nov 2025 (portrait)
  AEON         - an AEON mall in Bukit Indah, Johor Bahru
  CAUSEWAY_DAY - the Causeway by day from the Singapore side, 2023
  CAUSEWAY_CC0 - the Causeway from Princess Cove, Johor Bahru, 2020
  PIPE1973     - crossing by car in 1973-74, the water pipelines alongside
  KITLV1950    - a car on the Causeway, c.1950, the rubble embankment visible
  C1945        - the Causeway from the air, September 1945 (640px source)
  REPAIR1943   - labourers repairing the 1942 breach, from Djawa Baroe, 1943
  PAN2019      - a wide panorama from the Singapore shore, 2019
  WDL_CP       - Woodlands Checkpoint building, December 2023
  WDL_TRAIN    - the Woodlands Train Checkpoint
  SULTAN_CIQ   - the Sultan Iskandar checkpoint, Johor Bahru
  SECOND_LINK  - the Malaysia-Singapore Second Link bridge, 2019
  STAMP        - a Woodlands entry stamp in a Malaysian passport, 2007
  CHANGI_GATE  - automated immigration gates at Changi Airport Terminal 4 (portrait)
  RTS_CONSTR   - the Bukit Chagar RTS station under construction, June 2026

All photos, centred cover zoom, no horizontal pan.

44 slides, 717.925s.
"""

_U = "https://upload.wikimedia.org/wikipedia/commons"
_C = f"{_U}/thumb"

IMAGES = {
    "HERO_EMPTY": f"{_C}/9/9d/Empty_Singapore-Malaysia_Causeway_2.jpg/1280px-Empty_Singapore-Malaysia_Causeway_2.jpg",
    "BUSQUEUE": f"{_C}/f/f5/Woodlands_Checkpoint_Departure_Bus_Causeway_Link_-_Nov_2025.jpg/1280px-Woodlands_Checkpoint_Departure_Bus_Causeway_Link_-_Nov_2025.jpg",
    "AEON": f"{_C}/8/84/Aeon_Mall_and_a_rainbow%2C_Bukit_Indah%2C_Johor_Bahru%2C_Johor%2C_Malaysia.jpg/1280px-Aeon_Mall_and_a_rainbow%2C_Bukit_Indah%2C_Johor_Bahru%2C_Johor%2C_Malaysia.jpg",
    "CAUSEWAY_DAY": f"{_C}/c/c0/Johor_Causeway.jpg/1280px-Johor_Causeway.jpg",
    "CAUSEWAY_CC0": f"{_C}/a/a6/Causeway_11.jpg/1280px-Causeway_11.jpg",
    "PIPE1973": f"{_C}/4/40/Singapore-Johore-Causeway-1973-74-WUS08290.jpg/1280px-Singapore-Johore-Causeway-1973-74-WUS08290.jpg",
    "KITLV1950": f"{_C}/8/86/KITLV_A1363_-_Weg_van_Djohor_Bahru_naar_Singapore%2C_KITLV_78456.tiff/lossy-page1-1280px-KITLV_A1363_-_Weg_van_Djohor_Bahru_naar_Singapore%2C_KITLV_78456.tiff.jpg",
    "C1945": f"{_U}/0/01/The_Causeway_joining_Singapore_Island_with_Johore_in_1945.jpg",
    "REPAIR1943": f"{_C}/c/c4/Djohor_Baru_Bridge_in_Singapore_%28Syonan%29%2C_Djawa_Baroe%2C_Vol._1%2C_Iss._4_%281943-02-15%29%2C_pp18-19.jpg/1280px-Djohor_Baru_Bridge_in_Singapore_%28Syonan%29%2C_Djawa_Baroe%2C_Vol._1%2C_Iss._4_%281943-02-15%29%2C_pp18-19.jpg",
    "PAN2019": f"{_C}/0/0a/Johor-Singapore_Causeway_near_the_midway_point_of_the_border_06042019.jpg/1280px-Johor-Singapore_Causeway_near_the_midway_point_of_the_border_06042019.jpg",
    "WDL_CP": f"{_C}/7/73/Woodlands_Checkpoint_December_2023.jpg/1280px-Woodlands_Checkpoint_December_2023.jpg",
    "WDL_TRAIN": f"{_C}/3/36/Woodlands_Train_Checkpoint.jpg/1280px-Woodlands_Train_Checkpoint.jpg",
    "SULTAN_CIQ": f"{_C}/9/98/SultanIskandarCIQ.JPG/1280px-SultanIskandarCIQ.JPG",
    "SECOND_LINK": f"{_C}/0/09/Malaysia-Singapore_Second_Link_bridge.jpg/1280px-Malaysia-Singapore_Second_Link_bridge.jpg",
    "STAMP": f"{_C}/b/bc/Singapore_Woodlands_Checkpoint_entry_stamp_in_a_passport_-_20070720.jpg/1280px-Singapore_Woodlands_Checkpoint_entry_stamp_in_a_passport_-_20070720.jpg",
    "CHANGI_GATE": f"{_C}/4/42/Terminal_4_%28Changi%29_Immigration_automated_gate_entrance.jpg/1280px-Terminal_4_%28Changi%29_Immigration_automated_gate_entrance.jpg",
    "RTS_CONSTR": f"{_C}/0/0f/Bukit_Chagar_RTS_station_construction_site_20260613_175634.jpg/1280px-Bukit_Chagar_RTS_station_construction_site_20260613_175634.jpg",
}

_CVZ = {"type": "cover", "zoom": [1.0, 1.06, 1.12], "pan": [(0.5, 0.5)] * 3, "ease": "ease-in-out"}
_CVZO = {"type": "cover", "zoom": [1.12, 1.06, 1.0], "pan": [(0.5, 0.5)] * 3, "ease": "ease-out"}

SLIDES = [
    {"img": "HERO_EMPTY", **_CVZ},        # 0  s0-1   title; two rush hours, opposite directions
    {"img": "BUSQUEUE", **_CVZ},          # 1  s2     before dawn, Johor residents pour south to jobs
    {"img": "AEON", **_CVZ},              # 2  s3     the current reverses; Singaporeans head north for cheaper everything
    {"img": "CAUSEWAY_DAY", **_CVZO},     # 3  s4     one kilometre of road on a bank of rock
    {"img": "CAUSEWAY_CC0", **_CVZ},      # 4  s5-6   for a century everything went by ferry; by 1911 round the clock
    {"img": "PIPE1973", **_CVZ},          # 5  s7-8   1917, the consulting engineers; what they chose was not a bridge
    {"img": "KITLV1950", **_CVZ},         # 6  s9     a solid embankment of rock, road, rail, water pipes, a lock
    {"img": "REPAIR1943", **_CVZ},        # 7  s10    contract to Topham, Jones & Railton; granite tipped into the strait
    {"img": "C1945", **_CVZO},            # 8  s11-12 a 1920s slump nearly stopped it; it was finished anyway
    {"img": "KITLV1950", **_CVZO},        # 9  s13    strait sealed June 1923; the first passenger train, 1 October
    {"img": "C1945", **_CVZ},             # 10 s14    the formal opening, 28 June 1924, a convoy of eleven cars
    {"img": "PAN2019", **_CVZ},           # 11 s15    the island joined to the peninsula; the mainland railway terminus
    {"img": "C1945", **_CVZO},            # 12 s16-17 the most dramatic day; the British fall back across the strait
    {"img": "PAN2019", **_CVZO},          # 13 s18    the last unit over, the Argylls, piped across
    {"img": "REPAIR1943", **_CVZ},        # 14 s19-20 two charges; a 21-metre gap; the pipelines cut. It bought no time
    {"img": "C1945", **_CVZ},             # 15 s21-22 the Japanese take the island; after the war, Bailey bridges
    {"img": "PIPE1973", **_CVZ},          # 16 s23    the pipelines cut in 1942 are still there, and still matter
    {"img": "CAUSEWAY_DAY", **_CVZO},     # 17 s24-25 the 1961-62 water agreements; up to 250 million gallons a day; to 2061
    {"img": "PIPE1973", **_CVZO},         # 18 s26    the prices - 3 sen, 50 sen - have never changed
    {"img": "CAUSEWAY_CC0", **_CVZ},      # 19 s27    both governments call it unfinished business
    {"img": "CAUSEWAY_DAY", **_CVZ},      # 20 s28    Singapore makes its own water now, but Johor water still crosses
    {"img": "PAN2019", **_CVZ},           # 21 s29    over 300,000 crossings a day; the 543,000 single-day record
    {"img": "BUSQUEUE", **_CVZO},         # 22 s30-31 Johor residents who work in Singapore; the gap is stark
    {"img": "WDL_CP", **_CVZ},            # 23 s32    pay several times higher; in a Johor household the difference compounds
    {"img": "BUSQUEUE", **_CVZ},          # 24 s33    up at four or five; a motorbike or a bus; through immigration both sides
    {"img": "WDL_CP", **_CVZO},           # 25 s34-35 food courts, building sites, hospital staff; the ringgit's six per cent
    {"img": "STAMP", **_CVZ},             # 26 s36-37 clearance got faster; the "chop", W for Woodlands, T for Tuas
    {"img": "CHANGI_GATE", **_CVZ},       # 27 s38    now an automated gate scans a passport or QR code and takes a photo
    {"img": "WDL_CP", **_CVZ},            # 28 s39    Changi went further - iris and face, no passport - and it is coming here
    {"img": "BUSQUEUE", **_CVZO},         # 29 s40-41 the arithmetic is unchanged; automating the counter doesn't widen the road
    {"img": "AEON", **_CVZ},              # 30 s42-43 the second rush hour, discretionary; one dollar buys 3.3 ringgit
    {"img": "PAN2019", **_CVZO},          # 31 s44    petrol the classic reason; RON95 half price; the three-quarter-tank rule
    {"img": "AEON", **_CVZO},             # 32 s45-47 groceries a third to half cheaper; haircuts, servicing; the food
    {"img": "SULTAN_CIQ", **_CVZ},        # 33 s48    medical and dental, the widest gap; clinics quoting fees in Singapore dollars
    {"img": "BUSQUEUE", **_CVZ},          # 34 s49-51 none of it is comfortable; a four-hour queue home; people do it anyway
    {"img": "SECOND_LINK", **_CVZ},       # 35 s52-53 plans to relieve it; the Second Link at Tuas, opened 1998
    {"img": "CAUSEWAY_DAY", **_CVZO},     # 36 s54    proposals to replace the Causeway with a bridge, from 1996
    {"img": "RTS_CONSTR", **_CVZ},        # 37 s55-56 the current fix is a train; the RTS between Woodlands North and Bukit Chagar
    {"img": "WDL_TRAIN", **_CVZ},         # 38 s57    up to 10,000 an hour each way; a five-minute crossing
    {"img": "WDL_CP", **_CVZO},           # 39 s58-59 the high-speed line, cancelled and revived; Woodlands rebuilt by the 2030s
    {"img": "HERO_EMPTY", **_CVZ},        # 40 s60-62 March 2020 to early 2022 the border was shut; a side to choose and stay on
    {"img": "C1945", **_CVZO},            # 41 s63    the only other time the Causeway has been empty was 1945
    {"img": "CAUSEWAY_DAY", **_CVZ},      # 42 s64-65 the Causeway works because the two ends are unequal
    {"img": "HERO_EMPTY", **_CVZO},       # 43 s66    a kilometre of rock, now where two economies are settled by the tankful
]

SCHEDULE = [
    (0.0, 0), (10.625, 1), (18.925, 2), (36.125, 3), (43.75, 4),
    (64.35, 5), (78.75, 6), (98.675, 7), (115.65, 8), (134.675, 9),
    (146.6, 10), (163.3, 11), (171.65, 12), (188.15, 13), (202.375, 14),
    (218.475, 15), (239.175, 16), (246.1, 17), (270.8, 18), (281.575, 19),
    (299.225, 20), (313.75, 21), (333.675, 22), (348.775, 23), (367.375, 24),
    (381.225, 25), (403.425, 26), (416.6, 27), (428.7, 28), (448.55, 29),
    (463.7, 30), (482.875, 31), (504.125, 32), (523.875, 33), (543.95, 34),
    (563.175, 35), (581.65, 36), (599.875, 37), (618.7, 38), (632.825, 39),
    (649.175, 40), (670.95, 41), (681.2, 42), (704.7, 43),
]
TOTAL_DURATION = 717.925
TIMING_JSON = "audio/johor-singapore-causeway.timing.json"
