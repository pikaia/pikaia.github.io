"""Video config for the opium-farming post.

Four Commons photos (a genuinely thin pool beyond these), plus three
self-rendered chart/map PNGs mirroring the post's own inline SVGs:

  PROTECTORATE - the Chinese Protectorate building, KITLV postcard,
                 1906-1930 (Commons, CC BY 4.0) - cover, landscape,
                 the post's hero and thematic anchor for sentences with
                 no other photo (institutional/money/reform content)
  CHEANG       - Cheang Hong Lim, from Song Ong Siang's 1923 book
                 (Commons, CC BY-SA 4.0) - letterbox, portrait scan
  SOUTHBRIDGE  - South Bridge Road, c.1900, G.R. Lambert & Co.
                 (Commons, public domain) - cover, landscape
  TOMB         - Cheang Hong Lim's tomb, photographed 2021
                 (Commons, CC BY-SA 4.0) - letterbox, portrait photo
  REGIONALMAP  - rendered by scripts/render_opium_regional_map.py
  LOCALMAP     - rendered by scripts/render_opium_local_map.py
  TIMELINE     - rendered by scripts/render_opium_timeline_chart.py

42 slides, one per sentence.
"""

_U = "https://upload.wikimedia.org/wikipedia/commons"

IMAGES = {
    "PROTECTORATE": f"{_U}/thumb/5/53/Chinese_Protectorate%2C_Singapore%2C_KITLV_1404946.tiff/lossy-page1-1920px-Chinese_Protectorate%2C_Singapore%2C_KITLV_1404946.tiff.jpg",
    "CHEANG": f"{_U}/3/3d/Cheang_Hong_Lim.png",
    "SOUTHBRIDGE": f"{_U}/c/cf/Photographic_Views_of_Singapore_Plate_02_South_Bridge_Road.jpg",
    "TOMB": f"{_U}/6/6e/Tomb_of_Cheang_Hong_Lim.jpg",
    "REGIONALMAP": "/assets/images/opium-regional-map.png",
    "LOCALMAP": "/assets/images/opium-local-map.png",
    "TIMELINE": "/assets/images/opium-timeline-chart.png",
}

CREDITS = {
    "REGIONALMAP": "Chart by Lesser Known Singapore; map data © OpenStreetMap contributors",
    "LOCALMAP": "Chart by Lesser Known Singapore; map data © OpenStreetMap contributors",
    "TIMELINE": "Chart by Lesser Known Singapore, dates per the post's own Sources list",
}

_PROTA = {"type": "cover", "zoom": [1.0, 1.05, 1.1], "pan": [(0.5, 0.4)] * 3, "ease": "ease-in-out"}
_PROTB = {"type": "cover", "zoom": [1.15, 1.08, 1.0], "pan": [(0.35, 0.45)] * 3, "ease": "ease-out"}
_PROTC = {"type": "cover", "zoom": [1.0, 1.06, 1.12], "pan": [(0.65, 0.45)] * 3, "ease": "ease-in-out"}

_CHEA = {"type": "letterbox", "zoom": [1.0, 1.0, 1.0], "pan": [(0.5, 0.5)] * 3, "ease": "linear"}
_CHEB = _CHEA
# CHEANG's source scan is small (344x471) and some of its slides run 12-20s;
# a modest Ken-Burns zoom (the usual portrait-scan pattern, see
# docs/production-pipeline.md) still showed real held-frame jerkiness on
# those longer slides even after widening the zoom range (checked directly
# with --check-only, not guessed) - the image is simply too small to
# supersample enough distinct pixel positions at a slow zoom rate over that
# long a dwell time. Frozen (zero pan/zoom) avoids the question entirely,
# same accepted pattern as the chart/map slides below.

_SBA = {"type": "cover", "zoom": [1.0, 1.05, 1.1], "pan": [(0.5, 0.4)] * 3, "ease": "ease-in-out"}
_SBB = {"type": "cover", "zoom": [1.1, 1.05, 1.0], "pan": [(0.3, 0.42)] * 3, "ease": "ease-out"}
_SBC = {"type": "cover", "zoom": [1.0, 1.06, 1.12], "pan": [(0.7, 0.4)] * 3, "ease": "ease-in-out"}

_TOMBA = {"type": "letterbox", "zoom": [1.0, 1.0, 1.0], "pan": [(0.5, 0.5)] * 3, "ease": "linear"}
# TOMB's slides showed the same held-frame jerkiness at a modest zoom;
# frozen for the same reason as CHEANG above.

_CHART = {"type": "letterbox", "zoom": [1.0, 1.0, 1.0], "pan": [(0.5, 0.5)] * 3, "ease": "linear"}

SLIDES = [
    {"img": "PROTECTORATE", **_PROTA},  # s0  title
    {"img": "PROTECTORATE", **_PROTB},  # s1  govt paid bills with opium money
    {"img": "PROTECTORATE", **_PROTC},  # s2  not smuggling, openly auctioned
    {"img": "PROTECTORATE", **_PROTA},  # s3  single largest revenue source
    {"img": "PROTECTORATE", **_PROTB},  # s4  1820 Farquhar introduces farm
    {"img": "PROTECTORATE", **_PROTC},  # s5  auctioned monopoly licence
    {"img": "PROTECTORATE", **_PROTA},  # s6  farmer kept excess, govt banked cheque
    {"img": "PROTECTORATE", **_PROTB},  # s7  same system covered spirits/gambling
    {"img": "CHEANG", **_CHEA},         # s8  1870s Great Syndicate consolidated
    {"img": "CHEANG", **_CHEB},         # s9  leading figure Cheang Hong Lim
    {"img": "CHEANG", **_CHEA},         # s10 1871-79 held Singapore/Johor/Melaka/Riau
    {"img": "CHEANG", **_CHEB},         # s11 1876 funded Hong Lim Park
    {"img": "REGIONALMAP", **_CHART},   # s12 supply chain sat on top
    {"img": "REGIONALMAP", **_CHART},   # s13 Bengal/Malwa opium from India
    {"img": "REGIONALMAP", **_CHART},   # s14 Singapore transshipment point
    {"img": "REGIONALMAP", **_CHART},   # s15 1836, 3,900 chests in a week
    {"img": "PROTECTORATE", **_PROTC},  # s16 fiscal engine unlike anything else
    {"img": "PROTECTORATE", **_PROTA},  # s17 40-60 percent of revenue
    {"img": "PROTECTORATE", **_PROTB},  # s18 1914 military funding, opium
    {"img": "PROTECTORATE", **_PROTC},  # s19 free port running on a single drug
    {"img": "SOUTHBRIDGE", **_SBA},     # s20 collected one pipe at a time
    {"img": "SOUTHBRIDGE", **_SBB},     # s21 South Bridge Road, Boat Quay, Amoy St
    {"img": "LOCALMAP", **_CHART},      # s22 map below marks the story
    {"img": "PROTECTORATE", **_PROTA},  # s23 organised opposition building
    {"img": "PROTECTORATE", **_PROTB},  # s24 Lim Boon Keng co-founded 1906
    {"img": "PROTECTORATE", **_PROTC},  # s25 Anti-Opium Society 1907
    {"img": "PROTECTORATE", **_PROTA},  # s26 1909 Chandu Revenue Ordinance
    {"img": "TIMELINE", **_CHART},      # s27 ending farm didn't end dependence
    {"img": "TIMELINE", **_CHART},      # s28 1925 Reserve Fund, 1930 factory
    {"img": "SOUTHBRIDGE", **_SBC},     # s29 harder to pin down cost
    {"img": "SOUTHBRIDGE", **_SBA},     # s30 1907 Commission, scraping dregs
    {"img": "SOUTHBRIDGE", **_SBB},     # s31 campaigners like Lim Boon Keng
    {"img": "TIMELINE", **_CHART},      # s32 took a world war to end
    {"img": "TIMELINE", **_CHART},      # s33 1943 Japanese Occupation ban
    {"img": "TIMELINE", **_CHART},      # s34 1951 Dangerous Drugs Ordinance
    {"img": "TIMELINE", **_CHART},      # s35 Chen Su Lan lived to see it outlawed
    {"img": "TOMB", **_TOMBA},          # s36 Cheang did not live to see this
    {"img": "TOMB", **_TOMBA},          # s37 died 1893
    {"img": "TOMB", **_TOMBA},          # s38 tomb stands today, Hong Lim Park
    {"img": "PROTECTORATE", **_PROTA},  # s39 closing: free port charged no duties
    {"img": "PROTECTORATE", **_PROTB},  # s40 had opium instead
    {"img": "PROTECTORATE", **_PROTC},  # s41 single most reliable source, until...
]

SCHEDULE = [
    (0.0, 0), (3.52, 1), (10.68, 2), (29.5, 3), (45.88, 4),
    (64.78, 5), (84.0, 6), (93.65, 7), (102.05, 8), (114.28, 9),
    (121.5, 10), (139.12, 11), (158.95, 12), (168.22, 13), (184.15, 14),
    (198.38, 15), (209.95, 16), (216.45, 17), (232.53, 18), (251.7, 19),
    (258.85, 20), (263.0, 21), (276.77, 22), (301.5, 23), (307.9, 24),
    (323.82, 25), (336.43, 26), (355.12, 27), (361.65, 28), (387.93, 29),
    (397.9, 30), (410.52, 31), (418.8, 32), (422.4, 33), (435.85, 34),
    (448.15, 35), (463.18, 36), (467.7, 37), (475.55, 38), (491.82, 39),
    (502.1, 40), (504.57, 41),
]
TOTAL_DURATION = 522.27
TIMING_JSON = "audio/how-opium-paid-for-colonial-singapore.timing.json"
