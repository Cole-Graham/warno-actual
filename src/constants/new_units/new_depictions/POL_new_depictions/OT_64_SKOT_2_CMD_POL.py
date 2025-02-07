from typing import Dict, Any

# fmt: off
ot_64_skot_2_cmd_pol: Dict[str, Dict[str, Any]] = {
    "unit_name": "OT_64_SKOT_2_CMD_POL",
    "valid_files": ["DepictionVehicles.ndf", "ShowRoomUnits.ndf", "UnitCadavreDescriptor.ndf"],
    "DepictionVehicles_ndf": {
        "TacticVehicleDepictionTemplate": {
            f'export Gfx_OT_64_SKOT_2_CMD_POL is TacticVehicleDepictionTemplate'
            f'('
            f"    CoatingName = 'OT_64_SKOT_2_POL'"
            f'    Selector = SpecificVehicleDepictionSelector'
            f'    Alternatives = Alternatives_OT_64_SKOT_2_CMD_POL'
            f'    Operators = '
            f'    ['
            f'        DepictionOperator_CropFlattening,'
            f'        $/GFX/Sound/DepictionOperator_MovementSound_SM_Tatra,'
            f'        DepictionOperator_SoundProbe,'
            f'        DepictionOperator_CriticalEffects,'
            f'        DepictionOperator_Chassis_MediumTank,'
            f'        DepictionOperator_Propulsion_Wheels_Generic,'
            f'        DepictionOperator_Heat,'
            f'        DepictionOperator_MovementFX_Amphibious,'
            f'        DepictionOperator_EjectableProps_Vehicle'
            f'    ]'
            f'    Actions = MAP['
            f'\n            ]'
            f'\n            + DepictionAction_Stress_And_Wrecked'
            f'\n            + DepictionAction_MovementFX_Wheeled'
            f'\n            + DepictionAction_CriticalFX_Tank'
            f'\n            + DepictionAction_FX_Amphibious_NoPropulsion'
            f')'
        },
    },
    #  we probably shouldn't and/or don't need to manually define these
    # "ShowRoomUnits_ndf": {
    #     "TEntityDescriptor": {
    #         f'export Descriptor_ShowRoomUnit_OT_64_SKOT_2_CMD_POL is TEntityDescriptor'
    #         f'('
    #         f'    DescriptorId = GUID:{{6211126c-6458-4edc-8e7e-a7d17338c60a}}'
    #         f"    ClassNameForDebug = 'ShowRoomUnit_OT_64_SKOT_2_CMD_POL'"
    #         f'    ModulesDescriptors = '
    #         f'    ['
    #         f'        TTypeUnitModuleDescriptor'
    #         f'        ('
    #         f'            Coalition = ECoalition/Axis'
    #         f"            MotherCountry = 'POL'"
    #         f'            AcknowUnitType = ~/TAcknowUnitType_Command'
    #         f"            TypeUnitFormation = 'Supply'"
    #         f'        ),'
    #         f'        ~/ShowroomPositionModuleDescriptor,'
    #         f'        TApparenceModuleDescriptor'
    #         f'        ('
    #         f'            PickableObject = True'
    #         f'            Depiction = $/GFX/Depiction/Gfx_OT_64_SKOT_2_CMD_POL_Showroom'
    #         f'            ReferenceMesh = $/GFX/DepictionResources/Modele_OT_64_SKOT_2_POL'
    #         f'        ),'
    #         f'        ~/LinkTeamModuleDescriptor,'
    #         f'        ~/EffectApplierModuleDescriptor,'
    #         f'        TExperienceModuleDescriptor'
    #         f'        ('
    #         f'            ExperienceLevelsPackDescriptor = ~/ExperienceLevelsPackDescriptor_XP_pack_simple_v3'
    #         f'            CanWinExperience = True'
    #         f'            ExperienceGainBySecond = ~/ExperienceGainBySecond'
    #         f'            ExperienceMultiplierBonusOnKill = ~/ExperienceMultiplierBonusOnKill'
    #         f'        ),'
    #         f'        TCameraShowroomModuleDescriptor'
    #         f'        ('
    #         f'            SpawnType = EShowroomSpawnType/Vehicle'
    #         f'            HasServants = False'
    #         f'        )'
    #         f'    ]'
    #         f')'
    #     }
    # },
    # "UnitCadavreDescriptor_ndf": {
    #     "TEntityDescriptor": {
    #         f"Descriptor_UnitCadavre_OT_64_SKOT_2_CMD_POL is TEntityDescriptor"
    #         f"("
    #         f"    DescriptorId = GUID:{{8f3685da-a277-41c1-8870-3d60c6acc84f}}"
    #         f"    ClassNameForDebug = 'Unit_CadavreOT_64_SKOT_2_CMD_POL'"
    #         f"    ModulesDescriptors = "
    #         f"    ["
    #         f"        TTypeUnitModuleDescriptor"
    #         f"        ("
    #         f"            Coalition = ECoalition/Axis"
    #         f"            MotherCountry = 'POL'"
    #         f"            AcknowUnitType = ~/TAcknowUnitType_Transport"
    #         f"            TypeUnitFormation = 'Char'"
    #         f"        ),"
    #         f"        ~/EmptyTagsModuleDescriptor,"
    #         f"        ~/CadavreFlagsModuleDescriptor,"
    #         f"        ~/UnitCadavrePositionModuleDescriptor,"
    #         f"        ~/LinkTeamModuleDescriptor,"
    #         f"        UnitCadavreModuleDescriptor"
    #         f"        ("
    #         f"            KillAsVehicule = True"
    #         f"            CadavreDuration = ~/CadavreDurationApresFeu"
    #         f"            DeathExplosionAmmo = $/GFX/Weapon/Ammo_Mort_Unite_faible"
    #         f"            ModuleDescriptorsToSteal = "
    #         f"            ["
    #         f"                ~/Descriptor_Unit_OT_64_SKOT_2_POL/ApparenceModel,"
    #         f"                ~/Descriptor_Unit_OT_64_SKOT_2_POL/LandMovement,"
    #         f"                ~/Descriptor_Unit_OT_64_SKOT_2_POL/GenericMovement,"
    #         f"            ]"
    #         f"        ),"
    #         f"        ~/Descriptor_Unit_OT_64_SKOT_2_POL/ApparenceModel,"
    #         f"        ~/Descriptor_Unit_OT_64_SKOT_2_POL/LandMovement,"
    #         f"        ~/Descriptor_Unit_OT_64_SKOT_2_POL/GenericMovement,"
    #         f"        ~/PackSignauxModuleDescriptor,"
    #         f"        ~/DebugModuleDescriptor"
    #         f"    ]"
    #         f")"
    #     }
    # },
}
# fmt: on
