"""Video config for the William Farquhar post.

Nine images: his own portrait, a matching portrait of Raffles for
contrast, three pieces of the natural history collection he
commissioned (tapir, colugo, durian), the 1822 Jackson town plan, the
present-day Raffles statue and its plaque (the erasure beat), and the
present-day Farquhar Garden at Fort Canning (opening/closing bookend).

  HERO      - Farquhar portrait, c. 1830 (hero)
  RAFFLES   - Raffles portrait, by George Francis Joseph
  TAPIR     - Tapir of Malacca, William Farquhar Collection
  COLUGO    - Flying maucauco with its young, William Farquhar Collection
  DURIAN    - Durio zibethinus, William Farquhar Collection
  JACKSON   - Plan of the Town of Singapore, 1822
  STATUE    - Raffles statue at his landing site, present day
  PLAQUE    - close-up of the statue's English-language plaque
  GARDEN    - the Farquhar Garden at Fort Canning, present day

Both portraits and the label-heavy Jackson plan use letterbox (cover
would crop a face or the plan's text labels - see
docs/production-pipeline.md §3); the natural history drawings (tapir,
colugo) are close to landscape and use cover; DURIAN, STATUE, GARDEN
are portrait-oriented sources and use letterbox too.

50 slides, 498.625s.
"""

_U = "https://upload.wikimedia.org/wikipedia/commons"
_C = f"{_U}/thumb"

IMAGES = {
    "HERO": f"{_U}/f/f9/Portrait_of_William_Farquhar_%28c._1830%29.jpg",
    "RAFFLES": f"{_U}/a/a0/George_Francis_Joseph_-_Sir_Thomas_Stamford_Bingley_Raffles.jpg",
    "TAPIR": f"{_U}/1/18/Tapir_of_Malacca_%28William_Farquhar_Collection%2C_1819%E2%80%931823%29.jpg",
    "COLUGO": f"{_U}/7/76/Flying_maucauco_with_its_young_%28William_Farquhar_Collection%2C_1819%E2%80%931823%29.jpg",
    "DURIAN": f"{_U}/4/4b/Durio_zibethinus%3B_Doorian%3B_Boorong_Brass_Brass_%28William_Farquhar_Collection%2C_1819%E2%80%931823%29.jpg",
    "JACKSON": f"{_U}/6/60/Plan_of_the_Town_of_Singapore_%281822%29_by_Lieutenant_Philip_Jackson.jpg",
    "STATUE": f"{_U}/b/b4/Stamford_Raffles_Monument_near_Singapore_River.jpg",
    "PLAQUE": f"{_C}/6/68/RafflesStatue-EnglishPlaque-RafflesLandingSite-Singapore-20100803.jpg/1280px-RafflesStatue-EnglishPlaque-RafflesLandingSite-Singapore-20100803.jpg",
    "GARDEN": f"{_U}/1/1d/View_from_William_Farquhar%27s_Garden.jpg",
}

_CVZ = {"type": "cover", "zoom": [1.0, 1.06, 1.12], "pan": [(0.5, 0.5)] * 3, "ease": "ease-in-out"}
_CVZO = {"type": "cover", "zoom": [1.12, 1.06, 1.0], "pan": [(0.5, 0.5)] * 3, "ease": "ease-out"}
_LTB = {"type": "letterbox", "zoom": [1.0, 1.04, 1.08], "pan": [(0.5, 0.5)] * 3, "ease": "ease-in-out"}
_LTBO = {"type": "letterbox", "zoom": [1.08, 1.04, 1.0], "pan": [(0.5, 0.5)] * 3, "ease": "ease-out"}

SLIDES = [
    {"img": "HERO", **_LTB},       # 0  s0   title
    {"img": "GARDEN", **_LTB},     # 1  s1   Fort Canning garden, framed like his drawings
    {"img": "HERO", **_LTBO},      # 2  s2   almost nobody knows who Farquhar was
    {"img": "JACKSON", **_LTB},    # 3  s3   ran Singapore nearly 4.5 years
    {"img": "RAFFLES", **_LTB},    # 4  s4   Raffles, synonymous with the founding
    {"img": "RAFFLES", **_LTBO},   # 5  s5   an odd footnote in most national histories
    {"img": "HERO", **_LTB},       # 6  s6   a founding myth, a man written out
    {"img": "HERO", **_LTBO},      # 7  s7   Farquhar arrived Malacca 1795
    {"img": "HERO", **_LTB},       # 8  s8   two decades, anti-slavery, nine governors
    {"img": "TAPIR", **_CVZ},      # 9  s9   also, by inclination, a naturalist
    {"img": "DURIAN", **_LTBO},    # 10 s10  commissioned Chinese artists, 477 drawings
    {"img": "GARDEN", **_LTBO},    # 11 s11  Farquhar Garden echoes the collection
    {"img": "COLUGO", **_CVZ},     # 12 s12  Britain returned Malacca to the Dutch, 1815
    {"img": "JACKSON", **_LTBO},   # 13 s13  Aug 1818, treaty with the Sultan of Johor
    {"img": "HERO", **_LTBO},      # 14 s14  Carimon Islands unsuitable, proposed Singapore
    {"img": "HERO", **_LTB},       # 15 s15  Governor-General put him in charge
    {"img": "RAFFLES", **_LTB},    # 16 s16  Raffles landed 28 Jan 1819
    {"img": "RAFFLES", **_LTBO},   # 17 s17  he left the very next day
    {"img": "HERO", **_LTB},       # 18 s18  Farquhar stayed on as Resident
    {"img": "JACKSON", **_LTBO},   # 19 s19  what Farquhar built not really in dispute
    {"img": "HERO", **_LTB},       # 20 s20  cleared 650,000 square yards
    {"img": "JACKSON", **_LTB},    # 21 s21  first survey, first town plan, 1821
    {"img": "HERO", **_LTBO},      # 22 s22  rediscovered the harbour, drew in trade
    {"img": "HERO", **_LTB},       # 23 s23  asylum for Prince Belawa and Bugis refugees
    {"img": "JACKSON", **_LTBO},   # 24 s24  backed the settlement's first school
    {"img": "JACKSON", **_LTB},    # 25 s25  population grown to roughly 5,000
    {"img": "RAFFLES", **_LTB},    # 26 s26  none of it happened because Raffles was away
    {"img": "HERO", **_LTBO},      # 27 s27  the two men clashed on real substance
    {"img": "RAFFLES", **_LTBO},   # 28 s28  opium revenue licences
    {"img": "JACKSON", **_LTB},    # 29 s29  the East Beach town-planning dispute
    {"img": "HERO", **_LTB},       # 30 s30  a genuine difference in how each saw the place
    {"img": "HERO", **_LTBO},      # 31 s31  Farquhar still saw a Malay political order
    {"img": "RAFFLES", **_LTB},   # 32 s32  Raffles returned, October 1822
    {"img": "RAFFLES", **_LTBO},  # 33 s33  that didn't last
    {"img": "RAFFLES", **_LTB},   # 34 s34  excluded from the Town Committee
    {"img": "RAFFLES", **_LTBO},  # 35 s35  Jan 1823, not capable of the job
    {"img": "JACKSON", **_LTBO},  # 36 s36  next day, celebrating a great emporium
    {"img": "HERO", **_LTB},      # 37 s37  1 May 1823, dismissed as Resident
    {"img": "HERO", **_LTBO},     # 38 s38  Crawfurd arrives, dismissed a second time
    {"img": "HERO", **_LTB},      # 39 s39  appealed to Bengal and lost
    {"img": "HERO", **_LTBO},     # 40 s40  left Singapore, 28 Dec 1823
    {"img": "HERO", **_LTB},      # 41 s41  the farewell addresses, $3,000 in silverware
    {"img": "STATUE", **_LTB},    # 42 s42  the official record won out anyway
    {"img": "RAFFLES", **_LTBO},  # 43 s43  Boulger's 1897 biography set the template
    {"img": "STATUE", **_LTBO},   # 44 s44  a statue, an MRT station
    {"img": "PLAQUE", **_LTB},    # 45 s45  Farquhar Street, Mount Farquhar, gone
    {"img": "HERO", **_LTBO},     # 46 s46  modern historians pushed back for decades
    {"img": "HERO", **_LTB},      # 47 s47  his own tombstone, in Perth, Scotland
    {"img": "STATUE", **_LTBO},   # 48 s48  why it matters today
    {"img": "GARDEN", **_LTB},    # 49 s49  closing
]

SCHEDULE = [
    (0.000, 0), (5.025, 1), (22.575, 2), (28.425, 3), (32.375, 4),
    (41.725, 5), (47.175, 6), (55.925, 7), (70.450, 8), (87.775, 9),
    (91.675, 10), (112.975, 11), (125.900, 12), (140.675, 13), (147.800, 14),
    (156.300, 15), (164.000, 16), (178.600, 17), (181.075, 18), (188.750, 19),
    (195.475, 20), (206.875, 21), (219.325, 22), (232.675, 23), (240.225, 24),
    (246.400, 25), (254.750, 26), (262.850, 27), (268.150, 28), (281.975, 29),
    (302.775, 30), (311.375, 31), (318.750, 32), (328.100, 33), (330.025, 34),
    (345.000, 35), (352.950, 36), (364.325, 37), (376.725, 38), (383.925, 39),
    (387.250, 40), (396.700, 41), (414.075, 42), (417.550, 43), (429.225, 44),
    (436.475, 45), (442.425, 46), (453.325, 47), (466.150, 48), (476.775, 49),
]
TOTAL_DURATION = 498.625
TIMING_JSON = "audio/william-farquhar-the-co-founder-written-out-of-the-story.timing.json"
