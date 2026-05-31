"""Bedford_TM_6x6_supply_UK depiction edits."""

from typing import Dict, Tuple, Union

# fmt: off
bedford_tm_6x6_supply_uk: Dict[str, Dict[Union[str, Tuple[str, str]], dict]] = {
    "unit_name": "Bedford_TM_6x6_supply_UK",
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
