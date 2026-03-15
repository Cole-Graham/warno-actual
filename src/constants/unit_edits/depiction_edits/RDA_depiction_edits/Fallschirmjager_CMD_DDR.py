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
            2: ("edit", [("SelectorId", "WeaponAlternative_3"), ("MeshDescriptor", "RPG18")]),
            3: ("edit", [("SelectorId", "WeaponAlternative_4"), ("MeshDescriptor", "MainNue")]),
        },

        ("AllWeaponSubDepiction_Fallschirmjager_CMD_DDR", "TemplateAllSubWeaponDepiction"): {
            "Operators": {
                1: ("insert", [("FireEffectTag", "SAW_lMG_K_7_62mm"), ("WeaponShootDataPropertyName", "WeaponShootData_0_2")]),
                2: ("edit", [("FireEffectTag", "RocketInf_RPG18_64mm"), ("WeaponShootDataPropertyName", "WeaponShootData_0_3")]),
                3: ("edit", [("FireEffectTag", "Grenade_SMOKE"), ("WeaponShootDataPropertyName", "WeaponShootData_0_4")]),
            },
        },

        ("TacticDepiction_Fallschirmjager_CMD_DDR_Soldier", "TemplateInfantryDepictionFactoryTactic"): {
            "Operators": { # usually (always?) editing conditional tags submember
                0: ("edit", [("bazooka", "WeaponAlternative_3")]),
                1: ("edit", [("grenade", "WeaponAlternative_4")]),
            },
        },
    },
}
# fmt: on