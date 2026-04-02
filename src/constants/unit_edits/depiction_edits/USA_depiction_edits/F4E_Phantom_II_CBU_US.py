"""F4E_Phantom_II_CBU_US depiction edits."""

from typing import Dict, Tuple, Union

# fmt: off
f4e_phantom_ii_cbu_us: Dict[str, Dict[Union[str, Tuple[str, str]], dict]] = {
    "unit_name": "F4E_Phantom_II_CBU_US",
    "valid_files": ["DepictionAerialUnits.ndf", "MissileCarriage.ndf", "MissileCarriageDepiction.ndf"],
    
    "DepictionAerialUnits_ndf": {
        (None, "TacticAerialDepictionRegistration"): {
            "Actions": (
                'MAP[\n'
                '    ( "weapon_effet_tag1", Weapon_GatlingAir_M61_Vulcan_20mm ),\n'
                '    ( "weapon_effet_tag2", Weapon_Bomb_CBU_Mk20_Rockeye_II_250kg_x5 ),\n'
                '    ( "weapon_effet_tag3", Weapon_AA_AIM9J_Sidewinder ),\n'
                ']\n'
                '+ DepictionAction_Stress_And_Wrecked_Avion\n'
                '+ DepictionAction_CriticalFX_Airplane\n'
                '+ DepictionAction_MovementFX_DoubleReactorAirplane_VerySmoky\n'
                '+ DepictionAction_Flare_Simple\n'
            )
        },
    },
    
    "MissileCarriage_ndf": {
        ("MissileCarriage_F4E_Phantom_II_CBU_US", "TMissileCarriageConnoisseur"): { # (Namespace, Object type)
            "WeaponInfos": {
                0: {
                    "MissileCount": 5,
                },
            },
        },
    },
    
    "MissileCarriageDepiction_ndf": {
        ("SubGenerators_F4E_Phantom_II_CBU_US", "TStaticMissileCarriageSubDepictionGenerator"): {
            "Missiles": {
                0: ("replace", (
                    f'TStaticMissileCarriageSubDepictionMissileInfo'
                    f'('
                    f'    Depiction = TemplateDepictionStaticMissiles'
                    f'    ('
                    f'        PhysicalProperty = "Tourelle2_MissileCount"'
                    f'        ProjectileModelResource = $/GFX/DepictionResources/Modele_Missile_MK20_RockeyeII'
                    f'    )'
                    f'    MissileCount = 5'
                    f'    WeaponIndex = 2'
                    f')'
                )),
            },
        },
        ("SubGenerators_Showroom_F4E_Phantom_II_CBU_US", "TShowroomMissileCarriageSubDepictionGenerator"): {
            "Missiles": {
                0: ("replace", (
                    f'TShowroomMissileCarriageSubDepictionMissileInfo'
                    f'('
                    f'    Depiction = TemplateDepictionMissileShowroom'
                    f'    ('
                    f'        ProjectileModelResource = $/GFX/DepictionResources/Modele_Missile_MK20_RockeyeII'
                    f'    )'
                    f'    MissileCount = 5'
                    f'    WeaponIndex = 2'
                    f')'
                )),
            },
        },
    },
}
# fmt: on
