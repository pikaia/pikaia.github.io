"""Video config for the Jalan Payoh Lai / Kangkar post's Watch widget /
main video.

Re-cut (2026-09-03) to fold in nine photographs from the Chancery
Archives, Roman Catholic Archdiocese of Singapore, reproduced by
permission for this post and video only (Rev. Fr. Rene Nicolas
Collection; Maria Lee Ah Kin Collection). Each has a mandatory credit
line - see CREDITS; stage_youtube_text.py puts them in the description.
The three small Maria Lee Ah Kin photos (fisherman, Chng family, Punggol
girls) plus the Maistre carte-de-visite are shown frozen (no Ken Burns
zoom) since they don't take enlargement - _FRZ.

Resynced (2026-09-03) to the re-run narration
(audio/...-nativity-church.timing.json, 398.875s) after the Kangkar
pronunciation fix, and MAISTRE added on the Fr Maistre beat (slide 3);
FISHERMAN moved to the "Teochew planters / kangchu" beat (slide 10).

Slide 1 is a route-walk slide. build_watch_widget.py animates it in the
in-post widget; watch_video_lib.py renders it as a black segment
(28.475-55.675s) for the route clip from render_route_clip.py to be
spliced over (--duration ~27.25). See CLAUDE.md's Route animations section.

Cover slides use _CVZ (centred push-in) except two that pass the
smoothness check on a horizontal pan (_CVL, slides 13 and 18); the
_CVL/_CVR wide pan reads JERKY on lower-detail source images.

21 slides, 398.875s.
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
    "MAISTRE": f"{_C}/c/c0/Ambroise_Maistre%2C_MEP_missionary_%281821-1866%29.jpg",
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
# 2026). The Wikimedia images resolve their credits from the post/gallery
# captions; MAISTRE (also a Wikimedia Commons file now) gets an explicit
# line so the YouTube description reads cleanly.
CREDITS = {
    "MAISTRE": ("Portrait of Fr Ambroise Maistre (1821-1866), Missions Etrangeres de Paris; "
                "archives of the Institut de Recherche France-Asie (IRFA) / Missions Etrangeres "
                "de Paris, via Wikimedia Commons, public domain."),
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
    {"img": "MAISTRE", **_FRZ},           # 3
    {"img": "CHURCHNIGHT", **_CVZ},       # 4
    {"img": "CHURCHINT", **_CVZ},         # 5
    {"img": "HIESFACADE", **_LBI},        # 6
    {"img": "HIESGROUP", **_LBW},         # 7
    {"img": "HIESFACADE", **_LBO},        # 8
    {"img": "KAMPONGHOUSES", **_LBI},     # 9
    {"img": "FISHERMAN", **_FRZ},         # 10
    {"img": "PARISHIONERS", **_LBW},      # 11
    {"img": "CHNGFAMILY", **_FRZ},        # 12
    {"img": "PUNGGOLPARK", **_CVL},       # 13
    {"img": "PUNGGOLGIRLS", **_FRZ},      # 14
    {"img": "KAMPONGHOUSES", **_LBO},     # 15
    {"img": "HOUGANGHDB", **_CVZ},        # 16
    {"img": "AERIAL", **_CVZ},            # 17
    {"img": "WPHOUGANG", **_CVL},         # 18
    {"img": "CHURCHNIGHT", **_CVZ},       # 19
    {"img": "MARIANSTATUE", **_LBW},      # 20
]

# Real per-sentence starts from
# audio/jalan-payoh-lai-kangkar-montfort-nativity-church.timing.json
# (re-run narration, 2026-09-03). Slide index runs 0..20 in order.
#   0  s0-4    title; born 1960 on Jalan Payoh Lai; the twenty-minute walk
#              (AERIAL: the church, old school and new town in one frame)
#   1  s5-8    route-walk: the shortcut past Montfort down Holy Innocents'
#              Lane; the lane and cemetery gone from the map
#   2  s9-11   Sunday walk to Mass; the old church older than anything
#   3  s12-13  Fr Ambroise Maistre buys the land in 1857 for the Teochew
#              Catholic farmers and fishermen; converts from Shantou
#              (his carte-de-visite portrait)
#   4  s14-15  the attap chapel becomes the Neo-Gothic church, blessed
#              1901, a national monument since 2005
#   5  s16-17  the Teochew-language Mass; Montfort next door
#   6  s18-20  founded 1916 as Holy Innocents' English School; the
#              Brothers of Saint Gabriel take it over in 1936
#   7  s21-22  the tangle of "Holy Innocents" schools (Boys School, CHIJ
#              Our Lady of the Nativity, Holy Innocents' High to 1892)
#   8  s23-25  renamed Montfort in 1958 to end the confusion; which school
#              the lane was named for is unclear
#   9  s26-29  Montfort moves to Hougang Avenue 8 in 1992; the lane and
#              cemetery are cleared; "Au Kang" / "foot of the stream"
#   10 s30     Teochew planters and the kangchu jungle-clearing
#              plantations along Sungei Serangoon (kampong working life)
#   11 s31     roughly twenty kangkars by an 1849 count; the parish
#              community
#   12 s32     by 1986 more than nine in ten Kangkar villagers were still
#              Teochew
#   13 s33-34  the Kangkar of the 1980s was cleared in 1984, its land
#              folded into Punggol Park
#   14 s35-37  Punggol End and Kampong Wak Sumang; located, like
#              everywhere then, by road and milestone
#   15 s38-39  reclamation announced 1983; the fishing port lasted until
#              1997 and Punggol New Town
#   16 s40-41  Hougang New Town announced 1979, built out by 1992 - the
#              year Montfort left
#   17 s42-43  one thing about the area never got redeveloped; Hougang
#              held by the Workers' Party since 1991
#   18 s44     a marker of a matured electoral landscape
#   19 s45-47  the Kangkar of childhood can't be reconstructed; what's
#              left is the walk, and the church that outlasted it all
#   20 s48-50  why it matters; Montfort School and Nativity Church the
#              rare fixed points; still able to find the way back
SCHEDULE = [
    (0.0, 0), (28.475, 1), (55.675, 2), (77.425, 3), (91.75, 4),
    (108.4, 5), (127.425, 6), (149.025, 7), (165.625, 8), (191.275, 9),
    (212.675, 10), (222.875, 11), (229.7, 12), (239.2, 13), (253.15, 14),
    (279.525, 15), (298.275, 16), (318.225, 17), (332.85, 18), (346.4, 19),
    (372.725, 20),
]
TOTAL_DURATION = 398.875
TIMING_JSON = "audio/jalan-payoh-lai-kangkar-montfort-nativity-church.timing.json"
