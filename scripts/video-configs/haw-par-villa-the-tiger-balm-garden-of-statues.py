"""Video config for the Haw Par Villa post.

The pool is the post and gallery's eighteen pictures:
the entrance paifang (the hero), the entrance in 1960
and the arch in 2014, the terraced grounds, the Pond of
Legacy and the pavilion bridge, the pagoda, the Virtues
and Vices lane, the animal parade and the monkey army,
the giant apes of 1963, the brothers' own statues, and
the Ten Courts of Hell in five frames: the cave-mouth
entrance guarded by Ox-Head and Horse-Face, the First
Court, the Sixth Court, a close tableau, and the early
KITLV court photograph (the TIFF's 1280px JPEG derivative,
as used in the post).

Named-place audit: the First Court sentences run on the
First Court photograph; the Ox-Head and Horse-Face
sentence on the entrance they guard. The Second Court
runs on the Courts' entrance under a generic title; the
Third and Fifth Courts run on court tableaux whose
captions identify no court. The Sixth Court photograph
sits under the schoolchildren sentence, which names no
court, and is titled as what it is. Dragon World's
sentence runs on the Courts' entrance titled by its era;
no photograph of the dragon exists in the pool. The
villa is named in no slide title over a garden photograph.

52 slides, 738.12s. No slide over 30s; the
longest are the grounds-in-limbo slide at 25.87s and the
simple-garden-and-zoo slide at 25.93s. Narration: Kokoro
with the OpenVoice clone. Pronunciation overrides for
the post's names filed 2026-11-27, NOT ear-verified yet.
AVATAR: first and last 30s, cartoon with motion.
"""

IMAGES = {
    "PAIFANG": "https://upload.wikimedia.org/wikipedia/commons/1/14/Haw_Par_Villa_Paifang.jpg",
    "HILLS": "https://upload.wikimedia.org/wikipedia/commons/a/a2/Hilly_grounds_of_Haw_Par_Villa_%2814813779273%29.jpg",
    "ENT1960": "https://upload.wikimedia.org/wikipedia/commons/b/b5/TigerBalmGarden-HawParVilla-entrance-Singapore-196009.jpg",
    "ARCH2014": "https://upload.wikimedia.org/wikipedia/commons/0/0b/Chinese_arch_at_entrance_of_Haw_Par_Villa_%2814791657844%29.jpg",
    "POND": "https://upload.wikimedia.org/wikipedia/commons/6/63/Pond_of_Legacy%2C_Haw_Par_Villa_%2814790804261%29.jpg",
    "BRIDGE": "https://upload.wikimedia.org/wikipedia/commons/5/5c/Bridge_connecting_to_pavilion_island%2C_Haw_Par_Villa_%2814770947476%29.jpg",
    "LANE": "https://upload.wikimedia.org/wikipedia/commons/f/fb/Virtues_and_Vices_lane%2C_Haw_Par_Villa_%2814607157740%29.jpg",
    "PARADE": "https://upload.wikimedia.org/wikipedia/commons/a/ab/Animal_parade%2C_Haw_Par_Villa_%2814770865746%29.jpg",
    "PAGODA": "https://upload.wikimedia.org/wikipedia/commons/e/ef/Towering_pagoda%2C_Haw_Par_Villa_%2814607177310%29.jpg",
    "GARDEN1963": "https://upload.wikimedia.org/wikipedia/commons/0/0c/Haw_Par_Villa_Tiger_Balm_Gardens_Singapore_1963_01.jpg",
    "KITLV": "https://upload.wikimedia.org/wikipedia/commons/thumb/5/59/D_101_View_of_Haw_Par_Villa._S_%27pore.%2C_KITLV_1404805.tiff/lossy-page1-1280px-D_101_View_of_Haw_Par_Villa._S_%27pore.%2C_KITLV_1404805.tiff.jpg",
    "COURTCU": "https://upload.wikimedia.org/wikipedia/commons/d/db/Chinese_Court_of_Hell.jpg",
    "COURT1": "https://upload.wikimedia.org/wikipedia/commons/4/48/First_Court_of_Hell%2C_Haw_Par_Villa_%2814607331868%29.jpg",
    "COURT6": "https://upload.wikimedia.org/wikipedia/commons/5/55/Body_sawn_into_two%2C_Sixth_Court_of_Hell_%E2%80%93_Yama_King_Piencheng%2C_Haw_Par_Villa_%2814813818183%29.jpg",
    "HELLGATE": "https://upload.wikimedia.org/wikipedia/commons/4/45/Entrance_to_10_Courts_of_Hell.jpg",
    "MONKEYARMY": "https://upload.wikimedia.org/wikipedia/commons/f/f6/Monkey_army%2C_Haw_Par_Villa_%2814791531714%29.jpg",
    "MONKEY25": "https://upload.wikimedia.org/wikipedia/commons/5/54/20250629_monkeyking.jpg",
    "AWSTATUES": "https://upload.wikimedia.org/wikipedia/commons/c/c4/Aw_Boon_Haw%2C_Aw_Boon_Par%2C_Haw_Par_Villa_%2814813863263%29.jpg",
}

# Every image is captioned in the post or its gallery.
CREDITS = {}

# The channel's 2x2 thumbnail grid, in story order: the
# gate, the First Court, the garden in 1963, hell today.
THUMBNAIL = [
    {"img": "PAIFANG", "pan": (0.5, 0.5)},
    {"img": "COURT1", "pan": (0.5, 0.5)},
    {"img": "GARDEN1963", "pan": (0.5, 0.5)},
    {"img": "HELLGATE", "pan": (0.5, 0.5)},
]

_E = "ease-in-out"

SLIDES = [
    {"img": "PAIFANG", **{"type": "cover", "zoom": [1.0, 1.06, 1.12], "pan": [[0.5, 0.5], [0.5, 0.5], [0.5, 0.5]]}, "title": "Haw Par Villa"},  # 0  title (4.03s) (s0)
    {"img": "HILLS", **{"type": "cover", "zoom": [1.12, 1.06, 1.0], "pan": [[0.35, 0.5], [0.35, 0.5], [0.35, 0.5]]}, "title": "The strangest garden in Singapore"},  # 1  the hook: demons, monkeys, sinners sawn in half (20.38s) (s1)
    {"img": "ENT1960", **{"type": "cover", "zoom": [1.0, 1.06, 1.12], "pan": [[0.65, 0.5], [0.65, 0.5], [0.65, 0.5]]}, "title": "The entrance in 1960"},  # 2  it has outlived the mansion; it waits in limbo (14.60s) (s2-3)
    {"img": "ARCH2014", **{"type": "cover", "zoom": [1.12, 1.06, 1.0], "pan": [[0.5, 0.5], [0.5, 0.5], [0.5, 0.5]]}, "title": "The entrance arch"},  # 3  the garden's own story; the brothers have theirs (8.53s) (s4)
    {"img": "PAIFANG", **{"type": "cover", "zoom": [1.0, 1.06, 1.12], "pan": [[0.35, 0.5], [0.35, 0.5], [0.35, 0.5]]}, "title": "The founding, briefly"},  # 4  told briefly; the 1935 seafront hill (14.05s) (s5-6)
    {"img": "ARCH2014", **{"type": "cover", "zoom": [1.12, 1.06, 1.0], "pan": [[0.65, 0.5], [0.65, 0.5], [0.65, 0.5]]}, "title": "The gift to Boon Par"},  # 5  the Art Deco villa of 1937; the name Haw Par (17.18s) (s7-8)
    {"img": "HILLS", **{"type": "cover", "zoom": [1.0, 1.06, 1.12], "pan": [[0.5, 0.5], [0.5, 0.5], [0.5, 0.5]]}, "title": "The second Tiger Balm Garden"},  # 6  Hong Kong first, in 1932; this one opened free (12.88s) (s9)
    {"img": "PAIFANG", **{"type": "cover", "zoom": [1.12, 1.06, 1.0], "pan": [[0.35, 0.5], [0.35, 0.5], [0.35, 0.5]]}, "title": "The tiger at the gate"},  # 7  no secret: an advertisement for Tiger Balm (10.52s) (s10-11)
    {"img": "LANE", **{"type": "cover", "zoom": [1.0, 1.06, 1.12], "pan": [[0.65, 0.5], [0.65, 0.5], [0.65, 0.5]]}, "title": "A school in statues"},  # 8  also a school: piety, charity, judgement (14.30s) (s12)
    {"img": "HILLS", **{"type": "cover", "zoom": [1.12, 1.06, 1.0], "pan": [[0.5, 0.5], [0.5, 0.5], [0.5, 0.5]]}, "title": "Four terraces up the hill"},  # 9  four terraces; the garage at ground level (11.80s) (s13-14)
    {"img": "POND", **{"type": "cover", "zoom": [1.0, 1.06, 1.12], "pan": [[0.35, 0.5], [0.35, 0.5], [0.35, 0.5]]}, "title": "The Pond of Legacy"},  # 10  the second tier: the family's aquarium pond (8.07s) (s15)
    {"img": "BRIDGE", **{"type": "cover", "zoom": [1.12, 1.06, 1.0], "pan": [[0.65, 0.5], [0.65, 0.5], [0.65, 0.5]]}, "title": "The pavilion bridge"},  # 11  the pleasure ground; the villa on the top tier (14.65s) (s16-17)
    {"img": "PARADE", **{"type": "cover", "zoom": [1.0, 1.06, 1.12], "pan": [[0.5, 0.5], [0.5, 0.5], [0.5, 0.5]]}, "title": "The animal parade"},  # 12  the simple garden of 1937; the zoo that became statues (25.92s) (s18-19)
    {"img": "PAGODA", **{"type": "cover", "zoom": [1.12, 1.06, 1.0], "pan": [[0.35, 0.5], [0.35, 0.5], [0.35, 0.5]]}, "title": "The pagoda"},  # 13  fifteen storeys, later cut to four for Sakyamuni (14.78s) (s20)
    {"img": "COURTCU", **{"type": "cover", "zoom": [1.0, 1.06, 1.12], "pan": [[0.65, 0.5], [0.65, 0.5], [0.65, 0.5]]}, "title": "A court of hell, close up"},  # 14  the Swatow craftsmen; Kwek Hoon Sua and Kwek Choon Sua (19.30s) (s21-22)
    {"img": "KITLV", **{"type": "cover", "zoom": [1.12, 1.06, 1.0], "pan": [[0.5, 0.5], [0.5, 0.5], [0.5, 0.5]]}, "title": "An early court tableau"},  # 15  Tan See Hua, Tan Seng Hua and Mr Liu; no blueprints (9.20s) (s23-24)
    {"img": "HILLS", **{"type": "cover", "zoom": [1.0, 1.06, 1.12], "pan": [[0.35, 0.5], [0.35, 0.5], [0.35, 0.5]]}, "title": "The morning rounds"},  # 16  Boon Haw directs in person, down to the colours (16.65s) (s25)
    {"img": "PAIFANG", **{"type": "cover", "zoom": [1.12, 1.06, 1.0], "pan": [[0.65, 0.5], [0.65, 0.5], [0.65, 0.5]]}, "title": "Drawn at full scale"},  # 17  drawn in concrete by a man selling ointment (19.02s) (s26)
    {"img": "LANE", **{"type": "cover", "zoom": [1.0, 1.06, 1.12], "pan": [[0.5, 0.5], [0.5, 0.5], [0.5, 0.5]]}, "title": "The Virtues and Vices lane"},  # 18  the exhibits mixed; the lane of moral tales (12.97s) (s27-28)
    {"img": "MONKEY25", **{"type": "cover", "zoom": [1.12, 1.06, 1.0], "pan": [[0.35, 0.5], [0.35, 0.5], [0.35, 0.5]]}, "title": "The Monkey King, 2025"},  # 19  Journey to the West; the Eight Immortals (7.20s) (s29)
    {"img": "PARADE", **{"type": "cover", "zoom": [1.0, 1.06, 1.12], "pan": [[0.65, 0.5], [0.65, 0.5], [0.65, 0.5]]}, "title": "The animal parade"},  # 20  lotus and carp; instruction by spectacle (17.30s) (s30-31)
    {"img": "ENT1960", **{"type": "cover", "zoom": [1.12, 1.06, 1.0], "pan": [[0.5, 0.5], [0.5, 0.5], [0.5, 0.5]]}, "title": "The entrance in 1960"},  # 21  Boon Par leaves for Rangoon, dies 1944 (12.90s) (s32-33)
    {"img": "HILLS", **{"type": "cover", "zoom": [1.0, 1.06, 1.12], "pan": [[0.35, 0.5], [0.35, 0.5], [0.35, 0.5]]}, "title": "The garden survived"},  # 22  war damage; the villa bombed and demolished, undated (18.08s) (s34-35)
    {"img": "GARDEN1963", **{"type": "cover", "zoom": [1.12, 1.06, 1.0], "pan": [[0.65, 0.5], [0.65, 0.5], [0.65, 0.5]]}, "title": "The gardens in 1963"},  # 23  Boon Haw returns and rebuilds over the pleasure ground (19.10s) (s36-37)
    {"img": "COURT1", **{"type": "cover", "zoom": [1.0, 1.06, 1.12], "pan": [[0.5, 0.5], [0.5, 0.5], [0.5, 0.5]]}, "title": "The First Court of Hell"},  # 24  the famous statuary is post-war; the Courts above all (8.28s) (s38-39)
    {"img": "COURTCU", **{"type": "cover", "zoom": [1.12, 1.06, 1.0], "pan": [[0.35, 0.5], [0.35, 0.5], [0.35, 0.5]]}, "title": "The Ten Courts of Hell"},  # 25  the walk-through of the underworld (16.48s) (s40)
    {"img": "COURT1", **{"type": "cover", "zoom": [1.0, 1.06, 1.12], "pan": [[0.65, 0.5], [0.65, 0.5], [0.65, 0.5]]}, "title": "The First Court of Hell"},  # 26  cause and effect: one reaps what one sows (10.38s) (s41)
    {"img": "HELLGATE", **{"type": "cover", "zoom": [1.12, 1.06, 1.0], "pan": [[0.5, 0.5], [0.5, 0.5], [0.5, 0.5]]}, "title": "Guarded by Ox-Head and Horse-Face"},  # 27  the entrance and its escorts of the dead (5.22s) (s42)
    {"img": "COURT1", **{"type": "cover", "zoom": [1.0, 1.06, 1.12], "pan": [[0.35, 0.5], [0.35, 0.5], [0.35, 0.5]]}, "title": "The First Court of Hell"},  # 28  Qinguang; the bridges; the Mirror of Retribution (19.12s) (s43-44)
    {"img": "HELLGATE", **{"type": "cover", "zoom": [1.12, 1.06, 1.0], "pan": [[0.65, 0.5], [0.65, 0.5], [0.65, 0.5]]}, "title": "The Ten Courts of Hell"},  # 29  the punishments are specific; the Second Court (15.95s) (s45-46)
    {"img": "COURTCU", **{"type": "cover", "zoom": [1.0, 1.06, 1.12], "pan": [[0.5, 0.5], [0.5, 0.5], [0.5, 0.5]]}, "title": "A court of hell, close up"},  # 30  the Third Court, on an unidentified court tableau (12.43s) (s47)
    {"img": "KITLV", **{"type": "cover", "zoom": [1.12, 1.06, 1.0], "pan": [[0.35, 0.5], [0.35, 0.5], [0.35, 0.5]]}, "title": "An early court tableau"},  # 31  the Fifth Court, on the early KITLV tableau (10.03s) (s48)
    {"img": "COURT6", **{"type": "cover", "zoom": [1.0, 1.06, 1.12], "pan": [[0.65, 0.5], [0.65, 0.5], [0.65, 0.5]]}, "title": "The Sixth Court of Hell"},  # 32  schoolchildren walked through, promising to be good (11.30s) (s49)
    {"img": "MONKEYARMY", **{"type": "cover", "zoom": [1.12, 1.06, 1.0], "pan": [[0.5, 0.5], [0.5, 0.5], [0.5, 0.5]]}, "title": "The monkey army"},  # 33  the legend that the statues come alive at night (11.88s) (s50)
    {"img": "AWSTATUES", **{"type": "cover", "zoom": [1.0, 1.06, 1.12], "pan": [[0.35, 0.5], [0.35, 0.5], [0.35, 0.5]]}, "title": "Aw Boon Haw and Aw Boon Par"},  # 34  Boon Haw dies 1954; the garden passes to Cheng Chye (6.35s) (s51)
    {"img": "HILLS", **{"type": "cover", "zoom": [1.12, 1.06, 1.0], "pan": [[0.65, 0.5], [0.65, 0.5], [0.65, 0.5]]}, "title": "The International Corners"},  # 35  sumo wrestler, Thai dancer, Statue of Liberty replica (17.68s) (s52)
    {"img": "GARDEN1963", **{"type": "cover", "zoom": [1.0, 1.06, 1.12], "pan": [[0.5, 0.5], [0.5, 0.5], [0.5, 0.5]]}, "title": "The giant apes, 1963"},  # 36  after 1971, no major changes; a million visitors a year (19.50s) (s53)
    {"img": "AWSTATUES", **{"type": "cover", "zoom": [1.12, 1.06, 1.0], "pan": [[0.35, 0.5], [0.35, 0.5], [0.35, 0.5]]}, "title": "The brothers' memorial"},  # 37  1985 acquisition; the statues donated, the name kept (16.45s) (s54-55)
    {"img": "ARCH2014", **{"type": "cover", "zoom": [1.0, 1.06, 1.12], "pan": [[0.65, 0.5], [0.65, 0.5], [0.65, 0.5]]}, "title": "The entrance arch"},  # 38  the board takes over; the 1988 lease (11.03s) (s56)
    {"img": "HELLGATE", **{"type": "cover", "zoom": [1.12, 1.06, 1.0], "pan": [[0.5, 0.5], [0.5, 0.5], [0.5, 0.5]]}, "title": "Dragon World, 1990"},  # 39  the theme park; the Courts in a 60-metre dragon (17.38s) (s57)
    {"img": "HILLS", **{"type": "cover", "zoom": [1.0, 1.06, 1.12], "pan": [[0.35, 0.5], [0.35, 0.5], [0.35, 0.5]]}, "title": "A free public park again"},  # 40  it lost money heavily; free again in 2001 (15.32s) (s58-59)
    {"img": "COURTCU", **{"type": "cover", "zoom": [1.12, 1.06, 1.0], "pan": [[0.65, 0.5], [0.65, 0.5], [0.65, 0.5]]}, "title": "The Courts behind walls"},  # 41  the dragon demolished; the Courts behind stone walls (5.10s) (s60)
    {"img": "POND", **{"type": "cover", "zoom": [1.0, 1.06, 1.12], "pan": [[0.5, 0.5], [0.5, 0.5], [0.5, 0.5]]}, "title": "The Pond of Legacy"},  # 42  the Hua Song Museum; the 2014 festival (20.30s) (s61)
    {"img": "PAIFANG", **{"type": "cover", "zoom": [1.12, 1.06, 1.0], "pan": [[0.35, 0.5], [0.35, 0.5], [0.35, 0.5]]}, "title": "The entrance paifang"},  # 43  Journeys appointed in 2015 (7.92s) (s62)
    {"img": "ARCH2014", **{"type": "cover", "zoom": [1.0, 1.06, 1.12], "pan": [[0.65, 0.5], [0.65, 0.5], [0.65, 0.5]]}, "title": "The entrance arch"},  # 44  the 2020-21 restoration, the arch conserved (17.15s) (s63)
    {"img": "HELLGATE", **{"type": "cover", "zoom": [1.12, 1.06, 1.0], "pan": [[0.5, 0.5], [0.5, 0.5], [0.5, 0.5]]}, "title": "Hell's Museum"},  # 45  the world's first museum of death and the afterlife (24.65s) (s64)
    {"img": "PAIFANG", **{"type": "cover", "zoom": [1.0, 1.06, 1.12], "pan": [[0.35, 0.5], [0.35, 0.5], [0.35, 0.5]]}, "title": "The station at the gate"},  # 46  the Circle Line station named for the park (13.35s) (s65)
    {"img": "HILLS", **{"type": "cover", "zoom": [1.12, 1.06, 1.0], "pan": [[0.65, 0.5], [0.65, 0.5], [0.65, 0.5]]}, "title": "The grounds today"},  # 47  the story pauses; the contract ends, the gates partly close (25.88s) (s66-67)
    {"img": "ARCH2014", **{"type": "cover", "zoom": [1.0, 1.06, 1.12], "pan": [[0.5, 0.5], [0.5, 0.5], [0.5, 0.5]]}, "title": "The entrance arch"},  # 48  no reopening date; the park is not gazetted (9.57s) (s68-69)
    {"img": "HELLGATE", **{"type": "cover", "zoom": [1.12, 1.06, 1.0], "pan": [[0.35, 0.5], [0.35, 0.5], [0.35, 0.5]]}, "title": "Hell's Museum today"},  # 49  what remains open: the museum, daily, S$22 and S$12 (16.70s) (s70)
    {"img": "MONKEY25", **{"type": "cover", "zoom": [1.0, 1.06, 1.12], "pan": [[0.65, 0.5], [0.65, 0.5], [0.65, 0.5]]}, "title": "The Monkey King, 2025"},  # 50  Haw Ror Villa returns for a fifth Halloween (13.07s) (s71)
    {"img": "PAIFANG", **{"type": "cover", "zoom": [1.12, 1.06, 1.0], "pan": [[0.5, 0.5], [0.5, 0.5], [0.5, 0.5]]}, "title": "The entrance paifang"},  # 51  the close: built to sell balm, awaiting its future (16.27s) (s72)
]

SCHEDULE = [
    (0.000, 0), (4.025, 1), (24.400, 2),
    (39.000, 3), (47.525, 4), (61.575, 5),
    (78.750, 6), (91.625, 7), (102.150, 8),
    (116.450, 9), (128.250, 10), (136.325, 11),
    (150.975, 12), (176.900, 13), (191.675, 14),
    (210.975, 15), (220.175, 16), (236.825, 17),
    (255.850, 18), (268.825, 19), (276.025, 20),
    (293.325, 21), (306.225, 22), (324.300, 23),
    (343.400, 24), (351.675, 25), (368.150, 26),
    (378.525, 27), (383.750, 28), (402.875, 29),
    (418.825, 30), (431.250, 31), (441.275, 32),
    (452.575, 33), (464.450, 34), (470.800, 35),
    (488.475, 36), (507.975, 37), (524.425, 38),
    (535.450, 39), (552.825, 40), (568.150, 41),
    (573.250, 42), (593.550, 43), (601.475, 44),
    (618.625, 45), (643.275, 46), (656.625, 47),
    (682.500, 48), (692.075, 49), (708.775, 50),
    (721.850, 51)
]
TOTAL_DURATION = 738.125
TIMING_JSON = "audio/haw-par-villa-the-tiger-balm-garden-of-statues.timing.json"

# The avatar presenter, cartoon with motion: corner bubble for the first and last 30 s.
AVATAR = {"ranges": [(0, 30), (-30, None)], "motion": True}
