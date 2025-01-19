"""Vanilla weapon renames and removals."""

AMMUNITION_RENAMES = [
    ("Sniper_M14", "Sniper_M21"),
    ("RocketInf_M72_LAW_66mm", "RocketInf_M72A3_LAW_66mm"),
    ("PM_M4_Carbine", "Commando_733"),
    ("Mortier_M40_tower_107mm", "Mortier_M30_towed_107mm"),
    ("Mortier_M40_towed_107mm_SMOKE", "Mortier_M30_towed_107mm_SMOKE"),
    ("Mortier_M40_107mm_SMOKE", "Mortier_M30_107mm_SMOKE"),
    ("Mortier_M40_107mm", "Mortier_M30_107mm"),
    ("MMG_M60_7_62mm", "MMG_WA_M60E3_7_62mm"),
    ("RocketAir_S13_122mm_x10_avion", "RocketAir_S13_122mm_salvolength10_avion"),
]


AMMUNITION_MISSILES_RENAMES = [
    ("ATGM_9K115_Metis_M", "ATGM_9K115_Metis"),
    ("ATGM_9M119M_Svir", "ATGM_9K120_Svir"),
    ("ATGM_9M119M_Refleks", "ATGM_9M119_Refleks"),
    ("ATGM_9M112_1_Kobra", "ATGM_9M112_Kobra"),
    ("ATGM_9M113_KonkursM_late_x5", "ATGM_9M113M_KonkursM_x5"),
    ("ATGM_9M113_KonkursM_late", "ATGM_9M113M_KonkursM"),
    ("ATGM_9M113_KonkursM", "ATGM_9M113_Konkurs"),
    ("ATGM_9K111M_Fagot_M", "ATGM_9K111M_Faktoriya"),
    ("AGM_Kh28_X28", "AGM_Kh28"),
]

AMMUNITION_REMOVALS = []

AMMUNITION_MISSILES_REMOVALS = [
    "ATGM_9k111M_Faktoriya"
]

MERGED_RENAMES = list(set(AMMUNITION_RENAMES) | set(AMMUNITION_MISSILES_RENAMES))

