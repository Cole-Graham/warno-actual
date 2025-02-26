"""MANPAD_Stinger_C_Rifles_US depiction edits."""

from typing import Dict, Tuple, Union

# fmt: off
manpad_stinger_c_rifles_us: Dict[str, Dict[Union[str, Tuple[str, str]], dict]] = {
    "unit_name": "MANPAD_Stinger_C_Rifles_US",
    "valid_files": ["GeneratedDepictionInfantry.ndf"],
    "GeneratedDepictionInfantry_ndf": {
        ("AllWeaponAlternatives_MANPAD_Stinger_C_Rifles_US", None): { # (namespace, object type)
            # row: (edit type, [(property, value), (property, value), ...]) (edit types: "edit", "add", "remove")
            2: ("add", [("SelectorId", "MeshAlternative_3"), ("MeshDescriptor", "M14_Sniper")]), # (selector_id or mesh)
        },
        
        ("AllWeaponSubDepiction_MANPAD_Stinger_C_Rifles_US", "TemplateAllSubWeaponDepiction"): {
            # row: (edit type, [(property, value), (property, value), ...]) (edit types: "edit", "add", "remove")
            "Operators": {
                2: ("add", [("FireEffectTag", "Sniper_M14"), ("WeaponShootDataPropertyName", "0_3")]), # (selector_id or mesh)
            }
        },
        
        # ("TacticDepiction_MANPAD_Stinger_C_Rifles_US_Soldier", "TemplateInfantryDepictionFactoryTactic"): {
        #     "Operators": {
        #         1: ("add", [("mmg", "MeshAlternative_3")]),
        #     }
        # },
    },
}
# fmt: on
