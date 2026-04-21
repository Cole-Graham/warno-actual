"""Fallschirmjager_DDR depiction edits (auto-generated draft)."""

from typing import Dict, Tuple, Union

# fmt: off
fallschirmjager_ddr: Dict[str, Dict[Union[str, Tuple[str, str]], dict]] = {
    "unit_name": "Fallschirmjager_DDR",
    "valid_files": ["DepictionInfantry.ndf"],
    "DepictionInfantry_ndf": {
        
        ("AllWeaponAlternatives_Fallschirmjager_DDR", None): {
            0: ("edit", [("MeshDescriptor", "AKs74U")]),
        },
        
        ("AllWeaponSubDepiction_Fallschirmjager_DDR", "TemplateAllSubWeaponDepiction"): {
            "Operators": {
                0: ("edit", [("FireEffectTag", "PM_MPi_AKSU_74NK")]),
            },
        },
        
        ("TacticDepiction_Fallschirmjager_DDR_Soldier", "TemplateInfantryDepictionFactoryTactic"): {
            "Operators": {
                0: ("insert", [("smg", "WeaponAlternative_1")]),
            },
        },
    },
}
# fmt: on
