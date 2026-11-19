"""Video config for the COE post.

The pool is all sixteen pictures from the post and its gallery:
the ERP gantries over the expressways and the city (the BKE
hero, the toll station, Bugis, the night shot, an early gantry,
one from below, Dunearn Road in 2006), the two Restricted Zone
signs (ALS and ERP eras), the in-vehicle unit, and the ERP 2.0
on-board unit set, processing unit and display. Sixteen
pictures for just under eighteen minutes: images recur at new
story beats with varied pans and alternating zoom direction,
never twice in a row.

Named-person rule: the pool holds no portraits at all, so the
rule is met by construction. Named-place audit: the Dunearn
Road photograph sits under the sentence naming Dunearn Road
among the first removals; the in-vehicle unit photograph sits
under the In-vehicle Unit sentence; the on-board unit display
sits under the sentences describing the unit; the ALS sign
sits under the ALS sentences. The widower section is
anonymised in the post and shows only generic gantry and road
photographs.

Every slide carries its discreet photo title (standing rule,
Chris, 2026-11-11): the short form of its image's post/gallery
caption, drawn small in the top corner on a soft dark backing
for the slide's whole run.

58 slides, 1050.775s. One known flag: slide 47 (the
ERP 2.0 preparation sentence) is a single unsplittable sentence
at 31.1s. Narration: Kokoro with the OpenVoice clone.
Pronunciation candidates for the car makes (Honda, Integra,
Toyota, Altis) filed 2026-11-19, NOT ear-verified yet.
AVATAR: first and last 30s, cartoon with motion.
"""

IMAGES = {
    "HERO": "https://upload.wikimedia.org/wikipedia/commons/1/14/ERP_gantry_on_the_BKE.jpg",
    "ALSSIGN": "https://thumb.wikimedia.org/wikipedia/commons/thumb/8/89/Singapore_Road_Signs_-_Warning_Sign_-_Restricted_Zone_%28ALS%29.svg/960px-Singapore_Road_Signs_-_Warning_Sign_-_Restricted_Zone_%28ALS%29.svg.png",
    "NIGHT": "https://upload.wikimedia.org/wikipedia/commons/6/65/Singapore%27s_ERP_gantry_at_night.jpg",
    "IU": "https://upload.wikimedia.org/wikipedia/commons/2/2d/ERP_IU_unit_back_side.JPG",
    "ERPNEW": "https://upload.wikimedia.org/wikipedia/commons/0/03/ERP_new.jpg",
    "OBU": "https://upload.wikimedia.org/wikipedia/commons/e/e4/ERP2.0_On_Board_Unit_display.jpg",
    "DUNEARN": "https://upload.wikimedia.org/wikipedia/commons/f/f4/Dunearn_Rd_-_Wayang_Satu_flyover_20060402.JPG",
    "G_MULTI": "https://upload.wikimedia.org/wikipedia/commons/5/5c/ERP_in_Singapore.jpg",
    "G_TOLL": "https://upload.wikimedia.org/wikipedia/commons/3/35/ERP_toll_station.jpg",
    "G_SIGN": "https://upload.wikimedia.org/wikipedia/commons/d/dc/Singapore%27s_ERP_gantry.jpg",
    "G_BUGIS": "https://upload.wikimedia.org/wikipedia/commons/7/7a/ERPBugis.JPG",
    "G_EARLY": "https://upload.wikimedia.org/wikipedia/commons/c/c7/027_ERP_gantry.jpg",
    "G_PORTRAIT": "https://upload.wikimedia.org/wikipedia/commons/9/90/Electronic_Road_Pricing_gantry_in_Singapore.jpg",
    "G_OBUSET": "https://upload.wikimedia.org/wikipedia/commons/0/0c/Car_On_Board_Unit_Singapore.jpg",
    "G_OBUPROC": "https://upload.wikimedia.org/wikipedia/commons/0/0a/Car_On_Board_Processing_Unit_Singapore.jpg",
    "G_ERPSIGN": "https://thumb.wikimedia.org/wikipedia/commons/thumb/6/61/Singapore_Road_Signs_-_Warning_Sign_-_Restricted_Zone_%28ERP%29.svg/960px-Singapore_Road_Signs_-_Warning_Sign_-_Restricted_Zone_%28ERP%29.svg.png",
}

# Every image is captioned in the post or its gallery.
CREDITS = {}

# The channel's 2x2 thumbnail grid, in story order: the
# gantry, the 1975 sign, the unit in the car, the new display.
THUMBNAIL = [
    {"img": "HERO", "pan": (0.5, 0.5)},
    {"img": "ALSSIGN", "pan": (0.5, 0.5)},
    {"img": "IU", "pan": (0.5, 0.5)},
    {"img": "OBU", "pan": (0.5, 0.5)},
]

_E = "ease-in-out"

SLIDES = [
    {"img": "HERO", **{"type": "cover", "title": "An ERP gantry over the Bukit Timah Expressway", "zoom": [1.0, 1.06, 1.12], "pan": [(0.5, 0.5)] * 3, "ease": _E}},  # 0  s0 s0 title (5.7s)
    {"img": "G_TOLL", **{"type": "cover", "title": "An ERP toll station gantry", "zoom": [1.12, 1.06, 1.0], "pan": [(0.35, 0.5)] * 3, "ease": _E}},  # 1  s1-2 the gantries are coming down (17.18s)
    {"img": "G_MULTI", **{"type": "cover", "title": "An ERP gantry over a multi-lane road", "zoom": [1.0, 1.06, 1.12], "pan": [(0.65, 0.5)] * 3, "ease": _E}},  # 2  s3 the last working gantries charge until 31 Dec 2026 (17.73s)
    {"img": "ERPNEW", **{"type": "cover", "title": "A gantry of the current generation", "zoom": [1.12, 1.06, 1.0], "pan": [(0.5, 0.4)] * 3, "ease": _E}},  # 3  s4-6 pay to own, pay again to drive; the story of both (22.0s)
    {"img": "ALSSIGN", **{"type": "cover", "title": "The Restricted Zone sign of the ALS era", "zoom": [1.0, 1.06, 1.12], "pan": [(0.5, 0.5)] * 3, "ease": _E}},  # 4  s7-8 1975: the Area Licensing Scheme begins (29.53s)
    {"img": "G_SIGN", **{"type": "cover", "title": "An ERP gantry in the city", "zoom": [1.12, 1.06, 1.0], "pan": [(0.35, 0.5)] * 3, "ease": _E}},  # 5  s9-10 checked by eye; entries fell 76 per cent (28.18s)
    {"img": "ALSSIGN", **{"type": "cover", "title": "The Restricted Zone sign of the ALS era", "zoom": [1.0, 1.06, 1.12], "pan": [(0.65, 0.5)] * 3, "ease": _E}},  # 6  s11-13 the paper licence's built-in limits (19.32s)
    {"img": "G_MULTI", **{"type": "cover", "title": "An ERP gantry over a multi-lane road", "zoom": [1.12, 1.06, 1.0], "pan": [(0.5, 0.4)] * 3, "ease": _E}},  # 7  s14-16 price the driving itself; the other half of the question (17.93s)
    {"img": "HERO", **{"type": "cover", "title": "An ERP gantry over the Bukit Timah Expressway", "zoom": [1.0, 1.06, 1.12], "pan": [(0.5, 0.5)] * 3, "ease": _E}},  # 8  s17-18 the 1980s: 280,000 cars; roads at 12 per cent of the land (19.9s)
    {"img": "ERPNEW", **{"type": "cover", "title": "A gantry of the current generation", "zoom": [1.12, 1.06, 1.0], "pan": [(0.35, 0.5)] * 3, "ease": _E}},  # 9  s19 the select committee recommends rationing the fleet (12.15s)
    {"img": "G_TOLL", **{"type": "cover", "title": "An ERP toll station gantry", "zoom": [1.0, 1.06, 1.12], "pan": [(0.65, 0.5)] * 3, "ease": _E}},  # 10  s20-21 first bidding, April 1990; an auction product (18.23s)
    {"img": "G_MULTI", **{"type": "cover", "title": "An ERP gantry over a multi-lane road", "zoom": [1.12, 1.06, 1.0], "pan": [(0.5, 0.4)] * 3, "ease": _E}},  # 11  s22 the LTA quota formula (26.93s)
    {"img": "G_SIGN", **{"type": "cover", "title": "An ERP gantry in the city", "zoom": [1.0, 1.06, 1.12], "pan": [(0.5, 0.5)] * 3, "ease": _E}},  # 12  s23-24 sealed tender to open bidding; a COE lasts ten years (11.78s)
    {"img": "ERPNEW", **{"type": "cover", "title": "A gantry of the current generation", "zoom": [1.12, 1.06, 1.0], "pan": [(0.35, 0.5)] * 3, "ease": _E}},  # 13  s25 renew at the Prevailing Quota Premium, or deregister (18.18s)
    {"img": "HERO", **{"type": "cover", "title": "An ERP gantry over the Bukit Timah Expressway", "zoom": [1.0, 1.06, 1.12], "pan": [(0.65, 0.5)] * 3, "ease": _E}},  # 14  s26-27 the growth allowance; it began at 3 per cent (8.47s)
    {"img": "G_MULTI", **{"type": "cover", "title": "An ERP gantry over a multi-lane road", "zoom": [1.12, 1.06, 1.0], "pan": [(0.5, 0.4)] * 3, "ease": _E}},  # 15  s28 cut in stages to zero (19.77s)
    {"img": "G_TOLL", **{"type": "cover", "title": "An ERP toll station gantry", "zoom": [1.0, 1.06, 1.12], "pan": [(0.5, 0.5)] * 3, "ease": _E}},  # 16  s29-30 every new car replaces one; supply follows deregistrations (17.8s)
    {"img": "ERPNEW", **{"type": "cover", "title": "A gantry of the current generation", "zoom": [1.12, 1.06, 1.0], "pan": [(0.35, 0.5)] * 3, "ease": _E}},  # 17  s31 1994: premiums break S$100,000 (14.43s)
    {"img": "G_SIGN", **{"type": "cover", "title": "An ERP gantry in the city", "zoom": [1.0, 1.06, 1.12], "pan": [(0.65, 0.5)] * 3, "ease": _E}},  # 18  s32 1997: the collapse to S$50 (25.62s)
    {"img": "HERO", **{"type": "cover", "title": "An ERP gantry over the Bukit Timah Expressway", "zoom": [1.12, 1.06, 1.0], "pan": [(0.5, 0.4)] * 3, "ease": _E}},  # 19  s33 2008: Category A closes at S$2 (12.18s)
    {"img": "G_MULTI", **{"type": "cover", "title": "An ERP gantry over a multi-lane road", "zoom": [1.0, 1.06, 1.12], "pan": [(0.5, 0.5)] * 3, "ease": _E}},  # 20  s34-35 the swings have not gentled; the 2023 records (21.0s)
    {"img": "G_TOLL", **{"type": "cover", "title": "An ERP toll station gantry", "zoom": [1.12, 1.06, 1.0], "pan": [(0.35, 0.5)] * 3, "ease": _E}},  # 21  s36-37 the S$40,000 fall; cut-and-fill (24.62s)
    {"img": "ERPNEW", **{"type": "cover", "title": "A gantry of the current generation", "zoom": [1.0, 1.06, 1.12], "pan": [(0.65, 0.5)] * 3, "ease": _E}},  # 22  s38 November 2026: Category A at S$139,001 (21.65s)
    {"img": "NIGHT", **{"type": "cover", "title": "An ERP gantry after dark", "zoom": [1.12, 1.06, 1.0], "pan": [(0.5, 0.4)] * 3, "ease": _E}},  # 23  s39-40 1998: ERP arrives; the first phase complete (24.57s)
    {"img": "G_EARLY", **{"type": "cover", "title": "An early ERP gantry", "zoom": [1.0, 1.06, 1.12], "pan": [(0.5, 0.5)] * 3, "ease": _E}},  # 24  s41 the world's first electronic road pricing (11.4s)
    {"img": "IU", **{"type": "cover", "title": "The in-vehicle unit, with its CashCard slot", "zoom": [1.12, 1.06, 1.0], "pan": [(0.35, 0.5)] * 3, "ease": _E}},  # 25  s42 every vehicle carried an In-vehicle Unit (12.72s)
    {"img": "NIGHT", **{"type": "cover", "title": "An ERP gantry after dark", "zoom": [1.0, 1.06, 1.12], "pan": [(0.65, 0.5)] * 3, "ease": _E}},  # 26  s43 volumes fell 15 per cent; speeds rose to 55 (14.32s)
    {"img": "G_MULTI", **{"type": "cover", "title": "An ERP gantry over a multi-lane road", "zoom": [1.12, 1.06, 1.0], "pan": [(0.5, 0.4)] * 3, "ease": _E}},  # 27  s44-45 priced by evidence; quarterly rate reviews (24.55s)
    {"img": "G_SIGN", **{"type": "cover", "title": "An ERP gantry in the city", "zoom": [1.0, 1.06, 1.12], "pan": [(0.5, 0.5)] * 3, "ease": _E}},  # 28  s46-47 graduated steps; more than ninety locations (16.5s)
    {"img": "G_TOLL", **{"type": "cover", "title": "An ERP toll station gantry", "zoom": [1.12, 1.06, 1.0], "pan": [(0.35, 0.5)] * 3, "ease": _E}},  # 29  s48 London, Stockholm and New York came to learn (22.95s)
    {"img": "ERPNEW", **{"type": "cover", "title": "A gantry of the current generation", "zoom": [1.0, 1.06, 1.12], "pan": [(0.65, 0.5)] * 3, "ease": _E}},  # 30  s49-50 a pair of levers, in the LTA's words (16.75s)
    {"img": "HERO", **{"type": "cover", "title": "An ERP gantry over the Bukit Timah Expressway", "zoom": [1.12, 1.06, 1.0], "pan": [(0.5, 0.4)] * 3, "ease": _E}},  # 31  s51-52 10,500 extra COEs, 1997 to 2003 (17.25s)
    {"img": "G_MULTI", **{"type": "cover", "title": "An ERP gantry over a multi-lane road", "zoom": [1.0, 1.06, 1.12], "pan": [(0.5, 0.5)] * 3, "ease": _E}},  # 32  s53 October 2024: 20,000 more announced (19.68s)
    {"img": "G_SIGN", **{"type": "cover", "title": "An ERP gantry in the city", "zoom": [1.12, 1.06, 1.0], "pan": [(0.35, 0.5)] * 3, "ease": _E}},  # 33  s54-55 the minister in Parliament; an eighth of the island (19.23s)
    {"img": "G_OBUSET", **{"type": "cover", "title": "The ERP 2.0 on-board unit set in a car", "zoom": [1.0, 1.06, 1.12], "pan": [(0.65, 0.5)] * 3, "ease": _E}},  # 34  s56 distance-based charging: possible, not decided (19.5s)
    {"img": "ERPNEW", **{"type": "cover", "title": "A gantry of the current generation", "zoom": [1.12, 1.06, 1.0], "pan": [(0.5, 0.4)] * 3, "ease": _E}},  # 35  s57-58 the dearest place in the world to buy a car (22.52s)
    {"img": "G_TOLL", **{"type": "cover", "title": "An ERP toll station gantry", "zoom": [1.0, 1.06, 1.12], "pan": [(0.5, 0.5)] * 3, "ease": _E}},  # 36  s59 a Corolla Altis at S$173,000, divided (22.2s)
    {"img": "HERO", **{"type": "cover", "title": "An ERP gantry over the Bukit Timah Expressway", "zoom": [1.12, 1.06, 1.0], "pan": [(0.35, 0.5)] * 3, "ease": _E}},  # 37  s60 S$4.66 billion in quota premiums (15.8s)
    {"img": "G_MULTI", **{"type": "cover", "title": "An ERP gantry over a multi-lane road", "zoom": [1.0, 1.06, 1.12], "pan": [(0.65, 0.5)] * 3, "ease": _E}},  # 38  s61 the criticisms, aired in Parliament (21.95s)
    {"img": "G_SIGN", **{"type": "cover", "title": "An ERP gantry in the city", "zoom": [1.12, 1.06, 1.0], "pan": [(0.5, 0.4)] * 3, "ease": _E}},  # 39  s62 the replies, also on the record (23.7s)
    {"img": "ERPNEW", **{"type": "cover", "title": "A gantry of the current generation", "zoom": [1.0, 1.06, 1.12], "pan": [(0.5, 0.5)] * 3, "ease": _E}},  # 40  s63-64 the Cat A/B merger proposal; still undecided (25.6s)
    {"img": "G_BUGIS", **{"type": "cover", "title": "The ERP gantry at Bugis", "zoom": [1.12, 1.06, 1.0], "pan": [(0.35, 0.5)] * 3, "ease": _E}},  # 41  s65-66 no study measures it; one family's decisions (21.45s)
    {"img": "G_SIGN", **{"type": "cover", "title": "An ERP gantry in the city", "zoom": [1.0, 1.06, 1.12], "pan": [(0.65, 0.5)] * 3, "ease": _E}},  # 42  s67-68 the widower; when his wife was alive the house was full (14.05s)
    {"img": "G_TOLL", **{"type": "cover", "title": "An ERP toll station gantry", "zoom": [1.12, 1.06, 1.0], "pan": [(0.5, 0.4)] * 3, "ease": _E}},  # 43  s69-70 a son in Europe, a daughter in Singapore; she thought she would stay (14.32s)
    {"img": "G_MULTI", **{"type": "cover", "title": "An ERP gantry over a multi-lane road", "zoom": [1.0, 1.06, 1.12], "pan": [(0.5, 0.5)] * 3, "ease": _E}},  # 44  s71-72 the sums on the daily drive down the Central Expressway (19.15s)
    {"img": "NIGHT", **{"type": "cover", "title": "An ERP gantry after dark", "zoom": [1.12, 1.06, 1.0], "pan": [(0.35, 0.5)] * 3, "ease": _E}},  # 45  s73-74 the price of the road outweighed the family home (11.68s)
    {"img": "G_OBUSET", **{"type": "cover", "title": "The ERP 2.0 on-board unit set in a car", "zoom": [1.0, 1.06, 1.12], "pan": [(0.65, 0.5)] * 3, "ease": _E}},  # 46  s75 the gantry network at the end of its life (5.58s)
    {"img": "OBU", **{"type": "cover", "title": "The ERP 2.0 on-board unit display", "zoom": [1.12, 1.06, 1.0], "pan": [(0.5, 0.4)] * 3, "ease": _E}},  # 47  s76 the satellite successor's decade of preparation (one long sentence) (31.12s)
    {"img": "G_OBUPROC", **{"type": "cover", "title": "The on-board unit's processing unit", "zoom": [1.0, 1.06, 1.12], "pan": [(0.5, 0.5)] * 3, "ease": _E}},  # 48  s77 the card-reach complaint, answered (13.82s)
    {"img": "G_OBUSET", **{"type": "cover", "title": "The ERP 2.0 on-board unit set in a car", "zoom": [1.12, 1.06, 1.0], "pan": [(0.35, 0.5)] * 3, "ease": _E}},  # 49  s78 more than 98 per cent fitted (11.95s)
    {"img": "DUNEARN", **{"type": "cover", "title": "Dunearn Road in 2006, its gantry overhead", "zoom": [1.0, 1.06, 1.12], "pan": [(0.65, 0.5)] * 3, "ease": _E}},  # 50  s79-80 the frames come down; Dunearn Road among the first named (19.82s)
    {"img": "G_PORTRAIT", **{"type": "cover", "title": "An ERP gantry from below", "zoom": [1.12, 1.06, 1.0], "pan": [(0.5, 0.4)] * 3, "ease": _E}},  # 51  s81-82 the 33 still working; all 95 by June 2027 (19.65s)
    {"img": "OBU", **{"type": "cover", "title": "The ERP 2.0 on-board unit display", "zoom": [1.0, 1.06, 1.12], "pan": [(0.5, 0.5)] * 3, "ease": _E}},  # 52  s83-84 blue ovals on the lanes; the unit warns and confirms (15.4s)
    {"img": "G_ERPSIGN", **{"type": "cover", "title": "The Restricted Zone sign of the ERP era", "zoom": [1.12, 1.06, 1.0], "pan": [(0.35, 0.5)] * 3, "ease": _E}},  # 53  s85 the CashCard's last day (9.1s)
    {"img": "ERPNEW", **{"type": "cover", "title": "A gantry of the current generation", "zoom": [1.0, 1.06, 1.12], "pan": [(0.65, 0.5)] * 3, "ease": _E}},  # 54  s86 1 January 2027: charging by satellite begins (19.43s)
    {"img": "NIGHT", **{"type": "cover", "title": "An ERP gantry after dark", "zoom": [1.12, 1.06, 1.0], "pan": [(0.5, 0.4)] * 3, "ease": _E}},  # 55  s87-88 the levers unchanged; steer by a painted blue oval (12.18s)
    {"img": "HERO", **{"type": "cover", "title": "An ERP gantry over the Bukit Timah Expressway", "zoom": [1.0, 1.06, 1.12], "pan": [(0.5, 0.5)] * 3, "ease": _E}},  # 56  s89-90 the bigger story: price both halves of driving (25.55s)
    {"img": "G_MULTI", **{"type": "cover", "title": "An ERP gantry over a multi-lane road", "zoom": [1.12, 1.06, 1.0], "pan": [(0.35, 0.5)] * 3, "ease": _E}},  # 57  s91-92 the hardware keeps retiring; the arithmetic doesn't (5.08s)
]

SCHEDULE = [
    (0.000, 0), (5.700, 1), (22.875, 2), (40.600, 3), (62.600, 4), (92.125, 5),
    (120.300, 6), (139.625, 7), (157.550, 8), (177.450, 9), (189.600, 10), (207.825, 11),
    (234.750, 12), (246.525, 13), (264.700, 14), (273.175, 15), (292.950, 16), (310.750, 17),
    (325.175, 18), (350.800, 19), (362.975, 20), (383.975, 21), (408.600, 22), (430.250, 23),
    (454.825, 24), (466.225, 25), (478.950, 26), (493.275, 27), (517.825, 28), (534.325, 29),
    (557.275, 30), (574.025, 31), (591.275, 32), (610.950, 33), (630.175, 34), (649.675, 35),
    (672.200, 36), (694.400, 37), (710.200, 38), (732.150, 39), (755.850, 40), (781.450, 41),
    (802.900, 42), (816.950, 43), (831.275, 44), (850.425, 45), (862.100, 46), (867.675, 47),
    (898.800, 48), (912.625, 49), (924.575, 50), (944.400, 51), (964.050, 52), (979.450, 53),
    (988.550, 54), (1007.975, 55), (1020.150, 56), (1045.700, 57)
]
TOTAL_DURATION = 1050.775
TIMING_JSON = "audio/the-coe-paying-for-permission-to-own-a-car-then-paying-again-to-drive-it.timing.json"

# The avatar presenter, cartoon with motion: corner bubble for the first and last 30 s.
AVATAR = {"ranges": [(0, 30), (-30, None)], "motion": True}
