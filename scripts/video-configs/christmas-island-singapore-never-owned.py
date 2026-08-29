"""Video config for "Singapore 'Sold' Christmas Island in 1958 - Except It
Never Owned It" - Watch widget and main video.

The post's chart is a 2-bar payout comparison (M$48M foregone vs M$20M
received), rendered once to a static PNG by
scripts/render_christmas_island_payout_chart.py ->
assets/images/christmas-island-payout.png and used here as a near-static
slide (twice: the numbers beat and the close).

Images (3 post + the OSM distance map + 5 gallery):
  COVE      - Flying Fish Cove, Christmas Island's settlement (post hero)
  MAP       - the OSM map putting Singapore and Christmas Island ~1,550 km
              apart (map data (c) OpenStreetMap contributors)
  LYH       - Lim Yew Hock, Chief Minister when the 1958 transfer closed
  JUMAT     - Abdul Hamid Jumat, the Acting CM who told the Assembly the
              island "was asked to administer it and nothing more"
  LOCO      - a 1931 Christmas Island Phosphate Co. railway locomotive -
              the income actually at stake
  JAPANESE  - Japanese naval troops with a captured gun, April 1942
  STAMP     - Christmas Island's first stamp, 1958 (Australian overprint)
  ST1959    - The Sunday Times, 31 May 1959 - the PAP landslide, the
              self-government Singapore won a year after losing the claim
  DETENTION - the North West Point detention centre, opened 2008
  CHART     - the static payout PNG

18 slides, 373.65s. Aspect check (1280x720, ~1.44 cover threshold):
  COVE 1024x768 (1.33)     -> letterbox
  MAP 440x671 (0.66)       -> letterbox
  LYH 588x784 (0.75)       -> letterbox
  JUMAT 248x363 (0.68)     -> letterbox (low-res archival portrait)
  JAPANESE 800x586 (1.37)  -> letterbox
  STAMP 191x232 (0.82)     -> letterbox (a postage stamp, small by nature)
  ST1959 1000x1419 (0.70)  -> letterbox
  CHART 1280x720 (1.78)    -> letterbox (exact), near-zero zoom
  DETENTION 5294x3529 (1.50)-> cover, horizontal pan
  LOCO 750x279 (2.69)      -> cover, full L->R pan across the loco
Letterbox slides use zero pan (blurred-bg zoom only), so --check-only
flags them JERKY - the documented letterbox false positive (pipeline
section 5); the near-static CHART slides read JERKY for the same reason.
"""

_C = "https://upload.wikimedia.org/wikipedia/commons"

IMAGES = {
    "COVE": f"{_C}/6/6b/Flying_Fish_Cove_%2825341355156%29.jpg",
    "MAP": "/assets/images/osm-singapore-christmas-island.png",
    "LYH": f"{_C}/3/33/Lim_Yew_Hock%2C_1956_%28cropped%29.png",
    "JUMAT": f"{_C}/8/88/Abdul_Hamid_bin_Haji_Jumat.jpg",
    "LOCO": f"{_C}/b/b4/0-8-0_tender_locomotive_for_the_Christmas_Island_Phosphate_Co.%27s_Railway_by_Peckett_%26_Sons_Ltd._of_Bristol%2C_No._1824_of_March_1931.jpg",
    "JAPANESE": f"{_C}/d/dd/Japanese_Marines_in_Christmas_Island_1942.jpg",
    "STAMP": f"{_C}/6/67/Stamp_Christmas_Island_1958_2c.jpg",
    "ST1959": f"{_C}/9/95/ST31May1959.jpg",
    "DETENTION": f"{_C}/6/6f/Christmas_Island_Immigration_Detention_Centre_and_the_Lilac_compound_%285774458263%29.jpg",
    "CHART": "/assets/images/christmas-island-payout.png",
}

CREDITS = {
    "MAP": "Locator map: map data © OpenStreetMap contributors",
    "CHART": "Payout chart by Lesser Known Singapore, from the figures cited in the post",
}

SLIDES = [
    {"img": "COVE", "type": "letterbox", "zoom": [1, 1.06, 1.12], "pan": [(0.5, 0.5), (0.5, 0.5), (0.5, 0.5)], "ease": "ease-in-out"},
    {"img": "MAP", "type": "letterbox", "zoom": [1, 1.05, 1.10], "pan": [(0.5, 0.5), (0.5, 0.5), (0.5, 0.5)], "ease": "ease-in"},
    {"img": "COVE", "type": "letterbox", "zoom": [1.12, 1.06, 1], "pan": [(0.5, 0.5), (0.5, 0.5), (0.5, 0.5)], "ease": "ease-out"},
    {"img": "JUMAT", "type": "letterbox", "zoom": [1, 1.05, 1.10], "pan": [(0.5, 0.5), (0.5, 0.5), (0.5, 0.5)], "ease": "ease-in-out"},
    {"img": "MAP", "type": "letterbox", "zoom": [1.10, 1.05, 1], "pan": [(0.5, 0.5), (0.5, 0.5), (0.5, 0.5)], "ease": "ease-out"},
    {"img": "LOCO", "type": "cover", "zoom": [1, 1.04, 1.08], "pan": [(0.15, 0.5), (0.5, 0.5), (0.85, 0.5)], "ease": "linear"},
    {"img": "JAPANESE", "type": "letterbox", "zoom": [1, 1.06, 1.12], "pan": [(0.5, 0.5), (0.5, 0.5), (0.5, 0.5)], "ease": "ease-in-out"},
    {"img": "JAPANESE", "type": "letterbox", "zoom": [1.12, 1.06, 1], "pan": [(0.5, 0.5), (0.5, 0.5), (0.5, 0.5)], "ease": "ease-out"},
    {"img": "LYH", "type": "letterbox", "zoom": [1, 1.05, 1.10], "pan": [(0.5, 0.5), (0.5, 0.5), (0.5, 0.5)], "ease": "ease-in-out"},
    {"img": "STAMP", "type": "letterbox", "zoom": [1, 1.05, 1.10], "pan": [(0.5, 0.5), (0.5, 0.5), (0.5, 0.5)], "ease": "ease-in"},
    {"img": "LYH", "type": "letterbox", "zoom": [1.10, 1.05, 1], "pan": [(0.5, 0.5), (0.5, 0.5), (0.5, 0.5)], "ease": "ease-out"},
    {"img": "CHART", "type": "letterbox", "zoom": [1, 1.015, 1.03], "pan": [(0.5, 0.5), (0.5, 0.5), (0.5, 0.5)], "ease": "linear"},
    {"img": "JUMAT", "type": "letterbox", "zoom": [1, 1.06, 1.12], "pan": [(0.5, 0.5), (0.5, 0.5), (0.5, 0.5)], "ease": "ease-in-out"},
    {"img": "ST1959", "type": "letterbox", "zoom": [1, 1.06, 1.12], "pan": [(0.5, 0.5), (0.5, 0.5), (0.5, 0.5)], "ease": "ease-in-out"},
    {"img": "DETENTION", "type": "cover", "zoom": [1, 1.06, 1.12], "pan": [(0.36, 0.5), (0.5, 0.5), (0.62, 0.5)], "ease": "ease-in-out"},
    {"img": "COVE", "type": "letterbox", "zoom": [1, 1.07, 1.14], "pan": [(0.5, 0.5), (0.5, 0.5), (0.5, 0.5)], "ease": "ease-in-out"},
    {"img": "MAP", "type": "letterbox", "zoom": [1, 1.05, 1.10], "pan": [(0.5, 0.5), (0.5, 0.5), (0.5, 0.5)], "ease": "ease-in"},
    {"img": "CHART", "type": "letterbox", "zoom": [1, 1.02, 1.04], "pan": [(0.5, 0.5), (0.5, 0.5), (0.5, 0.5)], "ease": "linear"},
]

# Real values from audio/christmas-island-singapore-never-owned.timing.json.
# Every point is a real sentence start.
#   0  title + s1  the myth: Singapore owned it and sold it to Australia
#   1  s2-4    "it's a tidy story ... it's also wrong ... nothing to sell"
#   2  s5-6    British Crown 1888 / Straits Settlements 1900, "nothing more"
#   3  s7-9    Singapore's leaders said so / Abdul Hamid Jumat's quote
#   4  s10-11  "no title to give away" / what was on the table: phosphate
#   5  s12-13  LOCO - mining from 1897, ore to Japan/Germany, indentured
#             labour / revenue flowed to whoever administered
#   6  s14-15  the wartime disaster / the March 1942 garrison mutiny
#   7  s16-17  Japan took it without a shot / Australia's postwar interest
#   8  s18-19  1948 buyout / June 1957 transfer announced, Bill cleared
#   9  s20     1 Oct 1958 - Australian territory / Territory Day
#   10 s21     Lim Yew Hock's government gets the M$20M ex-gratia payment
#   11 s22-23  CHART - M$1.5M/yr x 32 yrs ~ M$48M vs the M$20M received
#   12 s24-25  the timing / finalised by outgoing colonial administrators
#   13 s26-27  self-government 1959, the PAP landslide / decided by people
#             who within a year wouldn't be running the place
#   14 s28-29  Christmas Island today / the 2008 detention centre
#   15 s30     the red-crab migration - the island's other fame
#   16 s31     nobody knows the rock was once run out of a Singapore office
#   17 s32-33  CHART - close: Singapore didn't lose an island, it lost the
#             chance to fix the story; it was only ever the landlord's agent
SCHEDULE = [
    (0.0, 0), (19.45, 1), (36.625, 2), (59.1, 3), (81.35, 4),
    (96.15, 5), (124.05, 6), (143.825, 7), (169.275, 8), (197.8, 9),
    (207.925, 10), (232.0, 11), (255.9, 12), (274.5, 13), (297.975, 14),
    (321.85, 15), (337.2, 16), (348.45, 17),
]
TOTAL_DURATION = 373.65
TIMING_JSON = "audio/christmas-island-singapore-never-owned.timing.json"
