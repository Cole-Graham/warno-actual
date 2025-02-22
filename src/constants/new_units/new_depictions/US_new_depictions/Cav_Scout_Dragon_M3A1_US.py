"""Cav_Scout_Dragon_US depiction edits."""

from typing import Dict, Tuple, Union

# fmt: off
cav_scout_dragon_m3a1_us: Dict[str, Dict[Union[str, Tuple[str, str]], dict]] = {
    "unit_name": "Cav_Scout_Dragon_M3A1_US",
    "valid_files": ["GeneratedDepictionInfantry.ndf"],
    "GeneratedDepictionInfantry_ndf": {
        ("AllWeaponAlternatives_Cav_Scout_Dragon_M3A1_US", None): { # (namespace, object type)
            # row: (edit type, [(property, value), (property, value), ...]) (edit types: "edit", "add", "remove")
            1: ("edit", [("MeshDescriptor", "M47_DRAGON_II")]), # (selector_id or mesh)
            2: ("edit", [("MeshDescriptor", "M14_Sniper")]),
            3: ("edit", [("ReferenceMeshForSkeleton", "M47_DRAGON_II")]),
        },
        
        ("AllWeaponSubDepiction_Cav_Scout_Dragon_M3A1_US", "TemplateAllSubWeaponDepiction"): {
            # row: (edit type, [(property, value), (property, value), ...]) (edit types: "edit", "add", "remove")
            "Operators": {
                1: ("edit", [("FireEffectTag", "M47_DRAGON_II")]), # (selector_id or mesh)
                2: ("edit", [("FireEffectTag", "Sniper_M14")]),
            }
        },
        
        ("TacticDepiction_Cav_Scout_Dragon_M3A1_US_Alternatives", None): {
            # row: (edit type, [(property, value), (property, value), ...]) (edit types: "edit", "add", "remove")
            0: ("edit", [("MeshDescriptor", "LRRP_US_05")]), # (selector_id or mesh)
            1: ("edit", [("MeshDescriptor", "LRRP_US_04")]),
            2: ("remove", None),
            3: ("remove", None),
            4: ("remove", None),
            5: ("remove", None),
            6: ("remove", None),
            7: ("remove", None),
            8: ("remove", None),
            9: ("remove", None),
            10: ("edit", [("MeshDescriptor", "LRRP_US_LOW")]),
            11: ("edit", [("ReferenceMeshForSkeleton", "LRRP_US")]),
        },
        
        ("TacticDepiction_Cav_Scout_Dragon_M3A1_US_Soldier", "TemplateInfantryDepictionFactoryTactic"): {
            "Operators": {
                0: ("remove", None),
                1: ("edit", [("bazooka", "MeshAlternative_2")]),
            }
        },
        
        (None, "TTransportedInfantryEntry"): {
            "Meshes": ["LRRP_US_05", "LRRP_US_04"],
        }
    },
}
# fmt: on
