"""AEC_Militant_UK depiction edits."""

from typing import Dict, Tuple, Union

# fmt: off
aec_militant_uk: Dict[str, Dict[Union[str, Tuple[str, str]], dict]] = {
    "unit_name": "AEC_Militant_UK",
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
