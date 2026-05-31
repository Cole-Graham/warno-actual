"""Validate aircraft Standard vision range vs mounted weapon ground range.

Ensures ``VisionRangesGRU["EVisionRange/Standard"]`` is at least as high as the
maximum post-patch ``MaximumRangeGRU`` among weapons mounted on each fixed-wing
or helicopter unit.

Known limitation: deep ``WeaponDescriptor.turrets.MountedWeapons`` insert/replace
edits that add ammo not present in vanilla ``game_db["weapons"]`` may be missed.
``equipmentchanges.replace`` swaps are applied.

Only units listed in active ``*_newdivisionrules`` dicts (referenced from
``*_new_divs``) produce error logs; other aircraft are skipped silently.
"""

from __future__ import annotations

import re
from typing import Any, Dict, List, Optional, Set, Tuple

from src.constants.new_units import NEW_UNITS
from src.constants.unit_edits import load_unit_edits
from src.constants.unit_edits.replace_schema import normalize_replace
from src.constants.weapons import ammunitions, missiles
from src.constants.weapons.standards.pattern.weapon_range import (
    WEAPON_RANGE_MEMBERS_TO_CHECK,
)
from src.utils.logging_utils import setup_logger
from src.utils.new_divisionrules_unit_validation import collect_newdivisionrules_unit_names

logger = setup_logger(__name__)

_SALVO_SUFFIX_RE = re.compile(r"(_x\d+|_salvolength\d+)$")
_GROUND_RANGE_STANDARDS = WEAPON_RANGE_MEMBERS_TO_CHECK.get("MaximumRangeGRU", {})


def _is_aircraft(unit_info: Dict[str, Any]) -> bool:
    if not isinstance(unit_info, dict):
        return False
    if "airplane_movement" in unit_info or unit_info.get("is_helo_unit"):
        return True
    tags = unit_info.get("tags") or []
    return "Avion" in tags or "Helico" in tags


def _resolve_standard_vision(
    unit_info: Dict[str, Any],
    edits: Optional[Dict[str, Any]],
) -> Optional[float]:
    vision: Optional[float] = None
    optics = unit_info.get("optics") or {}
    if optics.get("standard_range") is not None:
        vision = float(optics["standard_range"])
    elif optics.get("ground_range") is not None:
        vision = float(optics["ground_range"])

    if edits and isinstance(edits, dict):
        vision_ranges = edits.get("optics", {}).get("VisionRangesGRU", {})
        if isinstance(vision_ranges, dict) and "EVisionRange/Standard" in vision_ranges:
            try:
                vision = float(vision_ranges["EVisionRange/Standard"])
            except (TypeError, ValueError):
                pass

    return vision


def _build_unit_replace_map(
    unit_name: str,
    edits: Optional[Dict[str, Any]],
) -> Dict[str, str]:
    if not edits or not isinstance(edits, dict):
        return {}
    replacements: Dict[str, str] = {}
    replace_block = (
        edits.get("WeaponDescriptor", {})
        .get("equipmentchanges", {})
        .get("replace")
    )
    for spec in normalize_replace(replace_block):
        old_base = _SALVO_SUFFIX_RE.sub("", spec.old_weapon)
        new_base = _SALVO_SUFFIX_RE.sub("", spec.new_weapon)
        replacements[old_base] = new_base
    return replacements


def _resolve_weapon_descriptor_name(
    unit_name: str,
    donor_name: Optional[str],
    weapons_db: Dict[str, Any],
) -> Optional[str]:
    candidate_self = f"WeaponDescriptor_{unit_name}"
    if candidate_self in weapons_db:
        return candidate_self
    if donor_name:
        candidate_donor = f"WeaponDescriptor_{donor_name}"
        if candidate_donor in weapons_db:
            return candidate_donor
    return None


def _collect_mounted_ammo_bases(
    unit_name: str,
    game_db: Dict[str, Any],
    edits: Optional[Dict[str, Any]],
    donor_name: Optional[str] = None,
) -> Set[str]:
    weapons_db = game_db.get("weapons", {})
    descriptor_name = _resolve_weapon_descriptor_name(unit_name, donor_name, weapons_db)
    if not descriptor_name:
        return set()

    replace_map = _build_unit_replace_map(unit_name, edits)
    weapon_info = weapons_db.get(descriptor_name, {})
    bases: Set[str] = set()

    for turret in weapon_info.get("turrets", {}).values():
        for ammo_name in turret.get("weapons", {}).keys():
            base = _SALVO_SUFFIX_RE.sub("", ammo_name)
            effective = replace_map.get(base, base)
            bases.add(effective)

    return bases


def _lookup_vanilla_maximum_range_gru(
    base_ammo_name: str,
    ammo_props: Dict[str, Any],
) -> Optional[float]:
    candidates = [base_ammo_name]
    if "_salvolength" in base_ammo_name:
        prefix, suffix = base_ammo_name.rsplit("_salvolength", 1)
        if suffix.isdigit():
            candidates.extend([f"{prefix}_x{suffix}", prefix])
    if "_x" in base_ammo_name:
        prefix, suffix = base_ammo_name.rsplit("_x", 1)
        if suffix.isdigit():
            candidates.extend([f"{prefix}_salvolength{suffix}", prefix])

    seen: Set[str] = set()
    for name in candidates:
        if not name or name in seen:
            continue
        seen.add(name)
        entry = ammo_props.get(f"Ammo_{name}")
        if not entry:
            continue
        val = entry.get("MaximumRangeGRU")
        if val is not None:
            try:
                return float(val)
            except (TypeError, ValueError):
                continue
    return None


def _constants_maximum_range_gru(base_ammo_name: str) -> Optional[float]:
    for (name, _, _, _), data in {**ammunitions, **missiles}.items():
        if name != base_ammo_name or not isinstance(data, dict):
            continue
        ammunition = data.get("Ammunition")
        if not isinstance(ammunition, dict):
            break
        parent = ammunition.get("parent_membr") or {}
        if "MaximumRangeGRU" in parent:
            try:
                return float(parent["MaximumRangeGRU"])
            except (TypeError, ValueError):
                break
        break
    return None


def _apply_ground_range_standards(value: float) -> float:
    int_val = int(value)
    if int_val in _GROUND_RANGE_STANDARDS:
        return float(_GROUND_RANGE_STANDARDS[int_val])
    return value


def _effective_maximum_range_gru(base_ammo: str, game_db: Dict[str, Any]) -> Optional[float]:
    constants_val = _constants_maximum_range_gru(base_ammo)
    if constants_val is not None:
        return constants_val

    ammo_props = game_db.get("ammunition", {}).get("ammo_properties", {})
    vanilla_val = _lookup_vanilla_maximum_range_gru(base_ammo, ammo_props)
    if vanilla_val is None:
        return None
    return _apply_ground_range_standards(vanilla_val)


def _iter_aircraft_units(game_db: Dict[str, Any]) -> List[Tuple[str, Dict[str, Any], Optional[Dict[str, Any]], Optional[str], str]]:
    """Yield (unit_name, unit_info, edits, donor_name, source_label) for each aircraft."""
    unit_data = game_db.get("unit_data", {})
    unit_edits = load_unit_edits()
    results: List[Tuple[str, Dict[str, Any], Optional[Dict[str, Any]], Optional[str], str]] = []
    seen: Set[str] = set()

    for unit_name, unit_info in unit_data.items():
        if not isinstance(unit_info, dict):
            continue
        if not _is_aircraft(unit_info):
            continue
        edits = unit_edits.get(unit_name)
        source = "unit_edits" if unit_name in unit_edits else "vanilla"
        results.append((unit_name, unit_info, edits, None, source))
        seen.add(unit_name)

    for neu_key, new_unit_data in NEW_UNITS.items():
        if not isinstance(new_unit_data, dict):
            continue
        new_name = new_unit_data.get("NewName")
        if not isinstance(new_name, str) or new_name in seen:
            continue
        donor_name = neu_key[0] if isinstance(neu_key, tuple) and neu_key else None
        if not isinstance(donor_name, str):
            continue
        base_info = unit_data.get(new_name) or unit_data.get(donor_name, {})
        if not base_info or not _is_aircraft(base_info):
            continue
        results.append((new_name, base_info, new_unit_data, donor_name, "NEW_UNITS"))
        seen.add(new_name)

    return results


def validate_aircraft_vision_vs_weapon_range(game_db: Dict[str, Any]) -> bool:
    """Validate aircraft Standard vision vs max weapon MaximumRangeGRU.

    Returns True if any violations were found.
    """
    if not game_db:
        logger.warning("game_db missing; skipping aircraft vision validation")
        return False

    errors: List[str] = []
    warnings: List[str] = []
    division_rules_units = collect_newdivisionrules_unit_names()

    for unit_name, unit_info, edits, donor_name, source in _iter_aircraft_units(game_db):
        vision = _resolve_standard_vision(unit_info, edits)
        mounted = _collect_mounted_ammo_bases(unit_name, game_db, edits, donor_name)

        weapon_ranges: List[Tuple[str, float]] = []
        for base_ammo in mounted:
            range_gru = _effective_maximum_range_gru(base_ammo, game_db)
            if range_gru is not None and range_gru > 0:
                weapon_ranges.append((base_ammo, range_gru))

        if not weapon_ranges:
            continue

        required_max = max(r for _, r in weapon_ranges)
        offending = [name for name, r in weapon_ranges if r == required_max]

        if vision is None:
            warnings.append(
                f"[{source}] {unit_name}: cannot resolve EVisionRange/Standard "
                f"(max weapon MaximumRangeGRU={required_max:g}, weapons: {', '.join(offending)})",
            )
            continue

        if vision < required_max:
            if unit_name not in division_rules_units:
                continue
            errors.append(
                f"[{source}] {unit_name}: EVisionRange/Standard={vision:g} < "
                f"max weapon MaximumRangeGRU={required_max:g} ({', '.join(offending)})",
            )

    for warn in warnings:
        logger.warning("Aircraft vision validation: %s", warn)

    if errors:
        for err in errors:
            logger.error("Aircraft vision validation: %s", err)
        logger.error(
            "Found %s aircraft vision violation(s). "
            "Raise EVisionRange/Standard or reduce weapon MaximumRangeGRU.",
            len(errors),
        )
        return True

    if warnings:
        logger.warning(
            "Aircraft vision validation: %s unit(s) skipped due to missing Standard vision.",
            len(warnings),
        )

    return False
