"""Validate menu / tactical-label texture strings in unit_edits and NEW_UNITS.

Compares against vanilla allowlists in ``game_db["ui_texture_reference"]`` built
by ``gather_ui_texture_reference`` in ``unit_data.py`` (case-sensitive exact match).
``ButtonTexture`` is intentionally not validated here.
"""

from __future__ import annotations

from typing import Any, Dict, List, Set

from src.constants.new_units import NEW_UNITS
from src.constants.unit_edits import load_unit_edits
from src.utils.logging_utils import setup_logger

logger = setup_logger(__name__)


def validate_ui_texture_constants(
    game_db: Dict[str, Any],
) -> bool:
    """Check that texture fields in constants match vanilla reference data.

    Returns:
        True if any invalid reference was found (validation failed).
    """
    ref = game_db.get("ui_texture_reference") if game_db else None
    if not ref:
        logger.warning(
            "ui_texture_reference missing from game_db; skipping UI texture validation",
        )
        return False

    menu_ok: Set[str] = set(ref.get("menu_icon_textures", []))
    identified_ok: Set[str] = set(ref.get("tactical_label_identified_textures", []))
    unidentified_ok: Set[str] = set(ref.get("tactical_label_unidentified_textures", []))

    errors: List[str] = []

    unit_edits = load_unit_edits()
    for unit_name, edits in unit_edits.items():
        if isinstance(unit_name, str) and unit_name.endswith("_reference"):
            continue
        if not isinstance(edits, dict):
            continue
        _walk_constants_for_textures(
            edits,
            f"unit_edits[{unit_name}]",
            menu_ok,
            identified_ok,
            unidentified_ok,
            errors,
        )

    for neu_key, edits in NEW_UNITS.items():
        if isinstance(neu_key, str) and neu_key.endswith("_reference"):
            continue
        if not isinstance(edits, dict):
            continue
        label = repr(neu_key) if not isinstance(neu_key, str) else neu_key
        _walk_constants_for_textures(
            edits,
            f"NEW_UNITS[{label}]",
            menu_ok,
            identified_ok,
            unidentified_ok,
            errors,
        )

    if errors:
        for err in errors:
            logger.error("Invalid UI texture constant: %s", err)
        logger.error(
            "Found %s invalid UI texture constant(s). "
            "Use strings from ui_texture_reference or fix typos (case-sensitive).",
            len(errors),
        )
        return True
    return False


def _walk_constants_for_textures(
    obj: Any,
    path: str,
    menu_ok: Set[str],
    identified_ok: Set[str],
    unidentified_ok: Set[str],
    errors: List[str],
) -> None:
    if isinstance(obj, dict):
        for key, val in obj.items():
            child_path = f"{path}.{key}"
            if key == "IdentifiedTextures":
                _check_texture_list(val, identified_ok, child_path, errors)
                continue
            if key == "UnidentifiedTextures":
                _check_texture_list(val, unidentified_ok, child_path, errors)
                continue
            if key == "MenuIconTexture":
                _check_menu_icon(val, menu_ok, child_path, errors)
                continue
            _walk_constants_for_textures(
                val,
                child_path,
                menu_ok,
                identified_ok,
                unidentified_ok,
                errors,
            )
    elif isinstance(obj, list):
        for i, item in enumerate(obj):
            _walk_constants_for_textures(
                item,
                f"{path}[{i}]",
                menu_ok,
                identified_ok,
                unidentified_ok,
                errors,
            )


def _check_texture_list(
    value: Any,
    allow: Set[str],
    path: str,
    errors: List[str],
) -> None:
    if not isinstance(value, list):
        errors.append(f"{path}: expected list, got {type(value).__name__}")
        return
    for i, item in enumerate(value):
        if not isinstance(item, str):
            errors.append(
                f"{path}[{i}]: expected str, got {type(item).__name__}",
            )
            continue
        if item not in allow:
            errors.append(f"{path}[{i}]: unknown texture '{item}'")


def _check_menu_icon(
    value: Any,
    allow: Set[str],
    path: str,
    errors: List[str],
) -> None:
    if not isinstance(value, str):
        errors.append(f"{path}: expected str, got {type(value).__name__}")
        return
    if value not in allow:
        errors.append(f"{path}: unknown MenuIconTexture '{value}'")
