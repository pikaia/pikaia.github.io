"""Video config for the Blakang Mati post.

The island from Erédia's 1604 map to Sentosa today: the 1880 watercolour, harbour
views from around 1890 and 1910, a Pulau Brani kampong as a neighbouring stand-in
for the vanished Blakang Mati villages, Fort Siloso and Mount Imbiah, the 1945
military map, the 1951 ferry, the 1948 Straits Times ferry notice, the three-stage
island map, the timeline, and present-day Sentosa. Robert Little, Lee Kuan Yew,
E. W. Barker, Albert Winsemius, Alan Choe and Chia Thye Poh are named over places,
never over someone else's face; Trump and Kim (s77) are shown together at the
Capella. Portrait-shaped images, the Erédia map and the newspaper page are
letterboxed with a modest zoom; the maps and timeline are letterboxed and frozen.

53 slides, 878.075s. Narration: Kokoro with the OpenVoice clone.
AVATAR: first and last 30s, cartoon with motion.
"""

IMAGES = {
    "HERO": "https://upload.wikimedia.org/wikipedia/commons/thumb/f/f0/Singapore%3B_a_view_across_part_of_Blakang_Mati_Island._Waterc_Wellcome_V0037528.jpg/1280px-Singapore%3B_a_view_across_part_of_Blakang_Mati_Island._Waterc_Wellcome_V0037528.jpg",
    "PANO": "https://upload.wikimedia.org/wikipedia/commons/thumb/9/9b/Panorama_of_Sentosa%2C_Singapore_-_March_2018.jpg/1280px-Panorama_of_Sentosa%2C_Singapore_-_March_2018.jpg",
    "KEPPEL": "https://upload.wikimedia.org/wikipedia/commons/thumb/a/ac/Singapore_-_Keppel_Harb_1952.jpg/1280px-Singapore_-_Keppel_Harb_1952.jpg",
    "SKY2006": "https://upload.wikimedia.org/wikipedia/commons/thumb/1/10/Sentosa_viewed_from_the_Carlsberg_Sky_Tower%2C_Singapore_-_20060716-03.jpg/1280px-Sentosa_viewed_from_the_Carlsberg_Sky_Tower%2C_Singapore_-_20060716-03.jpg",
    "EREDIA": "https://upload.wikimedia.org/wikipedia/commons/f/f6/Map_of_Singapura_by_Godinho_de_Er%C3%A9dia_1604.jpg",
    "PORT1890": "https://upload.wikimedia.org/wikipedia/commons/thumb/7/7b/KITLV_-_377455_-_Port_at_Singapore_-_circa_1890.tif/lossy-page1-1280px-KITLV_-_377455_-_Port_at_Singapore_-_circa_1890.tif.jpg",
    "ENTRANCE": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/d4/KITLV_-_1404881_-_Singapore._Entrance_at_New_harbor._-_1895-1908.tif/lossy-page1-1280px-KITLV_-_1404881_-_Singapore._Entrance_at_New_harbor._-_1895-1908.tif.jpg",
    "NEWPORT": "https://upload.wikimedia.org/wikipedia/commons/thumb/3/38/KITLV_-_38151_-_The_new_port_at_Singapore_-_circa_1890.tif/lossy-page1-1280px-KITLV_-_38151_-_The_new_port_at_Singapore_-_circa_1890.tif.jpg",
    "STJAMES": "https://upload.wikimedia.org/wikipedia/commons/thumb/f/f0/Singapore._View_from_St._James%2C_KITLV_1404953.tiff/lossy-page1-1280px-Singapore._View_from_St._James%2C_KITLV_1404953.tiff.jpg",
    "BRANI": "https://upload.wikimedia.org/wikipedia/commons/thumb/5/50/KITLV_-_105809_-_Lambert_%26_Co.%2C_G.R._-_Singapore_-_Malay_village_on_the_island_of_Pulau_Brani_near_Singapore_-_circa_1900.tif/lossy-page1-1280px-KITLV_-_105809_-_Lambert_%26_Co.%2C_G.R._-_Singapore_-_Malay_village_on_the_island_of_Pulau_Brani_near_Singapore_-_circa_1900.tif.jpg",
    "NH1910": "https://upload.wikimedia.org/wikipedia/commons/thumb/6/63/KITLV_-_79927_-_Kleingrothe%2C_C.J._-_Medan_-_New_Harbour_in_Singapore_-_circa_1910.tif/lossy-page1-1280px-KITLV_-_79927_-_Kleingrothe%2C_C.J._-_Medan_-_New_Harbour_in_Singapore_-_circa_1910.tif.jpg",
    "IMBIAH": "https://upload.wikimedia.org/wikipedia/commons/thumb/4/4e/Gun_emplacement_remains%2C_Mount_Imbiah%2C_Sentosa%2C_Singapore_-_20071208.jpg/1280px-Gun_emplacement_remains%2C_Mount_Imbiah%2C_Sentosa%2C_Singapore_-_20071208.jpg",
    "MAP0": "/assets/images/blakang-mati-map-0.png",
    "SILOSO": "https://upload.wikimedia.org/wikipedia/commons/thumb/c/c3/Fort_Siloso%2C_Singapore_202410.jpg/1280px-Fort_Siloso%2C_Singapore_202410.jpg",
    "GUNS": "https://upload.wikimedia.org/wikipedia/commons/thumb/a/a5/Fort_Siloso_mortar_and_RML_64_pounder_64_cwt_guns_Flickr_4374799233_9e76025732_o.jpg/1280px-Fort_Siloso_mortar_and_RML_64_pounder_64_cwt_guns_Flickr_4374799233_9e76025732_o.jpg",
    "REPLICA": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/dd/Replica_BL_6_inch_Mk_VII_gun_at_Fort_Siloso%2C_Sentosa%2C_Singapore.jpg/1280px-Replica_BL_6_inch_Mk_VII_gun_at_Fort_Siloso%2C_Sentosa%2C_Singapore.jpg",
    "BCP": "https://upload.wikimedia.org/wikipedia/commons/thumb/9/9f/Battery_Command_Post%2C_Fort_Siloso_202410.jpg/1280px-Battery_Command_Post%2C_Fort_Siloso_202410.jpg",
    "MAP1945": "https://upload.wikimedia.org/wikipedia/commons/3/31/P_Blakang_Mati_1945_map.jpg",
    "WARYEARS": "https://upload.wikimedia.org/wikipedia/commons/thumb/4/4a/The_War_Years_1942-45_%28170858%29.jpg/1280px-The_War_Years_1942-45_%28170858%29.jpg",
    "SKY2004": "https://upload.wikimedia.org/wikipedia/commons/3/3b/Sky_Tower_view_E_Sentosa_2004.jpg",
    "FERRY": "https://upload.wikimedia.org/wikipedia/commons/thumb/f/f8/Blakang_Mati_Ferry_1951.jpg/1280px-Blakang_Mati_Ferry_1951.jpg",
    "USS": "https://upload.wikimedia.org/wikipedia/commons/thumb/3/3a/Universal_Studios_Singapore%2C_Resorts_World_Sentosa_-_20110728.jpg/1280px-Universal_Studios_Singapore%2C_Resorts_World_Sentosa_-_20110728.jpg",
    "MAP1": "/assets/images/blakang-mati-map-1.png",
    "ST1948": "/assets/images/straits-times-1948-06-22-page-2.jpg",
    "ARTAVE": "https://upload.wikimedia.org/wikipedia/commons/thumb/c/c1/Artillery_Avenue%2C_Sentosa%2C_Aug_06.JPG/1280px-Artillery_Avenue%2C_Sentosa%2C_Aug_06.JPG",
    "RWS": "https://upload.wikimedia.org/wikipedia/commons/thumb/1/1d/Aerial_view_of_Resorts_World_Sentosa%2C_Singapore_-_20100227.jpg/1280px-Aerial_view_of_Resorts_World_Sentosa%2C_Singapore_-_20100227.jpg",
    "PALAWAN": "https://upload.wikimedia.org/wikipedia/commons/c/c3/Aerial_view_of_Palawan_Beach%2C_Sentosa%2C_Singapore_-_20140213.jpg",
    "CABLE": "https://upload.wikimedia.org/wikipedia/commons/thumb/2/25/Singapore_cable_car_01.jpg/1280px-Singapore_cable_car_01.jpg",
    "MAP2": "/assets/images/blakang-mati-map-2.png",
    "MONORAIL": "https://upload.wikimedia.org/wikipedia/commons/thumb/b/b2/Sentosa_Monorail%2C_August_1996.jpg/1280px-Sentosa_Monorail%2C_August_1996.jpg",
    "EARTH": "https://upload.wikimedia.org/wikipedia/commons/thumb/4/4d/Sentosa_Satellite_Earth_Station.jpg/1280px-Sentosa_Satellite_Earth_Station.jpg",
    "FSENT": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/d6/Fort_Siloso_entrance.jpg/1280px-Fort_Siloso_entrance.jpg",
    "SUMMIT": "https://upload.wikimedia.org/wikipedia/commons/b/b8/Trump_Kim_Summit_at_the_Capella_Hotel_%281%29.jpg",
    "CORRIDOR": "https://upload.wikimedia.org/wikipedia/commons/3/37/Trump_and_Kim_walking_in_the_corridor.jpg",
    "CAPELLA": "https://upload.wikimedia.org/wikipedia/commons/a/a8/Capella_Singapore_aerial_view.jpg",
    "TIMELINE": "/assets/images/blakang-mati-timeline-chart.png",
}

# Credits for images not captioned in the post or its gallery.
CREDITS = {
    "TIMELINE": "Timeline by Lesser Known Singapore",
    "MAP0": "Map by Lesser Known Singapore; map data © OpenStreetMap contributors",
    "MAP1": "Map by Lesser Known Singapore; map data © OpenStreetMap contributors",
    "MAP2": "Map by Lesser Known Singapore; map data © OpenStreetMap contributors",
    "PANO": "Banej, CC BY-SA 4.0, via Wikimedia Commons",
    "SKY2006": "Terence Ong, CC BY 2.5, via Wikimedia Commons",
    "SKY2004": "Orderinchaos, CC BY-SA 4.0, via Wikimedia Commons",
    "STJAMES": "Max H. Hilckes, KITLV, CC BY 4.0, via Wikimedia Commons",
    "ENTRANCE": "Unknown photographer, KITLV, public domain, via Wikimedia Commons",
    "BCP": "FN-082, CC BY-SA 4.0, via Wikimedia Commons",
    "REPLICA": "Masteraah, CC BY-SA 2.0 DE, via Wikimedia Commons",
    "WARYEARS": "Moheen Reeyad, CC BY-SA 4.0, via Wikimedia Commons",
    "ARTAVE": "Sengkang, copyrighted free use, via Wikimedia Commons",
    "PALAWAN": "RM Bulseco, CC BY 2.0, via Wikimedia Commons",
    "EARTH": "Kai Hendry, CC BY 2.0, via Wikimedia Commons",
    "FSENT": "Apetrov09703, CC BY-SA 4.0, via Wikimedia Commons",
    "SUMMIT": "Shealah Craighead, The White House, public domain, via Wikimedia Commons",
    "CAPELLA": "dronepicr, CC BY 2.0, via Wikimedia Commons",
}

_E = "ease-in-out"
_IN = {"type": "cover", "zoom": [1.0, 1.06, 1.12], "pan": [(0.5, 0.5)] * 3, "ease": _E}
_OUT = {"type": "cover", "zoom": [1.12, 1.06, 1.0], "pan": [(0.5, 0.5)] * 3, "ease": _E}
# Portrait-shaped images, the Erédia map and the newspaper page: letterbox, modest zoom.
_PORT = {"type": "letterbox", "zoom": [1.0, 1.04, 1.08], "pan": [(0.5, 0.5)] * 3, "ease": _E}
# The maps and the timeline: letterbox, frozen.
_GFX = {"type": "letterbox", "zoom": [1, 1, 1], "pan": [(0.5, 0.5)] * 3}

SLIDES = [
    {"img": "HERO", **_IN},           # 0  s0  title
    {"img": "PANO", **_IN},           # 1  s1  the island we now call Sentosa
    {"img": "KEPPEL", **_IN},         # 2  s2  1,000 people in two kampongs by 1959
    {"img": "SKY2006", **_IN},        # 3  s3  renamed Sentosa; villagers to Telok Blangah
    {"img": "EREDIA", **_PORT},       # 4  s4  Eredia's 1604 map (his work, no portrait)
    {"img": "PORT1890", **_IN},       # 5  s6  behind death, dead back
    {"img": "ENTRANCE", **_IN},       # 6  s7  pirates in the strait; buried there (s8)
    {"img": "NEWPORT", **_IN},        # 7  s9  ships anchored off the western tip
    {"img": "HERO", **_OUT},          # 8  s10  the naturalist's Malay houses; signal station (s11)
    {"img": "STJAMES", **_IN},        # 9  s12  Robert Little's three villages (no portrait)
    {"img": "BRANI", **_IN},          # 10  s15  the Bugis women's sarongs
    {"img": "NH1910", **_IN},         # 11  s16  the 1827 warning; work begins 1878
    {"img": "IMBIAH", **_IN},         # 12  s18  Serapong and Imbiah; leases; Fort Palmer (s20)
    {"img": "MAP0", **_GFX},          # 13  s21  the garrison town
    {"img": "SILOSO", **_IN},         # 14  s23  Indian gunners; local workers; sampan (s25)
    {"img": "GUNS", **_IN},           # 15  s26  war: the guns, the bombs
    {"img": "REPLICA", **_IN},        # 16  s28  fired inland
    {"img": "BCP", **_IN},            # 17  s29  Siloso blown up; surrender (s30)
    {"img": "MAP1945", **_GFX},       # 18  s31  Kashima; prisoners of war
    {"img": "WARYEARS", **_PORT},     # 19  s33  the Sook Ching killings
    {"img": "SKY2004", **_IN},        # 20  s36  the Berhala Reping marker, golf club
    {"img": "FERRY", **_IN},          # 21  s37  after the war; 377 residents; 1,000
    {"img": "USS", **_IN},            # 22  s40  the Hokkien village by the jetty; the Yeos
    {"img": "MAP1", **_GFX},          # 23  s42  the Malay village; Lee Kuan Yew 1964 (no portrait); festivals
    {"img": "NH1910", **_OUT},        # 24  s45  fishing and ferry boats; garrison jobs
    {"img": "PORT1890", **_OUT},      # 25  s48  tailor, photographer; boatmen and ships
    {"img": "KEPPEL", **_OUT},        # 26  s50  a boatman's son
    {"img": "ST1948", **_PORT},       # 27  s51  the 1948 ferry notice
    {"img": "ENTRANCE", **_OUT},      # 28  s53  sampan fares; islanders wrote to the papers (s54)
    {"img": "FERRY", **_OUT},         # 29  s55  water; the 1959 pipeline
    {"img": "NEWPORT", **_OUT},       # 30  s57  schools, mosque, temples
    {"img": "ARTAVE", **_IN},         # 31  s60  Gurkha battalions
    {"img": "SKY2006", **_OUT},       # 32  s61  1963 agreement; 1967 handover; uses
    {"img": "SKY2004", **_OUT},       # 33  s63  E. W. Barker's remark (no portrait)
    {"img": "RWS", **_IN},            # 34  s64  Esso refinery; Winsemius and Choe (no portraits)
    {"img": "PALAWAN", **_IN},        # 35  s66  a resort; renamed Sentosa 1970
    {"img": "CABLE", **_IN},          # 36  s68  SDC 1972; cable car 1974
    {"img": "MAP2", **_GFX},          # 37  s69  villagers moved to Telok Blangah
    {"img": "MONORAIL", **_IN},       # 38  s71  jobs at the attractions; unusual tasks (s72)
    {"img": "EARTH", **_IN},          # 39  s73  the satellite earth station, 1971
    {"img": "FSENT", **_IN},          # 40  s74  Chia Thye Poh (no portrait)
    {"img": "BCP", **_OUT},           # 41  s76  the Fort Siloso guardhouse, 1989-92
    {"img": "SUMMIT", **_IN},         # 42  s77  Trump and Kim, 12 June 2018 (names both; shows both)
    {"img": "CORRIDOR", **_IN},       # 43  s78  the Capella and the old Officers' Mess
    {"img": "CAPELLA", **_IN},        # 44  s79  the Gurkha Contingent
    {"img": "SILOSO", **_OUT},        # 45  s80  Fort Siloso, a National Monument
    {"img": "ARTAVE", **_OUT},        # 46  s81  barracks conserved
    {"img": "SKY2006", **_IN},        # 47  s82  Officers' Mess; old hospital
    {"img": "USS", **_OUT},           # 48  s83  nothing left of the kampongs
    {"img": "PANO", **_OUT},          # 49  s84  the Yeo clan association
    {"img": "TIMELINE", **_GFX},      # 50  s85  why it matters
    {"img": "CABLE", **_OUT},         # 51  s86  forts and barracks keep the story
    {"img": "HERO", **_OUT},          # 52  s87  look for the red roofs
]

SCHEDULE = [(0, 0), (5.15, 1), (19.075, 2), (28.55, 3), (39.4, 4), (58.9, 5), (67.5, 6), (78.575, 7), (87.975, 8), (114.75, 9), (139, 10), (148.625, 11), (172.875, 12), (197.475, 13), (215.35, 14), (244.35, 15), (258.4, 16), (268.2, 17), (284.875, 18), (303.875, 19), (332.1, 20), (339.475, 21), (358.6, 22), (379.7, 23), (405.175, 24), (427.55, 25), (447.375, 26), (455.825, 27), (481.8, 28), (498.175, 29), (525.6, 30), (551.775, 31), (563.5, 32), (590.45, 33), (602.875, 34), (623.425, 35), (641.175, 36), (653.3, 37), (675.15, 38), (689.8, 39), (710.475, 40), (730.375, 41), (747.5, 42), (758.825, 43), (766.2, 44), (777.775, 45), (788.9, 46), (800.55, 47), (810.925, 48), (824.3, 49), (835.425, 50), (853.925, 51), (867.5, 52)]
TOTAL_DURATION = 878.075
TIMING_JSON = "audio/blakang-mati-before-sentosa-the-islands-kampongs-and-barracks.timing.json"

# The avatar presenter, cartoon with motion: corner bubble for the first and last 30 s.
AVATAR = {"ranges": [(0, 30), (-30, None)], "motion": True}
