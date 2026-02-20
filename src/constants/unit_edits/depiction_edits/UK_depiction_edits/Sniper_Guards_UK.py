"""Sniper_Guards_UK depiction edits."""

from typing import Dict, Tuple, Union

# fmt: off
sniper_guards_uk: Dict[str, Dict[Union[str, Tuple[str, str]], dict]] = {
    "unit_name": "Sniper_Guards_UK",
    "valid_files": ["DepictionInfantry.ndf", "WeaponDescriptor.ndf"],
    "DepictionInfantry_ndf": {
        ("AllWeaponAlternatives_Sniper_Guards_UK", None): { # (namespace, object type)
            # row: (edit type, [(property, value), (property, value), ...]) (edit types: "edit", "insert", "remove")
            # always insert and/or remove first, then define the rest based on adjusted indices
            2: ("insert", [("SelectorId", "WeaponAlternative_3"), ("MeshDescriptor", "M72A4")]),
            3: ("edit", [("ReferenceMeshForSkeleton", "M72A4")]),
        },

        ("AllWeaponSubDepiction_Sniper_Guards_UK", "TemplateAllSubWeaponDepiction"): {
            "Operators": {
                2: ("insert", [("FireEffectTag", "RocketInf_M72A4_LAW_66mm"), ("WeaponShootDataPropertyName", "WeaponShootData_0_3")]),
            },
        },
        
        ("TacticDepiction_Sniper_Guards_UK_Soldier", "TemplateInfantryDepictionFactoryTactic"): {
            "Operators": {
                0: ("insert", [("bazooka", "WeaponAlternative_3")]),
            },
        },
    }
}
# fmt: on
