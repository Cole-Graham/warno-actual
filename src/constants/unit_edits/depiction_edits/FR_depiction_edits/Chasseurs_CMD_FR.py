"""Chasseurs_CMD_FR depiction edits."""

from typing import Dict, Tuple, Union

# fmt: off
chasseurs_cmd_fr: Dict[str, Dict[Union[str, Tuple[str, str]], dict]] = {
    "unit_name": "Chasseurs_CMD_FR",
    "valid_files": ["DepictionInfantry.ndf", "WeaponDescriptor.ndf"],
    "DepictionInfantry_ndf": {
        ("AllWeaponAlternatives_Chasseurs_CMD_FR", None): { # (namespace, object type)
            # row: (edit type, [(property, value), (property, value), ...]) (edit types: "edit", "add", "remove", "replace")
            1: ("insert", [("SelectorId", "WeaponAlternative_2"), ("MeshDescriptor", "LRAC_F1")]),
            2: ("edit", [("SelectorId", "WeaponAlternative_3")]),
        },

        ("AllWeaponSubDepiction_Chasseurs_CMD_FR", "TemplateAllSubWeaponDepiction"): {
            "Operators": {
                1: ("insert", [("FireEffectTag", "RocketInf_LRAC_F1"), ("WeaponShootDataPropertyName", "WeaponShootData_0_2")]),
                2: ("edit", [("WeaponShootDataPropertyName", "WeaponShootData_0_3")])
            },
        },

        ("TacticDepiction_Chasseurs_CMD_FR_Soldier", "TemplateInfantryDepictionFactoryTactic"): {
            "Operators": { # usually (always?) editing conditional tags submember
                0: ("insert", [("bazooka", "WeaponAlternative_2")]),
                1: ("edit", [("grenade", "WeaponAlternative_3")]),
            }
        },
    }
}
# fmt: on
