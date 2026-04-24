"""F111F_Aardvark_CBU_US depiction edits."""

from typing import Dict, Tuple, Union

# fmt: off
f111f_aardvark_cbu_us: Dict[str, Dict[Union[str, Tuple[str, str]], dict]] = {
    "unit_name": "F111F_Aardvark_CBU_US",
    "valid_files": [
        "DepictionAerialUnits.ndf",
        "DepictionAerialUnitsShowRoom.ndf",
        "MissileCarriage.ndf",
        "MissileCarriageDepiction.ndf",
    ],
    
    "DepictionAerialUnits_ndf": {
        
        "new_objects": {
            "weapon3": """
                Op_F111F_Aardvark_CBU_US_Weapon3 is DepictionOperator_WeaponMissileCarriageFire
                (
                    Connoisseur = MissileCarriage_F111F_Aardvark_CBU_US
                    FireEffectTag = "weapon_effet_tag3"
                    NbProj = 1
                    WeaponIndex = 3
                    WeaponShootDataPropertyName = 
                    [
                        "WeaponShootData_0_3",
                    ]
                )
            """,
        },
        
        (None, "TacticAerialDepictionRegistration"): {
            "Actions": (
                'MAP[\n'
                '    ( "weapon_effet_tag2", Weapon_Bomb_CBU_Mk20_Rockeye_II_250kg_x12 ),\n'
                '    ( "weapon_effet_tag3", Weapon_Bomb_CBU_Mk20_Rockeye_II_250kg_x12 ),\n'
                ']\n'
                '+ DepictionAction_Stress_And_Wrecked_Avion\n'
                '+ DepictionAction_CriticalFX_Airplane\n'
                '+ DepictionAction_MovementFX_DoubleReactorAirplane\n'
                '+ DepictionAction_Flare_Double\n'
            ),
            "Operators": {
                3: ("insert", "Op_F111F_Aardvark_CBU_US_Weapon3,"),
            },
        },
    },
    
    "DepictionAerialUnitsShowRoom_ndf": {
        (None, "ShowroomAerialDepictionRegistration"): {
            "MeshDescriptor": "$/GFX/DepictionResources/Modele_F111F_Sweep40_US",
        },
    },
    
    "MissileCarriage_ndf": {
        ("MissileCarriage_F111F_Aardvark_CBU_US", "TMissileCarriageConnoisseur"): { # (Namespace, Object type)
            "MeshDescriptor": "$/GFX/DepictionResources/Modele_F111F_Sweep40_US",
            "WeaponInfos": {
                0: ("edit", {
                    "MissileCount": 12,
                }),
                
                1: ("insert", (
                    f'TMissileCarriageWeaponInfo'
                    f'('
                    f'    MissileCount = 12'
                    f'    MissileType = eAGM'
                    f'    MountingType = eMountingBomb'
                    f'    WeaponIndex = 3'
                    f')'
                )),
            },
        },
    },
    
    "MissileCarriageDepiction_ndf": {
        ("SubGenerators_F111F_Aardvark_CBU_US", "TStaticMissileCarriageSubDepictionGenerator"): {
            "Missiles": {
                0: ("replace", (
                    f'TStaticMissileCarriageSubDepictionMissileInfo'
                    f'('
                    f'    Depiction = TemplateDepictionStaticMissiles'
                    f'    ('
                    f'        PhysicalProperty = "Tourelle1_MissileCount"'
                    f'        ProjectileModelResource = $/GFX/DepictionResources/Modele_Missile_MK20_RockeyeII'
                    f'    )'
                    f'    MissileCount = 12'
                    f'    WeaponIndex = 2'
                    f')'
                )),
                1: ("insert", (
                    f'TStaticMissileCarriageSubDepictionMissileInfo'
                    f'('
                    f'    Depiction = TemplateDepictionStaticMissiles'
                    f'    ('
                    f'        PhysicalProperty = "Tourelle2_MissileCount"'
                    f'        ProjectileModelResource = $/GFX/DepictionResources/Modele_Missile_MK20_RockeyeII'
                    f'    )'
                    f'    MissileCount = 12'
                    f'    WeaponIndex = 3'
                    f')'
                )),
            },
            "ReferenceMesh": "$/GFX/DepictionResources/Modele_F111F_Sweep40_US",
        },
        ("SubGenerators_Showroom_F111F_Aardvark_CBU_US", "TShowroomMissileCarriageSubDepictionGenerator"): {
            "Missiles": {
                0: ("replace", (
                    f'TShowroomMissileCarriageSubDepictionMissileInfo'
                    f'('
                    f'    Depiction = TemplateDepictionMissileShowroom'
                    f'    ('
                    f'        ProjectileModelResource = $/GFX/DepictionResources/Modele_Missile_MK20_RockeyeII'
                    f'    )'
                    f'    MissileCount = 12'
                    f'    WeaponIndex = 2'
                    f')'
                )),
                1: ("insert", (
                    f'TShowroomMissileCarriageSubDepictionMissileInfo'
                    f'('
                    f'    Depiction = TemplateDepictionMissileShowroom'
                    f'    ('
                    f'        ProjectileModelResource = $/GFX/DepictionResources/Modele_Missile_MK20_RockeyeII'
                    f'    )'
                    f'    MissileCount = 12'
                    f'    WeaponIndex = 3'
                    f')'
                )),
            },
            "ReferenceMesh": "$/GFX/DepictionResources/Modele_F111F_Sweep40_US",
        },
    },
    
    "F111F_Sweep40_US_ndf": {
        "directory": "Avion",
        "ndf_code": """
            export Modele_F111F_Sweep40_US is TResourceMesh
            (
                Mesh="GameData:/Assets/3D/Units/US/Avion/f111f_sweep40_us/F111F_Sweep40_US/F111F_Sweep40_US.fbx"
            )

            export Modele_F111F_Sweep40_US_MID is TResourceMesh
            (
                Mesh="GameData:/Assets/3D/Units/US/Avion/f111f_sweep40_us/F111F_Sweep40_US/F111F_Sweep40_US.fbx"
            )

            export Modele_F111F_Sweep40_US_LOW is TResourceMesh
            (
                Mesh="GameData:/Assets/3D/Units/US/Avion/f111f_sweep40_us/F111F_Sweep40_US/F111F_Sweep40_US.fbx"
            )

            export Modele_F111F_Sweep40_US_train is TResourceMesh
            (
                Mesh="GameData:/Assets/3D/Units/US/Avion/Aardvark_F_111F/Aardvark_F_111F_train.fbx"
            )""",
    },
}
# fmt: on
