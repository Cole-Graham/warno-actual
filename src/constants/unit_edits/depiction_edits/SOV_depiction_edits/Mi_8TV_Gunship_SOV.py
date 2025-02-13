"""Mi_8TV_Gunship_SOV depiction edits."""

from typing import Dict, Tuple, Union

# fmt: off
mi_8tv_gunship_sov: Dict[str, Dict[Union[str, Tuple[str, str]], dict]] = {
    "unit_name": "Mi_8TV_Gunship_SOV",
    "valid_files": ["DepictionAerialUnits.ndf", "MissileCarriage.ndf", "MissileCarriageDepiction.ndf"],
    "DepictionAerialUnits_ndf": {
        ("Gfx_Mi_8TV_Gunship_SOV", "TacticAerialDepictionTemplate"): {  # (Namespace (can be None), Object type)
            "Operators": (
                f'\n    ['
                f'\n        $/GFX/Sound/DepictionOperator_MovementSound_SM_Helico_Mi17,'
                f'\n        DepictionOperator_SoundProbe,'
                f'\n        Op_Mi_8TV_Gunship_SOV_Weapon1,'
                f'\n        Op_Mi_8TV_Gunship_SOV_Weapon2,'
                f'\n        Op_Mi_8TV_Gunship_SOV_Weapon3,'
                f'\n        DepictionOperator_CriticalEffects,'
                f'\n        DepictionOperator_HelicopterLanding,'
                f'\n        DepictionOperator_GroundPuff_Helico,'
                f'\n        DepictionOperator_ShadowPointCloudProvider,'
                f'\n        DepictionOperator_Rotors'
                f'\n        ('
                f'\n            HelixList = ['
                f'\n                THelix'
                f'\n                ('
                f'\n                    BladeCount = 5'
                f'\n                    BladesBoneName = "helice_ls_1"'
                f'\n                    BlurActionId = ['
                f'\n                        "FX_Helice_1",'
                f'\n                    ]'
                f'\n                    Clockwise = False'
                f'\n                    HelixBoneName = "bloc_moteur_1"'
                f'\n                    RotationAxis = 2'
                f'\n                    RotationSpeed = 242'
                f'\n                ),'
                f'\n                THelix'
                f'\n                ('
                f'\n                    BladeCount = 3'
                f'\n                    BladesBoneName = "helice_ls_2"'
                f'\n                    BlurActionId = ['
                f'\n                        "FX_Helice_2",'
                f'\n                    ]'
                f'\n                    Clockwise = False'
                f'\n                    HelixBoneName = "bloc_moteur_2"'
                f'\n                    RotationAxis = 1'
                f'\n                    RotationSpeed = 242'
                f'\n                ),'
                f'\n            ]'
                f'\n        ),'
                f'\n        DepictionOperator_Feedback_Degat_Level1,'
                f'\n        DepictionOperator_Feedback_Degat_Level2,'
                f'\n        DepictionOperator_Heat,'
                f'\n        DepictionOperator_EjectableProps_Helico,'
                f'\n    ]'
            ),
            "Actions": (
                f'MAP['
                f'\n                    ( [ "weapon_effet_tag1" ], Weapon_AA_R60M_Vympel ),'
                f'\n                    ( [ "weapon_effet_tag3" ], Weapon_RocketAir_S24_240mm_x2 )'
                f'\n                ]'
                f'\n                + DepictionAction_Stress_And_Wrecked_Helicopter'
                f'\n                + MAP [ (["FX_Helice_1"], Template_DepictionAction_Rotor( PaleLength = 2030 PaleCount = 5 RotationAxis = float3[0, 0, 1] SousMobile = "bloc_moteur_1" ))]'
                f'\n                + MAP [ (["FX_Helice_2"], Template_DepictionAction_Rotor( PaleLength = 350 PaleCount = 3 RotationAxis = float3[0, 1, 0] SousMobile = "bloc_moteur_2" ))]'
                f'\n                + DepictionAction_CriticalFX_Helicopter'                
            ),
            "SubDepictions": (
                f'\n    ['
                f'\n        TSubDepiction'
                f'\n        ('
                f'\n            Anchors = ['
                f'\n                "pilot",'
                f'\n                "pilot2",'
                f'\n            ]'
                f'\n            Depiction = Pilot_Pilote_Helico_SOV'
                f'\n        )'
                f'\n    ]'                    
            ),
            "SubDepictionGenerators": (
                f'\n    ['
                f'\n        SubGenerators_Mi_8TV_Gunship_SOV,'
                f'\n        RocketSubDepictionTemplate'
                f'\n        ('
                f'\n            UnitMeshDescriptor = $/GFX/DepictionResources/Modele_Mi_8TV_Gunship_SOV'
                f'\n            RocketMeshDescriptor = $/GFX/DepictionResources/Modele_Missile_S_24_240mm'
                f'\n            RocketCount = 2'
                f'\n            WeaponIndex = 3'
                f'\n            PhysicalProperty = "Tourelle3_MissileCount"'
                f'\n            AirStartGroupIndex = 2'
                f'\n            GroundStartGroupIndex = 1'
                f'\n        )'
                f'\n    ]'            
            ),
        },
    },
    
    "MissileCarriage_ndf": {
        ("MissileCarriage_Mi_8TV_Gunship_SOV", "TMissileCarriageConnoisseur"): { # (Namespace, Object type)
            "WeaponInfos": {
                0: "remove",
                1: {
                    "Count": 4,
                    "WeaponIndex": 1,
                },
            },
        },
        ("MissileCarriage_Mi_8TV_Gunship_SOV_Showroom", "TMissileCarriageConnoisseur"): {
            "WeaponInfos": {
                0: "remove",
                1: {
                    "Count": 4,
                    "WeaponIndex": 1,
                },
            },
        },
    },
    
    "MissileCarriageDepiction_ndf": {
        ("SubGenerators_Mi_8TV_Gunship_SOV", "TStaticMissileCarriageSubDepictionGenerator"): {
            "Missiles": {
                0: ("replace", (
                    f'TStaticMissileCarriageSubDepictionMissileInfo'
                    f'('
                    f'    Depiction = TemplateDepictionStaticMissiles'
                    f'    ('
                    f'        PhysicalProperty = "Tourelle1_MissileCount"'
                    f'        ProjectileModelResource = $/GFX/DepictionResources/Modele_Missile_Vympel_R60'
                    f'    )'
                    f'    MissileCount = 4'
                    f'    WeaponIndex = 1'
                    f')'
                )),
            },
        },
        ("SubGenerators_Showroom_Mi_8TV_Gunship_SOV", "TStaticMissileCarriageSubDepictionGenerator"): {
            "Missiles": {
                0: ("replace", (
                    f'TStaticMissileCarriageSubDepictionMissileInfo'
                    f'('
                    f'    Depiction = TemplateDepictionMissileShowroom'
                    f'    ('
                    f'        ProjectileModelResource = $/GFX/DepictionResources/Modele_Missile_Vympel_R60'
                    f'    )'
                    f'    MissileCount = 4'
                    f'    WeaponIndex = 1'
                    f')'
                )),
            },
        },
    },
}
# fmt: on
