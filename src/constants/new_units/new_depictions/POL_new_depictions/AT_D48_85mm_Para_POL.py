from typing import Dict, Any

# fmt: off

at_d48_85mm_para_pol: Dict[str, Dict[str, Any]] = {
    "unit_name": "AT_D48_85mm_Para_POL",
    "valid_files": ["DepictionVehicles.ndf", "ShowRoomUnits.ndf", "UnitCadavreDescriptor.ndf"],
    "DepictionVehicles_ndf": {
        
        "DepictionOperator_WeaponInstantFire": (
            f'DepictionOperator_AT_D48_85mm_Para_POL_Weapon1 is DepictionOperator_WeaponInstantFire'
            f'('
            f'    FireEffectTag = "weapon_effet_tag1"'
            f'    Anchors = ["fx_tourelle1_tir_01"]'
            f'    WeaponShootDataPropertyName = ["WeaponShootData_0_1"]'
            f'    NbProj = 1'
            f')'
        ),
        "TacticVehicleDepictionRegistration": (
            f'unnamed TacticVehicleDepictionRegistration'
            f'    ('
            f'        CoatingName = "AT_D48_85mm_Para_POL"'
            f'        Selector = SpecificVehicleDepictionSelector'
            f'        Alternatives = Alternatives_AT_D48_85mm_Para_POL'
            f'        Operators = '
            f'        ['
            f'            DepictionOperator_CropFlattening,'
            f'            DepictionOperator_SoundProbe,'
            f'            DepictionOperator_CriticalEffects,'
            f'            DepictionOperator_Turret_1_Aim,'
            f'            DepictionOperator_Turret_1_HydraulicRecoil,'
            f'            DepictionOperator_AT_D48_85mm_Para_POL_Weapon1,'
            f'            DepictionOperator_AT_D48_85mm_Para_POL_Weapon2,'
            f'            DepictionOperator_Propulsion_Wheels_Canon,'
            f'            DepictionOperator_Carriable_Canon_Arms30,'
            f'            DepictionOperator_EjectableProps_Vehicle'
            f'        ]'
            f'        Actions = MAP['
            f'                    ( "weapon_effet_tag1", Weapon_Canon_AP_85mm_D48 ),'
            f'                    ( "weapon_effet_tag2", Weapon_Canon_HE_85mm_D48 ),'
            f'                ]'
            f'                + DepictionAction_CriticalFX_Towed'
            f'        SubDepictions = ['
            f'        ] + HumanSubDepictions_AT_D48_85mm_Para_POL'
            f'    )'
        ),
    },
}

# fmt: on