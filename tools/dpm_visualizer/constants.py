"""Constants for DPM Visualizer."""

# Range modifiers table for accuracy calculation
# Values are percentages as used in HitRollConstants.ndf (e.g., 300 = 300% = 3.0x multiplier)
RANGE_MODIFIERS_TABLE = [
    (0.05, 300),   # 300% multiplier at 5% of max range
    (0.17, 70),    # 70% multiplier at 17% of max range
    (0.33, 50),    # 50% multiplier at 33% of max range
    (0.50, 30),    # 30% multiplier at 50% of max range
    (0.67, 15),    # 15% multiplier at 67% of max range
    (1.00, 0)      # 0% multiplier at max range (no bonus)
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

# Infantry armor damage ratios for small arms
# Table indexed by attacker strength (2-14), then target strength (2-14)
# Example: A 7-strength infantry targeting an 8-strength infantry applies 96% damage
SA_INF_ARMOR_DAMAGE_RATIOS = [
    [1.0,  1.0,  1.0,  1.0,  1.0,  1.0,  1.0,  1.0,  1.0,  1.0,  1.0,  1.0,  1.0 ], # 2 strength
    [1.0,  1.0,  1.0,  1.0,  1.0,  1.0,  1.0,  1.0,  1.0,  1.0,  1.0,  1.0,  0.96], # 3 strength
    [1.0,  1.0,  1.0,  1.0,  1.0,  1.0,  1.0,  1.0,  1.0,  1.0,  1.0,  0.96, 0.92], # 4 strength
    [1.0,  1.0,  1.0,  1.0,  1.0,  1.0,  1.0,  1.0,  1.0,  1.0,  0.96, 0.92, 0.88], # 5 strength
    [1.0,  1.0,  1.0,  1.0,  1.0,  1.0,  1.0,  1.0,  1.0,  0.96, 0.92, 0.88, 0.84], # 6 strength
    [1.0,  1.0,  1.0,  1.0,  1.0,  1.0,  1.0,  1.0,  0.96, 0.92, 0.88, 0.84, 0.8 ], # 7 strength
    [1.0,  1.0,  1.0,  1.0,  1.0,  1.0,  1.0,  0.96, 0.92, 0.88, 0.84, 0.8,  0.76], # 8 strength
    [1.0,  1.0,  1.0,  1.0,  1.0,  1.0,  0.96, 0.92, 0.88, 0.84, 0.8,  0.76, 0.72], # 9 strength
    [1.0,  1.0,  1.0,  1.0,  1.0,  0.96, 0.92, 0.88, 0.84, 0.8,  0.76, 0.72, 0.68], # 10 strength
    [1.0,  1.0,  1.0,  1.0,  0.96, 0.92, 0.88, 0.84, 0.8,  0.76, 0.72, 0.68, 0.64], # 11 strength
    [1.0,  1.0,  1.0,  0.96, 0.92, 0.88, 0.84, 0.8,  0.76, 0.72, 0.68, 0.64, 0.6 ], # 12 strength
    [1.0,  1.0,  0.96, 0.92, 0.88, 0.84, 0.8,  0.76, 0.72, 0.68, 0.64, 0.6,  0.56], # 13 strength
    [1.0,  0.96, 0.92, 0.88, 0.84, 0.8,  0.76, 0.72, 0.68, 0.64, 0.6,  0.56, 0.52], # 14 strength
]

