"""Rifles_Gurkhas_CMD_UK depiction edits (auto-generated draft)."""

from typing import Dict, Tuple, Union

# fmt: off
rifles_gurkhas_cmd_uk: Dict[str, Dict[Union[str, Tuple[str, str]], dict]] = {
    "unit_name": "Rifles_Gurkhas_CMD_UK",
    "valid_files": ["DepictionInfantry.ndf"],
    "DepictionInfantry_ndf": {
        
        ("AllWeaponAlternatives_Rifles_Gurkhas_CMD_UK", None): {
            1: ("edit", [("MeshDescriptor", "L86A1_LSW")]),
        },
        
        ("AllWeaponSubDepiction_Rifles_Gurkhas_CMD_UK", "TemplateAllSubWeaponDepiction"): {
            "Operators": {
                1: ("edit", [("FireEffectTag", "SAW_L86A1_5_56mm")]),
            },
        },
        
        ("TacticDepiction_Rifles_Gurkhas_CMD_UK_Soldier", "TemplateInfantryDepictionFactoryTactic"): {
            "Operators": {
                0: ("remove", []),
            }
        },
    },
}
# fmt: on
