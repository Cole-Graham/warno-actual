"""fire weapon definitions."""

from typing import Dict, List, Optional, Tuple, Union

WeaponData = Dict[str, Union[Dict, List, int, float, str]]
WeaponKey = Tuple[str, str, Optional[str], bool]  # (weapon, category, donor, is_new)

# fmt: off
weapons: Dict[WeaponKey, WeaponData] = {
    ("Degats_napalm_leger", "fire", None, False): {
        "Ammunition": {
            "parent_membr": {
                "RadiusSplashPhysicalDamagesGRU": 80,
                "RadiusSplashSuppressDamagesGRU": 80,
            },
        },
    },
    
    ("Degats_napalm_leger_53m", "fire", "Degats_napalm_leger", True): {
        "Ammunition": {
            "parent_membr": {
                "RadiusSplashPhysicalDamagesGRU": 53,
                "RadiusSplashSuppressDamagesGRU": 53,
            },
        },
    },
}
# fmt: on
