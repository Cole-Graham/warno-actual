"""Sniper_Geb_RFA depiction edits."""

from typing import Dict, Tuple, Union

# fmt: off
sniper_geb_rfa: Dict[str, Dict[Union[str, Tuple[str, str]], dict]] = {
    "unit_name": "Sniper_Geb_RFA",
    "valid_files": ["DepictionInfantry.ndf"],
    "DepictionInfantry_ndf": {
        # Vanilla: 0 G3A3ZF/WA_1, 1 G3A3ZF/WA_2, 2 meshless
        # Target: one G3A3ZF on WA_1 (Sniper_G3A3ZF_double, NbWeapons 2)
        ("AllWeaponAlternatives_Sniper_Geb_RFA", None): {
            1: ("remove", []),
        },

        ("AllWeaponSubDepiction_Sniper_Geb_RFA", "TemplateAllSubWeaponDepiction"): {
            "Operators": {
                1: ("remove", []),
            },
        },
    }
}
# fmt: on
