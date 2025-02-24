"""F4E_Phantom_II_napalm_US depiction edits."""

from typing import Dict, Tuple, Union

# fmt: off
f4e_phantom_ii_napalm_us: Dict[str, Dict[Union[str, Tuple[str, str]], dict]] = {
    "unit_name": "F4E_Phantom_II_napalm_US",
    "valid_files": ["MissileCarriage.ndf", "MissileCarriageDepiction.ndf"],
    "MissileCarriage_ndf": {
        ("MissileCarriage_F4E_Phantom_II_napalm_US", "TMissileCarriageConnoisseur"): { # (Namespace, Object type)
            "WeaponInfos": {
                0: {
                    "Count": 5,
                },
            },
        },
        ("MissileCarriage_F4E_Phantom_II_napalm_US_Showroom", "TMissileCarriageConnoisseur"): {
            "WeaponInfos": {
                0: {
                    "Count": 5,
                },
            },
        },
    },
    
    "MissileCarriageDepiction_ndf": {
        ("SubGenerators_F4E_Phantom_II_napalm_US", "TStaticMissileCarriageSubDepictionGenerator"): {
            "Missiles": {
                0: ("replace", (
                    f'TStaticMissileCarriageSubDepictionMissileInfo'
                    f'('
                    f'    Depiction = TemplateDepictionStaticMissiles'
                    f'    ('
                    f'        PhysicalProperty = "Tourelle2_MissileCount"'
                    f'        ProjectileModelResource = $/GFX/DepictionResources/Modele_Missile_Mk_77'
                    f'    )'
                    f'    MissileCount = 5'
                    f'    WeaponIndex = 2'
                    f')'
                )),
            },
        },
        ("SubGenerators_Showroom_F4E_Phantom_II_napalm_US", "TStaticMissileCarriageSubDepictionGenerator"): {
            "Missiles": {
                0: ("replace", (
                    f'TStaticMissileCarriageSubDepictionMissileInfo'
                    f'('
                    f'    Depiction = TemplateDepictionMissileShowroom'
                    f'    ('
                    f'        ProjectileModelResource = $/GFX/DepictionResources/Modele_Missile_Mk_77'
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
