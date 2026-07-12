"""Widen AA missile turrets on helicopters to ±90° pitch/yaw."""

import re
from typing import Any, Dict

from src.constants.unit_edits.standards import (
    HELO_AA_TURRET_ANGLES_PATTERN_STANDARD,
    HeloAaTurretAnglesPatternStandard,
)
from src.utils.ndf_utils import is_obj_type, is_valid_turret

_AMMO_PREFIX = "$/GFX/Weapon/Ammo_"
_SUFFIX_RE = re.compile(r"(_x\d+|_salvolength\d+|_infmagazine\d+|_strength\d+)$")


def _extract_ammo_ns(ammo_path: str) -> str:
    if _AMMO_PREFIX in ammo_path:
        return ammo_path.split(_AMMO_PREFIX, 1)[1].strip()
    return ammo_path


def _base_helo_aa_ammo_name(ammo_namespace: str, ammo_bases: frozenset[str]) -> str | None:
    """Return matching helo AA base name if ``ammo_namespace`` is that base or a variant."""
    stripped = _SUFFIX_RE.sub("", ammo_namespace)
    if stripped.endswith("_HAGRU"):
        stripped = stripped[: -len("_HAGRU")]
    if stripped in ammo_bases:
        return stripped
    return None


def _apply_turret_angles(turret: Any, angles: Dict[str, str]) -> None:
    for membr, value in angles.items():
        row = turret.v.by_m(membr, False)
        if row is not None:
            row.v = value
        else:
            turret.v.add(f"{membr} = {value}")


def apply_helo_aa_turret_angles_pattern_standard(
    logger: Any,
    source_path: Any,
    game_db: Dict[str, Any],
    std: HeloAaTurretAnglesPatternStandard | None = None,
) -> None:
    """Widen turrets carrying helo AA ammo on helicopter WeaponDescriptors."""
    if std is None:
        std = HELO_AA_TURRET_ANGLES_PATTERN_STANDARD

    unit_db = game_db.get("unit_data", {})
    ammo_bases = frozenset(std["ammo_bases"])
    angles = std["turret_angles"]
    applied = 0

    for weapon_descr in source_path:
        if not hasattr(weapon_descr, "namespace"):
            continue
        if not weapon_descr.namespace.startswith("WeaponDescriptor_"):
            continue
        unit_name = weapon_descr.namespace.replace("WeaponDescriptor_", "")
        unit_info = unit_db.get(unit_name, {})
        if not unit_info.get("is_helo_unit"):
            continue

        turret_list_membr = weapon_descr.v.by_m("TurretDescriptorList", False)
        if turret_list_membr is None:
            continue

        for turret in turret_list_membr.v:
            if not is_valid_turret(turret.v):
                continue
            mounted_list = turret.v.by_m("MountedWeaponDescriptorList", False)
            if mounted_list is None:
                continue

            has_helo_aa = False
            for mount in mounted_list.v:
                if not is_obj_type(mount.v, "TMountedWeaponDescriptor"):
                    continue
                ammo_membr = mount.v.by_m("Ammunition", False)
                if ammo_membr is None:
                    continue
                ammo_ns = _extract_ammo_ns(str(ammo_membr.v))
                if _base_helo_aa_ammo_name(ammo_ns, ammo_bases) is not None:
                    has_helo_aa = True
                    break

            if not has_helo_aa:
                continue

            _apply_turret_angles(turret, angles)
            applied += 1
            logger.debug(f"Helo AA turret angles applied on {unit_name}")

    logger.info(f"Helo AA turret angle pattern applied to {applied} turrets")
