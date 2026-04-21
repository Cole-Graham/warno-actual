"""Scout_USMC_US depiction edits."""

from typing import Dict, Tuple, Union

# fmt: off
scout_usmc_us: Dict[str, Dict[Union[str, Tuple[str, str]], dict]] = {
    "unit_name": "Scout_USMC_US",
    "valid_files": ["DepictionInfantry.ndf", "WeaponDescriptor.ndf"],
    "DepictionInfantry_ndf": {
        ("AllWeaponAlternatives_Scout_USMC_US", None): { # (namespace, object type)
            # row: (edit type, [(property, value), (property, value), ...]) (edit types: "edit", "insert", "remove", "replace")
            1: ("insert", [("SelectorId", "WeaponAlternative_2"), ("MeshDescriptor", "M249")]),
            2: ("edit", [("SelectorId", "WeaponAlternative_3")]),
        },

        ("AllWeaponSubDepiction_Scout_USMC_US", "TemplateAllSubWeaponDepiction"): {
            "Operators": {
                1: ("insert", [("FireEffectTag", "SAW_M249_5_56mm"), ("WeaponShootDataPropertyName", "WeaponShootData_0_2")]),
                2: ("edit", [("WeaponShootDataPropertyName", "WeaponShootData_0_3")]),
            },
        },

        ("TacticDepiction_Scout_USMC_US_Soldier", "TemplateInfantryDepictionFactoryTactic"): {
            "Operators": { # usually (always?) editing conditional tags submember
                0: ("edit", [("bazooka", "WeaponAlternative_3")]),
            }
        },
    }
}
# fmt: on
