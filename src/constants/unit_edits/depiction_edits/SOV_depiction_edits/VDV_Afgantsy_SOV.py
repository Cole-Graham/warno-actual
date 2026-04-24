"""VDV_Afgantsy_SOV depiction edits (auto-generated draft)."""

from typing import Dict, Tuple, Union

# fmt: off
vdv_afgantsy_sov: Dict[str, Dict[Union[str, Tuple[str, str]], dict]] = {
    "unit_name": "VDV_Afgantsy_SOV",
    "valid_files": ["DepictionInfantry.ndf"],
    "DepictionInfantry_ndf": {
        
        ("AllWeaponAlternatives_VDV_Afgantsy_SOV", None): {
            1: ("edit", [("MeshDescriptor", "PKM")]),
        },
        
        ("AllWeaponSubDepiction_VDV_Afgantsy_SOV", "TemplateAllSubWeaponDepiction"): {
            "Operators": {
                1: ("edit", [("FireEffectTag", "MMG_PKM_7_62mm")]),
            },
        },
        
        ("TacticDepiction_VDV_Afgantsy_SOV_Soldier", "TemplateInfantryDepictionFactoryTactic"): {
            "Operators": {
                0: ("insert", [("mmg", "WeaponAlternative_2")]),
            },
        },
    },
}
# fmt: on
