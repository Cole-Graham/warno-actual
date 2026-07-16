"""Tornado_Marine_CLU_RFA depiction edits."""

from typing import Dict, Tuple, Union

# fmt: off
tornado_marine_clu_rfa: Dict[str, Dict[Union[str, Tuple[str, str]], dict]] = {
    "unit_name": "Tornado_Marine_CLU_RFA",
    "valid_files": ["MissileCarriage.ndf", "MissileCarriageDepiction.ndf"],
    "MissileCarriage_ndf": {
        ("MissileCarriage_Tornado_Marine_CLU_RFA", "TMissileCarriageConnoisseur"): { # (Namespace, Object type)
            "WeaponInfos": {
                1: ("edit", {
                    "MissileCount": 4,
                }),
            },
        },
    },

    "MissileCarriageDepiction_ndf": {
        ("SubGenerators_Tornado_Marine_CLU_RFA", "TStaticMissileCarriageSubDepictionGenerator"): {
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
        ("SubGenerators_Showroom_Tornado_Marine_CLU_RFA", "TShowroomMissileCarriageSubDepictionGenerator"): {
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
