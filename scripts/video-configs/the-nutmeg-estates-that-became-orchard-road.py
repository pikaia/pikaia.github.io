"""Video config for the nutmeg / Orchard Road post.

Four eras covered with 14 images: an 1819-23 Chinese-artist botanical
watercolour of nutmeg (Farquhar Collection), an 1842 painting of the
actual Cairnhill estate, a 1923 photo of a Singapore nutmeg grove, the
plantation-era survivors (Cuppage's gravestone, Burkill Hall), the
Peranakan suburb that followed (Emerald Hill Road in 1973-74 and
today), the modern shopping belt (Orchard Road at night, ION Orchard
with the Nutmeg and Mace sculpture), and five present-day street-sign
shots that are the post's own "fossil record" payoff.

  HERO_NIGHT      - Orchard Road at night, 2011 (hero)
  FARQUHAR        - nutmeg branch, Chinese-artist watercolour, 1819-23
  NUTMEG_TREES    - nutmeg trees, Singapore, 1923 photo
  DYCE_CAIRNHILL  - Cairnhill estate, painted by C. A. Dyce, 1842
  CUPPAGE_GRAVE   - gravestone of William Cuppage, Fort Canning Green
  BURKILL_HALL    - Burkill Hall, Singapore Botanic Gardens
  EMERALD_1973    - Emerald Hill Road, 1973-74
  EMERALD_TERRACE - Emerald Hill Road terrace houses, 2012
  ION_ORCHARD     - ION Orchard at dusk (the Nutmeg and Mace sculpture
                    is faintly visible at street level)
  NUTMEG_ROAD     - Nutmeg Road street sign, Novena
  CUPPAGE_ROAD    - Cuppage Road street sign
  KILLINEY_ROAD   - Killiney Road street sign
  CLAYMORE_ROAD   - Claymore Road street sign
  SCOTTS_ROAD     - Scotts Road street sign

All photos, centred cover zoom, no horizontal pan.

40 slides, 655.875s.
"""

_U = "https://upload.wikimedia.org/wikipedia/commons"
_C = f"{_U}/thumb"

IMAGES = {
    "HERO_NIGHT": f"{_C}/a/a0/Orchard_Road_at_night%2C_2011.jpg/1280px-Orchard_Road_at_night%2C_2011.jpg",
    "FARQUHAR": f"{_U}/5/5d/Booa_Palla%3B_Nutmeg%3B_Myristica_moschata_%28William_Farquhar_Collection%2C_1819%E2%80%931823%29.jpg",
    "NUTMEG_TREES": f"{_C}/d/d1/Nutmeg-trees%2C_Singapore%2C_photo_from_The_Encyclopedia_of_Food_by_Artemas_Ward.jpg/1280px-Nutmeg-trees%2C_Singapore%2C_photo_from_The_Encyclopedia_of_Food_by_Artemas_Ward.jpg",
    "DYCE_CAIRNHILL": f"{_C}/0/07/Charles_Andrew_Dyce%2C_Cairnhill%2C_Singapore%2C_1842%2C_Watercolour_%26_ink_on_paper%2C_263_x_363_mm.png/1280px-Charles_Andrew_Dyce%2C_Cairnhill%2C_Singapore%2C_1842%2C_Watercolour_%26_ink_on_paper%2C_263_x_363_mm.png",
    "CUPPAGE_GRAVE": f"{_C}/5/57/Gravestone_of_William_Cuppage%2C_Fort_Canning_Green%2C_Singapore_-_20130401-01.jpg/1280px-Gravestone_of_William_Cuppage%2C_Fort_Canning_Green%2C_Singapore_-_20130401-01.jpg",
    "BURKILL_HALL": f"{_C}/2/25/Burkill_Hall_%2843566915180%29.jpg/1280px-Burkill_Hall_%2843566915180%29.jpg",
    "EMERALD_1973": f"{_C}/7/75/Singapore-Emerald_Hill_Road-1973-74-WUS08237.jpg/1280px-Singapore-Emerald_Hill_Road-1973-74-WUS08237.jpg",
    "EMERALD_TERRACE": f"{_C}/a/a6/Terraced_houses_along_Emerald_Hill_Road%2C_Singapore_-_20121028.jpg/1280px-Terraced_houses_along_Emerald_Hill_Road%2C_Singapore_-_20121028.jpg",
    "ION_ORCHARD": f"{_C}/8/8d/ION_Orchard.jpg/1280px-ION_Orchard.jpg",
    "NUTMEG_ROAD": f"{_C}/3/34/Nutmeg_Road_2.JPG/1280px-Nutmeg_Road_2.JPG",
    "CUPPAGE_ROAD": f"{_C}/2/2d/Cuppage_Road%2C_Singapore_-_20061029.jpg/1280px-Cuppage_Road%2C_Singapore_-_20061029.jpg",
    "KILLINEY_ROAD": f"{_C}/a/a9/Killiney_Road.JPG/1280px-Killiney_Road.JPG",
    "CLAYMORE_ROAD": f"{_C}/a/ad/Claymore_Road.JPG/1280px-Claymore_Road.JPG",
    "SCOTTS_ROAD": f"{_U}/f/fe/Scotts-Road-Singapore-2006.jpg",
}

_CVZ = {"type": "cover", "zoom": [1.0, 1.06, 1.12], "pan": [(0.5, 0.5)] * 3, "ease": "ease-in-out"}
_CVZO = {"type": "cover", "zoom": [1.12, 1.06, 1.0], "pan": [(0.5, 0.5)] * 3, "ease": "ease-out"}

SLIDES = [
    {"img": "HERO_NIGHT", **_CVZ},        # 0  s0-1   title; Orchard Road today, glass towers and malls
    {"img": "FARQUHAR", **_CVZ},          # 1  s2     its name a leftover clue; colonial speculators chasing a spice fortune
    {"img": "NUTMEG_ROAD", **_CVZO},      # 2  s3     the men who planted it are still on the street signs
    {"img": "ION_ORCHARD", **_CVZ},       # 3  s4     Singapore's most expensive shopping street, a map of a spice that failed
    {"img": "FARQUHAR", **_CVZ},          # 4  s5     nutmeg, one of the most valuable commodities on earth; the Dutch monopoly
    {"img": "NUTMEG_TREES", **_CVZ},      # 5  s6     breaking that monopoly; Raffles, Bencoolen, Fort Canning, 1819
    {"img": "DYCE_CAIRNHILL", **_CVZ},    # 6  s7     the pattern that followed through the late 1830s and 1840s
    {"img": "DYCE_CAIRNHILL", **_CVZO},   # 7  s8     an "unthinking mania": Tanglin, Cairnhill, Claymore, Emerald Hill
    {"img": "NUTMEG_TREES", **_CVZ},      # 8  s9-10  a couple of decades a very good bet; land cheap, prices high
    {"img": "FARQUHAR", **_CVZO},         # 9  s11    merchants, surgeons and harbour officials put savings into trees
    {"img": "CUPPAGE_ROAD", **_CVZ},      # 10 s12    the street map still carries the names of the men who planted it
    {"img": "CUPPAGE_GRAVE", **_CVZ},     # 11 s13    William Cuppage; Cuppage Road and Cuppage Terrace
    {"img": "KILLINEY_ROAD", **_CVZO},    # 12 s14    Dr Thomas Oxley, Killiney Estate; Oxley Road and Killiney Road
    {"img": "DYCE_CAIRNHILL", **_CVZ},    # 13 s15    Charles Carnie, Cairnhill, 4,370 nutmeg trees
    {"img": "CLAYMORE_ROAD", **_CVZ},     # 14 s16    Captain William Scott, Claymore Estate; Claymore Road and Scotts Road
    {"img": "SCOTTS_ROAD", **_CVZO},      # 15 s17    none of these men left behind a portrait that has survived
    {"img": "CUPPAGE_ROAD", **_CVZ},      # 16 s18    what is left: an entire grid of roads named for a vanished crop
    {"img": "NUTMEG_TREES", **_CVZ},      # 17 s19-20 the mania collapsed; "nutmeg canker" appeared in the 1840s
    {"img": "NUTMEG_TREES", **_CVZO},     # 18 s21    nobody at the time understood the cause
    {"img": "DYCE_CAIRNHILL", **_CVZ},    # 19 s22-23 the effect was total; "ruin staring the proprietors in the face"
    {"img": "EMERALD_1973", **_CVZ},      # 20 s24    by 1862 cultivation had ceased; estates broken up and sold
    {"img": "BURKILL_HALL", **_CVZ},      # 21 s25    the scale of the wipeout is easy to underestimate
    {"img": "BURKILL_HALL", **_CVZO},     # 22 s26    the Botanic Gardens, 1859, an abandoned nutmeg plantation
    {"img": "BURKILL_HALL", **_CVZ},      # 23 s27    Lawrence Niven; Burkill Hall, the last Anglo-Malay plantation house
    {"img": "EMERALD_1973", **_CVZO},     # 24 s28    with the nutmeg gone, the estates became a quiet suburb
    {"img": "CUPPAGE_GRAVE", **_CVZ},     # 25 s29    Cuppage moved onto the land himself; died there in 1872
    {"img": "EMERALD_1973", **_CVZ},      # 26 s30    daughters, then Edwin Koek, then the Seah brothers
    {"img": "EMERALD_TERRACE", **_CVZO},  # 27 s31    1901, subdivided into 38 lots; Lim Boon Keng bought three
    {"img": "EMERALD_1973", **_CVZ},      # 28 s32    first house 1902; by the 1930s a majority Peranakan street
    {"img": "EMERALD_TERRACE", **_CVZ},   # 29 s33    architect R. T. Rajoo; Peranakan terrace housing
    {"img": "KILLINEY_ROAD", **_CVZ},     # 30 s34    Oxley Road, Lee Kuan Yew's home; Kwa Geok Choo, Peranakan herself
    {"img": "KILLINEY_ROAD", **_CVZO},    # 31 s35    a pleasant coincidence; the surgeon who tried and failed
    {"img": "EMERALD_TERRACE", **_CVZ},   # 32 s36    well into the 20th century, still largely residential
    {"img": "HERO_NIGHT", **_CVZ},        # 33 s37    department stores and cinemas from the 1950s and 60s
    {"img": "ION_ORCHARD", **_CVZO},      # 34 s38    by the 1980s, Singapore's premier shopping street
    {"img": "ION_ORCHARD", **_CVZ},       # 35 s39-40 almost nothing, but not quite; the Nutmeg and Mace sculpture, 2009
    {"img": "NUTMEG_ROAD", **_CVZ},       # 36 s41    easy to walk past without noticing what it is a picture of
    {"img": "NUTMEG_TREES", **_CVZO},     # 37 s42-43 one nutmeg tree still stands; the exception that proves the rule
    {"img": "NUTMEG_ROAD", **_CVZ},       # 38 s44    why it matters today: a street name the only monument left
    {"img": "FARQUHAR", **_CVZO},         # 39 s45    nutmeg never disappeared; Penang, Balik Pulau, still bearing fruit
]

SCHEDULE = [
    (0.0, 0), (14.375, 1), (30.375, 2), (43.975, 3), (51.275, 4),
    (69.075, 5), (91.875, 6), (109.475, 7), (129.700, 8), (143.025, 9),
    (148.750, 10), (153.625, 11), (174.200, 12), (198.075, 13), (216.850, 14),
    (236.125, 15), (247.525, 16), (259.725, 17), (274.400, 18), (292.725, 19),
    (307.650, 20), (318.700, 21), (323.850, 22), (341.425, 23), (362.900, 24),
    (380.325, 25), (392.800, 26), (413.175, 27), (428.975, 28), (449.600, 29),
    (471.300, 30), (489.725, 31), (504.175, 32), (520.025, 33), (544.300, 34),
    (557.600, 35), (581.650, 36), (586.600, 37), (616.375, 38), (636.550, 39),
]
TOTAL_DURATION = 655.875
TIMING_JSON = "audio/the-nutmeg-estates-that-became-orchard-road.timing.json"
