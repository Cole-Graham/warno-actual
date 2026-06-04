"""Pattern standard: HOBS missiles on units without helmet-mounted display (_hmd)."""

from typing import TypedDict


class HobsNoHmdTurretAngles(TypedDict):
    AngleRotationMax: str
    AngleRotationMaxPitch: str
    AngleRotationMinPitch: str


class HobsNoHmdMissileRule(TypedDict):
    """Per-missile rule: swap HOBS base ammo to NoOBS and narrow turret arcs."""

    hobs_base: str
    no_obs_base: str
    hagru_base: str
    no_obs_hagru_base: str
    turret_angles: HobsNoHmdTurretAngles


class HobsNoHmdPatternStandard(TypedDict):
    hmd_trait: str
    missile_rules: tuple[HobsNoHmdMissileRule, ...]


_R73_NO_HMD_TURRET_ANGLES: HobsNoHmdTurretAngles = {
    "AngleRotationMax": "1.3962634015954636",
    "AngleRotationMaxPitch": "0.5235987755982988",
    "AngleRotationMinPitch": "-0.5235987755982988",
}

HOBS_NO_HMD_PATTERN_STANDARD: HobsNoHmdPatternStandard = {
    "hmd_trait": "_hmd",
    "missile_rules": (
        {
            "hobs_base": "AA_R73_Vympel",
            "no_obs_base": "AA_R73_Vympel_NoOBS",
            "hagru_base": "AA_R73_Vympel_HAGRU",
            "no_obs_hagru_base": "AA_R73_Vympel_NoOBS_HAGRU",
            "turret_angles": _R73_NO_HMD_TURRET_ANGLES,
        },
    ),
}
