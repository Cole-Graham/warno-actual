"""Groupe_AT_US depiction edits."""

from typing import Dict, Tuple, Union

# fmt: off
groupe_at_us: Dict[str, Dict[Union[str, Tuple[str, str]], dict]] = {
    "unit_name": "Groupe_AT_US",
    "valid_files": ["DepictionInfantry.ndf", "WeaponDescriptor.ndf"],
    "DepictionInfantry_ndf": {
        ("AllWeaponAlternatives_Groupe_AT_US", None): { # (namespace, object type)
            # row: (edit type, [(property, value), (property, value), ...]) (edit types: "edit", "add", "remove", "replace")
            1: ("insert", [("SelectorId", "WeaponAlternative_2"), ("MeshDescriptor", "M249")]),
            2: ("edit", [("SelectorId", "WeaponAlternative_3")]),
            3: ("edit", [("SelectorId", "WeaponAlternative_4")]),
        },

        ("AllWeaponSubDepiction_Groupe_AT_US", "TemplateAllSubWeaponDepiction"): {
            "Operators": {
                1: ("insert", [("FireEffectTag", "SAW_M249_5_56mm"), ("WeaponShootDataPropertyName", "WeaponShootData_0_2")]),
                2: ("edit", [("WeaponShootDataPropertyName", "WeaponShootData_0_3")]),
                3: ("edit", [("WeaponShootDataPropertyName", "WeaponShootData_0_4")]),
            },
        },

        ("TacticDepiction_Groupe_AT_US_Soldier", "TemplateInfantryDepictionFactoryTactic"): {
            "Operators": { # usually (always?) editing conditional tags submember
                0: ("edit", [("bazooka", "WeaponAlternative_3")]),
                1: ("edit", [("bazooka", "WeaponAlternative_4")]),
            }
        },
    }
}
# fmt: on
