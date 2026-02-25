"""Fallschirmjager_FalseFlag_CMD_DDR depiction edits."""

from typing import Dict, Tuple, Union

# fmt: off
fallschirmjager_falseflag_cmd_ddr: Dict[str, Dict[Union[str, Tuple[str, str]], dict]] = {
    "unit_name": "Fallschirmjager_FalseFlag_CMD_DDR",
    "valid_files": ["DepictionInfantry.ndf", "WeaponDescriptor.ndf"],
    "DepictionInfantry_ndf": {
        ("AllWeaponAlternatives_Fallschirmjager_FalseFlag_CMD_DDR", None): { # (namespace, object type)
            # row: (edit type, [(property, value), (property, value), ...]) (edit types: "edit", "add", "remove", "replace")
            1: ("insert", [("SelectorId", "WeaponAlternative_2"),("MeshDescriptor", "M249")]),
            2: ("edit", [("SelectorId", "WeaponAlternative_3"),("MeshDescriptor", "M72A4")]), # (selector_id or mesh)
            3: ("insert", [("SelectorId", "WeaponAlternative_4"),("MeshDescriptor", "MainNue")]),
        },

        ("AllWeaponSubDepiction_Fallschirmjager_FalseFlag_CMD_DDR", "TemplateAllSubWeaponDepiction"): {
            "Operators": {
                1: ("insert", [("FireEffectTag", "SAW_M249_5_56mm")]),
                3: ("insert", [("FireEffectTag", "Grenade_SMOKE")]),
            },
        },

        ("TacticDepiction_Fallschirmjager_FalseFlag_CMD_DDR_Soldier", "TemplateInfantryDepictionFactoryTactic"): {
            "Operators": { # usually (always?) editing conditional tags submember
                0: ("edit", [("bazooka", "WeaponAlternative_3")]),
                1: ("insert", [("grenade", "WeaponAlternative_4")]),
            },
        },
    },
}
# fmt: on