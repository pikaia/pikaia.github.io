"""Short config for the Eu Tong Sen post - a synopsis re-cut.

Built with: python scripts/build_short_audio.py eu-tong-sen-the-eu-yan-sang-king-whose-name-is-on-the-street 0,6,10,18,29,34,39,52,59,61,74,79,85
(13 sentences, 177.875s - under the 3-minute Shorts ceiling
with margin, and well over TikTok's 1-minute floor.)

The post's points, and the sentences that carry each:
1. The founding: Eu Kong's 1879 Gopeng medicine shop, for
   the opium-addicted coolies of the Kinta Valley. (s6)
2. The harder edge: the 1882 opium tax farm financed the
   tin mines and the medicine business. (s10)
3. The son rebuilt it: prospecting from 1898 to 11 mines
   and the King of Tin by 1908. (s18)
4. Singapore: the chain reaches 265-271 South Bridge Road
   in 1910, Bidwell's shophouses. (s29)
5. The street: Wayang Street renamed Eu Tong Sen Street
   in 1919, in his lifetime. (s34)
6. The Majestic: his Cantonese opera house of 1927 at
   number 80. (s39)
7. The name on the hill: a Raffles College hostel took
   his name, the Eu Tong Sen Building. (s52)
8. The end: death at Sirmio on 11 May 1941, and he never
   returned to Singapore. (s59, s61)
9. The return of the firm: Richard Eu's 1993 buyback,
   reunification and the SGX listing. (s74)
10. Today: Rohto and Mitsui buy in, June 2024; the family
    keeps about 10 per cent and the chair. (s79)
11. The close: the smallest thing the family built, one
    1879 medicine shop, still open 147 years on. (s85)

Every slide is letterboxed and carries its photo title,
as in the main config. The pool's only portrait is Eu
Tong Sen himself, under the King of Tin sentence, which
is his own.
"""

WIDTH, HEIGHT = 1080, 1920

IMAGES = {
    "YUEHWA25": "https://upload.wikimedia.org/wikipedia/commons/1/15/Yue_Hwa_Building%2C_Singapore%2C_2025_%2801%29.jpg",
    "GOPENG": "https://thumb.wikimedia.org/wikipedia/commons/thumb/4/40/KITLV_-_79993_-_Kleingrothe%2C_C.J._-_Medan_-_Gopeng_in_Ipoh%2C_Malaysia_-_circa_1910.tif/1280px-KITLV_-_79993_-_Kleingrothe%2C_C.J._-_Medan_-_Gopeng_in_Ipoh%2C_Malaysia_-_circa_1910.tif.jpg",
    "PORTRAIT": "https://upload.wikimedia.org/wikipedia/commons/3/3a/Eu_Tong_Sen.jpg",
    "SBR23": "https://upload.wikimedia.org/wikipedia/commons/c/c4/271_South_Bridge_Road_Singapore_%28old_Eu_Yan_Sang_building%29_2023_--_01.jpg",
    "DRAGON": "https://upload.wikimedia.org/wikipedia/commons/a/a7/Chinese_New_Year_dragon_decoration_along_Eu_Tong_Sen_Street%2C_Singapore_-_20120116.jpg",
    "MAJ18": "https://upload.wikimedia.org/wikipedia/commons/0/0e/The_Majestic%2C_Singapore%2C_2018_%2801%29.jpg",
    "NUS": "https://upload.wikimedia.org/wikipedia/commons/8/85/Eu_Tong_Sen_Building%2C_Block_B_and_Upper_Quadrangle%2C_Faculty_of_Law%2C_National_University_of_Singapore.jpg",
    "SCHOOL": "https://upload.wikimedia.org/wikipedia/commons/0/0d/HK_PloverCoveEuTongSenSchool.jpg",
    "GEORGE": "https://upload.wikimedia.org/wikipedia/commons/d/d3/Eu_Yan_Sang_George_Town_01.jpg",
    "STREET25": "https://upload.wikimedia.org/wikipedia/commons/2/20/Eu_Tong_Sen_Street%2C_Singapore%2C_2025_%2801%29.jpg",
    "NIGHT14": "https://upload.wikimedia.org/wikipedia/commons/5/5d/Eu_Tong_Sen_Street_%2B_New_Bridge_Road%2C_Singapore%2C_2014_%2801%29.JPG",
    "MAJ05": "https://upload.wikimedia.org/wikipedia/commons/2/20/The_Majestic%2C_Dec_05.JPG",
    "MAJ25": "https://upload.wikimedia.org/wikipedia/commons/3/35/Chinatown-SG_-_The_Majestic_%282025%29_-_img_01.jpg",
    "YUEHWA05": "https://upload.wikimedia.org/wikipedia/commons/1/15/Yue_Hwa_Building%2C_Dec_05.JPG",
    "YUEHWASTORE": "https://upload.wikimedia.org/wikipedia/commons/3/37/Yue_Hwa_Chinese_Products_Singapore_Store.jpg",
    "SBR25": "https://upload.wikimedia.org/wikipedia/commons/6/6f/Chinatown-SG_-_Old_Eu_Yan_Sang_Building%2C_South_Bridge_Road%2C_Singapore_%282025%29_-_img_01.jpg",
    "HQ10": "https://upload.wikimedia.org/wikipedia/commons/4/44/Eu_Yan_Sang_Headquarters_2010.jpg",
    "HKCENTRAL": "https://upload.wikimedia.org/wikipedia/commons/6/6e/Eu_Yan_Sang_20071110.jpg",
    "SSP": "https://upload.wikimedia.org/wikipedia/commons/8/85/EuYanSang_Shamshuipo.jpg",
    "SUZHOU": "https://upload.wikimedia.org/wikipedia/commons/2/23/Eu_Yan_Sang_counter_at_Jiuguang_Department_Store%2C_Suzhou.jpg",
}

# Every image is captioned in the post or its gallery.
CREDITS = {}

# The main video's thumbnail grid, re-panned for tall cells.
THUMBNAIL = [
    {"img": "PORTRAIT", "pan": (0.5, 0.5)},
    {"img": "DRAGON", "pan": (0.5, 0.5)},
    {"img": "MAJ25", "pan": (0.5, 0.5)},
    {"img": "GEORGE", "pan": (0.5, 0.5)},
]

_E = "ease-in-out"
_LB = {"type": "letterbox", "zoom": [1.0, 1.03, 1.06], "pan": [(0.5, 0.5)] * 3, "ease": _E}

SLIDES = [
    {"img": "DRAGON", **_LB, "title": "Eu Tong Sen Street, Chinese New Year 2012"},   # s0 title (4.70s),
    {"img": "GOPENG", **_LB, "title": "Gopeng, the first Yan Sang shop, c. 1910"},   # s6 1879: Eu Kong opens the Gopeng shop for opium-addicted coolies (13.53s),
    {"img": "GEORGE", **_LB, "title": "A Eu Yan Sang shop in George Town, 2026"},   # s10 the harder edge: the opium tax farm financed the business (18.55s),
    {"img": "PORTRAIT", **_LB, "title": "Eu Tong Sen (1877-1941)"},   # s18 the son rebuilt it: 11 mines by 1908, the King of Tin (11.97s),
    {"img": "SBR23", **_LB, "title": "The Eu Yan Sang Building, 2023"},   # s29 Singapore 1910: the South Bridge Road building (15.65s),
    {"img": "DRAGON", **_LB, "title": "Eu Tong Sen Street, Chinese New Year 2012"},   # s34 1919: the street renamed for him in his lifetime (16.07s),
    {"img": "MAJ25", **_LB, "title": "The Majestic in 2025"},   # s39 1927: the Majestic, his Cantonese opera house (17.43s),
    {"img": "NUS", **_LB, "title": "The Eu Tong Sen Building at Bukit Timah"},   # s52 the Eu Tong Sen Building at Raffles College (10.60s),
    {"img": "HKCENTRAL", **_LB, "title": "A Eu Yan Sang shop in Hong Kong, 2007"},   # s59 11 May 1941: he dies at Sirmio, Hong Kong (7.97s),
    {"img": "STREET25", **_LB, "title": "Eu Tong Sen Street in 2025"},   # s61 he never returned to Singapore (2.98s),
    {"img": "HQ10", **_LB, "title": "South Bridge Road headquarters, 2010"},   # s74 1993: Richard Eu buys the business back (25.32s),
    {"img": "SUZHOU", **_LB, "title": "A Eu Yan Sang counter in Suzhou, 2021"},   # s79 2024: Rohto and Mitsui buy in; the family keeps its stake (16.00s),
    {"img": "GEORGE", **_LB, "title": "A Eu Yan Sang shop in George Town, 2026"},   # s85 one 1879 medicine shop, still open 147 years on (17.10s),
]
SCHEDULE = [
    (0.000, 0), (4.700, 1), (18.225, 2), (36.775, 3), (48.750, 4), (64.400, 5),
    (80.475, 6), (97.900, 7), (108.500, 8), (116.475, 9), (119.450, 10), (144.775, 11),
    (160.775, 12)
]
TOTAL_DURATION = 177.875
TIMING_JSON = "audio/eu-tong-sen-the-eu-yan-sang-king-whose-name-is-on-the-street-short.timing.json"

BURN_CAPTIONS = True
CAPTION_FONT_RATIO = 0.032
CAPTION_MAX_WIDTH_FRAC = 0.86
CAPTION_Y_FRAC = 0.70

# The avatar presenter, cartoon with motion: corner bubble for the first and last 30 s.
AVATAR = {"ranges": [(0, 30), (-30, None)], "motion": True}
