"""Su_24M_clu_SOV depiction edits."""

from typing import Dict, Tuple, Union

# fmt: off
su_24m_clu_sov: Dict[str, Dict[Union[str, Tuple[str, str]], dict]] = {
    "unit_name": "Su_24M_clu_SOV",
    "valid_files": ["DepictionAerialUnits.ndf", "MissileCarriage.ndf", "MissileCarriageDepiction.ndf"],
    
    "DepictionAerialUnits_ndf": {
        
        # "new_objects": {
        #     "weapon3": """
        #         Op_Su_24M_clu_SOV_Weapon3 is DepictionOperator_WeaponMissileCarriageFire
        #         (
        #             Connoisseur = MissileCarriage_Su_24M_clu_SOV
        #             FireEffectTag = "weapon_effet_tag3"
        #             NbProj = 1
        #             WeaponIndex = 3
        #             WeaponShootDataPropertyName = 
        #             [
        #                 "WeaponShootData_0_3",
        #             ]
        #         )
        #     """,
        # },
        
        (None, "TacticAerialDepictionRegistration"): {
            "Actions": (
                'MAP[\n'
                '    ( "weapon_effet_tag1", Weapon_GatlingAir_Gsh_23_6_23mm ),\n'
                '    ( "weapon_effet_tag2", Weapon_Bomb_CLU_RBK_250kg_x8 ),\n'
                # '    ( "weapon_effet_tag3", Weapon_Bomb_CLU_RBK_250kg_x8 ),\n'
                ']\n'
                '+ DepictionAction_Stress_And_Wrecked_Avion\n'
                '+ DepictionAction_CriticalFX_Airplane\n'
                '+ DepictionAction_MovementFX_DoubleReactorAirplane\n'
                '+ DepictionAction_Flare_Double\n'
            ),
            # "Operators": {
            #     5: ("insert", "Op_Su_24M_clu_SOV_Weapon3,"),
            # },
        },
    },
    
    "MissileCarriage_ndf": {
        ("MissileCarriage_Su_24M_clu_SOV", "TMissileCarriageConnoisseur"): { # (Namespace, Object type)
            "WeaponInfos": {
                0: ("edit", {
                    "MissileCount": 16,
                }),
                # 1: ("insert", (
                #     f'TMissileCarriageWeaponInfo'
                #     f'('
                #     f'    MissileCount = 8'
                #     f'    MissileType = eAGM'
                #     f'    MountingType = eMountingBomb'
                #     f'    WeaponIndex = 3'
                #     f')'
                # )),
            },
        },
    },
    
    "MissileCarriageDepiction_ndf": {
        ("SubGenerators_Su_24M_clu_SOV", "TStaticMissileCarriageSubDepictionGenerator"): {
            "Missiles": {
                0: ("replace", (
                    f'TStaticMissileCarriageSubDepictionMissileInfo'
                    f'('
                    f'    Depiction = TemplateDepictionStaticMissiles'
                    f'    ('
                    f'        PhysicalProperty = "Tourelle2_MissileCount"'
                    f'        ProjectileModelResource = $/GFX/DepictionResources/Modele_Missile_FAB_250'
                    f'    )'
                    f'    MissileCount = 16'
                    f'    WeaponIndex = 2'
                    f')'
                )),
                
                # 1: ("insert", (
                #     f'TStaticMissileCarriageSubDepictionMissileInfo'
                #     f'('
                #     f'    Depiction = TemplateDepictionStaticMissiles'
                #     f'    ('
                #     f'        PhysicalProperty = "Tourelle3_MissileCount"'
                #     f'        ProjectileModelResource = $/GFX/DepictionResources/Modele_Missile_FAB_250'
                #     f'    )'
                #     f'    MissileCount = 8'
                #     f'    WeaponIndex = 3'
                #     f')'
                # )),
            },
        },
        ("SubGenerators_Showroom_Su_24M_clu_SOV", "TShowroomMissileCarriageSubDepictionGenerator"): {
            "Missiles": {
                0: ("replace", (
                    f'TShowroomMissileCarriageSubDepictionMissileInfo'
                    f'('
                    f'    Depiction = TemplateDepictionMissileShowroom'
                    f'    ('
                    f'        ProjectileModelResource = $/GFX/DepictionResources/Modele_Missile_FAB_250'
                    f'    )'
                    f'    MissileCount = 16'
                    f'    WeaponIndex = 2'
                    f')'
                )),
                
                # 1: ("insert", (
                #     f'TShowroomMissileCarriageSubDepictionMissileInfo'
                #     f'('
                #     f'    Depiction = TemplateDepictionMissileShowroom'
                #     f'    ('
                #     f'        ProjectileModelResource = $/GFX/DepictionResources/Modele_Missile_FAB_250'
                #     f'    )'
                #     f'    MissileCount = 8'
                #     f'    WeaponIndex = 3'
                #     f')'
                # )),
            },
        },
    },
}
# fmt: on
