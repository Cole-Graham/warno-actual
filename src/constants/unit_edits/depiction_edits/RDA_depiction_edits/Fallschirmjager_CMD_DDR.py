"""Fallschirmjager_CMD_DDR depiction edits."""

from typing import Dict, Tuple, Union

# fmt: off
fallschirmjager_cmd_ddr: Dict[str, Dict[Union[str, Tuple[str, str]], dict]] = {
    "unit_name": "Fallschirmjager_CMD_DDR",
    "valid_files": ["DepictionInfantry.ndf", "WeaponDescriptor.ndf"],
    "DepictionInfantry_ndf": {
        ("AllWeaponAlternatives_Fallschirmjager_CMD_DDR", None): { # (namespace, object type)
            # row: (edit type, [(property, value), (property, value), ...]) (edit types: "edit", "add", "remove", "replace")
            1: ("insert", [("SelectorId", "WeaponAlternative_2"), ("MeshDescriptor", "RPK")]),
        },

        ("AllWeaponSubDepiction_Fallschirmjager_CMD_DDR", "TemplateAllSubWeaponDepiction"): {
            "Operators": {
                1: ("insert", [("FireEffectTag", "SAW_lMG_K_7_62mm")]),
            },
        },
    },
}
# fmt: on