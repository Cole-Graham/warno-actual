"""Pattern standard: widen turret arcs on helicopter AA missile mounts."""

from typing import TypedDict


class HeloAaTurretAngles(TypedDict):
    AngleRotationMax: str
    AngleRotationMaxPitch: str
    AngleRotationMinPitch: str


class HeloAaTurretAnglesPatternStandard(TypedDict):
    ammo_bases: tuple[str, ...]
    turret_angles: HeloAaTurretAngles


HELO_AA_TURRET_ANGLES_PATTERN_STANDARD: HeloAaTurretAnglesPatternStandard = {
    "ammo_bases": (
        "AA_R60M_Vympel_helo",
        "AA_AIM9L_Sidewinder_Helo",
        "SAM_IglaV",
        "SAM_FIM92_Stinger_CS",
        "SAM_Strela2",
    ),
    "turret_angles": {
        "AngleRotationMax": "1.570796",
        "AngleRotationMaxPitch": "1.570796",
        "AngleRotationMinPitch": "-1.570796",
    },
}
