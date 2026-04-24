"""MANPAD_Igla_Para_POL depiction edits (auto-generated draft)."""

from typing import Dict, Tuple, Union

# fmt: off
manpad_igla_para_pol: Dict[str, Dict[Union[str, Tuple[str, str]], dict]] = {
    "unit_name": "MANPAD_Igla_Para_POL",
    "valid_files": ["DepictionInfantry.ndf"],
    "DepictionInfantry_ndf": {
        
        ("AllWeaponAlternatives_MANPAD_Igla_Para_POL", None): {
            0: ("edit", [("MeshDescriptor", "AK74")]),
            1: ("edit", [("MeshDescriptor", "MANPAD_igla")]),
        },
        
        ("AllWeaponSubDepiction_MANPAD_Igla_Para_POL", "TemplateAllSubWeaponDepiction"): {
            "Operators": {
                1: ("edit", [("FireEffectTag", "MANPAD_igla")]),
            },
        },
    },
}
# fmt: on
