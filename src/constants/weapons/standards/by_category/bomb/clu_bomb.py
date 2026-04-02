"""Standards for ammunition category `clu_bomb` (cluster bombs).

Each `ratios.ammunition` entry is ``(multiplier, base_member)``: the target NDF member is set to
``round(multiplier * value(base_member))``, with ``base_member`` read from the descriptor (after
edits) or ``game_db`` ammo_properties.
"""

from typing import FrozenSet

from ..types import CategoryStandardEntry


def _clu_bomb_weapon_names() -> FrozenSet[str]:
    from src.constants.weapons.ammunition.bomb import weapons as bomb_weapons

    return frozenset(key[0] for key in bomb_weapons if key[1] == "clu_bomb")


CLU_BOMB_WEAPON_NAMES: FrozenSet[str] = _clu_bomb_weapon_names()

CLU_BOMB_STANDARDS: CategoryStandardEntry = {
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
