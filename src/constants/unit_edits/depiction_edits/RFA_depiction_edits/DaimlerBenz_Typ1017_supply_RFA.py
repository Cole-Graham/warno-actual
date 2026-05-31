"""DaimlerBenz_Typ1017_supply_RFA depiction edits."""

from typing import Dict, Tuple, Union

# fmt: off
daimlerbenz_typ1017_supply_rfa: Dict[str, Dict[Union[str, Tuple[str, str]], dict]] = {
    "unit_name": "DaimlerBenz_Typ1017_supply_RFA",
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
