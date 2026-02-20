"""Commandos_Para_CMD_POL depiction edits."""

from typing import Dict, Tuple, Union

# fmt: off
commandos_para_cmd_pol: Dict[str, Dict[Union[str, Tuple[str, str]], dict]] = {
    "unit_name": "Commandos_Para_CMD_POL",
    "valid_files": ["DepictionInfantry.ndf", "WeaponDescriptor.ndf"],
    "DepictionInfantry_ndf": {
        ("AllWeaponAlternatives_Commandos_Para_CMD_POL", None): { # (namespace, object type)
            # row: (edit type, [(property, value), (property, value), ...]) (edit types: "edit", "add", "remove", "replace")
            0: ("edit", [("MeshDescriptor", "PM63_RAK")]), # (selector_id or mesh)
            1: ("edit", [("MeshDescriptor", "MainNue")]), # (selector_id or mesh)
            2: ("edit", [("MeshDescriptor", "RPG76Komar")]),
        },

        ("AllWeaponSubDepiction_Commandos_Para_CMD_POL", "TemplateAllSubWeaponDepiction"): {
            "Operators": {
                0: ("edit", [("FireEffectTag", "PM_PM63_RAK")]),
                1: ("edit", [("FireEffectTag", "Grenade_Satchel_Charge")]),
                2: ("edit", [("FireEffectTag", "RocketInf_RPG76_Komar")]),
            },
        },

        ("TacticDepiction_Commandos_Para_CMD_POL_Soldier", "TemplateInfantryDepictionFactoryTactic"): {
            "Operators": { # usually (always?) editing conditional tags submember
                0: ("edit", [("smg", "WeaponAlternative_1")]),
                1: ("edit", [("grenade", "WeaponAlternative_2")]),
                2: ("insert", [("bazooka", "WeaponAlternative_3")]),
                3: ("insert", [("grenade", "WeaponAlternative_4")]),
            },
        },
    },
}
# fmt: on