"""Mi_24P_s8_AT_DDR depiction edits."""

from typing import Dict, Tuple, Union

# fmt: off
mi_24p_s8_at_ddr: Dict[str, Dict[Union[str, Tuple[str, str]], dict]] = {
    "unit_name": "Mi_24P_s8_AT_DDR",
    "valid_files": ["DepictionAerialUnits.ndf"],
    "DepictionAerialUnits_ndf": {
        ("Op_Mi_24P_s8_AT_DDR_Weapon1", "DepictionOperator_WeaponContinuousFire"): {
            "add_members": [
                ("WeaponActiveAndCanShootPropertyName", "'WeaponActiveAndCanShoot_1'"),
            ],
            "replace_members": [
                ("NbProj", "NbFX", None), # member, replacement, new value (None if old value should be used)
            ],
            "WeaponShootDataPropertyName": "'WeaponShootData_0_1'",
        },
        
        ("Op_Mi_24P_s8_AT_DDR_Weapon2", "DepictionOperator_WeaponContinuousFire"): {
            "add_members": [
                ("WeaponActiveAndCanShootPropertyName", "'WeaponActiveAndCanShoot_2'"),
            ],
            "replace_members": [
                ("NbProj", "NbFX", None),
            ],
            "WeaponShootDataPropertyName": "'WeaponShootData_0_2'",
        },
        
        ("Gfx_Mi_24P_s8_AT_DDR", "TacticAerialDepictionTemplate"): { # (Namespace (can be None), Object type)
            "Actions": (
                f'MAP['
                f'\n                    ( "weapon_effet_tag1", Weapon_GatlingAir_AP_Gsh_30_2_30mm_x2 ),'
                f'\n                    ( "weapon_effet_tag2", Weapon_GatlingAir_Gsh_30_2_30mm_x2 ),'
                f'\n                    ( "weapon_effet_tag3", Weapon_AGM_9M114M_KokonM_x4 ),'
                f'\n                    ( "weapon_effet_tag4", Weapon_RocketAir_B8_80mm_x10 )'
                f'\n                ]'
                f'\n                + DepictionAction_Stress_And_Wrecked_Helicopter'
                f'\n                + MAP [ ("FX_Helice_1", Template_DepictionAction_Rotor( PaleLength = 1800 PaleCount = 5 RotationAxis = float3[0, 0, 1] SousMobile = "bloc_moteur_1" ))]'
                f'\n                + MAP [ ("FX_Helice_2", Template_DepictionAction_Rotor( PaleLength = 450 PaleCount = 3 RotationAxis = float3[0, 1, 0] SousMobile = "bloc_moteur_2" ))]'
                f'\n                + DepictionAction_CriticalFX_Helicopter'
                f'\n                + DepictionAction_Flare_Simple'
            ),
        },
    },
}
# fmt: on
