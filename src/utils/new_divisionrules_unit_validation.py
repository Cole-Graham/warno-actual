"""Validate unit/transport names in active new division rules against unit_edits and NEW_UNITS.

Also validates that each division's ``standout_units`` appear in the merged division rules
(primary unit or transport), matching WARNO's Division.ndf checks.

``transport_overrides`` transport names are checked against the union of transports in 4th
tuple fields across that division's merged ``division_rules``; overrides and
``rule_exclusions`` are not applied when building that union.
"""

import importlib
import logging
from pathlib import Path
from typing import Any, Dict, Iterable, List, Optional, Set

from src.constants.generated.gameplay.decks import load_new_divisions, new_divisions
from src.constants.new_units import NEW_UNITS
from src.constants.unit_edits import load_unit_edits
from src.utils.logging_utils import setup_logger

logger = setup_logger(__name__)

_NEW_DIVISIONRULES_PKG = "src.constants.generated.gameplay.decks.new_divisions.new_divisionrules"

_NEW_DIVS_EXCLUDED_FROM_RULE_SCAN = frozenset({"spec_matrices", "DIV_TYPE_TO_TOKEN"})


def collect_used_newdivisionrules_dict_ids() -> Set[int]:
    """Object ids of division rule dicts listed under division_rules in new_divisions exports."""
    used: set[int] = set()
    for export_name in new_divisions.__all__:
        if export_name in _NEW_DIVS_EXCLUDED_FROM_RULE_SCAN:
            continue
        divs = getattr(new_divisions, export_name, None)
        if not isinstance(divs, dict):
            continue
        for _key, cfg in divs.items():
            if not isinstance(cfg, dict):
                continue
            rules = cfg.get("division_rules")
            if not isinstance(rules, list):
                continue
            for item in rules:
                if isinstance(item, dict):
                    used.add(id(item))
    return used


def _iter_rule_unit_and_transport_names(rules_dict: dict[str, Any]) -> Iterable[str]:
    for _category, entries in rules_dict.items():
        if not isinstance(entries, list):
            continue
        for row in entries:
            if not isinstance(row, tuple) or len(row) < 3:
                continue
            primary = row[0]
            if isinstance(primary, str):
                yield primary
            if len(row) >= 4 and isinstance(row[3], list):
                for transport in row[3]:
                    if isinstance(transport, str):
                        yield transport


def _valid_unit_and_new_unit_names() -> set[str]:
    unit_edits = load_unit_edits()
    names = set(unit_edits.keys())
    for edits in NEW_UNITS.values():
        if isinstance(edits, dict):
            new_name = edits.get("NewName")
            if isinstance(new_name, str):
                names.add(new_name)
    return names


def _collect_units_emitted_for_new_division(
    div_data: Dict[str, Any],
    game_db: Dict[str, Any] | None,
) -> Set[str]:
    """Unit names that ``_create_national_division_rules`` would add (primary or transport).

    Mirrors the per-tuple filtering in ``division_rules._create_national_division_rules`` so
    standout validation matches in-game ``StandoutUnits`` checks.
    """
    # Local import: ``validate_new_divisionrules_units`` does not need division_rules; this path does.
    from src.gameplay_mods.generated.gameplay.decks.division_rules import (
        _validate_unit_name,
    )

    present: set[str] = set()
    custom_rules = div_data.get("division_rules")
    if not custom_rules:
        return present

    rule_exclusions = div_data.get("rule_exclusions", []) or []
    transport_overrides = div_data.get("transport_overrides", {}) or {}

    if isinstance(custom_rules, dict):
        rules_dicts = [custom_rules]
    elif isinstance(custom_rules, list):
        rules_dicts = custom_rules
    else:
        return present

    for rules_dict in rules_dicts:
        if not isinstance(rules_dict, dict):
            continue
        for _category, unit_rules in rules_dict.items():
            if not isinstance(unit_rules, list):
                continue
            for rule_tuple in unit_rules:
                if len(rule_tuple) == 3:
                    unit_name, _cards, availability = rule_tuple
                    transports = None
                elif len(rule_tuple) == 4:
                    unit_name, _cards, availability, transports = rule_tuple
                else:
                    continue

                if not isinstance(unit_name, str):
                    continue

                if unit_name in transport_overrides:
                    transports = transport_overrides[unit_name]

                if rule_exclusions and unit_name in rule_exclusions:
                    continue

                if not isinstance(availability, list) or len(availability) != 4:
                    continue

                if transports is not None and not isinstance(transports, list):
                    transports = None

                if transports:
                    valid_transports: List[Optional[str]] = []
                    for transport in transports:
                        if transport is None:
                            valid_transports.append(None)
                            continue
                        if not isinstance(transport, str):
                            continue
                        if " " in transport:
                            continue
                        if game_db is not None and not _validate_unit_name(transport, game_db):
                            continue
                        valid_transports.append(transport)
                    transports = valid_transports if valid_transports else None

                if " " in unit_name:
                    continue

                if game_db is not None and not _validate_unit_name(unit_name, game_db):
                    continue

                present.add(unit_name)
                if transports:
                    for transport in transports:
                        if isinstance(transport, str) and transport:
                            present.add(transport)

    return present


def validate_standout_units_in_division_rules(
    log: logging.Logger | None = None,
    game_db: Dict[str, Any] | None = None,
) -> None:
    """Emit a warning for each ``standout_units`` entry not in merged ``division_rules``.

    WARNO fails at mod load with one unit at a time; this lists all mismatches in the patcher log.
    """
    log = log or logger
    new_divisions_merged = load_new_divisions()
    for div_key, div_data in new_divisions_merged.items():
        if not isinstance(div_data, dict):
            continue
        standout_units = div_data.get("standout_units") or []
        if not standout_units:
            continue
        present = _collect_units_emitted_for_new_division(div_data, game_db)
        cfg_name = div_data.get("cfg_name", div_key)
        for unit in standout_units:
            if isinstance(unit, str) and unit not in present:
                log.warning(
                    "Standout unit %r is not present in merged division_rules for %s "
                    "(cfg_name=%s); Division.ndf will reject the mod until this unit appears "
                    "as a primary unit or transport in that division's rules.",
                    unit,
                    div_key,
                    cfg_name,
                )


def validate_new_divisionrules_units(log: logging.Logger | None = None) -> None:
    """Warn once per missing unit/transport for division rules used in *_new_divs.

    Skips rule dicts that are never referenced from a division's division_rules list
    (e.g. POL_marines_newdivisionrules while marines are commented out in POL_new_divs).
    """
    log = log or logger
    used_ids = collect_used_newdivisionrules_dict_ids()
    valid_names = _valid_unit_and_new_unit_names()
    warned: set[str] = set()

    pkg = importlib.import_module(_NEW_DIVISIONRULES_PKG)
    rules_dir = Path(next(iter(pkg.__path__)))
    for path in sorted(rules_dir.glob("*_newdivisionrules.py")):
        stem = path.stem
        mod = importlib.import_module(f"{_NEW_DIVISIONRULES_PKG}.{stem}")
        for attr_name in dir(mod):
            if not attr_name.endswith("_newdivisionrules"):
                continue
            rules_dict = getattr(mod, attr_name)
            if not isinstance(rules_dict, dict):
                continue
            if id(rules_dict) not in used_ids:
                continue
            for name in _iter_rule_unit_and_transport_names(rules_dict):
                if name in valid_names or name in warned:
                    continue
                if name.startswith("FOB_"):
                    continue
                warned.add(name)
                log.warning(
                    "New division rules (%s) reference unit or transport %r not found in "
                    "unit_edits or NEW_UNITS",
                    attr_name,
                    name,
                )


def _collect_transport_names_from_division_rules(division_rules: Any) -> Set[str]:
    """All transport unit names in 4-tuple rows across one division's rule dict(s).

    ``division_rules`` is a single category->rules dict or a list of such dicts, matching
    ``_create_national_division_rules``. Does not apply ``transport_overrides`` or
    ``rule_exclusions``; the set is the pool declared in the newdivisionrules data.
    """
    names: set[str] = set()
    if isinstance(division_rules, dict):
        rules_dicts: List[dict[str, Any]] = [division_rules]
    elif isinstance(division_rules, list):
        rules_dicts = division_rules
    else:
        return names

    for rules_dict in rules_dicts:
        if not isinstance(rules_dict, dict):
            continue
        for _category, unit_rules in rules_dict.items():
            if not isinstance(unit_rules, list):
                continue
            for rule_tuple in unit_rules:
                if (
                    not isinstance(rule_tuple, tuple)
                    or len(rule_tuple) < 4
                    or not isinstance(rule_tuple[3], list)
                ):
                    continue
                for transport in rule_tuple[3]:
                    if isinstance(transport, str) and transport:
                        names.add(transport)
    return names


def validate_transport_overrides_against_division_rule_transports(
    log: logging.Logger | None = None,
) -> None:
    """Emit a warning when ``transport_overrides`` lists a transport not in any 4-tuple in merged rules.

    Allowed transports are the union of all transport names from 4th tuple fields across
    this division's ``division_rules`` dicts (same as national newdivisionrules merged for
    that deck entry).
    """
    log = log or logger
    new_divisions_merged = load_new_divisions()
    for div_key, div_data in new_divisions_merged.items():
        if not isinstance(div_data, dict):
            continue
        transport_overrides = div_data.get("transport_overrides") or {}
        if not transport_overrides:
            continue
        allowed = _collect_transport_names_from_division_rules(
            div_data.get("division_rules"),
        )
        cfg_name = div_data.get("cfg_name", div_key)
        for unit_name, transport_list in transport_overrides.items():
            if not isinstance(transport_list, list):
                continue
            for t in transport_list:
                if not isinstance(t, str) or not t:
                    continue
                if t in allowed:
                    continue
                log.warning(
                    "transport_overrides for division %r (cfg_name=%s) lists transport %r for "
                    "unit %r, but that transport does not appear in any 4-tuple transport list "
                    "in this division's division_rules; add it to a rule row or remove it from "
                    "the override.",
                    div_key,
                    cfg_name,
                    t,
                    unit_name,
                )
