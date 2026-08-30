"""Video config for "The Vegetable Seller Behind Singapore's Most
Recognisable Hospital Name" (Tan Tock Seng) - Watch widget and main video.

The post's chart is a single horizontal relocation timeline (Pearl's
Hill 1844 -> Serangoon Road 1861 -> Moulmein Road 1909 -> Novena 2000),
which compose_chart_frame() can't animate (single calendar-year line
only). It's rendered once to a static PNG by
scripts/render_tan_tock_seng_timeline.py ->
assets/images/tan-tock-seng-timeline.png and used here as a near-static
slide on the "four addresses in 156 years" beat.

Images (2 post + the chart + 8 gallery):
  PORTRAIT   - Tan Tock Seng, painted c.1840s (post hero)
  HOSPITAL   - the hospital's original Pearl's Hill building, c.1844-1856
  CHART      - the static relocation-timeline PNG
  KIMCHING   - Tan Kim Ching, the son who kept funding it
  THIAN      - Thian Hock Keng temple, c.1890 - Telok Ayer St
  BOATQUAY   - the Singapore River / harbour from Boat Quay, 1860 (a wide
               panorama - covers with a long horizontal pan)
  HARBOUR    - Singapore harbour, 1866 engraving by Frederick Grosse
  SHOPHOUSES - shophouses along the Singapore River (KITLV)
  TELOKAYER  - Telok Ayer Market, drawn by J.T. Thomson in 1847
  PUBLICOFF  - the colonial Public Offices, drawn by J.T. Thomson in 1846
  OUTRAM     - Outram / Pearl's Hill Prison, photographed in the 1850s

19 slides, 297.475s. Aspect check (1280x720, ~1.44 cover threshold):
  PORTRAIT 512x744 (0.69)   -> letterbox
  HOSPITAL 680x388 (1.75)   -> letterbox (only 680px wide - keep it small)
  CHART 1280x720 (1.78)     -> letterbox (exact fit), near-zero zoom
  KIMCHING 2426x3334 (0.73) -> letterbox
  THIAN 6378x4803 (1.33)    -> letterbox
  BOATQUAY 12874x2716 (4.74)-> cover, long horizontal pan across the panorama
  HARBOUR 4182x3187 (1.31)  -> letterbox
  SHOPHOUSES 2311x1753 (1.32)-> letterbox
  TELOKAYER 1600x1200 (1.33)-> letterbox
  PUBLICOFF 800x549 (1.46)  -> letterbox (only 800px wide)
  OUTRAM 3150x1339 (2.35)   -> cover, horizontal pan
Letterbox slides use zero pan (blurred-bg zoom only), so --check-only
flags them JERKY - the documented letterbox false positive (pipeline
section 5); the near-static CHART slide reads JERKY for the same reason.
"""

_C = "https://upload.wikimedia.org/wikipedia/commons"
_T = "https://upload.wikimedia.org/wikipedia/commons/thumb"

IMAGES = {
    "PORTRAIT": f"{_C}/4/45/Tan_Tock_Seng.jpg",
    "HOSPITAL": f"{_C}/c/c3/Tan_Tock_Seng_Hospital_circa_1844-1856.jpg",
    "CHART": "/assets/images/tan-tock-seng-timeline.png",
    "KIMCHING": f"{_C}/c/cc/Tan_Kim_Ching.jpg",
    "THIAN": f"{_T}/8/81/KITLV_-_103742_-_Lambert_%26_Co._-_Thian_Hock_Keng_Temple_in_Singapore_-_circa_1890.tif/lossy-page1-1280px-KITLV_-_103742_-_Lambert_%26_Co._-_Thian_Hock_Keng_Temple_in_Singapore_-_circa_1890.tif.jpg",
    "BOATQUAY": f"{_T}/7/79/KITLV_-_29175_-_View_of_the_harbor_of_Singapore_-_1860.tif/lossy-page1-1920px-KITLV_-_29175_-_View_of_the_harbor_of_Singapore_-_1860.tif.jpg",
    "HARBOUR": f"{_C}/0/07/Singapore_January_20_1866_Frederick_Grosse.jpg",
    "SHOPHOUSES": f"{_T}/4/44/Shophouses_aan_de_Singapore-rivier_te_Singapore%2C_KITLV_156146.tiff/lossy-page1-1280px-Shophouses_aan_de_Singapore-rivier_te_Singapore%2C_KITLV_156146.tiff.jpg",
    "TELOKAYER": f"{_C}/7/77/Telok_Ayer_Market_-_J.T._Thomson.jpg",
    "PUBLICOFF": f"{_C}/d/df/Public_Offices%2C_Singapore_by_John_Turnbull_Thomson_1846.jpg",
    "OUTRAM": f"{_C}/5/54/Photograph_of_Outram_Prison_%28Pearl%E2%80%99s_Hill_Prison%29_in_the_1850%27s.jpg",
}

CREDITS = {
    "CHART": "Relocation timeline by Lesser Known Singapore, from the dates cited in the post",
}

SLIDES = [
    {"img": "PORTRAIT", "type": "letterbox", "zoom": [1, 1.05, 1.10], "pan": [(0.5, 0.5), (0.5, 0.5), (0.5, 0.5)], "ease": "ease-in-out"},
    {"img": "BOATQUAY", "type": "cover", "zoom": [1, 1.04, 1.08], "pan": [(0.08, 0.5), (0.5, 0.5), (0.92, 0.5)], "ease": "linear"},
    {"img": "SHOPHOUSES", "type": "letterbox", "zoom": [1, 1.06, 1.12], "pan": [(0.5, 0.5), (0.5, 0.5), (0.5, 0.5)], "ease": "ease-in"},
    {"img": "TELOKAYER", "type": "letterbox", "zoom": [1, 1.06, 1.12], "pan": [(0.5, 0.5), (0.5, 0.5), (0.5, 0.5)], "ease": "ease-in-out"},
    {"img": "PUBLICOFF", "type": "letterbox", "zoom": [1, 1.05, 1.10], "pan": [(0.5, 0.5), (0.5, 0.5), (0.5, 0.5)], "ease": "ease-in-out"},
    {"img": "THIAN", "type": "letterbox", "zoom": [1, 1.06, 1.12], "pan": [(0.5, 0.5), (0.5, 0.5), (0.5, 0.5)], "ease": "ease-in"},
    {"img": "HARBOUR", "type": "letterbox", "zoom": [1, 1.05, 1.10], "pan": [(0.5, 0.5), (0.5, 0.5), (0.5, 0.5)], "ease": "ease-in-out"},
    {"img": "OUTRAM", "type": "cover", "zoom": [1, 1.05, 1.10], "pan": [(0.15, 0.5), (0.5, 0.5), (0.85, 0.5)], "ease": "ease-in-out"},
    {"img": "PORTRAIT", "type": "letterbox", "zoom": [1.10, 1.05, 1], "pan": [(0.5, 0.5), (0.5, 0.5), (0.5, 0.5)], "ease": "ease-out"},
    {"img": "PUBLICOFF", "type": "letterbox", "zoom": [1.10, 1.05, 1], "pan": [(0.5, 0.5), (0.5, 0.5), (0.5, 0.5)], "ease": "ease-out"},
    {"img": "HOSPITAL", "type": "letterbox", "zoom": [1, 1.06, 1.12], "pan": [(0.5, 0.5), (0.5, 0.5), (0.5, 0.5)], "ease": "ease-in-out"},
    {"img": "OUTRAM", "type": "cover", "zoom": [1.10, 1.05, 1], "pan": [(0.85, 0.5), (0.5, 0.5), (0.15, 0.5)], "ease": "ease-in-out"},
    {"img": "HOSPITAL", "type": "letterbox", "zoom": [1.12, 1.06, 1], "pan": [(0.5, 0.5), (0.5, 0.5), (0.5, 0.5)], "ease": "ease-out"},
    {"img": "PORTRAIT", "type": "letterbox", "zoom": [1, 1.05, 1.10], "pan": [(0.5, 0.5), (0.5, 0.5), (0.5, 0.5)], "ease": "ease-in-out"},
    {"img": "KIMCHING", "type": "letterbox", "zoom": [1, 1.05, 1.10], "pan": [(0.5, 0.5), (0.5, 0.5), (0.5, 0.5)], "ease": "ease-in-out"},
    {"img": "CHART", "type": "letterbox", "zoom": [1, 1.015, 1.03], "pan": [(0.5, 0.5), (0.5, 0.5), (0.5, 0.5)], "ease": "linear"},
    {"img": "PORTRAIT", "type": "letterbox", "zoom": [1.10, 1.05, 1], "pan": [(0.5, 0.5), (0.5, 0.5), (0.5, 0.5)], "ease": "ease-out"},
    {"img": "PUBLICOFF", "type": "letterbox", "zoom": [1, 1.06, 1.12], "pan": [(0.5, 0.5), (0.5, 0.5), (0.5, 0.5)], "ease": "ease-in-out"},
    {"img": "HOSPITAL", "type": "letterbox", "zoom": [1, 1.05, 1.10], "pan": [(0.5, 0.5), (0.5, 0.5), (0.5, 0.5)], "ease": "ease-in-out"},
]

# Real values from audio/tan-tock-seng-pauper-to-philanthropist.timing.json.
# Every point is a real sentence start.
#   0  title + s1     1819: a 21-year-old lands from Malacca with nothing
#   1  s2-4    sells vegetables off a cart / his rise took eight years
#   2  s5-6    Boat Quay shop 1827, the Whitehead land-speculation deal
#   3  s7      by his forties: 50 acres, shophouses, plantations
#   4  s8      "Captain of the Chinese"; first Asian Justice of the Peace
#   5  s9      Hokkien Huay Kuan; helped build Thian Hock Keng, Telok Ayer
#   6  s10-12  not the money - the govt's two-decade failure / the 1840s
#              streets of sick destitute migrants
#   7  s13     the 1834 Chinese Poor House, turned into a jail
#   8  s14     Cham Chan Sang's $2,000 will; Tan adds $5,000
#   9  s15     the govt's answer: a tax on the Chinese; the petition
#   10 s16-17  Tan wins; foundation stone at Pearl's Hill, 25 May 1844
#   11 s18     built 1846, used as a convict jail; the sick in an attap shed
#   12 s19     the shed stands until an 1849 storm; patients finally move in
#   13 s20     Tan dies 24 Feb 1850; 500,000 Spanish dollars to his family
#   14 s21     Tan Kim Ching keeps funding it; moves it to Serangoon Rd 1861
#   15 s22     CHART - Moulmein Rd 1909, Novena 2000: four addresses, 156 yrs
#   16 s23     nobody at Novena connects the name to the man
#   17 s24     the first safety-net hospital wasn't a govt program
#   18 s25     the name is remembered; the fight to get it accepted isn't
SCHEDULE = [
    (0.0, 0), (21.5, 1), (43.025, 2), (57.025, 3), (73.15, 4),
    (87.85, 5), (98.275, 6), (120.65, 7), (131.7, 8), (144.975, 9),
    (161.45, 10), (174.675, 11), (192.325, 12), (208.95, 13), (219.975, 14),
    (235.825, 15), (251.325, 16), (267.025, 17), (288.2, 18),
]
TOTAL_DURATION = 297.475
TIMING_JSON = "audio/tan-tock-seng-pauper-to-philanthropist.timing.json"
