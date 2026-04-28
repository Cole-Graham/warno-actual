"""Spetsnaz_Naval_SOV depiction edits.

Unit edit replaces ``RocketInf_RPO_A_93mm`` with ``RocketInf_RPO_RYS`` on the
naval Spetsnaz squad; mesh / fire effect must follow the new launcher.
"""

from typing import Dict, Tuple, Union

# fmt: off
spetsnaz_naval_sov: Dict[str, Dict[Union[str, Tuple[str, str]], dict]] = {
    "unit_name": "Spetsnaz_Naval_SOV",
    "valid_files": ["DepictionInfantry.ndf"],
    "DepictionInfantry_ndf": {
        ("AllWeaponAlternatives_Spetsnaz_Naval_SOV", None): {
            # Secondary handheld: RPO-A -> RPO RYS (if in-game layout differs, adjust index).
            2: ("edit", [("MeshDescriptor", "M72_LAW")]), # Vanilla game uses LAW placeholder model
            3: ("edit", [("ReferenceMeshForSkeleton", "M72_LAW")]),
        },
        ("AllWeaponSubDepiction_Spetsnaz_Naval_SOV", "TemplateAllSubWeaponDepiction"): {
            "Operators": {
                2: ("edit", [("FireEffectTag", "RocketInf_RPO_RYS")]),
            },
        },
    },
}
# fmt: on
