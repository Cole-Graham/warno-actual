"""F16E_TER_CLU_US depiction edits."""

from typing import Dict, Tuple, Union

# fmt: off
f16e_ter_clu_us: Dict[str, Dict[Union[str, Tuple[str, str]], dict]] = {
    "unit_name": "F16E_TER_CLU_US",
    "valid_files": [
        "DepictionAerialUnits.ndf",
        "DepictionAerialUnitsShowRoom.ndf",
        "MissileCarriage.ndf",
        "MissileCarriageDepiction.ndf",
    ],
    
    "DepictionAerialUnits_ndf": {
        
        "new_objects": {
            "weapon4": """
                Op_F16E_TER_CLU_US_Weapon4 is DepictionOperator_WeaponMissileCarriageFire
                (
                    Connoisseur = MissileCarriage_F16E_TER_CLU_US
                    FireEffectTag = "weapon_effet_tag4"
                    NbProj = 1
                    WeaponIndex = 4
                    WeaponShootDataPropertyName = 
                    [
                        "WeaponShootData_0_4",
                    ]
                )
            """,
        },
        
        (None, "TacticAerialDepictionRegistration"): {
            "Actions": (
                'MAP[\n'
                '    ( "weapon_effet_tag1", Weapon_GatlingAir_M61_Vulcan_20mm ),\n'
                '    ( "weapon_effet_tag2", Weapon_Bomb_CBU_Mk20_Rockeye_II_250kg_x6 ),\n'
                '    ( "weapon_effet_tag3", Weapon_Bomb_CBU_Mk20_Rockeye_II_250kg_x6 ),\n'
                '    ( "weapon_effet_tag4", Weapon_AA_AIM9M_Sidewinder ),\n'
                ']\n'
                '+ DepictionAction_Stress_And_Wrecked_Avion\n'
                '+ DepictionAction_CriticalFX_Airplane\n'
                '+ DepictionAction_MovementFX_SingleReactorAirplane_Smoky\n'
                '+ DepictionAction_Flare_Simple\n'
            ),
            "Operators": {
                6: ("insert", "Op_F16E_TER_CLU_US_Weapon4,"),
            },
        },
    },
    
    "DepictionAerialUnitsShowRoom_ndf": {
        (None, "ShowroomAerialDepictionRegistration"): {
            "MeshDescriptor": "$/GFX/DepictionResources/Modele_F16E_TER_2T_US",
        },
    },
    
    "MissileCarriage_ndf": {
        ("MissileCarriage_F16E_TER_CLU_US", "TMissileCarriageConnoisseur"): { # (Namespace, Object type)
            "MeshDescriptor": "$/GFX/DepictionResources/Modele_F16E_TER_2T_US",
            "WeaponInfos": (
                "[\n"
                f"    TMissileCarriageWeaponInfo"
                f"    ("
                f"        MissileCount = 6"
                f"        MissileType = eAGM"
                f"        MountingType = eMountingBomb"
                f"        WeaponIndex = 2"
                f"    ),\n"
                f"    TMissileCarriageWeaponInfo"
                f"    ("
                f"        MissileCount = 6"
                f"        MissileType = eAGM"
                f"        MountingType = eMountingBomb"
                f"        WeaponIndex = 3"
                f"    ),\n"
                f"    TMissileCarriageWeaponInfo"
                f"    ("
                f"        MissileCount = 2"
                f"        MissileType = eAAM"
                f"        WeaponIndex = 4"
                f"    ),\n"
                "]"
            ),
        },
    },
    
    "MissileCarriageDepiction_ndf": {
        ("SubGenerators_F16E_TER_CLU_US", "TStaticMissileCarriageSubDepictionGenerator"): {
            "Missiles": (
                "[\n"
                f"    TStaticMissileCarriageSubDepictionMissileInfo"
                f"    ("
                f"        Depiction = TemplateDepictionStaticMissiles"
                f"        ("
                f"            PhysicalProperty = \"Tourelle2_MissileCount\""
                f"            ProjectileModelResource = $/GFX/DepictionResources/Modele_Missile_MK20_RockeyeII"
                f"        )"
                f"        MissileCount = 6"
                f"        WeaponIndex = 2"
                f"    ),\n"
                f"    TStaticMissileCarriageSubDepictionMissileInfo"
                f"    ("
                f"        Depiction = TemplateDepictionStaticMissiles"
                f"        ("
                f"            PhysicalProperty = \"Tourelle3_MissileCount\""
                f"            ProjectileModelResource = $/GFX/DepictionResources/Modele_Missile_MK20_RockeyeII"
                f"        )"
                f"        MissileCount = 6"
                f"        WeaponIndex = 3"
                f"    ),\n"
                f"    TStaticMissileCarriageSubDepictionMissileInfo"
                f"    ("
                f"        Depiction = TemplateDepictionStaticMissiles"
                f"        ("
                f"            PhysicalProperty = \"Tourelle4_MissileCount\""
                f"            ProjectileModelResource = $/GFX/DepictionResources/Modele_Missile_SideWinder"
                f"        )"
                f"        MissileCount = 2"
                f"        WeaponIndex = 4"
                f"    ),\n"
                "]"
            ),
            "ReferenceMesh": "$/GFX/DepictionResources/Modele_F16E_TER_2T_US",
        },
        
        ("SubGenerators_Showroom_F16E_TER_CLU_US", "TShowroomMissileCarriageSubDepictionGenerator"): {
            "Missiles": (
                "[\n"
                f"    TShowroomMissileCarriageSubDepictionMissileInfo"
                f"    ("
                f"        Depiction = TemplateDepictionMissileShowroom"
                f"        ("
                f"            ProjectileModelResource = $/GFX/DepictionResources/Modele_Missile_MK20_RockeyeII"
                f"        )"
                f"        MissileCount = 6"
                f"        WeaponIndex = 2"
                f"    ),\n"
                f"    TShowroomMissileCarriageSubDepictionMissileInfo"
                f"    ("
                f"        Depiction = TemplateDepictionMissileShowroom"
                f"        ("
                f"            ProjectileModelResource = $/GFX/DepictionResources/Modele_Missile_MK20_RockeyeII"
                f"        )"
                f"        MissileCount = 6"
                f"        WeaponIndex = 3"
                f"    ),\n"
                f"    TShowroomMissileCarriageSubDepictionMissileInfo"
                f"    ("
                f"        Depiction = TemplateDepictionMissileShowroom"
                f"        ("
                f"            ProjectileModelResource = $/GFX/DepictionResources/Modele_Missile_SideWinder"
                f"        )"
                f"        MissileCount = 2"
                f"        WeaponIndex = 4"
                f"    ),\n"
                "]"
            ),
            "ReferenceMesh": "$/GFX/DepictionResources/Modele_F16E_TER_2T_US",
        },
    },
    
    "F16E_TER_2T_US_ndf": {
        "directory": "Avion",
        "ndf_code": """
            export Modele_F16E_TER_2T_US is TResourceMesh
            (
                Mesh="GameData:/Assets/3D/Units/US/Avion/f16e_ter_2t_us/F16E_TER_2T_US/F16E_TER_2T_US.fbx"
            )

            export Modele_F16E_TER_2T_US_MID is TResourceMesh
            (
                Mesh="GameData:/Assets/3D/Units/US/Avion/f16e_ter_2t_us/F16E_TER_2T_US/F16E_TER_2T_US.fbx"
            )

            export Modele_F16E_TER_2T_US_LOW is TResourceMesh
            (
                Mesh="GameData:/Assets/3D/Units/US/Avion/f16e_ter_2t_us/F16E_TER_2T_US/F16E_TER_2T_US.fbx"
            )

            export Modele_F16E_TER_2T_US_train is TResourceMesh
            (
                Mesh="GameData:/Assets/3D/Units/US/Avion/F16A_B15_Fighting_Falcon/F16A_B15_Fighting_Falcon_train.fbx"
            )""",
    },
}
# fmt: on
