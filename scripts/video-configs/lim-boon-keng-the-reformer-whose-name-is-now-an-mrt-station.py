"""Video config for the Lim Boon Keng post.

The pool is all twelve pictures from the post and its gallery:
two portraits of Lim (the Lee Brothers photograph of the 1930s
and the portrait from his Xiamen years), Song Ong Siang's
portrait and the title page of his One Hundred Years' History,
Tan Kah Kee photographed with Sun Yat-sen in 1911, Sun alone in
1910, the Singapore Chinese Girls' School as it stands today,
the Wenqing Pavilion at Xiamen University with Lim's statue,
his and Grace's tombstone and the old Bidadari Cemetery gate,
and two photographs of Boon Keng MRT station. Twelve pictures
for fourteen and a half minutes: images recur at new story
beats with varied pans and alternating zoom direction, never
twice in a row.

Named-person rule: the pool holds portraits of Lim, of Song
Ong Siang and of Sun Yat-sen (alone and with Tan Kah Kee). A
sentence naming Song or Sun shows that man's own portrait or
photograph, or Lim himself; sentences naming anyone else -
Hullett, Robertson, Mitchell, Ridley, Tan Chay Yan, Lim Peng
Siang, Lim Nee Soon, Kang Youwei, Lee Kuan Yew - show Lim, the
school, the book or the station, never another named man's
portrait. Sentences naming Lim Peng Siang and Lim Nee Soon,
where Lim Boon Keng is himself the subject, show Lim or the
book that chronicles the banks.

Every slide carries its discreet photo title (standing rule,
Chris, 2026-11-11): the short form of its image's post/gallery
caption, drawn small in the top corner on a soft dark backing
for the slide's whole run.

51 slides, 865.18s. Narration: Kokoro with the OpenVoice clone.
Pronunciations cleared by Chris's ear 2026-11-16.
AVATAR: first and last 30s, cartoon with motion.
"""

IMAGES = {
    "LIM30": "https://upload.wikimedia.org/wikipedia/commons/9/92/Lim_Boon_Keng_in_the_1930s.jpg",
    "LIMX": "https://upload.wikimedia.org/wikipedia/commons/a/a5/Lim_Boon_Keng_from_The_Chinese_in_Southeast_Asia_Will_Forever_Remain_Eternally_Successful%2C_1947.jpg",
    "SONG": "https://upload.wikimedia.org/wikipedia/commons/9/9e/Song_Ong_Siang.jpg",
    "BOOK": "https://upload.wikimedia.org/wikipedia/commons/a/a4/One_Hundred_Years%27_History_of_the_Chinese_in_Singapore_-_title_page.jpg",
    "SCGS": "https://upload.wikimedia.org/wikipedia/commons/e/e3/Singapore_Chinese_Girls_School_20240519_01.jpg",
    "TANSUN": "https://upload.wikimedia.org/wikipedia/commons/9/96/Tan_Kah_Kee_with_Dr_Sun_Yat_Sen.jpg",
    "SUN": "https://upload.wikimedia.org/wikipedia/commons/4/48/Sun_Yat-sen_1910.jpg",
    "WENQING": "https://upload.wikimedia.org/wikipedia/commons/8/86/Xiamen_University_Wenqing_Pavillion.jpg",
    "GRAVE": "https://upload.wikimedia.org/wikipedia/commons/7/73/Gravestone_of_Lim_Boon_Keng_and_Grace_Yin_at_Bidadari_Memorial_Garden%2C_Singapore_-_20110227.jpg",
    "GATE": "https://upload.wikimedia.org/wikipedia/commons/8/8e/Gate_of_Bidadari_Cemetery%2C_Singapore_-_20110227.jpg",
    "MRT": "https://upload.wikimedia.org/wikipedia/commons/7/78/NE9_Boon_Keng_MRT_Entrance_20201010_01.jpg",
    "EXIT": "https://upload.wikimedia.org/wikipedia/commons/8/8a/NE9_Boon_Keng_Exit_A_20201010.jpg",
}

# Every image is captioned in the post or its gallery.
CREDITS = {}

# The channel's 2x2 thumbnail grid, in story order: the man,
# his friend and rival, the school he founded, his station.
THUMBNAIL = [
    {"img": "LIM30", "pan": (0.5, 0.5)},
    {"img": "SONG", "pan": (0.5, 0.5)},
    {"img": "SCGS", "pan": (0.5, 0.5)},
    {"img": "EXIT", "pan": (0.5, 0.5)},
]

_E = "ease-in-out"

SLIDES = [
    {"img": "EXIT", **{"type": "cover", "title": "Boon Keng MRT, Exit A", "zoom": [1.0, 1.06, 1.12], "pan": [(0.5, 0.5)] * 3, "ease": _E}},  # 0  s0-1 title + the station hook: thousands tap in daily (14.3s)
    {"img": "LIM30", **{"type": "cover", "title": "Lim Boon Keng in the 1930s", "zoom": [1.12, 1.06, 1.0], "pan": [(0.35, 0.5)] * 3, "ease": _E}},  # 1  s2 the name is a man's: the whole life in one sentence (24.6s)
    {"img": "LIMX", **{"type": "cover", "title": "Lim Boon Keng, the Xiamen portrait", "zoom": [1.0, 1.06, 1.12], "pan": [(0.5, 0.5)] * 3, "ease": _E}},  # 2  s3-4 the Grand Old Man of Singapore; today, nobody knows (10.1s)
    {"img": "LIM30", **{"type": "cover", "title": "Lim Boon Keng in the 1930s", "zoom": [1.12, 1.06, 1.0], "pan": [(0.65, 0.5)] * 3, "ease": _E}},  # 3  s5-6 third-generation Peranakan; the grandfather from Fujian, 1839 (20.8s)
    {"img": "LIMX", **{"type": "cover", "title": "Lim Boon Keng, the Xiamen portrait", "zoom": [1.0, 1.06, 1.12], "pan": [(0.5, 0.4)] * 3, "ease": _E}},  # 4  s7-8 both parents dead by fourteen; Raffles, and Hullett paying the fees (names Hullett: Lim himself) (21.1s)
    {"img": "LIM30", **{"type": "cover", "title": "Lim Boon Keng in the 1930s", "zoom": [1.12, 1.06, 1.0], "pan": [(0.5, 0.5)] * 3, "ease": _E}},  # 5  s9-11 turned towards medicine; the 1887 exam; 'He came second.' (15.6s)
    {"img": "SONG", **{"type": "cover", "title": "Song Ong Siang", "zoom": [1.0, 1.06, 1.12], "pan": [(0.5, 0.5)] * 3, "ease": _E}},  # 6  s12-13 Song topped it twice and was underage both times; the scholarship fell to the runner-up (names Song: his portrait) (18.0s)
    {"img": "BOOK", **{"type": "cover", "title": "Song's One Hundred Years' History, 1923", "zoom": [1.12, 1.06, 1.0], "pan": [(0.35, 0.5)] * 3, "ease": _E}},  # 7  s14 Song won it properly in 1888; collaborators for the rest of their lives (11.6s)
    {"img": "LIMX", **{"type": "cover", "title": "Lim Boon Keng, the Xiamen portrait", "zoom": [1.0, 1.06, 1.12], "pan": [(0.5, 0.5)] * 3, "ease": _E}},  # 8  s15 Edinburgh: first-class honours, the only one of 204 graduates (16.4s)
    {"img": "LIM30", **{"type": "cover", "title": "Lim Boon Keng in the 1930s", "zoom": [1.12, 1.06, 1.0], "pan": [(0.65, 0.5)] * 3, "ease": _E}},  # 9  s16-17 the Royal Medical Society; Cambridge after; home in 1893, aged twenty-four (17.4s)
    {"img": "LIMX", **{"type": "cover", "title": "Lim Boon Keng, the Xiamen portrait", "zoom": [1.0, 1.06, 1.12], "pan": [(0.5, 0.4)] * 3, "ease": _E}},  # 10  s18-19 private practice on Telok Ayer Street; The Dispensary partnership, 1896 (19.9s)
    {"img": "LIM30", **{"type": "cover", "title": "Lim Boon Keng in the 1930s", "zoom": [1.12, 1.06, 1.0], "pan": [(0.5, 0.5)] * 3, "ease": _E}},  # 11  s20 'offered free treatment to patients who were poor' (9.8s)
    {"img": "LIMX", **{"type": "cover", "title": "Lim Boon Keng, the Xiamen portrait", "zoom": [1.0, 1.06, 1.12], "pan": [(0.5, 0.5)] * 3, "ease": _E}},  # 12  s21 taught at the medical school, 1907-1910, without pay (12.0s)
    {"img": "LIM30", **{"type": "cover", "title": "Lim Boon Keng in the 1930s", "zoom": [1.12, 1.06, 1.0], "pan": [(0.35, 0.5)] * 3, "ease": _E}},  # 13  s22-23 what opium was doing; the Anti-Opium Society and the Opium Refuge (24.8s)
    {"img": "BOOK", **{"type": "cover", "title": "Song's One Hundred Years' History, 1923", "zoom": [1.0, 1.06, 1.12], "pan": [(0.5, 0.5)] * 3, "ease": _E}},  # 14  s24-25 the 1898 essay; campaigns against the mui tsai, foot-binding and gambling (20.9s)
    {"img": "LIMX", **{"type": "cover", "title": "Lim Boon Keng, the Xiamen portrait", "zoom": [1.12, 1.06, 1.0], "pan": [(0.65, 0.5)] * 3, "ease": _E}},  # 15  s26-27 the Legislative Council at twenty-six; Governor Mitchell's objection overruled (names Mitchell: Lim himself) (19.5s)
    {"img": "LIM30", **{"type": "cover", "title": "Lim Boon Keng in the 1930s", "zoom": [1.0, 1.06, 1.12], "pan": [(0.5, 0.4)] * 3, "ease": _E}},  # 16  s28 served to 1903, reappointed 1915: fourteen years in all (14.8s)
    {"img": "LIMX", **{"type": "cover", "title": "Lim Boon Keng, the Xiamen portrait", "zoom": [1.12, 1.06, 1.0], "pan": [(0.5, 0.5)] * 3, "ease": _E}},  # 17  s29-30 housing, sanitation, a minimum wage; the 1896 Commission of Inquiry into poverty (21.6s)
    {"img": "LIM30", **{"type": "cover", "title": "Lim Boon Keng in the 1930s", "zoom": [1.0, 1.06, 1.12], "pan": [(0.5, 0.5)] * 3, "ease": _E}},  # 18  s31-32 the cluster of offices before thirty; the OBE, 1918 (18.5s)
    {"img": "SONG", **{"type": "cover", "title": "Song Ong Siang", "zoom": [1.12, 1.06, 1.0], "pan": [(0.35, 0.5)] * 3, "ease": _E}},  # 19  s33-34 the reform circle around Lim and Song; the Chinese Philomathic Society, 1896 (names Song: his portrait) (20.5s)
    {"img": "BOOK", **{"type": "cover", "title": "Song's One Hundred Years' History, 1923", "zoom": [1.0, 1.06, 1.12], "pan": [(0.5, 0.5)] * 3, "ease": _E}},  # 20  s35 The Straits Chinese Magazine, 1897: Straits-born, in English (19.5s)
    {"img": "SCGS", **{"type": "cover", "title": "Singapore Chinese Girls' School today", "zoom": [1.12, 1.06, 1.0], "pan": [(0.65, 0.5)] * 3, "ease": _E}},  # 21  s36 the Singapore Chinese Girls' School founded, 1899 (18.5s)
    {"img": "LIM30", **{"type": "cover", "title": "Lim Boon Keng in the 1930s", "zoom": [1.0, 1.06, 1.12], "pan": [(0.5, 0.4)] * 3, "ease": _E}},  # 22  s37 Mandarin classes at his own home, the same year (9.7s)
    {"img": "LIMX", **{"type": "cover", "title": "Lim Boon Keng, the Xiamen portrait", "zoom": [1.12, 1.06, 1.0], "pan": [(0.5, 0.5)] * 3, "ease": _E}},  # 23  s38-39 'His most visible campaign was over hair': cut the towchang (23.4s)
    {"img": "BOOK", **{"type": "cover", "title": "Song's One Hundred Years' History, 1923", "zoom": [1.0, 1.06, 1.12], "pan": [(0.5, 0.5)] * 3, "ease": _E}},  # 24  s40 institution after institution: a newspaper, the SCBA, the Chamber (17.6s)
    {"img": "LIMX", **{"type": "cover", "title": "Lim Boon Keng, the Xiamen portrait", "zoom": [1.12, 1.06, 1.0], "pan": [(0.35, 0.5)] * 3, "ease": _E}},  # 25  s41-42 the businessman's eye; Ridley preaching rubber (names Ridley: Lim himself) (14.0s)
    {"img": "LIM30", **{"type": "cover", "title": "Lim Boon Keng in the 1930s", "zoom": [1.0, 1.06, 1.12], "pan": [(0.5, 0.5)] * 3, "ease": _E}},  # 26  s43-44 Tan Chay Yan's Malacca planting; the Serangoon Road Company; the boom (names Tan: Lim himself) (16.7s)
    {"img": "LIMX", **{"type": "cover", "title": "Lim Boon Keng, the Xiamen portrait", "zoom": [1.12, 1.06, 1.0], "pan": [(0.65, 0.5)] * 3, "ease": _E}},  # 27  s45-46 'Banking followed': all three Hokkien banks (names Lim Peng Siang: Lim himself, the sentence's subject) (19.2s)
    {"img": "LIM30", **{"type": "cover", "title": "Lim Boon Keng in the 1930s", "zoom": [1.0, 1.06, 1.12], "pan": [(0.5, 0.4)] * 3, "ease": _E}},  # 28  s47-48 31 October 1932: the three amalgamated into OCBC; he had no hand in it (20.2s)
    {"img": "BOOK", **{"type": "cover", "title": "Song's One Hundred Years' History, 1923", "zoom": [1.12, 1.06, 1.0], "pan": [(0.5, 0.5)] * 3, "ease": _E}},  # 29  s49-50 what he co-founded were the three banks that became it; the Overseas Assurance Corporation, 1920 (names Lim Nee Soon: the book) (17.2s)
    {"img": "TANSUN", **{"type": "cover", "title": "Tan Kah Kee with Sun Yat-sen, 1911", "zoom": [1.0, 1.06, 1.12], "pan": [(0.5, 0.5)] * 3, "ease": _E}},  # 30  s51-52 China: Sun Yat-sen and Kang Youwei; agent and fundraiser for the Tongmenghui (names Sun: his photo with Tan) (23.5s)
    {"img": "SUN", **{"type": "cover", "title": "Sun Yat-sen, 1910", "zoom": [1.12, 1.06, 1.0], "pan": [(0.35, 0.5)] * 3, "ease": _E}},  # 31  s53 1911: Sun's personal physician, his secretary, the health posts (names Sun: his portrait) (21.8s)
    {"img": "TANSUN", **{"type": "cover", "title": "Tan Kah Kee with Sun Yat-sen, 1911", "zoom": [1.0, 1.06, 1.12], "pan": [(0.5, 0.5)] * 3, "ease": _E}},  # 32  s54-55 the 1921 call; Tan Kah Kee's new university at Xiamen (names Tan: his photo) (20.0s)
    {"img": "LIMX", **{"type": "cover", "title": "Lim Boon Keng, the Xiamen portrait", "zoom": [1.12, 1.06, 1.0], "pan": [(0.65, 0.5)] * 3, "ease": _E}},  # 33  s56 resigned the Council, gave up his businesses: president 1921-1937, without salary (12.8s)
    {"img": "WENQING", **{"type": "cover", "title": "His statue at Xiamen University", "zoom": [1.0, 1.06, 1.12], "pan": [(0.5, 0.4)] * 3, "ease": _E}},  # 34  s57 the Li Sao in English; Giles's preface; Tagore's visit (names Qu Yuan, Giles, Tagore: his university) (14.8s)
    {"img": "LIM30", **{"type": "cover", "title": "Lim Boon Keng in the 1930s", "zoom": [1.12, 1.06, 1.0], "pan": [(0.5, 0.5)] * 3, "ease": _E}},  # 35  s58-59 home in 1937; the Straits Chinese China Relief Fund (22.0s)
    {"img": "LIMX", **{"type": "cover", "title": "Lim Boon Keng, the Xiamen portrait", "zoom": [1.0, 1.06, 1.12], "pan": [(0.5, 0.5)] * 3, "ease": _E}},  # 36  s60 the Occupation: pressured to head the Oversea Chinese Association (14.6s)
    {"img": "LIM30", **{"type": "cover", "title": "Lim Boon Keng in the 1930s", "zoom": [1.12, 1.06, 1.0], "pan": [(0.35, 0.5)] * 3, "ease": _E}},  # 37  s61 coerced: the refusal, Grace made to kneel, the figurehead role, the feigned drunkenness (21.4s)
    {"img": "LIMX", **{"type": "cover", "title": "Lim Boon Keng, the Xiamen portrait", "zoom": [1.0, 1.06, 1.12], "pan": [(0.5, 0.5)] * 3, "ease": _E}},  # 38  s62-64 the levy fell short, and he said so: 'We never told a lie' - 'then die we will' (15.2s)
    {"img": "LIM30", **{"type": "cover", "title": "Lim Boon Keng in the 1930s", "zoom": [1.12, 1.06, 1.0], "pan": [(0.65, 0.5)] * 3, "ease": _E}},  # 39  s65 part of the sum raised; the balance a loan from the Yokohama Specie Bank (6.5s)
    {"img": "LIMX", **{"type": "cover", "title": "Lim Boon Keng, the Xiamen portrait", "zoom": [1.0, 1.06, 1.12], "pan": [(0.5, 0.4)] * 3, "ease": _E}},  # 40  s66 from 1937: 1 Paterson Hill, an attap-roofed mansion (8.1s)
    {"img": "LIM30", **{"type": "cover", "title": "Lim Boon Keng in the 1930s", "zoom": [1.12, 1.06, 1.0], "pan": [(0.5, 0.5)] * 3, "ease": _E}},  # 41  s67 the house filled with relatives and dependants: his own 'kampong' (19.2s)
    {"img": "LIMX", **{"type": "cover", "title": "Lim Boon Keng, the Xiamen portrait", "zoom": [1.0, 1.06, 1.12], "pan": [(0.5, 0.5)] * 3, "ease": _E}},  # 42  s68-69 retired after the war; the last decade a blank in the record (16.1s)
    {"img": "GRAVE", **{"type": "cover", "title": "His tombstone at Bidadari Memorial Garden", "zoom": [1.12, 1.06, 1.0], "pan": [(0.35, 0.5)] * 3, "ease": _E}},  # 43  s70 died at home, 1 January 1957: Grace, six children, Stella Kon among the descendants (16.2s)
    {"img": "GATE", **{"type": "cover", "title": "The gate of Bidadari Cemetery", "zoom": [1.0, 1.06, 1.12], "pan": [(0.5, 0.5)] * 3, "ease": _E}},  # 44  s71 Bidadari cleared in the 2000s; the tombstone kept in the Memorial Garden (17.1s)
    {"img": "MRT", **{"type": "cover", "title": "Boon Keng MRT station", "zoom": [1.12, 1.06, 1.0], "pan": [(0.65, 0.5)] * 3, "ease": _E}},  # 45  s72-73 posterity kept his name in two public places; the first is Boon Keng Road (8.1s)
    {"img": "EXIT", **{"type": "cover", "title": "Boon Keng MRT, Exit A", "zoom": [1.0, 1.06, 1.12], "pan": [(0.5, 0.4)] * 3, "ease": _E}},  # 46  s74 the second is the station beneath it: NE9, opened 20 June 2003 (13.1s)
    {"img": "MRT", **{"type": "cover", "title": "Boon Keng MRT station", "zoom": [1.12, 1.06, 1.0], "pan": [(0.5, 0.5)] * 3, "ease": _E}},  # 47  s75 Lee Kuan Yew, 2004: a role model of biculturalism (names Lee: the station, no portrait) (17.9s)
    {"img": "LIM30", **{"type": "cover", "title": "Lim Boon Keng in the 1930s", "zoom": [1.0, 1.06, 1.12], "pan": [(0.5, 0.5)] * 3, "ease": _E}},  # 48  s76-77 the commuters get the name without the life; what this one did (18.1s)
    {"img": "EXIT", **{"type": "cover", "title": "Boon Keng MRT, Exit A", "zoom": [1.12, 1.06, 1.0], "pan": [(0.35, 0.5)] * 3, "ease": _E}},  # 49  s78 the bigger story: stations named after roads, roads after half-forgotten men (8.5s)
    {"img": "LIM30", **{"type": "cover", "title": "Lim Boon Keng in the 1930s", "zoom": [1.0, 1.06, 1.12], "pan": [(0.5, 0.5)] * 3, "ease": _E}},  # 50  s79-80 his name survives where his work was aimed; the gap is the most lesser-known thing of all (21.6s)
]

SCHEDULE = [
    (0.000, 0), (14.300, 1), (38.950, 2), (49.050, 3), (69.875, 4), (91.025, 5),
    (106.650, 6), (124.625, 7), (136.250, 8), (152.650, 9), (170.075, 10), (190.000, 11),
    (199.850, 12), (211.825, 13), (236.575, 14), (257.525, 15), (277.000, 16), (291.775, 17),
    (313.350, 18), (331.825, 19), (352.375, 20), (371.875, 21), (390.400, 22), (400.050, 23),
    (423.475, 24), (441.125, 25), (455.150, 26), (471.850, 27), (491.100, 28), (511.350, 29),
    (528.575, 30), (552.075, 31), (573.875, 32), (593.900, 33), (606.750, 34), (621.500, 35),
    (643.475, 36), (658.050, 37), (679.500, 38), (694.725, 39), (701.225, 40), (709.300, 41),
    (728.525, 42), (744.650, 43), (760.875, 44), (777.950, 45), (786.000, 46), (799.050, 47),
    (816.950, 48), (835.075, 49), (843.550, 50),
]
TOTAL_DURATION = 865.17
TIMING_JSON = "audio/lim-boon-keng-the-reformer-whose-name-is-now-an-mrt-station.timing.json"

# The avatar presenter, cartoon with motion: corner bubble for the first and last 30 s.
AVATAR = {"ranges": [(0, 30), (-30, None)], "motion": True}
