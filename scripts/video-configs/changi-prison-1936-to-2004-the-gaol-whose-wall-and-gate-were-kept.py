"""Video config for the Changi Prison post.

The pool is the post and gallery's eight pictures:
the liberation photograph from the State Library of
Victoria (the hero), the gaol's own cell door at the
National Museum, outside and in, the Nationaal Archief
portrait of a prisoner eating in his hut (CC0), the
2/18th Battalion men at their hut in September 1945,
the Prison Link Centre of the present complex, one of
the two surviving turrets (a crop of the October 2025
bus-window photograph, self-hosted as a repo asset),
and the 2009 Yellow Ribbon banner on the new wall.
The pool is thin because the Changi Murals and Selarang
posts already used the wartime set; the neighbours'
images are excluded, and the Leslie Cole paintings
are IWM Non Commercial besides.

Named-place audit: the liberation sentences (s50-51,
s51 names the head photograph itself) run on the
liberation photograph; the cell-door sentences
(s12-13) on the door; the gazetting and monument
sentences (s78-80) on the surviving turret; the new
complex sentences (s71-72, s76-77) on the Prison Link
Centre. No slide title names a place its photograph
does not show: the framing slide (s14-15) is titled
for the camp-versus-gaol point, not for the barracks
it names.

53 slides, 979.00s. No slide over 30s; the
longest dwell is 26.65s. Narration: Kokoro with the
OpenVoice clone. Pronunciation overrides for the
post's names filed 2026-11-27, NOT ear-verified yet.
AVATAR: first and last 30s, cartoon with motion.
"""

IMAGES = {
    "GATES": "https://upload.wikimedia.org/wikipedia/commons/9/91/Allied_prisoners_of_war_after_the_liberation_of_Changi_Prison%2C_Singapore_-_c._1945_-_02_edited.jpg",
    "DOOR": "https://upload.wikimedia.org/wikipedia/commons/a/a6/Changi_Prison_cell_door_%28exterior%29%2C_Singapore_History_Gallery%2C_National_Museum_of_Singapore_-_20151125.jpg",
    "DOORIN": "https://upload.wikimedia.org/wikipedia/commons/a/a6/Changi_Prison_cell_door_%28interior%29%2C_Singapore_History_Gallery%2C_National_Museum_of_Singapore_-_20151125.jpg",
    "POW": "https://upload.wikimedia.org/wikipedia/commons/2/2d/Krijgsgevangene_van_de_Japanners_in_Changi_gevangenis_in_Singapore%2C_Bestanddeelnr_935-3623.jpg",
    "HUT": "https://upload.wikimedia.org/wikipedia/commons/2/28/2-18th_Changi.jpg",
    "LINK": "https://upload.wikimedia.org/wikipedia/commons/b/b2/Changi_Prison%2C_Singapore.jpg",
    "TURRET": "/assets/images/changi-turret-2025.jpg",
    "BANNER": "https://upload.wikimedia.org/wikipedia/commons/4/45/Banner_on_a_wall_of_Changi_Prison%2C_Singapore_-_20090116.jpg",
}

# Every image is captioned in the post or its gallery.
CREDITS = {}

# The channel's 2x2 thumbnail grid, in story order: the
# cell door, the prisoner, liberation, the turret kept.
THUMBNAIL = [
    {"img": "DOOR", "pan": (0.5, 0.5)},
    {"img": "POW", "pan": (0.5, 0.5)},
    {"img": "GATES", "pan": (0.5, 0.5)},
    {"img": "TURRET", "pan": (0.5, 0.5)},
]

_E = "ease-in-out"

SLIDES = [
    {"img": "GATES", **{"type": "cover", "zoom": [1.0, 1.06, 1.12], "pan": [[0.5, 0.5], [0.5, 0.5], [0.5, 0.5]]}, "title": "Changi Prison"},  # 0  title (6.62s) (s0)
    {"img": "TURRET", **{"type": "cover", "zoom": [1.12, 1.06, 1.0], "pan": [[0.35, 0.5], [0.35, 0.5], [0.35, 0.5]]}, "title": "The gate and wall today"},  # 1  the fragment on Upper Changi Road North; a monument behind wire (24.45s) (s1-2)
    {"img": "DOORIN", **{"type": "cover", "zoom": [1.0, 1.06, 1.12], "pan": [[0.5, 0.5], [0.5, 0.5], [0.5, 0.5]]}, "title": "The gaol's own story"},  # 2  the gaol's five lives, in turn; this is its own story (21.30s) (s3-4)
    {"img": "DOOR", **{"type": "cover", "zoom": [1.12, 1.06, 1.0], "pan": [[0.5, 0.5], [0.5, 0.5], [0.5, 0.5]]}, "title": "A new gaol for Changi, 1933"},  # 3  Pearl's Hill overcrowded; the 1933 approval; Woh Hup builds (25.40s) (s5-6)
    {"img": "DOOR", **{"type": "cover", "zoom": [1.0, 1.06, 1.12], "pan": [[0.5, 0.5], [0.5, 0.5], [0.5, 0.5]]}, "title": "The telephone-pole plan"},  # 4  the Public Works design; Ward; blocks off a central corridor (21.70s) (s7)
    {"img": "DOORIN", **{"type": "cover", "zoom": [1.12, 1.06, 1.0], "pan": [[0.5, 0.5], [0.5, 0.5], [0.5, 0.5]]}, "title": "Work rooms, hospital, punishment cells"},  # 5  around the cells: work rooms, hospital, the European block (16.18s) (s8)
    {"img": "DOOR", **{"type": "cover", "zoom": [1.0, 1.06, 1.12], "pan": [[0.5, 0.5], [0.5, 0.5], [0.5, 0.5]]}, "title": "Built for 600 men"},  # 6  600 long-sentence men; a light and a flushing latrine in every cell (18.50s) (s9)
    {"img": "DOORIN", **{"type": "cover", "zoom": [1.12, 1.06, 1.0], "pan": [[0.5, 0.5], [0.5, 0.5], [0.5, 0.5]]}, "title": "Gazetted 1936, opened 1937"},  # 7  the most modern in the East; first prisoners, 4 January 1937 (25.88s) (s10-11)
    {"img": "DOOR", **{"type": "cover", "zoom": [1.0, 1.06, 1.12], "pan": [[0.5, 0.5], [0.5, 0.5], [0.5, 0.5]]}, "title": "A cell door survives"},  # 8  the blue door at the National Museum; remember it as the numbers climb (23.48s) (s12-13)
    {"img": "GATES", **{"type": "cover", "zoom": [1.12, 1.06, 1.0], "pan": [[0.5, 0.5], [0.5, 0.5], [0.5, 0.5]]}, "title": "Changi the camp, Changi the gaol"},  # 9  the camp was the barracks; the gaol had a different war (25.00s) (s14-15)
    {"img": "HUT", **{"type": "cover", "zoom": [1.0, 1.06, 1.12], "pan": [[0.5, 0.4], [0.5, 0.4], [0.5, 0.4]]}, "title": "Singapore fell, February 1942"},  # 10  the gaol's different war begins; Singapore fell on 15 February (11.80s) (s16-17)
    {"img": "DOORIN", **{"type": "cover", "zoom": [1.12, 1.06, 1.0], "pan": [[0.5, 0.5], [0.5, 0.5], [0.5, 0.5]]}, "title": "The civilians marched in"},  # 11  17 February: the European civilians rounded up (8.45s) (s18)
    {"img": "DOOR", **{"type": "cover", "zoom": [1.0, 1.06, 1.12], "pan": [[0.5, 0.5], [0.5, 0.5], [0.5, 0.5]]}, "title": "2,620 people, a gaol for 600"},  # 12  the NLB breakdown: 2,200 men, 359 women, 61 children (20.65s) (s19)
    {"img": "DOOR", **{"type": "cover", "zoom": [1.12, 1.06, 1.0], "pan": [[0.5, 0.5], [0.5, 0.5], [0.5, 0.5]]}, "title": "The Governor among them"},  # 13  Sir Shenton Thomas, interned in his own colony's gaol (8.62s) (s20)
    {"img": "GATES", **{"type": "cover", "zoom": [1.0, 1.06, 1.12], "pan": [[0.65, 0.5], [0.65, 0.5], [0.65, 0.5]]}, "title": "The internees ran the camp"},  # 14  block leaders, schools, concerts and lectures (17.75s) (s21-22)
    {"img": "GATES", **{"type": "cover", "zoom": [1.12, 1.06, 1.0], "pan": [[0.5, 0.5], [0.5, 0.5], [0.5, 0.5]]}, "title": "Messages in the concert songs"},  # 15  families pass messages in code; the women publish POW WOW (26.00s) (s23-24)
    {"img": "DOORIN", **{"type": "cover", "zoom": [1.0, 1.06, 1.12], "pan": [[0.5, 0.5], [0.5, 0.5], [0.5, 0.5]]}, "title": "Dysentery, malaria, beri-beri"},  # 16  food adequate at first; disease and malnutrition follow (18.90s) (s25)
    {"img": "DOOR", **{"type": "cover", "zoom": [1.12, 1.06, 1.0], "pan": [[0.5, 0.5], [0.5, 0.5], [0.5, 0.5]]}, "title": "Three quilts, 66 squares each"},  # 17  the women make three signature quilts, 1942 (14.57s) (s26-27)
    {"img": "DOORIN", **{"type": "cover", "zoom": [1.0, 1.06, 1.12], "pan": [[0.5, 0.5], [0.5, 0.5], [0.5, 0.5]]}, "title": "Ethel Mulvany's idea"},  # 18  Mulvany's quilts; their real purpose: the men must know (23.57s) (s28-29)
    {"img": "DOOR", **{"type": "cover", "zoom": [1.12, 1.06, 1.0], "pan": [[0.5, 0.5], [0.5, 0.5], [0.5, 0.5]]}, "title": "Gifts for the wounded"},  # 19  something of herself in every square; the commandant's permission (16.52s) (s30-31)
    {"img": "DOORIN", **{"type": "cover", "zoom": [1.0, 1.06, 1.12], "pan": [[0.5, 0.5], [0.5, 0.5], [0.5, 0.5]]}, "title": "The word prison was unpicked"},  # 20  prison unpicked from the squares; gaol was allowed (9.40s) (s32)
    {"img": "DOOR", **{"type": "cover", "zoom": [1.12, 1.06, 1.0], "pan": [[0.5, 0.5], [0.5, 0.5], [0.5, 0.5]]}, "title": "A list of names in thread"},  # 21  the quilts today: Canberra and London; names in thread (26.12s) (s33-34)
    {"img": "DOORIN", **{"type": "cover", "zoom": [1.0, 1.06, 1.12], "pan": [[0.5, 0.5], [0.5, 0.5], [0.5, 0.5]]}, "title": "They travel in words"},  # 22  no photograph is freely licensed; they travel in words (7.20s) (s35)
    {"img": "POW", **{"type": "cover", "zoom": [1.12, 1.06, 1.0], "pan": [[0.5, 0.35], [0.5, 0.35], [0.5, 0.35]]}, "title": "Operation Jaywick"},  # 23  Jaywick sinks seven ships; the Kempeitai suspect the internees (22.65s) (s36-37)
    {"img": "POW", **{"type": "cover", "zoom": [1.0, 1.06, 1.12], "pan": [[0.5, 0.35], [0.5, 0.35], [0.5, 0.35]]}, "title": "The Double Tenth arrests"},  # 24  10 October 1943: 57 taken to the YMCA and the police stations (26.65s) (s38-39)
    {"img": "DOORIN", **{"type": "cover", "zoom": [1.12, 1.06, 1.0], "pan": [[0.5, 0.5], [0.5, 0.5], [0.5, 0.5]]}, "title": "Fifteen died under torture"},  # 25  fifteen died; John Long executed; Bishop Wilson; Elizabeth Choy (23.90s) (s40-42)
    {"img": "HUT", **{"type": "cover", "zoom": [1.0, 1.06, 1.12], "pan": [[0.5, 0.4], [0.5, 0.4], [0.5, 0.4]]}, "title": "Moved out to Sime Road, 1944"},  # 26  May 1944: the civilians leave for Sime Road Camp (9.28s) (s43)
    {"img": "POW", **{"type": "cover", "zoom": [1.12, 1.06, 1.0], "pan": [[0.5, 0.35], [0.5, 0.35], [0.5, 0.35]]}, "title": "A grimmer population"},  # 27  the POWs of the Changi area concentrated at the gaol (13.88s) (s44-45)
    {"img": "POW", **{"type": "cover", "zoom": [1.0, 1.06, 1.12], "pan": [[0.5, 0.35], [0.5, 0.35], [0.5, 0.35]]}, "title": "Five men to a cell"},  # 28  the AWM figures: 5,000 in the building, five to a cell (25.02s) (s46)
    {"img": "HUT", **{"type": "cover", "zoom": [1.12, 1.06, 1.0], "pan": [[0.5, 0.4], [0.5, 0.4], [0.5, 0.4]]}, "title": "The Playhouse Theatre"},  # 29  worse than the barracks; a theatre opens inside, September 1944 (23.10s) (s47-48)
    {"img": "POW", **{"type": "cover", "zoom": [1.0, 1.06, 1.12], "pan": [[0.5, 0.35], [0.5, 0.35], [0.5, 0.35]]}, "title": "Sparrows and rats"},  # 30  the last months: food so short men ate sparrows and rats (8.25s) (s49)
    {"img": "GATES", **{"type": "cover", "zoom": [1.12, 1.06, 1.0], "pan": [[0.35, 0.5], [0.35, 0.5], [0.35, 0.5]]}, "title": "Liberation, September 1945"},  # 31  released 6 September; the photograph at the head of the post (21.00s) (s50-51)
    {"img": "DOORIN", **{"type": "cover", "zoom": [1.0, 1.06, 1.12], "pan": [[0.5, 0.5], [0.5, 0.5], [0.5, 0.5]]}, "title": "The gaol changed sides"},  # 32  war-crimes suspects; most executions carried out at Changi (26.40s) (s52-53)
    {"img": "DOOR", **{"type": "cover", "zoom": [1.12, 1.06, 1.0], "pan": [[0.5, 0.5], [0.5, 0.5], [0.5, 0.5]]}, "title": "131 war-crimes trials"},  # 33  one count says 135 executed; 131 trials, 1946 to 1948 (18.48s) (s54-55)
    {"img": "DOORIN", **{"type": "cover", "zoom": [1.0, 1.06, 1.12], "pan": [[0.5, 0.5], [0.5, 0.5], [0.5, 0.5]]}, "title": "The Double Tenth trial"},  # 34  March to April 1946: 21 Kempeitai and interpreters accused (18.52s) (s56-57)
    {"img": "DOOR", **{"type": "cover", "zoom": [1.12, 1.06, 1.0], "pan": [[0.5, 0.5], [0.5, 0.5], [0.5, 0.5]]}, "title": "Eight sentenced to hang"},  # 35  fourteen guilty; Sumida among the eight condemned (20.20s) (s58)
    {"img": "DOORIN", **{"type": "cover", "zoom": [1.0, 1.06, 1.12], "pan": [[0.5, 0.5], [0.5, 0.5], [0.5, 0.5]]}, "title": "Handed back, October 1947"},  # 36  15 October 1947: back to the Prisons Department (13.60s) (s59)
    {"img": "BANNER", **{"type": "cover", "zoom": [1.12, 1.06, 1.0], "pan": [[0.35, 0.5], [0.35, 0.5], [0.35, 0.5]]}, "title": "Singapore's main prison"},  # 37  the peacetime half-century begins (10.57s) (s60)
    {"img": "BANNER", **{"type": "cover", "zoom": [1.0, 1.06, 1.12], "pan": [[0.65, 0.5], [0.65, 0.5], [0.65, 0.5]]}, "title": "The prison farm"},  # 38  the first prison farm: 30 acres, from July 1949 (22.40s) (s61)
    {"img": "BANNER", **{"type": "cover", "zoom": [1.12, 1.06, 1.0], "pan": [[0.5, 0.5], [0.5, 0.5], [0.5, 0.5]]}, "title": "Work, and eight cents a day"},  # 39  good-conduct men on the farm; the 1950 earning scheme (16.23s) (s62-63)
    {"img": "DOOR", **{"type": "cover", "zoom": [1.0, 1.06, 1.12], "pan": [[0.5, 0.5], [0.5, 0.5], [0.5, 0.5]]}, "title": "Corrective training, 1955"},  # 40  corrective training and preventive detention, 1955 (19.57s) (s64)
    {"img": "DOORIN", **{"type": "cover", "zoom": [1.12, 1.06, 1.0], "pan": [[0.5, 0.5], [0.5, 0.5], [0.5, 0.5]]}, "title": "597 cells; the upgrades"},  # 41  the 1948 count: 597 cells, 1,000 comfortably; the new blocks (23.38s) (s65-66)
    {"img": "DOOR", **{"type": "cover", "zoom": [1.0, 1.06, 1.12], "pan": [[0.5, 0.5], [0.5, 0.5], [0.5, 0.5]]}, "title": "The political prisoners"},  # 42  unionists and Cold Store detainees: Lim Chin Siong and the rest (26.52s) (s67-68)
    {"img": "DOORIN", **{"type": "cover", "zoom": [1.12, 1.06, 1.0], "pan": [[0.5, 0.5], [0.5, 0.5], [0.5, 0.5]]}, "title": "Released, 4 June 1959"},  # 43  Nair and others released to 2,000 supporters (18.43s) (s69)
    {"img": "DOOR", **{"type": "cover", "zoom": [1.0, 1.06, 1.12], "pan": [[0.5, 0.5], [0.5, 0.5], [0.5, 0.5]]}, "title": "The gaol's other function"},  # 44  hanging, then as now, at Changi (10.47s) (s70)
    {"img": "LINK", **{"type": "cover", "zoom": [1.12, 1.06, 1.0], "pan": [[0.5, 0.5], [0.5, 0.5], [0.5, 0.5]]}, "title": "One complex to replace them all"},  # 45  the late-1990s decision; ground broken 31 December 1999 (20.67s) (s71-72)
    {"img": "TURRET", **{"type": "cover", "zoom": [1.0, 1.06, 1.12], "pan": [[0.35, 0.5], [0.35, 0.5], [0.35, 0.5]]}, "title": "Demolition resisted"},  # 46  former POWs and Australian politicians resist (12.70s) (s73)
    {"img": "TURRET", **{"type": "cover", "zoom": [1.12, 1.06, 1.0], "pan": [[0.65, 0.5], [0.65, 0.5], [0.65, 0.5]]}, "title": "The fragment that was kept"},  # 47  the March 2004 compromise; everything else demolished (18.77s) (s74-75)
    {"img": "LINK", **{"type": "cover", "zoom": [1.0, 1.06, 1.12], "pan": [[0.5, 0.5], [0.5, 0.5], [0.5, 0.5]]}, "title": "The new complex, 11,000 places"},  # 48  Cluster A, 2004; Cluster B, 2010; 11,000 prisoners (19.85s) (s76-77)
    {"img": "TURRET", **{"type": "cover", "zoom": [1.12, 1.06, 1.0], "pan": [[0.35, 0.5], [0.35, 0.5], [0.35, 0.5]]}, "title": "Gazetted a monument, 2016"},  # 49  15 February 2016: the 72nd National Monument (17.15s) (s78)
    {"img": "TURRET", **{"type": "cover", "zoom": [1.0, 1.06, 1.12], "pan": [[0.65, 0.5], [0.65, 0.5], [0.65, 0.5]]}, "title": "An enduring symbol"},  # 50  Jean Wee, NHB: an enduring symbol of suffering (18.27s) (s79)
    {"img": "TURRET", **{"type": "cover", "zoom": [1.12, 1.06, 1.0], "pan": [[0.5, 0.5], [0.5, 0.5], [0.5, 0.5]]}, "title": "Closed to the public"},  # 51  inside a restricted area; read it from the road (12.62s) (s80)
    {"img": "GATES", **{"type": "cover", "zoom": [1.0, 1.06, 1.12], "pan": [[0.35, 0.5], [0.35, 0.5], [0.35, 0.5]]}, "title": "The threshold remains"},  # 52  the closing lines: the gate every prisoner passed through (22.38s) (s81-82)
]

SCHEDULE = [
    (0.000, 0), (6.625, 1), (31.075, 2),
    (52.375, 3), (77.775, 4), (99.475, 5),
    (115.650, 6), (134.150, 7), (160.025, 8),
    (183.500, 9), (208.500, 10), (220.300, 11),
    (228.750, 12), (249.400, 13), (258.025, 14),
    (275.775, 15), (301.775, 16), (320.675, 17),
    (335.250, 18), (358.825, 19), (375.350, 20),
    (384.750, 21), (410.875, 22), (418.075, 23),
    (440.725, 24), (467.375, 25), (491.275, 26),
    (500.550, 27), (514.425, 28), (539.450, 29),
    (562.550, 30), (570.800, 31), (591.800, 32),
    (618.200, 33), (636.675, 34), (655.200, 35),
    (675.400, 36), (689.000, 37), (699.575, 38),
    (721.975, 39), (738.200, 40), (757.775, 41),
    (781.150, 42), (807.675, 43), (826.100, 44),
    (836.575, 45), (857.250, 46), (869.950, 47),
    (888.725, 48), (908.575, 49), (925.725, 50),
    (944.000, 51), (956.625, 52)
]
TOTAL_DURATION = 979.000
TIMING_JSON = "audio/changi-prison-1936-to-2004-the-gaol-whose-wall-and-gate-were-kept.timing.json"

# The avatar presenter, cartoon with motion: corner bubble for the first and last 30 s.
AVATAR = {"ranges": [(0, 30), (-30, None)], "motion": True}
