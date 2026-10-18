"""Video config for the Tanjong Katong post.

The seafront from the 1840s to today, told through Taylor's 1879 watercolours,
KITLV photographs of the Katong shore, the Sea View Hotel and Crescent Flats,
the three-stage shoreline map, the timeline and present-day photos of Sea Breeze
Lodge, Katong Park, Meyer Road and Marine Parade. No portraits: Dunman, Buckley,
Choa Kim Keat, Manasseh Meyer, the Sarkies brothers, Lee Choon Guan and Eric Choa
are named over places, never over someone else's face. The 1950s bathers photo
(s39) sits under the sentence about post-war swimmers at Marine Parade.
Portrait-shaped photos and the 1942 map are letterboxed with a modest zoom; the
maps and timeline are letterboxed and frozen.
Video-only: three more KITLV shore views, the 1942 map, a second Sea Breeze Lodge
view, Katong Park, the Meyer Road junction, a Marine Parade HDB block and the
Tanjong Katong high rises.

48 slides, 710.725s. Narration: Kokoro with the OpenVoice clone.
AVATAR: first and last 30s, cartoon with motion.
"""

IMAGES = {
    "HERO": "https://upload.wikimedia.org/wikipedia/commons/thumb/3/38/John_Edmund_Taylor%2C_Singapore._From_Tanjong_Katong._%281879%2C_Wellcome_V0037488%29.jpg/1280px-John_Edmund_Taylor%2C_Singapore._From_Tanjong_Katong._%281879%2C_Wellcome_V0037488%29.jpg",
    "BUNGALOWS": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/d9/John_Edmund_Taylor%2C_Under_the_Cocoa_Nut_Trees._The_Bungalows._Tanjong_Katong%2C_Singapore._%281879%2C_Wellcome_V0037492%29.jpg/1280px-John_Edmund_Taylor%2C_Under_the_Cocoa_Nut_Trees._The_Bungalows._Tanjong_Katong%2C_Singapore._%281879%2C_Wellcome_V0037492%29.jpg",
    "LODGE24": "https://upload.wikimedia.org/wikipedia/commons/thumb/0/00/%28SGP-Singapore%29_Sea_Breeze_Lodge_2024-08-17.jpg/1280px-%28SGP-Singapore%29_Sea_Breeze_Lodge_2024-08-17.jpg",
    "BEACH": "https://upload.wikimedia.org/wikipedia/commons/thumb/9/93/Strand_van_Tanjong_Katong_te_Singapore%2C_KITLV_104808.tiff/lossy-page1-1280px-Strand_van_Tanjong_Katong_te_Singapore%2C_KITLV_104808.tiff.jpg",
    "SEAVIEW": "https://upload.wikimedia.org/wikipedia/commons/thumb/4/4b/Sea_View_Hotel_te_Singapore%2C_KITLV_104797.tiff/lossy-page1-1280px-Sea_View_Hotel_te_Singapore%2C_KITLV_104797.tiff.jpg",
    "CRESCENT": "https://upload.wikimedia.org/wikipedia/commons/thumb/8/8d/Crescent_flats_Tanjong_Katon%2C_Singapore%2C_KITLV_1404949.tiff/lossy-page1-1280px-Crescent_flats_Tanjong_Katon%2C_Singapore%2C_KITLV_1404949.tiff.jpg",
    "SWIM": "https://upload.wikimedia.org/wikipedia/commons/0/04/Indians-MarineParade-Singapore-1950s.jpg",
    "MRT": "https://upload.wikimedia.org/wikipedia/commons/thumb/0/06/%28SGP-Singapore%29_Katong_Park_MRT_Station_Exit_1_2024-06-23.jpg/1280px-%28SGP-Singapore%29_Katong_Park_MRT_Station_Exit_1_2024-06-23.jpg",
    "LODGE25": "https://upload.wikimedia.org/wikipedia/commons/thumb/9/9a/Sea_Breeze_Lodge_%28Choa_Family_Bungalow%29_Marine_Parade%2C_Singapore_%282025%29_-_img_01.jpg/1280px-Sea_Breeze_Lodge_%28Choa_Family_Bungalow%29_Marine_Parade%2C_Singapore_%282025%29_-_img_01.jpg",
    "MAP1": "/assets/images/katong-shore-map-1.png",
    "MAP2": "/assets/images/katong-shore-map-2.png",
    "TIMELINE": "/assets/images/katong-timeline-chart.png",
    "POINT": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/db/John_Edmund_Taylor%2C_The_Point._Tanjong_Katong._%281879%2C_Wellcome_V0037485%29.jpg/1280px-John_Edmund_Taylor%2C_The_Point._Tanjong_Katong._%281879%2C_Wellcome_V0037485%29.jpg",
    "LOOKING": "https://upload.wikimedia.org/wikipedia/commons/thumb/6/6f/John_Edmund_Taylor%2C_Tanjong_Katong%2C_Looking_towards_Singapore_%281879%2C_Wellcome_V0037481%29.jpg/1280px-John_Edmund_Taylor%2C_Tanjong_Katong%2C_Looking_towards_Singapore_%281879%2C_Wellcome_V0037481%29.jpg",
    "COCO": "https://upload.wikimedia.org/wikipedia/commons/thumb/4/48/Cocoanut_plantation_Tanjong_Katong._Singapore.%2C_KITLV_1404873.tiff/lossy-page1-1280px-Cocoanut_plantation_Tanjong_Katong._Singapore.%2C_KITLV_1404873.tiff.jpg",
    "PLATE20": "https://upload.wikimedia.org/wikipedia/commons/6/66/Photographic_Views_of_Singapore_Plate_20_Scenery_at_Tanjong_Katong.jpg",
    "PALM": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/d4/Tandjong_Katong%2C_Singapore%2C_KITLV_1407451.tiff/lossy-page1-1280px-Tandjong_Katong%2C_Singapore%2C_KITLV_1407451.tiff.jpg",
    "HUT": "https://upload.wikimedia.org/wikipedia/commons/thumb/9/90/Tanjong_W_ton%2C_Singapore%2C_KITLV_1404753.tiff/lossy-page1-1280px-Tanjong_W_ton%2C_Singapore%2C_KITLV_1404753.tiff.jpg",
    "ROAD": "https://upload.wikimedia.org/wikipedia/commons/thumb/1/16/Tanjong_Katon_Singapore%2C_KITLV_1404950.tiff/lossy-page1-1280px-Tanjong_Katon_Singapore%2C_KITLV_1404950.tiff.jpg",
    "SEAVIEW2": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/dc/Sea_View_Hotel%2C_Singapore%2C_KITLV_1407450.tiff/lossy-page1-1280px-Sea_View_Hotel%2C_Singapore%2C_KITLV_1407450.tiff.jpg",
    "FORTREM": "https://upload.wikimedia.org/wikipedia/commons/d/de/Remains_of_Fort_Tanjong_Katong%2C_Katong_Park%2C_Singapore_-_20060826.jpg",
    "ECP": "https://upload.wikimedia.org/wikipedia/commons/thumb/f/f3/Singapore_-_Marine_Parade_-_east_coast_park_IMG_9176.jpg/1280px-Singapore_-_Marine_Parade_-_east_coast_park_IMG_9176.jpg",
    "SHORE1404758": "https://upload.wikimedia.org/wikipedia/commons/thumb/0/01/Tanjong_Katong%2C_Singapore%2C_KITLV_1404758.tiff/lossy-page1-1280px-Tanjong_Katong%2C_Singapore%2C_KITLV_1404758.tiff.jpg",
    "NIGHT": "https://upload.wikimedia.org/wikipedia/commons/thumb/b/b7/Tandjong_Kantong%2C_Singapore.%2C_KITLV_1404859.tiff/lossy-page1-1280px-Tandjong_Kantong%2C_Singapore.%2C_KITLV_1404859.tiff.jpg",
    "PALMS2": "https://upload.wikimedia.org/wikipedia/commons/thumb/2/2e/Tandjong_Katong%2C_Singapore%2C_KITLV_1407452.tiff/lossy-page1-1280px-Tandjong_Katong%2C_Singapore%2C_KITLV_1407452.tiff.jpg",
    "LODGE25B": "https://upload.wikimedia.org/wikipedia/commons/thumb/2/23/Sea_Breeze_Lodge_%28Choa_Family_Bungalow%29_Marine_Parade%2C_Singapore_%282025%29_-_img_03.jpg/1280px-Sea_Breeze_Lodge_%28Choa_Family_Bungalow%29_Marine_Parade%2C_Singapore_%282025%29_-_img_03.jpg",
    "KPARK": "https://upload.wikimedia.org/wikipedia/commons/thumb/9/9b/Katong_Park.jpg/1280px-Katong_Park.jpg",
    "JUNCTION": "https://upload.wikimedia.org/wikipedia/commons/thumb/b/be/Junction_of_Meyer_Road_and_Tanjong_Katong_Road_South.jpg/1280px-Junction_of_Meyer_Road_and_Tanjong_Katong_Road_South.jpg",
    "HDB": "https://upload.wikimedia.org/wikipedia/commons/9/96/Marine_Parade_Housing_Estate%2C_Typical_point_block%2C_Dec_05.JPG",
    "HIGHRISE": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/db/Tanjong_Katong%2C_Singapore_high_rises_December_2024.jpg/1280px-Tanjong_Katong%2C_Singapore_high_rises_December_2024.jpg",
    "MAP1942": "https://upload.wikimedia.org/wikipedia/commons/thumb/4/46/Singapore_map_1942.jpg/1280px-Singapore_map_1942.jpg",
}

# Credits for images not captioned in the post or its gallery.
CREDITS = {
    "TIMELINE": "Timeline by Lesser Known Singapore",
    "MAP1": "Map by Lesser Known Singapore; map data (c) OpenStreetMap contributors",
    "MAP2": "Map by Lesser Known Singapore; map data (c) OpenStreetMap contributors",
    "SHORE1404758": "Unknown photographer, KITLV, CC BY 4.0, via Wikimedia Commons",
    "NIGHT": "Unknown photographer, KITLV, CC BY 4.0, via Wikimedia Commons",
    "PALMS2": "Unknown photographer, KITLV, CC BY 4.0, via Wikimedia Commons",
    "LODGE25B": "Chainwit., CC BY 4.0, via Wikimedia Commons",
    "KPARK": "Zenney100, CC BY-SA 4.0, via Wikimedia Commons",
    "JUNCTION": "Imbluey2, CC BY-SA 4.0, via Wikimedia Commons",
    "HDB": "User:Sengkang, copyrighted free use, via Wikimedia Commons",
    "HIGHRISE": "Sharon Hahn Darlin, CC BY 2.0, via Wikimedia Commons",
    "MAP1942": "Unknown author, public domain, via Wikimedia Commons",
}

_E = "ease-in-out"
_IN = {"type": "cover", "zoom": [1.0, 1.06, 1.12], "pan": [(0.5, 0.5)] * 3, "ease": _E}
_OUT = {"type": "cover", "zoom": [1.12, 1.06, 1.0], "pan": [(0.5, 0.5)] * 3, "ease": _E}
# Portrait-shaped photos and the 1942 map: letterbox, modest zoom.
_PORT = {"type": "letterbox", "zoom": [1.0, 1.04, 1.08], "pan": [(0.5, 0.5)] * 3, "ease": _E}
_PORT_OUT = {"type": "letterbox", "zoom": [1.08, 1.04, 1.0], "pan": [(0.5, 0.5)] * 3, "ease": _E}
# The shoreline maps and the timeline: letterbox, frozen.
_GFX = {"type": "letterbox", "zoom": [1, 1, 1], "pan": [(0.5, 0.5)] * 3}

SLIDES = [
    {"img": "HERO", **_IN},               # 0  s0  title
    {"img": "BEACH", **_IN},              # 1  s1  Singapore's seaside
    {"img": "PALM", **_IN},               # 2  s2  Meyer Road and Marine Parade Road on the beach
    {"img": "MAP2", **_GFX},              # 3  s3  the sea now several hundred metres away; the MRT
    {"img": "TIMELINE", **_GFX},          # 4  s4  coconut coast to inland suburb
    {"img": "COCO", **_PORT},             # 5  s5  'turtle point'; cotton, then coconuts (s6)
    {"img": "PLATE20", **_PORT},          # 6  s7  660 acres of coconut palms by the 1830s
    {"img": "BUNGALOWS", **_IN},          # 7  s8  Dunman's estate (no portrait)
    {"img": "ROAD", **_IN},               # 8  s9  Grove Estate, along today's Mountbatten Road
    {"img": "BUNGALOWS", **_OUT},         # 9  s10  his house and three shore bungalows; Buckley (s11)
    {"img": "LOOKING", **_IN},            # 10  s12  not alone for long; the 1868 directory (s13)
    {"img": "POINT", **_IN},              # 11  s14  the Tanjong Katong Hotel, 1883; weekend houses
    {"img": "LODGE24", **_IN},            # 12  s15  one still stands: Sea Breeze Lodge, 1898 (s16)
    {"img": "LODGE25B", **_IN},           # 13  s17  raised bungalow, 5 m from the sea; weekend retreat (s18)
    {"img": "HUT", **_IN},                # 14  s19  the beach filled up; Buckley, 1902 (s20)
    {"img": "SHORE1404758", **_IN},       # 15  s21  seafront parcelled out
    {"img": "SEAVIEW", **_IN},            # 16  s22  the Sea View Hotel opens, 1906 (s23); Meyer, no portrait
    {"img": "SEAVIEW2", **_IN},           # 17  s24  'by sea and road'; 40 rooms, the tram (s25)
    {"img": "SEAVIEW", **_OUT},           # 18  s26  the Sarkies brothers, 1923; top three hotels (s27)
    {"img": "NIGHT", **_IN},              # 19  s28  dances most nights
    {"img": "MAP1942", **_PORT},          # 20  s29  the Occupation
    {"img": "HUT", **_OUT},               # 21  s30  swimming clubs; the Tanjong Katong Swimming Party (s31)
    {"img": "PALMS2", **_PORT},           # 22  s32  Amber Road, 1921 (Lee Choon Guan, no portrait); the SSC (s33)
    {"img": "BEACH", **_OUT},             # 23  s34  the 1939 seawater pool
    {"img": "ROAD", **_OUT},              # 24  s35  plantations broken into lots; desirable seafront (s36)
    {"img": "CRESCENT", **_IN},           # 25  s37  Crescent Flats, 1909; Meyer Road houses (s38)
    {"img": "SWIM", **_PORT},             # 26  s39  post-war swimmers at Marine Parade
    {"img": "SHORE1404758", **_OUT},      # 27  s40  the 1952 seawall and promenade
    {"img": "SEAVIEW2", **_OUT},          # 28  s41  the resort era ends; closed and demolished (s42-43)
    {"img": "HIGHRISE", **_PORT},         # 29  s44  the 1969 tower, then a condominium
    {"img": "MAP1", **_GFX},              # 30  s45  1966: the reclamation; hills cut down (s46)
    {"img": "MAP2", **_GFX},              # 31  s47  458 ha by 1971; headland breakwaters (s48)
    {"img": "TIMELINE", **_GFX},          # 32  s49  1,525 ha by 1985
    {"img": "FORTREM", **_IN},            # 33  s50  Katong Park and the swimming club lose the sea
    {"img": "LODGE25", **_IN},            # 34  s51  the Lodge faces a road; the new land (s52)
    {"img": "HDB", **_PORT},              # 35  s53  Marine Parade on reclaimed land; 1974 prices (s54)
    {"img": "ECP", **_IN},                # 36  s55  resale prices, 1988 and 1996
    {"img": "JUNCTION", **_IN},           # 37  s56  Meyer Road condominiums; Meyer Park en bloc (s57)
    {"img": "CRESCENT", **_OUT},          # 38  s58  Crescent and Meyer Flats demolished
    {"img": "MRT", **_IN},                # 39  s59  Katong Park MRT, 2024
    {"img": "LODGE24", **_OUT},           # 40  s60  the last pre-reclamation bungalow; Eric Choa (s61), no portrait
    {"img": "LODGE25B", **_OUT},          # 41  s62  the 2011 sale
    {"img": "LODGE25", **_OUT},           # 42  s63  conserved by URA
    {"img": "MAP2", **_GFX},              # 43  s64  the East Coast may change again: Long Island (s65)
    {"img": "KPARK", **_IN},              # 44  s66  still being studied
    {"img": "HIGHRISE", **_PORT_OUT},     # 45  s67  buyers then and now
    {"img": "HERO", **_OUT},              # 46  s68  why it matters (s69)
    {"img": "LODGE24", **_IN},            # 47  s70  the bungalow marks where the beach was
]

SCHEDULE = [(0.0, 0), (5.925, 1), (11.75, 2), (21.275, 3), (34.4, 4), (49.95, 5), (64.175, 6), (74.675, 7), (85.075, 8), (97.275, 9), (112.55, 10), (128.725, 11), (141.05, 12), (155.25, 13), (168.675, 14), (188.275, 15), (194.8, 16), (213.5, 17), (229.325, 18), (248.0, 19), (255.8, 20), (266.2, 21), (282.65, 22), (302.05, 23), (310.85, 24), (325.15, 25), (343.9, 26), (354.175, 27), (376.325, 28), (398.875, 29), (410.7, 30), (431.225, 31), (455.1, 32), (467.5, 33), (485.15, 34), (495.85, 35), (518.975, 36), (539.575, 37), (563.025, 38), (568.675, 39), (577.175, 40), (592.45, 41), (612.975, 42), (625.7, 43), (645.6, 44), (657.7, 45), (674.4, 46), (695.475, 47)]
TOTAL_DURATION = 710.725
TIMING_JSON = "audio/tanjong-katong-by-the-sea-from-dunmans-bungalows-to-the-seaside-resort.timing.json"

# The avatar presenter, cartoon with motion: corner bubble for the first and last 30 s.
AVATAR = {"ranges": [(0, 30), (-30, None)], "motion": True}
