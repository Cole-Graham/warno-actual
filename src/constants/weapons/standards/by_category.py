"""Standards keyed by ammunition/missile dictionary category.

Each constant maps NDF descriptor sections to override values,
consumed by category-specific handlers in gameplay_mods.
"""

from typing import FrozenSet, Tuple

# (multiplier, base_member_name) -- target member = round(multiplier * value(base_member))
RatioSpec = Tuple[float, str]

# -- AA missiles (A2A / SAM / MANPAD) -------------------------------------
#
# Range-scaled accuracy is disabled (``DistanceToTarget = False``) only on
# missile descriptors that exclusively engage planes:
#   * ``_HAGRU`` variants, which use a damage family that ignores helicopters.
#   * Non-HAGRU SAM/A2A originals whose ``MaximumRangeHelicopterGRU`` is 0
#     (the missile has no helicopter engagement range and is plane-only by
#     virtue of its range envelope, e.g. AA_R98MT, AA_Skyflash).
# All other AA missiles keep the vanilla default (``True``) so accuracy still
# degrades with range when engaging helicopters.

A2A_STANDARDS: dict = {}

SAM_STANDARDS: dict = {}

MANPAD_STANDARDS: dict = {}

AA_HAGRU_STANDARDS: dict = {
    "hit_roll": {
        "DistanceToTarget": False,
    },
}

# AdditionalSuppressDamagePerLostPhysicalDamage = 25 // c'est un multiplicateur des degats physiques qu'on va appliquer en stress.
# GDConstants.ndf value. The engine adds this * PhysicalDamages to the written
# ``SuppressDamages`` at runtime, so the handler must subtract the same product
# from the intended total below before writing the descriptor.
#
# Stun alignment note: the engine deals stun damage equal to the *written*
# ``SuppressDamages`` (the ``- 25*P`` value below), not the intended total --
# the engine bonus only applies to suppress, not stun. With
# ``Airplane_MaxStunDamages = 255`` and the airplane stun pack threshold at
# 0.70, the stun pack fires when cumulative written suppress reaches 178.5.
# The intended I values are tuned so every "must stun" case clears that
# threshold by >= 11 written suppress (>= 11 sec of stun-regen tolerance, since
# Airplane_StunDamagesRegen = 1/sec) and every "must NOT stun" case stays
# below it by >= 18. Suppress-side intent (350 on Ms = 500) is preserved by
# the original I values in the comments. Phys 4 multi-missile salvos
# suppress-stun but never stun-pack-stun (acceptable low-tier edge). SPAAGs
# use a separate ``DamageFamily_he_dca_airtargets`` air ammo whose written
# suppress is reduced (default 2/3 of vanilla) so the same stun pack
# threshold also matches each SPAAG's vanilla suppress-stun timing without
# affecting its ground performance.
AA_ADDITIONAL_SUPPRESS_PER_LOST_PHYSICAL: int = 25

# Intended total suppress damage (written value + engine bonus) by PhysicalDamages.
# Targets suppress-stunned at 350 damage (suppress pack threshold = 0.70 * 500).
# Stun pack also fires (Airplane_MaxStunDamages=255, threshold = 178.5 written W).
# I values are tuned so the binding "must stun" cases (phys 7 fresh, phys 9 vet 2,
# phys 6 vet 3 two-shot) all clear the stun threshold by >= 11 W with the
# 25*P engine bonus accounted for, while preserving the original suppress-side
# design (e.g. phys 7 vet 2 still does NOT suppress-stun, phys 6 vet 3 two-shot
# still does).
AA_SUPPRESS_BY_PHYSICAL_DAMAGE: dict[int, int] = {
    9: 465, # Target at vet 2 with 20% suppression resistance, will still stun
    8: 465,
    7: 365, # Target at vet 2 with 20% suppression resistance, will NOT stun
    6: 310, # Target at vet 3 with 40% suppression resistance, 2 shots will still stun
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
