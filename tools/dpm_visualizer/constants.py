"""Constants for DPM Visualizer."""

# Range modifiers table for accuracy calculation
RANGE_MODIFIERS_TABLE = [
    (0.05, 3.0),    # 200% bonus at 5% of max range (total 300% of base accuracy)
    (0.17, 1.70),   # 70% bonus at 17% of max range
    (0.33, 1.50),   # 50% bonus at 33% of max range
    (0.50, 1.30),   # 30% bonus at 50% of max range
    (0.67, 1.15),   # 15% bonus at 67% of max range
    (1.00, 0)       # 0% bonus at max range
]

# Small arms damage families
SMALL_ARMS_DAMAGE_FAMILIES = {
    "DamageFamily_sniper",
    "DamageFamily_sa_intermediate",
    "DamageFamily_sa_full",
    "DamageFamily_12_7",
    "DamageFamily_14_5",
    "DamageFamily_fmballe",
}

