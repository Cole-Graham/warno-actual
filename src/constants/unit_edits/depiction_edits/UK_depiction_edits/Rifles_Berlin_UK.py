"""Rifles_Berlin_UK depiction edits."""

from typing import Dict, Tuple, Union

# fmt: off
rifles_berlin_uk: Dict[str, Dict[Union[str, Tuple[str, str]], dict]] = {
    "unit_name": "Rifles_Berlin_UK",
    "valid_files": ["DepictionInfantry.ndf", "WeaponDescriptor.ndf"],
    "DepictionInfantry_ndf": {
        ("AllWeaponAlternatives_Rifles_Berlin_UK", None): { # (namespace, object type)
            # row: (edit type, [(property, value), (property, value), ...]) (edit types: "edit", "insert", "remove")
            # always insert and/or remove first, then define the rest based on adjusted indices
            2: ("insert", [("SelectorId", "WeaponAlternative_3"), ("MeshDescriptor", "L7A2")]),
            3: ("edit", [("SelectorId", "WeaponAlternative_4")]),
        },

        ("AllWeaponSubDepiction_Rifles_Berlin_UK", "TemplateAllSubWeaponDepiction"): {
            "Operators": {
                2: ("insert", [("FireEffectTag", "MMG_inf_L7A2_7_62mm"), ("WeaponShootDataPropertyName", "WeaponShootData_0_3")]),
                3: ("edit", [("WeaponShootDataPropertyName", "WeaponShootData_0_4")]),
            },
        },
        
        ("TacticDepiction_Rifles_Berlin_UK_Soldier", "TemplateInfantryDepictionFactoryTactic"): {
            "Operators": {
                0: ("insert", [("mmg", "WeaponAlternative_3")]),
                1: ("edit", [("bazooka", "WeaponAlternative_4")]),
            },
        },
    }
}
# fmt: on
