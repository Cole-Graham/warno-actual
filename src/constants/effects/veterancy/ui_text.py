"""Ingame hint body strings built from level bonus constants."""

from __future__ import annotations

from src.constants.effects.veterancy._schema import LevelBonuses
from src.constants.effects.veterancy.levels import AVION_VET_REBALANCE_ENABLED, EXTRA_LEVEL_ENTRIES, PACK_LEVELS

TIER_COLORS: tuple[str, ...] = (
    "style1",
    "moral_color_bad_2",
    "styleGreen",
    "styleTurquoise",
)


def _tier_color(level_index: int) -> str:
    if level_index < len(TIER_COLORS):
        return TIER_COLORS[level_index]
    return TIER_COLORS[-1]


def pct_bonus(value: int) -> str:
    return f"+{value}%"


def pct_reduction(value: int) -> str:
    return f"-{value}%"


def recovery_plain(value: float) -> str:
    return f"{value:.1f}"


def recovery_colored(value: float) -> str:
    return f"{value:.1f}"


def _display_accuracy_pct(level: LevelBonuses) -> int:
    if level.accuracy_pct is not None:
        return level.accuracy_pct
    return level.precision_moving_pct  # type: ignore[return-value]


def _body_infantry_standard(level: LevelBonuses, level_index: int) -> str:
    if level_index == 0:
        recovery = recovery_plain(level.stress_recovery)  # type: ignore[arg-type]
        return (
            "#style1{- Accuracy: normal}"
            "\n#style1{- Aiming time: normal}"
            "\n#style1{- Reload time: normal}"
            "\n#style1{- Stress resistance: normal}"
            f"\n#style1{{- Stress recovery: {recovery} per second}}"
        )

    color = _tier_color(level_index)
    acc = pct_bonus(level.accuracy_pct)  # type: ignore[arg-type]
    aim = pct_reduction(level.aim_time_reduction_pct)  # type: ignore[arg-type]
    reload = pct_reduction(level.salvo_reload_reduction_pct)  # type: ignore[arg-type]
    stress = pct_bonus(level.stress_resistance_pct)  # type: ignore[arg-type]
    recovery = recovery_colored(level.stress_recovery)  # type: ignore[arg-type]
    return (
        f"#style1{{- Accuracy:}} #{color}{{{acc}}}"
        f"\n#style1{{- Aiming time:}} #{color}{{{aim}}}"
        f"\n#style1{{- Reload time:}} #{color}{{{reload}}}"
        f"\n#style1{{- Stress resistance:}} #{color}{{{stress}}}"
        f"\n#style1{{- Stress recovery:}} #{color}{{{recovery}}} #style1{{per second}}"
    )


def _body_sf_standard(level: LevelBonuses, level_index: int) -> str:
    if level_index == 0:
        recovery = recovery_plain(level.stress_recovery)  # type: ignore[arg-type]
        return (
            "#style1{- Movement speed: normal}"
            "\n#style1{- Accuracy: normal}"
            "\n#style1{- Aiming time: normal}"
            "\n#style1{- Reload Time: normal}"
            "\n#style1{- Stress resistance: normal}"
            "\n#style1{- Physical damage resistance: normal}"
            "\n#style1{- Stun damage resistance: normal}"
            f"\n#style1{{- Stress recovery: {recovery} per second}}"
        )

    color = _tier_color(level_index)
    movement_color = "styleGreen" if level_index == 1 else color
    speed = pct_bonus(level.movement_speed_pct)  # type: ignore[arg-type]
    acc = pct_bonus(level.accuracy_pct)  # type: ignore[arg-type]
    aim = pct_reduction(level.aim_time_reduction_pct)  # type: ignore[arg-type]
    reload = pct_reduction(level.salvo_reload_reduction_pct)  # type: ignore[arg-type]
    stress = pct_bonus(level.stress_resistance_pct)  # type: ignore[arg-type]
    physical = pct_bonus(level.physical_damage_reduction_pct)  # type: ignore[arg-type]
    stun = pct_bonus(level.stun_damage_reduction_pct)  # type: ignore[arg-type]
    recovery = recovery_colored(level.stress_recovery)  # type: ignore[arg-type]
    return (
        f"#style1{{- Movement speed:}} #{movement_color}{{{speed}}}"
        f"\n#style1{{- Accuracy:}} #{color}{{{acc}}}"
        f"\n#style1{{- Aiming time:}} #{color}{{{aim}}}"
        f"\n#style1{{- Reload time:}} #{color}{{{reload}}}"
        f"\n#style1{{- Stress resistance:}} #{color}{{{stress}}}"
        f"\n#style1{{- Physical damage resistance:}} #{color}{{{physical}}}"
        f"\n#style1{{- Stun damage resistance:}} #{color}{{{stun}}}"
        f"\n#style1{{- Stress recovery:}} #{color}{{{recovery}}} #style1{{per second}}"
    )


def _body_helico(level: LevelBonuses, level_index: int) -> str:
    if level_index == 0:
        recovery = recovery_plain(level.stress_recovery)  # type: ignore[arg-type]
        return (
            "#style1{- Precision: normal}"
            "\n#style1{- Aiming time: normal}"
            "\n#style1{- Stress resistance: normal}"
            f"\n#style1{{- Stress recovery: {recovery} per second}}"
        )

    color = _tier_color(level_index)

    if level_index == 1:
        aim = pct_reduction(level.aim_time_reduction_pct)  # type: ignore[arg-type]
        recovery = recovery_colored(level.stress_recovery)  # type: ignore[arg-type]
        return (
            "#style1{- Precision: normal}"
            f"\n#style1{{- Aiming time:}} #{color}{{{aim}}}"
            "\n#style1{- Stress resistance: normal}"
            f"\n#style1{{- Stress recovery:}} #{color}{{{recovery}}} #style1{{per second}}"
        )

    acc = pct_bonus(level.accuracy_pct)  # type: ignore[arg-type]
    aim = pct_reduction(level.aim_time_reduction_pct)  # type: ignore[arg-type]
    stress = pct_bonus(level.stress_resistance_pct)  # type: ignore[arg-type]
    recovery = recovery_colored(level.stress_recovery)  # type: ignore[arg-type]
    body = (
        f"#style1{{- Precision:}} #{color}{{{acc}}}"
        f"\n#style1{{- Aiming time:}} #{color}{{{aim}}}"
        f"\n#style1{{- Stress resistance:}} #{color}{{{stress}}}"
        f"\n#style1{{- Stress recovery:}} #{color}{{{recovery}}} #style1{{per second}}"
    )
    if level.evasion_pct is not None:
        evasion = pct_bonus(level.evasion_pct)
        body += f"\n#style1{{- Evasion:}} #{color}{{{evasion}}}"
    return body


def _body_helico_sf(level: LevelBonuses) -> str:
    color = "styleTurquoise"
    speed = pct_bonus(level.movement_speed_pct)  # type: ignore[arg-type]
    acc = pct_bonus(level.accuracy_pct)  # type: ignore[arg-type]
    aim = pct_reduction(level.aim_time_reduction_pct)  # type: ignore[arg-type]
    reload = pct_reduction(level.salvo_reload_reduction_pct)  # type: ignore[arg-type]
    stress = pct_bonus(level.stress_resistance_pct)  # type: ignore[arg-type]
    recovery = recovery_colored(level.stress_recovery)  # type: ignore[arg-type]
    evasion = pct_bonus(level.evasion_pct)  # type: ignore[arg-type]
    return (
        f"#style1{{- Movement speed:}} #{color}{{{speed}}}"
        f"\n#style1{{- Accuracy:}} #{color}{{{acc}}}"
        f"\n#style1{{- Aiming time:}} #{color}{{{aim}}}"
        f"\n#style1{{- Reload time:}} #{color}{{{reload}}}"
        f"\n#style1{{- Stress resistance:}} #{color}{{{stress}}}"
        f"\n#style1{{- Stress recovery:}} #{color}{{{recovery}}} #style1{{per second}}"
        f"\n#style1{{- Evasion:}} #{color}{{{evasion}}}"
    )


def _body_avion(level: LevelBonuses, level_index: int) -> str:
    evasion_normal_line = (
        "" if AVION_VET_REBALANCE_ENABLED else "\n#style1{- Evasive maneuvers: normal}"
    )

    if level_index == 0:
        return (
            "#style1{- Accuracy: normal}"
            "\n#style1{- Aiming time: normal}"
            "\n#style1{- Stress resistance: normal}"
            "\n#style1{- Stress recovery: normal}"
            f"{evasion_normal_line}"
        )

    color = _tier_color(level_index)

    if level_index == 1:
        recovery = recovery_colored(level.stress_recovery)  # type: ignore[arg-type]
        return (
            "#style1{- Accuracy: normal}"
            "\n#style1{- Aiming time: normal}"
            "\n#style1{- Stress resistance: normal}"
            f"\n#style1{{- Stress recovery:}} #{color}{{{recovery}}} #style1{{per second}}"
            f"{evasion_normal_line}"
        )

    acc = pct_bonus(_display_accuracy_pct(level))
    aim = pct_reduction(level.aim_time_reduction_pct)  # type: ignore[arg-type]
    stress = pct_bonus(level.stress_resistance_pct)  # type: ignore[arg-type]
    recovery = recovery_colored(level.stress_recovery)  # type: ignore[arg-type]
    evasion_line = ""
    if not AVION_VET_REBALANCE_ENABLED and level.evasion_pct is not None:
        evasion = pct_bonus(level.evasion_pct)
        evasion_line = f"\n#style1{{- Evasive maneuvers:}} #{color}{{{evasion}}}"
    return (
        f"#style1{{- Accuracy:}} #{color}{{{acc}}}"
        f"\n#style1{{- Aiming time:}} #{color}{{{aim}}}"
        f"\n#style1{{- Stress resistance:}} #{color}{{{stress}}}"
        f"\n#style1{{- Stress recovery:}} #{color}{{{recovery}}} #style1{{per second}}"
        f"{evasion_line}"
    )


_BODY_BUILDERS: dict[str, object] = {
    "simple_v3": _body_infantry_standard,
    "simple_v3_multiplicative": _body_infantry_standard,
    "SF_v2": _body_sf_standard,
    "SF_v2_multiplicative": _body_sf_standard,
    "artillery": _body_infantry_standard,
    "helico": _body_helico,
    "helico_attack": _body_helico,
    "avion": _body_avion,
}


def build_level_body(pack_type: str, level: LevelBonuses, level_index: int) -> str:
    if level.level_key == "helico_SF_3":
        return _body_helico_sf(level)
    builder = _BODY_BUILDERS[pack_type]
    return builder(level, level_index)  # type: ignore[operator]


def build_veterancy_ui_bodies() -> dict[str, dict[str, str]]:
    bodies: dict[str, dict[str, str]] = {}
    for pack_type, levels in PACK_LEVELS.items():
        bodies[pack_type] = {
            level.level_key: build_level_body(pack_type, level, level_index)
            for level_index, level in enumerate(levels)
        }
    for pack_type, extra_level in EXTRA_LEVEL_ENTRIES:
        bodies[pack_type][extra_level.level_key] = build_level_body(
            pack_type,
            extra_level,
            3,
        )
    return bodies


VETERANCY_UI_BODIES = build_veterancy_ui_bodies()
