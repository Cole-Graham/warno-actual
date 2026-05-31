"""LAV_L_US depiction edits."""

from typing import Dict, Tuple, Union

# fmt: off
lav_l_us: Dict[str, Dict[Union[str, Tuple[str, str]], dict]] = {
    "unit_name": "LAV_L_US",
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
