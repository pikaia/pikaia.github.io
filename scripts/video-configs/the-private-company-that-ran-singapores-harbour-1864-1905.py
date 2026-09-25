"""Video config for the Tanjong Pagar Dock Company post.

A rich pool: the company's own album (Rijksmuseum, CC0) plus KITLV, the Admiralty
chart, two pages of the Straits Times of 1 July 1905, and a self-rendered bar
chart. The album pages carry cream mounts, so they are zoomed to 1.5-1.75 to crop
the margins and stay inside the photograph. The portrait-format album pages use
higher zooms; the Straits Times pages zoom in on the relevant columns. The
portrait of Tan Kim Ching, the Admiralty chart and the bar chart are frozen
letterbox (graphics/small portraits).

  BAR     - scripts/render_tanjong_pagar_bar_chart.py
  ST4/ST5 - The Straits Times, 1 July 1905, pages 4 and 5 (whole pages, public domain)

65 slides; sentences 21, 26, 43, 46 (short fragments) continue the slide before.
"""

IMAGES = {
    "ALBERT": "https://upload.wikimedia.org/wikipedia/commons/thumb/2/21/Ingang_van_het_Albert-reparatiedok_van_de_Tanjong_Pagar_Dock_Co._Ltd._in_Singapore_Entrance_of_Albert_Graving_dock_%28titel_op_object%29%2C_RP-F-F01140-N.jpg/1920px-Ingang_van_het_Albert-reparatiedok_van_de_Tanjong_Pagar_Dock_Co._Ltd._in_Singapore_Entrance_of_Albert_Graving_dock_%28titel_op_object%29%2C_RP-F-F01140-N.jpg",
    "BANGKOK": "https://upload.wikimedia.org/wikipedia/commons/thumb/7/79/Sleepboot_%27Bangkok%27_van_de_Tanjong_Pagar_Dock_Co._Ltd._in_Singapore_Company%27s_tug_boat_Bangkok_%28titel_op_object%29%2C_RP-F-F01140-AT.jpg/1920px-Sleepboot_%27Bangkok%27_van_de_Tanjong_Pagar_Dock_Co._Ltd._in_Singapore_Company%27s_tug_boat_Bangkok_%28titel_op_object%29%2C_RP-F-F01140-AT.jpg",
    "BAR": "/assets/images/tanjong-pagar-share-price-chart.png",
    "CHART": "https://upload.wikimedia.org/wikipedia/commons/thumb/6/6f/Admiralty_Chart_No_2023_Keppel_Harbor%2C_Singapore%2C_Published_1893.jpg/1920px-Admiralty_Chart_No_2023_Keppel_Harbor%2C_Singapore%2C_Published_1893.jpg",
    "COOLQ": "https://upload.wikimedia.org/wikipedia/commons/thumb/7/73/Woningen_van_de_kolensjouwers_van_de_Tanjong_Pagar_Dock_Co._Ltd._in_Singapore_Coal_coolies_quarters_%28titel_op_object%29%2C_RP-F-F01140-AC.jpg/1920px-Woningen_van_de_kolensjouwers_van_de_Tanjong_Pagar_Dock_Co._Ltd._in_Singapore_Coal_coolies_quarters_%28titel_op_object%29%2C_RP-F-F01140-AC.jpg",
    "CRUISERS": "https://upload.wikimedia.org/wikipedia/commons/thumb/e/eb/Drie_Chinese_schepen_in_een_dok_van_de_Tanjong_Pagar_Dock_Co._Ltd._in_Singapore_Three_Chinese_cruisers_in_dock_%28titel_op_object%29%2C_RP-F-F01140-E.jpg/1920px-Drie_Chinese_schepen_in_een_dok_van_de_Tanjong_Pagar_Dock_Co._Ltd._in_Singapore_Three_Chinese_cruisers_in_dock_%28titel_op_object%29%2C_RP-F-F01140-E.jpg",
    "DERUYTER": "https://upload.wikimedia.org/wikipedia/commons/thumb/2/2f/Hr._Ms._%27De_Ruyter%27_en_bemanning_in_een_dok_van_de_Tanjong_Pagar_Dock_Co._Ltd._in_Singapore_H.N.M.S._De_Ruyter_%28titel_op_object%29%2C_RP-F-F01140-G.jpg/1920px-Hr._Ms._%27De_Ruyter%27_en_bemanning_in_een_dok_van_de_Tanjong_Pagar_Dock_Co._Ltd._in_Singapore_H.N.M.S._De_Ruyter_%28titel_op_object%29%2C_RP-F-F01140-G.jpg",
    "GLEN": "https://upload.wikimedia.org/wikipedia/commons/thumb/e/ee/Drie_schepen_van_de_Glen_Line_aan_de_kade_van_de_Tanjong_Pagar_Dock_Co._Ltd._in_Singapore_Three_glen_steamers_alongside_the_wharf_%28titel_op_object%29%2C_RP-F-F01140-O.jpg/1920px-thumbnail.jpg",
    "GODOWN": "https://upload.wikimedia.org/wikipedia/commons/thumb/c/cf/Interieur_van_een_pakhuis_van_de_Tanjong_Pagar_Dock_Co._Ltd._in_Singapore_Interior_of_a_wharf_godown_%28titel_op_object%29%2C_RP-F-F01140-Q.jpg/1920px-Interieur_van_een_pakhuis_van_de_Tanjong_Pagar_Dock_Co._Ltd._in_Singapore_Interior_of_a_wharf_godown_%28titel_op_object%29%2C_RP-F-F01140-Q.jpg",
    "KONING": "https://upload.wikimedia.org/wikipedia/commons/thumb/f/ff/Nederlands_schip_in_een_dok_van_de_Tanjong_Pagar_Dock_Co._Ltd._in_Singapore_H.N.M.S._King_of_the_Netherlands_%28titel_op_object%29%2C_RP-F-F01140-C.jpg/1920px-Nederlands_schip_in_een_dok_van_de_Tanjong_Pagar_Dock_Co._Ltd._in_Singapore_H.N.M.S._King_of_the_Netherlands_%28titel_op_object%29%2C_RP-F-F01140-C.jpg",
    "MACHINE": "https://upload.wikimedia.org/wikipedia/commons/thumb/1/16/Gezicht_op_het_machinehuis_van_de_Tanjong_Pagar_Dock_Co._Ltd._in_Singapore_Machine_shop_outside_%28titel_op_object%29%2C_RP-F-F01140-I.jpg/1920px-Gezicht_op_het_machinehuis_van_de_Tanjong_Pagar_Dock_Co._Ltd._in_Singapore_Machine_shop_outside_%28titel_op_object%29%2C_RP-F-F01140-I.jpg",
    "MEAL": "https://upload.wikimedia.org/wikipedia/commons/thumb/9/90/Schepen_in_een_dok_van_de_Tanjong_Pagar_Dock_Co._Ltd._in_Singapore_met_eromheen_personeel_Meal_hour%2C_Tanjong_Pagar_Dock%2C_men_leaving_off_work_%28titel_op_object%29%2C_RP-F-F01140-A.jpg/1920px-thumbnail.jpg",
    "NH1910": "https://upload.wikimedia.org/wikipedia/commons/thumb/6/63/KITLV_-_79927_-_Kleingrothe%2C_C.J._-_Medan_-_New_Harbour_in_Singapore_-_circa_1910.tif/lossy-page1-1280px-KITLV_-_79927_-_Kleingrothe%2C_C.J._-_Medan_-_New_Harbour_in_Singapore_-_circa_1910.tif.jpg",
    "NHENT": "https://upload.wikimedia.org/wikipedia/commons/thumb/7/78/Gezicht_op_de_ingang_van_de_nieuwe_haven_te_Singapore_Entrance_to_New-harbour._S.pore_%28titel_op_object%29%2C_RP-F-F01104-X.jpg/1920px-Gezicht_op_de_ingang_van_de_nieuwe_haven_te_Singapore_Entrance_to_New-harbour._S.pore_%28titel_op_object%29%2C_RP-F-F01104-X.jpg",
    "ORION": "https://upload.wikimedia.org/wikipedia/commons/thumb/9/9e/H.M.S._%27Orion%27_en_bemanning_in_een_dok_van_de_Tanjong_Pagar_Dock_Co._Ltd._in_Singapore_H.M.S._Orion_%28titel_op_object%29%2C_RP-F-F01140-B.jpg/1920px-H.M.S._%27Orion%27_en_bemanning_in_een_dok_van_de_Tanjong_Pagar_Dock_Co._Ltd._in_Singapore_H.M.S._Orion_%28titel_op_object%29%2C_RP-F-F01140-B.jpg",
    "PANW": "https://upload.wikimedia.org/wikipedia/commons/thumb/3/35/Tanjong_Pagar_in_Singapore_gezien_vanuit_het_westen_Panoramic_view_of_Tanjong_Pagar_from_the_west_%28titel_op_object%29%2C_RP-F-F01140-AE.jpg/1920px-Tanjong_Pagar_in_Singapore_gezien_vanuit_het_westen_Panoramic_view_of_Tanjong_Pagar_from_the_west_%28titel_op_object%29%2C_RP-F-F01140-AE.jpg",
    "POLICE": "https://upload.wikimedia.org/wikipedia/commons/thumb/c/c0/Politieagenten_voor_het_politiebureau_van_Tanjong_Pagar_in_Singapore_Tanjong_Pagar_police_station_%28titel_op_object%29%2C_RP-F-F01140-AQ.jpg/1920px-Politieagenten_voor_het_politiebureau_van_Tanjong_Pagar_in_Singapore_Tanjong_Pagar_police_station_%28titel_op_object%29%2C_RP-F-F01140-AQ.jpg",
    "RICKMERS": "https://upload.wikimedia.org/wikipedia/commons/thumb/e/ec/Vijfmaster_%27Maria_Rickmers%27_in_het_Albert-dok_van_de_Tanjong_Pagar_Dock_Co._Ltd._in_Singapore_Auxiliary_five-masted_ship_Maria_Rickmers_in_Albert_Dock%2C_Tanjong_Pagar%2C_bow_view_%28titel_op_object%29%2C_RP-F-F01140-AS.jpg/1920px-thumbnail.jpg",
    "SLIP": "https://upload.wikimedia.org/wikipedia/commons/thumb/9/98/Gezicht_op_de_kades%2C_scheepshellingen_en_gebouwen_van_de_Singapore_slipway_and_engineering_Company_Limited_in_Tanjong_Pagar_Branch_establishments_Singapore_slipway_and_engineering_Company%2C_Limited_%28titel_op_object%29%2C_RP-F-F01140-AY.jpg/1920px-thumbnail.jpg",
    "ST4": "/assets/images/straits-times-1905-07-01-page-4.jpg",
    "ST5": "/assets/images/straits-times-1905-07-01-page-5.jpg",
    "TKC": "https://upload.wikimedia.org/wikipedia/commons/thumb/c/cc/Tan_Kim_Ching.jpg/1920px-Tan_Kim_Ching.jpg",
    "WHARF": "https://upload.wikimedia.org/wikipedia/commons/thumb/7/7d/Deel_van_de_scheepswerf_van_de_Tanjong_Pagar_Dock_Co._Ltd._in_Singapore_View_shewing_section_of_wharf_%28titel_op_object%29%2C_RP-F-F01140-P.jpg/1920px-Deel_van_de_scheepswerf_van_de_Tanjong_Pagar_Dock_Co._Ltd._in_Singapore_View_shewing_section_of_wharf_%28titel_op_object%29%2C_RP-F-F01140-P.jpg",
}

CREDITS = {
    "BAR": "Chart by Lesser Known Singapore, figures per the post's own Sources list",
}

_EA = {"type": "cover", "zoom": [1.25, 1.3, 1.35], "pan": [(0.45, 0.5), (0.5, 0.5), (0.55, 0.5)], "ease": "ease-in-out"}
_EB = {"type": "cover", "zoom": [1.35, 1.3, 1.25], "pan": [(0.55, 0.5), (0.5, 0.5), (0.45, 0.5)], "ease": "ease-in-out"}
_FIX = {"type": "letterbox", "zoom": [1.0, 1.0, 1.0], "pan": [(0.5, 0.5)] * 3, "ease": "linear"}
_LA = {"type": "cover", "zoom": [1.5, 1.55, 1.6], "pan": [(0.52, 0.42), (0.57, 0.5), (0.62, 0.58)], "ease": "ease-in-out"}
_LB = {"type": "cover", "zoom": [1.6, 1.55, 1.5], "pan": [(0.62, 0.58), (0.57, 0.5), (0.52, 0.42)], "ease": "ease-in-out"}
_LC = {"type": "cover", "zoom": [1.5, 1.6, 1.7], "pan": [(0.57, 0.5), (0.57, 0.5), (0.57, 0.5)], "ease": "ease-in-out"}
_NA = {"type": "cover", "zoom": [1.0, 1.05, 1.1], "pan": [(0.4, 0.5), (0.5, 0.5), (0.6, 0.5)], "ease": "ease-in-out"}
_NB = {"type": "cover", "zoom": [1.1, 1.05, 1.0], "pan": [(0.6, 0.5), (0.5, 0.5), (0.4, 0.5)], "ease": "ease-in-out"}
_PA = {"type": "cover", "zoom": [1.65, 1.7, 1.75], "pan": [(0.5, 0.3), (0.5, 0.42), (0.5, 0.55)], "ease": "ease-in-out"}
_PB = {"type": "cover", "zoom": [1.75, 1.7, 1.65], "pan": [(0.5, 0.55), (0.5, 0.42), (0.5, 0.3)], "ease": "ease-in-out"}
_PP = {"type": "cover", "zoom": [1.65, 1.7, 1.75], "pan": [(0.42, 0.3), (0.42, 0.4), (0.42, 0.5)], "ease": "ease-in-out"}
_S4F = {"type": "cover", "zoom": [2.6, 2.7, 2.8], "pan": [(0.80, 0.34), (0.82, 0.35), (0.85, 0.36)], "ease": "ease-in-out"}
_S4N = {"type": "cover", "zoom": [2.1, 2.15, 2.2], "pan": [(0.45, 0.07), (0.45, 0.085), (0.45, 0.10)], "ease": "ease-in-out"}
_S4N2 = {"type": "cover", "zoom": [2.2, 2.15, 2.1], "pan": [(0.45, 0.10), (0.45, 0.085), (0.45, 0.07)], "ease": "ease-in-out"}
_S4N3 = {"type": "cover", "zoom": [2.1, 2.2, 2.3], "pan": [(0.45, 0.20), (0.45, 0.22), (0.45, 0.24)], "ease": "ease-in-out"}
_S5C = {"type": "cover", "zoom": [3.0, 3.0, 3.0], "pan": [(0.154, 0.83), (0.154, 0.90), (0.154, 0.975)], "ease": "ease-in-out"}
_S5L = {"type": "cover", "zoom": [3.0, 3.0, 3.0], "pan": [(0.78, 0.55), (0.80, 0.60), (0.82, 0.65)], "ease": "ease-in-out"}
_S5L2 = {"type": "cover", "zoom": [3.0, 3.0, 3.0], "pan": [(0.82, 0.65), (0.80, 0.60), (0.78, 0.55)], "ease": "ease-in-out"}

SLIDES = [
    {"img": "MEAL", **_LA},  # s0 The Private Company That Ran Singapore's Harbo
    {"img": "PANW", **_LB},  # s1 In 1905 the government of the Straits Settleme
    {"img": "WHARF", **_PB},  # s2 The company had begun in 1864 as the first loc
    {"img": "GLEN", **_LA},  # s3 Steamships had to be fed.
    {"img": "NH1910", **_NA},  # s4 When the Peninsular and Oriental Steam Navigat
    {"img": "BANGKOK", **_LB},  # s5 It was slow work, worse in choppy weather when
    {"img": "NHENT", **_EA},  # s6 In 1852 P&O became the first shipping company 
    {"img": "CHART", **_FIX},  # s7 The anchorage was sheltered, the water was dee
    {"img": "ORION", **_LA},  # s8 New Harbour was renamed Keppel Harbour in 1900
    {"img": "MACHINE", **_LB},  # s9 Ship repair was the next need.
    {"img": "ALBERT", **_LA},  # s10 In 1859 a British mariner, Captain William Clo
    {"img": "CRUISERS", **_LB},  # s11 In 1864 a group of investors decided to build 
    {"img": "SLIP", **_LA},  # s12 To raise the money they set up a joint-stock l
    {"img": "TKC", **_FIX},  # s13 The agency house Guthrie & Co. and the Chinese
    {"img": "GODOWN", **_LB},  # s14 The company hoped to raise $200,000 in Singapo
    {"img": "KONING", **_LA},  # s15 Its articles of association gave a London Cons
    {"img": "TKC", **_FIX},  # s16 Tan Kim Ching was the eldest of the three sons
    {"img": "DERUYTER", **_LB},  # s17 Song Ong Siang's 1923 history records that his
    {"img": "PANW", **_LA},  # s18 The same book notes that Ong Kew Ho, a Malacca
    {"img": "MEAL", **_LB},  # s19 The company's first dock, Victoria Dock, was o
    {"img": "RICKMERS", **_PA},  # s20 The Patent Slip and Dock Company, which now fa
    {"img": "GLEN", **_LB},  # s21 Then the Suez Canal opened in 1869, more steam
    {"img": "ALBERT", **_LB},  # s22 The Patent company built a second dock in 1870
    {"img": "NHENT", **_EB},  # s23 In 1871 a meeting was held at the office of Bo
    {"img": "BANGKOK", **_LA},  # s24 H. A. K. Whampoa was elected one of its provis
    {"img": "WHARF", **_PA},  # s25 Meanwhile, the company bought up smaller rival
    {"img": "NH1910", **_NB},  # s26 In 1899 it merged with the New Harbour Dock Co
    {"img": "MEAL", **_LC},  # s27 Behind the docks was a large workforce.
    {"img": "COOLQ", **_LA},  # s28 Song Ong Siang's history describes Chinese coo
    {"img": "GODOWN", **_LA},  # s29 Much of the labour was arranged through contra
    {"img": "COOLQ", **_LB},  # s30 Gan Eng Seng, who died in 1899, was labour con
    {"img": "POLICE", **_PP},  # s31 The company also kept its own police force and
    {"img": "PANW", **_LB},  # s32 By 1904 Singapore was the seventh-largest port
    {"img": "CHART", **_FIX},  # s33 The Singapore board and the London Consulting 
    {"img": "MACHINE", **_LA},  # s34 In March 1904 the company submitted a $12-mill
    {"img": "NHENT", **_EA},  # s35 The company then asked the Straits Settlements
    {"img": "ORION", **_LB},  # s36 The government decided instead to take over th
    {"img": "KONING", **_LB},  # s37 The London committee, for its part, had said i
    {"img": "RICKMERS", **_PB},  # s38 The Tanjong Pagar Dock Bill was introduced in 
    {"img": "WHARF", **_PB},  # s39 The Governor's stated ground, as recorded by S
    {"img": "GLEN", **_LA},  # s40 Mr Napier, supporting the bill, said that publ
    {"img": "DERUYTER", **_LA},  # s41 He recalled that the first chairman, Thomas Sc
    {"img": "SLIP", **_LB},  # s42 Tan Jiak Kim added that the company was not po
    {"img": "ST4", **_S4N},  # s43 The bill passed on the 13th of April 1905, and
    {"img": "ST4", **_S4N2},  # s44 The Straits Times of Saturday the 1st of July 
    {"img": "ST4", **_S4N3},  # s45 They said that the company's undertaking had, 
    {"img": "ST4", **_S4F},  # s46 A short item on the same page recorded that th
    {"img": "ST5", **_S5C},  # s47 The Governor had told the Legislative Council 
    {"img": "ST5", **_S5L},  # s48 The Board had nine appointed members and two o
    {"img": "ST5", **_S5L2},  # s49 One of the appointed members was J. Rumney Nic
    {"img": "CRUISERS", **_LA},  # s50 Compensation was settled by arbitration, with 
    {"img": "BAR", **_FIX},  # s51 When the Under-Secretary of State for the Colo
    {"img": "BAR", **_FIX},  # s52 The National Library Board's account gives $76
    {"img": "BAR", **_FIX},  # s53 The questioner, Josiah Wedgwood, put the other
    {"img": "BANGKOK", **_LB},  # s54 Churchill accepted that the figures were corre
    {"img": "CRUISERS", **_LC},  # s55 Twelve per cent, he said, was the smallest div
    {"img": "PANW", **_LA},  # s56 The Governor, he added, had told the directors
    {"img": "GODOWN", **_LB},  # s57 He also confirmed that the arbitration would c
    {"img": "ALBERT", **_LC},  # s58 The Tanjong Pagar Dock Board was reconstituted
    {"img": "MACHINE", **_LB},  # s59 The Board kept the company's ship-repair busin
    {"img": "NHENT", **_EB},  # s60 Through later changes of name it became the Po
    {"img": "ORION", **_LA},  # s61 Where it fits in the bigger story: Singapore's
    {"img": "PANW", **_LB},  # s62 This part of it began with an agency house, a 
    {"img": "COOLQ", **_LC},  # s63 The docks, the coaling wharves and the people 
    {"img": "ST4", **_S4N},  # s64 What changed in 1905 was who owned the port.
]

SCHEDULE = [
    (0.0, 0), (6.525, 1), (25.35, 2), (43.9, 3), (46.45, 4),
    (69.375, 5), (77.1, 6), (87.425, 7), (95.8, 8), (109.825, 9),
    (112.725, 10), (126.425, 11), (133.45, 12), (151.2, 13), (158.15, 14),
    (172.5, 15), (184.3, 16), (202.3, 17), (222.425, 18), (236.65, 19),
    (248.25, 20), (259.625, 21), (269.175, 22), (285.675, 23), (297.95, 24),
    (315.625, 25), (319.2, 26), (332.25, 27), (335.65, 28), (347.725, 29),
    (351.8, 30), (369.05, 31), (374.15, 32), (390.25, 33), (396.8, 34),
    (412.65, 35), (417.925, 36), (422.3, 37), (431.325, 38), (442.825, 39),
    (460.2, 40), (469.725, 41), (486.55, 42), (502.0, 43), (512.45, 44),
    (522.475, 45), (541.85, 46), (552.675, 47), (567.475, 48), (572.05, 49),
    (585.025, 50), (595.575, 51), (610.8, 52), (622.65, 53), (654.35, 54),
    (659.475, 55), (675.125, 56), (688.575, 57), (699.8, 58), (716.125, 59),
    (725.0, 60), (736.4, 61), (744.825, 62), (764.2, 63), (769.225, 64),
]
TOTAL_DURATION = 773.475
TIMING_JSON = "audio/the-private-company-that-ran-singapores-harbour-1864-1905.timing.json"
