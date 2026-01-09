"""Chasseurs_CMD2_FR depiction edits."""

from typing import Dict, Tuple, Union

# fmt: off
chasseurs_cmd2_fr: Dict[str, Dict[Union[str, Tuple[str, str]], dict]] = {
    "unit_name": "Chasseurs_CMD2_FR",
    "valid_files": ["DepictionInfantry.ndf"],
    "DepictionInfantry_ndf": {
        ("AllWeaponAlternatives_Chasseurs_CMD2_FR", None): ( # (namespace, object type)
            f'[\n'
            f'    TDepictionVisual\n'
            f'    (\n'
            f'        SelectorId = ["WeaponAlternative_1"]\n'
            f'        MeshDescriptor = $/GFX/DepictionResources/Modele_Famas_F1\n'
            f'    ),\n'
            f'    TDepictionVisual\n'
            f'    (\n'
            f'        SelectorId = ["WeaponAlternative_2"]\n'
            f'        MeshDescriptor = $/GFX/DepictionResources/Modele_LRAC_F1\n'
            f'    ),\n'
            f'    TDepictionVisual\n'
            f'    (\n'
            f'        SelectorId = ["WeaponAlternative_3"]\n'
            f'        MeshDescriptor = $/GFX/DepictionResources/Modele_MainNue\n'
            f'    ),\n'
            f'    TMeshlessDepictionDescriptor\n'
            f'    (\n'
            f'        SelectorId = ["none"]\n'
            f'        ReferenceMeshForSkeleton = $/GFX/DepictionResources/Modele_MainNue\n'
            f'    )\n'
            f']'
        ),
        
        ("AllWeaponSubDepiction_Chasseurs_CMD2_FR", "TemplateAllSubWeaponDepiction"): {
            "Operators": (
                f'[\n'
                f'    DepictionOperator_WeaponInstantFireInfantry\n'
                f'    (\n'
                f'        FireEffectTag = "FireEffect_FM_FAMAS"\n'
                f'        WeaponShootDataPropertyName = "WeaponShootData_0_1"\n'
                f'    ),\n'
                f'    DepictionOperator_WeaponInstantFireInfantry\n'
                f'    (\n'
                f'        FireEffectTag = "FireEffect_Grenade_SMOKE"\n'
                f'        WeaponShootDataPropertyName = "WeaponShootData_0_2"\n'
                f'    ),\n'
                f'    DepictionOperator_WeaponInstantFireInfantry\n'
                f'    (\n'
                f'        FireEffectTag = "FireEffect_RocketInf_LRAC_F1"\n'
                f'        WeaponShootDataPropertyName = "WeaponShootData_0_3"\n'
                f'    )\n'
                f']'
            )
        },
        
        ("TacticDepiction_Chasseurs_CMD2_FR_Soldier", "TemplateInfantryDepictionFactoryTactic"): {
            "Operators": {
                # 0: ("remove", None),
                0: ("edit", [("bazooka", "WeaponAlternative_2")]),
            }
        },
    },
}
# fmt: on
