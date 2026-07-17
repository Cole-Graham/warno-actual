"""Validate infantry FireEffect stems against ``depiction_data.all_fire_effects``.

Infantry muzzle FX are registered as ``FireEffect_<stem>`` keys (scraped into
``game_db["depiction_data"]["all_fire_effects"]``, matching InfanterieWeaponsUnites).
Magazine salvolength / infmagazine suffixes must never appear on those tags.

Vehicle channel tags (``weapon_effet_tagN``) and he_dca ``*_AIR`` EffectTags are
out of scope. MountedWeapons EffectTags that are not in the infantry registry
and have no magazine suffix are also skipped (vanilla has many vehicle-only
mount tags).

Dedicated HMG/MMG teams (name prefix), AT teams (``Infanterie_AT`` TagSet), heavy
equipment, and aircraft use vehicle / aerial depiction Actions (not
DepictionInfantry), so their WeaponDescriptor ``swap_fire_effect`` stems are
not required to exist in ``all_fire_effects``.
"""

from __future__ import annotations

import json
import re
from pathlib import Path
from typing import Any, Dict, List, Mapping, Optional, Set, Tuple

from src.constants.new_units import NEW_DEPICTIONS, NEW_UNITS
from src.constants.unit_edits import load_depiction_edits, load_unit_edits
from src.constants.unit_edits.replace_schema import (
    fire_effect_stem_from_ammo,
    normalize_replace,
)
from src.data.depiction_lookups import lookup as _dd_lookup
from src.utils.logging_utils import setup_logger
from src.utils.ndf_utils import strip_quotes

logger = setup_logger(__name__)

_MAGAZINE_SUFFIX_RE = re.compile(r"(_salvolength\d+|_infmagazine\d+)")
_FIRE_EFFECT_TAG_RE = re.compile(
    r'FireEffectTag\s*=\s*["\']FireEffect_([^"\']+)["\']',
)
_EFFECT_TAG_MEMBER_RE = re.compile(
    r"^FireEffect_(.+)$",
)

# HMG/MMG teams use DepictionVehicles Actions maps, not infantry FireEffect_* stems.
# AT teams are detected via the Infanterie_AT TagSet tag (not all use ATteam_ prefix).
_VEHICLE_STYLE_WEAPON_TEAM_PREFIXES: tuple[str, ...] = (
    "HMGteam_",
    "MMGteam_",
)

_INFANTERIE_AT_TAG = "Infanterie_AT"

_AERIAL_UNIT_TAGS: frozenset[str] = frozenset({"Avion", "Helico", "Air"})


def _all_fire_effects(game_db: Optional[Mapping[str, Any]]) -> Mapping[str, Any]:
    if not game_db:
        return {}
    depiction_data = game_db.get("depiction_data") or {}
    return depiction_data.get("all_fire_effects") or {}


def _normalize_raw_body(raw: str) -> str:
    """Strip quotes and optional ``FireEffect_`` prefix (keep magazine suffixes)."""
    stem = strip_quotes(raw) if isinstance(raw, str) else str(raw)
    if stem.startswith("FireEffect_"):
        stem = stem[len("FireEffect_"):]
    return stem


def _normalize_authored_stem(raw: str) -> str:
    """Strip quotes, optional FireEffect_ prefix, and magazine suffixes."""
    return fire_effect_stem_from_ammo(_normalize_raw_body(raw))


def _is_vehicle_channel_tag(stem: str) -> bool:
    return strip_quotes(stem).startswith("weapon_effet_tag")


def _is_he_dca_air_tag(stem: str) -> bool:
    return strip_quotes(stem).endswith("_AIR")


def _has_magazine_suffix(raw: str) -> bool:
    return bool(_MAGAZINE_SUFFIX_RE.search(raw))


def is_vehicle_style_weapon_team(unit_name: str) -> bool:
    """True for HMG/MMG teams by name prefix (vehicle depiction FX, not infantry)."""
    return unit_name.startswith(_VEHICLE_STYLE_WEAPON_TEAM_PREFIXES)


def _tags_from_edits(edits: Optional[Mapping[str, Any]]) -> Set[str]:
    """Collect authored TagSet names from unit_edits / NEW_UNITS."""
    if not isinstance(edits, Mapping):
        return set()
    tagset = edits.get("TagSet")
    if not isinstance(tagset, Mapping):
        # NEW_UNITS often uses a flat list under TagSet / overwrite_all style.
        if isinstance(tagset, (list, tuple)):
            return {strip_quotes(str(t)) for t in tagset}
        return set()
    tags: Set[str] = set()
    if "overwrite_all" in tagset and isinstance(tagset["overwrite_all"], (list, tuple)):
        tags.update(strip_quotes(str(t)) for t in tagset["overwrite_all"])
    if "add_tags" in tagset and isinstance(tagset["add_tags"], (list, tuple)):
        tags.update(strip_quotes(str(t)) for t in tagset["add_tags"])
    return tags


def _unit_data_tags(
    unit_name: str,
    game_db: Optional[Mapping[str, Any]],
) -> Set[str]:
    if not game_db:
        return set()
    unit_info = (game_db.get("unit_data") or {}).get(unit_name) or {}
    tags = unit_info.get("tags") or []
    return {strip_quotes(str(t)) for t in tags}


def _unit_has_infanterie_at(
    unit_name: str,
    edits: Optional[Mapping[str, Any]],
    game_db: Optional[Mapping[str, Any]],
) -> bool:
    """True when live or authored TagSet includes Infanterie_AT."""
    if _INFANTERIE_AT_TAG in _tags_from_edits(edits):
        return True
    return _INFANTERIE_AT_TAG in _unit_data_tags(unit_name, game_db)


def unit_skips_infantry_fire_registry(
    unit_name: str,
    edits: Optional[Mapping[str, Any]] = None,
    game_db: Optional[Mapping[str, Any]] = None,
) -> bool:
    """True when WeaponDescriptor fire effects are not infantry DepictionInfantry FX."""
    if is_vehicle_style_weapon_team(unit_name):
        return True
    if _unit_has_infanterie_at(unit_name, edits, game_db):
        return True
    if isinstance(edits, Mapping):
        if edits.get("is_aerial"):
            return True
        if edits.get("is_heavy_equipment"):
            return True
        if edits.get("is_ground_vehicle") and not edits.get("is_infantry"):
            return True
    tags = _unit_data_tags(unit_name, game_db)
    if tags & _AERIAL_UNIT_TAGS:
        return True
    return False


def fire_effect_exists(
    stem: str,
    game_db: Optional[Mapping[str, Any]],
) -> bool:
    """True when ``stem`` resolves in ``all_fire_effects`` (rename-aware)."""
    normalized = _normalize_authored_stem(stem)
    if not normalized or _is_vehicle_channel_tag(normalized):
        return True
    if _is_he_dca_air_tag(normalized):
        base = normalized[: -len("_AIR")]
        return _dd_lookup(_all_fire_effects(game_db), base) is not None
    return _dd_lookup(_all_fire_effects(game_db), normalized) is not None


def ensure_fire_effect_exists(
    stem: str,
    *,
    game_db: Optional[Mapping[str, Any]] = None,
    context: str = "",
    strict: bool = False,
    require_infantry_registry: bool = True,
) -> bool:
    """Log (and optionally raise) when an infantry fire-effect stem is invalid.

    Returns:
        True if the stem is acceptable, False if invalid.
    """
    if not stem:
        return True
    raw_body = _normalize_raw_body(stem)

    if _is_vehicle_channel_tag(raw_body):
        return True

    ctx = f" ({context})" if context else ""

    if _has_magazine_suffix(raw_body):
        msg = (
            f"Fire effect must not include magazine suffixes{ctx}: "
            f"{raw_body!r} (use bare stem {fire_effect_stem_from_ammo(raw_body)!r})"
        )
        logger.error(msg)
        if strict:
            raise RuntimeError(msg)
        return False

    if _is_he_dca_air_tag(raw_body):
        # AIR tags are synthetic mount identifiers; FX assets use the ground stem.
        return True

    if not require_infantry_registry:
        return True

    all_fe = _all_fire_effects(game_db)
    if not all_fe:
        logger.debug(
            "ensure_fire_effect_exists: all_fire_effects unavailable; skipping lookup%s",
            ctx,
        )
        return True

    normalized = fire_effect_stem_from_ammo(raw_body)
    if _dd_lookup(all_fe, normalized) is not None:
        return True

    msg = f"Unknown infantry fire effect{ctx}: {normalized!r}"
    logger.error(msg)
    if strict:
        raise RuntimeError(msg)
    return False


def validate_fire_effect_constants(
    game_db: Optional[Mapping[str, Any]],
    *,
    strict: bool = False,
) -> bool:
    """Walk unit/new-unit/depiction constants for invalid infantry fire effects.

    Returns:
        True if any invalid reference was found (validation failed).
    """
    all_fe = _all_fire_effects(game_db)
    if not all_fe:
        logger.warning(
            "depiction_data.all_fire_effects missing; skipping fire-effect validation",
        )
        return False

    errors: List[str] = []
    seen: Set[Tuple[str, str]] = set()

    def record(path: str, raw: str, *, require_registry: bool) -> None:
        key = (path, raw)
        if key in seen:
            return
        seen.add(key)
        raw_body = _normalize_raw_body(raw)
        if _is_vehicle_channel_tag(raw_body):
            return
        if _is_he_dca_air_tag(raw_body):
            return
        if _has_magazine_suffix(raw_body):
            errors.append(
                f"{path}: magazine suffix on fire effect {raw_body!r} "
                f"(use {fire_effect_stem_from_ammo(raw_body)!r})",
            )
            return
        if not require_registry:
            # Vehicle / aerial / MountedWeapons: only magazine-suffix rule above.
            if _dd_lookup(all_fe, fire_effect_stem_from_ammo(raw_body)) is None:
                return
        stem = fire_effect_stem_from_ammo(raw_body)
        if _dd_lookup(all_fe, stem) is None:
            errors.append(f"{path}: unknown infantry fire effect {stem!r}")

    unit_edits = load_unit_edits()
    for unit_name, edits in unit_edits.items():
        if not isinstance(edits, dict):
            continue
        _collect_from_weapon_descriptor(
            edits.get("WeaponDescriptor"),
            f"unit_edits[{unit_name}].WeaponDescriptor",
            record,
            require_registry=not unit_skips_infantry_fire_registry(
                unit_name, edits, game_db,
            ),
        )

    for neu_key, edits in NEW_UNITS.items():
        if not isinstance(edits, dict):
            continue
        label = edits.get("NewName") or repr(neu_key)
        unit_label = str(label)
        _collect_from_weapon_descriptor(
            edits.get("WeaponDescriptor"),
            f"NEW_UNITS[{label}].WeaponDescriptor",
            record,
            require_registry=not unit_skips_infantry_fire_registry(
                unit_label, edits, game_db,
            ),
        )

    depiction_edits = load_depiction_edits()
    for unit_name, unit_data in depiction_edits.items():
        if not isinstance(unit_data, dict):
            continue
        _collect_from_depiction_envelope(
            unit_data,
            f"depiction_edits[{unit_name}]",
            record,
        )

    for unit_key, unit_data in NEW_DEPICTIONS.items():
        if not isinstance(unit_data, dict):
            continue
        label = unit_data.get("unit_name") or unit_key
        _collect_from_depiction_envelope(
            unit_data,
            f"NEW_DEPICTIONS[{label}]",
            record,
        )

    if errors:
        for err in errors:
            logger.error("Invalid fire effect constant: %s", err)
        logger.error(
            "Found %s invalid fire-effect constant(s). "
            "Use bare stems present in depiction_data.all_fire_effects.",
            len(errors),
        )
        if strict:
            raise RuntimeError(
                f"Fire-effect validation failed: {len(errors)} invalid reference(s).",
            )
        return True
    logger.info("Fire-effect validation: all authored infantry FireEffect stems are known.")
    return False


def run_fire_effect_validation(
    *,
    game_db: Optional[Mapping[str, Any]] = None,
    strict: bool = False,
) -> bool:
    """Convenience entry that loads depiction_data when ``game_db`` is omitted."""
    if game_db is None:
        game_db = {"depiction_data": _load_depiction_data() or {}}
    return validate_fire_effect_constants(game_db, strict=strict)


def _load_depiction_data() -> Optional[Mapping[str, Any]]:
    try:
        from config.config_loader import load_config

        config = load_config()
        db_path = Path(config["data_config"]["database_path"])
        depiction_data_path = db_path / "depiction_data.json"
        if not depiction_data_path.exists():
            return None
        with open(depiction_data_path) as f:
            return json.load(f)
    except Exception as exc:  # noqa: BLE001 - best-effort
        logger.debug("Could not load depiction_data for fire-effect validation: %s", exc)
        return None


def _collect_from_weapon_descriptor(
    weapon_descriptor: Any,
    path: str,
    record,
    *,
    require_registry: bool = True,
) -> None:
    if not isinstance(weapon_descriptor, dict):
        return
    equipment = weapon_descriptor.get("equipmentchanges")
    if isinstance(equipment, dict):
        replace_block = equipment.get("replace")
        for spec in normalize_replace(replace_block):
            if not spec.swap_fire_effect:
                continue
            # Baked-in hull/vehicle FX are not infantry DepictionInfantry stems.
            row_require = require_registry and not spec.depiction_baked_in
            if spec.old_fire_effect:
                record(
                    f"{path}.equipmentchanges.replace[{spec.old_weapon}].old_fire_effect",
                    spec.old_fire_effect,
                    require_registry=row_require,
                )
            if spec.new_fire_effect:
                record(
                    f"{path}.equipmentchanges.replace[{spec.old_weapon}].new_fire_effect",
                    spec.new_fire_effect,
                    require_registry=row_require,
                )
        insert_block = equipment.get("insert")
        if isinstance(insert_block, (list, tuple)):
            for i, item in enumerate(insert_block):
                if isinstance(item, (list, tuple)) and len(item) >= 3:
                    fe = item[2]
                    if isinstance(fe, str):
                        record(
                            f"{path}.equipmentchanges.insert[{i}].fire_effect",
                            fe,
                            require_registry=require_registry,
                        )
    mounted = weapon_descriptor.get("MountedWeapons")
    if mounted is not None:
        _walk_for_effect_tag_members(
            mounted,
            f"{path}.MountedWeapons",
            record,
            require_registry=False,
        )


def _walk_for_effect_tag_members(
    obj: Any,
    path: str,
    record,
    *,
    require_registry: bool,
) -> None:
    if isinstance(obj, dict):
        for key, val in obj.items():
            child = f"{path}.{key}" if not isinstance(key, int) else f"{path}[{key}]"
            if key == "EffectTag" and isinstance(val, str):
                body = strip_quotes(val)
                match = _EFFECT_TAG_MEMBER_RE.match(body)
                if match:
                    record(child, match.group(1), require_registry=require_registry)
                elif _has_magazine_suffix(body):
                    record(child, body, require_registry=require_registry)
                continue
            _walk_for_effect_tag_members(
                val, child, record, require_registry=require_registry,
            )
    elif isinstance(obj, (list, tuple)):
        for i, item in enumerate(obj):
            _walk_for_effect_tag_members(
                item, f"{path}[{i}]", record, require_registry=require_registry,
            )


def _depiction_section_requires_infantry_registry(section_key: str) -> bool:
    """Only DepictionInfantry_* sections author infantry FireEffect_* stems."""
    return section_key.startswith("DepictionInfantry")


def _collect_from_depiction_envelope(
    unit_data: Mapping[str, Any],
    path: str,
    record,
) -> None:
    for key, section in unit_data.items():
        if not isinstance(key, str) or not key.endswith("_ndf"):
            continue
        require = _depiction_section_requires_infantry_registry(key)
        _walk_depiction_section(section, f"{path}.{key}", record, require_registry=require)


def _walk_depiction_section(
    obj: Any,
    path: str,
    record,
    *,
    require_registry: bool = True,
) -> None:
    if isinstance(obj, dict):
        for key, val in obj.items():
            child = f"{path}.{key}" if not isinstance(key, int) else f"{path}[{key}]"
            # Indexed op: (edit_type, [(submember, value), ...]) or similar
            if isinstance(key, int) and isinstance(val, (list, tuple)) and val:
                _collect_from_indexed_op(
                    val, child, record, require_registry=require_registry,
                )
                continue
            if key == "FireEffectTag" and isinstance(val, str):
                record(child, val, require_registry=require_registry)
                continue
            if isinstance(val, str) and "FireEffectTag" in val:
                for match in _FIRE_EFFECT_TAG_RE.finditer(val):
                    record(f"{child}[ndf]", match.group(1), require_registry=require_registry)
                continue
            _walk_depiction_section(
                val, child, record, require_registry=require_registry,
            )
    elif isinstance(obj, (list, tuple)):
        for i, item in enumerate(obj):
            if isinstance(item, str) and "FireEffectTag" in item:
                for match in _FIRE_EFFECT_TAG_RE.finditer(item):
                    record(
                        f"{path}[{i}][ndf]",
                        match.group(1),
                        require_registry=require_registry,
                    )
            else:
                _walk_depiction_section(
                    item, f"{path}[{i}]", record, require_registry=require_registry,
                )
    elif isinstance(obj, str) and "FireEffectTag" in obj:
        for match in _FIRE_EFFECT_TAG_RE.finditer(obj):
            record(f"{path}[ndf]", match.group(1), require_registry=require_registry)


def _collect_from_indexed_op(
    op: Any,
    path: str,
    record,
    *,
    require_registry: bool = True,
) -> None:
    """Handle ``(edit_type, payload)`` depiction operator rows."""
    if not isinstance(op, (list, tuple)) or not op:
        return
    edit_type = op[0]
    if edit_type not in ("edit", "insert", "add", "replace"):
        return
    payload = op[1] if len(op) > 1 else None
    if isinstance(payload, (list, tuple)):
        for entry in payload:
            if isinstance(entry, (list, tuple)) and len(entry) >= 2:
                submember, mv = entry[0], entry[1]
                if submember == "FireEffectTag" and isinstance(mv, str):
                    record(
                        f"{path}.FireEffectTag",
                        mv,
                        require_registry=require_registry,
                    )
    elif isinstance(payload, str) and "FireEffectTag" in payload:
        for match in _FIRE_EFFECT_TAG_RE.finditer(payload):
            record(f"{path}[ndf]", match.group(1), require_registry=require_registry)


# Re-export for tests / callers that collect stems without full validation.
def collect_fire_effect_stems_from_replace(replace_block: Any) -> List[str]:
    """Return fire-effect stems that ``swap_fire_effect`` replace rows will write."""
    stems: List[str] = []
    for spec in normalize_replace(replace_block):
        if not spec.swap_fire_effect:
            continue
        if spec.new_fire_effect:
            stems.append(spec.new_fire_effect)
        if spec.old_fire_effect:
            stems.append(spec.old_fire_effect)
    return stems
