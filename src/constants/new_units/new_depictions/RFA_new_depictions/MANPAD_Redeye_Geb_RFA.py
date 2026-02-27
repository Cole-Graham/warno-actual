"""MANPAD_MANPAD_Redeye_Geb_RFA depiction edits."""

from typing import Dict, Tuple, Union

# fmt: off
manpad_redeye_geb_rfa: Dict[str, Dict[Union[str, Tuple[str, str]], dict]] = {
    "unit_name": "MANPAD_Redeye_Geb_RFA",
    "valid_files": ["DepictionInfantry.ndf"],
    "DepictionInfantry_ndf": {
        ("AllWeaponAlternatives_MANPAD_Redeye_Geb_RFA", None): ( # (namespace, object type)
            # row: (edit type, [(property, value), (property, value), ...]) (edit types: "edit", "add", "remove")
            # 1: ("add", [("SelectorId", "WeaponAlternative_2"), ("MeshDescriptor", "M14_Sniper")]), # (selector_id or mesh)
            # 2: ("edit", [("SelectorId", "WeaponAlternative_3")]),
            f'[\n'
            f'    TDepictionVisual\n'
            f'    (\n'
            f'        SelectorId = ["WeaponAlternative_1"]\n'
            f'        MeshDescriptor = $/GFX/DepictionResources/Modele_Uzi\n'
            f'    ),\n'
            f'    TDepictionVisual\n'
            f'    (\n'
            f'        SelectorId = ["WeaponAlternative_2"]\n'
            f'        MeshDescriptor = $/GFX/DepictionResources/Modele_MANPAD_FIM43\n'
            f'    ),\n'
            f'    TMeshlessDepictionDescriptor\n'
            f'    (\n'
            f'        SelectorId = ["none"]\n'
            f'        ReferenceMeshForSkeleton = $/GFX/DepictionResources/Modele_MANPAD_FIM43\n'
            f'    ),\n'
            f']'
        ),
        
        ("AllWeaponSubDepiction_MANPAD_Redeye_Geb_RFA", "TemplateAllSubWeaponDepiction"): {
            # row: (edit type, [(property, value), (property, value), ...]) (edit types: "edit", "add", "remove")
            "Operators": (
                # 1: ("add", [("FireEffectTag", "Sniper_M14"), ("WeaponShootDataPropertyName", "0_2")]), # (selector_id or mesh)
                f'[\n'
                f'    DepictionOperator_WeaponInstantFireInfantry\n'
                f'    (\n'
                f'        FireEffectTag = "FireEffect_PM_uzi"\n'
                f'        WeaponShootDataPropertyName = "WeaponShootData_0_1"\n'
                f'    ),\n'
                f'    DepictionOperator_WeaponInstantFireInfantry\n'
                f'    (\n'
                f'        FireEffectTag = "FireEffect_MANPAD_FIM43"\n'
                f'        WeaponShootDataPropertyName = "WeaponShootData_0_2"\n'
                f'    ),\n'
                f']'
            )
        },
        
        # ("TacticDepiction_MANPAD_Stinger_C_Rifles_US_Soldier", "TemplateInfantryDepictionFactoryTactic"): {
        #     "Operators": {
        #         1: ("add", [("mmg", "WeaponAlternative_3")]),
        #     }
        # },
    },
}
# fmt: on
