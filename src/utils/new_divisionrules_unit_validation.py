"""Validate unit/transport names in active new division rules against unit_edits and NEW_UNITS."""

import importlib
import logging
from pathlib import Path
from typing import Any, Iterable, Set

from src.constants.generated.gameplay.decks import new_divisions
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
