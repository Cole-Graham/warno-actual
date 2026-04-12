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
    "ratios": {
        "ammunition": {
            "DispersionAtMaxRangeGRU": (1.4, "RadiusSplashPhysicalDamagesGRU"),
            "DispersionAtMinRangeGRU": (1.4, "RadiusSplashPhysicalDamagesGRU"),
        },
    },
}

BOMB_STANDARDS: dict[str, dict] = {
    "clu_bomb": CLU_BOMB_STANDARDS,
}

BOMB_CATEGORY_WEAPON_WHITELIST: dict[str, FrozenSet[str]] = {
    "clu_bomb": CLU_BOMB_WEAPON_NAMES,
}
