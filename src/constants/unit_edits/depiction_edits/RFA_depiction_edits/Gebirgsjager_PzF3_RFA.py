"""Gebirgsjager_PzF3_RFA depiction edits."""

from typing import Dict, Tuple, Union

# fmt: off
gebirgsjager_pzf3_rfa: Dict[str, Dict[Union[str, Tuple[str, str]], dict]] = {
    "unit_name": "Gebirgsjager_PzF3_RFA",
    "valid_files": ["DepictionInfantry.ndf", "WeaponDescriptor.ndf"],
    "DepictionInfantry_ndf": {
        ("AllWeaponAlternatives_Gebirgsjager_PzF3_RFA", None): { # (namespace, object type)
            # row: (edit type, [(property, value), (property, value), ...]) (edit types: "edit", "insert", "remove")
            # always insert and/or remove first, then define the rest based on adjusted indices
            1: ("remove", []), # This does not seem to work
        },

        ("AllWeaponSubDepiction_Gebirgsjager_PzF3_RFA", "TemplateAllSubWeaponDepiction"): {
            "Operators": {
                1: ("remove", []), # This does not seem to work
            },
        },
    }
}
# fmt: on
