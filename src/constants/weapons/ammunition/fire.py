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
    
    ("incendiary_magnesium_53m", "fire", "Degats_napalm_leger", True): {
        "Ammunition": {
            "parent_membr": {
                "RadiusSplashPhysicalDamagesGRU": 53,
                "RadiusSplashSuppressDamagesGRU": 53,
                "PhysicalDamages": 0.3,
                "SuppressDamages": 30,
            },
        },
    },
    
    ("Degats_napalm_bomb", "fire", "Degats_napalm_buratino", True): {
        "Ammunition": {
            "Arme": {
                "Family": "DamageFamily_nplm_bomb_flamme",
            },
        },
    },
}
# fmt: on
