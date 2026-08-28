"""Video config for "A Typical Day for Singapore's Silver Generation"
Watch widget and main video.

9 images: HERO (Our Tampines Hub, also front matter - used twice, once
for the AAC-hub opening and once for its own explicit mention later),
HaigRoad and Woodlands (two of Chris's own photos of Singapore fitness
corners - Haig Road shows real seniors mid-routine, Woodlands is a
static equipment shot), BedokHawker (present-day hawker centre work),
StreetVendor73/HawkerCentre73... actually HawkerCentre73 isn't used
here, keeping StreetVendor73/PublicHousing73 (1973/74 historical
photos of the informal-trade and public-housing eras this generation
lived through), CPFBuilding (the retirement scheme's former HQ),
HDBLivingRoom (a recreated 1970s/80s flat, for the "large families"
paragraph), EastCoastParkway (Chris's own third fitness-corner photo,
a different seaside setting, used as the closing present-day image).

10 slides follow the narrative arc: opening/AAC hub -> morning exercise
-> hawker work -> historical informal trade -> CPF history -> large
families/HDB living -> public housing construction -> fitness corner
(as "infrastructure built for seniors") -> Tampines Hub again (its own
explicit mention) -> closing seaside fitness corner.

Aspect check (1280x720 target, 1.778): HERO (1.778) is cover; BedokHawker/
StreetVendor73/PublicHousing73 (1.5) are cover; HaigRoad/Woodlands/
EastCoastParkway (1.33) and HDBLivingRoom (1.333) are letterbox - below
the ~1.44 threshold this project has used elsewhere; CPFBuilding (0.667,
portrait) is letterbox.
"""

IMAGES = {
    "HERO": "https://upload.wikimedia.org/wikipedia/commons/7/7a/Our_Tampines_Hub_Town_Square.jpg",
    "HAIGROAD": "/assets/images/haig_road_park_connector.jpeg",
    "WOODLANDS": "https://upload.wikimedia.org/wikipedia/commons/7/75/Outdoor_adult_exercise_equipment_on_Woodlands_Street_83%2C_Singapore.jpg",
    "BEDOKHAWKER": "https://upload.wikimedia.org/wikipedia/commons/6/66/Bedok_Hawker_Centre.jpg",
    "STREETVENDOR73": "https://upload.wikimedia.org/wikipedia/commons/e/ef/Singapore-Street_Vendor_1973-74-WUS08155.jpg",
    "CPFBUILDING": "https://upload.wikimedia.org/wikipedia/commons/c/cf/CPF_Building.jpg",
    "HDBLIVINGROOM": "https://upload.wikimedia.org/wikipedia/commons/1/15/HDB_living_room_%281970s_and_1980s%29%2C_Singapore_History_Gallery%2C_National_Museum_of_Singapore_-_20151125-01.jpg",
    "PUBLICHOUSING73": "https://upload.wikimedia.org/wikipedia/commons/8/87/Singapore-Public_Housing-1973-74-WUS08215.jpg",
    "EASTCOASTPARKWAY": "/assets/images/east_cost_parkway.jpeg",
}

SLIDES = [
    {"img": "HERO", "type": "cover", "zoom": [1, 1.07, 1.14], "pan": [(0.45, 0.5), (0.5, 0.5), (0.55, 0.5)], "ease": "ease-in-out"},
    {"img": "HAIGROAD", "type": "letterbox", "zoom": [1, 1.08, 1.16], "pan": [(0.5, 0.5), (0.5, 0.5), (0.5, 0.5)], "ease": "ease-out"},
    {"img": "BEDOKHAWKER", "type": "cover", "zoom": [1.15, 1.07, 1], "pan": [(0.55, 0.5), (0.5, 0.5), (0.45, 0.5)], "ease": "ease-in"},
    {"img": "STREETVENDOR73", "type": "cover", "zoom": [1, 1.08, 1.16], "pan": [(0.45, 0.45), (0.5, 0.5), (0.55, 0.55)], "ease": "ease-in-out"},
    {"img": "CPFBUILDING", "type": "letterbox", "zoom": [1, 1.06, 1.12], "pan": [(0.5, 0.5), (0.5, 0.5), (0.5, 0.5)], "ease": "ease-out"},
    {"img": "HDBLIVINGROOM", "type": "letterbox", "zoom": [1.14, 1.07, 1], "pan": [(0.5, 0.55), (0.5, 0.5), (0.5, 0.45)], "ease": "ease-in"},
    {"img": "PUBLICHOUSING73", "type": "cover", "zoom": [1, 1.08, 1.16], "pan": [(0.4, 0.5), (0.5, 0.5), (0.6, 0.5)], "ease": "ease-in-out"},
    {"img": "WOODLANDS", "type": "letterbox", "zoom": [1, 1.07, 1.14], "pan": [(0.5, 0.5), (0.5, 0.5), (0.5, 0.5)], "ease": "ease-out"},
    {"img": "HERO", "type": "cover", "zoom": [1.14, 1.07, 1], "pan": [(0.55, 0.55), (0.5, 0.5), (0.45, 0.45)], "ease": "ease-in"},
    {"img": "EASTCOASTPARKWAY", "type": "letterbox", "zoom": [1, 1.06, 1.12], "pan": [(0.5, 0.5), (0.5, 0.5), (0.5, 0.5)], "ease": "ease-out"},
]

# Real values from audio/a-typical-day-for-singapores-silver-generation.timing.json.
# Schedule points skip the shortest/transitional sentences (1, 4, 6, 8),
# letting each visual hold through them rather than cutting rapidly -
# their content still gets shown under the preceding slide.
SCHEDULE = [
    (0.0, 0), (15.125, 1), (23.5, 2), (42.525, 3), (61.85, 4),
    (80.4, 5), (91.45, 6), (98.85, 7), (119.55, 8), (140.425, 9),
]
TOTAL_DURATION = 161.875
TIMING_JSON = "audio/a-typical-day-for-singapores-silver-generation.timing.json"
