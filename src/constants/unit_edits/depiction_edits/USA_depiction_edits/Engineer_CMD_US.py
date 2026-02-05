"""Engineer_CMD_US depiction edits."""

from typing import Dict, Tuple, Union

# fmt: off
engineer_cmd_us: Dict[str, Dict[Union[str, Tuple[str, str]], dict]] = {
    "unit_name": "Engineer_CMD_US",
    "valid_files": ["DepictionInfantry.ndf", "WeaponDescriptor.ndf"],
    "DepictionInfantry_ndf": {
        ("AllWeaponAlternatives_Engineer_CMD_US", None): { # (namespace, object type)
            # row: (edit type, [(property, value), (property, value), ...]) (edit types: "edit", "insert", "remove")
            # always insert and/or remove first, then define the rest based on adjusted indices
            2: ("insert", [("SelectorId", "WeaponAlternative_3"), ("MeshDescriptor", "M72A4")]),
            3: ("edit", [("ReferenceMeshForSkeleton", "M72A4")]),
        },

        ("AllWeaponSubDepiction_Engineer_CMD_US", "TemplateAllSubWeaponDepiction"): {
            "Operators": {
                2: ("insert", [("FireEffectTag", "RocketInf_M72A4_LAW_66mm"), ("WeaponShootDataPropertyName", "WeaponShootData_0_3")]),
            },
        },
        
        ("TacticDepiction_Engineer_CMD_US_Soldier", "TemplateInfantryDepictionFactoryTactic"): {
            "Operators": {
                1: ("insert", [("bazooka", "WeaponAlternative_3")]),
            },
        },
    }
}
# fmt: on
