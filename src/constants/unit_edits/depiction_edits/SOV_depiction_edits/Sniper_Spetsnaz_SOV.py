"""Sniper_Spetsnaz_SOV depiction edits."""

from typing import Dict, Tuple, Union

# fmt: off
sniper_spetsnaz_sov: Dict[str, Dict[Union[str, Tuple[str, str]], dict]] = {
    "unit_name": "Sniper_Spetsnaz_SOV",
    "valid_files": ["DepictionInfantry.ndf", "WeaponDescriptor.ndf"],
    "DepictionInfantry_ndf": {
        ("AllWeaponAlternatives_Sniper_Spetsnaz_SOV", None): { # (namespace, object type)
            # row: (edit type, [(property, value), (property, value), ...]) (edit types: "edit", "add", "remove", "replace")
            2: ("insert", [("SelectorId", "WeaponAlternative_3"), ("MeshDescriptor", "RPG26")]),
            3: ("edit", [("ReferenceMeshForSkeleton", "RPG26")]),
        },

        ("AllWeaponSubDepiction_Sniper_Spetsnaz_SOV", "TemplateAllSubWeaponDepiction"): {
            "Operators": {
                2: ("insert", [("FireEffectTag", "RocketInf_RPG26_72_5mm"), ("WeaponShootDataPropertyName", "WeaponShootData_0_3")]),
            },
        },

        ("TacticDepiction_Sniper_Spetsnaz_SOV_Alternatives", None):
            """[
    TDepictionVisual
    (
        SelectorId = [LOD_High, '01']
        MeshDescriptor = $/GFX/DepictionResources/Modele_Sniper_Spetsnaz_SOV
    ),
    TDepictionVisual
    (
        SelectorId = [LOD_High, '02']
        MeshDescriptor = $/GFX/DepictionResources/Modele_Sniper_Spetsnaz_SOV_02
    ),
    TDepictionVisual
    (
        SelectorId = [LOD_High, '03']
        MeshDescriptor = $/GFX/DepictionResources/Modele_Sniper_Spetsnaz_SOV_02
    ),
    TDepictionVisual
    (
        SelectorId = [LOD_Low]
        MeshDescriptor = $/GFX/DepictionResources/Modele_Sniper_Spetsnaz_SOV_LOW
    ),
    TMeshlessDepictionDescriptor
    (
        SelectorId = ['none']
        ReferenceMeshForSkeleton = $/GFX/DepictionResources/Modele_Sniper_Spetsnaz_SOV
    )
]""",  
        
        ("TacticDepiction_Sniper_Spetsnaz_SOV_Soldier", "TemplateInfantryDepictionFactoryTactic"): {
            "Selector": "02_03",
            "Operators": { # usually (always?) editing conditional tags submember
                0: ("insert", [("bazooka", "WeaponAlternative_3")]),
            },
        },
                
        ("TacticDepiction_Sniper_Spetsnaz_SOV_Ghost", "TemplateInfantryDepictionFactoryGhost"): {
            "Selector": "02_03"
        },
                
        (None, "TTransportedInfantryEntry"): {
            "Count": 3,
            "Meshes": [
                "Sniper_Spetsnaz_SOV",
                "Sniper_Spetsnaz_SOV_02",
                "Sniper_Spetsnaz_SOV_02",
            ],
            "UniqueCount": 2,
        },
    }
}
# fmt: on
