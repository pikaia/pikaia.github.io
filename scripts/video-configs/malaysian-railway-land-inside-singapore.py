"""Video config for "The Strip of Malaysia That Ran Through Singapore
Until 2011" - Watch widget and main video.

Two diagrams with CREDITS lines: the OSM map of the former KTM line down
the island (render_malaysian_railway_land_map.py) and the 1903-to-present
timeline (render_malaysian_railway_land_timeline.py), the latter shown
static (zoom held at 1.0) while the narration walks it.

This is a policy-and-history story with very little freely-licensed
photography - a station, a strip of land, a green trail - so the station
facade, the interior hall, the platforms and especially the map recur
many times, re-triggering a fresh slow zoom. 9 image assets (3 captioned
in the post, 4 in the gallery, 2 originals with CREDITS), so
stage_youtube_text.py resolves every credit.

The timeline slide is letterbox + zoom [1,1,1] (deliberately frozen, and
never cover - cover crops the chart labels in the Watch widget); the
rest mix cover pans and letterbox zooms. Letterbox + zero pan and a held
chart both read JERKY in --check-only - the documented false positives
(pipeline section 5). Longest hold ~25s (a two-sentence merge); gap
report clean.

35 slides, 565.5s.
"""

_C = "https://upload.wikimedia.org/wikipedia/commons"

IMAGES = {
    "FACADE": f"{_C}/0/0c/Tanjong_Pagar_Railway_Station_exterior_view%281_retouched%29.jpg",
    "MURAL": f"{_C}/7/7e/TanjongPagarRailwayStation-mural-Singapore-20080223.jpg",
    "PLATFORM": f"{_C}/f/fe/Platforms_and_tracks%2C_Tanjong_Pagar_Railway_Station%2C_Singapore_-_20100619-01.jpg",
    "HALL": f"{_C}/8/8e/Tanjong_Pagar_Railway_Station_interior_-_public_hall_%281%29.jpg",
    "TRAIN": f"{_C}/f/fb/Disused_train%2C_Tanjong_Pagar_Railway_Station%2C_Singapore_-_20090822.jpg",
    "CORRIDOR1": f"{_C}/b/b9/Rail_Corridor_running_on_a_former_railway_bridge_over_Hindhede_Drive.jpg",
    "CORRIDOR2": f"{_C}/1/19/Rail_Corridor%2C_Singapore_in_2024-09-27_3.jpg",
    "MAP": "/assets/images/malaysian-railway-land-map.png",
    "TIMELINE": "/assets/images/malaysian-railway-land-timeline.png",
}

CREDITS = {
    "MAP": "Map by Lesser Known Singapore; base map data © OpenStreetMap contributors",
    "TIMELINE": "Chart by Lesser Known Singapore",
}

_LBI = {"type": "letterbox", "zoom": [1, 1.05, 1.10], "pan": [(0.5, 0.5)] * 3, "ease": "ease-in-out"}
_LBO = {"type": "letterbox", "zoom": [1.10, 1.05, 1], "pan": [(0.5, 0.5)] * 3, "ease": "ease-out"}
_LBW = {"type": "letterbox", "zoom": [1, 1.06, 1.12], "pan": [(0.5, 0.5)] * 3, "ease": "ease-in-out"}
_MAPMOVE = {"type": "letterbox", "zoom": [1, 1.03, 1.05], "pan": [(0.5, 0.5)] * 3, "ease": "linear"}
_CVL = {"type": "cover", "zoom": [1.06, 1.06, 1.06], "pan": [(0.15, 0.5), (0.5, 0.5), (0.85, 0.5)], "ease": "ease-in-out"}
_CVR = {"type": "cover", "zoom": [1.06, 1.06, 1.06], "pan": [(0.85, 0.5), (0.5, 0.5), (0.15, 0.5)], "ease": "ease-in-out"}
_CVZ = {"type": "cover", "zoom": [1.0, 1.06, 1.12], "pan": [(0.5, 0.5)] * 3, "ease": "ease-in-out"}
# Graphics are letterbox + frozen, never cover: cover fills the frame and
# clips the overflow, which crops chart labels off the edges in the
# in-post Watch widget (it runs at the browser window's aspect, not 16:9).
_CHART = {"type": "letterbox", "zoom": [1.0, 1.0, 1.0], "pan": [(0.5, 0.5)] * 3, "ease": "linear"}

SLIDES = [
    {"img": "FACADE", **_LBI},      # 0
    {"img": "PLATFORM", **_CVL},    # 1
    {"img": "MAP", **_MAPMOVE},     # 2
    {"img": "FACADE", **_LBW},      # 3
    {"img": "MURAL", **_LBI},       # 4
    {"img": "HALL", **_LBI},        # 5
    {"img": "FACADE", **_LBO},      # 6
    {"img": "PLATFORM", **_CVR},    # 7
    {"img": "FACADE", **_LBI},      # 8
    {"img": "MAP", **_MAPMOVE},     # 9
    {"img": "FACADE", **_LBW},      # 10
    {"img": "MAP", **_MAPMOVE},     # 11
    {"img": "PLATFORM", **_CVL},    # 12
    {"img": "HALL", **_LBW},        # 13
    {"img": "MAP", **_MAPMOVE},     # 14
    {"img": "TIMELINE", **_CHART},  # 15
    {"img": "TIMELINE", **_CHART},  # 16
    {"img": "TIMELINE", **_CHART},  # 17
    {"img": "TIMELINE", **_CHART},  # 18
    {"img": "MAP", **_MAPMOVE},     # 19
    {"img": "MAP", **_MAPMOVE},     # 20
    {"img": "HALL", **_LBI},        # 21
    {"img": "PLATFORM", **_CVR},    # 22
    {"img": "TRAIN", **_LBI},       # 23
    {"img": "FACADE", **_LBO},      # 24
    {"img": "CORRIDOR1", **_LBI},   # 25
    {"img": "FACADE", **_LBI},      # 26
    {"img": "TIMELINE", **_CHART},  # 27
    {"img": "TIMELINE", **_CHART},  # 28
    {"img": "TIMELINE", **_CHART},  # 29
    {"img": "MAP", **_MAPMOVE},     # 30
    {"img": "MAP", **_MAPMOVE},     # 31
    {"img": "CORRIDOR2", **_CVL},   # 32
    {"img": "MAP", **_MAPMOVE},     # 33
    {"img": "FACADE", **_CVZ},      # 34
]

# Real values from audio/malaysian-railway-land-inside-singapore.timing.json.
# Every point is a real sentence start; slide index runs 0..34 in order.
#   0  s0-1   title; until 2011, boarding at Tanjong Pagar meant clearing
#             Malaysian immigration in the centre of Singapore
#   1  s2-3   the station, platforms and a ribbon of land were Malaysian-run;
#             46 years after Separation, foreign ground through the country
#   2  s4-5   the railway reached Singapore in 1903; in 1918 ~217 ha leased
#             to the FMSR for 999 years, railway use only
#   3  s6-7   1932 - the line rerouted, a new Art Deco terminus at Tanjong
#             Pagar, by Swan and Maclaren
#   4  s8     four marble figures, "F M S R", the Doulton panels of Malayan
#             industry
#   5  s9     Governor Clementi opens it, 2 May 1932
#   6  s10    1965 - the Separation Agreement says nothing about the railway
#   7  s11    KTM keeps the track, the land and the stations
#   8  s12    Tanjong Pagar stays a Malaysian-run terminus - flag, staff,
#             customs, immigration
#   9  s13-15 mostly a curiosity; the sharpest case was immigration - an
#             early-90s deal to co-locate both checkpoints at Woodlands
#   10 s16-17 Singapore moved on schedule; Malaysia refused and stayed at
#             Tanjong Pagar
#   11 s18-19 for 13 years: stamped out of Singapore at Woodlands, then a
#             20 km ride south to Tanjong Pagar before crossing the Causeway
#   12 s20-21 arriving passengers admitted at Woodlands, off in the city on
#             ground Singapore didn't administer; breach vs unilateral
#   13 s22    27 Nov 1990 - the Points of Agreement, Lee Kuan Yew and Daim
#             Zainuddin for Mahathir
#   14 s23-25 KTM to leave Tanjong Pagar; the land to revert; three parcels
#             to a 60/40 joint company
#   15 s26-27 then frozen 20 years - did it take effect on signing, or only
#             once KTM moved out?
#   16 s28-29 arguments over valuation, charges, extra Bukit Timah land, the
#             checkpoint; the 1990s rounds produced nothing
#   17 s30-31 a 2001 package deal - railway, water, airspace, a new bridge -
#             collapsed; Mahathir stepped down in 2003
#   18 s32-33 24 May 2010 - Lee Hsien Loong and Najib Razak break the
#             deadlock; KTM to Woodlands by 1 July 2011
#   19 s34    the joint company, M+S, 60% Khazanah / 40% Temasek
#   20 s35-37 the other side of the trade: six parcels at Marina South and
#             Ophir-Rochor; Marina One and DUO built on them
#   21 s38-39 land for land, not a ruling - though a 2014 tribunal in The
#             Hague settled a leftover charge, for Malaysia
#   22 s40-41 30 June 2011 - thousands at Tanjong Pagar; platform tickets
#             and souvenir spikes
#   23 s42-44 the last train, just before ten, driven by the Sultan of
#             Johor; the next morning the line closed and the rails came up
#   24 s45    Tanjong Pagar gazetted a monument; the Bukit Timah truss
#             bridges kept
#   25 s46    the 24 km strip becomes the Rail Corridor, reopening in
#             sections since 2021
#   26 s47    the terminus used for events; a future Cantonment MRT station
#   27 s48-49 the 2010 deal also unblocked new cross-border rail plans; the
#             larger one did not survive
#   28 s50    the KL-Jurong East high-speed line - agreed 2016, suspended
#             2018, terminated 2021
#   29 s51    Malaysia paid Singapore about 103 million dollars
#   30 s52-53 the smaller one is nearly here - the RTS Link, Bukit Chagar to
#             Woodlands North, suspended 2019, revived 2020
#   31 s54    due by the end of 2026 or early 2027
#   32 s55    its feature: clear both countries' immigration once, before
#             boarding - the reverse of Tanjong Pagar
#   33 s56    where it fits: 46 years of foreign-administered ground through
#             Singapore, because 1965 never dealt with the railway
#   34 s57    resolved by a trade of land, not a court; the cross-border
#             train rebuilt, shorter and faster, at the edge of the island
# Exact sentence starts from the timing.json produced after the "Loong"
# and "Hsien" pronunciation fixes.
SCHEDULE = [
    (0.0, 0), (21.675, 1), (39.875, 2), (64.525, 3), (80.5, 4),
    (100.825, 5), (114.05, 6), (122.325, 7), (134.0, 8), (148.75, 9),
    (168.85, 10), (188.375, 11), (205.95, 12), (225.125, 13), (242.6, 14),
    (267.075, 15), (281.825, 16), (297.6, 17), (319.25, 18), (334.25, 19),
    (351.575, 20), (373.1, 21), (391.775, 22), (407.9, 23), (426.95, 24),
    (436.825, 25), (450.7, 26), (460.575, 27), (471.8, 28), (490.075, 29),
    (496.825, 30), (516.875, 31), (523.425, 32), (537.65, 33), (553.05, 34),
]
TOTAL_DURATION = 565.6
TIMING_JSON = "audio/malaysian-railway-land-inside-singapore.timing.json"
