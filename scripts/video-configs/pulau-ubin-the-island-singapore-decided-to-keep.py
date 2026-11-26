"""Video config for the Pulau Ubin post.

The pool is the post and gallery's twenty pictures: the
kampong house with its own solar panels (the hero), the
1945 military map, the flooded quarry, the elderly
islander, the German Girl Shrine outside and in and as
rebuilt in 2015, the bicycle shops, the Chek Jawa
boardwalk, shore and visitor centre, the bumboats, the
island panorama, two more kampong houses, the wayang
stage cycle hire, a village taxi, the jetty at night,
the 2025 crossing and a tame wild boar.

Named-place audit: Chek Jawa pictures sit only under
Chek Jawa sentences; the shrine pictures only under the
shrine passage; the solar-panel house carries the
micro-grid passage, the one place the post's own power
story has a picture. Named-person audit: the elderly
islander's portrait sits under the population figures,
which name nobody; the sentence naming Ahmad Kassim and
Ong Ang Kui carries a kampong house (Ahmad's wooden
house is named in it), never the portrait. The Outward
Bound passage has no photograph anywhere - it runs on
island views, and the night jetty carries the
thunderflash memory.

Every slide carries its discreet photo title (standing
rule, Chris, 2026-11-11): the short form of its image's
post/gallery caption, drawn small in the top corner on a
soft dark backing for the slide's whole run.

63 slides, 885.725s. No slide over 30s; the
longest is the parliamentary coda at 25.75s. Narration:
Kokoro with the OpenVoice clone. Pronunciation overrides
for the post's names filed 2026-11-25, NOT ear-verified
yet. AVATAR: first and last 30s, cartoon with motion.
"""

IMAGES = {
    "SOLARHOUSE": "https://upload.wikimedia.org/wikipedia/commons/6/60/Kampong_house%2C_Pulau_Ubin%2C_Singapore_-_20090801.jpg",
    "MAP1945": "https://upload.wikimedia.org/wikipedia/commons/d/dc/P_Ubin_1945_map.jpg",
    "QUARRY": "https://upload.wikimedia.org/wikipedia/commons/c/c6/Ubin_Quarry_01.jpg",
    "ELDER": "https://upload.wikimedia.org/wikipedia/commons/0/09/Elderly_Chinese_man%2C_Pulau_Ubin%2C_Singapore_-_20070225.jpg",
    "SHRINE": "https://upload.wikimedia.org/wikipedia/commons/e/e5/German_Girl_Shrine_%28526020601%29.jpg",
    "BIKESHOP": "https://upload.wikimedia.org/wikipedia/commons/4/43/Bicycle_rental_shop%2C_Pulau_Ubin%2C_Singapore_-_20071102-01.jpg",
    "CJPANO": "https://upload.wikimedia.org/wikipedia/commons/e/e8/Chek_Jawa%2C_panorama_6%2C_Aug_07.jpg",
    "BUMBOATS": "https://upload.wikimedia.org/wikipedia/commons/4/4d/SINGAPOREAN_BUMBOATS.jpg",
    "PANO": "https://upload.wikimedia.org/wikipedia/commons/2/22/Singapore_Pulau_Ubin_02.jpg",
    "KHOUSE": "https://upload.wikimedia.org/wikipedia/commons/4/45/Pulau_Ubin_kampong_house.jpg",
    "NHOUSE": "https://upload.wikimedia.org/wikipedia/commons/b/bb/House_near_the_northern_coast_of_Pulau_Ubin%2C_Singapore_-_20050803.jpg",
    "CYCLEHIRE": "https://upload.wikimedia.org/wikipedia/commons/c/ce/Pulau_Ubin_cycle_hire.jpg",
    "TAXI": "https://upload.wikimedia.org/wikipedia/commons/a/a1/Toyota_Crown_%28S110%29%2C_Pulau_Ubin%2C_Singapore_-_20071102.jpg",
    "SHRINEIN": "https://upload.wikimedia.org/wikipedia/commons/e/ea/Inside_German_Girl_Shrine_%28525927644%29.jpg",
    "BARBIE": "https://upload.wikimedia.org/wikipedia/commons/0/01/German_girl_shrine_a.k.a._Barbie_doll_shrine_-singapore_%2816664410223%29.jpg",
    "CJ2": "https://upload.wikimedia.org/wikipedia/commons/b/b8/Chek_Jawa_2%2C_Aug_07.JPG",
    "HOUSE1": "https://upload.wikimedia.org/wikipedia/commons/0/01/Chek_Jawa_Visitor_Centre%2C_Pulau_Ubin_%E2%80%93_Singapore_%283817430741%29.jpg",
    "NIGHTJETTY": "https://upload.wikimedia.org/wikipedia/commons/0/00/Leaving_Pulau_Ubin_jetty_on_a_bumboat_%2814043336260%29.jpg",
    "CROSS2025": "https://upload.wikimedia.org/wikipedia/commons/6/6a/SC3619D_Changi_Point_to_Pulau_Ubin_10-08-2025%281%29.jpg",
    "BOAR": "https://upload.wikimedia.org/wikipedia/commons/6/64/Pulau_Ubin_tame_wild_boar.jpg",
}

# Every image is captioned in the post or its gallery.
CREDITS = {}

# The channel's 2x2 thumbnail grid, in story order: the
# island in 1945, the stone it gave up, the shrine it
# kept, the house that powers itself.
THUMBNAIL = [
    {"img": "MAP1945", "pan": (0.5, 0.5)},
    {"img": "QUARRY", "pan": (0.5, 0.5)},
    {"img": "SHRINE", "pan": (0.5, 0.5)},
    {"img": "SOLARHOUSE", "pan": (0.5, 0.5)},
]

_E = "ease-in-out"

SLIDES = [
    {"img": "SOLARHOUSE", **{"type": "cover", "title": "Kampong house with solar panels, 2009", "zoom": [1.0, 1.06, 1.12], "pan": [(0.5, 0.5)] * 3, "ease": _E}},  # 0  title (4.25s) (s0)
    {"img": "BUMBOATS", **{"type": "cover", "title": "Bumboats at the jetty", "zoom": [1.12, 1.06, 1.0], "pan": [(0.35, 0.5)] * 3, "ease": _E}},  # 1  ten minutes by bumboat (5.58s) (s1)
    {"img": "PANO", **{"type": "cover", "title": "Pulau Ubin from the water", "zoom": [1.0, 1.06, 1.12], "pan": [(0.65, 0.5)] * 3, "ease": _E}},  # 2  another country: no traffic lights, a village of bicycle shops (17.65s) (s2)
    {"img": "KHOUSE", **{"type": "cover", "title": "A kampong house on Ubin", "zoom": [1.12, 1.06, 1.0], "pan": [(0.5, 0.4)] * 3, "ease": _E}},  # 3  every other island remade; Ubin alone was left; the story (17.62s) (s3-5)
    {"img": "MAP1945", **{"type": "cover", "title": "Pulau Ubin in 1945", "zoom": [1.0, 1.06, 1.12], "pan": [(0.5, 0.5)] * 3, "ease": _E}},  # 4  the name: Pulau Batu Jubin, jubin tiles, Chioh-sua (17.02s) (s6-7)
    {"img": "MAP1945", **{"type": "cover", "title": "Pulau Ubin in 1945", "zoom": [1.12, 1.06, 1.0], "pan": [(0.35, 0.5)] * 3, "ease": _E}},  # 5  once five islands, joined by bunds; 1,020 hectares (15.68s) (s8)
    {"img": "QUARRY", **{"type": "cover", "title": "A flooded granite quarry", "zoom": [1.0, 1.06, 1.12], "pan": [(0.65, 0.5)] * 3, "ease": _E}},  # 6  the stone was the point; the quarries fed Singapore (7.97s) (s9-10)
    {"img": "QUARRY", **{"type": "cover", "title": "A flooded granite quarry", "zoom": [1.12, 1.06, 1.0], "pan": [(0.5, 0.4)] * 3, "ease": _E}},  # 7  granite for Horsburgh, the Istana, the Causeway (18.52s) (s11)
    {"img": "MAP1945", **{"type": "cover", "title": "Pulau Ubin in 1945", "zoom": [1.0, 1.06, 1.12], "pan": [(0.5, 0.5)] * 3, "ease": _E}},  # 8  six quarries counted: Balai, Kekek, Ketam, Pekan, Petai, Ubin (10.80s) (s12)
    {"img": "QUARRY", **{"type": "cover", "title": "A flooded granite quarry", "zoom": [1.12, 1.06, 1.0], "pan": [(0.35, 0.5)] * 3, "ease": _E}},  # 9  Ketam, Aik Hwa from 1964; a hundred men; 30 to 40 percent of demand (22.35s) (s13-14)
    {"img": "QUARRY", **{"type": "cover", "title": "A flooded granite quarry", "zoom": [1.0, 1.06, 1.12], "pan": [(0.65, 0.5)] * 3, "ease": _E}},  # 10  Ketam closed May 1999; the pits became lakes (15.38s) (s15-16)
    {"img": "NHOUSE", **{"type": "cover", "title": "House on the northern coast, 2005", "zoom": [1.12, 1.06, 1.0], "pan": [(0.5, 0.4)] * 3, "ease": _E}},  # 11  people came for the stone; Orang Laut; the coffee estate of 1879 (20.05s) (s17-18)
    {"img": "KHOUSE", **{"type": "cover", "title": "A kampong house on Ubin", "zoom": [1.0, 1.06, 1.12], "pan": [(0.5, 0.5)] * 3, "ease": _E}},  # 12  the founding migration: Endut Senin from the Kallang River (12.78s) (s19)
    {"img": "NHOUSE", **{"type": "cover", "title": "House on the northern coast, 2005", "zoom": [1.12, 1.06, 1.0], "pan": [(0.35, 0.5)] * 3, "ease": _E}},  # 13  Chinese quarry workers followed; the kampongs filled (13.93s) (s20)
    {"img": "KHOUSE", **{"type": "cover", "title": "A kampong house on Ubin", "zoom": [1.0, 1.06, 1.12], "pan": [(0.65, 0.5)] * 3, "ease": _E}},  # 14  real institutions: Bin Kiang School, 1952; the clinic, 1957 (14.75s) (s21-22)
    {"img": "CYCLEHIRE", **{"type": "cover", "title": "Cycle hire and the wayang stage", "zoom": [1.12, 1.06, 1.0], "pan": [(0.5, 0.4)] * 3, "ease": _E}},  # 15  the Tua Pek Kong temple and its opera stage (10.43s) (s23)
    {"img": "NHOUSE", **{"type": "cover", "title": "House on the northern coast, 2005", "zoom": [1.0, 1.06, 1.12], "pan": [(0.5, 0.5)] * 3, "ease": _E}},  # 16  coffee, rubber, durian, prawns and fish (6.45s) (s24)
    {"img": "NHOUSE", **{"type": "cover", "title": "House on the northern coast, 2005", "zoom": [1.12, 1.06, 1.0], "pan": [(0.35, 0.5)] * 3, "ease": _E}},  # 17  the century turned; resettlement emptied the island (10.05s) (s25-26)
    {"img": "ELDER", **{"type": "cover", "title": "An elderly islander, 2007", "zoom": [1.0, 1.06, 1.12], "pan": [(0.65, 0.5)] * 3, "ease": _E}},  # 18  the figures are stark: 2,028 in 1970, 38 by 2012 (16.23s) (s27)
    {"img": "KHOUSE", **{"type": "cover", "title": "A kampong house on Ubin", "zoom": [1.12, 1.06, 1.0], "pan": [(0.5, 0.4)] * 3, "ease": _E}},  # 19  Bin Kiang closed in 1985, demolished in 2000 (6.05s) (s28)
    {"img": "KHOUSE", **{"type": "cover", "title": "A kampong house on Ubin", "zoom": [1.0, 1.06, 1.12], "pan": [(0.5, 0.5)] * 3, "ease": _E}},  # 20  known by name: Ahmad Kassim's house; the Ah Ma Drink Stall (19.00s) (s29)
    {"img": "SHRINE", **{"type": "cover", "title": "The German Girl Shrine, 2007", "zoom": [1.12, 1.06, 1.0], "pan": [(0.35, 0.5)] * 3, "ease": _E}},  # 21  on a hill path stands a small shrine (10.70s) (s30)
    {"img": "SHRINEIN", **{"type": "cover", "title": "Inside the German Girl Shrine, 2007", "zoom": [1.0, 1.06, 1.12], "pan": [(0.65, 0.5)] * 3, "ease": _E}},  # 22  the legend: 1914, the soldiers, the daughter who fled (19.88s) (s31-32)
    {"img": "SHRINE", **{"type": "cover", "title": "The German Girl Shrine, 2007", "zoom": [1.12, 1.06, 1.0], "pan": [(0.5, 0.4)] * 3, "ease": _E}},  # 23  her body found, buried on the hill; gamblers came (12.95s) (s33)
    {"img": "BARBIE", **{"type": "cover", "title": "The shrine rebuilt, 2015", "zoom": [1.0, 1.06, 1.12], "pan": [(0.5, 0.5)] * 3, "ease": _E}},  # 24  a wonderful story; on the evidence, not true (8.43s) (s34-35)
    {"img": "SHRINEIN", **{"type": "cover", "title": "Inside the German Girl Shrine, 2007", "zoom": [1.12, 1.06, 1.0], "pan": [(0.35, 0.5)] * 3, "ease": _E}},  # 25  Gibson in the archives, 2021; Brandt had sold in 1907 (18.95s) (s36-37)
    {"img": "SHRINE", **{"type": "cover", "title": "The German Girl Shrine, 2007", "zoom": [1.0, 1.06, 1.12], "pan": [(0.65, 0.5)] * 3, "ease": _E}},  # 26  no German family in 1914; no internment raid (17.00s) (s38-39)
    {"img": "SHRINEIN", **{"type": "cover", "title": "Inside the German Girl Shrine, 2007", "zoom": [1.12, 1.06, 1.0], "pan": [(0.5, 0.4)] * 3, "ease": _E}},  # 27  one informant, born in 1928, who had it second-hand (13.25s) (s40)
    {"img": "QUARRY", **{"type": "cover", "title": "A flooded granite quarry", "zoom": [1.0, 1.06, 1.12], "pan": [(0.5, 0.5)] * 3, "ease": _E}},  # 28  the shrine is genuine and older: a datuk keramat; the hill is now the Ketam pond (22.45s) (s41-42)
    {"img": "SHRINE", **{"type": "cover", "title": "The German Girl Shrine, 2007", "zoom": [1.12, 1.06, 1.0], "pan": [(0.35, 0.5)] * 3, "ease": _E}},  # 29  Aik Hwa moved the shrine and built the yellow hut (9.95s) (s43)
    {"img": "BARBIE", **{"type": "cover", "title": "The shrine rebuilt, 2015", "zoom": [1.0, 1.06, 1.12], "pan": [(0.65, 0.5)] * 3, "ease": _E}},  # 30  rebuilt in 2015; Berlin Heiligtum, dated 1896 by mistake (16.98s) (s44)
    {"img": "SHRINEIN", **{"type": "cover", "title": "Inside the German Girl Shrine, 2007", "zoom": [1.12, 1.06, 1.0], "pan": [(0.5, 0.4)] * 3, "ease": _E}},  # 31  Barbie dolls among the offerings; the island kept the story (13.27s) (s45-46)
    {"img": "MAP1945", **{"type": "cover", "title": "Pulau Ubin in 1945", "zoom": [1.0, 1.06, 1.12], "pan": [(0.5, 0.5)] * 3, "ease": _E}},  # 32  the war, brief and strange: occupied 7 February 1942 (16.73s) (s47-48)
    {"img": "MAP1945", **{"type": "cover", "title": "Pulau Ubin in 1945", "zoom": [1.12, 1.06, 1.0], "pan": [(0.35, 0.5)] * 3, "ease": _E}},  # 33  a diversion; the real invasion crossed in the west (9.38s) (s49-50)
    {"img": "PANO", **{"type": "cover", "title": "Pulau Ubin from the water", "zoom": [1.0, 1.06, 1.12], "pan": [(0.65, 0.5)] * 3, "ease": _E}},  # 34  twenty-five years later: Outward Bound founded, 1967 (16.52s) (s51-52)
    {"img": "NHOUSE", **{"type": "cover", "title": "House on the northern coast, 2005", "zoom": [1.12, 1.06, 1.0], "pan": [(0.5, 0.4)] * 3, "ease": _E}},  # 35  the British camp, the first intakes, a fifteen-year-old Lee Hsien Loong (25.27s) (s53)
    {"img": "KHOUSE", **{"type": "cover", "title": "A kampong house on Ubin", "zoom": [1.0, 1.06, 1.12], "pan": [(0.5, 0.5)] * 3, "ease": _E}},  # 36  MINDEF ran it 1970 to 1991; the new campus, 1997 (22.07s) (s54)
    {"img": "PANO", **{"type": "cover", "title": "Pulau Ubin from the water", "zoom": [1.12, 1.06, 1.0], "pan": [(0.35, 0.5)] * 3, "ease": _E}},  # 37  today every Secondary 3 student goes through Outward Bound (13.03s) (s55)
    {"img": "NHOUSE", **{"type": "cover", "title": "House on the northern coast, 2005", "zoom": [1.0, 1.06, 1.12], "pan": [(0.65, 0.5)] * 3, "ease": _E}},  # 38  seen at first hand: a friend from Holy Innocents Lane (17.20s) (s56-57)
    {"img": "BOAR", **{"type": "cover", "title": "A tame wild boar", "zoom": [1.12, 1.06, 1.0], "pan": [(0.5, 0.4)] * 3, "ease": _E}},  # 39  an adventurer's life: the camp, the boats, the jungle (7.40s) (s58)
    {"img": "NIGHTJETTY", **{"type": "cover", "title": "The Ubin jetty at night, 2014", "zoom": [1.0, 1.06, 1.12], "pan": [(0.5, 0.5)] * 3, "ease": _E}},  # 40  the bunk at night: thunderflashes around the trainees (13.90s) (s59)
    {"img": "PANO", **{"type": "cover", "title": "Pulau Ubin from the water", "zoom": [1.12, 1.06, 1.0], "pan": [(0.35, 0.5)] * 3, "ease": _E}},  # 41  the solo night, a rite of passing (8.12s) (s60)
    {"img": "PANO", **{"type": "cover", "title": "Pulau Ubin from the water", "zoom": [1.0, 1.06, 1.12], "pan": [(0.65, 0.5)] * 3, "ease": _E}},  # 42  thousands passed through; not a day trip; where they were toughened (11.00s) (s61-63)
    {"img": "CJPANO", **{"type": "cover", "title": "Chek Jawa boardwalk, 2007", "zoom": [1.12, 1.06, 1.0], "pan": [(0.5, 0.4)] * 3, "ease": _E}},  # 43  Chek Jawa: six habitats at the eastern tip (12.25s) (s64)
    {"img": "CJ2", **{"type": "cover", "title": "The Chek Jawa shore, 2007", "zoom": [1.0, 1.06, 1.12], "pan": [(0.5, 0.5)] * 3, "ease": _E}},  # 44  slated for reclamation, saved at the end of 2001 (13.40s) (s65)
    {"img": "HOUSE1", **{"type": "cover", "title": "Chek Jawa Visitor Centre, 2009", "zoom": [1.12, 1.06, 1.0], "pan": [(0.35, 0.5)] * 3, "ease": _E}},  # 45  its own post on this blog; the boardwalk and House No. 1 (16.95s) (s66)
    {"img": "SOLARHOUSE", **{"type": "cover", "title": "Kampong house with solar panels, 2009", "zoom": [1.0, 1.06, 1.12], "pan": [(0.65, 0.5)] * 3, "ease": _E}},  # 46  never connected to the national grid; wells and diesel (18.05s) (s67-68)
    {"img": "SOLARHOUSE", **{"type": "cover", "title": "Kampong house with solar panels, 2009", "zoom": [1.12, 1.06, 1.0], "pan": [(0.5, 0.4)] * 3, "ease": _E}},  # 47  sixty consumers; a mainland cable is not cost-effective (14.38s) (s69)
    {"img": "NHOUSE", **{"type": "cover", "title": "House on the northern coast, 2005", "zoom": [1.0, 1.06, 1.12], "pan": [(0.5, 0.5)] * 3, "ease": _E}},  # 48  an experiment instead: the micro-grid inaugurated, 2013 (17.70s) (s70-71)
    {"img": "TAXI", **{"type": "cover", "title": "One of Ubin's taxis, 2007", "zoom": [1.12, 1.06, 1.0], "pan": [(0.35, 0.5)] * 3, "ease": _E}},  # 49  thirty homes and businesses near the jetty, on the new grid (17.38s) (s72)
    {"img": "BIKESHOP", **{"type": "cover", "title": "Bicycle rental shop, 2007", "zoom": [1.0, 1.06, 1.12], "pan": [(0.65, 0.5)] * 3, "ease": _E}},  # 50  chillers and air-conditioners changed what the shops could sell (6.28s) (s73)
    {"img": "SOLARHOUSE", **{"type": "cover", "title": "Kampong house with solar panels, 2009", "zoom": [1.12, 1.06, 1.0], "pan": [(0.5, 0.4)] * 3, "ease": _E}},  # 51  the 2023 upgrade: solar panels and a flow battery (10.90s) (s74)
    {"img": "NHOUSE", **{"type": "cover", "title": "House on the northern coast, 2005", "zoom": [1.0, 1.06, 1.12], "pan": [(0.5, 0.5)] * 3, "ease": _E}},  # 52  the honest coda: 2025 ran 10 percent solar, thirteen trips (25.75s) (s75-76)
    {"img": "KHOUSE", **{"type": "cover", "title": "A kampong house on Ubin", "zoom": [1.12, 1.06, 1.0], "pan": [(0.35, 0.5)] * 3, "ease": _E}},  # 53  a better battery due in 2026; the tariff fixed to 2034 (7.58s) (s77)
    {"img": "PANO", **{"type": "cover", "title": "Pulau Ubin from the water", "zoom": [1.0, 1.06, 1.12], "pan": [(0.65, 0.5)] * 3, "ease": _E}},  # 54  the experiment continues, at village scale (15.18s) (s78-79)
    {"img": "PANO", **{"type": "cover", "title": "Pulau Ubin from the water", "zoom": [1.12, 1.06, 1.0], "pan": [(0.5, 0.4)] * 3, "ease": _E}},  # 55  NParks the single agency since 2016 (9.40s) (s80)
    {"img": "KHOUSE", **{"type": "cover", "title": "A kampong house on Ubin", "zoom": [1.0, 1.06, 1.12], "pan": [(0.5, 0.5)] * 3, "ease": _E}},  # 56  the Ubin Project's promise; the next phase to 2034 (24.73s) (s81-82)
    {"img": "CROSS2025", **{"type": "cover", "title": "The Changi Point crossing, 2025", "zoom": [1.12, 1.06, 1.0], "pan": [(0.35, 0.5)] * 3, "ease": _E}},  # 57  300,000 visitors a year make the crossing (5.10s) (s83)
    {"img": "BUMBOATS", **{"type": "cover", "title": "Bumboats at the jetty", "zoom": [1.0, 1.06, 1.12], "pan": [(0.65, 0.5)] * 3, "ease": _E}},  # 58  the bumboats: four dollars, ten minutes, a dozen passengers (10.10s) (s84)
    {"img": "BIKESHOP", **{"type": "cover", "title": "Bicycle rental shop, 2007", "zoom": [1.12, 1.06, 1.0], "pan": [(0.5, 0.4)] * 3, "ease": _E}},  # 59  bicycle shops by the jetty; the Ketam Mountain Bike Park (15.22s) (s85)
    {"img": "PANO", **{"type": "cover", "title": "Pulau Ubin from the water", "zoom": [1.0, 1.06, 1.12], "pan": [(0.5, 0.5)] * 3, "ease": _E}},  # 60  where it fits: every other island was remade (8.43s) (s86)
    {"img": "MAP1945", **{"type": "cover", "title": "Pulau Ubin in 1945", "zoom": [1.12, 1.06, 1.0], "pan": [(0.35, 0.5)] * 3, "ease": _E}},  # 61  the remaking stopped; one island kept as a reminder (16.02s) (s87)
    {"img": "SOLARHOUSE", **{"type": "cover", "title": "Kampong house with solar panels, 2009", "zoom": [1.0, 1.06, 1.12], "pan": [(0.65, 0.5)] * 3, "ease": _E}},  # 62  the last villagers, the schoolboys, the grid: its own beginning (14.00s) (s88)
]

SCHEDULE = [
    (0.000, 0), (4.250, 1), (9.825, 2),
    (27.475, 3), (45.100, 4), (62.125, 5),
    (77.800, 6), (85.775, 7), (104.300, 8),
    (115.100, 9), (137.450, 10), (152.825, 11),
    (172.875, 12), (185.650, 13), (199.575, 14),
    (214.325, 15), (224.750, 16), (231.200, 17),
    (241.250, 18), (257.475, 19), (263.525, 20),
    (282.525, 21), (293.225, 22), (313.100, 23),
    (326.050, 24), (334.475, 25), (353.425, 26),
    (370.425, 27), (383.675, 28), (406.125, 29),
    (416.075, 30), (433.050, 31), (446.325, 32),
    (463.050, 33), (472.425, 34), (488.950, 35),
    (514.225, 36), (536.300, 37), (549.325, 38),
    (566.525, 39), (573.925, 40), (587.825, 41),
    (595.950, 42), (606.950, 43), (619.200, 44),
    (632.600, 45), (649.550, 46), (667.600, 47),
    (681.975, 48), (699.675, 49), (717.050, 50),
    (723.325, 51), (734.225, 52), (759.975, 53),
    (767.550, 54), (782.725, 55), (792.125, 56),
    (816.850, 57), (821.950, 58), (832.050, 59),
    (847.275, 60), (855.700, 61), (871.725, 62),
]
TOTAL_DURATION = 885.725
TIMING_JSON = "audio/pulau-ubin-the-island-singapore-decided-to-keep.timing.json"

# The avatar presenter, cartoon with motion: corner bubble for the first and last 30 s.
AVATAR = {"ranges": [(0, 30), (-30, None)], "motion": True}
