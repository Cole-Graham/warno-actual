"""MotRifles_RPG7V_TTsko_SOV depiction edits."""

from typing import Dict, Tuple, Union

# fmt: off
motrifles_rpg7v_ttsko_sov: Dict[str, Dict[Union[str, Tuple[str, str]], dict]] = {
    "unit_name": "MotRifles_RPG7V_TTsko_SOV",
    "valid_files": ["DepictionInfantry.ndf"],
    "DepictionInfantry_ndf": {
        ("AllWeaponAlternatives_MotRifles_RPG7V_TTsko_SOV", None): { # (namespace, object type)
            # row: (edit type, [(property, value), (property, value), ...]) (edit types: "edit", "add", "remove", "replace")
            2: ("edit", [("MeshDescriptor", "RPG7V")]), # (selector_id or mesh)
            3: ("edit", [("ReferenceMeshForSkeleton", "RPG7V")]),
        },
    },
}
# fmt: on
