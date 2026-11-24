"""Video config for the Eu Tong Sen post.

The pool is all twenty pictures from the post and its
gallery: the Yue Hwa Building in 2025 and 2005 and its
2010 storefront, Kleingrothe's Gopeng of about 1910, the
portrait of Eu Tong Sen, the South Bridge Road building
in 2023, in 2025 and as the 2010 headquarters, Chris's
own pick - the Chinese New Year dragon over Eu Tong Sen
Street with the street sign below - the street in 2025
and at night in 2014, the Majestic in 2005, 2018 and
2025, the Eu Tong Sen Building at Bukit Timah, the Shuen
Wan school in Tai Po, and the firm's shops in George
Town, Central, Sham Shui Po and Suzhou. Twenty pictures
for just under seventeen minutes: images recur at new
story beats with varied pans and alternating zoom
direction, never twice in a row.

Named-person audit: the pool's only portrait is Eu Tong
Sen himself, and it sits only under sentences about him.
Sentences naming Eu Kong, Eu Keng Chee or Richard Eu
carry shop or building photographs, never the portrait.
Named-place audit: the South Bridge Road photographs sit
under the South Bridge Road sentences, the Majestic
photographs under the Majestic sentences, the Yue Hwa
photographs under the Nam Tin passage, the Bukit Timah
photograph under the Raffles College sentences, and the
school photograph under the Shuen Wan sentences. The
remittance sentence names Hong Kong among its agent
cities and carries the Central shop photograph.

Every slide carries its discreet photo title (standing
rule, Chris, 2026-11-11): the short form of its image's
post/gallery caption, drawn small in the top corner on a
soft dark backing for the slide's whole run.

67 slides, 1006.900s. No slide over 30s; the longest is the
Hong Kong move and mansions at 29.30s. Narration: Kokoro
with the OpenVoice clone. Pronunciation overrides for
the post's names filed 2026-11-22, NOT ear-verified yet.
AVATAR: first and last 30s, cartoon with motion.
"""

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

# The channel's 2x2 thumbnail grid, in story order: the
# man, the street that took his name, his theatre, his
# firm's shop still trading today.
THUMBNAIL = [
    {"img": "PORTRAIT", "pan": (0.5, 0.5)},
    {"img": "DRAGON", "pan": (0.5, 0.5)},
    {"img": "MAJ25", "pan": (0.5, 0.5)},
    {"img": "GEORGE", "pan": (0.5, 0.5)},
]

_E = "ease-in-out"

SLIDES = [
    {"img": "DRAGON", **{"type": "cover", "title": "Eu Tong Sen Street under a Chinese New Year dragon, 2012", "zoom": [1.0, 1.06, 1.12], "pan": [(0.50, 0.50)] * 3, "ease": _E}},  # 0  s0 title (4.70s),
    {"img": "STREET25", **{"type": "cover", "title": "Eu Tong Sen Street in 2025", "zoom": [1.12, 1.06, 1.0], "pan": [(0.35, 0.50)] * 3, "ease": _E}},  # 1  s1 the street today, the name unthought-of (8.28s),
    {"img": "PORTRAIT", **{"type": "cover", "title": "Eu Tong Sen (1877-1941)", "zoom": [1.0, 1.06, 1.12], "pan": [(0.65, 0.50)] * 3, "ease": _E}},  # 2  s2 the man: a Penang-born tin magnate, died Hong Kong 1941 (12.95s),
    {"img": "GEORGE", **{"type": "cover", "title": "A Eu Yan Sang shop in George Town, Penang, 2026", "zoom": [1.12, 1.06, 1.0], "pan": [(0.50, 0.40)] * 3, "ease": _E}},  # 3  s3 the firm at 147 years, still trading (17.85s),
    {"img": "NIGHT14", **{"type": "cover", "title": "Eu Tong Sen Street and New Bridge Road at night, 2014", "zoom": [1.0, 1.06, 1.12], "pan": [(0.50, 0.50)] * 3, "ease": _E}},  # 4  s4 the story framed: the man, the empire, the name (7.83s),
    {"img": "GOPENG", **{"type": "cover", "title": "Gopeng, the tin town of the first Yan Sang shop, c. 1910", "zoom": [1.12, 1.06, 1.0], "pan": [(0.35, 0.50)] * 3, "ease": _E}},  # 5  s5-6 Eu Kong: Foshan to Penang to Gopeng, the 1879 shop (24.12s),
    {"img": "GEORGE", **{"type": "cover", "title": "A Eu Yan Sang shop in George Town, Penang, 2026", "zoom": [1.0, 1.06, 1.12], "pan": [(0.65, 0.50)] * 3, "ease": _E}},  # 6  s7 the Kinta Valley coolies; Yan Sang, caring for mankind (14.43s),
    {"img": "HKCENTRAL", **{"type": "cover", "title": "A Eu Yan Sang shop in Central, Hong Kong, 2007", "zoom": [1.12, 1.06, 1.0], "pan": [(0.50, 0.40)] * 3, "ease": _E}},  # 7  s8 the company's own telling: the act of care (6.85s),
    {"img": "GOPENG", **{"type": "cover", "title": "Gopeng, the tin town of the first Yan Sang shop, c. 1910", "zoom": [1.0, 1.06, 1.12], "pan": [(0.50, 0.50)] * 3, "ease": _E}},  # 8  s9-10 the harder edge: the 1882 Batang Padang tax farm (24.70s),
    {"img": "SSP", **{"type": "cover", "title": "A Eu Yan Sang shopfront in Sham Shui Po, Hong Kong", "zoom": [1.12, 1.06, 1.0], "pan": [(0.35, 0.50)] * 3, "ease": _E}},  # 9  s11-12 two sides of one enterprise; both belong in the story (9.65s),
    {"img": "PORTRAIT", **{"type": "cover", "title": "Eu Tong Sen (1877-1941)", "zoom": [1.0, 1.06, 1.12], "pan": [(0.65, 0.50)] * 3, "ease": _E}},  # 10  s13-14 born Penang 1877; Foshan at four, the opera love (21.27s),
    {"img": "GOPENG", **{"type": "cover", "title": "Gopeng, the tin town of the first Yan Sang shop, c. 1910", "zoom": [1.12, 1.06, 1.0], "pan": [(0.50, 0.40)] * 3, "ease": _E}},  # 11  s15-16 father dead 1890; the depleted business; the rock face (21.83s),
    {"img": "PORTRAIT", **{"type": "cover", "title": "Eu Tong Sen (1877-1941)", "zoom": [1.0, 1.06, 1.12], "pan": [(0.50, 0.50)] * 3, "ease": _E}},  # 12  s17-18 prospecting on elephant back; 11 mines, King of Tin (24.60s),
    {"img": "GOPENG", **{"type": "cover", "title": "Gopeng, the tin town of the first Yan Sang shop, c. 1910", "zoom": [1.12, 1.06, 1.0], "pan": [(0.35, 0.50)] * 3, "ease": _E}},  # 13  s19-20 hydraulic machinery, foundry, smelting; rubber acres (20.02s),
    {"img": "GEORGE", **{"type": "cover", "title": "A Eu Yan Sang shop in George Town, Penang, 2026", "zoom": [1.0, 1.06, 1.12], "pan": [(0.65, 0.50)] * 3, "ease": _E}},  # 14  s21 the shops famous, but not the most profitable (5.67s),
    {"img": "HKCENTRAL", **{"type": "cover", "title": "A Eu Yan Sang shop in Central, Hong Kong, 2007", "zoom": [1.12, 1.06, 1.0], "pan": [(0.50, 0.40)] * 3, "ease": _E}},  # 15  s22 remittances: Ipoh 1906, agents in Hong Kong and Canton (26.95s),
    {"img": "PORTRAIT", **{"type": "cover", "title": "Eu Tong Sen (1877-1941)", "zoom": [1.0, 1.06, 1.12], "pan": [(0.50, 0.50)] * 3, "ease": _E}},  # 16  s23 Lee Wah Bank, 1920, his family's until 1973 (14.00s),
    {"img": "GOPENG", **{"type": "cover", "title": "Gopeng, the tin town of the first Yan Sang shop, c. 1910", "zoom": [1.12, 1.06, 1.0], "pan": [(0.35, 0.50)] * 3, "ease": _E}},  # 17  s24-25 the opium paradox: farm shares and the Anti-Opium Society (23.45s),
    {"img": "PORTRAIT", **{"type": "cover", "title": "Eu Tong Sen (1877-1941)", "zoom": [1.0, 1.06, 1.12], "pan": [(0.65, 0.50)] * 3, "ease": _E}},  # 18  s26-27 his justification; the record carries both (18.38s),
    {"img": "HKCENTRAL", **{"type": "cover", "title": "A Eu Yan Sang shop in Central, Hong Kong, 2007", "zoom": [1.12, 1.06, 1.0], "pan": [(0.50, 0.40)] * 3, "ease": _E}},  # 19  s28 the chain spreads: Hong Kong, first overseas, 1909 (11.12s),
    {"img": "SBR23", **{"type": "cover", "title": "The Eu Yan Sang Building, South Bridge Road, 2023", "zoom": [1.0, 1.06, 1.12], "pan": [(0.50, 0.50)] * 3, "ease": _E}},  # 20  s29 Singapore 1910: 265-271 South Bridge Road, Bidwell's row (15.65s),
    {"img": "HQ10", **{"type": "cover", "title": "The South Bridge Road building as headquarters, 2010", "zoom": [1.12, 1.06, 1.0], "pan": [(0.35, 0.50)] * 3, "ease": _E}},  # 21  s30 three parts; Yan Sang becomes Eu Yan Sang (14.78s),
    {"img": "STREET25", **{"type": "cover", "title": "Eu Tong Sen Street in 2025", "zoom": [1.0, 1.06, 1.12], "pan": [(0.65, 0.50)] * 3, "ease": _E}},  # 22  s31 1910: headquarters and the man move to Singapore (6.17s),
    {"img": "DRAGON", **{"type": "cover", "title": "Eu Tong Sen Street under a Chinese New Year dragon, 2012", "zoom": [1.12, 1.06, 1.0], "pan": [(0.50, 0.40)] * 3, "ease": _E}},  # 23  s32 Wayang Street, named for its opera theatres (8.40s),
    {"img": "STREET25", **{"type": "cover", "title": "Eu Tong Sen Street in 2025", "zoom": [1.0, 1.06, 1.12], "pan": [(0.50, 0.50)] * 3, "ease": _E}},  # 24  s33 he bought property along it (6.62s),
    {"img": "DRAGON", **{"type": "cover", "title": "Eu Tong Sen Street under a Chinese New Year dragon, 2012", "zoom": [1.12, 1.06, 1.0], "pan": [(0.35, 0.50)] * 3, "ease": _E}},  # 25  s34 1918 improvements; renamed Eu Tong Sen Street, 1919 (16.07s),
    {"img": "NIGHT14", **{"type": "cover", "title": "Eu Tong Sen Street and New Bridge Road at night, 2014", "zoom": [1.0, 1.06, 1.12], "pan": [(0.65, 0.50)] * 3, "ease": _E}},  # 26  s35 two explanations for the honour, both may be true (6.05s),
    {"img": "PORTRAIT", **{"type": "cover", "title": "Eu Tong Sen (1877-1941)", "zoom": [1.12, 1.06, 1.0], "pan": [(0.50, 0.40)] * 3, "ease": _E}},  # 27  s36 the First World War gift: a tank and a fighter plane (15.18s),
    {"img": "MAJ18", **{"type": "cover", "title": "The Majestic at 80 Eu Tong Sen Street, 2018", "zoom": [1.0, 1.06, 1.12], "pan": [(0.50, 0.50)] * 3, "ease": _E}},  # 28  s37 he rebuilt it and bought its two opera theatres (11.07s),
    {"img": "MAJ05", **{"type": "cover", "title": "The Majestic Theatre in 2005", "zoom": [1.12, 1.06, 1.0], "pan": [(0.35, 0.50)] * 3, "ease": _E}},  # 29  s38 the eighth-wife anecdote, left as the story that is told (13.20s),
    {"img": "MAJ25", **{"type": "cover", "title": "The Majestic in 2025", "zoom": [1.0, 1.06, 1.12], "pan": [(0.65, 0.50)] * 3, "ease": _E}},  # 30  s39 1927: the Majestic rises at number 80 (17.43s),
    {"img": "MAJ18", **{"type": "cover", "title": "The Majestic at 80 Eu Tong Sen Street, 2018", "zoom": [1.12, 1.06, 1.0], "pan": [(0.50, 0.40)] * 3, "ease": _E}},  # 31  s40 built for his wife, refused an opera elsewhere (9.72s),
    {"img": "MAJ05", **{"type": "cover", "title": "The Majestic Theatre in 2005", "zoom": [1.0, 1.06, 1.12], "pan": [(0.50, 0.50)] * 3, "ease": _E}},  # 32  s41 the Majestic survives beside People's Park Complex (12.55s),
    {"img": "YUEHWA25", **{"type": "cover", "title": "The Yue Hwa Building, Eu Tong Sen Street, 2025", "zoom": [1.12, 1.06, 1.0], "pan": [(0.35, 0.50)] * 3, "ease": _E}},  # 33  s42 the other 1927 landmark: Nam Tin, the Great Southern Hotel (19.50s),
    {"img": "YUEHWASTORE", **{"type": "cover", "title": "The Yue Hwa store frontage, 2010", "zoom": [1.0, 1.06, 1.12], "pan": [(0.65, 0.50)] * 3, "ease": _E}},  # 34  s43-44 today the Yue Hwa Building; was it Eu's building? (9.78s),
    {"img": "YUEHWA05", **{"type": "cover", "title": "The Yue Hwa Building in 2005", "zoom": [1.12, 1.06, 1.0], "pan": [(0.50, 0.40)] * 3, "ease": _E}},  # 35  s45-46 the Board's biography and BiblioAsia count it his (19.08s),
    {"img": "YUEHWA25", **{"type": "cover", "title": "The Yue Hwa Building, Eu Tong Sen Street, 2025", "zoom": [1.0, 1.06, 1.12], "pan": [(0.50, 0.50)] * 3, "ease": _E}},  # 36  s47 the hotel's own history and Roots say Lum Chang (11.20s),
    {"img": "MAJ18", **{"type": "cover", "title": "The Majestic at 80 Eu Tong Sen Street, 2018", "zoom": [1.12, 1.06, 1.0], "pan": [(0.35, 0.50)] * 3, "ease": _E}},  # 37  s48 the Majestic's attribution is solid; this one is not (8.93s),
    {"img": "YUEHWA05", **{"type": "cover", "title": "The Yue Hwa Building in 2005", "zoom": [1.0, 1.06, 1.12], "pan": [(0.65, 0.50)] * 3, "ease": _E}},  # 38  s49 the documented later life: sold 1993, reopened 1996 (21.57s),
    {"img": "NUS", **{"type": "cover", "title": "The Eu Tong Sen Building at Bukit Timah", "zoom": [1.12, 1.06, 1.0], "pan": [(0.50, 0.40)] * 3, "ease": _E}},  # 39  s50-51 Raffles College: his contribution was $100,000 (20.53s),
    {"img": "PORTRAIT", **{"type": "cover", "title": "Eu Tong Sen (1877-1941)", "zoom": [1.0, 1.06, 1.12], "pan": [(0.50, 0.50)] * 3, "ease": _E}},  # 40  s52 a hostel around the Upper Quadrangle took his name (10.60s),
    {"img": "NUS", **{"type": "cover", "title": "The Eu Tong Sen Building at Bukit Timah", "zoom": [1.12, 1.06, 1.0], "pan": [(0.35, 0.50)] * 3, "ease": _E}},  # 41  s53 gazetted 2009; the law faculty's entrance until 2026 (18.52s),
    {"img": "HKCENTRAL", **{"type": "cover", "title": "A Eu Yan Sang shop in Central, Hong Kong, 2007", "zoom": [1.0, 1.06, 1.12], "pan": [(0.65, 0.50)] * 3, "ease": _E}},  # 42  s54 Hong Kong: $30,000 for the HKU gymnasium, 1936 (15.03s),
    {"img": "PORTRAIT", **{"type": "cover", "title": "Eu Tong Sen (1877-1941)", "zoom": [1.12, 1.06, 1.0], "pan": [(0.50, 0.40)] * 3, "ease": _E}},  # 43  s55 the $55,000 figure no HKU source supports (15.60s),
    {"img": "SSP", **{"type": "cover", "title": "A Eu Yan Sang shopfront in Sham Shui Po, Hong Kong", "zoom": [1.0, 1.06, 1.12], "pan": [(0.50, 0.50)] * 3, "ease": _E}},  # 44  s56-57 the late 1920s move to Hong Kong; three mansions (29.30s),
    {"img": "HKCENTRAL", **{"type": "cover", "title": "A Eu Yan Sang shop in Central, Hong Kong, 2007", "zoom": [1.12, 1.06, 1.0], "pan": [(0.35, 0.50)] * 3, "ease": _E}},  # 45  s58-59 Eu Keng Chee; death at Sirmio, 11 May 1941 (16.30s),
    {"img": "SSP", **{"type": "cover", "title": "A Eu Yan Sang shopfront in Sham Shui Po, Hong Kong", "zoom": [1.0, 1.06, 1.12], "pan": [(0.65, 0.50)] * 3, "ease": _E}},  # 46  s60-61 buried at Sirmio, moved to Tsuen Wan; never returned (15.22s),
    {"img": "SCHOOL", **{"type": "cover", "title": "The former Shuen Wan Eu Tong Sen School, Tai Po, 2015", "zoom": [1.12, 1.06, 1.0], "pan": [(0.50, 0.40)] * 3, "ease": _E}},  # 47  s62-63 the Shuen Wan school that bore his name until 1994 (15.55s),
    {"img": "HKCENTRAL", **{"type": "cover", "title": "A Eu Yan Sang shop in Central, Hong Kong, 2007", "zoom": [1.0, 1.06, 1.12], "pan": [(0.50, 0.50)] * 3, "ease": _E}},  # 48  s64-65 no source records why; dated 1950, a memorial (19.15s),
    {"img": "SCHOOL", **{"type": "cover", "title": "The former Shuen Wan Eu Tong Sen School, Tai Po, 2015", "zoom": [1.12, 1.06, 1.0], "pan": [(0.35, 0.50)] * 3, "ease": _E}},  # 49  s66 the site today: Good House transitional housing (13.97s),
    {"img": "GEORGE", **{"type": "cover", "title": "A Eu Yan Sang shop in George Town, Penang, 2026", "zoom": [1.0, 1.06, 1.12], "pan": [(0.65, 0.50)] * 3, "ease": _E}},  # 50  s67 what returned was not the man but the firm (4.25s),
    {"img": "PORTRAIT", **{"type": "cover", "title": "Eu Tong Sen (1877-1941)", "zoom": [1.12, 1.06, 1.0], "pan": [(0.50, 0.40)] * 3, "ease": _E}},  # 51  s68 the estate divided 13 ways; the empire sold off (14.00s),
    {"img": "HKCENTRAL", **{"type": "cover", "title": "A Eu Yan Sang shop in Central, Hong Kong, 2007", "zoom": [1.0, 1.06, 1.12], "pan": [(0.50, 0.50)] * 3, "ease": _E}},  # 52  s69-70 the split: Hong Kong firm, Singapore-Malaysia firm; Lee Wah gone (19.35s),
    {"img": "GEORGE", **{"type": "cover", "title": "A Eu Yan Sang shop in George Town, Penang, 2026", "zoom": [1.12, 1.06, 1.0], "pan": [(0.35, 0.50)] * 3, "ease": _E}},  # 53  s71-72 the second founder: Richard Eu, fourth generation (20.70s),
    {"img": "YUEHWA05", **{"type": "cover", "title": "The Yue Hwa Building in 2005", "zoom": [1.0, 1.06, 1.12], "pan": [(0.65, 0.50)] * 3, "ease": _E}},  # 54  s73 1990: the Lum Chang takeover of Eu Yan Sang Holdings (10.00s),
    {"img": "HQ10", **{"type": "cover", "title": "The South Bridge Road building as headquarters, 2010", "zoom": [1.12, 1.06, 1.0], "pan": [(0.50, 0.40)] * 3, "ease": _E}},  # 55  s74 1993: the buyback, reunification, the SGX listing (25.32s),
    {"img": "SBR25", **{"type": "cover", "title": "The old Eu Yan Sang Building, South Bridge Road, 2025", "zoom": [1.0, 1.06, 1.12], "pan": [(0.50, 0.50)] * 3, "ease": _E}},  # 56  s75 Tai Seng Drive 2013; the old building sold, reopened 2022 (18.43s),
    {"img": "SUZHOU", **{"type": "cover", "title": "A Eu Yan Sang counter in Suzhou, 2021", "zoom": [1.12, 1.06, 1.0], "pan": [(0.35, 0.50)] * 3, "ease": _E}},  # 57  s76 the milestones tell it tidier than the record (15.32s),
    {"img": "GEORGE", **{"type": "cover", "title": "A Eu Yan Sang shop in George Town, Penang, 2026", "zoom": [1.0, 1.06, 1.12], "pan": [(0.65, 0.50)] * 3, "ease": _E}},  # 58  s77-78 2016: taken private by Tower Capital, Temasek, the family (20.62s),
    {"img": "SUZHOU", **{"type": "cover", "title": "A Eu Yan Sang counter in Suzhou, 2021", "zoom": [1.12, 1.06, 1.0], "pan": [(0.50, 0.40)] * 3, "ease": _E}},  # 59  s79 June 2024: Rohto and Mitsui, an S$808 million valuation (16.00s),
    {"img": "HQ10", **{"type": "cover", "title": "The South Bridge Road building as headquarters, 2010", "zoom": [1.0, 1.06, 1.12], "pan": [(0.50, 0.50)] * 3, "ease": _E}},  # 60  s80 the family rolls over 10 per cent; Richard Eu still chairman (15.97s),
    {"img": "HKCENTRAL", **{"type": "cover", "title": "A Eu Yan Sang shop in Central, Hong Kong, 2007", "zoom": [1.12, 1.06, 1.0], "pan": [(0.35, 0.50)] * 3, "ease": _E}},  # 61  s81 170 outlets and 30 clinics; 43 stores in Singapore (15.32s),
    {"img": "SUZHOU", **{"type": "cover", "title": "A Eu Yan Sang counter in Suzhou, 2021", "zoom": [1.0, 1.06, 1.12], "pan": [(0.65, 0.50)] * 3, "ease": _E}},  # 62  s82 bird's nest and Bak Foong beside collagen and NMN (10.88s),
    {"img": "GEORGE", **{"type": "cover", "title": "A Eu Yan Sang shop in George Town, Penang, 2026", "zoom": [1.12, 1.06, 1.0], "pan": [(0.50, 0.40)] * 3, "ease": _E}},  # 63  s83 the 147th anniversary, October 2026; the 150th in 2029 (12.53s),
    {"img": "DRAGON", **{"type": "cover", "title": "Eu Tong Sen Street under a Chinese New Year dragon, 2012", "zoom": [1.0, 1.06, 1.12], "pan": [(0.50, 0.50)] * 3, "ease": _E}},  # 64  s84 the bigger story: the name on a street, a hostel, a school sign (16.60s),
    {"img": "GOPENG", **{"type": "cover", "title": "Gopeng, the tin town of the first Yan Sang shop, c. 1910", "zoom": [1.12, 1.06, 1.0], "pan": [(0.35, 0.50)] * 3, "ease": _E}},  # 65  s85 one Perak medicine shop of 1879, still open (17.10s),
    {"img": "GEORGE", **{"type": "cover", "title": "A Eu Yan Sang shop in George Town, Penang, 2026", "zoom": [1.0, 1.06, 1.12], "pan": [(0.65, 0.50)] * 3, "ease": _E}},  # 66  s86 the empire went; the shop endured (3.12s),
]

SCHEDULE = [
    (0.000, 0), (4.700, 1), (12.975, 2),
    (25.925, 3), (43.775, 4), (51.600, 5),
    (75.725, 6), (90.150, 7), (97.000, 8),
    (121.700, 9), (131.350, 10), (152.625, 11),
    (174.450, 12), (199.050, 13), (219.075, 14),
    (224.750, 15), (251.700, 16), (265.700, 17),
    (289.150, 18), (307.525, 19), (318.650, 20),
    (334.300, 21), (349.075, 22), (355.250, 23),
    (363.650, 24), (370.275, 25), (386.350, 26),
    (392.400, 27), (407.575, 28), (418.650, 29),
    (431.850, 30), (449.275, 31), (459.000, 32),
    (471.550, 33), (491.050, 34), (500.825, 35),
    (519.900, 36), (531.100, 37), (540.025, 38),
    (561.600, 39), (582.125, 40), (592.725, 41),
    (611.250, 42), (626.275, 43), (641.875, 44),
    (671.175, 45), (687.475, 46), (702.700, 47),
    (718.250, 48), (737.400, 49), (751.375, 50),
    (755.625, 51), (769.625, 52), (788.975, 53),
    (809.675, 54), (819.675, 55), (845.000, 56),
    (863.425, 57), (878.750, 58), (899.375, 59),
    (915.375, 60), (931.350, 61), (946.675, 62),
    (957.550, 63), (970.075, 64), (986.675, 65),
    (1003.775, 66)
]
TOTAL_DURATION = 1006.900
TIMING_JSON = "audio/eu-tong-sen-the-eu-yan-sang-king-whose-name-is-on-the-street.timing.json"

# The avatar presenter, cartoon with motion: corner bubble for the first and last 30 s.
AVATAR = {"ranges": [(0, 30), (-30, None)], "motion": True}
