"""MotRifles_BTR_SOV depiction edits (auto-generated draft)."""

from typing import Dict, Tuple, Union

# fmt: off
motrifles_btr_sov: Dict[str, Dict[Union[str, Tuple[str, str]], dict]] = {
    "unit_name": "MotRifles_BTR_SOV",
    "valid_files": ["DepictionInfantry.ndf"],
    "DepictionInfantry_ndf": {
        
        ("AllWeaponAlternatives_MotRifles_BTR_SOV", None): {
            1: ("edit", [("MeshDescriptor", "PKM")]),
        },
        
        ("AllWeaponSubDepiction_MotRifles_BTR_SOV", "TemplateAllSubWeaponDepiction"): {
            "Operators": {
                1: ("edit", [("FireEffectTag", "MMG_PKM_7_62mm")]),
            },
        },
        
        ("TacticDepiction_MotRifles_BTR_SOV_Soldier", "TemplateInfantryDepictionFactoryTactic"): {
            "Operators": {
                0: ("insert", [("mmg", "WeaponAlternative_2")]),
            },
        },
    },
}
# fmt: on
