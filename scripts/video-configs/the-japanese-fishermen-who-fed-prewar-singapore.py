"""Video config for the Japanese fishermen post.

Nine images. The Commons pool is thin (no photographs of the Japanese
fleet, its crews or the markets exist there), so the local-waterfront
photos repeat with different pans and the newspaper pages carry the
squeeze section.

  PASIR  - Pasir Puteh fishing stakes and boats, c.1910 (Kleingrothe,
           KITLV, Commons) - cover, three pans
  ROCHOR - Rochor proa harbour, c.1910 (Kleingrothe, KITLV) - cover
  RIVER  - prao harbour, presumably the Singapore River, c.1910
           (Kleingrothe, KITLV, 1920px thumb) - a 3:1 panorama, so cover
           with a slow left-to-right sweep
  MAP    - Admiralty chart 2586, eastern Johore Strait, 1924 - letterbox
  ST1003 - The Straits Times, 3 Oct 1939, page 10 (whole page, local scan,
           NewspaperSG / SPH, public domain by age) - letterbox
  ST38   - The Sunday Times, 30 Jan 1938, page 3 (same basis)
  ST39   - The Sunday Times, 2 Apr 1939, page 7 (same basis)
  KRAIT  - the Krait at Darwin (AWM 067338, Commons) - small and grainy,
           so letterbox
  CREW   - men aboard the Krait during Operation Jaywick (AWM, Commons) -
           small and grainy, so letterbox

53 slides, 696.525s.
"""

_U = "https://upload.wikimedia.org/wikipedia/commons"

IMAGES = {
    "PASIR": f"{_U}/thumb/c/c8/KITLV_-_79910_-_Kleingrothe%2C_C.J._-_Medan_-_Pasir_Puteh_at_Singapore_-_circa_1910.tif/lossy-page1-1280px-KITLV_-_79910_-_Kleingrothe%2C_C.J._-_Medan_-_Pasir_Puteh_at_Singapore_-_circa_1910.tif.jpg",
    "ROCHOR": f"{_U}/thumb/2/2b/KITLV_-_79908_-_Kleingrothe%2C_C.J._-_Medan_-_Rochor%2C_Singapore_proa_harbor_-_circa_1910.tif/lossy-page1-1280px-KITLV_-_79908_-_Kleingrothe%2C_C.J._-_Medan_-_Rochor%2C_Singapore_proa_harbor_-_circa_1910.tif.jpg",
    "RIVER": f"{_U}/thumb/e/e1/KITLV_-_79919_-_Kleingrothe%2C_C.J._-_Medan_-_Prao_harbour_in_Singapore%2C_presumably_in_the_Singapore_River_-_circa_1910.tif/lossy-page1-1920px-KITLV_-_79919_-_Kleingrothe%2C_C.J._-_Medan_-_Prao_harbour_in_Singapore%2C_presumably_in_the_Singapore_River_-_circa_1910.tif.jpg",
    "MAP": f"{_U}/thumb/3/39/Admiralty_Chart_No_2586_Eastern_Portion_of_Johore_Strait_%28Singapore_Old_Strait%29_Pulo_Ubin_to_Sungi_Kranji%2C_Published_1924.jpg/1920px-Admiralty_Chart_No_2586_Eastern_Portion_of_Johore_Strait_%28Singapore_Old_Strait%29_Pulo_Ubin_to_Sungi_Kranji%2C_Published_1924.jpg",
    "ST1003": "/assets/images/straits-times-1939-10-03-page-10.jpg",
    "ST38": "/assets/images/straits-times-1938-01-30-page-3.jpg",
    "ST39": "/assets/images/straits-times-1939-04-02-page-7.jpg",
    "KRAIT": f"{_U}/b/b1/Krait_%28AWM_067338%29.jpg",
    "CREW": f"{_U}/1/18/Krait-crew.jpg",
}

_LTB = {"type": "letterbox", "zoom": [1.0, 1.04, 1.08], "pan": [(0.5, 0.5)] * 3, "ease": "ease-in-out"}
_LTBO = {"type": "letterbox", "zoom": [1.08, 1.04, 1.0], "pan": [(0.5, 0.5)] * 3, "ease": "ease-out"}

# Pasir Puteh: boat at far left, stakes centre, huts right.
_CVA = {"type": "cover", "zoom": [1.0, 1.05, 1.1], "pan": [(0.5, 0.6)] * 3, "ease": "ease-in-out"}
_CVB = {"type": "cover", "zoom": [1.12, 1.06, 1.0], "pan": [(0.3, 0.68)] * 3, "ease": "ease-out"}
_CVC = {"type": "cover", "zoom": [1.0, 1.06, 1.12], "pan": [(0.72, 0.55)] * 3, "ease": "ease-in-out"}
# Panorama: slow sweeps across the river (cover crops to ~60% of the width).
_SWEEP = {"type": "cover", "zoom": [1.0, 1.0, 1.0], "pan": [(0.3, 0.5), (0.5, 0.5), (0.7, 0.5)], "ease": "ease-in-out"}
_SWEEP2 = {"type": "cover", "zoom": [1.0, 1.0, 1.0], "pan": [(0.7, 0.5), (0.5, 0.5), (0.3, 0.5)], "ease": "ease-in-out"}

SLIDES = [
    {"img": "PASIR", **_CVA},      # 0  s0  title
    {"img": "RIVER", **_SWEEP},    # 1  s1  hook: 40-50% of the fresh fish
    {"img": "ST1003", **_LTB},     # 2  s2  licence limits, boycott, suspicion
    {"img": "ROCHOR", **_CVA},     # 3  s3  tried since the late 19th century
    {"img": "MAP", **_LTB},        # 4  s4  1913 Takayama survey of the waters
    {"img": "RIVER", **_SWEEP2},   # 5  s5  his report: demand, markets
    {"img": "PASIR", **_CVB},      # 6  s6  firms in the early 1920s
    {"img": "ROCHOR", **_CVB},     # 7  s7  men from Okinawa, Itoman
    {"img": "PASIR", **_CVC},      # 8  s8  80 per cent from Itoman
    {"img": "RIVER", **_SWEEP},    # 9  s9  Itoman had almost no farmland
    {"img": "MAP", **_LTBO},       # 10 s10 Okinawan grounds depleted
    {"img": "ROCHOR", **_CVA},     # 11 s11 Okinawan men rose 292 to 1,035
    {"img": "PASIR", **_CVA},      # 12 s12 muro-ami team effort, crew
    {"img": "ROCHOR", **_CVB},     # 13 s13 divers, bag net, boys
    {"img": "RIVER", **_SWEEP2},   # 14 s16 indentured boys
    {"img": "MAP", **_LTB},        # 15 s17 600 of 801 in 1929
    {"img": "PASIR", **_CVB},      # 16 s18 firms financed the move
    {"img": "ROCHOR", **_CVA},     # 17 s20 boat and carrier costs, 40/60 split
    {"img": "PASIR", **_CVC},      # 18 s22 local fishermen, kelongs
    {"img": "RIVER", **_SWEEP},    # 19 s24 powered boats and ice
    {"img": "ROCHOR", **_CVB},     # 20 s25 15 vs 150 katties
    {"img": "PASIR", **_CVA},      # 21 s26 katti; 40-50 per cent of markets
    {"img": "RIVER", **_SWEEP2},   # 22 s28 Depression, prices, income
    {"img": "ROCHOR", **_CVA},     # 23 s30 drift nets, Ishizu bankrupt
    {"img": "MAP", **_LTBO},       # 24 s32 Taichong takes over, 671 of 1,038
    {"img": "PASIR", **_CVB},      # 25 s33 ice factory, holding company, Tanjong Rhu
    {"img": "RIVER", **_SWEEP},    # 26 s35 karayuki-san community
    {"img": "ROCHOR", **_CVB},     # 27 s36 war approached, concern
    {"img": "MAP", **_LTB},        # 28 s37 naval base and airfields
    {"img": "PASIR", **_CVC},      # 29 s38 40 intrusion cases
    {"img": "RIVER", **_SWEEP2},   # 30 s39 evidence for spying hard to pin down
    {"img": "ST1003", **_LTBO},    # 31 s41 suspicion shaped policy, restrictions in steps
    {"img": "MAP", **_LTB},        # 32 s44 1938: 30 of about 150 boats
    {"img": "RIVER", **_SWEEP},    # 33 s45 Feb 1939: 20 power boats
    {"img": "ROCHOR", **_CVA},     # 34 s46 no more renewals
    {"img": "PASIR", **_CVA},      # 35 s47 30 firms to three
    {"img": "ST38", **_LTB},       # 36 s49 trade dispute, boycott
    {"img": "ST38", **_LTBO},      # 37 s51 30 Jan 1938 Sunday Times report
    {"img": "ST39", **_LTB},       # 38 s52 petition, half then a quarter
    {"img": "ST39", **_LTBO},      # 39 s54 1,400 to 900, boats gone
    {"img": "MAP", **_LTBO},       # 40 s56 petitioners; government's line
    {"img": "ROCHOR", **_CVB},     # 41 s58 displaced men, Bukit Besi mine
    {"img": "PASIR", **_CVB},      # 42 s60 2,300 Chinese miners quit
    {"img": "RIVER", **_SWEEP},    # 43 s61 remnant by 1940
    {"img": "ROCHOR", **_CVA},     # 44 s62 December 1941 internment
    {"img": "MAP", **_LTB},        # 45 s63 nearly 2,700 to India
    {"img": "KRAIT", **_LTB},      # 46 s64 one boat's afterlife, Kofuku Maru
    {"img": "KRAIT", **_LTBO},     # 47 s66 1,100 people, Australia, renamed Krait
    {"img": "CREW", **_LTB},       # 48 s67 Jaywick, September 1943
    {"img": "KRAIT", **_LTB},      # 49 s69 raid; an ordinary sight
    {"img": "PASIR", **_CVA},      # 50 s70 why it matters today
    {"img": "RIVER", **_SWEEP},    # 51 s71 reshaped an ordinary trade
    {"img": "KRAIT", **_LTBO},     # 52 s72 30 firms to three, a boat on the Allied side
]

SCHEDULE = [
    (0.0, 0), (4.0, 1), (20.0, 2), (31.5, 3), (42.7, 4),
    (53.975, 5), (63.75, 6), (75.325, 7), (84.3, 8), (93.725, 9),
    (100.55, 10), (115.1, 11), (125.925, 12), (128.95, 13), (150.425, 14),
    (167.65, 15), (179.4, 16), (191.875, 17), (209.45, 18), (221.65, 19),
    (230.05, 20), (246.175, 21), (263.875, 22), (285.85, 23), (298.375, 24),
    (311.85, 25), (331.325, 26), (344.975, 27), (353.125, 28), (365.05, 29),
    (378.225, 30), (401.575, 31), (414.8, 32), (428.725, 33), (439.775, 34),
    (448.45, 35), (461.125, 36), (476.35, 37), (494.025, 38), (511.575, 39),
    (530.025, 40), (549.125, 41), (564.725, 42), (573.95, 43), (583.925, 44),
    (591.55, 45), (609.95, 46), (626.75, 47), (639.6, 48), (658.275, 49),
    (664.925, 50), (679.75, 51), (685.175, 52),
]
TOTAL_DURATION = 696.525
TIMING_JSON = "audio/the-japanese-fishermen-who-fed-prewar-singapore.timing.json"
