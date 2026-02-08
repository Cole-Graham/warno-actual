"""Engineers_CMD_UK depiction edits."""

from typing import Dict, Tuple, Union

# fmt: off
engineers_cmd_uk: Dict[str, Dict[Union[str, Tuple[str, str]], dict]] = {
    "unit_name": "Engineers_CMD_UK",
    "valid_files": ["DepictionInfantry.ndf", "WeaponDescriptor.ndf"],
    "DepictionInfantry_ndf": {
        ("AllWeaponAlternatives_Engineers_CMD_UK", None): { # (namespace, object type)
            # row: (edit type, [(property, value), (property, value), ...]) (edit types: "edit", "insert", "remove")
            # always insert and/or remove first, then define the rest based on adjusted indices
            1: ("insert", [("SelectorId", "WeaponAlternative_2"), ("MeshDescriptor", "M72A4")]),
            2: ("edit", [("ReferenceMeshForSkeleton", "M72A4")]),
        },

        ("AllWeaponSubDepiction_Engineers_CMD_UK", "TemplateAllSubWeaponDepiction"): {
            "Operators": {
                1: ("insert", [("FireEffectTag", "RocketInf_M72A4_LAW_66mm"), ("WeaponShootDataPropertyName", "WeaponShootData_0_2")]),
            },
        },
        
        ("TacticDepiction_Engineers_CMD_UK_Soldier", "TemplateInfantryDepictionFactoryTactic"): {
            "Operators": {
                1: ("insert", [("bazooka", "WeaponAlternative_2")]),
            },
        },
    }
}
# fmt: on
