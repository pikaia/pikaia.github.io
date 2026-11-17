"""Short config for the Lim Boon Keng post - a synopsis re-cut.

Built with: python scripts/build_short_audio.py lim-boon-keng-the-reformer-whose-name-is-now-an-mrt-station 1,12,13,20,23,26,36,46,53,54,56,63,64,74,80
(15 sentences, 172.25s - under the 3-minute Shorts ceiling
with margin, and well over TikTok's 1-minute floor.)

The post's points, and the sentences that carry each:
1. The hook: thousands tap in at Boon Keng station every
   morning, and the name is a man's. (s1)
2. The scholarship: Song Ong Siang topped the Queen's
   Scholarship exam in 1886 and 1887 and was disqualified
   both times as under sixteen, so the award fell to the
   runner-up - Lim, the first Chinese Queen's Scholar.
   (s12, s13)
3. The doctor: in his practice he treated the poor free
   of charge. (s20)
4. The signature cause: he founded the Anti-Opium Society
   and opened an Opium Refuge for addicts. (s23)
5. The lawmaker: appointed to the Legislative Council in
   1895, aged twenty-six. (s26)
6. The school: in 1899 he co-founded the Singapore Chinese
   Girls' School. (s36)
7. The banks: he helped establish all three of the era's
   Hokkien banks, the ones that later formed OCBC. (s46)
8. China: personal physician and secretary to Sun Yat-sen
   in 1911 (s53); then the 1921 call (s54) - president of
   Xiamen University for sixteen years, without salary. (s56)
9. The Occupation: when the levy fell short he faced the
   authorities with it - "We never told a lie... If we are
   unable to pay, then die we will." (s63, s64)
10. The name today: Boon Keng MRT station, NE9, opened
    20 June 2003 (s74); and the gap between the name
    everyone uses and the life nobody remembers. (s80)

Every slide is letterboxed and carries its photo title, as in
the main config. Named-person rule as in the main config.
"""

WIDTH, HEIGHT = 1080, 1920

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

# The main video's thumbnail grid, re-panned for tall cells.
THUMBNAIL = [
    {"img": "LIM30", "pan": (0.5, 0.5)},
    {"img": "SONG", "pan": (0.5, 0.5)},
    {"img": "SCGS", "pan": (0.5, 0.5)},
    {"img": "EXIT", "pan": (0.5, 0.5)},
]

_E = "ease-in-out"
_LB = {"type": "letterbox", "zoom": [1.0, 1.03, 1.06], "pan": [(0.5, 0.5)] * 3, "ease": _E}

SLIDES = [
    {"img": "EXIT", **_LB, "title": "Boon Keng MRT, Exit A"},   # s1 the hook: thousands tap in at his station daily (9.2s)
    {"img": "SONG", **_LB, "title": "Song Ong Siang"},   # s12 Song topped the exam in 1886 and 1887, underage both times (names Song: his portrait) (12.1s)
    {"img": "LIM30", **_LB, "title": "Lim Boon Keng in the 1930s"},   # s13 so the scholarship went to the runner-up: the first Chinese Queen's Scholar (5.9s)
    {"img": "LIMX", **_LB, "title": "Lim Boon Keng, the Xiamen portrait"},   # s20 'offered free treatment to patients who were poor' (9.8s)
    {"img": "LIM30", **_LB, "title": "Lim Boon Keng in the 1930s"},   # s23 the Anti-Opium Society and the Opium Refuge (18.2s)
    {"img": "LIMX", **_LB, "title": "Lim Boon Keng, the Xiamen portrait"},   # s26 the Legislative Council at twenty-six (9.0s)
    {"img": "SCGS", **_LB, "title": "Singapore Chinese Girls' School today"},   # s36 the Singapore Chinese Girls' School founded, 1899 (18.5s)
    {"img": "BOOK", **_LB, "title": "Song's One Hundred Years' History, 1923"},   # s46 all three Hokkien banks (names Lim Peng Siang: the book) (17.3s)
    {"img": "SUN", **_LB, "title": "Sun Yat-sen, 1910"},   # s53 Sun Yat-sen's personal physician; the health posts of 1911 (names Sun: his portrait) (21.8s)
    {"img": "LIMX", **_LB, "title": "Lim Boon Keng, the Xiamen portrait"},   # s54 in 1921, the call that took him away for sixteen years (6.4s)
    {"img": "WENQING", **_LB, "title": "His statue at Xiamen University"},   # s56 president of Xiamen University 1921-1937, without salary (12.8s)
    {"img": "LIM30", **_LB, "title": "Lim Boon Keng in the 1930s"},   # s63 'We never told a lie' - his words to the authorities, recalled in 1947 (6.9s)
    {"img": "LIMX", **_LB, "title": "Lim Boon Keng, the Xiamen portrait"},   # s64 'If we are unable to pay, then die we will.' (3.6s)
    {"img": "MRT", **_LB, "title": "Boon Keng MRT station"},   # s74 the station beneath the road: NE9, opened 20 June 2003 (13.1s)
    {"img": "LIM30", **_LB, "title": "Lim Boon Keng in the 1930s"},   # s80 the gap between the name everyone uses and the life nobody remembers (7.7s)
]
SCHEDULE = [
    (0.000, 0), (9.150, 1), (21.200, 2), (27.125, 3), (36.975, 4), (55.150, 5),
    (64.150, 6), (82.675, 7), (100.000, 8), (121.800, 9), (128.175, 10), (141.025, 11),
    (147.925, 12), (151.500, 13), (164.550, 14),
]
TOTAL_DURATION = 172.25
TIMING_JSON = "audio/lim-boon-keng-the-reformer-whose-name-is-now-an-mrt-station-short.timing.json"

BURN_CAPTIONS = True
CAPTION_FONT_RATIO = 0.032
CAPTION_MAX_WIDTH_FRAC = 0.86
CAPTION_Y_FRAC = 0.70

# The avatar presenter, cartoon with motion: corner bubble for the first and last 30 s.
AVATAR = {"ranges": [(0, 30), (-30, None)], "motion": True}
