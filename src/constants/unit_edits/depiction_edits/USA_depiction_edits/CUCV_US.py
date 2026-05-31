"""CUCV_US depiction edits."""

from typing import Dict, Tuple, Union

# fmt: off
cucv_us: Dict[str, Dict[Union[str, Tuple[str, str]], dict]] = {
    "unit_name": "CUCV_US",
    "valid_files": ["DepictionVehicles.ndf"],
    "DepictionVehicles_ndf": {
        (None, "TacticVehicleDepictionRegistration"): {
            "SubDepictionGenerators": {
                "TowedUnitSubDepictionGenerator": {
                    "add": None,
                },
            },
        },
    },
}
# fmt: on
