"""MAN_Kat_6x6_RFA depiction edits."""

from typing import Dict, Tuple, Union

# fmt: off
man_kat_6x6_rfa: Dict[str, Dict[Union[str, Tuple[str, str]], dict]] = {
    "unit_name": "MAN_Kat_6x6_RFA",
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
