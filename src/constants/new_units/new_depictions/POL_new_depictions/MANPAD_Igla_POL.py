"""MANPAD_Igla_POL depiction edits (auto-generated draft)."""

from typing import Dict, Tuple, Union

# fmt: off
manpad_igla_pol: Dict[str, Dict[Union[str, Tuple[str, str]], dict]] = {
    "unit_name": "MANPAD_Igla_POL",
    "valid_files": ["DepictionInfantry.ndf"],
    "DepictionInfantry_ndf": {
        
        ("AllWeaponAlternatives_MANPAD_Igla_POL", None): {
            1: ("edit", [("MeshDescriptor", "MANPAD_igla")]),
        },
        
        ("AllWeaponSubDepiction_MANPAD_Igla_POL", "TemplateAllSubWeaponDepiction"): {
            "Operators": {
                1: ("edit", [("FireEffectTag", "MANPAD_igla")]),
            },
        },
    },
}
# fmt: on
