"""Apply MissileDescriptor movement fields to guided-missile movement configs."""

from typing import Any, Dict, Optional

from src import ndf

_PHASE_CONFIG_MEMBERS = ("AscendantPhaseConfig", "TerminalPhaseConfig")


def resolve_missile_max_acceleration_gru(
    missile_descriptor: Dict[str, Any],
    max_speed: Optional[int] = None,
) -> Optional[int]:
    """Return explicit or derived (2/3 of MaxSpeedGRU) acceleration, or None."""
    if "MaxAccelerationGRU" in missile_descriptor:
        return missile_descriptor["MaxAccelerationGRU"]
    speed = max_speed if max_speed is not None else missile_descriptor.get("MaxSpeedGRU")
    if speed is not None:
        return round(speed * 2 / 3)
    return None


def apply_ammunition_missile_acceleration(
    descr: Any,
    data: Dict[str, Any],
    logger: Any,
) -> None:
    """Set flat MaxAccelerationGRU on a TAmmunitionDescriptor when not explicit in constants."""
    missile_descriptor = data.get("MissileDescriptor")
    if not isinstance(missile_descriptor, dict):
        return
    if "MaxAccelerationGRU" in missile_descriptor:
        return

    parent_membr = data.get("Ammunition", {}).get("parent_membr") or {}
    if "MaxAccelerationGRU" in parent_membr:
        return

    max_accel = resolve_missile_max_acceleration_gru(missile_descriptor)
    if max_accel is None:
        return

    descr.v.by_m("MaxAccelerationGRU").v = str(max_accel)  # noqa
    logger.debug(f"Changed {descr.namespace} ammunition max acceleration to {max_accel}")


def _phase_config_if_present(movement_module: Any, member_name: str) -> Any | None:
    row = movement_module.v.by_m(member_name, False)
    if row is None:
        return None
    if isinstance(row.v, ndf.model.Object):
        return row
    return None


def _apply_speed_and_accel(
    cfg: Any,
    max_speed: Optional[int],
    max_accel: Optional[int],
    namespace: str,
    config_label: str,
    logger: Any,
) -> None:
    if max_speed is not None:
        cfg.v.by_m("MaxSpeedGRU").v = str(max_speed)  # noqa
        logger.debug(f"Changed {namespace} {config_label} max speed to {max_speed}")

    if max_accel is not None:
        cfg.v.by_m("MaxAccelerationGRU").v = str(max_accel)  # noqa
        logger.debug(f"Changed {namespace} {config_label} max acceleration to {max_accel}")


def apply_missile_descriptor_movement_configs(
    movement_module: Any,
    missile_descriptor: Dict[str, Any],
    namespace: str,
    logger: Any,
) -> None:
    """Write MaxSpeedGRU, MaxAccelerationGRU, and AutoGyr from constants edits."""
    max_speed = missile_descriptor.get("MaxSpeedGRU")
    max_accel = resolve_missile_max_acceleration_gru(missile_descriptor, max_speed)

    default_cfg = movement_module.v.by_m("DefaultConfig")
    uncontrollable_cfg = movement_module.v.by_m("UncontrollableConfig")
    _apply_speed_and_accel(default_cfg, max_speed, max_accel, namespace, "default", logger)
    _apply_speed_and_accel(
        uncontrollable_cfg, max_speed, max_accel, namespace, "uncontrollable", logger,
    )

    for phase_member in _PHASE_CONFIG_MEMBERS:
        phase_cfg = _phase_config_if_present(movement_module, phase_member)
        if phase_cfg is None:
            continue
        _apply_speed_and_accel(
            phase_cfg, max_speed, max_accel, namespace, phase_member, logger,
        )

    if "AutoGyr" in missile_descriptor:
        auto_gyr = missile_descriptor["AutoGyr"]
        default_cfg.v.by_m("AutoGyr").v = str(auto_gyr)  # noqa
        logger.debug(f"Changed {namespace} auto gyr to {auto_gyr} (90 degrees)")
