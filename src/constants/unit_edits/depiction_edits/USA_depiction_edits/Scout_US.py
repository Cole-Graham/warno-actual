"""Scout_US depiction edits."""

from typing import Dict, Tuple, Union

# fmt: off
scout_us: Dict[str, Dict[Union[str, Tuple[str, str]], dict]] = {
    "unit_name": "Scout_US",
    "valid_files": ["DepictionInfantry.ndf", "WeaponDescriptor.ndf"],
    "DepictionInfantry_ndf": {
        ("AllWeaponAlternatives_Scout_US", None): { # (namespace, object type)
            # row: (edit type, [(property, value), (property, value), ...]) (edit types: "edit", "insert", "remove")
            # always insert and/or remove first, then define the rest based on adjusted indices
            2: ("insert", [("SelectorId", "WeaponAlternative_3"), ("MeshDescriptor", "M72A4")]),
            1: ("edit", [("MeshDescriptor", "M249")]), # (selector_id or mesh)
            3: ("edit", [("ReferenceMeshForSkeleton", "M72A4")]),
        },

        ("AllWeaponSubDepiction_Scout_US", "TemplateAllSubWeaponDepiction"): {
            "Operators": {
                2: ("insert", [("FireEffectTag", "RocketInf_M72_LAW_66mm"), ("WeaponShootDataPropertyName", "WeaponShootData_0_3")]),
                1: ("edit", [("FireEffectTag", "SAW_M249_5_56mm")]),
            },
        },
        
        ("TacticDepiction_Scout_US_Soldier", "TemplateInfantryDepictionFactoryTactic"): {
            "Operators": {
                0: ("edit", [("bazooka", "WeaponAlternative_3")]),
            },
        },
    }
}
# fmt: on
