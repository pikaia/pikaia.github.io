"""Short config for the Sikh Police Contingent post.

Excerpt: the opening hook (sentences 0-3, 0.0-38.95s): the 1881 arrival, the
165-man contingent, and the community that outlasted it. Ends exactly where
sentence 4 begins in the main config's own timing. Vertical 1080x1920.
"""

WIDTH, HEIGHT = 1080, 1920

IMAGES = {
    "POL1931": "https://upload.wikimedia.org/wikipedia/commons/0/0a/Photograph_of_members_of_the_Sikh_Police_Contingent_in-front_of_Gurdwara_Sahib_Silat_Road_in_1931.jpg",
    "POLICE": "https://upload.wikimedia.org/wikipedia/commons/thumb/c/c0/Politieagenten_voor_het_politiebureau_van_Tanjong_Pagar_in_Singapore_Tanjong_Pagar_police_station_%28titel_op_object%29%2C_RP-F-F01140-AQ.jpg/1920px-Politieagenten_voor_het_politiebureau_van_Tanjong_Pagar_in_Singapore_Tanjong_Pagar_police_station_%28titel_op_object%29%2C_RP-F-F01140-AQ.jpg",
    "MEMBER": "https://upload.wikimedia.org/wikipedia/commons/b/b0/Sikh_Contingent_member%2C_Straits_Settlements_Police.jpg",
    "SILAT2015": "https://thumb.wikimedia.org/wikipedia/commons/thumb/8/88/Silat_Road_Sikh_Temple%2C_Singapore.jpg/1920px-Silat_Road_Sikh_Temple%2C_Singapore.jpg",
}

_VA = {"type": "cover", "zoom": [1.45, 1.5, 1.55], "pan": [(0.3, 0.5), (0.45, 0.5), (0.6, 0.5)], "ease": "ease-in-out"}
_VP = {"type": "cover", "zoom": [1.3, 1.35, 1.4], "pan": [(0.35, 0.55), (0.45, 0.58), (0.55, 0.6)], "ease": "ease-in-out"}
_VM = {"type": "cover", "zoom": [1.0, 1.05, 1.1], "pan": [(0.5, 0.3), (0.5, 0.4), (0.5, 0.5)], "ease": "ease-in-out"}
_VS = {"type": "cover", "zoom": [1.0, 1.05, 1.1], "pan": [(0.35, 0.5), (0.45, 0.5), (0.55, 0.5)], "ease": "ease-in-out"}

SLIDES = [
    {"img": "POL1931", **_VA},  # s0 title
    {"img": "POLICE", **_VP},  # s1 26 March 1881
    {"img": "MEMBER", **_VM},  # s2 165 men
    {"img": "SILAT2015", **_VS},  # s3 community still here
]

SCHEDULE = [(0.0, 0), (5.975, 1), (21.625, 2), (27.875, 3)]
TOTAL_DURATION = 38.95
TIMING_JSON = "audio/the-sikh-police-who-came-in-1881-and-the-community-they-left-behind.timing.json"

BURN_CAPTIONS = True
CAPTION_FONT_RATIO = 0.032
CAPTION_MAX_WIDTH_FRAC = 0.86
CAPTION_Y_FRAC = 0.80
