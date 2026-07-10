"""Remount organic infantry AT/AA onto magazine salvolength variants."""

from __future__ import annotations

from collections import defaultdict
from typing import Any, Dict, List, Optional, Set, Tuple

from src.constants.weapons import LIGHT_AT_AMMO, ammunitions, missiles
from src.data.infantry_magazine_salvo import (
    INFANTRY_MAGAZINE_CATEGORIES,
    magazine_ammo_name,
    magazine_suffix_kind,
    parse_magazine_length,
    split_hagru_base,
    strip_magazine_suffixes,
    unify_shared_pool_magazine_length,
)
from src.utils.ndf_utils import is_obj_type, is_valid_turret
from src.utils.logging_utils import setup_logger

logger = setup_logger(__name__)

_AMMO_PREFIX = "$/GFX/Weapon/Ammo_"


def _category_for_ammo(ammo_name: str) -> Optional[str]:
    bare, _ = split_hagru_base(strip_magazine_suffixes(ammo_name))
    for (name, category, _, _), _ in {**ammunitions, **missiles}.items():
        if name == bare:
            return category
    return None


def _set_salves_at_index(weapon_descr: Any, salvo_index: int, value: int) -> None:
    salves_list = weapon_descr.v.by_m("Salves").v
    salves_list.replace(int(salvo_index), str(value))


def _remount_weapon(
    mounted: Any,
    weapon_descr: Any,
    new_ammo: str,
    salvo_index: Optional[int],
) -> None:
    mounted.v.by_m("Ammunition").v = f"{_AMMO_PREFIX}{new_ammo}"
    if salvo_index is not None:
        _set_salves_at_index(weapon_descr, salvo_index, 1)


def _hagru_variant_name(bare: str, length: int, kind: str) -> str:
    if kind == "infmagazine":
        return f"{bare}_HAGRU_infmagazine{length}"
    return f"{bare}_HAGRU_salvolength{length}"


def _resolve_pool_length(
    group: List[Dict[str, Any]],
    remount_lookup: Dict[Tuple[str, str, bool], Dict[str, Any]],
    unit_name: str,
    strength_i: Optional[int],
) -> Optional[int]:
    """Unify magazine length for every mount sharing an AmmoBoxIndex."""
    lengths: List[int] = []
    for entry in group:
        bare = entry["bare"]
        is_hagru = entry["is_hagru"]
        category = entry["category"]

        if category == "light_at" and strength_i is not None and strength_i in LIGHT_AT_AMMO:
            lengths.append(int(LIGHT_AT_AMMO[strength_i]))

        row = remount_lookup.get((unit_name, bare, is_hagru))
        if not row and is_hagru:
            row = remount_lookup.get((unit_name, bare, False))
        if row:
            lengths.append(int(row["length"]))
            continue

        # Already on a magazine variant — keep that length in the pool vote
        existing = parse_magazine_length(entry["ammo_name"])
        if existing is not None and existing > 1:
            lengths.append(existing)

    return unify_shared_pool_magazine_length(lengths)


def apply_infantry_magazine_salvo_remounts(
    source_path: Any,
    logger_: Any,
    game_db: Dict[str, Any],
) -> None:
    """Remount in-scope squad AT/AA to magazine variants and set Salves to 1.

    Also remaps ``light_at`` mounts to ``LIGHT_AT_AMMO[strength]`` magazine
    variants (Salves stay 1).

    Mounts that share ``AmmoBoxIndex`` are remounted to the same magazine
    length so GenerateMod's ``ShotsCountPerSalvo`` check passes.
    """
    ammo_db = game_db.get("ammunition") or {}
    data = ammo_db.get("infantry_at_aa_magazine_salvos") or {}
    remounts = data.get("remounts") or []
    if not remounts:
        logger_.debug("No infantry magazine remounts in game_db")
        return

    remount_lookup: Dict[Tuple[str, str, bool], Dict[str, Any]] = {}
    units: Set[str] = set()
    for row in remounts:
        unit = row["unit"]
        units.add(unit)
        remount_lookup[(unit, row["base_ammo"], bool(row.get("hagru")))] = row

    unit_db = game_db.get("unit_data") or {}
    renames = ammo_db.get("renames_old_new") or {}

    for unit_name in sorted(units):
        weapon_descr = source_path.by_namespace(
            f"WeaponDescriptor_{unit_name}",
            strict=False,
        )
        if not weapon_descr:
            logger_.debug("No weapon descriptor for infantry magazine remount: %s", unit_name)
            continue

        unit_info = unit_db.get(unit_name, {})
        try:
            strength_i = int(unit_info["strength"]) if unit_info.get("strength") is not None else None
        except (TypeError, ValueError):
            strength_i = None

        # Collect live mounts, grouped by AmmoBoxIndex (shared ammo pool).
        by_box: Dict[Optional[int], List[Dict[str, Any]]] = defaultdict(list)
        turret_list = weapon_descr.v.by_m("TurretDescriptorList")
        for turret in turret_list.v:
            if not is_valid_turret(turret.v):
                continue
            for mounted in turret.v.by_m("MountedWeaponDescriptorList").v:
                if not is_obj_type(mounted.v, "TMountedWeaponDescriptor"):
                    continue
                ammo_path = mounted.v.by_m("Ammunition").v
                if not isinstance(ammo_path, str) or not ammo_path.startswith(_AMMO_PREFIX):
                    continue
                ammo_name = ammo_path[len(_AMMO_PREFIX):]
                bare, is_hagru = split_hagru_base(strip_magazine_suffixes(ammo_name))
                bare = renames.get(bare, bare)
                category = _category_for_ammo(bare)

                salvo_index = None
                ammo_box = mounted.v.by_m("AmmoBoxIndex", False)
                if ammo_box is not None:
                    try:
                        salvo_index = int(str(ammo_box.v))
                    except (TypeError, ValueError):
                        salvo_index = None

                by_box[salvo_index].append({
                    "mounted": mounted,
                    "ammo_name": ammo_name,
                    "bare": bare,
                    "is_hagru": is_hagru,
                    "category": category,
                    "salvo_index": salvo_index,
                })

        for _box_idx, group in by_box.items():
            magazine_group = [
                e for e in group
                if e["category"] in INFANTRY_MAGAZINE_CATEGORIES
                or e["category"] == "light_at"
            ]
            if not magazine_group:
                continue

            length = _resolve_pool_length(
                magazine_group, remount_lookup, unit_name, strength_i,
            )
            if length is None or length <= 1:
                continue

            for entry in magazine_group:
                bare = entry["bare"]
                is_hagru = entry["is_hagru"]
                ammo_name = entry["ammo_name"]
                salvo_index = entry["salvo_index"]
                kind = magazine_suffix_kind(bare, length)
                new_ammo = magazine_ammo_name(bare, length, hagru=is_hagru)
                if is_hagru and "_HAGRU" not in new_ammo:
                    new_ammo = _hagru_variant_name(bare, length, kind)

                if ammo_name != new_ammo or parse_magazine_length(ammo_name) != length:
                    _remount_weapon(entry["mounted"], weapon_descr, new_ammo, salvo_index)
                    logger_.info(
                        "Infantry magazine remount %s: %s -> %s (shared ammo box)",
                        unit_name,
                        ammo_name,
                        new_ammo,
                    )
                elif salvo_index is not None:
                    _set_salves_at_index(weapon_descr, salvo_index, 1)
