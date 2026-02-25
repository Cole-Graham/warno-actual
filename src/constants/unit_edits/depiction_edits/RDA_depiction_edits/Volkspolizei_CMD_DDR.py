"""Volkspolizei_CMD_DDR depiction edits."""

from typing import Dict, Tuple, Union

# fmt: off
volkspolizei_cmd_ddr: Dict[str, Dict[Union[str, Tuple[str, str]], dict]] = {
    "unit_name": "Volkspolizei_CMD_DDR",
    "valid_files": ["DepictionInfantry.ndf", "WeaponDescriptor.ndf"],
    "DepictionInfantry_ndf": {
        ("AllWeaponAlternatives_Volkspolizei_CMD_DDR", None): { # (namespace, object type)
            # row: (edit type, [(property, value), (property, value), ...]) (edit types: "edit", "add", "remove", "replace")
            1: ("insert", [("SelectorId", "WeaponAlternative_2"),("MeshDescriptor", "RPG18")]), # (selector_id or mesh)
            2: ("insert", [("SelectorId", "WeaponAlternative_3"),("MeshDescriptor", "MainNue")]),
        },

        ("AllWeaponSubDepiction_Volkspolizei_CMD_DDR", "TemplateAllSubWeaponDepiction"): {
            "Operators": {
                1: ("insert", [("FireEffectTag", "RocketInf_RPG18_64mm")]),
                2: ("insert", [("FireEffectTag", "Grenade_SMOKE")]),
            },
        },

        ("TacticDepiction_Volkspolizei_CMD_DDR_Soldier", "TemplateInfantryDepictionFactoryTactic"): {
            "Operators": { # usually (always?) editing conditional tags submember
                2: ("insert", [("bazooka", "WeaponAlternative_2")]),
                3: ("insert", [("grenade", "WeaponAlternative_3")]),
            },
        },
    },
}
# fmt: on