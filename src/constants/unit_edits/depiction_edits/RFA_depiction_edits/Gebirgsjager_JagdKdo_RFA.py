"""Gebirgsjager_JagdKdo_RFA depiction edits."""

from typing import Dict, Tuple, Union

# fmt: off
gebirgsjager_jagdkdo_rfa: Dict[str, Dict[Union[str, Tuple[str, str]], dict]] = {
    "unit_name": "Gebirgsjager_JagdKdo_RFA",
    "valid_files": ["DepictionInfantry.ndf", "WeaponDescriptor.ndf"],
    "DepictionInfantry_ndf": {
        ("AllWeaponAlternatives_Gebirgsjager_JagdKdo_RFA", None): { # (namespace, object type)
            # row: (edit type, [(property, value), (property, value), ...]) (edit types: "edit", "insert", "remove")
            # always insert and/or remove first, then define the rest based on adjusted indices
            1: ("remove", [("MeshDescriptor", "G3A3ZF")]),
            1: ("edit", [("SelectorId", "WeaponAlternative_2")]),
            2: ("edit", [("SelectorId", "WeaponAlternative_3")]),
        },

        ("AllWeaponSubDepiction_Gebirgsjager_JagdKdo_RFA", "TemplateAllSubWeaponDepiction"): {
            "Operators": {
                1: ("remove", [("FireEffectTag", "Sniper_G3A3ZF")]),
                1: ("edit", [("WeaponShootDataPropertyName", "WeaponShootData_0_2")]),
                2: ("edit", [("WeaponShootDataPropertyName", "WeaponShootData_0_3")]),
            },
        },

        ("TacticDepiction_Gebirgsjager_JagdKdo_RFA_Soldier", "TemplateInfantryDepictionFactoryTactic"): {
            "Operators": {
                0: ("edit", [("mmg", "WeaponAlternative_2")]),
                1: ("edit", [("grenade", "WeaponAlternative_3")]),
            },
        },
    }
}
# fmt: on
