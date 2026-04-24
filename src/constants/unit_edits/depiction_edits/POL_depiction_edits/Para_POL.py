"""Para_POL depiction edits (auto-generated draft)."""

from typing import Dict, Tuple, Union

# fmt: off
para_pol: Dict[str, Dict[Union[str, Tuple[str, str]], dict]] = {
    "unit_name": "Para_POL",
    "valid_files": ["DepictionInfantry.ndf"],
    "DepictionInfantry_ndf": {
        
        ("AllWeaponAlternatives_Para_POL", None): {
            0: ("edit", [("MeshDescriptor", "Wz88_Tantal")]),
            1: ("edit", [("MeshDescriptor", "RPK74")]),
            3: ("edit", [("MeshDescriptor", "RPG7V")]),
        },
        
        ("AllWeaponSubDepiction_Para_POL", "TemplateAllSubWeaponDepiction"): {
            "Operators": {
                1: ("edit", [("FireEffectTag", "SAW_RPK_74_5_56mm")]),
                3: ("edit", [("FireEffectTag", "RocketInf_RPG7VL")]),
            },
        },
    },
}
# fmt: on
