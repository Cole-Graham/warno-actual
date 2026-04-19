"""Standards keyed by ammunition/missile dictionary category.

Each constant maps NDF descriptor sections to override values,
consumed by category-specific handlers in gameplay_mods.
"""

from typing import FrozenSet, Tuple

# (multiplier, base_member_name) -- target member = round(multiplier * value(base_member))
RatioSpec = Tuple[float, str]

# -- AA missiles (A2A / SAM / MANPAD) -------------------------------------

A2A_STANDARDS: dict = {
    "hit_roll": {
        "DistanceToTarget": False,
    },
}

SAM_STANDARDS: dict = {
    "hit_roll": {
        "DistanceToTarget": False,
    },
}

MANPAD_STANDARDS: dict = {
    "hit_roll": {
        "DistanceToTarget": False,
    },
}

# AdditionalSuppressDamagePerLostPhysicalDamage = 25 // c'est un multiplicateur des degats physiques qu'on va appliquer en stress.
# GDConstants.ndf value. The engine adds this * PhysicalDamages to the written
# ``SuppressDamages`` at runtime, so the handler must subtract the same product
# from the intended total below before writing the descriptor.
AA_ADDITIONAL_SUPPRESS_PER_LOST_PHYSICAL: int = 25

# Intended total suppress damage (written value + engine bonus) by PhysicalDamages.
# Targets stunned at 350 damage.
AA_SUPPRESS_BY_PHYSICAL_DAMAGE: dict[int, int] = {
    9: 450, # Target at vet 2 with 20% suppression resistance, will still stun
    8: 450,
    7: 360, # Target at vet 2 with 20% suppression resistance, will NOT stun
    6: 300, # Target at vet 3 with 40% suppression resistance, 2 shots will still stun
    5: 240,
    4: 180,
}

AA_CATEGORIES: frozenset[str] = frozenset({"A2A", "SAM", "MANPAD"})

# -- DCA autocannon --------------------------------------------------------

DCA_STANDARDS: dict = {
    "hit_roll": {
        "DistanceToTarget": False,
    },
    "experience_unit": {
        "ExperienceMultiplierBonusOnKill": 0.1,
    },
}

# -- SEAD (AntiRadiation) -------------------------------------------------

SEAD_STANDARDS: dict = {
    "Arme": {
        "Family": "DamageFamily_sead_missile_wa",
    },
}

# -- Bombs (fixed values + ratio-based values) ----------------------------


def _clu_bomb_weapon_names() -> FrozenSet[str]:
    from src.constants.weapons.ammunition.bomb import weapons as bomb_weapons

    return frozenset(key[0] for key in bomb_weapons if key[1] == "clu_bomb")


CLU_BOMB_WEAPON_NAMES: FrozenSet[str] = _clu_bomb_weapon_names()

CLU_BOMB_STANDARDS: dict = {
    "fixed_values": {
        "ammunition": {
            "PhysicalDamages": 1,
        },
    },
    # Ratio-based values, e.g. DispersionAtMaxRangeGRU = 1.4 * RadiusSplashPhysicalDamagesGRU
    "ratios": {
        "ammunition": {
            "DispersionAtMaxRangeGRU": (1.3, "RadiusSplashPhysicalDamagesGRU"),
            "DispersionAtMinRangeGRU": (1.3, "RadiusSplashPhysicalDamagesGRU"),
        },
    },
}

BOMB_STANDARDS: dict[str, dict] = {
    "clu_bomb": CLU_BOMB_STANDARDS,
}

BOMB_CATEGORY_WEAPON_WHITELIST: dict[str, FrozenSet[str]] = {
    "clu_bomb": CLU_BOMB_WEAPON_NAMES,
}
