"""Engineers_paras_POL depiction edits."""

from typing import Dict, Tuple, Union

# fmt: off
engineers_paras_pol: Dict[str, Dict[Union[str, Tuple[str, str]], dict]] = {
    "unit_name": "Engineers_paras_POL",
    "valid_files": ["DepictionInfantry.ndf", "WeaponDescriptor.ndf"],
    "DepictionInfantry_ndf": {
        ("AllWeaponAlternatives_Engineers_paras_POL", None): { # (namespace, object type)
            # row: (edit type, [(property, value), (property, value), ...]) (edit types: "edit", "insert", "remove")
            # always insert and/or remove first, then define the rest based on adjusted indices
            3: ("insert", [("SelectorId", "WeaponAlternative_4"), ("MeshDescriptor", "RPG7V")]),
            4: ("edit", [("ReferenceMeshForSkeleton", "RPG7V")]),
        },

        ("AllWeaponSubDepiction_Engineers_paras_POL", "TemplateAllSubWeaponDepiction"): {
            "Operators": {
                3: ("insert", [("FireEffectTag", "FireEffect_RocketInf_RPG7"), ("WeaponShootDataPropertyName", "WeaponShootData_0_4")]),
            },
        },
        
        ("TacticDepiction_Engineers_paras_POL_Soldier", "TemplateInfantryDepictionFactoryTactic"): {
            "Operators": {
                2: ("insert", [("bazooka", "WeaponAlternative_4")]),
            },
        },
    }
}
# fmt: on