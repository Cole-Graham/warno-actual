"""MotSchutzen_RPG29_DDR depiction edits.

Donor ``MotSchutzen_DDR``: WeaponAlternative_1 = AK-74N, _2 / _3 = two RPG-7VR
mounts. Loadout replaces first AT slot with 2x RPK-74 and second with RPG-29.
"""

from typing import Dict, Tuple, Union

# fmt: off
mot_schutzen_rpg29_ddr: Dict[str, Dict[Union[str, Tuple[str, str]], dict]] = {
    "unit_name": "MotSchutzen_RPG29_DDR",
    "valid_files": ["DepictionInfantry.ndf"],
    "DepictionInfantry_ndf": {

        ("AllWeaponAlternatives_MotSchutzen_RPG29_DDR", None): {
            1: ("edit", [("MeshDescriptor", "RPK")]),
            2: ("edit", [("MeshDescriptor", "RPG29")]),
            3: ("edit", [("ReferenceMeshForSkeleton", "RPG29")]),
        },

        ("AllWeaponSubDepiction_MotSchutzen_RPG29_DDR", "TemplateAllSubWeaponDepiction"): {
            "Operators": {
                1: ("edit", [("FireEffectTag", "SAW_lMG_K_7_62mm")]),
                2: ("edit", [("FireEffectTag", "RocketInf_RPG29_105mm")]),
            },
        },
    },
}
# fmt: on
