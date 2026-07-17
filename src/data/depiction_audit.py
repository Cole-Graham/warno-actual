"""Audit step that flags units missing depiction edits.

After the depiction-editing refactor, ``WeaponDescriptor.equipmentchanges`` no
longer triggers automatic mesh / fire-effect / animation swaps inside
``DepictionInfantry.ndf``. Units that previously relied on that auto-swap need
a hand-authored entry in ``src/constants/unit_edits/depiction_edits/`` (for
existing units) or in ``src/constants/new_units/new_depictions/`` (for new
units).

This module walks ``unit_edits`` and ``NEW_UNITS`` and emits warnings (or
optionally raises) when a unit has equipment-changes but no matching depiction
file.

It also consults ``depiction_data`` (built from ``DepictionInfantry.ndf``) to
silently skip ``replace`` rows that are pure ammo-name swaps with no actual
depiction change. A row is considered a no-op when:

  * ``swap_fire_effect`` is ``False`` and ``all_weapon_meshes[old]`` equals
    ``all_weapon_meshes[new]``.
  * ``swap_fire_effect`` is ``True`` and both ``all_weapon_meshes`` and
    ``all_fire_effects`` agree for old and new.

Output is also written to ``logs/depiction_audit.json`` for batch review.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any, Dict, List, Mapping, Optional

from src.constants.unit_edits.replace_schema import ReplaceSpec, normalize_replace
from src.data.depiction_lookups import lookup as _dd_lookup
from src.data.depiction_lookups import same_vanilla
from src.utils.logging_utils import setup_logger

logger = setup_logger(__name__)

# Equipment-change keys that historically implied a depiction edit.
_EQUIPMENT_CHANGE_KEYS_NEEDING_DEPICTION = (
    "replace",
    "replace_fixedsalvo", # Not used and probably won't be needed in the future
    "add",
)


def _equipment_change_keys(weapon_descriptor: Any) -> List[str]:
    """Return the subset of equipmentchanges keys that imply a depiction edit."""
    if not isinstance(weapon_descriptor, dict):
        return []
    equipment_changes = weapon_descriptor.get("equipmentchanges")
    if not isinstance(equipment_changes, dict):
        return []
    return [k for k in _EQUIPMENT_CHANGE_KEYS_NEEDING_DEPICTION if k in equipment_changes]


def _is_replace_spec_noop(
    spec: ReplaceSpec, depiction_data: Optional[Mapping[str, Any]]
) -> bool:
    """Return True when this replace spec produces no visible depiction change.

    Four paths to no-op:

    1. **Baked-in opt-out**: ``spec.depiction_baked_in`` is True. Used for
       vehicles / aircraft whose weapon mesh is part of the hull/turret
       model rather than a separate WeaponAlternative.
    2. **Pure ammo rename**: ``old`` and ``new`` collapse to the same vanilla
       weapon id under ``MERGED_RENAMES``. Nothing in the rendered NDF
       actually changes -- the patcher's rename pass already keeps depiction
       references in sync.
    3. **Auto-detected**: ``all_weapon_meshes`` and (when ``swap_fire_effect``
       is True) ``all_fire_effects`` resolve to identical values for old and
       new weapons. Both lookups returning ``None`` (i.e. the weapons aren't
       infantry) does NOT auto-classify as no-op on its own - we only auto-
       detect when at least one side is known.
    4. **Explicit opt-out**: ``swap_fire_effect`` is False AND no mesh
       evidence contradicts the author. This covers aerial/vehicle weapon
       variants (e.g. ``RocketAir_S24_240mm_salvolength2`` vs ``...length4``)
       whose meshes never enter ``DepictionInfantry.ndf`` and therefore can't
       be auto-compared.

    All ``depiction_data`` lookups go through ``_dd_lookup`` so post-rename
    weapon ids in ``spec`` resolve to the vanilla-keyed depiction-data
    entries.
    """
    if spec.depiction_baked_in:
        return True
    if same_vanilla(spec.old_weapon, spec.new_weapon):
        return True

    all_weapon_meshes: Mapping[str, Any] = (depiction_data or {}).get("all_weapon_meshes") or {}
    all_fire_effects: Mapping[str, Any] = (depiction_data or {}).get("all_fire_effects") or {}

    old_mesh = _dd_lookup(all_weapon_meshes, spec.old_weapon)
    new_mesh = _dd_lookup(all_weapon_meshes, spec.new_weapon)
    meshes_known = old_mesh is not None and new_mesh is not None
    meshes_disagree = meshes_known and old_mesh != new_mesh
    if meshes_disagree:
        return False

    if not spec.swap_fire_effect:
        return True

    if not meshes_known:
        return False

    # Prefer bare fire-effect stems from ReplaceSpec (magazine suffixes stripped).
    old_fe_key = spec.old_fire_effect or spec.old_weapon
    new_fe_key = spec.new_fire_effect or spec.new_weapon
    old_fe = _dd_lookup(all_fire_effects, old_fe_key)
    new_fe = _dd_lookup(all_fire_effects, new_fe_key)
    if old_fe is None or new_fe is None:
        return False
    return old_fe == new_fe


def _filter_triggered_keys(
    weapon_descriptor: Any,
    triggered_keys: List[str],
    depiction_data: Optional[Mapping[str, Any]],
) -> List[str]:
    """Drop ``"replace"`` from the triggered set if every spec is a no-op."""
    if "replace" not in triggered_keys:
        return triggered_keys
    equipment_changes = weapon_descriptor.get("equipmentchanges") or {}
    specs = normalize_replace(equipment_changes.get("replace"))
    if not specs:
        return [k for k in triggered_keys if k != "replace"]
    # When ``depiction_data`` is unavailable we can still honour the
    # per-row ``depiction_baked_in`` / explicit ``swap_fire_effect=False``
    # opt-outs, so run the no-op check regardless.
    if all(_is_replace_spec_noop(s, depiction_data) for s in specs):
        return [k for k in triggered_keys if k != "replace"]
    return triggered_keys


def audit_missing_depiction_edits(
    *,
    unit_edits: Dict[str, Any],
    new_units: Dict[Any, Dict[str, Any]],
    depiction_edits: Dict[str, Any],
    new_depictions: Dict[str, Any],
    logs_dir: Path,
    depiction_data: Optional[Mapping[str, Any]] = None,
    strict: bool = False,
) -> Dict[str, Any]:
    """Compare ``unit_edits`` / ``new_units`` against authored depiction files.

    Args:
        unit_edits: Result of ``load_unit_edits()``.
        new_units: ``NEW_UNITS`` dict keyed by ``(donor_name, index)``.
        depiction_edits: Result of ``load_depiction_edits()``.
        new_depictions: ``NEW_DEPICTIONS`` dict keyed by ``unit_name.lower()``.
        logs_dir: Directory to write ``depiction_audit.json`` in.
        depiction_data: Optional ``game_db['depiction_data']`` used to detect
            no-op replace rows. When None, no-op detection is disabled.
        strict: If True, raise ``RuntimeError`` when any warnings are emitted.

    Returns:
        The audit report dict that was written to disk.
    """
    existing_unit_warnings: List[Dict[str, Any]] = []
    new_unit_warnings: List[Dict[str, Any]] = []

    for unit_name, edits in unit_edits.items():
        if not isinstance(edits, dict):
            continue
        weapon_descriptor = edits.get("WeaponDescriptor")
        triggered_keys = _equipment_change_keys(weapon_descriptor)
        if not triggered_keys:
            continue
        triggered_keys = _filter_triggered_keys(
            weapon_descriptor, triggered_keys, depiction_data,
        )
        if not triggered_keys:
            continue
        if unit_name in depiction_edits:
            continue
        existing_unit_warnings.append({
            "unit_name": unit_name,
            "equipmentchanges_keys": triggered_keys,
        })
        logger.warning(
            f"Unit '{unit_name}' has WeaponDescriptor.equipmentchanges keys "
            f"{triggered_keys} but no entry in depiction_edits/. "
            f"Weapon meshes / fire effects / animation tags will not be updated."
        )

    for donor_key, edits in new_units.items():
        if not isinstance(edits, dict):
            continue
        new_name = edits.get("NewName")
        if not new_name:
            continue
        weapon_descriptor = edits.get("WeaponDescriptor")
        triggered_keys = _equipment_change_keys(weapon_descriptor)
        if not triggered_keys:
            continue
        triggered_keys = _filter_triggered_keys(
            weapon_descriptor, triggered_keys, depiction_data,
        )
        if not triggered_keys:
            continue
        depiction_key = new_name.lower()
        if depiction_key in new_depictions:
            continue
        donor_name = donor_key[0] if isinstance(donor_key, tuple) and donor_key else str(donor_key)
        new_unit_warnings.append({
            "donor": donor_name,
            "new_name": new_name,
            "equipmentchanges_keys": triggered_keys,
        })
        logger.warning(
            f"New unit '{new_name}' (donor '{donor_name}') has WeaponDescriptor.equipmentchanges "
            f"keys {triggered_keys} but no entry in new_depictions/. "
            f"Weapon meshes / fire effects / animation tags will not be updated."
        )

    report = {
        "summary": {
            "existing_units_missing_depiction_edits": len(existing_unit_warnings),
            "new_units_missing_new_depictions": len(new_unit_warnings),
            "equipment_change_keys_audited": list(_EQUIPMENT_CHANGE_KEYS_NEEDING_DEPICTION),
            "noop_detection_enabled": depiction_data is not None,
        },
        "existing_units": existing_unit_warnings,
        "new_units": new_unit_warnings,
    }

    logs_dir.mkdir(parents=True, exist_ok=True)
    audit_path = logs_dir / "depiction_audit.json"
    with open(audit_path, "w") as f:
        json.dump(report, f, indent=4)

    total_warnings = len(existing_unit_warnings) + len(new_unit_warnings)
    if total_warnings:
        logger.info(
            f"Depiction audit: {total_warnings} unit(s) missing depiction edits. "
            f"See {audit_path}."
        )
        if strict:
            raise RuntimeError(
                f"Depiction audit failed in strict mode: {total_warnings} unit(s) "
                f"missing depiction edits. See {audit_path}."
            )
    else:
        logger.info("Depiction audit: all units with equipment changes have depiction edits.")

    return report


def _load_depiction_data() -> Optional[Mapping[str, Any]]:
    """Best-effort load of ``depiction_data.json`` from the standard db path.

    Returns ``None`` (and logs a debug note) when the file is missing - the
    caller falls back to coarse audit behaviour.
    """
    try:
        from config.config_loader import load_config

        config = load_config()
        db_path = Path(config["data_config"]["database_path"])
        depiction_data_path = db_path / "depiction_data.json"
        if not depiction_data_path.exists():
            logger.debug(
                f"Depiction audit: {depiction_data_path} not found; running without no-op detection."
            )
            return None
        with open(depiction_data_path) as f:
            return json.load(f)
    except Exception as exc:  # noqa: BLE001 - best-effort
        logger.debug(f"Depiction audit: could not load depiction_data ({exc}); no-op detection disabled.")
        return None


def run_depiction_audit(
    *, strict: bool = False, depiction_data: Optional[Mapping[str, Any]] = None,
) -> Dict[str, Any]:
    """Convenience entry point that resolves the standard data sources itself.

    Imports are done lazily so this module stays cheap to import in contexts
    that don't need the audit (or where the constants packages are not yet
    fully loaded).
    """
    from src.constants.new_units import NEW_DEPICTIONS, NEW_UNITS
    from src.constants.unit_edits import load_depiction_edits, load_unit_edits

    if depiction_data is None:
        depiction_data = _load_depiction_data()

    logs_dir = Path(__file__).resolve().parents[2] / "logs"
    return audit_missing_depiction_edits(
        unit_edits=load_unit_edits(),
        new_units=NEW_UNITS,
        depiction_edits=load_depiction_edits(),
        new_depictions=NEW_DEPICTIONS,
        logs_dir=logs_dir,
        depiction_data=depiction_data,
        strict=strict,
    )
