"""Para_Metis_POL depiction edits (auto-generated draft)."""

from typing import Dict, Tuple, Union

# fmt: off
para_metis_pol: Dict[str, Dict[Union[str, Tuple[str, str]], dict]] = {
    "unit_name": "Para_Metis_POL",
    "valid_files": ["DepictionInfantry.ndf"],
    "DepictionInfantry_ndf": {
        
        ("AllWeaponAlternatives_Para_Metis_POL", None): {
            0: ("edit", [("MeshDescriptor", "Wz88_Tantal")]),
            1: ("edit", [("MeshDescriptor", "RPK74")]),
        },
        
        ("AllWeaponSubDepiction_Para_Metis_POL", "TemplateAllSubWeaponDepiction"): {
            "Operators": {
                1: ("edit", [("FireEffectTag", "SAW_RPK_74_5_56mm")]),
            },
        },
    },
}
# fmt: on
