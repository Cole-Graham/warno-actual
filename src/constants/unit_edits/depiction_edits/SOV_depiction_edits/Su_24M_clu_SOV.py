"""Su_24M_clu_SOV depiction edits."""

from typing import Dict, Tuple, Union

# fmt: off
su_24m_clu_sov: Dict[str, Dict[Union[str, Tuple[str, str]], dict]] = {
    "unit_name": "Su_24M_clu_SOV",
    "valid_files": ["DepictionAerialUnits.ndf","MissileCarriage.ndf", "MissileCarriageDepiction.ndf"],
    
    "DepictionAerialUnits_ndf": {
        (None, "TacticAerialDepictionRegistration"): {
            "Actions": (
                'MAP[\n'
                '    ( "weapon_effet_tag2", Weapon_Bomb_CLU_RBK_250kg_x8 ),\n'
                ']\n'
                '+ DepictionAction_Stress_And_Wrecked_Avion\n'
                '+ DepictionAction_CriticalFX_Airplane\n'
                '+ DepictionAction_MovementFX_DoubleReactorAirplane\n'
                '+ DepictionAction_Flare_Double\n'
            )
        },
    },
    
    "MissileCarriage_ndf": {
        ("MissileCarriage_Su_24M_clu_SOV", "TMissileCarriageConnoisseur"): { # (Namespace, Object type)
            "WeaponInfos": {
                0: {
                    "MissileCount": 16,
                },
            },
        },
    },
    
    "MissileCarriageDepiction_ndf": {
        ("SubGenerators_Su_24M_clu_SOV", "TStaticMissileCarriageSubDepictionGenerator"): {
            "Missiles": {
                0: ("replace", (
                    f'TStaticMissileCarriageSubDepictionMissileInfo'
                    f'('
                    f'    Depiction = TemplateDepictionStaticMissiles'
                    f'    ('
                    f'        PhysicalProperty = "Tourelle2_MissileCount"'
                    f'        ProjectileModelResource = $/GFX/DepictionResources/Modele_Missile_FAB_250'
                    f'    )'
                    f'    MissileCount = 16'
                    f'    WeaponIndex = 2'
                    f')'
                )),
            },
        },
        ("SubGenerators_Showroom_Su_24M_clu_SOV", "TShowroomMissileCarriageSubDepictionGenerator"): {
            "Missiles": {
                0: ("replace", (
                    f'TShowroomMissileCarriageSubDepictionMissileInfo'
                    f'('
                    f'    Depiction = TemplateDepictionMissileShowroom'
                    f'    ('
                    f'        ProjectileModelResource = $/GFX/DepictionResources/Modele_Missile_FAB_250'
                    f'    )'
                    f'    MissileCount = 16'
                    f'    WeaponIndex = 2'
                    f')'
                )),
            },
        },
    },
}
# fmt: on
