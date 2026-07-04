"""Validate default multiplayer deck loadouts against division rules and activation limits."""

from __future__ import annotations

import logging
from dataclasses import dataclass
from typing import Any, Dict, Iterable, List, Optional, Tuple

from src.constants.generated.gameplay.decks import load_default_multi_decks, load_new_divisions
from src.constants.generated.gameplay.decks.new_divisions import spec_matrices
from src.gameplay_mods.generated.gameplay.decks.default_multi_decks import (
    DEFAULT_CATEGORY_ORDER,
    parse_entry,
    strip_unit_descriptor,
)
from src.utils.logging_utils import setup_logger

logger = setup_logger(__name__)

DEFAULT_DECK_CATEGORY_TO_FACTORY = {
    "Logistic": "Factory/Logistic",
    "Infantry": "Factory/Infantry",
    "Artillery": "Factory/Art",
    "Tanks": "Factory/Tanks",
    "Recon": "Factory/Recons",
    "AA": "Factory/DCA",
    "Helicopters": "Factory/Helis",
    "Air": "Factory/Planes",
}

MAX_UNUSED_ACTIVATION_POINTS = 2


@dataclass(frozen=True)
class MergedUnitRule:
    max_cards: int
    availability: Tuple[int, int, int, int]
    transports: Optional[Tuple[Optional[str], ...]]


def flatten_categories_with_category(categories: Dict) -> List[Tuple[str, Dict]]:
    if not categories:
        return []

    entries: List[Tuple[str, Dict]] = []
    for category in DEFAULT_CATEGORY_ORDER:
        cat_entries = categories.get(category)
        if not cat_entries:
            continue
        for entry in cat_entries:
            entries.append((category, entry))

    for category, cat_entries in categories.items():
        if category in DEFAULT_CATEGORY_ORDER or not cat_entries:
            continue
        for entry in cat_entries:
            entries.append((category, entry))

    return entries


def _merge_transport_names(
    transports_a: Optional[List[Optional[str]]],
    transports_b: Optional[List[Optional[str]]],
) -> Optional[Tuple[Optional[str], ...]]:
    if transports_a is None and transports_b is None:
        return None

    merged: List[Optional[str]] = []
    seen: set[Optional[str]] = set()
    for transport_list in (transports_a, transports_b):
        if not transport_list:
            continue
        for transport in transport_list:
            if transport in seen:
                continue
            seen.add(transport)
            merged.append(transport)
    return tuple(merged) if merged else None


def build_merged_division_unit_rules(div_data: Dict[str, Any]) -> Dict[str, MergedUnitRule]:
    """Merge division_rules the same way division_rules.py dedupes by primary unit."""
    merged: Dict[str, MergedUnitRule] = {}
    custom_rules = div_data.get("division_rules")
    if not custom_rules:
        return merged

    rule_exclusions = div_data.get("rule_exclusions", []) or []
    transport_overrides = div_data.get("transport_overrides", {}) or {}

    if isinstance(custom_rules, dict):
        rules_dicts = [custom_rules]
    elif isinstance(custom_rules, list):
        rules_dicts = custom_rules
    else:
        return merged

    for rules_dict in rules_dicts:
        if not isinstance(rules_dict, dict):
            continue
        for _category, unit_rules in rules_dict.items():
            if not isinstance(unit_rules, list):
                continue
            for rule_tuple in unit_rules:
                if len(rule_tuple) == 3:
                    unit_name, cards, availability = rule_tuple
                    transports = None
                elif len(rule_tuple) == 4:
                    unit_name, cards, availability, transports = rule_tuple
                else:
                    continue

                if not isinstance(unit_name, str):
                    continue
                if rule_exclusions and unit_name in rule_exclusions:
                    continue
                if unit_name in transport_overrides:
                    transports = transport_overrides[unit_name]
                if not isinstance(availability, list) or len(availability) != 4:
                    continue
                if not all(isinstance(value, int) for value in availability):
                    continue
                if transports is not None and not isinstance(transports, list):
                    transports = None

                availability_tuple = tuple(availability)
                transport_tuple = tuple(transports) if transports else None

                if unit_name in merged:
                    existing = merged[unit_name]
                    if cards > existing.max_cards:
                        merged[unit_name] = MergedUnitRule(
                            max_cards=cards,
                            availability=availability_tuple,
                            transports=_merge_transport_names(
                                list(existing.transports) if existing.transports else None,
                                list(transport_tuple) if transport_tuple else None,
                            ),
                        )
                    elif cards == existing.max_cards:
                        merged[unit_name] = MergedUnitRule(
                            max_cards=cards,
                            availability=existing.availability,
                            transports=_merge_transport_names(
                                list(existing.transports) if existing.transports else None,
                                list(transport_tuple) if transport_tuple else None,
                            ),
                        )
                    else:
                        merged[unit_name] = MergedUnitRule(
                            max_cards=existing.max_cards,
                            availability=existing.availability,
                            transports=_merge_transport_names(
                                list(existing.transports) if existing.transports else None,
                                list(transport_tuple) if transport_tuple else None,
                            ),
                        )
                else:
                    merged[unit_name] = MergedUnitRule(
                        max_cards=cards,
                        availability=availability_tuple,
                        transports=transport_tuple,
                    )

    return merged


def resolve_division_cost_matrix(div_key: str, div_data: Dict[str, Any]) -> Dict[str, List[int]]:
    if "_" in div_key:
        div_type = div_key.split("_", 1)[1]
    else:
        div_type = "general"

    matrix_override = div_data.get("matrix_override")
    spec_key = matrix_override if matrix_override else div_type
    if spec_key not in spec_matrices:
        return {}

    matrix_data = {
        factory: list(costs)
        for factory, costs in spec_matrices[spec_key].items()
        if factory != "total_for_valid"
    }
    if "matrix_overrides" in div_data:
        matrix_data.update(div_data["matrix_overrides"])
    return matrix_data


def _divisions_by_cfg_name() -> Dict[str, Tuple[str, Dict[str, Any]]]:
    by_cfg_name: Dict[str, Tuple[str, Dict[str, Any]]] = {}
    for div_key, div_data in load_new_divisions().items():
        if not isinstance(div_data, dict):
            continue
        cfg_name = div_data.get("cfg_name")
        if cfg_name:
            by_cfg_name[cfg_name] = (div_key, div_data)
    return by_cfg_name


def _iter_default_deck_cards(
    cfg_name: str,
    categories: Dict,
) -> Iterable[Tuple[str, str, int, Optional[str]]]:
    for category, entry in flatten_categories_with_category(categories):
        unit_ref, opts = parse_entry(entry)
        unit_name = strip_unit_descriptor(unit_ref)
        vet = opts["vet"]
        transport_name = None
        if "transport" in opts:
            transport_name = strip_unit_descriptor(opts["transport"])
        yield category, unit_name, vet, transport_name


def validate_default_multi_decks(log: logging.Logger | None = None) -> bool:
    """Validate default multiplayer decks against division rules and activation limits.

    Returns True when any validation error was logged.
    """
    log = log or logger
    default_decks = load_default_multi_decks()
    if not default_decks:
        return False

    divisions_by_cfg_name = _divisions_by_cfg_name()
    failed = False

    for cfg_name, categories in default_decks.items():
        entries = flatten_categories_with_category(categories)
        if not entries:
            continue

        division_info = divisions_by_cfg_name.get(cfg_name)
        if division_info is None:
            log.warning(
                "Default multiplayer deck %r has cards but no matching division metadata in "
                "load_new_divisions(); skipping validation",
                cfg_name,
            )
            failed = True
            continue

        div_key, div_data = division_info
        merged_rules = build_merged_division_unit_rules(div_data)
        cost_matrix = resolve_division_cost_matrix(div_key, div_data)
        max_activation = div_data.get("activation_points", 85)
        factory_slot_counts: Dict[str, int] = {}
        unit_pick_counts: Dict[str, int] = {}
        total_activation = 0

        for category, unit_name, vet, transport_name in _iter_default_deck_cards(cfg_name, categories):
            rule = merged_rules.get(unit_name)
            if rule is None:
                log.warning(
                    "Default deck %r (%s) includes unit %r, which is not available in merged "
                    "division_rules for %s",
                    cfg_name,
                    div_key,
                    unit_name,
                    cfg_name,
                )
                failed = True
                continue

            unit_pick_counts[unit_name] = unit_pick_counts.get(unit_name, 0) + 1
            if unit_pick_counts[unit_name] > rule.max_cards:
                log.warning(
                    "Default deck %r (%s) takes unit %r %d times but division rules allow "
                    "MaxPackNumber=%d",
                    cfg_name,
                    div_key,
                    unit_name,
                    unit_pick_counts[unit_name],
                    rule.max_cards,
                )
                failed = True

            if vet < 0 or vet >= len(rule.availability):
                log.warning(
                    "Default deck %r (%s) uses invalid vet level %d for unit %r",
                    cfg_name,
                    div_key,
                    vet,
                    unit_name,
                )
                failed = True
                continue

            if rule.availability[vet] <= 0:
                log.warning(
                    "Default deck %r (%s) uses vet level %d for unit %r but merged division rules "
                    "only allow vets %s (availability=%s)",
                    cfg_name,
                    div_key,
                    vet,
                    unit_name,
                    [index for index, count in enumerate(rule.availability) if count > 0],
                    list(rule.availability),
                )
                failed = True

            if transport_name and rule.transports is not None:
                allowed_transports = {
                    transport
                    for transport in rule.transports
                    if isinstance(transport, str) and transport
                }
                if transport_name not in allowed_transports:
                    log.warning(
                        "Default deck %r (%s) uses transport %r for unit %r but merged division "
                        "rules only allow transports %s",
                        cfg_name,
                        div_key,
                        transport_name,
                        unit_name,
                        sorted(allowed_transports),
                    )
                    failed = True

            factory = DEFAULT_DECK_CATEGORY_TO_FACTORY.get(category)
            if factory is None:
                log.warning(
                    "Default deck %r (%s) uses unknown category %r for unit %r",
                    cfg_name,
                    div_key,
                    category,
                    unit_name,
                )
                failed = True
                continue

            slot_index = factory_slot_counts.get(factory, 0)
            factory_costs = cost_matrix.get(factory, [])
            if slot_index >= len(factory_costs):
                log.warning(
                    "Default deck %r (%s) exceeds cost-matrix slots for %s: card %d for unit %r "
                    "but matrix only defines %d slot(s)",
                    cfg_name,
                    div_key,
                    factory,
                    slot_index + 1,
                    unit_name,
                    len(factory_costs),
                )
                failed = True
                continue

            total_activation += factory_costs[slot_index]
            factory_slot_counts[factory] = slot_index + 1

        if total_activation > max_activation:
            log.warning(
                "Default deck %r (%s) spends %d activation points but division limit is %d",
                cfg_name,
                div_key,
                total_activation,
                max_activation,
            )
            failed = True

        min_activation = max_activation - MAX_UNUSED_ACTIVATION_POINTS
        if total_activation < min_activation:
            unused = max_activation - total_activation
            log.warning(
                "Default deck %r (%s) spends %d/%d activation points (%d unused); "
                "default decks may leave at most %d AP unused (minimum spend %d)",
                cfg_name,
                div_key,
                total_activation,
                max_activation,
                unused,
                MAX_UNUSED_ACTIVATION_POINTS,
                min_activation,
            )
            failed = True

    return failed
