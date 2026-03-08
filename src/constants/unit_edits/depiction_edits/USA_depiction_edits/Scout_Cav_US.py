"""Scout_Cav_US depiction edits."""

from typing import Dict, Tuple, Union

# fmt: off
scout_cav_us: Dict[str, Dict[Union[str, Tuple[str, str]], dict]] = {
    "unit_name": "Scout_Cav_US",
    "valid_files": ["DepictionInfantry.ndf", "WeaponDescriptor.ndf"],
    "DepictionInfantry_ndf": {
        ("AllWeaponAlternatives_Scout_Cav_US", None): { # (namespace, object type)
            # row: (edit type, [(property, value), (property, value), ...]) (edit types: "edit", "add", "remove", "replace")
            1: ("insert", [("SelectorId", "WeaponAlternative_2"), ("MeshDescriptor", "M60")]),
            2: ("edit", [("SelectorId", "WeaponAlternative_3")]),
        },

        ("AllWeaponSubDepiction_Scout_Cav_US", "TemplateAllSubWeaponDepiction"): {
            "Operators": {
                1: ("insert", [("FireEffectTag", "MMG_M60_7_62mm"), ("WeaponShootDataPropertyName", "WeaponShootData_0_2")]),
                2: ("edit", [("WeaponShootDataPropertyName", "WeaponShootData_0_3")]),
            },
        },

        ("TacticDepiction_Scout_Cav_US_Soldier", "TemplateInfantryDepictionFactoryTactic"): {
            "Operators": { # usually (always?) editing conditional tags submember
                0: ("edit", [("bazooka", "WeaponAlternative_3")]),
            }
        },
    }
}
# fmt: on