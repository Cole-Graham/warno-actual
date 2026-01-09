"""MotRifles_BTR_TTsko_SOV depiction edits."""

from typing import Dict, Tuple, Union

# fmt: off
motrifles_btr_ttsko_sov: Dict[str, Dict[Union[str, Tuple[str, str]], dict]] = {
    "unit_name": "MotRifles_BTR_TTsko_SOV",
    "valid_files": ["DepictionInfantry.ndf", "WeaponDescriptor.ndf"],
    "DepictionInfantry_ndf": {
        
        ("AllWeaponAlternatives_MotRifles_BTR_TTsko_SOV", None): { # (namespace, object type)
            # row: (edit type, [(property, value), (property, value), ...]) (edit types: "edit", "add", "remove", "replace")
            1: ("edit", [("MeshDescriptor", "PKM")]), # (selector_id or mesh)
        },
    }
}
# fmt: on
