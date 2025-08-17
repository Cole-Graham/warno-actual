"""Cav_Scout_Dragon_US depiction edits."""

from typing import Dict, Tuple, Union

# fmt: off
cav_scout_dragon_m3a1_us: Dict[str, Dict[Union[str, Tuple[str, str]], dict]] = {
    "unit_name": "Cav_Scout_Dragon_M3A1_US",
    "valid_files": ["DepictionInfantry.ndf"],
    "DepictionInfantry_ndf": {
        ("AllWeaponAlternatives_Cav_Scout_Dragon_M3A1_US", None): ( # (namespace, object type)
            # row: (edit type, [(property, value), (property, value), ...]) (edit types: "edit", "add", "insert", "remove")
            # 1: ("edit", [("MeshDescriptor", "M14_Sniper")]), # (SelectorId or mesh)
            # 2: ("insert", [("SelectorId", "['MeshAlternative_3']"), ("MeshDescriptor", "M47_DRAGON_II")]),
            # 2: ("edit", [("ReferenceMeshForSkeleton", "M47_DRAGON_II")]),
            f'['
            f'    TDepictionVisual\n'
            f'    (\n'
            f'        SelectorId = ["MeshAlternative_1"]\n'
            f'        MeshDescriptor = $/GFX/DepictionResources/Modele_M16A2\n'
            f'    ),\n'
            f'    TDepictionVisual\n'
            f'    (\n'
            f'        SelectorId = ["MeshAlternative_2"]\n'
            f'        MeshDescriptor = $/GFX/DepictionResources/Modele_M14_Sniper\n'
            f'    ),\n'
            f'    TDepictionVisual\n'
            f'    (\n'
            f'        SelectorId = ["MeshAlternative_3"]\n'
            f'        MeshDescriptor = $/GFX/DepictionResources/Modele_M47_DRAGON_II\n'
            f'    ),\n'
            f'    TMeshlessDepictionDescriptor\n'
            f'    (\n'
            f'        SelectorId = ["none"]\n'
            f'        ReferenceMeshForSkeleton = $/GFX/DepictionResources/Modele_M47_DRAGON_II\n'
            f'    )\n'
            f']'
        ),
        
        ("AllWeaponSubDepiction_Cav_Scout_Dragon_M3A1_US", "TemplateAllSubWeaponDepiction"): {
            # row: (edit type, [(property, value), (property, value), ...]) (edit types: "edit", "add", "insert", "remove")
            "Operators": (
            #     1: ("edit", [("FireEffectTag", "Sniper_M14")]), # (FireEffectTag)
            #     2: ("add", [("FireEffectTag", "M47_DRAGON_II")]),
                f'[\n'
                f'    DepictionOperator_WeaponInstantFireInfantry\n'
                f'    (\n'
                f'        FireEffectTag = "FireEffect_FM_M16"\n'
                f'        WeaponShootDataPropertyName = "WeaponShootData_0_1"\n'
                f'    ),\n'
                f'    DepictionOperator_WeaponInstantFireInfantry\n'
                f'    (\n'
                f'        FireEffectTag = "FireEffect_Sniper_M14"\n'
                f'        WeaponShootDataPropertyName = "WeaponShootData_0_3"\n'
                f'    ),\n'
                f'    DepictionOperator_WeaponInstantFireInfantry\n'
                f'    (\n'
                f'        FireEffectTag = "FireEffect_M47_DRAGON_II"\n'
                f'        WeaponShootDataPropertyName = "WeaponShootData_0_2"\n'
                f'    ),\n'
                f']'
            )
        },
        
        ("TacticDepiction_Cav_Scout_Dragon_M3A1_US_Alternatives", None): (
            # row: (edit type, [(property, value), (property, value), ...]) (edit types: "edit", "add", "insert", "remove")
        #     0: ("edit", [("MeshDescriptor", "LRRP_US_05")]), # (SelectorId or mesh)
        #     1: ("edit", [("MeshDescriptor", "LRRP_US_04")]),
        #     2: ("remove", None),
        #     3: ("remove", None),
        #     4: ("remove", None),
        #     5: ("remove", None),
        #     6: ("remove", None),
        #     7: ("remove", None),
        #     8: ("remove", None),
        #     9: ("remove", None),
        #     10: ("edit", [("MeshDescriptor", "LRRP_US_LOW")]),
        #     11: ("edit", [("ReferenceMeshForSkeleton", "LRRP_US")]),
            f'[\n'
            f'    TDepictionVisual\n'
            f'    (\n'
            f'        SelectorId = [LOD_High, "01"]\n'
            f'        MeshDescriptor = $/GFX/DepictionResources/Modele_LRRP_US_05\n'
            f'    ),\n'
            f'    TDepictionVisual\n'
            f'    (\n'
            f'        SelectorId = [LOD_High, "02"]\n'
            f'        MeshDescriptor = $/GFX/DepictionResources/Modele_LRRP_US_04\n'
            f'    ),'
            f'    TDepictionVisual\n'
            f'    (\n'
            f'        SelectorId = [LOD_Low]\n'
            f'        MeshDescriptor = $/GFX/DepictionResources/Modele_LRRP_US_LOW\n'
            f'    ),\n'
            f'    TMeshlessDepictionDescriptor\n'
            f'    (\n'
            f'        SelectorId = ["none"]\n'
            f'        ReferenceMeshForSkeleton = $/GFX/DepictionResources/Modele_LRRP_US\n'
            f'    )\n'
            f']'
        ),
        
        ("TacticDepiction_Cav_Scout_Dragon_M3A1_US_Soldier", "TemplateInfantryDepictionFactoryTactic"): {
            "Operators": {
                # 0: ("remove", None),
                0: ("edit", [("bazooka", "MeshAlternative_3")]),
            }
        },
        
        (None, "TTransportedInfantryEntry"): {
            "Meshes": ["LRRP_US_05", "LRRP_US_04"],
        }
    },
}
# fmt: on
