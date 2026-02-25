from typing import Dict, Any

# fmt: off
hmgteam_ags17_fj_ddr: Dict[str, Dict[str, Any]] = {
    "unit_name": "HMGteam_AGS17_FJ_DDR",
    "valid_files": ["DepictionVehicles.ndf", "ShowRoomUnits.ndf", "UnitCadavreDescriptor.ndf"],
    "DepictionVehicles_ndf": {
        
        "DepictionOperator_WeaponInstantFire": (
            f'DepictionOperator_HMGteam_AGS17_FJ_DDR_Weapon1 is DepictionOperator_WeaponInstantFire'
            f'('
            f'    FireEffectTag = "weapon_effet_tag1"'
            f'    Anchors = ["fx_tourelle1_tir_01"]'
            f'    WeaponShootDataPropertyName = ["WeaponShootData_0_1"]'
            f'    NbProj = 1'
            f')'
        ),
        "TacticVehicleDepictionRegistration": (
            f'unnamed TacticVehicleDepictionRegistration'
            f'  ('
            f'      CoatingName = "HMGteam_AGS17_FJ_DDR"'
            f'      Selector = SpecificVehicleDepictionSelector'
            f'      Alternatives = Alternatives_HMGteam_AGS17_FJ_DDR'
            f'      Operators = '
            f'      ['
            f'          DepictionOperator_CropFlattening,'
            f'          $/GFX/Sound/DepictionOperator_MovementSound_SM_Infanterie_GER,'
            f'          DepictionOperator_SoundProbe,'
            f'          DepictionOperator_CriticalEffects,'
            f'          DepictionOperator_Turret_1_Aim,'
            f'          DepictionOperator_Turret_1_HydraulicRecoil,'
            f'          DepictionOperator_HMGteam_AGS17_FJ_DDR_Weapon1,'
            f'          DepictionOperator_Carriable_ATGM,'
            f'          DepictionOperator_EjectableProps_Vehicle'
            f'      ]'
            f'      Actions = MAP['
            f'                  ( "weapon_effet_tag1", Weapon_Lance_grenade_AGS17 ),'
            f'              ]'
            f'              + DepictionAction_CriticalFX_ATGM'
            f'      SubDepictions = ['
            f'      ] + HumanSubDepictions_HMGteam_AGS17_FJ_DDR'
            f'  )'
        ),
    },
}
# fmt: on
