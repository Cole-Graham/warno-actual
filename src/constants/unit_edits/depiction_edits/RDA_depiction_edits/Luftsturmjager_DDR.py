"""Luftsturmjager_DDR depiction edits."""

from typing import Dict, Tuple, Union

# fmt: off
luftsturmjager_ddr: Dict[str, Dict[Union[str, Tuple[str, str]], dict]] = {
    "unit_name": "Luftsturmjager_DDR",
    "valid_files": ["DepictionInfantry.ndf", "WeaponDescriptor.ndf"],
    "DepictionInfantry_ndf": {
        ("AllWeaponAlternatives_Luftsturmjager_DDR", None): { # (namespace, object type)
            # row: (edit type, [(property, value), (property, value), ...]) (edit types: "edit", "add", "remove", "replace")
            2: ("insert", [("SelectorId", "WeaponAlternative_3"), ("MeshDescriptor", "PKM")]),
            3: ("edit", [("SelectorId", "WeaponAlternative_4"), ("MeshDescriptor", "RPG7V")]),
        },

        ("AllWeaponSubDepiction_Luftsturmjager_DDR", "TemplateAllSubWeaponDepiction"): {
            "Operators": {
                2: ("insert", [("FireEffectTag", "MMG_PKM_7_62mm"), ("WeaponShootDataPropertyName", "WeaponShootData_0_3")]),
                3: ("edit", [("FireEffectTag", "RocketInf_RPG7VL"), ("WeaponShootDataPropertyName", "WeaponShootData_0_3")]),
            },
        },
    },
}
# fmt: on