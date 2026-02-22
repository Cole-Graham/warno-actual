"""Reserve_CMD_POL depiction edits."""

from typing import Dict, Tuple, Union

# fmt: off
reserve_cmd_pol: Dict[str, Dict[Union[str, Tuple[str, str]], dict]] = {
    "unit_name": "Reserve_CMD_POL",
    "valid_files": ["DepictionInfantry.ndf", "WeaponDescriptor.ndf"],
    "DepictionInfantry_ndf": {
        ("AllWeaponAlternatives_Reserve_CMD_POL", None): { # (namespace, object type)
            # row: (edit type, [(property, value), (property, value), ...]) (edit types: "edit", "insert", "remove")
            # always insert and/or remove first, then define the rest based on adjusted indices
            2: ("insert", [("SelectorId", "WeaponAlternative_3"), ("MeshDescriptor", "RPG7V")]),
            3: ("edit", [("ReferenceMeshForSkeleton", "RPG7V")]),
        },

        ("AllWeaponSubDepiction_Reserve_CMD_POL", "TemplateAllSubWeaponDepiction"): {
            "Operators": {
                2: ("insert", [("FireEffectTag", "FireEffect_RocketInf_RPG7"), ("WeaponShootDataPropertyName", "WeaponShootData_0_3")]),
            },
        },
        
        ("TacticDepiction_Reserve_CMD_POL_Soldier", "TemplateInfantryDepictionFactoryTactic"): {
            "Operators": {
                0: ("insert", [("bazooka", "WeaponAlternative_3")]),
            },
        },
    }
}
# fmt: on