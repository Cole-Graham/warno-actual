"""Pattern standards for unit and weapon-descriptor batch handlers."""

from .helicopter_movement import (
    HELICOPTER_MOVEMENT_MANOEUVRABILITY_PATTERN_STANDARD,
    HelicopterMovementManoeuvrabilityPatternStandard,
)
from .atgm_infantry_team_strength import (
    ATGM_INFANTRY_TEAM_STRENGTH_PATTERN_STANDARD,
    ATGM_TYPE_CATEGORY_TOKEN,
    VERYHEAVY_EQUIP_SPECIALTY,
    AtgmInfantryTeamStrengthPatternStandard,
)
from .air_rocket_platform import (
    AIR_ROCKET_DAMAGE_FAMILY,
    AIR_ROCKET_PLATFORM_PAIRS,
    AirRocketPlatformPair,
    build_air_rocket_platform_maps,
)
from .artillery_deployment import (
    ARTILLERY_DEPLOYMENT_CALIBER_THRESHOLD_GRU,
    ARTILLERY_DEPLOYMENT_PHYSICAL_THRESHOLD,
    ARTILLERY_DEPLOYMENT_TIME_LARGE,
    ARTILLERY_DEPLOYMENT_TIME_SMALL,
    ARTILLERY_PACKUP_TIME,
)
from .helo_aa_turret_angles import (
    HELO_AA_TURRET_ANGLES_PATTERN_STANDARD,
    HeloAaTurretAngles,
    HeloAaTurretAnglesPatternStandard,
)
from .hobs_no_hmd import (
    HOBS_NO_HMD_PATTERN_STANDARD,
    HobsNoHmdMissileRule,
    HobsNoHmdPatternStandard,
    HobsNoHmdTurretAngles,
)

__all__ = [
    "AIR_ROCKET_DAMAGE_FAMILY",
    "AIR_ROCKET_PLATFORM_PAIRS",
    "AirRocketPlatformPair",
    "build_air_rocket_platform_maps",
    "ARTILLERY_DEPLOYMENT_CALIBER_THRESHOLD_GRU",
    "ARTILLERY_DEPLOYMENT_PHYSICAL_THRESHOLD",
    "ARTILLERY_DEPLOYMENT_TIME_LARGE",
    "ARTILLERY_DEPLOYMENT_TIME_SMALL",
    "ARTILLERY_PACKUP_TIME",
    "ATGM_INFANTRY_TEAM_STRENGTH_PATTERN_STANDARD",
    "ATGM_TYPE_CATEGORY_TOKEN",
    "AtgmInfantryTeamStrengthPatternStandard",
    "HELICOPTER_MOVEMENT_MANOEUVRABILITY_PATTERN_STANDARD",
    "HelicopterMovementManoeuvrabilityPatternStandard",
    "HELO_AA_TURRET_ANGLES_PATTERN_STANDARD",
    "HeloAaTurretAngles",
    "HeloAaTurretAnglesPatternStandard",
    "HOBS_NO_HMD_PATTERN_STANDARD",
    "HobsNoHmdMissileRule",
    "HobsNoHmdPatternStandard",
    "HobsNoHmdTurretAngles",
    "VERYHEAVY_EQUIP_SPECIALTY",
]
