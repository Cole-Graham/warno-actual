"""Gebirgsjager_JagdKdo_RFA depiction edits."""

from typing import Dict, Tuple, Union

# fmt: off
gebirgsjager_jagdkdo_rfa: Dict[str, Dict[Union[str, Tuple[str, str]], dict]] = {
    "unit_name": "Gebirgsjager_JagdKdo_RFA",
    "valid_files": ["DepictionInfantry.ndf"],
    "DepictionInfantry_ndf": {
        # Vanilla: 0 G3/WA_1, 1 G3A3ZF/WA_2, 2 MG3/WA_3, 3 MainNue/WA_4
        # Target: drop sniper only; MG3/WA_3 and satchel/WA_4 keep their ids
        ("AllWeaponAlternatives_Gebirgsjager_JagdKdo_RFA", None): {
            1: ("remove", []),
        },

        ("AllWeaponSubDepiction_Gebirgsjager_JagdKdo_RFA", "TemplateAllSubWeaponDepiction"): {
            "Operators": {
                1: ("remove", []),
            },
        },
        # ConditionalTags already [mmg/WA_3, grenade/WA_4] — no TacticDepiction change
    }
}
# fmt: on
