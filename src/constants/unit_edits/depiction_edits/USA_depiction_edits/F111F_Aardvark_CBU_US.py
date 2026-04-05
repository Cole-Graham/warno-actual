"""F111F_Aardvark_CBU_US depiction edits."""

from typing import Dict, Tuple, Union

# fmt: off
f111f_aardvark_cbu_us: Dict[str, Dict[Union[str, Tuple[str, str]], dict]] = {
    "unit_name": "F111F_Aardvark_CBU_US",
    "valid_files": ["DepictionAerialUnits.ndf","MissileCarriage.ndf", "MissileCarriageDepiction.ndf"],
    
    "DepictionAerialUnits_ndf": {
        (None, "TacticAerialDepictionRegistration"): {
            "Actions": (
                'MAP[\n'
                '    ( "weapon_effet_tag2", Weapon_Bomb_CBU_Mk20_Rockeye_II_250kg_x12 ),\n'
                ']\n'
                '+ DepictionAction_Stress_And_Wrecked_Avion\n'
                '+ DepictionAction_CriticalFX_Airplane\n'
                '+ DepictionAction_MovementFX_DoubleReactorAirplane\n'
                '+ DepictionAction_Flare_Double\n'
            )
        },
    },
    
    "MissileCarriage_ndf": {
        ("MissileCarriage_F111F_Aardvark_CBU_US", "TMissileCarriageConnoisseur"): { # (Namespace, Object type)
            "WeaponInfos": {
                0: {
                    "MissileCount": 12,
                },
            },
        },
    },
    
    "MissileCarriageDepiction_ndf": {
        ("SubGenerators_F111F_Aardvark_CBU_US", "TStaticMissileCarriageSubDepictionGenerator"): {
            "Missiles": {
                0: ("replace", (
                    f'TStaticMissileCarriageSubDepictionMissileInfo'
                    f'('
                    f'    Depiction = TemplateDepictionStaticMissiles'
                    f'    ('
                    f'        PhysicalProperty = "Tourelle2_MissileCount"'
                    f'        ProjectileModelResource = $/GFX/DepictionResources/Modele_Missile_MK20_RockeyeII'
                    f'    )'
                    f'    MissileCount = 12'
                    f'    WeaponIndex = 2'
                    f')'
                )),
            },
        },
        ("SubGenerators_Showroom_F111F_Aardvark_CBU_US", "TShowroomMissileCarriageSubDepictionGenerator"): {
            "Missiles": {
                0: ("replace", (
                    f'TShowroomMissileCarriageSubDepictionMissileInfo'
                    f'('
                    f'    Depiction = TemplateDepictionMissileShowroom'
                    f'    ('
                    f'        ProjectileModelResource = $/GFX/DepictionResources/Modele_Missile_MK20_RockeyeII'
                    f'    )'
                    f'    MissileCount = 12'
                    f'    WeaponIndex = 2'
                    f')'
                )),
            },
        },
    },
}
# fmt: on
