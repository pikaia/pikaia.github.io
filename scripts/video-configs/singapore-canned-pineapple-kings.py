"""Video config for the pineapple-kings post's Watch widget / main video.

First pass through the pipeline. Originally written with only 8 real
photos for this whole story (portraits of the three towkays plus a
second, older Tan Kah Kee portrait and a group shot with Tan Lark Sye,
and three loosely-connected place/institution photos), since no
plantation/cannery photography seemed to survive on Wikimedia Commons.
Chris then found four real ones while reviewing the rendered video -
a Kleingrothe plantation photo (Buona Vista Road, c.1910) and three
photos from the 1902/1904 Agricultural Bulletin of the Straits and
Federated Malay States (a bullock cart delivering pineapples, a pile of
them ready for tinning, and a cannery interior) - so slides 2-6 (the
"how the industry worked" stretch) were re-cut to use those instead of
the original filler. The other images still repeat 2-5 times each
across the rest of the video.

Almost every portrait/institution source is a portrait or near-square
scan (see IMAGES comments for exact pixel dimensions), so those slides
are letterbox; the four new industry photos and NEESOONRD are landscape
and use cover. A horizontal pan (_CVL/_CVR-style) on NEESOONRD read
JERKY on the smoothness check - the same failure mode as the Kangkar
post - so it's centred push-in/pull-out only (_CVZ/_CVZO), no pan; the
same presets are reused for the new photos rather than risking the same
issue with an untested pan. NEESOONRD is also a very large scan
(12127x8159, over PIL's default decompression-bomb pixel limit - a
warning, not an error) - rendering it may be visibly slower than the
other slides; expected.

Slide 24 (previously a repeated GROUP portrait) was then swapped for a
custom OSM map (scripts/render_singapore_canned_pineapple_kings_map.py,
assets/images/singapore-canned-pineapple-kings-map.png) showing where
the story actually happened: the cannery cluster around the Singapore
River, Lim Nee Soon's and Tan Kah Kee's estates in the north, and Lee
Pineapple's factory in Skudai, Johor - the one place this is still a
going concern rather than pure history. It's letterbox like the chart
slides on other posts (per docs/production-pipeline.md ss3): a full
informational graphic with its own baked-in text/credit, so it must
stay uncropped, not cover-cropped. It reuses the existing slide 24
timing rather than reflowing the whole SCHEDULE.

28 slides, 531.75s.
"""

_C = "https://upload.wikimedia.org/wikipedia/commons"

IMAGES = {
    "GROUP": f"{_C}/a/a6/Tan_Kah_Kee%2C_Lee_Kong_Chian%2C_and_Tan_Lark_Sye%2C_1946.png",  # 933x674
    "NEESOON": f"{_C}/2/24/Lim_Nee_Soon.png",                                              # 339x493 (portrait)
    "TKKYOUNG": f"{_C}/0/03/%E5%B9%B4%E8%BD%BB%E7%9A%84%E9%99%88%E5%98%89%E5%BA%9A.jpg",   # 463x617 (portrait)
    "LKC": f"{_C}/e/e4/Lee_Kong_Chian%2C_1946.png",                                        # 351x521 (portrait)
    "TKKOLDER": f"{_C}/7/7b/%E9%99%88%E5%98%89%E5%BA%9A2.jpg",                              # 400x609 (portrait)
    "CHS": f"{_C}/b/b2/%E6%96%B0%E5%8A%A0%E5%9D%A1%E5%8D%97%E6%B4%8B%E5%8D%8E%E4%BE%A8%E4%B8%AD%E5%AD%A6%E9%92%9F%E6%A5%BC.JPG",  # 3859x2604
    "CHSCLASS": f"{_C}/9/95/Classroom_building_in_the_50s.JPG",                            # 600x583 (near-square)
    "NEESOONRD": f"{_C}/6/6b/Nee_Soon_Road.jpg",                                           # 12127x8159 (landscape)
    "PLANTATION": f"{_C}/thumb/c/cc/KITLV_-_79906_-_Kleingrothe%2C_C.J._-_Medan_-_Pineapple_plantation_in_the_Buona_Vista_Road%2C_Singapore_-_circa_1910.tif/lossy-page1-3840px-KITLV_-_79906_-_Kleingrothe%2C_C.J._-_Medan_-_Pineapple_plantation_in_the_Buona_Vista_Road%2C_Singapore_-_circa_1910.tif.jpg",  # 3840x2501 (JPG thumb of a TIF original)
    "BULLOCKCART": f"{_C}/6/60/Agricultural_bulletin_of_the_Straits_and_Federated_Malay_States._New_series_%281902%29_%2817944867551%29.jpg",  # 4623x2496
    "TINNING": f"{_C}/1/1a/Agricultural_bulletin_of_the_Straits_and_Federated_Malay_States._New_series_%281902%29_%2817756609000%29.jpg",  # 4620x2480
    "CANNERYINSIDE": f"{_C}/1/18/Agricultural_bulletin_of_the_Straits_and_Federated_Malay_States._New_series_BHL43583042.jpg",  # 4623x2592
    "MAP": "/assets/images/singapore-canned-pineapple-kings-map.png",                    # 1600x1142, OSM-based, committed locally
}

_LBI = {"type": "letterbox", "zoom": [1.0, 1.04, 1.08], "pan": [(0.5, 0.5)] * 3, "ease": "ease-in-out"}
_LBW = {"type": "letterbox", "zoom": [1.0, 1.05, 1.10], "pan": [(0.5, 0.5)] * 3, "ease": "ease-in-out"}
_LBO = {"type": "letterbox", "zoom": [1.08, 1.04, 1.0], "pan": [(0.5, 0.5)] * 3, "ease": "ease-out"}
_LBN = {"type": "letterbox", "zoom": [1.0, 1.03, 1.06], "pan": [(0.5, 0.5)] * 3, "ease": "ease-in"}
_CVZ = {"type": "cover", "zoom": [1.0, 1.08, 1.14], "pan": [(0.5, 0.5)] * 3, "ease": "ease-in-out"}
_CVZO = {"type": "cover", "zoom": [1.14, 1.06, 1.0], "pan": [(0.5, 0.5)] * 3, "ease": "ease-out"}

SLIDES = [
    {"img": "GROUP", **_LBI},        # 0
    {"img": "TKKOLDER", **_LBN},     # 1
    {"img": "PLANTATION", **_LBI},   # 2
    {"img": "PLANTATION", **_LBO},   # 3
    {"img": "BULLOCKCART", **_CVZ},  # 4
    {"img": "TINNING", **_CVZO},     # 5
    {"img": "CANNERYINSIDE", **_CVZ},  # 6
    {"img": "LKC", **_LBN},          # 7
    {"img": "NEESOON", **_LBW},      # 8
    {"img": "NEESOONRD", **_CVZ},    # 9
    {"img": "NEESOON", **_LBO},      # 10
    {"img": "NEESOONRD", **_CVZ},    # 11
    {"img": "CHS", **_LBO},          # 12
    {"img": "NEESOONRD", **_CVZO},   # 13
    {"img": "TKKYOUNG", **_LBW},     # 14
    {"img": "TKKOLDER", **_LBI},     # 15
    {"img": "GROUP", **_LBN},        # 16
    {"img": "CHS", **_LBW},          # 17
    {"img": "TKKOLDER", **_LBO},     # 18
    {"img": "LKC", **_LBI},          # 19
    {"img": "LKC", **_LBW},          # 20
    {"img": "CHSCLASS", **_LBN},     # 21
    {"img": "LKC", **_LBO},          # 22
    {"img": "CHS", **_LBI},          # 23
    {"img": "MAP", **_LBN},          # 24
    {"img": "CHSCLASS", **_LBO},     # 25
    {"img": "NEESOON", **_LBN},      # 26
    {"img": "GROUP", **_LBO},        # 27
]

# Real per-sentence starts from
# audio/singapore-canned-pineapple-kings.timing.json. Slide index runs
# 0..27 in order.
#   0  s0-2    title; 1912 world's-largest-exporter hook; absent from
#              the economic story now
#   1  s3-4    pineapple came first; seeded 3 fortunes
#   2  s5-6    commercial scale 1880s; rubber's 5-7 year wait
#              (a real Buona Vista Road pineapple plantation, c.1910)
#   3  s7-8    pineapple's 18-month fruiting / poor soil; planters
#              interplant the two (same plantation photo, pulled out)
#   4  s9-10   catch-cropping term; canneries follow the plantations
#              (a bullock cart delivering pineapples to a cannery, 1902)
#   5  s11-12  canneries cluster at Clarke Quay etc; some large operations
#              (a pile of pineapples ready for tinning, 1902)
#   6  s13-14  J. P. Bastiani's cannery; most owners Chinese
#              (inside a Chinese-run cannery, 1904)
#   7  s15     the "pineapple kings" named (Tan Tye, and the three ahead)
#   8  s16-17  Lim Nee Soon named; born 1879, estates, chamber president
#   9  s18-19  ran his estates; "Pineapple King" nickname
#   10 s20-21  died Shanghai 1936, buried Nanjing
#   11 s22-23  estates became Yishun; Nee Soon Road gazetted 1950
#   12 s24-26  1980s Mandarin standardisation; complaints; the older name
#              survives (Road, Camp, electoral division)
#   13 s27-28  Khatib Camp NS aside; never knew the name was a person
#   14 s29-30  Tan Kah Kee named; pineapple where his fortune began
#   15 s31-32  Sembawang cannery; into rubber; 15,000 acres by mid-1920s
#   16 s33-35  Depression collapse 1934; remembered for the money spent
#   17 s36-37  Chinese High School 1919 / Xiamen University 1921; wartime
#              fundraising puts him on the Kempeitai's list
#   18 s38-39  left for China 1950, died Beijing 1961
#   19 s40     Lee Kong Chian named; arrived 1903, married Tan's daughter
#   20 s41-42  Lee Rubber late 1920s; Lee Pineapple ~1930; OCBC/pro-chancellor
#   21 s43-45  Lee Pineapple moved to Johor; ran 92 years
#   22 s46-47  stopped canning end 2023, turned to oil palm; Lee Foundation 1952
#   23 s48-49  names on institutions; why it vanished from Singapore
#   24 s50-51  land value priced pineapple out; plantations built over
#              (OSM map of where the story happened: canneries, estates,
#              and Skudai across the Causeway, still running until 2023)
#   25 s52     Malaya's own industry peaked late 1960s, then fell away
#   26 s53-54  why it fits the bigger story; no monument, no museum
#   27 s55     what's left is indirect - a town's name, a foundation
#              still giving, a tin of pineapple tarts
SCHEDULE = [
    (0.0, 0), (29.225, 1), (49.975, 2), (65.7, 3), (84.375, 4),
    (97.725, 5), (113.575, 6), (127.6, 7), (141.45, 8), (166.3, 9),
    (182.525, 10), (198.25, 11), (214.95, 12), (240.25, 13), (254.125, 14),
    (268.65, 15), (297.425, 16), (314.65, 17), (342.8, 18), (355.35, 19),
    (366.625, 20), (389.95, 21), (409.875, 22), (432.625, 23), (446.925, 24),
    (475.7, 25), (495.275, 26), (506.475, 27),
]
TOTAL_DURATION = 531.75
TIMING_JSON = "audio/singapore-canned-pineapple-kings.timing.json"
