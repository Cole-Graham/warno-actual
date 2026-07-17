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
from .commander_capacite import (
    CMD_UNIT_CAPACITY_NAME,
    CMD_UNIT_TAG,
    COMMANDER_CAPACITE_PATTERN_STANDARD,
    INFANTERIE_TAG,
    LDR_INF_CAPACITY_NAME,
    LDR_SPECIALTIES,
    LDR_UNIT_TAGS,
    CommanderCapacitePatternStandard,
    resolve_commander_capacite_name,
)
from .infantry_armor import (
    EXCLUDED_AT_TEAM_TAG,
    EXCLUDED_WEAPON_TEAM_PREFIXES,
    INFANTRY_ARMOR_PATTERN_STANDARD,
    INFANTRY_WA_ARMOR_FAMILY,
    REWRITABLE_INFANTRY_ARMOR_FAMILIES,
    VANILLA_INFANTRY_ARMOR_FAMILY,
    InfantryArmorPatternStandard,
    infantry_wa_armor_index,
    is_excluded_hmg_team_unit,
    is_excluded_weapon_team_unit,
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
    "CMD_UNIT_CAPACITY_NAME",
    "CMD_UNIT_TAG",
    "COMMANDER_CAPACITE_PATTERN_STANDARD",
    "CommanderCapacitePatternStandard",
    "EXCLUDED_AT_TEAM_TAG",
    "EXCLUDED_WEAPON_TEAM_PREFIXES",
    "INFANTERIE_TAG",
    "INFANTRY_ARMOR_PATTERN_STANDARD",
    "INFANTRY_WA_ARMOR_FAMILY",
    "InfantryArmorPatternStandard",
    "LDR_INF_CAPACITY_NAME",
    "LDR_SPECIALTIES",
    "LDR_UNIT_TAGS",
    "REWRITABLE_INFANTRY_ARMOR_FAMILIES",
    "VANILLA_INFANTRY_ARMOR_FAMILY",
    "infantry_wa_armor_index",
    "is_excluded_hmg_team_unit",
    "is_excluded_weapon_team_unit",
    "resolve_commander_capacite_name",
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
