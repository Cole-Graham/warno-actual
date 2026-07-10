"""Apply HOBS no-HMD pattern to existing units on WeaponDescriptor.ndf (before unit_edits).

New units are out of scope: they are added later in ``new_units_weapondescriptor`` and
configure HOBS turrets / ammo explicitly in ``NEW_UNITS`` (not ``unit_edits``).
"""

import re
from typing import Any, Dict

from src.constants.unit_edits.standards import HOBS_NO_HMD_PATTERN_STANDARD, HobsNoHmdPatternStandard
from src.utils.ndf_utils import is_obj_type, is_valid_turret, strip_quotes

_AMMO_PREFIX = "$/GFX/Weapon/Ammo_"
_SUFFIX_RE = re.compile(r"(_x\d+|_salvolength\d+|_infmagazine\d+|_strength\d+)$")
_NOOBS_MARKER = "NoOBS"


def _normalize_trait(spec: str) -> str:
    return strip_quotes(spec)


def _unit_has_projected_hmd(
    unit_name: str,
    unit_edits: Dict[str, Any],
    hmd_trait: str,
) -> bool:
    specs: set[str] = set()

    edits = unit_edits.get(unit_name, {})
    sl = edits.get("SpecialtiesList", {})
    if isinstance(sl, dict):
        for spec in sl.get("add_specs", []):
            specs.add(_normalize_trait(spec))
        for spec in sl.get("overwrite_all", []):
            specs.add(_normalize_trait(spec))
        for spec in sl.get("remove_specs", []):
            specs.discard(_normalize_trait(spec))
    elif isinstance(sl, list):
        for spec in sl:
            specs.add(_normalize_trait(spec))

    return hmd_trait in specs


def _base_ammo_name(ammo_namespace: str) -> str:
    return _SUFFIX_RE.sub("", ammo_namespace)


def _resolve_swap_target(base: str, rule: Dict[str, Any]) -> str | None:
    if _NOOBS_MARKER in base:
        return None
    if base == rule["hobs_base"]:
        return rule["no_obs_base"]
    if base == rule.get("hagru_base"):
        return rule.get("no_obs_hagru_base")
    return None


def _swap_ammo_path(current_path: str, new_base: str) -> str:
    if _AMMO_PREFIX not in current_path:
        return current_path
    ammo_ns = current_path.split(_AMMO_PREFIX, 1)[1]
    suffix = ammo_ns[len(_base_ammo_name(ammo_ns)) :]
    return f"{_AMMO_PREFIX}{new_base}{suffix}"


def _swappable_hobs_bases(rule: Dict[str, Any]) -> frozenset[str]:
    bases = {rule["hobs_base"]}
    hagru = rule.get("hagru_base")
    if hagru:
        bases.add(hagru)
    return frozenset(bases)


def _apply_turret_angles(turret: Any, angles: Dict[str, str]) -> None:
    for membr, value in angles.items():
        row = turret.v.by_m(membr, False)
        if row is not None:
            row.v = value


def apply_hobs_no_hmd_pattern_for_weapon_descr(
    logger: Any,
    weapon_descr: Any,
    unit_name: str,
    unit_edits: Dict[str, Any],
    std: HobsNoHmdPatternStandard | None = None,
) -> bool:
    """Apply HOBS no-HMD rules to one weapon descriptor. Returns True if anything changed."""
    if std is None:
        std = HOBS_NO_HMD_PATTERN_STANDARD

    if _unit_has_projected_hmd(unit_name, unit_edits, std["hmd_trait"]):
        return False

    turret_list_membr = weapon_descr.v.by_m("TurretDescriptorList", False)
    if turret_list_membr is None:
        return False

    changed = False
    for rule in std["missile_rules"]:
        swappable_bases = _swappable_hobs_bases(rule)

        for turret in turret_list_membr.v:
            if not is_valid_turret(turret.v):
                continue

            mounted_list = turret.v.by_m("MountedWeaponDescriptorList", False)
            if mounted_list is None:
                continue

            turret_has_hobs = False
            for mount in mounted_list.v:
                if not is_obj_type(mount.v, "TMountedWeaponDescriptor"):
                    continue
                ammo_membr = mount.v.by_m("Ammunition", False)
                if ammo_membr is None:
                    continue
                base = _base_ammo_name(_extract_ammo_ns(str(ammo_membr.v)))
                if base in swappable_bases:
                    turret_has_hobs = True
                    break

            if not turret_has_hobs:
                continue

            _apply_turret_angles(turret, rule["turret_angles"])
            changed = True

            for mount in mounted_list.v:
                if not is_obj_type(mount.v, "TMountedWeaponDescriptor"):
                    continue
                ammo_membr = mount.v.by_m("Ammunition", False)
                if ammo_membr is None:
                    continue
                current = str(ammo_membr.v)
                base = _base_ammo_name(_extract_ammo_ns(current))
                new_base = _resolve_swap_target(base, rule)
                if new_base is None:
                    continue
                new_path = _swap_ammo_path(current, new_base)
                if new_path != current:
                    ammo_membr.v = new_path
                    changed = True
                    logger.debug(
                        f"HOBS no-HMD: {unit_name} {base} -> {new_base}",
                    )

    if changed:
        logger.debug(f"HOBS no-HMD pattern applied to {unit_name}")

    return changed


def _extract_ammo_ns(ammo_path: str) -> str:
    if _AMMO_PREFIX in ammo_path:
        return ammo_path.split(_AMMO_PREFIX, 1)[1].strip()
    return ammo_path


def apply_hobs_no_hmd_pattern_standard(
    logger: Any,
    source_path: Any,
    game_db: Dict[str, Any],
) -> None:
    """Batch-apply HOBS no-HMD pattern before unit_edits (dict edits override)."""
    from src.constants.unit_edits import load_unit_edits

    unit_edits = load_unit_edits()
    std = HOBS_NO_HMD_PATTERN_STANDARD
    applied = 0

    for weapon_descr in source_path:
        if not hasattr(weapon_descr, "namespace"):
            continue
        if not weapon_descr.namespace.startswith("WeaponDescriptor_"):
            continue
        unit_name = weapon_descr.namespace.replace("WeaponDescriptor_", "")
        if apply_hobs_no_hmd_pattern_for_weapon_descr(
            logger,
            weapon_descr,
            unit_name,
            unit_edits,
            std,
        ):
            applied += 1

    if applied:
        logger.info(
            f"HOBS no-HMD pattern applied to {applied} weapon descriptor(s)",
        )
