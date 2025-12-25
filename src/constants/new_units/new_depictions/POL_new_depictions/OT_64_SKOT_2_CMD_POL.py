from typing import Dict, Any

# fmt: off
ot_64_skot_2_cmd_pol: Dict[str, Dict[str, Any]] = {
    "unit_name": "OT_64_SKOT_2_CMD_POL",
    "valid_files": ["DepictionVehicles.ndf", "ShowRoomUnits.ndf", "UnitCadavreDescriptor.ndf"],
    "DepictionVehicles_ndf": {
        "TacticVehicleDepictionRegistration": {
            f'unnamed TacticVehicleDepictionRegistration'
            f'('
            f"    CoatingName = 'OT_64_SKOT_2_CMD_POL'"
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

}
# fmt: on
