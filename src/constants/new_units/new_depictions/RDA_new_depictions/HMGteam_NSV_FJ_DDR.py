from typing import Dict, Any

# fmt: off

hmgteam_nsv_fj_ddr: Dict[str, Dict[str, Any]] = {
    "unit_name": "HMGteam_NSV_FJ_DDR",
    "valid_files": ["DepictionVehicles.ndf", "ShowRoomUnits.ndf", "UnitCadavreDescriptor.ndf"],
    "DepictionVehicles_ndf": {       
        "DepictionOperator_WeaponContinuousFire": (
            f'DepictionOperator_HMGteam_NSV_FJ_DDR_Weapon1 is DepictionOperator_WeaponContinuousFire'
            f'('
            f'    FireEffectTag = "weapon_effet_tag1"'
            f'    Anchors = ["fx_tourelle1_tir_01"]'
            f'    WeaponShootDataPropertyName = "WeaponShootData_0_1"'
            f'    WeaponActiveAndCanShootPropertyName = "WeaponActiveAndCanShoot_1"'
            f'    NbFX = 1'
            f')'
        ),
        "TacticVehicleDepictionRegistration": (
            f'unnamed TacticVehicleDepictionRegistration'
            f'    ('
            f'        CoatingName = "HMGteam_NSV_FJ_DDR"'
            f'        Selector = SpecificVehicleDepictionSelector'
            f'        Alternatives = Alternatives_HMGteam_NSV_FJ_DDR'
            f'        Operators = '
            f'        ['
            f'            DepictionOperator_CropFlattening,'
            f'            $/GFX/Sound/DepictionOperator_MovementSound_SM_Infanterie_POL,'
            f'            DepictionOperator_SoundProbe,'
            f'            DepictionOperator_CriticalEffects,'
            f'            DepictionOperator_Turret_1_Aim,'
            f'            DepictionOperator_Turret_1_TurretRockingRecoil_LightMachineGun,'
            f'            DepictionOperator_HMGteam_NSV_FJ_DDR_Weapon1,'
            f'            DepictionOperator_Carriable_ATGM,'
            f'            DepictionOperator_EjectableProps_Vehicle'
            f'        ]'
            f'        Actions = MAP['
            f'                    ( "weapon_effet_tag1", Weapon_HMG_team_12_7_mm_NSV ),'
            f'                ]'
            f'                + DepictionAction_CriticalFX_ATGM'
            f'        SubDepictions = ['
            f'        ] + HumanSubDepictions_HMGteam_NSV_FJ_DDR'
            f'    )'
        ),
    },
}

# fmt: on
