"""Video config for the Elizabeth Choy post.

Eight images for a historically thin-photo subject - just two real
portraits of Choy herself survive on Commons, so the wartime/Kempeitai
sections lean on the YMCA site itself (the post's own hook, and
genuinely what those sentences are about) and the England/Occupation
context images (Changi Prison, the surrender ceremony, liberated POWs,
the Gordine sculpture) rather than forcing variety the source material
doesn't have.

  HERO_YMCA     - the YMCA building today, 1 Orchard Road (hero)
  WEDDING1941   - Elizabeth Choy on her wedding day, 16 August 1941
  CHANGI1936    - Changi Prison, photographed in 1936
  SURRENDER1945 - the Japanese surrender ceremony, September 1945
  POW1945       - liberated Allied POWs at Changi Prison, c. 1945
  SERENEJADE    - "Serene Jade" (1949) by Dora Gordine, National Gallery
  CHOY1953      - Elizabeth Choy with her daughters, 1953
  MUSEUM        - the National Museum of Singapore, across the road
                  from the YMCA site (closing image)

All photos, centred cover zoom, no horizontal pan.

31 slides, 475.55s.
"""

_U = "https://upload.wikimedia.org/wikipedia/commons"
_C = f"{_U}/thumb"

IMAGES = {
    "HERO_YMCA": f"{_C}/b/b8/YMCA_Building_2.JPG/1280px-YMCA_Building_2.JPG",
    "WEDDING1941": f"{_U}/0/03/Elizabeth_Choy%2C_1941.jpg",
    "CHANGI1936": f"{_C}/3/31/Changi_Prison_in_1936.jpg/1280px-Changi_Prison_in_1936.jpg",
    "SURRENDER1945": f"{_U}/b/ba/Signing_of_the_Japanese_Surrender_at_Singapore%2C_1945_CF719.jpg",
    "POW1945": f"{_U}/f/f2/Allied_prisoners_of_war_after_the_liberation_of_Changi_Prison%2C_Singapore_-_c._1945.jpg",
    "SERENEJADE": f"{_C}/5/50/Serene_Jade_%281949%29_by_Dora_Gordine%2C_National_Gallery_Singapore_-_20160101.jpg/1280px-Serene_Jade_%281949%29_by_Dora_Gordine%2C_National_Gallery_Singapore_-_20160101.jpg",
    "CHOY1953": f"{_U}/7/79/Elizabeth_Choy%2C_1953.png",
    "MUSEUM": f"{_C}/c/c5/National_Museum_of_Singapore%2C_Stamford_Road%2C_October_2025.jpg/1280px-National_Museum_of_Singapore%2C_Stamford_Road%2C_October_2025.jpg",
}

_CVZ = {"type": "cover", "zoom": [1.0, 1.06, 1.12], "pan": [(0.5, 0.5)] * 3, "ease": "ease-in-out"}
_CVZO = {"type": "cover", "zoom": [1.12, 1.06, 1.0], "pan": [(0.5, 0.5)] * 3, "ease": "ease-out"}

# WEDDING1941 (351x522) and CHOY1953 (532x813) are small, portrait-oriented
# scans - covering a landscape frame already crops in hard on just a
# vertical strip, so the normal _CVZ/_CVZO zoom range pushes past her face
# into a tight, pixelated close-up by the end of the animation (caught by
# Chris watching the rendered video, 2026-09-11). Same pan, much flatter
# zoom for these two images only.
_CVZ_FLAT = {"type": "cover", "zoom": [1.0, 1.015, 1.03], "pan": [(0.5, 0.5)] * 3, "ease": "ease-in-out"}
_CVZO_FLAT = {"type": "cover", "zoom": [1.03, 1.015, 1.0], "pan": [(0.5, 0.5)] * 3, "ease": "ease-out"}

SLIDES = [
    {"img": "HERO_YMCA", **_CVZ},        # 0  s0-1   title; the YMCA, Orchard/Stamford junction
    {"img": "HERO_YMCA", **_CVZO},       # 1  s2     nobody knows; Kempeitai East District Branch, 200 days
    {"img": "WEDDING1941", **_CVZ_FLAT}, # 2  s3-4   born Yong Su-Moi, Kudat; father, Kadazan nanny
    {"img": "WEDDING1941", **_CVZO_FLAT},# 3  s5-6   grandfather's school, St Monica's; Singapore, CHIJ, Selegie Road
    {"img": "WEDDING1941", **_CVZ_FLAT}, # 4  s7-8   mother died, Depression; teaching career begins
    {"img": "WEDDING1941", **_CVZO_FLAT},# 5  s9     married Choy Khun Heng, 16 August 1941
    {"img": "CHANGI1936", **_CVZ},       # 6  s10-11 Singapore falls; the canteen at Miyako Hospital
    {"img": "CHANGI1936", **_CVZO},      # 7  s12    smuggling food, medicine, money, radio parts to Changi
    {"img": "CHANGI1936", **_CVZ},       # 8  s13    Operation Jaywick
    {"img": "HERO_YMCA", **_CVZ},        # 9  s14    the Kempeitai's Double Tenth reprisals
    {"img": "HERO_YMCA", **_CVZO},       # 10 s15    57 detained, 15 died
    {"img": "HERO_YMCA", **_CVZ},        # 11 s16    an informant names the Choys
    {"img": "HERO_YMCA", **_CVZO},       # 12 s17    her husband arrested, 29 October
    {"img": "HERO_YMCA", **_CVZ},        # 13 s18    she goes to ask after him, lured back
    {"img": "HERO_YMCA", **_CVZO},       # 14 s19    interrogated at the East District Branch
    {"img": "HERO_YMCA", **_CVZ},        # 15 s20-21 starved and tortured 200 days; R. H. Scott's testimony
    {"img": "HERO_YMCA", **_CVZO},       # 16 s22-23 her faith kept her intact; her husband released later
    {"img": "SURRENDER1945", **_CVZ},    # 17 s24    the Japanese surrender, Lady Mountbatten's invitation
    {"img": "POW1945", **_CVZ},          # 18 s25    invited to England to recuperate
    {"img": "SURRENDER1945", **_CVZO},   # 19 s26    the Girl Guides' Bronze Cross, the Star of Sarawak
    {"img": "SURRENDER1945", **_CVZ},    # 20 s27    OBE, the private audience with Queen Elizabeth
    {"img": "SERENEJADE", **_CVZ},       # 21 s28    modelling for Dora Gordine's sculptures
    {"img": "CHOY1953", **_CVZ_FLAT},    # 22 s29-30 back in Singapore, 1949; the 1950 City Council election
    {"img": "CHOY1953", **_CVZO_FLAT},   # 23 s31    nominated to the Legislative Council
    {"img": "CHOY1953", **_CVZ_FLAT},    # 24 s32    the coronation of Elizabeth the Second, 1953
    {"img": "CHOY1953", **_CVZO_FLAT},   # 25 s33    Queenstown, then leaving politics
    {"img": "CHOY1953", **_CVZ_FLAT},    # 26 s34    back to teaching; the Singapore School for the Blind
    {"img": "CHOY1953", **_CVZO_FLAT},   # 27 s35    qipaos and bangles; "Gunner Choy"
    {"img": "WEDDING1941", **_CVZ_FLAT}, # 28 s36    Elizabeth Choy dies, 2006, aged 95
    {"img": "HERO_YMCA", **_CVZO},       # 29 s37    why it matters: the building still stands
    {"img": "MUSEUM", **_CVZ},           # 30 s38    her name survives in institutions, not a street sign
]

SCHEDULE = [
    (0.0, 0), (17.350, 1), (34.000, 2), (54.725, 3), (81.150, 4),
    (111.575, 5), (122.525, 6), (140.250, 7), (156.200, 8), (169.775, 9),
    (188.850, 10), (196.050, 11), (202.150, 12), (206.625, 13), (219.650, 14),
    (233.600, 15), (254.350, 16), (266.450, 17), (285.025, 18), (290.275, 19),
    (301.150, 20), (322.050, 21), (340.250, 22), (355.600, 23), (369.800, 24),
    (386.000, 25), (393.625, 26), (406.425, 27), (427.750, 28), (437.925, 29),
    (459.375, 30),
]
TOTAL_DURATION = 475.55
TIMING_JSON = "audio/elizabeth-choy-canteen-operator-who-wouldnt-break.timing.json"
