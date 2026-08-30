"""Video config for "The Satay Club Moved Four Times. The Satay Stayed the
Same." - Watch widget and main video.

No chart in this post, but there is a locations map: an annotated
OpenStreetMap tile (assets/images/satay-club-locations-map.png,
committed per the route-walk / OSM convention) marking the club's homes
and the two later revivals. It runs twice - on the "moved four times"
beat and on the mid-1950s Dhoby Ghaut detour.

Images (5 post + 8 gallery, minus the c.1880 dhoby-field gallery photo,
which stays gallery-only):
  HERO       - satay being prepared at the Esplanade Satay Club, 1973-74
               (post hero)
  SATMAP     - the annotated locations map (Map data (c) OpenStreetMap
               contributors)
  ALHAMBRA   - the Alhambra Cinema on Beach Road, 1920s - beside the
               Satay Club's first location
  ESP_VIEW   - a general view of the Esplanade Satay Club, 1973-74
  SATAYPREP2 - another view of satay preparation there, 1973-74
  FOODSTALL  - a food stall at the Esplanade Satay Club, 1973-74
  QEWALK     - Queen Elizabeth Walk, 2006
  ESP_THEA   - Esplanade - Theatres on the Bay, built on the cleared site
  INSIDE_SBTB- inside Satay by the Bay, 2026
  SBTB       - Satay by the Bay, exterior, 2026
  LAUPASAT25 - satay at Lau Pa Sat, 2025
  LAUPASAT24 - satay at Lau Pa Sat, 2024
  SATE_RT    - sate prepared for a Dutch rijsttafel, Dutch East Indies,
               1943-45

18 slides, 311.125s. Aspect check (1280x720, ~1.44 cover threshold):
  HERO 5916x3941 (1.50)       -> cover, horizontal pan
  SATMAP 1238x702 (1.76)      -> letterbox (exact-ish fit), near-zero zoom
  ALHAMBRA 696x444 (1.57)     -> letterbox (low-res 1920s photo)
  ESP_VIEW 5859x3906 (1.50)   -> cover, horizontal pan
  SATAYPREP2 4344x2893 (1.50) -> cover, horizontal pan
  FOODSTALL 5859x3906 (1.50)  -> cover, horizontal pan
  QEWALK 1600x1200 (1.33)     -> letterbox
  ESP_THEA 5402x3601 (1.50)   -> cover, horizontal pan
  INSIDE_SBTB 4000x3000 (1.33)-> letterbox
  SBTB 4000x3000 (1.33)       -> letterbox
  LAUPASAT25 8064x6048 (1.33) -> letterbox
  LAUPASAT24 8064x6048 (1.33) -> letterbox
  SATE_RT 3095x2549 (1.21)    -> letterbox
Letterbox slides use zero pan (blurred-bg zoom only), so --check-only
flags them JERKY - the documented letterbox false positive (pipeline
section 5); the near-static SATMAP slides read JERKY for the same
reason. Four slides run 21-28s over a single long sentence with no
internal timing.json boundary to cut on; slow zooms carry them.
"""

_C = "https://upload.wikimedia.org/wikipedia/commons"

IMAGES = {
    "HERO": f"{_C}/0/0a/Singapore-Satay-1973-74-WUS08150.jpg",
    "SATMAP": "/assets/images/satay-club-locations-map.png",
    "ALHAMBRA": f"{_C}/5/5e/1920s_photo_of_Marlborough_Cinema_and_the_next-door_Alhambra_Cinema.jpg",
    "ESP_VIEW": f"{_C}/6/6d/Singapore-Hawker_Centre.1973-74-WUS08151.jpg",
    "SATAYPREP2": f"{_C}/2/2f/Singapore-Satay-1973-74-WUS08150-2.jpg",
    "FOODSTALL": f"{_C}/9/97/Singapore-Food_stall-1973-74-WUS08236.jpg",
    "QEWALK": f"{_C}/4/40/Queen_Elizabeth_Walk%2C_Aug_06.JPG",
    "ESP_THEA": f"{_C}/d/d4/Esplanade_Theatres_on_the_Bay_Singapore_at_blue_hour.jpg",
    "INSIDE_SBTB": f"{_C}/e/ee/Satay_by_the_Bay_%2814314%29.jpg",
    "SBTB": f"{_C}/8/8d/Satay_by_the_Bay.jpg",
    "LAUPASAT25": f"{_C}/4/4f/Lau_Pa_Sat_satay_and_shrimp_10-08-2025.jpg",
    "LAUPASAT24": f"{_C}/8/86/Lau_Pa_Sat_satay_and_shrimp_04-12-2024.jpg",
    "SATE_RT": f"{_C}/f/f6/Collectie_Wereldmuseum%2C_TM-FV-0586-104%2C_Foto%2C_%27Bereiding_van_sat%C3%A9_voor_een_offici%C3%ABle_rijsttafel_met_leden_van_de_luchtmacht_en_de_NICA%2C_tijdens_de_bevrijding_van_Nieuw-Guinea%27%2C_1943-1945.jpg",
}

CREDITS = {
    "SATMAP": "Locations map by Lesser Known Singapore; base map data © OpenStreetMap contributors",
}

SLIDES = [
    {"img": "HERO", "type": "cover", "zoom": [1, 1.05, 1.10], "pan": [(0.3, 0.5), (0.5, 0.5), (0.7, 0.5)], "ease": "ease-in-out"},
    {"img": "SATMAP", "type": "letterbox", "zoom": [1, 1.01, 1.02], "pan": [(0.5, 0.5), (0.5, 0.5), (0.5, 0.5)], "ease": "linear"},
    {"img": "ALHAMBRA", "type": "letterbox", "zoom": [1, 1.05, 1.10], "pan": [(0.5, 0.5), (0.5, 0.5), (0.5, 0.5)], "ease": "ease-in"},
    {"img": "SATMAP", "type": "letterbox", "zoom": [1.02, 1.01, 1], "pan": [(0.5, 0.5), (0.5, 0.5), (0.5, 0.5)], "ease": "linear"},
    {"img": "QEWALK", "type": "letterbox", "zoom": [1, 1.05, 1.10], "pan": [(0.5, 0.5), (0.5, 0.5), (0.5, 0.5)], "ease": "ease-in-out"},
    {"img": "ESP_VIEW", "type": "cover", "zoom": [1, 1.05, 1.10], "pan": [(0.2, 0.5), (0.5, 0.5), (0.8, 0.5)], "ease": "ease-in-out"},
    {"img": "SATAYPREP2", "type": "cover", "zoom": [1, 1.06, 1.12], "pan": [(0.35, 0.5), (0.5, 0.5), (0.65, 0.5)], "ease": "ease-in-out"},
    {"img": "ESP_THEA", "type": "cover", "zoom": [1, 1.05, 1.10], "pan": [(0.15, 0.5), (0.5, 0.5), (0.85, 0.5)], "ease": "ease-in-out"},
    {"img": "FOODSTALL", "type": "cover", "zoom": [1, 1.06, 1.12], "pan": [(0.3, 0.5), (0.5, 0.5), (0.7, 0.5)], "ease": "ease-in"},
    {"img": "INSIDE_SBTB", "type": "letterbox", "zoom": [1, 1.05, 1.10], "pan": [(0.5, 0.5), (0.5, 0.5), (0.5, 0.5)], "ease": "ease-in-out"},
    {"img": "SBTB", "type": "letterbox", "zoom": [1, 1.05, 1.10], "pan": [(0.5, 0.5), (0.5, 0.5), (0.5, 0.5)], "ease": "ease-in"},
    {"img": "ALHAMBRA", "type": "letterbox", "zoom": [1.10, 1.05, 1], "pan": [(0.5, 0.5), (0.5, 0.5), (0.5, 0.5)], "ease": "ease-out"},
    {"img": "HERO", "type": "cover", "zoom": [1, 1.06, 1.12], "pan": [(0.7, 0.5), (0.5, 0.5), (0.3, 0.5)], "ease": "ease-in-out"},
    {"img": "SATAYPREP2", "type": "cover", "zoom": [1.12, 1.06, 1], "pan": [(0.65, 0.5), (0.5, 0.5), (0.35, 0.5)], "ease": "ease-out"},
    {"img": "LAUPASAT25", "type": "letterbox", "zoom": [1, 1.05, 1.10], "pan": [(0.5, 0.5), (0.5, 0.5), (0.5, 0.5)], "ease": "ease-in-out"},
    {"img": "SATE_RT", "type": "letterbox", "zoom": [1, 1.03, 1.06], "pan": [(0.5, 0.5), (0.5, 0.5), (0.5, 0.5)], "ease": "linear"},
    {"img": "LAUPASAT24", "type": "letterbox", "zoom": [1, 1.05, 1.10], "pan": [(0.5, 0.5), (0.5, 0.5), (0.5, 0.5)], "ease": "ease-in"},
    {"img": "HERO", "type": "cover", "zoom": [1, 1.05, 1.10], "pan": [(0.4, 0.5), (0.5, 0.5), (0.6, 0.5)], "ease": "ease-in-out"},
]

# Real values from audio/satay-club-esplanade-alhambra-history.timing.json.
# Every point is a real sentence start.
#   0  s0-2   title; "I went to the Esplanade Satay Club as a kid"
#   1  s3-4   that wasn't where it started - it moved four times before it
#             finally closed for good (SATMAP)
#   2  s5     the first Satay Club: Hoi How Road, flanked by two cinemas
#             (one the Alhambra) and the Volunteer Corps HQ
#   3  s6     mid-1950s to a field by Dhoby Ghaut; trade dried up; a
#             petition brought them back to Beach Road (SATMAP)
#   4  s7     they stayed until 1970, then were moved to the Esplanade /
#             Queen Elizabeth Walk
#   5  s8     the January 1971 version everyone remembers - "romantic
#             spot", "iconic waterfront hawker haven", the STB brochures
#   6  s9     ~26 stalls, nearly all satay, billed by the skewer
#   7  s10-11 1995: the site cleared for the arts centre and Nicoll
#             Highway; stallholders given to May to move
#   8  s12-13 eight try Clarke Quay (rent S$300 -> S$3,000); a later
#             Esplanade Bridge attempt folds
#   9  s14    Satay by the Bay opens 2013 - "reminiscent of the old Satay
#             Club", a themed recreation for tourists
#   10 s15    the closest thing to a real survivor is easy to walk past
#   11 s16    Encik Saiful bin Haji Juwahir's Original Alhambra Satay -
#             the recipe traces to his father's first Beach Road stall
#   12 s17    inherited 1980; every stick by hand - charcoal, thigh meat,
#             an eight-spice marinade
#   13 s18-19 the last of the original stallholders; what persisted is the
#             food, moving two ways at once
#   14 s20    locally satay got pricier - 30 cents in the 1980s to a
#             dollar-plus now, bar one stubborn Geylang Bahru stall
#   15 s21    the dish travelled the other way - Dutch "sate", South
#             African "sosatie", every continent
#   16 s22-24 the pavement I sat on went under the road and the arts
#             centre; the skewer itself hasn't gone anywhere
#   17 s25    four moves, two failed revivals, one themed recreation - and
#             it outlived all of them
SCHEDULE = [
    (0.0, 0), (15.375, 1), (30.725, 2), (44.975, 3), (58.25, 4),
    (70.175, 5), (90.0, 6), (102.1, 7), (118.375, 8), (137.05, 9),
    (155.575, 10), (161.925, 11), (182.825, 12), (201.45, 13), (218.175, 14),
    (242.65, 15), (270.475, 16), (293.375, 17),
]
TOTAL_DURATION = 311.125
TIMING_JSON = "audio/satay-club-esplanade-alhambra-history.timing.json"
