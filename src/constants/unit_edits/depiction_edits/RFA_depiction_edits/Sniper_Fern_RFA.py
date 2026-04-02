"""Sniper_Fern_RFA depiction edits."""

from typing import Dict, Tuple, Union

# fmt: off
sniper_fern_rfa: Dict[str, Dict[Union[str, Tuple[str, str]], dict]] = {
    "unit_name": "Sniper_Fern_RFA",
    "valid_files": ["DepictionInfantry.ndf", "WeaponDescriptor.ndf"],
    "DepictionInfantry_ndf": {
        ("AllWeaponAlternatives_Sniper_Fern_RFA", None): { # (namespace, object type)
            # row: (edit type, [(property, value), (property, value), ...]) (edit types: "edit", "insert", "remove")
            # always insert and/or remove first, then define the rest based on adjusted indices
            2: ("insert", [("SelectorId", "WeaponAlternative_3"), ("MeshDescriptor", "M72A4")]),
            3: ("edit", [("ReferenceMeshForSkeleton", "M72A4")]),
        },

        ("AllWeaponSubDepiction_Sniper_Fern_RFA", "TemplateAllSubWeaponDepiction"): {
            "Operators": {
                2: ("insert", [("FireEffectTag", "RocketInf_M72A4_LAW_66mm"), ("WeaponShootDataPropertyName", "WeaponShootData_0_3")]),
            },
        },
        
        ("TacticDepiction_Sniper_Fern_RFA_Soldier", "TemplateInfantryDepictionFactoryTactic"): {
            "Operators": {
                0: ("edit", [("bazooka", "WeaponAlternative_3")]),
            },
        },
    }
}
# fmt: on
