"""MANPAD_Stinger_C_Rifles_US depiction edits."""

from typing import Dict, Tuple, Union

# fmt: off
manpad_stinger_c_rifles_us: Dict[str, Dict[Union[str, Tuple[str, str]], dict]] = {
    "unit_name": "MANPAD_Stinger_C_Rifles_US",
    "valid_files": ["DepictionInfantry.ndf"],
    "DepictionInfantry_ndf": {
        ("AllWeaponAlternatives_MANPAD_Stinger_C_Rifles_US", None): ( # (namespace, object type)
            # row: (edit type, [(property, value), (property, value), ...]) (edit types: "edit", "add", "remove")
            # 1: ("add", [("SelectorId", "MeshAlternative_2"), ("MeshDescriptor", "M14_Sniper")]), # (selector_id or mesh)
            # 2: ("edit", [("SelectorId", "MeshAlternative_3")]),
            f'[\n'
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
            f'        MeshDescriptor = $/GFX/DepictionResources/Modele_MANPAD_FIM92\n'
            f'    ),\n'
            f'    TMeshlessDepictionDescriptor\n'
            f'    (\n'
            f'        SelectorId = ["none"]\n'
            f'        ReferenceMeshForSkeleton = $/GFX/DepictionResources/Modele_MANPAD_FIM92\n'
            f'    ),\n'
            f']'
        ),
        
        ("AllWeaponSubDepiction_MANPAD_Stinger_C_Rifles_US", "TemplateAllSubWeaponDepiction"): {
            # row: (edit type, [(property, value), (property, value), ...]) (edit types: "edit", "add", "remove")
            "Operators": (
                # 1: ("add", [("FireEffectTag", "Sniper_M14"), ("WeaponShootDataPropertyName", "0_2")]), # (selector_id or mesh)
                f'[\n'
                f'    DepictionOperator_WeaponInstantFireInfantry\n'
                f'    (\n'
                f'        FireEffectTag = "FireEffect_FM_M16"\n'
                f'        WeaponShootDataPropertyName = "WeaponShootData_0_1"\n'
                f'    ),\n'
                f'    DepictionOperator_WeaponInstantFireInfantry\n'
                f'    (\n'
                f'        FireEffectTag = "FireEffect_Sniper_M14"\n'
                f'        WeaponShootDataPropertyName = "WeaponShootData_0_2"\n'
                f'    ),\n'
                f'    DepictionOperator_WeaponInstantFireInfantry\n'
                f'    (\n'
                f'        FireEffectTag = "FireEffect_MANPAD_FIM92"\n'
                f'        WeaponShootDataPropertyName = "WeaponShootData_0_3"\n'
                f'    ),\n'
                f']'
            )
        },
        
        # ("TacticDepiction_MANPAD_Stinger_C_Rifles_US_Soldier", "TemplateInfantryDepictionFactoryTactic"): {
        #     "Operators": {
        #         1: ("add", [("mmg", "MeshAlternative_3")]),
        #     }
        # },
    },
}
# fmt: on
