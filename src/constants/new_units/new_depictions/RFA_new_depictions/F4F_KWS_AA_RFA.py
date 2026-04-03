from typing import Dict, Any

# fmt: off
f4f_kws_aa_rfa: Dict[str, Dict[str, Any]] = {
    "unit_name": "F4F_KWS_AA_RFA",
    "valid_files": ["DepictionAerialUnits.ndf", "DepictionAerialUnitsShowRoom.ndf", "MissileCarriage.ndf",
                    "MissileCarriageDepiction.ndf"],
    "DepictionAerialUnits_ndf": {
        
        "weapon1": """
            Op_F4F_KWS_AA_RFA_Weapon1 is DepictionOperator_WeaponContinuousFire
            (
                Anchors = ["fx_tourelle1_tir_01"]
                FireEffectTag = "weapon_effet_tag1"
                NbFX = 1
                WeaponActiveAndCanShootPropertyName = "WeaponActiveAndCanShoot_1"
                WeaponShootDataPropertyName = "WeaponShootData_0_1"
            )""",

        "weapon2": 
            """Op_F4F_KWS_AA_RFA_Weapon2 is DepictionOperator_WeaponMissileCarriageFire
            (
                Connoisseur = MissileCarriage_F4F_KWS_AA_RFA
                FireEffectTag = "weapon_effet_tag2"
                NbProj = 1
                WeaponIndex = 2
                WeaponShootDataPropertyName = 
                [
                    "WeaponShootData_0_2",
                ]
            )""",

        "weapon3": """
            Op_F4F_KWS_AA_RFA_Weapon3 is DepictionOperator_WeaponMissileCarriageFire
            (
                Connoisseur = MissileCarriage_F4F_KWS_AA_RFA
                FireEffectTag = "weapon_effet_tag3"
                NbProj = 1
                WeaponIndex = 3
                WeaponShootDataPropertyName = 
                [
                    "WeaponShootData_0_3",
                ]
            )""",

        "TacticAerialDepictionRegistration": """
            unnamed TacticAerialDepictionRegistration
            (
                Deviator = DepictionDeviator_Airplane
                AdditionalTextures = $/M3D/Shader/AirplaneDestTextures
                Selector = SpecificMechanicalDepictionSelector
                BlackHoleKey = 'F4F_KWS_AA_RFA'
                Alternatives = Alternatives_F4F_KWS_AA_RFA

                Operators = 
                    [
                        $/GFX/Sound/DepictionOperator_MovementSound_SM_SD_avion_multirole_F4,
                        DepictionOperator_SoundProbe,
                        Op_F4F_KWS_AA_RFA_Weapon1,
                        Op_F4F_KWS_AA_RFA_Weapon2,
                        Op_F4F_KWS_AA_RFA_Weapon3,
                        DepictionOperator_CriticalEffects,
                        DepictionOperator_AirplaneParts,
                        DepictionOperator_Airplane,
                        DepictionOperator_AirplaneShadow,
                        DepictionOperator_Feedback_Degat_Level1,
                        DepictionOperator_Feedback_Degat_Level2,
                        DepictionOperator_EjectableProps_Plane,
                        DepictionOperator_Flares,
                    ]
                    Actions = MAP[
                                ( "weapon_effet_tag1", Weapon_GatlingAir_M61_Vulcan_20mm ),
                                ( "weapon_effet_tag2", Weapon_AA_AIM120A_AMRAAM ),
                                ( "weapon_effet_tag3", Weapon_AA_AIM9M_Sidewinder ),
                            ]
                            + DepictionAction_Stress_And_Wrecked_Avion
                            + DepictionAction_CriticalFX_Airplane
                            + DepictionAction_MovementFX_DoubleReactorAirplane_VerySmoky
                            + DepictionAction_Flare_Simple

                    SubDepictions = 
                    [
                        TSubDepiction
                        (
                            Anchors = 
                            [
                                "pilot",
                                "pilot2",
                            ]
                            Depiction = Pilot_Pilote_US
                        ),
                    ]        
                    SubDepictionGenerators = [ SubGenerators_F4F_KWS_AA_RFA ]
            )""",
    },
    
    "DepictionAerialUnitsShowroom_ndf": {
        "ShowroomAerialDepictionRegistration": """
            unnamed ShowroomAerialDepictionRegistration
            (
                BlackHoleKey = 'showroom_F4F_KWS_AA_RFA'
                MeshDescriptor = $/GFX/DepictionResources/Modele_F4F_KWS_AA_RFA
                SubDepictionGenerators = 
                [
                    SubGenerators_Showroom_F4F_KWS_AA_RFA,
                ]
                SubDepictions = 
                [
                    ShowroomLandingGear
                    (
                        MeshDescriptor = $/GFX/DepictionResources/Modele_F4F_KWS_AA_RFA_train
                    ),
                ]
            )""",
    },
    
    "MissileCarriage_ndf": {
        "carriage": """
            export MissileCarriage_F4F_KWS_AA_RFA is TMissileCarriageConnoisseur
            (
                MeshDescriptor = $/GFX/DepictionResources/Modele_F4F_KWS_AA_RFA
                PylonSet = ~/DepictionPylonSet_Airplane_Default
                WeaponInfos = 
                [
                    TMissileCarriageWeaponInfo( MissileCount=3 MissileType=eAAM WeaponIndex=2 ),
                    TMissileCarriageWeaponInfo( MissileCount=2 MissileType=eAAM WeaponIndex=3 ),
                ]
            )""",
        "carriage_showroom": """
            export MissileCarriage_F4F_KWS_AA_RFA_Showroom is TMissileCarriageConnoisseur
            (
                MeshDescriptor = $/GFX/DepictionResources/Modele_F4F_KWS_AA_RFA
                PylonSet = ~/DepictionPylonSet_Airplane_Default_Showroom
                WeaponInfos = ~/MissileCarriage_F4F_KWS_AA_RFA.WeaponInfos
            )""",
    },
    
    "MissileCarriageDepiction_ndf": {
        "carriage_depiction": """
            SubGenerators_F4F_KWS_AA_RFA is TStaticMissileCarriageSubDepictionGenerator
            (
                MissileCarriageConnoisseur = MissileCarriage_F4F_KWS_AA_RFA
                Missiles = 
                [
                    TStaticMissileCarriageSubDepictionMissileInfo
                    (
                        Depiction = TemplateDepictionStaticMissiles
                        (
                            PhysicalProperty = "Tourelle2_MissileCount"
                            ProjectileModelResource = $/GFX/DepictionResources/Modele_Missile_AIM_120_Amraam
                        )
                        MissileCount = 3
                        WeaponIndex = 2
                    ),
                    TStaticMissileCarriageSubDepictionMissileInfo
                    (
                        Depiction = TemplateDepictionStaticMissiles
                        (
                            PhysicalProperty = "Tourelle3_MissileCount"
                            ProjectileModelResource = $/GFX/DepictionResources/Modele_Missile_SideWinder
                        )
                        MissileCount = 2
                        WeaponIndex = 3
                    ),
                ]
                Pylons = ~/DepictionPylonSet_Airplane_Default
                ReferenceMesh = $/GFX/DepictionResources/Modele_F4F_KWS_AA_RFA
            )""",
        "carriage_depiction_showroom": """
            SubGenerators_Showroom_F4F_KWS_AA_RFA is TShowroomMissileCarriageSubDepictionGenerator
            (
                MissileCarriageConnoisseur = MissileCarriage_F4F_KWS_AA_RFA_Showroom
                Missiles = 
                [
                    TShowroomMissileCarriageSubDepictionMissileInfo
                    (
                        Depiction = TemplateDepictionMissileShowroom
                        (
                            ProjectileModelResource = $/GFX/DepictionResources/Modele_Missile_AIM_120_Amraam
                        )
                        MissileCount = 3
                        WeaponIndex = 2
                    ),
                    TShowroomMissileCarriageSubDepictionMissileInfo
                    (
                        Depiction = TemplateDepictionMissileShowroom
                        (
                            ProjectileModelResource = $/GFX/DepictionResources/Modele_Missile_SideWinder
                        )
                        MissileCount = 2
                        WeaponIndex = 3
                    ),
                ]
                Pylons = ~/DepictionPylonSet_Airplane_Default_Showroom
                ReferenceMesh = $/GFX/DepictionResources/Modele_F4F_KWS_AA_RFA
            )""",
    },
    "F4F_KWS_AA_RFA_ndf": {
        "directory": "Avion",
        "ndf_code": """
            export Modele_F4F_KWS_AA_RFA is TResourceMesh
            (
                Mesh="GameData:/Assets/3D/Units/RFA/Avion/F4F_ICE/F4F_ICE/F4F_ICE.fbx"
            )

            export Modele_F4F_KWS_AA_RFA_MID is TResourceMesh
            (
                Mesh="GameData:/Assets/3D/Units/RFA/Avion/F4F_ICE/F4F_ICE/F4F_ICE.fbx"
            )

            export Modele_F4F_KWS_AA_RFA_LOW is TResourceMesh
            (
                Mesh="GameData:/Assets/3D/Units/RFA/Avion/F4F_ICE/F4F_ICE/F4F_ICE.fbx"
            )

            export Modele_F4F_KWS_AA_RFA_train is TResourceMesh
            (
                Mesh="GameData:/Assets/3D/Units/RFA/Avion/F4F_ICE/F4F_ICE/F4G_train.fbx"
            )""",
    },
}
# fmt: on
