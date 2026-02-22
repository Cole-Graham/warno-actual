"""Bedford_MJ_4t_UK depiction edits."""

from typing import Dict, Tuple, Union

# fmt: off
bedford_mj_4t_uk: Dict[str, Dict[Union[str, Tuple[str, str]], dict]] = {
    "unit_name": "Bedford_MJ_4t_UK",
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
