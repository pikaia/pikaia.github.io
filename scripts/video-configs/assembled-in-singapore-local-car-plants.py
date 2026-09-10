"""Video config for the "Assembled in Singapore" car-plants post.

A genuinely image-thin topic - no period photography of the assembly
lines exists - so the set leans on the Former Ford Factory (five views:
two exteriors, the museum interior, the monument plaque, the "Peace"
sculpture), the 1942 surrender signed inside it, a 1924 Model T, the
Temasek Shophouse on the old Orchard Road showroom stretch, and a
present-day Ioniq 5 and its robotaxi version for the Jurong return.

  IONIQ5        - a Hyundai Ioniq 5, the model built at HMGICS (title / bookend)
  HERO_FORD     - the Former Ford Factory, white Art Deco frontage + sign (2017)
  FORD2025      - the same building, a 2025 view
  FORD_INT      - inside the Former Ford Factory museum
  PLAQUE        - the building's national-monument plaque
  PEACE         - the "Peace" sculpture outside the factory
  MODELT        - an unrestored 1924 Ford Model T Tourer (museum piece)
  SURRENDER     - Yamashita and Percival at the surrender table, 15 Feb 1942
  SURRENDER_FLAG - Percival's party carrying the Union flag to surrender, 1942
  TEMASEK       - Temasek Shophouse, 28 Orchard Road, restored 2019
  ROBOTAXI      - the driverless Ioniq 5 robotaxi

All photos, centred cover zoom, no horizontal pan. HERO_FORD and
FORD_INT are taller than 16:9 with the building's flagpole/tower high in
frame, so they take a raised crop (_TOPM); see docs/production-pipeline.md
s3.

41 slides, 613.15s.
"""

_U = "https://upload.wikimedia.org/wikipedia/commons"
_C = f"{_U}/thumb"

IMAGES = {
    "IONIQ5": f"{_C}/4/4d/Hyundai_Ioniq_5.jpg/1280px-Hyundai_Ioniq_5.jpg",
    "HERO_FORD": f"{_C}/2/22/Old_Ford_Motor_Factory_-_www.joyofmuseums.com_-_external.jpg/1280px-Old_Ford_Motor_Factory_-_www.joyofmuseums.com_-_external.jpg",
    "FORD2025": f"{_C}/7/7c/Former_Ford_Factory%2C_October_2025.jpg/1280px-Former_Ford_Factory%2C_October_2025.jpg",
    "FORD_INT": f"{_C}/5/54/Old_Ford_Motor_Factory_-_www.joyofmuseums.com_-_internal.jpg/1280px-Old_Ford_Motor_Factory_-_www.joyofmuseums.com_-_internal.jpg",
    "PLAQUE": f"{_C}/8/8d/Plaque%28former-ford-factory%29.jpg/1280px-Plaque%28former-ford-factory%29.jpg",
    "PEACE": f"{_U}/f/f3/Peace_by_Chua_Boon_Kee%2C_Old_Ford_Motor_Factory%2C_Singapore_-_20070316.jpg",
    "MODELT": f"{_C}/3/3f/1924_Ford_T_Tourer_%2814467176824%29.jpg/1280px-1924_Ford_T_Tourer_%2814467176824%29.jpg",
    "SURRENDER": f"{_U}/4/40/Yamashita_and_Percival_discuss_surrender_terms.jpg",
    "SURRENDER_FLAG": f"{_C}/a/a6/Surrender_Singapore.jpg/1280px-Surrender_Singapore.jpg",
    "TEMASEK": f"{_C}/c/c7/Temasek_Shophouse%2C_Singapore_-_03.jpg/1280px-Temasek_Shophouse%2C_Singapore_-_03.jpg",
    "ROBOTAXI": f"{_C}/d/df/Hyundai_Ioniq_5_Robotaxi_IAA_2021_1X7A0002.jpg/1280px-Hyundai_Ioniq_5_Robotaxi_IAA_2021_1X7A0002.jpg",
}

_CVZ = {"type": "cover", "zoom": [1.0, 1.06, 1.12], "pan": [(0.5, 0.5)] * 3, "ease": "ease-in-out"}
_CVZO = {"type": "cover", "zoom": [1.12, 1.06, 1.0], "pan": [(0.5, 0.5)] * 3, "ease": "ease-out"}

# Raised crop for a source taller than 16:9 whose subject sits high (the
# Ford building's flagpole/tower). Merge after the cover preset so the pan
# wins. See docs/production-pipeline.md s3.
_TOPM = {"pan": [(0.5, 0.33)] * 3}

SLIDES = [
    {"img": "IONIQ5", **_CVZ},                    # 0  s0-1   title; Hyundai builds EVs in Jurong since 2023
    {"img": "HERO_FORD", **_CVZ, **_TOPM},        # 1  s2-3   the gap looks natural; but for half a century it did assemble
    {"img": "FORD2025", **_CVZO},                 # 2  s4     never large, never lasted; the last shut in 1980
    {"img": "MODELT", **_CVZ},                    # 3  s5-6   it starts with Ford; incorporated 1926, a shophouse off Enggor St
    {"img": "HERO_FORD", **_CVZO, **_TOPM},       # 4  s7     "generous to call it an assembly plant" - fitting wheels to Model Ts
    {"img": "FORD_INT", **_CVZ, **_TOPM},         # 5  s8     1929 Prince Edward Road; 1930 semi-knocked-down kits for re-export
    {"img": "MODELT", **_CVZO},                   # 6  s9-10  Ford did well; 80% of the Malayan market by 1939
    {"img": "HERO_FORD", **_CVZ, **_TOPM},        # 7  s11    1941: the Bukit Timah plant, Brizay's Art Deco, the green windows
    {"img": "FORD2025", **_CVZ},                  # 8  s12    the first full assembly plant in Southeast Asia; body assembly
    {"img": "SURRENDER", **_CVZ},                 # 9  s13-14 the plant's most famous day; the surrender signed at the table
    {"img": "SURRENDER_FLAG", **_CVZ},            # 10 s15    the occupation; the Japanese assemble Nissan trucks here
    {"img": "FORD_INT", **_CVZO, **_TOPM},        # 11 s16    back to Ford 1946; resumed 1947; CKD kits from five countries
    {"img": "HERO_FORD", **_CVZO, **_TOPM},       # 12 s17    closed June 1980; 150,000 vehicles; 16 workers grown to 300
    {"img": "FORD2025", **_CVZO},                 # 13 s18    the only assembler here until 1965 - the action was next door
    {"img": "MODELT", **_CVZ},                    # 14 s19-20 import-substitution behind a tariff wall; cars an obvious target
    {"img": "HERO_FORD", **_CVZ, **_TOPM},        # 15 s21    1963: Malaysia invites plants; a cluster in Johor and Selangor
    {"img": "PLAQUE", **_CVZ},                    # 16 s22-23 in Malaysia, then separate; on the wrong side of the arithmetic
    {"img": "HERO_FORD", **_CVZO, **_TOPM},       # 17 s24-25 plants went where the customers were; Proton 1983, Singapore nothing
    {"img": "FORD_INT", **_CVZ, **_TOPM},         # 18 s26-27 a few lines of its own: Cycle & Carriage, Mercedes at Hillview, 1965
    {"img": "FORD2025", **_CVZ},                  # 19 s28    four assemblers by the 1970s: Ford, C&C, Nissan, Volvo
    {"img": "MODELT", **_CVZO},                   # 20 s29    all of them there for the same reason - the tariff
    {"img": "HERO_FORD", **_CVZ, **_TOPM},        # 21 s30    the tariff was the whole business model
    {"img": "FORD_INT", **_CVZO, **_TOPM},        # 22 s31    the EDB bet on exports - electronics, oil, ship repair - not protection
    {"img": "PLAQUE", **_CVZO},                   # 23 s32    propping up sub-scale car lines was the opposite kind of policy
    {"img": "FORD2025", **_CVZ},                  # 24 s33-34 the protection came off; 1980, the tariff advantage withdrawn
    {"img": "PLAQUE", **_CVZ},                    # 25 s35    within the year all four stopped assembling
    {"img": "PEACE", **_CVZ},                     # 26 s36-37 Ford left; C&C's plant became a respray shop, then terrace homes
    {"img": "HERO_FORD", **_CVZO, **_TOPM},       # 27 s38    the Ford building: half of it a condo, the rest a monument
    {"img": "TEMASEK", **_CVZ},                   # 28 s39-40 four decades of no cars; the motor trade became importing and reselling
    {"img": "PLAQUE", **_CVZO},                   # 29 s41    among the world's most expensive cars; none of it paid to a builder here
    {"img": "TEMASEK", **_CVZO},                  # 30 s42    the selling side left better buildings behind
    {"img": "MODELT", **_CVZ},                    # 31 s43    Malayan Motors, a Wearne Brothers firm - Rover, Rolls-Royce, Studebaker
    {"img": "PEACE", **_CVZO},                    # 32 s44    its last sale, August 1980; the building became offices, then a college
    {"img": "TEMASEK", **_CVZ},                   # 33 s45    the 1928 block beside it, restored, reopened 2019 as Temasek Shophouse
    {"img": "ROBOTAXI", **_CVZ},                  # 34 s46    Hyundai's Innovation Centre Singapore, Jurong, 2023
    {"img": "IONIQ5", **_CVZO},                   # 35 s47    ~30,000 EVs a year: the Ioniq 5, a robotaxi, the Ioniq 6 to come
    {"img": "ROBOTAXI", **_CVZO},                 # 36 s48    heavily automated, cell-based, a digital twin, a rooftop test track
    {"img": "IONIQ5", **_CVZ},                    # 37 s49    "less a factory than a place to work out how cars might be made"
    {"img": "HERO_FORD", **_CVZ, **_TOPM},        # 38 s50-51 the old plants: low-skill lines kept alive by a tax on the alternative
    {"img": "IONIQ5", **_CVZO},                   # 39 s52-53 the Jurong plant: capital-intensive, research; cars again, opposite terms
    {"img": "HERO_FORD", **_CVZO, **_TOPM},       # 40 s54-55 where it fits: a measure of how Singapore chooses to make things
]

SCHEDULE = [
    (0.0, 0), (19.025, 1), (35.975, 2), (47.225, 3), (67.325, 4),
    (77.65, 5), (96.95, 6), (112.975, 7), (129.0, 8), (138.95, 9),
    (157.5, 10), (164.75, 11), (180.875, 12), (191.075, 13), (201.8, 14),
    (221.625, 15), (243.0, 16), (263.075, 17), (279.875, 18), (302.8, 19),
    (313.5, 20), (323.925, 21), (330.6, 22), (352.9, 23), (360.5, 24),
    (373.35, 25), (380.15, 26), (393.9, 27), (410.2, 28), (430.75, 29),
    (440.25, 30), (447.625, 31), (466.55, 32), (480.15, 33), (501.4, 34),
    (512.6, 35), (526.975, 36), (541.975, 37), (549.975, 38), (568.575, 39),
    (586.125, 40),
]
TOTAL_DURATION = 613.15
TIMING_JSON = "audio/assembled-in-singapore-local-car-plants.timing.json"
