"""Video config for the Jalan Payoh Lai / Kangkar post's Watch widget /
main video.

Re-cut (2026-09-03) to fold in nine photographs from the Chancery
Archives, Roman Catholic Archdiocese of Singapore, reproduced by
permission for this post and video only (Rev. Fr. Rene Nicolas
Collection; Maria Lee Ah Kin Collection). Each has a mandatory credit
line - see CREDITS; stage_youtube_text.py puts them in the description.
The three small Maria Lee Ah Kin photos (fisherman, Chng family, Punggol
girls) are shown frozen (no Ken Burns zoom) since they don't take
enlargement - _FRZ.

Slide 1 is a route-walk slide, not renderable by watch_video_lib.py
(see render_route_clip.py and CLAUDE.md's Route animations section);
build_watch_widget.py flags it MANUAL.

20 slides, 361.125s.
"""

_C = "https://upload.wikimedia.org/wikipedia/commons"
_A = "/assets/images/chancery"

# The post's two SVG maps (Hougang locator, SMC boundary) are left in the
# post/gallery only - watch_video_lib.py can't rasterise SVG, and the
# route-walk slide already carries the "where is this" job here.
IMAGES = {
    "CHURCHNIGHT": f"{_C}/f/f5/Church_of_the_Nativity_of_the_Blessed_Virgin_Mary%2C_night%2C_July_2017.jpg",
    "CHURCHINT": f"{_C}/1/1f/Church_of_the_Nativity_of_the_Blessed_Virgin_Mary_5%2C_Nov_06.JPG",
    "PUNGGOLPARK": f"{_C}/3/3e/Punggol_Park%2C_Nov_06.JPG",
    "HOUGANGHDB": f"{_C}/4/4b/Hougang_HDB_3.JPG",
    "WPHOUGANG": f"{_C}/9/9c/WorkersPartyHougangSupporters.jpg",
    "MARIANSTATUE": f"{_A}/nativity-old-marian-statue.jpg",
    "AERIAL": f"{_A}/nativity-aerial.jpg",
    "HIESFACADE": f"{_A}/hies-facade-1910s.jpg",
    "HIESGROUP": f"{_A}/hies-anniversary.jpg",
    "KAMPONGHOUSES": f"{_A}/aukang-kampong-houses.jpg",
    "PARISHIONERS": f"{_A}/aukang-parishioners.jpg",
    "FISHERMAN": f"{_A}/aukang-fisherman.jpg",
    "PUNGGOLGIRLS": f"{_A}/aukang-punggol-girls.jpg",
    "CHNGFAMILY": f"{_A}/aukang-chng-family-1932.jpg",
}

# Mandatory credit lines from the Chancery Archives (Amanda Lim, 3 Sep
# 2026). The Wikimedia images and the two SVG maps resolve their credits
# from the post/gallery captions.
CREDITS = {
    "MARIANSTATUE": ("Black and white photograph of the outdoor statue of the Blessed Virgin Mary, "
                     "Church of the Nativity of the Blessed Virgin Mary, Hougang, Singapore, undated. "
                     "Rev. Fr. Rene Nicolas Collection, courtesy of the Chancery Archives, Roman Catholic "
                     "Archdiocese of Singapore."),
    "AERIAL": ("Aerial shot of the Church of the Nativity of the Blessed Virgin Mary, Hougang, and its "
               "surrounding complex, undated. Rev. Fr. Rene Nicolas Collection, courtesy of the Chancery "
               "Archives, Roman Catholic Archdiocese of Singapore."),
    "HIESFACADE": ("Black and white photograph of the Holy Innocents' English School building facade, "
                   "c. 1910s. Rev. Fr. Rene Nicolas Collection, courtesy of the Chancery Archives, Roman "
                   "Catholic Archdiocese of Singapore."),
    "HIESGROUP": ("The old school building when Montfort was known as Holy Innocents' English School, "
                  "undated. Rev. Fr. Rene Nicolas Collection, courtesy of the Chancery Archives, Roman "
                  "Catholic Archdiocese of Singapore."),
    "KAMPONGHOUSES": ("Black and white photograph of the parish kampong houses of old Aukang, "
                      "Teochew-Catholic Enclave, Singapore, c.1920s-1930s. Rev. Fr. Rene Nicolas "
                      "Collection, courtesy of the Chancery Archives, Roman Catholic Archdiocese of "
                      "Singapore."),
    "PARISHIONERS": ("Black and white photograph of the kampong parishioners of old Aukang, "
                     "Teochew-Catholic Enclave, Singapore, c.1920s-1930s. Rev. Fr. Rene Nicolas "
                     "Collection, courtesy of the Chancery Archives, Roman Catholic Archdiocese of "
                     "Singapore."),
    "FISHERMAN": ("Working life in the kampong - a young fisherman mending the prawn trawler nets, "
                  "c. 1930s. Maria Lee Ah Kin Collection, courtesy of the Chancery Archives, Roman "
                  "Catholic Archdiocese of Singapore."),
    "PUNGGOLGIRLS": ("Kampong girls riding around the Ponggol 10th milestone neighbourhood, c. 1930s. "
                     "Maria Lee Ah Kin Collection, courtesy of the Chancery Archives, Roman Catholic "
                     "Archdiocese of Singapore."),
    "CHNGFAMILY": ("The extended Chng Family comprising three generations of Aukang Teochew Catholics "
                   "in front of an attap house, 1932. Maria Lee Ah Kin Collection, courtesy of the "
                   "Chancery Archives, Roman Catholic Archdiocese of Singapore."),
}

_CVZ = {"type": "cover", "zoom": [1.0, 1.08, 1.14], "pan": [(0.5, 0.5)] * 3, "ease": "ease-in-out"}
_CVL = {"type": "cover", "zoom": [1.06, 1.06, 1.06], "pan": [(0.2, 0.5), (0.5, 0.5), (0.8, 0.5)], "ease": "ease-in-out"}
_CVR = {"type": "cover", "zoom": [1.06, 1.06, 1.06], "pan": [(0.8, 0.5), (0.5, 0.5), (0.2, 0.5)], "ease": "ease-in-out"}
_LBI = {"type": "letterbox", "zoom": [1.0, 1.04, 1.08], "pan": [(0.5, 0.5)] * 3, "ease": "ease-in-out"}
_LBW = {"type": "letterbox", "zoom": [1.0, 1.05, 1.10], "pan": [(0.5, 0.5)] * 3, "ease": "ease-in-out"}
_LBO = {"type": "letterbox", "zoom": [1.08, 1.04, 1.0], "pan": [(0.5, 0.5)] * 3, "ease": "ease-out"}
_FRZ = {"type": "letterbox", "zoom": [1.0, 1.0, 1.0], "pan": [(0.5, 0.5)] * 3, "ease": "linear"}

SLIDES = [
    {"img": "AERIAL", **_LBI},            # 0
    {"type": "route-walk"},               # 1  MANUAL - see render_route_clip.py
    {"img": "MARIANSTATUE", **_LBI},      # 2
    {"img": "FISHERMAN", **_FRZ},         # 3
    {"img": "CHURCHNIGHT", **_CVR},       # 4
    {"img": "CHURCHINT", **_CVL},         # 5
    {"img": "HIESFACADE", **_LBI},        # 6
    {"img": "HIESGROUP", **_LBW},         # 7
    {"img": "HIESFACADE", **_LBO},        # 8
    {"img": "KAMPONGHOUSES", **_LBI},     # 9
    {"img": "PARISHIONERS", **_LBW},      # 10
    {"img": "CHNGFAMILY", **_FRZ},        # 11
    {"img": "PUNGGOLPARK", **_CVL},       # 12
    {"img": "PUNGGOLGIRLS", **_FRZ},      # 13
    {"img": "KAMPONGHOUSES", **_LBO},     # 14
    {"img": "HOUGANGHDB", **_CVR},        # 15
    {"img": "AERIAL", **_CVZ},            # 16
    {"img": "WPHOUGANG", **_CVL},         # 17
    {"img": "CHURCHNIGHT", **_CVR},       # 18
    {"img": "MARIANSTATUE", **_LBW},      # 19
]

# Real per-sentence starts from
# audio/jalan-payoh-lai-kangkar-montfort-nativity-church-kokoro.timing.json
# (narration unchanged in the re-cut). Slide index runs 0..19 in order.
#   0  s0-4    title; born 1960 on Jalan Payoh Lai; the twenty-minute walk
#              (AERIAL: the church, old school and new town in one frame)
#   1  s5-8    route-walk: the shortcut past Montfort down Holy Innocents'
#              Lane; the lane and cemetery gone from the map
#   2  s9-11   Sunday walk to Mass; the old church; Fr Maistre buys the
#              land in 1857
#   3  s12-13  for the Teochew Catholic farmers and fishermen of Aukang;
#              converts from Shantou
#   4  s14-15  the attap chapel becomes the Neo-Gothic church, blessed
#              1901, a national monument since 2005
#   5  s16-17  the Teochew-language Mass; Montfort next door
#   6  s18-20  founded 1916 as Holy Innocents' English School; the
#              Brothers of St Gabriel take it over in 1936
#   7  s21-24  the tangle of "Holy Innocents" schools; renamed Montfort
#              in 1958 to end the confusion
#   8  s25-26  which school the lane was named for is unclear; Montfort
#              moves to Hougang Avenue 8 in 1992; the lane is cleared
#   9  s27-30  "Au Kang" / "foot of the stream"; Teochew planters and the
#              kangchu jungle-clearing plantations along Sungei Serangoon
#   10 s31     roughly twenty kangkars by an 1849 count; the parish
#              community
#   11 s32     by 1986 more than nine in ten Kangkar villagers were still
#              Teochew
#   12 s33-34  the Kangkar of the 1980s was cleared in 1984, its land
#              folded into Punggol Park
#   13 s35-37  Punggol End and Kampong Wak Sumang; located, like
#              everywhere then, by road and milestone
#   14 s38-39  reclamation announced 1983; the fishing port lasted until
#              1997 and Punggol New Town
#   15 s40-41  Hougang New Town announced 1979, built out by 1992 - the
#              year Montfort left
#   16 s42     one thing about the area never got redeveloped
#   17 s43     Hougang held by the Workers' Party since 1991; a marker of
#              a matured electoral landscape
#   18 s44-46  the Kangkar of childhood can't be reconstructed; what's
#              left is the walk, and the church that outlasted it all
#   19 s47-50  why it matters; Montfort School and Nativity Church the
#              rare fixed points; still able to find the way back
SCHEDULE = [
    (0.0, 0), (24.775, 1), (49.825, 2), (69.3, 3), (82.35, 4),
    (97.425, 5), (114.8, 6), (134.2, 7), (162.5, 8), (183.05, 9),
    (201.375, 10), (207.575, 11), (216.125, 12), (228.425, 13), (252.3, 14),
    (269.55, 15), (287.725, 16), (300.45, 17), (312.675, 18), (336.875, 19),
]
TOTAL_DURATION = 361.125
TIMING_JSON = "audio/jalan-payoh-lai-kangkar-montfort-nativity-church-kokoro.timing.json"
