"""Scout_FJ_DDR depiction edits."""

from typing import Dict, Tuple, Union

# fmt: off
scout_fj_ddr: Dict[str, Dict[Union[str, Tuple[str, str]], dict]] = {
    "unit_name": "Scout_FJ_DDR",
    "valid_files": ["DepictionInfantry.ndf", "WeaponDescriptor.ndf"],
    "DepictionInfantry_ndf": {
        ("AllWeaponAlternatives_Scout_FJ_DDR", None): { # (namespace, object type)
            # row: (edit type, [(property, value), (property, value), ...]) (edit types: "edit", "add", "remove", "replace")
            3: ("edit", [("MeshDescriptor", "RPG7V")]),
            4: ("edit", [("ReferenceMeshForSkeleton", "RPG7V")]),
        },

        ("AllWeaponSubDepiction_Scout_FJ_DDR", "TemplateAllSubWeaponDepiction"): {
            "Operators": {
                3: ("edit", [("FireEffectTag", "RocketInf_RPG7VL")]),
            },
        },
    },
}
# fmt: on