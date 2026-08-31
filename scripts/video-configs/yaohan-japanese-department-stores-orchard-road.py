"""Video config for "How a Japanese Greengrocer Changed the Way Singapore
Shops" - Watch widget and main video.

No chart. One diagram: the OpenStreetMap store-location map
(scripts/render_yaohan_store_map.py -> assets/images/yaohan-store-map.png),
a near-static letterbox slide with a CREDITS line.

The post's Orchard Road panorama is 1024x175 - far too thin to fill a
1280x720 frame without heavy blur - so it is left in the post only and
not used here. That leaves 11 usable images (4 captioned in the post,
7 in the gallery), so stage_youtube_text.py resolves every credit; the
Plaza Singapura, Ngee Ann City and interior shots each recur several
times, re-triggering a fresh slow zoom, because there simply aren't
more freely-licensed photos of this subject.

All slides letterbox (largest usable image is 1.33; SHAW/WISMA are
portrait). Letterbox + zero pan reads JERKY in --check-only - the
documented false positive (pipeline section 5). No slide held past
~26s (gap report clean).

29 slides, 436.57s.
"""

_C = "https://upload.wikimedia.org/wikipedia/commons"

IMAGES = {
    "PLAZA": f"{_C}/c/c3/Plaza_Singapura%2C_Dec_05.JPG",
    "PLAZAINT": f"{_C}/2/28/Large_interior_view_of_Plaza_Singapura_Shopping_mall_Orchard_Road_Singapore.jpg",
    "NGEEANN": f"{_C}/2/2e/Ngee_Ann_City%2C_Dec_05.JPG",
    "WISMA": f"{_C}/a/aa/Wisma_Atria_building_2011.jpg",
    "SHAW": f"{_C}/b/bd/Shaw_House_2%2C_Xmas%2C_Dec_06.JPG",
    "LIANG": f"{_C}/4/49/Liang_Court%2C_Feb_06.JPG",
    "RAFFLES": f"{_C}/2/21/RafflesCityExterior.JPG",
    "DDD": f"{_C}/f/f3/DON_DON_DONKI_in_Singapore.jpg",
    "JEWEL": f"{_C}/f/fa/Jewel_Changi_Airport_Don_Don_Donki_18-05-2024%285%29.jpg",
    "MITSUWA": f"{_C}/e/ed/Mitsuwa_in_NJ.JPG",
    "STOREMAP": "/assets/images/yaohan-store-map.png",
}

CREDITS = {
    "STOREMAP": "Map by Lesser Known Singapore; base map data © OpenStreetMap contributors",
}

_IN = {"type": "letterbox", "zoom": [1, 1.05, 1.10], "pan": [(0.5, 0.5)] * 3, "ease": "ease-in-out"}
_OUT = {"type": "letterbox", "zoom": [1.10, 1.05, 1], "pan": [(0.5, 0.5)] * 3, "ease": "ease-out"}
_WIDE = {"type": "letterbox", "zoom": [1, 1.06, 1.12], "pan": [(0.5, 0.5)] * 3, "ease": "ease-in-out"}
_MAP = {"type": "letterbox", "zoom": [1, 1.02, 1.04], "pan": [(0.5, 0.5)] * 3, "ease": "linear"}

SLIDES = [
    {"img": "PLAZA", **_IN},
    {"img": "PLAZAINT", **_IN},
    {"img": "NGEEANN", **_WIDE},
    {"img": "PLAZAINT", **_OUT},
    {"img": "PLAZA", **_WIDE},
    {"img": "STOREMAP", **_MAP},
    {"img": "PLAZAINT", **_IN},
    {"img": "PLAZAINT", **_OUT},
    {"img": "PLAZA", **_IN},
    {"img": "STOREMAP", **_MAP},
    {"img": "WISMA", **_IN},
    {"img": "LIANG", **_IN},
    {"img": "RAFFLES", **_IN},
    {"img": "NGEEANN", **_IN},
    {"img": "NGEEANN", **_OUT},
    {"img": "PLAZA", **_OUT},
    {"img": "PLAZAINT", **_WIDE},
    {"img": "PLAZA", **_IN},
    {"img": "MITSUWA", **_IN},
    {"img": "RAFFLES", **_OUT},
    {"img": "LIANG", **_OUT},
    {"img": "SHAW", **_IN},
    {"img": "NGEEANN", **_WIDE},
    {"img": "JEWEL", **_IN},
    {"img": "NGEEANN", **_OUT},
    {"img": "DDD", **_IN},
    {"img": "MITSUWA", **_OUT},
    {"img": "PLAZA", **_WIDE},
    {"img": "DDD", **_OUT},
]

# Real values from
# audio/yaohan-japanese-department-stores-orchard-road.timing.json.
# Every point is a real sentence start; slide index runs 0..28 in order.
#   0  s0-1   title; Yaohan opens at Plaza Singapura, 1 Nov 1974 - one
#             roof, fixed prices, staff at the door
#   1  s2-3   nothing like it; ~1M shoppers in week one, population 2.2M
#   2  s4     half a century on, the stores are mostly gone - the basement
#             idea outlasted them
#   3  s5     Yaohan began 1930, a fruit-and-veg shop in Atami; Ryohei &
#             Katsu Wada
#   4  s6     son Kazuo Wada; Shizuoka chain, then abroad - Brazil,
#             Singapore, Hong Kong, and on
#   5  s7     at its height, ~450 stores in 16 countries
#   6  s8     Wada and Seicho-no-Ie; recruits expected to join
#   7  s9-10  the Singapore company was a DBS joint venture; 16 checkouts,
#             19 counters, the largest of its kind
#   8  s11-12 before Yaohan: wet market and provision shop; Yaohan put it
#             together, cooked food to take away, a price on everything
#   9  s13-14 the format spread - Katong, Thomson, Bukit Timah, Jurong,
#             Parkway - out into the estates
#   10 s15-16 it had company: Isetan, two years earlier, 1972, Havelock
#             Road, the first Japanese department store here
#   11 s17    Daimaru anchored Liang Court from 1983
#   12 s18    Sogo opened at Raffles City in 1986
#   13 s19    Takashimaya arrived last and largest, Ngee Ann City, 1993
#   14 s20-21 for two decades the template for a Singapore mall - anchor,
#             basement food hall, fixed-price floor; the retailers' reasons
#   15 s22    by 1990 Wada bet the company on China, base moved to Hong Kong
#   16 s23-24 a thousand China stores, a giant Shanghai flagship; heavy
#             borrowing, thin capital when the 1997 crisis hit
#   17 s25-26 18 Sep 1997: the parent files, ~161bn yen owed - the biggest
#             postwar failure in Japanese retail
#   18 s27-28 sold in pieces - Aeon, Jusco, and from 1998 Mitsuwa in the
#             US; the Singapore stores close through 1997-98
#   19 s29-30 not the only one to go: Sogo into judicial management, shut
#             Raffles City in 2000
#   20 s31    Daimaru closed at Liang Court in 2003
#   21 s32    Isetan closed store after store - down from six in 2013 to
#             one, the Scotts Road flagship
#   22 s33    only Takashimaya still trades close to its old form -
#             location, size, a year-round calendar of events
#   23 s34-35 what carried through is the basement: depachika, the food
#             hall of prepared dishes, bento, bakery, deli
#   24 s36    Takashimaya's B2 hall and Isetan's basement are still where
#             the shoppers go
#   25 s37-38 December 2017: Don Don Donki at Orchard Central - cheap, good,
#             ready-to-eat, close to Yaohan 1974; now island-wide
#   26 s39-40 Yaohan did not vanish: Mitsuwa in the US, New Yaohan in
#             Macau, a former Yaohan in a Chicago suburb
#   27 s41-42 where it fits: the ordinary-mall shape was a Japanese import
#             from a company that bet on China and lost; the stores are
#             nearly all gone
#   28 s43    the habit they taught - going downstairs for something good
#             to eat - is stronger than ever
SCHEDULE = [
    (0.0, 0), (21.77, 1), (31.32, 2), (47.0, 3), (58.67, 4),
    (78.88, 5), (85.0, 6), (99.28, 7), (117.67, 8), (139.25, 9),
    (158.28, 10), (173.4, 11), (177.72, 12), (181.97, 13), (188.38, 14),
    (214.82, 15), (229.15, 16), (248.15, 17), (265.07, 18), (281.9, 19),
    (299.82, 20), (305.32, 21), (325.5, 22), (342.45, 23), (355.02, 24),
    (365.32, 25), (388.0, 26), (408.32, 27), (429.75, 28),
]
TOTAL_DURATION = 436.57
TIMING_JSON = "audio/yaohan-japanese-department-stores-orchard-road.timing.json"
