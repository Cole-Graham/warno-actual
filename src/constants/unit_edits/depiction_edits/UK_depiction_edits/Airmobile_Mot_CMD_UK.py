"""Airmobile_Mot_CMD_UK depiction edits."""

from typing import Dict, Tuple, Union

# fmt: off
airmobile_mot_cmd_uk: Dict[str, Dict[Union[str, Tuple[str, str]], dict]] = {
    "unit_name": "Airmobile_Mot_CMD_UK",
    "valid_files": ["DepictionInfantry.ndf", "WeaponDescriptor.ndf"],
    "DepictionInfantry_ndf": {
        ("AllWeaponAlternatives_Airmobile_Mot_CMD_UK", None): { # (namespace, object type)
            # row: (edit type, [(property, value), (property, value), ...]) (edit types: "edit", "insert", "remove")
            # always insert and/or remove first, then define the rest based on adjusted indices
            1: ("insert", [("SelectorId", "WeaponAlternative_2"), ("MeshDescriptor", "M72A4")]),
            2: ("edit", [("SelectorId", "WeaponAlternative_3")]),
        },

        ("AllWeaponSubDepiction_Airmobile_Mot_CMD_UK", "TemplateAllSubWeaponDepiction"): {
            "Operators": {
                1: ("insert", [("FireEffectTag", "RocketInf_M72_LAW_66mm"), ("WeaponShootDataPropertyName", "WeaponShootData_0_2")]),
                2: ("edit", [("WeaponShootDataPropertyName", "WeaponShootData_0_3")]),
            },
        },
        
        ("TacticDepiction_Airmobile_Mot_CMD_UK_Soldier", "TemplateInfantryDepictionFactoryTactic"): {
            "Operators": {
                0: ("insert", [("bazooka", "WeaponAlternative_2")]),
                1: ("edit", [("grenade", "WeaponAlternative_3")]),
            },
        },
    }
}
# fmt: on
