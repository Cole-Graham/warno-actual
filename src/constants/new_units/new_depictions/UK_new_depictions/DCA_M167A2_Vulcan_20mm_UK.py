from typing import Dict, Any

# fmt: off
dca_m167a2_vulcan_20mm_uk: Dict[str, Dict[str, Any]] = {
    "unit_name": "DCA_M167A2_Vulcan_20mm_UK",
    "valid_files": ["DepictionVehicles.ndf", "ShowRoomUnits.ndf", "UnitCadavreDescriptor.ndf"],
    "DepictionVehicles_ndf": {
        
        "DepictionOperator_WeaponContinuousFire": (
            f'DepictionOperator_DCA_M167A2_Vulcan_20mm_UK_Weapon1 is DepictionOperator_WeaponContinuousFire'
            f'('
            f'    FireEffectTag = "weapon_effet_tag1"'
            f'    Anchors = ["fx_tourelle1_tir_01"]'
            f'    WeaponShootDataPropertyName = "WeaponShootData_0_1"'
            f'    WeaponActiveAndCanShootPropertyName = "WeaponActiveAndCanShoot_1"'
            f'    NbFX = 1'
            f')'
        ),
        "TacticVehicleDepictionDesc": (
            f'TacticDepiction_DCA_M167A2_Vulcan_20mm_UK is TacticVehicleDepictionDesc'
            f'('
            f"    CoatingName = 'DCA_M167A2_Vulcan_20mm_UK'"
            f'    Selector = SpecificVehicleDepictionSelector'
            f'    Alternatives = Alternatives_DCA_M167A2_Vulcan_20mm_UK'
            f'    Operators = '
            f'    ['
            f'        DepictionOperator_CropFlattening,'
            f'        $/GFX/Sound/DepictionOperator_MovementSound_SM_Infanterie_Crew_UK,'
            f'        DepictionOperator_SoundProbe,'
            f'        DepictionOperator_CriticalEffects,'
            f'        DepictionOperator_Turret_1_Aim,'
            f'        $/GFX/Sound/DepictionOperator_TurretSound_ST_SAM_US,'
            f'        DepictionOperator_Turret_1_HydraulicRecoil,'
            f'        DepictionOperator_DCA_M167A2_Vulcan_20mm_UK_Weapon1,'
            f'        DepictionOperator_Propulsion_Wheels_Canon,'
            f'        DepictionOperator_Carriable_Canon,'
            f'        DepictionOperator_EjectableProps_Vehicle'
            f'    ]'
            f'    Actions = MAP[\n'
            f'               ( "weapon_effet_tag1", Weapon_Gatling_M61_Vulcan_20mm_late_TOWED ),\n'
            f'            ]\n'
            f'            + DepictionAction_CriticalFX_Towed'
            f'    SubDepictions = [\n'
            f'    ] + HumanSubDepictions_DCA_M167A2_Vulcan_20mm_UK'
            f')'
        ),
    },
}
# fmt: on
