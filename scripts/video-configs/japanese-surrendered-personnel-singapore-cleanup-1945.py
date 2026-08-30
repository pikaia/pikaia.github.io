"""Video config for "The Japanese Soldiers Who Rebuilt Postwar Singapore
Were Never Called Prisoners" - Watch widget and main video.

No chart in this post. Every image is an ~800px IWM / RAF official
photograph (public domain), so the whole video is letterbox slides
(blurred-bg zoom, zero pan) - --check-only flags all of them JERKY,
the documented letterbox false positive (pipeline section 5). Several
slides hold 17-23s over one long sentence with no closer boundary;
slow wide zooms carry them.

Images (3 post + 7 gallery, all letterbox - largest aspect is 1.43,
just under the 1.44 cover threshold):
  SE4843  - crowd of civilians watching Japanese POWs clear up outside
            the Municipal Building, 1945 (post hero)
  IND4826 - Japanese POWs marched at the double to cleanup work, 1945
            (post inline) - the "the work" image
  SE4887  - Japanese medical orderlies at the JSP labour camp near
            Seletar, 1945 (post floated) - matches the s17 narration
  SE4702  - the Japanese surrender delegation on the Municipal Building
            steps, 12 Sep 1945 (gallery)
  SE4723  - Royal Marines band at the victory parade, 1945 (gallery)
  MOUNTB  - Mountbatten inspecting a guard of honour, Sep 1945 (gallery)
            - the SEAC command that adopted the "surrendered personnel"
            designation
  SE4649  - 5th Indian Division riding through Singapore with the
            reoccupation force, 1945 (gallery)
  DOCKS   - RAF driver surveying Allied bomb damage at Singapore docks,
            1945 (gallery)
  CRUISER - a damaged Japanese cruiser at Singapore, 25 Sep 1945
            (gallery)
  JAVA    - a Japanese surrendered soldier watching an RAF Dakota land
            at Bandoeng, Java, May 1946 (gallery) - the SEAC-wide beat

All 10 images carry captions in the post or its gallery, so
stage_youtube_text.py resolves every credit - no CREDITS block needed.

21 slides, 305.83s.
"""

_C = "https://upload.wikimedia.org/wikipedia/commons"

IMAGES = {
    "SE4843": f"{_C}/7/70/The_British_Reoccupation_of_Singapore_SE4843.jpg",
    "IND4826": f"{_C}/e/e5/British_Reoccupation_of_Singapore%2C_1945_IND4826.jpg",
    "SE4887": f"{_C}/0/0d/The_British_Reoccupation_of_Singapore_SE4887.jpg",
    "SE4702": f"{_C}/c/ca/The_Japanese_Southern_Armies_Surrender_at_Singapore%2C_1945_SE4702.jpg",
    "SE4723": f"{_C}/7/7b/The_Japanese_Southern_Armies_Surrender_at_Singapore%2C_1945_SE4723.jpg",
    "MOUNTB": f"{_C}/e/ea/Louis_Mountbatten_Inspection%2C_Singapore_1945.jpg",
    "SE4649": f"{_C}/4/48/British_Reoccupation_of_Singapore%2C_1945_SE4649.jpg",
    "DOCKS": f"{_C}/f/fd/Damage_caused_by_Allied_bombing.jpg",
    "CRUISER": f"{_C}/e/e4/CAPTAIN_POWER_VISITS_DAMAGED_JAPANESE_CRUISER._25_SEPTEMBER_1945%2C_SINGAPORE.jpg",
    "JAVA": f"{_C}/c/c4/Japanese_POW_in_Java_during_1946.jpg",
}

SLIDES = [
    {"img": "SE4843", "type": "letterbox", "zoom": [1, 1.05, 1.10], "pan": [(0.5, 0.5), (0.5, 0.5), (0.5, 0.5)], "ease": "ease-in-out"},
    {"img": "IND4826", "type": "letterbox", "zoom": [1, 1.05, 1.10], "pan": [(0.5, 0.5), (0.5, 0.5), (0.5, 0.5)], "ease": "ease-in"},
    {"img": "SE4843", "type": "letterbox", "zoom": [1.10, 1.05, 1], "pan": [(0.5, 0.5), (0.5, 0.5), (0.5, 0.5)], "ease": "ease-out"},
    {"img": "SE4702", "type": "letterbox", "zoom": [1, 1.05, 1.10], "pan": [(0.5, 0.5), (0.5, 0.5), (0.5, 0.5)], "ease": "ease-in-out"},
    {"img": "MOUNTB", "type": "letterbox", "zoom": [1, 1.06, 1.12], "pan": [(0.5, 0.5), (0.5, 0.5), (0.5, 0.5)], "ease": "ease-in-out"},
    {"img": "JAVA", "type": "letterbox", "zoom": [1, 1.06, 1.12], "pan": [(0.5, 0.5), (0.5, 0.5), (0.5, 0.5)], "ease": "ease-in"},
    {"img": "DOCKS", "type": "letterbox", "zoom": [1, 1.06, 1.12], "pan": [(0.5, 0.5), (0.5, 0.5), (0.5, 0.5)], "ease": "ease-in-out"},
    {"img": "SE4649", "type": "letterbox", "zoom": [1.12, 1.06, 1], "pan": [(0.5, 0.5), (0.5, 0.5), (0.5, 0.5)], "ease": "ease-out"},
    {"img": "DOCKS", "type": "letterbox", "zoom": [1.10, 1.05, 1], "pan": [(0.5, 0.5), (0.5, 0.5), (0.5, 0.5)], "ease": "ease-out"},
    {"img": "IND4826", "type": "letterbox", "zoom": [1, 1.06, 1.12], "pan": [(0.5, 0.5), (0.5, 0.5), (0.5, 0.5)], "ease": "ease-in-out"},
    {"img": "SE4843", "type": "letterbox", "zoom": [1, 1.05, 1.10], "pan": [(0.5, 0.5), (0.5, 0.5), (0.5, 0.5)], "ease": "ease-in-out"},
    {"img": "IND4826", "type": "letterbox", "zoom": [1.10, 1.05, 1], "pan": [(0.5, 0.5), (0.5, 0.5), (0.5, 0.5)], "ease": "ease-out"},
    {"img": "SE4887", "type": "letterbox", "zoom": [1, 1.05, 1.10], "pan": [(0.5, 0.5), (0.5, 0.5), (0.5, 0.5)], "ease": "ease-in"},
    {"img": "SE4887", "type": "letterbox", "zoom": [1.10, 1.05, 1], "pan": [(0.5, 0.5), (0.5, 0.5), (0.5, 0.5)], "ease": "ease-out"},
    {"img": "SE4649", "type": "letterbox", "zoom": [1, 1.06, 1.12], "pan": [(0.5, 0.5), (0.5, 0.5), (0.5, 0.5)], "ease": "ease-in-out"},
    {"img": "SE4887", "type": "letterbox", "zoom": [1, 1.05, 1.10], "pan": [(0.5, 0.5), (0.5, 0.5), (0.5, 0.5)], "ease": "ease-in-out"},
    {"img": "CRUISER", "type": "letterbox", "zoom": [1, 1.06, 1.12], "pan": [(0.5, 0.5), (0.5, 0.5), (0.5, 0.5)], "ease": "ease-in-out"},
    {"img": "JAVA", "type": "letterbox", "zoom": [1.10, 1.05, 1], "pan": [(0.5, 0.5), (0.5, 0.5), (0.5, 0.5)], "ease": "ease-out"},
    {"img": "SE4723", "type": "letterbox", "zoom": [1, 1.05, 1.10], "pan": [(0.5, 0.5), (0.5, 0.5), (0.5, 0.5)], "ease": "ease-in-out"},
    {"img": "IND4826", "type": "letterbox", "zoom": [1, 1.06, 1.12], "pan": [(0.5, 0.5), (0.5, 0.5), (0.5, 0.5)], "ease": "ease-in-out"},
    {"img": "SE4702", "type": "letterbox", "zoom": [1.10, 1.05, 1], "pan": [(0.5, 0.5), (0.5, 0.5), (0.5, 0.5)], "ease": "ease-out"},
]

# Real values from
# audio/japanese-surrendered-personnel-singapore-cleanup-1945.timing.json.
# Every point is a real sentence start.
#   0  s0-1   title; Jan 1947, ten days into the municipal strike, the men
#             clearing the drains were Japanese soldiers
#   1  s2     they belonged to the army that had run the island until
#             eighteen months earlier
#   2  s3     the Straits Times photo caption could not settle on a word:
#             "Dismal Days For The POWs", in inverted commas
#   3  s4-5   officially not prisoners of war - that was the whole point;
#             the category was Japanese Surrendered Personnel, Japan's idea
#   4  s6-7   last weeks of the war, Tokyo proposed "surrendered personnel",
#             no basis in law; the Allies, Britain in particular, accepted
#   5  s8-9   a POW was covered by the 1929 Geneva Convention - prompt
#             repatriation, no military-linked labour; a surrendered person
#             was covered by none of it
#   6  s10    Britain came out of the war short of manpower and shipping,
#             colonies to rebuild - the disarmed troops were how it proposed
#             to do the work
#   7  s11    ~35,000 moved to Johor after Sep 1945, but tens of thousands
#             stayed as a labour pool and Singapore drew on them heavily
#   8  s12-13 the city was in poor shape; Allied aircraft had bombed the
#             docks and Keppel Harbour, utilities unreliable
#   9  s14    set to the wharves and the Seletar naval base, roads and
#             railway bridges - the Connaught bridge on the Klang line -
#             rubble, and exhuming the occupation's mass graves
#   10 s15    repatriation announced early 1947; the Municipal President,
#             Mr Rayman, objected - the municipality could not replace them
#   11 s16    organised as army labour battalions, under guard; the
#             conditions were not gentle
#   12 s17    a photo from the camp near Seletar: medical orderlies in
#             masks, preparing for "the sick and dying"
#   13 s18    April 1947, a man from the RAF Tengah camp remanded on a
#             charge of killing another with an axe
#   14 s19    that July the rules narrowed: from 1 August no "non-essential"
#             work, grooms among the banned jobs, basic reconstruction only
#   15 s20    the same month, an English missionary who spoke Japanese was
#             months into welfare work in the camps
#   16 s21-22 repatriation ran in batches; the first 132 left on the
#             troopship Dilwara in March, then Japanese-manned ships from
#             Seletar
#   17 s23    the last JSP held anywhere under South East Asia Command went
#             home in October 1947
#   18 s24    historians have noted the Allies took care not to draw
#             attention to how much recovery ran on Japanese labour
#   19 s25    where it fits: a real portion of the work that got Singapore
#             running again - cleared sites, repaired quays, drains
#             unblocked in the rain - was done by the former occupier
#   20 s26    done under a name settled on jointly by the defeated and the
#             victors, chosen so neither had to describe the arrangement
SCHEDULE = [
    (0.0, 0), (19.48, 1), (25.15, 2), (37.92, 3), (50.38, 4),
    (69.0, 5), (89.42, 6), (110.05, 7), (127.4, 8), (139.65, 9),
    (162.18, 10), (177.95, 11), (184.75, 12), (196.03, 13), (205.1, 14),
    (221.8, 15), (231.32, 16), (253.5, 17), (263.05, 18), (274.82, 19),
    (293.85, 20),
]
TOTAL_DURATION = 305.83
TIMING_JSON = "audio/japanese-surrendered-personnel-singapore-cleanup-1945.timing.json"
