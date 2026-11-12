"""Video config for the Pulau Semakau post.

The pool is nine pictures: Sengkang's two Semakau panoramas and two
further island views from November 2006, the receiving station, and
four wildlife photographs (giant clam, knobbly sea star, seagrass,
great-billed heron). The gallery's location map is an SVG and cannot
be rendered by the video library, so it stays on the page. Nine
pictures for twenty-four minutes is a thin pool, so images recur at
new story beats with varied pans and alternating zoom direction;
the four wildlife pictures are held for the sentences that name
their subjects.

Named-person rule: the pool holds no portrait of Minah, Rani, Sidek
Saniff, the Teo brothers, Mak Imah, Saniah, Mah Bow Tan, Kanwaljit
Soin, Chu Jian or Firdaus Sani, so every sentence naming a person
shows the island, its shore or its works — never another person.

88 slides, 1457.05s. Narration: Kokoro with the OpenVoice clone.
AVATAR: first and last 30s, cartoon with motion.
"""

IMAGES = {
    "PANO": "https://upload.wikimedia.org/wikipedia/commons/4/40/Pulau_Semakau%2C_panorama%2C_Nov_06.jpg",
    "STATION": "https://upload.wikimedia.org/wikipedia/commons/4/4a/Semakaustation.jpg",
    "PS10": "https://upload.wikimedia.org/wikipedia/commons/8/82/Pulau_Semakau_10%2C_Nov_06.JPG",
    "CLAM": "https://upload.wikimedia.org/wikipedia/commons/c/cf/Tridacna_squamosa_%28Giant_clam%29_brown_and_blue.jpg",
    "PANO3": "https://upload.wikimedia.org/wikipedia/commons/c/c6/Pulau_Semakau%2C_panorama_3%2C_Nov_06.jpg",
    "PS32": "https://upload.wikimedia.org/wikipedia/commons/c/c9/Pulau_Semakau_32%2C_Nov_06.JPG",
    "STAR": "https://upload.wikimedia.org/wikipedia/commons/d/d6/Knobbly_sea_star_%28Protoreaster_nodosus%29.jpg",
    "SEAGRASS": "https://upload.wikimedia.org/wikipedia/commons/b/be/Enhalus_acoroides_%2830774220094%29.jpg",
    "HERON": "https://upload.wikimedia.org/wikipedia/commons/4/44/Great-billed_heron_%28Ardea_sumatrana_sumatrana%29_Danum_Valley.jpg"
}

# Every image is captioned in the post or its gallery.
CREDITS = {}

# The channel's 2x2 thumbnail grid, in story order: the village
# shore, the receiving station that replaced the village island,
# the reef life that survived, and the island panorama today.
THUMBNAIL = [
    {"img": "PANO3", "pan": (0.5, 0.5)},
    {"img": "STATION", "pan": (0.5, 0.5)},
    {"img": "CLAM", "pan": (0.5, 0.5)},
    {"img": "PANO", "pan": (0.5, 0.5)},
]

_E = "ease-in-out"

SLIDES = [
    {"img": "PANO", **{"type": "cover", "zoom": [1.0, 1.06, 1.12], "pan": [(0.5, 0.5)] * 3, "ease": _E}},  # 0  title: the island panorama (5.0s)
    {"img": "PANO3", **{"type": "cover", "zoom": [1.12, 1.06, 1.0], "pan": [(0.5, 0.5)] * 3, "ease": _E}},  # 1  s1-2 Minah and Rani resettled to Telok Blangah; rarely slept in the flat (15.5s)
    {"img": "PS10", **{"type": "cover", "zoom": [1.0, 1.06, 1.12], "pan": [(0.5, 0.5)] * 3, "ease": _E}},  # 2  s3 back across the water to the beach hut (17.0s)
    {"img": "PANO", **{"type": "cover", "zoom": [1.12, 1.06, 1.0], "pan": [(0.35, 0.5)] * 3, "ease": _E}},  # 3  s4-5 Minah at ninety; 'Our hearts are attached to the island' (9.8s)
    {"img": "PS32", **{"type": "cover", "zoom": [1.0, 1.06, 1.12], "pan": [(0.5, 0.5)] * 3, "ease": _E}},  # 4  s6 the island she could not leave is now the landfill (12.4s)
    {"img": "PANO3", **{"type": "cover", "zoom": [1.12, 1.06, 1.0], "pan": [(0.35, 0.5)] * 3, "ease": _E}},  # 5  s7 the story preview: two villages, a living island, building with ash (16.1s)
    {"img": "PS10", **{"type": "cover", "zoom": [1.0, 1.06, 1.12], "pan": [(0.5, 0.5)] * 3, "ease": _E}},  # 6  s8-9 eight kilometres south; Mangrove Island, 1844 (22.4s)
    {"img": "PANO", **{"type": "cover", "zoom": [1.12, 1.06, 1.0], "pan": [(0.65, 0.5)] * 3, "ease": _E}},  # 7  s10 Kampong Tengah grows up on the western side (14.9s)
    {"img": "PS32", **{"type": "cover", "zoom": [1.0, 1.06, 1.12], "pan": [(0.5, 0.5)] * 3, "ease": _E}},  # 8  s11-12 780 people, fishing from kolek boats; catch to the mainland (17.8s)
    {"img": "PANO3", **{"type": "cover", "zoom": [1.12, 1.06, 1.0], "pan": [(0.65, 0.5)] * 3, "ease": _E}},  # 9  s13-15 a hard, self-contained world; water ferried; evening generator (14.5s)
    {"img": "PS10", **{"type": "cover", "zoom": [1.0, 1.06, 1.12], "pan": [(0.5, 0.5)] * 3, "ease": _E}},  # 10  s16-17 latrines over the water; the Floating Dispensary nurse (14.5s)
    {"img": "PANO", **{"type": "cover", "zoom": [1.12, 1.06, 1.0], "pan": [(0.5, 0.4)] * 3, "ease": _E}},  # 11  s18 mosque, school, football field: the village complete (12.1s)
    {"img": "PS32", **{"type": "cover", "zoom": [1.0, 1.06, 1.12], "pan": [(0.5, 0.5)] * 3, "ease": _E}},  # 12  s19 Sidek Saniff, the young teacher (names him: no portrait in pool) (14.9s)
    {"img": "PANO3", **{"type": "cover", "zoom": [1.12, 1.06, 1.0], "pan": [(0.5, 0.4)] * 3, "ease": _E}},  # 13  s20-21 Bukom families taken in; islanders shuffled island to island (17.3s)
    {"img": "PS10", **{"type": "cover", "zoom": [1.0, 1.06, 1.12], "pan": [(0.5, 0.5)] * 3, "ease": _E}},  # 14  s22-23 ten minutes by sampan; Pulau Seking, houses on pillars (16.5s)
    {"img": "PANO", **{"type": "cover", "zoom": [1.12, 1.06, 1.0], "pan": [(0.5, 0.5)] * 3, "ease": _E}},  # 15  s24 Orang Selat, people of the Straits (12.4s)
    {"img": "PS32", **{"type": "cover", "zoom": [1.0, 1.06, 1.12], "pan": [(0.5, 0.5)] * 3, "ease": _E}},  # 16  s25 before colonial times; 'the final link to pre-Raffles Singapore' (20.6s)
    {"img": "PANO3", **{"type": "cover", "zoom": [1.12, 1.06, 1.0], "pan": [(0.5, 0.5)] * 3, "ease": _E}},  # 17  s26-27 census counts; fishing, boat-building, Bukom refinery work (19.4s)
    {"img": "PS10", **{"type": "cover", "zoom": [1.0, 1.06, 1.12], "pan": [(0.5, 0.5)] * 3, "ease": _E}},  # 18  s28 the Teo brothers' provision shop (names them: the island, no portrait) (11.2s)
    {"img": "PANO", **{"type": "cover", "zoom": [1.12, 1.06, 1.0], "pan": [(0.35, 0.5)] * 3, "ease": _E}},  # 19  s29 Keng of Riau, the island's chieftain and her shrine (16.5s)
    {"img": "PS32", **{"type": "cover", "zoom": [1.0, 1.06, 1.12], "pan": [(0.5, 0.5)] * 3, "ease": _E}},  # 20  s30 the year-end carnival with the Riau islanders (19.6s)
    {"img": "PANO3", **{"type": "cover", "zoom": [1.12, 1.06, 1.0], "pan": [(0.35, 0.5)] * 3, "ease": _E}},  # 21  s31-32 the villages did not end together; Kampong Tengah relocated 1977 (17.0s)
    {"img": "PS10", **{"type": "cover", "zoom": [1.0, 1.06, 1.12], "pan": [(0.5, 0.5)] * 3, "ease": _E}},  # 22  s33-34 some went quietly; Mak Imah rebuilt her house in Riau (names her: place) (14.9s)
    {"img": "PANO", **{"type": "cover", "zoom": [1.12, 1.06, 1.0], "pan": [(0.65, 0.5)] * 3, "ease": _E}},  # 23  s35-36 Minah and Rani declined the flat; the island left to nature (15.1s)
    {"img": "PS32", **{"type": "cover", "zoom": [1.0, 1.06, 1.12], "pan": [(0.5, 0.5)] * 3, "ease": _E}},  # 24  s37-38 Seking's longer goodbye; development announced 1975 (16.1s)
    {"img": "PANO3", **{"type": "cover", "zoom": [1.12, 1.06, 1.0], "pan": [(0.65, 0.5)] * 3, "ease": _E}},  # 25  s39 1983: Jurong Town Corporation to take over (17.9s)
    {"img": "PS10", **{"type": "cover", "zoom": [1.0, 1.06, 1.12], "pan": [(0.5, 0.5)] * 3, "ease": _E}},  # 26  s40-41 down to 139 people; Mah Bow Tan tells Parliament (names him: place) (17.9s)
    {"img": "PANO", **{"type": "cover", "zoom": [1.12, 1.06, 1.0], "pan": [(0.5, 0.4)] * 3, "ease": _E}},  # 27  s42-43 Kanwaljit Soin's appeal refused; the S$130 million alternative (names her: place) (18.2s)
    {"img": "PS32", **{"type": "cover", "zoom": [1.0, 1.06, 1.12], "pan": [(0.5, 0.5)] * 3, "ease": _E}},  # 28  s44-45 'Raya terakhir di Pulau Seking'; the last residents leave, 1994 (21.1s)
    {"img": "PANO3", **{"type": "cover", "zoom": [1.12, 1.06, 1.0], "pan": [(0.5, 0.4)] * 3, "ease": _E}},  # 29  s46 Saniah, the last penghulu's widow: 'like being caged' (names her: shore) (15.8s)
    {"img": "PS10", **{"type": "cover", "zoom": [1.0, 1.06, 1.12], "pan": [(0.5, 0.5)] * 3, "ease": _E}},  # 30  s47-49 why the sea at all: the mainland filled up; Lorong Halus (22.0s)
    {"img": "PS32", **{"type": "cover", "zoom": [1.12, 1.06, 1.0], "pan": [(0.5, 0.5)] * 3, "ease": _E}},  # 31  s50-52 Lim Chu Kang closes; Lorong Halus full; Semakau opens next morning (16.6s)
    {"img": "STATION", **{"type": "cover", "zoom": [1.0, 1.06, 1.12], "pan": [(0.5, 0.5)] * 3, "ease": _E}},  # 32  s53 building it, 1995-99, S$610 million (11.4s)
    {"img": "PS10", **{"type": "cover", "zoom": [1.12, 1.06, 1.0], "pan": [(0.5, 0.5)] * 3, "ease": _E}},  # 33  s54 the seven-kilometre bund; 350 hectares enclosed (15.4s)
    {"img": "PS32", **{"type": "cover", "zoom": [1.0, 1.06, 1.12], "pan": [(0.5, 0.5)] * 3, "ease": _E}},  # 34  s55-56 membrane and marine clay; the sea divided into cells (17.1s)
    {"img": "STATION", **{"type": "cover", "zoom": [1.12, 1.06, 1.0], "pan": [(0.5, 0.5)] * 3, "ease": _E}},  # 35  s57-59 the receiving station built on Pulau Seking itself; the front door (20.9s)
    {"img": "PS10", **{"type": "cover", "zoom": [1.0, 1.06, 1.12], "pan": [(0.5, 0.5)] * 3, "ease": _E}},  # 36  s60-62 almost nothing arrives as rubbish; burning cuts ninety per cent (19.6s)
    {"img": "STATION", **{"type": "cover", "zoom": [1.12, 1.06, 1.0], "pan": [(0.5, 0.5)] * 3, "ease": _E}},  # 37  s63 Tuas transfer station; the night barges' 33-kilometre journey (19.2s)
    {"img": "PS32", **{"type": "cover", "zoom": [1.0, 1.06, 1.12], "pan": [(0.5, 0.5)] * 3, "ease": _E}},  # 38  s64 excavators, 35-tonne trucks, the bund-top road (19.7s)
    {"img": "PS10", **{"type": "cover", "zoom": [1.12, 1.06, 1.0], "pan": [(0.5, 0.5)] * 3, "ease": _E}},  # 39  s65 2,100 tonnes a day on the 2019 figures (17.5s)
    {"img": "STATION", **{"type": "cover", "zoom": [1.0, 1.06, 1.12], "pan": [(0.5, 0.5)] * 3, "ease": _E}},  # 40  s66 REMEX at Tuas pulls the metal out first (15.2s)
    {"img": "PANO3", **{"type": "cover", "zoom": [1.12, 1.06, 1.0], "pan": [(0.5, 0.5)] * 3, "ease": _E}},  # 41  s67-68 a filled cell is covered with earth and turns green (15.5s)
    {"img": "PANO", **{"type": "cover", "zoom": [1.0, 1.06, 1.12], "pan": [(0.5, 0.5)] * 3, "ease": _E}},  # 42  s69 'Garbage of Eden': built against a living shore (11.9s)
    {"img": "PANO3", **{"type": "cover", "zoom": [1.12, 1.06, 1.0], "pan": [(0.35, 0.5)] * 3, "ease": _E}},  # 43  s70 east anchored to the landfill; the western shore left natural (10.4s)
    {"img": "PS32", **{"type": "cover", "zoom": [1.0, 1.06, 1.12], "pan": [(0.5, 0.5)] * 3, "ease": _E}},  # 44  s71-72 13.6 hectares of mangrove replanted outside the bund (22.0s)
    {"img": "PANO3", **{"type": "cover", "zoom": [1.12, 1.06, 1.0], "pan": [(0.65, 0.5)] * 3, "ease": _E}},  # 45  s73-74 healthy mangroves: the liners are not leaking; 'the first alarm is a forest' (12.1s)
    {"img": "SEAGRASS", **{"type": "cover", "zoom": [1.0, 1.06, 1.12], "pan": [(0.5, 0.5)] * 3, "ease": _E}},  # 46  s75-76 the low-tide roll-call; the tape seagrass bed (its own picture) (22.5s)
    {"img": "STAR", **{"type": "cover", "zoom": [1.12, 1.06, 1.0], "pan": [(0.5, 0.5)] * 3, "ease": _E}},  # 47  s77 knobbly sea stars on the flats (their own picture) (6.6s)
    {"img": "CLAM", **{"type": "cover", "zoom": [1.0, 1.06, 1.12], "pan": [(0.5, 0.5)] * 3, "ease": _E}},  # 48  s78 giant clams on the reef (their own picture) (11.7s)
    {"img": "PANO3", **{"type": "cover", "zoom": [1.12, 1.06, 1.0], "pan": [(0.5, 0.4)] * 3, "ease": _E}},  # 49  s79 the 2005 survey's endangered plants (9.2s)
    {"img": "HERON", **{"type": "cover", "zoom": [1.0, 1.06, 1.12], "pan": [(0.5, 0.5)] * 3, "ease": _E}},  # 50  s80 the great-billed heron, Jimmy (its own picture) (9.9s)
    {"img": "SEAGRASS", **{"type": "cover", "zoom": [1.12, 1.06, 1.0], "pan": [(0.5, 0.5)] * 3, "ease": _E}},  # 51  s81 TeamSeagrass and the 2007 coral nursery (20.6s)
    {"img": "PANO3", **{"type": "cover", "zoom": [1.0, 1.06, 1.12], "pan": [(0.5, 0.5)] * 3, "ease": _E}},  # 52  s82-83 2014: the southern lagoon had quietly become a reef (17.7s)
    {"img": "CLAM", **{"type": "cover", "zoom": [1.12, 1.06, 1.0], "pan": [(0.5, 0.5)] * 3, "ease": _E}},  # 53  s84-85 the lagoon emptied; 700 coral colonies transplanted (18.6s)
    {"img": "STAR", **{"type": "cover", "zoom": [1.0, 1.06, 1.12], "pan": [(0.5, 0.5)] * 3, "ease": _E}},  # 54  s86 rarities: the fluted giant clam and the Neptune's Cup sponge (17.8s)
    {"img": "PANO", **{"type": "cover", "zoom": [1.12, 1.06, 1.0], "pan": [(0.35, 0.5)] * 3, "ease": _E}},  # 55  s87-88 450 fish caught and released; 'rescue a reef from its own lagoon' (13.6s)
    {"img": "PS32", **{"type": "cover", "zoom": [1.0, 1.06, 1.12], "pan": [(0.5, 0.5)] * 3, "ease": _E}},  # 56  s89-90 opened to the public, 2005; forty Seking families back as guests (25.6s)
    {"img": "PANO3", **{"type": "cover", "zoom": [1.12, 1.06, 1.0], "pan": [(0.35, 0.5)] * 3, "ease": _E}},  # 57  s91 the Teo brothers' own return in 2004 (names them: shore) (9.7s)
    {"img": "PS10", **{"type": "cover", "zoom": [1.0, 1.06, 1.12], "pan": [(0.5, 0.5)] * 3, "ease": _E}},  # 58  s92-93 visits ran for years; now suspended (22.1s)
    {"img": "PS32", **{"type": "cover", "zoom": [1.12, 1.06, 1.0], "pan": [(0.5, 0.5)] * 3, "ease": _E}},  # 59  s94 designed to last until 2045 (8.4s)
    {"img": "PANO", **{"type": "cover", "zoom": [1.0, 1.06, 1.12], "pan": [(0.65, 0.5)] * 3, "ease": _E}},  # 60  s95 the date walks backwards; Phase II completed 2015 (21.3s)
    {"img": "PS10", **{"type": "cover", "zoom": [1.12, 1.06, 1.0], "pan": [(0.5, 0.5)] * 3, "ease": _E}},  # 61  s96-97 full by about 2035; the Zero Waste arithmetic (25.9s)
    {"img": "PS32", **{"type": "cover", "zoom": [1.0, 1.06, 1.12], "pan": [(0.5, 0.5)] * 3, "ease": _E}},  # 62  s98-100 the newest chapter: not burying the ash at all (12.3s)
    {"img": "STATION", **{"type": "cover", "zoom": [1.12, 1.06, 1.0], "pan": [(0.5, 0.5)] * 3, "ease": _E}},  # 63  s101 2001: the ministry studies building with bottom ash (21.8s)
    {"img": "PS10", **{"type": "cover", "zoom": [1.0, 1.06, 1.12], "pan": [(0.5, 0.5)] * 3, "ease": _E}},  # 64  s102 the 2009 road trial enters the LTA specifications (13.5s)
    {"img": "PANO", **{"type": "cover", "zoom": [1.12, 1.06, 1.0], "pan": [(0.5, 0.4)] * 3, "ease": _E}},  # 65  s103 NEWSand: treated ash with a brand echoing NEWater (20.8s)
    {"img": "PS32", **{"type": "cover", "zoom": [1.0, 1.06, 1.12], "pan": [(0.5, 0.5)] * 3, "ease": _E}},  # 66  s104-105 gasified slag; 'already under Singaporeans' feet' (14.5s)
    {"img": "PANO3", **{"type": "cover", "zoom": [1.12, 1.06, 1.0], "pan": [(0.65, 0.5)] * 3, "ease": _E}},  # 67  s106 the Scotts Road plaza and the Tampines footpath (16.5s)
    {"img": "PS10", **{"type": "cover", "zoom": [1.0, 1.06, 1.12], "pan": [(0.5, 0.5)] * 3, "ease": _E}},  # 68  s107 the Tanah Merah Coast Road trial, 2020 (18.8s)
    {"img": "PS32", **{"type": "cover", "zoom": [1.12, 1.06, 1.0], "pan": [(0.5, 0.5)] * 3, "ease": _E}},  # 69  s108 the road opens, April 2022; ash performs comparably (9.1s)
    {"img": "PANO", **{"type": "cover", "zoom": [1.0, 1.06, 1.12], "pan": [(0.5, 0.5)] * 3, "ease": _E}},  # 70  s109-110 proven in a real road, not yet routine; the standards gate (25.8s)
    {"img": "PS32", **{"type": "cover", "zoom": [1.12, 1.06, 1.0], "pan": [(0.5, 0.5)] * 3, "ease": _E}},  # 71  s111-112 the funding machine: S$45 million, then S$80 million (27.7s)
    {"img": "PS10", **{"type": "cover", "zoom": [1.0, 1.06, 1.12], "pan": [(0.5, 0.5)] * 3, "ease": _E}},  # 72  s113 'green aggregates', licensed to industry (11.4s)
    {"img": "PANO3", **{"type": "cover", "zoom": [1.12, 1.06, 1.0], "pan": [(0.5, 0.4)] * 3, "ease": _E}},  # 73  s114 'Breaking the Ground': studying what is inside the cells (23.3s)
    {"img": "PANO", **{"type": "cover", "zoom": [1.0, 1.06, 1.12], "pan": [(0.35, 0.5)] * 3, "ease": _E}},  # 74  s115-117 study complete; no excavation yet; a stockpile awaiting a use (17.8s)
    {"img": "PS32", **{"type": "cover", "zoom": [1.12, 1.06, 1.0], "pan": [(0.5, 0.5)] * 3, "ease": _E}},  # 75  s118-119 REIDS, the renewable-energy testbed since 2014 (27.9s)
    {"img": "PS10", **{"type": "cover", "zoom": [1.0, 1.06, 1.12], "pan": [(0.5, 0.5)] * 3, "ease": _E}},  # 76  s120 a rubbish island that generates its own power (7.4s)
    {"img": "STATION", **{"type": "cover", "zoom": [1.12, 1.06, 1.0], "pan": [(0.5, 0.5)] * 3, "ease": _E}},  # 77  s121 TREASURES arrives, June 2026: the research centre on the island (24.8s)
    {"img": "PANO", **{"type": "cover", "zoom": [1.0, 1.06, 1.12], "pan": [(0.65, 0.5)] * 3, "ease": _E}},  # 78  s122 Professor Chu Jian's 'transit storage and processing hub' (names him: place) (13.4s)
    {"img": "PS32", **{"type": "cover", "zoom": [1.12, 1.06, 1.0], "pan": [(0.5, 0.5)] * 3, "ease": _E}},  # 79  s123-125 nothing built yet; the direction runs opposite to the barges (20.5s)
    {"img": "PANO3", **{"type": "cover", "zoom": [1.0, 1.06, 1.12], "pan": [(0.5, 0.5)] * 3, "ease": _E}},  # 80  s126-127 the people rebuilding elsewhere; Firdaus Sani's page (names him: shore) (16.5s)
    {"img": "PS10", **{"type": "cover", "zoom": [1.12, 1.06, 1.0], "pan": [(0.5, 0.5)] * 3, "ease": _E}},  # 81  s128 grandparents moved to Telok Blangah, near open water (12.6s)
    {"img": "PANO", **{"type": "cover", "zoom": [1.0, 1.06, 1.12], "pan": [(0.5, 0.4)] * 3, "ease": _E}},  # 82  s129 Orang Laut SG: tours, feasts, his grandmother's recipes (16.6s)
    {"img": "PS32", **{"type": "cover", "zoom": [1.12, 1.06, 1.0], "pan": [(0.5, 0.5)] * 3, "ease": _E}},  # 83  s130-131 the first Hari Orang Pulau, 2025; the carnival's mainland descendant (23.1s)
    {"img": "PANO3", **{"type": "cover", "zoom": [1.0, 1.06, 1.12], "pan": [(0.35, 0.5)] * 3, "ease": _E}},  # 84  s132 where it fits in the bigger story (15.9s)
    {"img": "PS10", **{"type": "cover", "zoom": [1.12, 1.06, 1.0], "pan": [(0.5, 0.5)] * 3, "ease": _E}},  # 85  s133-135 a reef rescued; a village under the station; an island of ash (15.0s)
    {"img": "PANO", **{"type": "cover", "zoom": [1.0, 1.06, 1.12], "pan": [(0.5, 0.5)] * 3, "ease": _E}},  # 86  s136-137 Minah and Rani were early: 'Our hearts are attached to the island' (16.0s)
    {"img": "PANO3", **{"type": "cover", "zoom": [1.12, 1.06, 1.0], "pan": [(0.65, 0.5)] * 3, "ease": _E}},  # 87  s138-139 the rubbish came later; the attachment is still there (11.9s)
]

SCHEDULE = [
    (0.000, 0), (5.050, 1), (20.550, 2), (37.525, 3), (47.275, 4), (59.650, 5),
    (75.775, 6), (98.150, 7), (113.050, 8), (130.800, 9), (145.300, 10), (159.800, 11),
    (171.875, 12), (186.825, 13), (204.125, 14), (220.600, 15), (232.975, 16), (253.600, 17),
    (272.975, 18), (284.225, 19), (300.775, 20), (320.400, 21), (337.350, 22), (352.250, 23),
    (367.400, 24), (383.450, 25), (401.350, 26), (419.225, 27), (437.475, 28), (458.550, 29),
    (474.350, 30), (496.375, 31), (512.975, 32), (524.400, 33), (539.775, 34), (556.900, 35),
    (577.750, 36), (597.350, 37), (616.600, 38), (636.325, 39), (653.800, 40), (668.975, 41),
    (684.525, 42), (696.450, 43), (706.825, 44), (728.800, 45), (740.925, 46), (763.375, 47),
    (769.950, 48), (781.675, 49), (790.900, 50), (800.775, 51), (821.425, 52), (839.100, 53),
    (857.675, 54), (875.450, 55), (889.025, 56), (914.575, 57), (924.275, 58), (946.425, 59),
    (954.850, 60), (976.150, 61), (1002.000, 62), (1014.300, 63), (1036.125, 64), (1049.600, 65),
    (1070.400, 66), (1084.900, 67), (1101.375, 68), (1120.200, 69), (1129.300, 70), (1155.075, 71),
    (1182.775, 72), (1194.200, 73), (1217.500, 74), (1235.325, 75), (1263.200, 76), (1270.600, 77),
    (1295.400, 78), (1308.800, 79), (1329.300, 80), (1345.850, 81), (1358.425, 82), (1375.025, 83),
    (1398.150, 84), (1414.100, 85), (1429.125, 86), (1445.125, 87)
]
TOTAL_DURATION = 1457.05
TIMING_JSON = "audio/pulau-semakau-from-fishing-village-to-the-island-made-of-rubbish.timing.json"

# The avatar presenter, cartoon with motion: corner bubble for the first and last 30 s.
AVATAR = {"ranges": [(0, 30), (-30, None)], "motion": True}
