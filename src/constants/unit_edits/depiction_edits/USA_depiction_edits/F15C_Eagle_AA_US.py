"""F15C_Eagle_AA_US depiction edits."""

from typing import Dict, Tuple, Union

# fmt: off
f15c_eagle_aa_us: Dict[str, Dict[Union[str, Tuple[str, str]], dict]] = {
    "unit_name": "F15C_Eagle_AA_US",
    "valid_files": ["MissileCarriage.ndf", "MissileCarriageDepiction.ndf"],
    "MissileCarriage_ndf": {
        ("MissileCarriage_F15C_Eagle_AA_US", "TMissileCarriageConnoisseur"): { # (Namespace, Object type)
            "WeaponInfos": {
                1: ("edit", {
                    "MissileCount": 4,
                }),
            },
        },
    },
    
    "MissileCarriageDepiction_ndf": {
        ("SubGenerators_F15C_Eagle_AA_US", "TStaticMissileCarriageSubDepictionGenerator"): {
            "Missiles": {
                1: ("replace", (
                    f'TStaticMissileCarriageSubDepictionMissileInfo'
                    f'('
                    f'    Depiction = TemplateDepictionStaticMissiles'
                    f'    ('
                    f'        PhysicalProperty = "Tourelle3_MissileCount"'
                    f'        ProjectileModelResource = $/GFX/DepictionResources/Modele_Missile_SideWinder'
                    f'    )'
                    f'    MissileCount = 4'
                    f'    WeaponIndex = 3'
                    f')'
                )),
            },
        },
        ("SubGenerators_Showroom_F15C_Eagle_AA_US", "TShowroomMissileCarriageSubDepictionGenerator"): {
            "Missiles": {
                1: ("replace", (
                    f'TShowroomMissileCarriageSubDepictionMissileInfo'
                    f'('
                    f'    Depiction = TemplateDepictionMissileShowroom'
                    f'    ('
                    f'        ProjectileModelResource = $/GFX/DepictionResources/Modele_Missile_SideWinder'
                    f'    )'
                    f'    MissileCount = 4'
                    f'    WeaponIndex = 3'
                    f')'
                )),
            },
        },
    },
}
# fmt: on
