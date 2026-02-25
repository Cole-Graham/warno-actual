"""Luftsturmjager_Metis_DDR depiction edits."""

from typing import Dict, Tuple, Union

# fmt: off
luftsturmjager_metis_ddr: Dict[str, Dict[Union[str, Tuple[str, str]], dict]] = {
    "unit_name": "Luftsturmjager_Metis_DDR",
    "valid_files": ["DepictionInfantry.ndf", "WeaponDescriptor.ndf"],
    "DepictionInfantry_ndf": {
        ("AllWeaponAlternatives_Luftsturmjager_Metis_DDR", None): { # (namespace, object type)
            # row: (edit type, [(property, value), (property, value), ...]) (edit types: "edit", "add", "remove", "replace")
            1: ("insert", [("SelectorId", "WeaponAlternative_3"), ("MeshDescriptor", "PKM")]),
        },

        ("AllWeaponSubDepiction_Luftsturmjager_Metis_DDR", "TemplateAllSubWeaponDepiction"): {
            "Operators": {
                1: ("insert", [("FireEffectTag", "MMG_PKM_7_62mm")]),
            },
        },
    },
}
# fmt: on