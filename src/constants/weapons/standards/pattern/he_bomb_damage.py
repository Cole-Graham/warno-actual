"""HE bomb damage standards (by weight class) and name substring matching for Ammunition.ndf."""

from typing import Dict, List

HE_BOMB_DAMAGE_BY_WEIGHT: Dict[str, Dict[str, int]] = {
    "he_100kg": {
        "PhysicalDamages": 5,
        "RadiusSplashPhysicalDamagesGRU": 58,
        "RadiusSplashSuppressDamagesGRU": 77,
    },
    "he_250kg": {
        "PhysicalDamages": 10,
        "RadiusSplashPhysicalDamagesGRU": 110,
        "RadiusSplashSuppressDamagesGRU": 147,
    },
    "he_500kg": {
        "PhysicalDamages": 15,
        "RadiusSplashPhysicalDamagesGRU": 150,
        "RadiusSplashSuppressDamagesGRU": 200,
    },
    "he_1000kg": {
        "PhysicalDamages": 20,
        "SuppressDamages": 750,
        "RadiusSplashPhysicalDamagesGRU": 170,
        "RadiusSplashSuppressDamagesGRU": 225,
    },
    "he_1250kg": {
        "PhysicalDamages": 25,
        "SuppressDamages": 990,
        "RadiusSplashPhysicalDamagesGRU": 200,
        "RadiusSplashSuppressDamagesGRU": 265,
    },
}

# TraitsToken: For matching HE bombs in Ammunition.ndf (and AmmunitionMissiles.ndf for PGBs)
HE_BOMB_TRAIT_TOKENS: List[str] = [
    "'HE'",
]

# Weight class key -> substrings matched against ammo namespace (see apply_bomb_damage_standards)
HE_BOMB_NAME_MATCH: Dict[str, List[str]] = {
    "100": ["119kg"],
    "250": ["250kg", "GBU_12"],
    "500": ["_500Kr", "_500L", "400kg", "450kg", "500kg", "513kg", "CPU_123"],
    "1000": ["920kg", "1000kg", "GBU_10", "GBU_27"],
    "1250": ["KAB_1500"],
}
