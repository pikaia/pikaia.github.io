"""Video config for the Indian convicts post.

Photos: St Andrew's around 1860, the 1879 harbour watercolour (zoomed to Fort
Canning for the dhobies), Government House (Lambert c.1890, and McNair's 1869
plate in scaffolding), Cavenagh Bridge, the Istana in 2022 (Chris's own photo),
and McNair's plates of the monthly muster, the jail gate and the Pulau Ubin
quarry. The convict portraits from McNair's book (book pages, cropped to each portrait with a slow drift)
sit only under sentences that name no one; sentences naming Bonham,
Butterworth, Coleman, Man, MacPherson, Ord, McNair, Church, Hammapah or Rajaram
show buildings or plates instead. Page 156 of the book is zoomed to its two
photos; the 1873 offences chart (scripts/render_convict_crimes_chart.py) is
frozen; the Straits Times Overland Journal of 3 May 1873 is zoomed to the
Paknam report.

59 slides, one per sentence.
"""

CREDITS = {
    "CHART": "Chart by Lesser Known Singapore, figures per the post's own Sources list",
}

IMAGES = {
    "CAV1880": "https://upload.wikimedia.org/wikipedia/commons/thumb/e/eb/KITLV_-_89910_-_Cavanagh_Bridge_in_Singapore_-_before_1880.tif/lossy-page1-1920px-KITLV_-_89910_-_Cavanagh_Bridge_in_Singapore_-_before_1880.tif.jpg",
    "CHART": "/assets/images/convicts-1873-offences-chart.png",
    "GATE": "https://upload.wikimedia.org/wikipedia/commons/thumb/c/c5/Main_gate_of_Singapore_Jail%2C_Bras_Basah_%28McNair_1899%2C_Plate_XI%29.jpg/1920px-Main_gate_of_Singapore_Jail%2C_Bras_Basah_%28McNair_1899%2C_Plate_XI%29.jpg",
    "GH1869": "https://upload.wikimedia.org/wikipedia/commons/thumb/5/56/Government_House%2C_Singapore%2C_approaching_completion%2C_1869_%28McNair_1899%2C_Plate_XVIII%29.jpg/1920px-Government_House%2C_Singapore%2C_approaching_completion%2C_1869_%28McNair_1899%2C_Plate_XVIII%29.jpg",
    "GH1890": "https://upload.wikimedia.org/wikipedia/commons/thumb/8/87/KITLV_-_103751_-_Government_House_in_Singapore_-_circa_1890.tif/lossy-page1-1920px-KITLV_-_103751_-_Government_House_in_Singapore_-_circa_1890.tif.jpg",
    "GHL": "https://upload.wikimedia.org/wikipedia/commons/thumb/8/8a/KITLV_-_53172_-_Lambert_%26_Co.%2C_G.R._-_Singapore_-_Government_House_in_Singapore_-_circa_1890.tif/lossy-page1-1920px-KITLV_-_53172_-_Lambert_%26_Co.%2C_G.R._-_Singapore_-_Government_House_in_Singapore_-_circa_1890.tif.jpg",
    "ISTANA": "https://upload.wikimedia.org/wikipedia/commons/thumb/4/40/Istana_Singapore%2C_main_building_from_the_lawn_during_an_open_house%2C_2022.jpg/1920px-Istana_Singapore%2C_main_building_from_the_lawn_during_an_open_house%2C_2022.jpg",
    "MUSTER": "https://upload.wikimedia.org/wikipedia/commons/thumb/1/16/General_monthly_muster_of_the_convicts%2C_Singapore_Jail_%28McNair_1899%2C_frontispiece%29.jpg/1920px-General_monthly_muster_of_the_convicts%2C_Singapore_Jail_%28McNair_1899%2C_frontispiece%29.jpg",
    "OUTRAM": "https://upload.wikimedia.org/wikipedia/commons/thumb/3/30/J_F_A_McNair%2C_architectural_drawing_of_a_proposed_prison_at_Outram%2C_Singapore_%281880s%29.jpg/1920px-J_F_A_McNair%2C_architectural_drawing_of_a_proposed_prison_at_Outram%2C_Singapore_%281880s%29.jpg",
    "P12": "https://upload.wikimedia.org/wikipedia/commons/thumb/c/c4/California_Digital_Library_%28IA_prisonerstheirow00mcnarich%29.pdf/page12-1280px-California_Digital_Library_%28IA_prisonerstheirow00mcnarich%29.pdf.jpg",
    "P127": "https://upload.wikimedia.org/wikipedia/commons/thumb/c/c4/California_Digital_Library_%28IA_prisonerstheirow00mcnarich%29.pdf/page127-1280px-California_Digital_Library_%28IA_prisonerstheirow00mcnarich%29.pdf.jpg",
    "P135": "https://upload.wikimedia.org/wikipedia/commons/thumb/c/c4/California_Digital_Library_%28IA_prisonerstheirow00mcnarich%29.pdf/page135-1280px-California_Digital_Library_%28IA_prisonerstheirow00mcnarich%29.pdf.jpg",
    "P143": "https://upload.wikimedia.org/wikipedia/commons/thumb/c/c4/California_Digital_Library_%28IA_prisonerstheirow00mcnarich%29.pdf/page143-1280px-California_Digital_Library_%28IA_prisonerstheirow00mcnarich%29.pdf.jpg",
    "P156": "https://upload.wikimedia.org/wikipedia/commons/thumb/c/c4/California_Digital_Library_%28IA_prisonerstheirow00mcnarich%29.pdf/page156-1280px-California_Digital_Library_%28IA_prisonerstheirow00mcnarich%29.pdf.jpg",
    "QUARRY": "https://upload.wikimedia.org/wikipedia/commons/thumb/3/33/Convicts_stone-quarrying_at_Pulau_Ubin%2C_Singapore_%28McNair_1899%2C_Plate_XX%29.jpg/1920px-Convicts_stone-quarrying_at_Pulau_Ubin%2C_Singapore_%28McNair_1899%2C_Plate_XX%29.jpg",
    "SA06": "https://upload.wikimedia.org/wikipedia/commons/8/86/Photographic_Views_of_Singapore_Plate_06_St_Andrew%27s_Cathedral_and_Raffles_Monument.jpg",
    "SA1860": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/d4/KITLV_-_29163_-_St._Andrew%27s_Cathedral%2C_belonging_to_the_Anglican_Church%2C_Singapore_-_1860.tif/lossy-page1-1920px-KITLV_-_29163_-_St._Andrew%27s_Cathedral%2C_belonging_to_the_Anglican_Church%2C_Singapore_-_1860.tif.jpg",
    "SAEUR": "https://upload.wikimedia.org/wikipedia/commons/thumb/0/0c/KITLV_-_89904_-_Hotel_de_l%27Europe_against_the_backdrop_of_St_Andrews_Cathedral_in_Singapore_-_before_1880.tif/lossy-page1-1920px-KITLV_-_89904_-_Hotel_de_l%27Europe_against_the_backdrop_of_St_Andrews_Cathedral_in_Singapore_-_before_1880.tif.jpg",
    "SAWC": "https://upload.wikimedia.org/wikipedia/commons/thumb/2/2f/Malaysia%3B_view_across_the_harbour_to_Fort_Canning_and_the_ca_Wellcome_V0037489.jpg/1920px-Malaysia%3B_view_across_the_harbour_to_Fort_Canning_and_the_ca_Wellcome_V0037489.jpg",
    "ST73": "/assets/images/straits-times-overland-journal-1873-05-03-page-8.jpg",
}

_P0 = {"type": "cover", "zoom": [1.0, 1.05, 1.1], "pan": [(0.3, 0.5), (0.5, 0.5), (0.7, 0.5)], "ease": "ease-in-out"}
_P1 = {"type": "cover", "zoom": [1.35, 1.4, 1.45], "pan": [(0.5, 0.5), (0.5, 0.5), (0.5, 0.5)], "ease": "ease-in-out"}
_P2 = {"type": "cover", "zoom": [1.00, 1.02, 1.04], "pan": [(0.5, 0.453), (0.0, 0.469), (0.0, 0.485)], "ease": "ease-in-out"}
_P3 = {"type": "letterbox", "zoom": [1.0, 1.0, 1.0], "pan": [(0.5, 0.5)] * 3, "ease": "linear"}
_P4 = {"type": "cover", "zoom": [1.1, 1.05, 1.0], "pan": [(0.7, 0.5), (0.5, 0.5), (0.3, 0.5)], "ease": "ease-in-out"}
_P5 = {"type": "cover", "zoom": [1.4, 1.45, 1.5], "pan": [(0.75, 0.5), (0.72, 0.5), (0.69, 0.5)], "ease": "ease-in-out"}
_P6 = {"type": "cover", "zoom": [1.00, 1.02, 1.04], "pan": [(0.5, 0.405), (0.0, 0.422), (0.0, 0.438)], "ease": "ease-in-out"}
_P7 = {"type": "cover", "zoom": [1.5, 1.55, 1.6], "pan": [(0.35, 0.45), (0.38, 0.45), (0.41, 0.45)], "ease": "ease-in-out"}
_P8 = {"type": "cover", "zoom": [1.45, 1.49, 1.52], "pan": [(0.629, 0.206), (0.622, 0.221), (0.617, 0.237)], "ease": "ease-in-out"}
_P9 = {"type": "cover", "zoom": [1.45, 1.49, 1.52], "pan": [(0.629, 0.794), (0.622, 0.805), (0.617, 0.816)], "ease": "ease-in-out"}
_P10 = {"type": "cover", "zoom": [1.0, 1.02, 1.04], "pan": [(0.45, 0.5), (0.5, 0.5), (0.55, 0.5)], "ease": "ease-in-out"}
_P11 = {"type": "cover", "zoom": [2.80, 2.87, 2.94], "pan": [(0.687, 0.563), (0.684, 0.574), (0.682, 0.585)], "ease": "ease-in-out"}
_P12 = {"type": "cover", "zoom": [1.40, 1.43, 1.47], "pan": [(0.5, 0.0), (0.5, 0.0), (0.5, 0.0)], "ease": "ease-in-out"}

SLIDES = [
    {"img": "SA1860", **_P0},  # s0 The Indian Convicts Who Built Colonial Singa
    {"img": "SAWC", **_P0},  # s1 On the 18th of April 1825 the brig Horatio r
    {"img": "SAWC", **_P1},  # s2 A week later 122 more arrived from Bengal.
    {"img": "GHL", **_P0},  # s3 For the next 48 years Singapore took in conv
    {"img": "QUARRY", **_P0},  # s4 Britain had been sending Indian convicts to 
    {"img": "MUSTER", **_P0},  # s5 Singapore was short of labour and grew faste
    {"img": "GATE", **_P0},  # s6 In 1857 the jail held 2,139 convicts from In
    {"img": "OUTRAM", **_P0},  # s7 According to J. F. A. McNair, who ran it fro
    {"img": "P143", **_P2},  # s8 Most were ordinary criminals, sentenced by I
    {"img": "CHART", **_P3},  # s9 McNair's count of the convicts still in the 
    {"img": "CHART", **_P3},  # s10 Most of the rest had been convicted of murde
    {"img": "GATE", **_P1},  # s11 A smaller number were political prisoners.
    {"img": "SAWC", **_P4},  # s12 After the uprising of 1857 in India, rebels 
    {"img": "MUSTER", **_P4},  # s13 The first group, 17 men and 2 women who arri
    {"img": "GATE", **_P4},  # s14 The Sikh leader Bhai Maharaj Singh, sent to 
    {"img": "MUSTER", **_P5},  # s15 When the first convicts landed, four free wa
    {"img": "QUARRY", **_P4},  # s16 The Resident, George Bonham, found that the 
    {"img": "MUSTER", **_P0},  # s17 McNair thought this was possibly the first t
    {"img": "P127", **_P6},  # s18 As more convicts arrived, one convict warder
    {"img": "GATE", **_P0},  # s19 Under rules formalised by Governor William B
    {"img": "P143", **_P2},  # s20 New arrivals worked in light irons in the fo
    {"img": "P135", **_P6},  # s21 After a probation, a convict moved into the 
    {"img": "MUSTER", **_P4},  # s22 At the top was the first class, trustworthy 
    {"img": "P12", **_P2},  # s23 A man serving a life sentence could reach it
    {"img": "GATE", **_P4},  # s24 The convicts also built their own jail.
    {"img": "GATE", **_P1},  # s25 It took about twenty years, was finished in 
    {"img": "SAWC", **_P0},  # s26 The convicts were not the first Indians in t
    {"img": "SAWC", **_P7},  # s27 Indian washermen, or dhobies, had come in 18
    {"img": "SAWC", **_P4},  # s28 They were free workers, mostly from what is 
    {"img": "SAEUR", **_P0},  # s29 Singapore's early Indian population grew fro
    {"img": "CAV1880", **_P0},  # s30 The convicts' first big task was filling in 
    {"img": "QUARRY", **_P1},  # s31 From 1833, when the architect G. D. Coleman 
    {"img": "P156", **_P8},  # s32 From 1845 the superintendent Henry Man turne
    {"img": "QUARRY", **_P4},  # s33 Convicts learned carpentry, bricklaying, bla
    {"img": "SA1860", **_P0},  # s34 Their best-known work is Saint Andrew's Chur
    {"img": "SAEUR", **_P4},  # s35 Its designer, Ronald MacPherson, chose a sim
    {"img": "SA1860", **_P1},  # s36 They plastered its walls and columns with Ma
    {"img": "GH1869", **_P0},  # s37 Government House, now the Istana, followed.
    {"img": "GHL", **_P4},  # s38 When the Straits Settlements passed from Ind
    {"img": "P156", **_P9},  # s39 According to McNair, convicts did all the br
    {"img": "GH1869", **_P4},  # s40 The house was ready for the visit of the Duk
    {"img": "MUSTER", **_P1},  # s41 For the colony, the convicts were a cheap so
    {"img": "QUARRY", **_P0},  # s42 In the early years each convict received rat
    {"img": "GH1890", **_P0},  # s43 In 1849 the Resident Councillor, Thomas Chur
    {"img": "ISTANA", **_P0},  # s44 According to BiblioAsia, the large public bu
    {"img": "SAEUR", **_P0},  # s45 Some convicts made careers after their relea
    {"img": "CAV1880", **_P4},  # s46 Hammapah, a convict land surveyor, set up a 
    {"img": "GH1890", **_P4},  # s47 According to BiblioAsia, Somapah Village off
    {"img": "SA06", **_P10},  # s48 Bawajee Rajaram, a convict from Bombay, beca
    {"img": "CAV1880", **_P1},  # s49 After his release he worked on municipal dra
    {"img": "GHL", **_P0},  # s50 Transportation to Singapore officially ended
    {"img": "ST73", **_P11},  # s51 On the 3rd of May 1873 the Straits Times Ove
    {"img": "ST73", **_P12},  # s52 The last convicts left on the Paknam on the 
    {"img": "MUSTER", **_P0},  # s53 Those on a ticket-of-leave were allowed to s
    {"img": "P12", **_P2},  # s54 McNair wrote that they merged into the popul
    {"img": "GATE", **_P4},  # s55 The old and infirm were kept in Singapore at
    {"img": "SA1860", **_P4},  # s56 Where it fits in the bigger story: Singapore
    {"img": "MUSTER", **_P5},  # s57 Much of the labour came from Indian convicts
    {"img": "ISTANA", **_P4},  # s58 Many stayed on after 1873, and along with th
]

SCHEDULE = [
    (0.0, 0), (6.9, 1), (19.425, 2), (24.425, 3), (38.275, 4),
    (52.775, 5), (66.85, 6), (74.85, 7), (86.025, 8), (92.875, 9),
    (114.275, 10), (119.7, 11), (123.025, 12), (129.225, 13), (147.05, 14),
    (158.85, 15), (165.075, 16), (178.05, 17), (185.1, 18), (195.275, 19),
    (204.0, 20), (211.975, 21), (226.225, 22), (236.1, 23), (241.35, 24),
    (244.75, 25), (258.8, 26), (263.25, 27), (276.25, 28), (293.1, 29),
    (301.175, 30), (310.825, 31), (329.0, 32), (336.225, 33), (349.95, 34),
    (355.4, 35), (365.075, 36), (378.35, 37), (381.775, 38), (394.3, 39),
    (403.975, 40), (410.725, 41), (414.875, 42), (426.8, 43), (447.3, 44),
    (458.95, 45), (462.725, 46), (471.7, 47), (478.475, 48), (491.425, 49),
    (499.925, 50), (512.2, 51), (531.175, 52), (536.925, 53), (540.65, 54),
    (550.525, 55), (556.25, 56), (565.625, 57), (577.05, 58),
]
TOTAL_DURATION = 588.35
TIMING_JSON = "audio/the-indian-convicts-who-built-colonial-singapore-1825-1873.timing.json"
