"""Sapeurs_CMD_FR depiction edits."""

from typing import Dict, Tuple, Union

# fmt: off
sapeurs_cmd_fr: Dict[str, Dict[Union[str, Tuple[str, str]], dict]] = {
    "unit_name": "Sapeurs_CMD_FR",
    "valid_files": ["DepictionInfantry.ndf", "WeaponDescriptor.ndf"],
    "DepictionInfantry_ndf": {
        ("AllWeaponAlternatives_Sapeurs_CMD_FR", None): { # (namespace, object type)
            # row: (edit type, [(property, value), (property, value), ...]) (edit types: "edit", "add", "remove", "replace")
            2: ("insert", [("SelectorId", "WeaponAlternative_3"), ("MeshDescriptor", "LRAC_F1")]),
            3: ("edit", [("ReferenceMeshForSkeleton", "LRAC_F1")]),
        },

        ("AllWeaponSubDepiction_Sapeurs_CMD_FR", "TemplateAllSubWeaponDepiction"): {
            "Operators": {
                2: ("insert", [("FireEffectTag", "RocketInf_LRAC_F1"), ("WeaponShootDataPropertyName", "WeaponShootData_0_3")]),
            },
        },

        ("TacticDepiction_Sapeurs_CMD_FR_Soldier", "TemplateInfantryDepictionFactoryTactic"): {
            "Operators": { # usually (always?) editing conditional tags submember
                1: ("insert", [("bazooka", "WeaponAlternative_3")]),
            }
        },
    }
}
# fmt: on
