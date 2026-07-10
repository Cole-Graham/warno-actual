"""Infantry squad AT/AA magazine-style salvolength precompute and helpers.

Organic rifle squads mount AT/AA as 1-shot salvos with stock in ``Salves``.
Veterancy multiplies ``TimeBetweenTwoSalvos``, which speeds those weapons.
Magazine variants put all ammo in one salvo (``ShotsCountPerSalvo = N``) so RoF
is governed by ``TimeBetweenTwoShots`` instead.

Dedicated weapon teams (no countable small arms) are excluded.
"""

from __future__ import annotations

import json
import re
from pathlib import Path
from typing import Any, Dict, List, Mapping, Optional, Set, Tuple

from src.constants.new_units import NEW_UNITS
from src.constants.unit_edits import load_unit_edits
from src.constants.weapons import LIGHT_AT_AMMO, ammunitions, missiles
from src.data.infantry_small_arms_strength_validation import (
    _is_infantry_squad,
    _is_weapon_team_by_loadout,
    _resolve_strength,
    _strip_ammo_suffixes,
    build_countable_small_arms_weapons,
    resolve_infantry_mounts_by_turret,
)
from src.utils.database_utils import ensure_db_directory
from src.utils.logging_utils import setup_logger

logger = setup_logger(__name__)

INFANTRY_MAGAZINE_CATEGORIES: frozenset[str] = frozenset({
    "light_at",
    "medium_at",
    "heavy_at",
    "recoilless",
    "ATGM",
    "MANPAD",
    "napalm",
})

_MAGAZINE_SUFFIX_RE = re.compile(r"_(?:salvolength|infmagazine)(\d+)$")
_HAGRU_RE = re.compile(r"_HAGRU(?:_salvolength\d+|_infmagazine\d+)?$")


_DEDICATED_TEAM_PREFIXES: tuple[str, ...] = (
    "ATteam_",
    "HMGteam_",
    "MMGteam_",
)


def is_dedicated_weapon_team_unit(unit_name: str) -> bool:
    """True for dedicated ATGM/MANPAD/HMG teams (even if they carry escort rifles).

    ``MANPAD_*_Rifles_*`` organic rifle+MANPAD squads are not dedicated teams.
    """
    if unit_name.startswith(_DEDICATED_TEAM_PREFIXES):
        return True
    if unit_name.startswith("MANPAD_") and "Rifles" not in unit_name:
        return True
    return False


def strip_magazine_suffixes(ammo_name: str) -> str:
    """Strip strength / quantity / magazine suffixes; keep ``_HAGRU`` when present."""
    base = re.sub(r"_strength\d+", "", ammo_name)
    base = re.sub(r"_x\d+$", "", base)
    base = _MAGAZINE_SUFFIX_RE.sub("", base)
    return base


def parse_magazine_length(ammo_name: str) -> Optional[int]:
    match = _MAGAZINE_SUFFIX_RE.search(ammo_name)
    if not match:
        return None
    return int(match.group(1))


def split_hagru_base(ammo_name: str) -> Tuple[str, bool]:
    """Return (base without HAGRU/magazine suffixes, is_hagru)."""
    stripped = strip_magazine_suffixes(ammo_name)
    if stripped.endswith("_HAGRU"):
        return stripped[: -len("_HAGRU")], True
    return stripped, False


def _ammo_category(weapon_name: str) -> Optional[str]:
    base, _ = split_hagru_base(weapon_name)
    for (name, category, _, _), _data in {**ammunitions, **missiles}.items():
        if name == base or name == weapon_name:
            return category
    return None


def is_infantry_magazine_category(weapon_name: str) -> bool:
    category = _ammo_category(weapon_name)
    return category in INFANTRY_MAGAZINE_CATEGORIES


def shared_salvo_index_companions(
    unit_name: str,
    ammo_base: str,
    game_db: Dict[str, Any],
    donor_name: Optional[str] = None,
) -> Set[str]:
    """Bare ammo names that share an AmmoBoxIndex / salvo_index with ``ammo_base``.

    WARNO requires every mount on the same ammo box to use the same
    ``ShotsCountPerSalvo``. AP/HE recoilless pairs (and similar dual mounts)
    are discovered via ``weapons_db`` ``salvo_mapping``, not name heuristics.
    """
    from src.data.infantry_small_arms_strength_validation import (
        _apply_vanilla_rename,
        _build_vanilla_ammo_rename_map,
    )

    bare, _ = split_hagru_base(strip_magazine_suffixes(ammo_base))
    renames = game_db.get("ammunition", {}).get("renames_old_new", {})
    vanilla_renames = _build_vanilla_ammo_rename_map()
    bare = renames.get(bare, bare)
    bare = _apply_vanilla_rename(bare, vanilla_renames)

    weapons_db = game_db.get("weapons", {})
    descr_names = [f"WeaponDescriptor_{unit_name}"]
    if donor_name:
        descr_names.append(f"WeaponDescriptor_{donor_name}")

    for descr_name in descr_names:
        info = weapons_db.get(descr_name) or {}
        mapping = info.get("salvo_mapping") or {}
        if not mapping:
            continue

        indices_by_bare: Dict[str, Set[int]] = {}
        for key, idxs in mapping.items():
            key_bare, _ = split_hagru_base(strip_magazine_suffixes(str(key)))
            key_bare = renames.get(key_bare, key_bare)
            key_bare = _apply_vanilla_rename(key_bare, vanilla_renames)
            try:
                indices_by_bare.setdefault(key_bare, set()).update(int(i) for i in idxs)
            except (TypeError, ValueError):
                continue

        target_indices = indices_by_bare.get(bare)
        if not target_indices:
            # Caller may still use the pre-rename name
            for old_name, new_name in vanilla_renames.items():
                if new_name == bare and old_name in indices_by_bare:
                    target_indices = indices_by_bare[old_name]
                    break
        if not target_indices:
            continue

        companions = {
            key_bare
            for key_bare, idxs in indices_by_bare.items()
            if idxs & target_indices
        }
        if companions:
            return companions

    return {bare}


def unify_shared_pool_magazine_length(lengths: List[int]) -> Optional[int]:
    """Pick one magazine length for every mount on a shared ammo box.

    Uses the max resolved length so a Salves override on one sibling and a
    vanilla salves count on another still converge (GenerateMod requires
    identical ``ShotsCountPerSalvo`` on the box).
    """
    valid = [n for n in lengths if isinstance(n, int) and n > 1]
    if not valid:
        return None
    return max(valid)


def existing_vehicle_salvo_lengths(weapon_name: str) -> Set[int]:
    """SalvoLengths already owned by vehicle/missile dict entries for this weapon."""
    base, _ = split_hagru_base(weapon_name)
    lengths: Set[int] = set()
    for (name, _category, _donor, _is_new), data in missiles.items():
        if name != base and name != f"{base}_HAGRU":
            continue
        wd = data.get("WeaponDescriptor") or {}
        for length in wd.get("SalvoLengths") or []:
            try:
                lengths.add(int(length))
            except (TypeError, ValueError):
                continue
    return lengths


def magazine_suffix_kind(weapon_name: str, length: int) -> str:
    """Return ``salvolength`` or ``infmagazine`` based on vehicle SalvoLengths collision."""
    if length in existing_vehicle_salvo_lengths(weapon_name):
        return "infmagazine"
    return "salvolength"


def magazine_ammo_name(weapon_name: str, length: int, *, hagru: bool = False) -> str:
    """Build mount/ammo name for an infantry magazine variant."""
    base, was_hagru = split_hagru_base(weapon_name)
    use_hagru = hagru or was_hagru
    kind = magazine_suffix_kind(base, length)
    stem = f"{base}_HAGRU" if use_hagru else base
    return f"{stem}_{kind}{length}"


def _category_lookup() -> Dict[str, str]:
    out: Dict[str, str] = {}
    for (name, category, _, _), _ in {**ammunitions, **missiles}.items():
        out[name] = category
    return out


def _salves_override_for_ammo(
    edits: Optional[Dict[str, Any]],
    ammo_base: str,
    companion_bares: Optional[Set[str]] = None,
) -> Optional[int]:
    """Return magazine length N for ammo from unit-edit Salves / replace.

    After constants rewrite, Salves keys are often ``Ammo_salvolength{N}: 1``.
    Prefer N from the magazine suffix on the key (or replace ``new_weapon``)
    over the integer value when that value is ``1``.

    ``companion_bares`` are other ammo names on the same AmmoBoxIndex; Salves
    authored for any sibling apply to the whole pool.
    """
    if not edits:
        return None
    wd = edits.get("WeaponDescriptor") or {}
    bare, _ = split_hagru_base(strip_magazine_suffixes(ammo_base))
    bares = {bare}
    if companion_bares:
        bares.update(companion_bares)

    # Prefer explicit magazine suffix on Salves keys / replace targets
    lengths: List[int] = []
    salves = wd.get("Salves")
    if isinstance(salves, dict):
        for key, val in salves.items():
            if key in ("insert", "remove"):
                continue
            key_s = str(key)
            key_bare, _ = split_hagru_base(strip_magazine_suffixes(key_s))
            if key_bare not in bares:
                continue
            parsed = parse_magazine_length(key_s)
            if parsed is not None and parsed > 1:
                lengths.append(parsed)
                continue
            try:
                n = int(val[0]) if isinstance(val, (list, tuple)) and val else int(val)
            except (TypeError, ValueError):
                continue
            if n > 1:
                lengths.append(n)

    from src.constants.unit_edits.replace_schema import normalize_replace

    for spec in normalize_replace((wd.get("equipmentchanges") or {}).get("replace")):
        new_bare, _ = split_hagru_base(strip_magazine_suffixes(spec.new_weapon))
        old_bare, _ = split_hagru_base(strip_magazine_suffixes(spec.old_weapon))
        if new_bare not in bares and old_bare not in bares:
            continue
        parsed = parse_magazine_length(spec.new_weapon)
        if parsed is not None and parsed > 1:
            lengths.append(parsed)

    # Also scan raw replace dict/list for magazine names normalize_replace may skip
    raw_replace = (wd.get("equipmentchanges") or {}).get("replace")
    if isinstance(raw_replace, dict):
        for old_w, payload in raw_replace.items():
            candidates = [str(old_w)]
            if isinstance(payload, str):
                candidates.append(payload)
            elif isinstance(payload, Mapping):
                nw = payload.get("new_weapon")
                if isinstance(nw, str):
                    candidates.append(nw)
            elif isinstance(payload, list):
                for item in payload:
                    if isinstance(item, Mapping):
                        nw = item.get("new_weapon")
                        if isinstance(nw, str):
                            candidates.append(nw)
            for cand in candidates:
                cand_bare, _ = split_hagru_base(strip_magazine_suffixes(cand))
                if cand_bare not in bares:
                    continue
                parsed = parse_magazine_length(cand)
                if parsed is not None and parsed > 1:
                    lengths.append(parsed)
    elif isinstance(raw_replace, list):
        for item in raw_replace:
            if isinstance(item, (list, tuple)) and len(item) >= 2:
                for cand in (str(item[0]), str(item[1])):
                    cand_bare, _ = split_hagru_base(strip_magazine_suffixes(cand))
                    if cand_bare not in bares:
                        continue
                    parsed = parse_magazine_length(cand)
                    if parsed is not None and parsed > 1:
                        lengths.append(parsed)

    if lengths:
        return max(lengths)
    return None


def _vanilla_salves_for_ammo(
    unit_name: str,
    donor_name: Optional[str],
    ammo_base: str,
    game_db: Dict[str, Any],
) -> Optional[int]:
    from src.data.infantry_small_arms_strength_validation import (
        _apply_vanilla_rename,
        _build_vanilla_ammo_rename_map,
    )

    weapons_db = game_db.get("weapons", {})
    descr_names = [f"WeaponDescriptor_{unit_name}"]
    if donor_name:
        descr_names.append(f"WeaponDescriptor_{donor_name}")

    bare, _ = split_hagru_base(strip_magazine_suffixes(ammo_base))
    vanilla_renames = _build_vanilla_ammo_rename_map()
    renames_old_new = game_db.get("ammunition", {}).get("renames_old_new", {})
    renames_new_old = game_db.get("ammunition", {}).get("renames_new_old", {})

    # Match both post-rename names (constants) and pre-rename vanilla mount keys
    # (e.g. ATGM_9K115_Metis_M -> ATGM_9K115_Metis).
    ammo_targets = {
        ammo_base,
        bare,
        strip_magazine_suffixes(ammo_base),
        renames_old_new.get(bare, bare),
        renames_new_old.get(bare, bare),
        _apply_vanilla_rename(bare, vanilla_renames),
    }
    for old_name, new_name in vanilla_renames.items():
        if new_name == bare or old_name == bare:
            ammo_targets.add(old_name)
            ammo_targets.add(new_name)

    for descr_name in descr_names:
        info = weapons_db.get(descr_name)
        if not info:
            continue
        for turret in info.get("turrets", {}).values():
            for mount_name, wdata in turret.get("weapons", {}).items():
                mount_base = strip_magazine_suffixes(mount_name)
                mount_candidates = {
                    mount_base,
                    renames_old_new.get(mount_base, mount_base),
                    _apply_vanilla_rename(mount_base, vanilla_renames),
                    split_hagru_base(mount_base)[0],
                }
                if mount_candidates & ammo_targets:
                    try:
                        return int(wdata.get("salves"))
                    except (TypeError, ValueError):
                        continue
        # Fallback via salvo_mapping + salves_list
        mapping = info.get("salvo_mapping") or {}
        salves_list = info.get("salves_list") or []
        for key, indices in mapping.items():
            key_base = strip_magazine_suffixes(key)
            key_candidates = {
                key_base,
                renames_old_new.get(key_base, key_base),
                _apply_vanilla_rename(key_base, vanilla_renames),
                split_hagru_base(key_base)[0],
            }
            if not (key_candidates & ammo_targets):
                continue
            for idx in indices:
                try:
                    return int(salves_list[int(idx)])
                except (TypeError, ValueError, IndexError):
                    continue
    return None


def resolve_magazine_length(
    unit_name: str,
    ammo_base: str,
    edits: Optional[Dict[str, Any]],
    unit_info: Dict[str, Any],
    donor_name: Optional[str],
    game_db: Dict[str, Any],
    category: str,
    companion_bares: Optional[Set[str]] = None,
) -> Optional[int]:
    """Resolve final magazine length N for an in-scope mount."""
    existing = parse_magazine_length(ammo_base)
    if existing is not None:
        return existing

    if companion_bares is None:
        companion_bares = shared_salvo_index_companions(
            unit_name, ammo_base, game_db, donor_name,
        )

    override = _salves_override_for_ammo(edits, ammo_base, companion_bares)
    if override is not None:
        return override

    if category == "light_at":
        strength = _resolve_strength(edits, unit_info)
        if strength is not None and strength in LIGHT_AT_AMMO:
            return int(LIGHT_AT_AMMO[strength])

    vanilla = _vanilla_salves_for_ammo(unit_name, donor_name, ammo_base, game_db)
    return vanilla


def _iter_infantry_squad_units(
    game_db: Dict[str, Any],
) -> List[Tuple[str, Dict[str, Any], Optional[Dict[str, Any]], Optional[str], str]]:
    """Infantry squads from unit_edits, NEW_UNITS, and vanilla unit_data."""
    unit_edits = load_unit_edits()
    unit_data = game_db.get("unit_data", {})
    results: List[Tuple[str, Dict[str, Any], Optional[Dict[str, Any]], Optional[str], str]] = []
    seen: Set[str] = set()

    for unit_name, edits in unit_edits.items():
        if unit_name.endswith("_reference"):
            continue
        unit_info = unit_data.get(unit_name, {})
        if not _is_infantry_squad(edits, unit_info):
            continue
        if is_dedicated_weapon_team_unit(unit_name):
            continue
        results.append((unit_name, unit_info, edits, None, "unit_edits"))
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
        unit_info = unit_data.get(new_name) or unit_data.get(donor_name, {})
        if not _is_infantry_squad(new_unit_data, unit_info):
            continue
        if is_dedicated_weapon_team_unit(new_name):
            continue
        results.append((new_name, unit_info, new_unit_data, donor_name, "NEW_UNITS"))
        seen.add(new_name)

    for unit_name, unit_info in unit_data.items():
        if unit_name in seen or unit_name == "all_tags":
            continue
        if not isinstance(unit_info, dict):
            continue
        if not _is_infantry_squad(None, unit_info):
            continue
        if is_dedicated_weapon_team_unit(unit_name):
            continue
        results.append((unit_name, unit_info, None, None, "vanilla"))
        seen.add(unit_name)

    return results


def _register_variant(
    variants: Dict[str, Dict[int, str]],
    weapon_name: str,
    length: int,
) -> None:
    if length <= 1:
        return
    bare, is_hagru = split_hagru_base(weapon_name)
    if not is_infantry_magazine_category(bare):
        return
    kind = magazine_suffix_kind(bare, length)
    variants.setdefault(bare, {})[length] = kind
    if is_hagru:
        variants.setdefault(f"{bare}_HAGRU", {})[length] = kind


def _iter_magazine_names_from_edits(edits: Optional[Dict[str, Any]]) -> List[str]:
    """Collect ammo names that already carry magazine suffixes from unit edits."""
    if not edits:
        return []
    wd = edits.get("WeaponDescriptor") or {}
    names: List[str] = []

    salves = wd.get("Salves")
    if isinstance(salves, dict):
        for key in salves:
            if key in ("insert", "remove"):
                continue
            if parse_magazine_length(str(key)) is not None:
                names.append(str(key))

    raw_replace = (wd.get("equipmentchanges") or {}).get("replace")
    if isinstance(raw_replace, dict):
        for old_w, payload in raw_replace.items():
            candidates = [str(old_w)]
            if isinstance(payload, str):
                candidates.append(payload)
            elif isinstance(payload, Mapping):
                nw = payload.get("new_weapon")
                if isinstance(nw, str):
                    candidates.append(nw)
            elif isinstance(payload, list):
                for item in payload:
                    if isinstance(item, Mapping):
                        nw = item.get("new_weapon")
                        if isinstance(nw, str):
                            candidates.append(nw)
                    elif isinstance(item, (list, tuple)) and len(item) >= 2:
                        candidates.extend([str(item[0]), str(item[1])])
            for cand in candidates:
                if parse_magazine_length(cand) is not None:
                    names.append(cand)
    elif isinstance(raw_replace, list):
        for item in raw_replace:
            if isinstance(item, (list, tuple)) and len(item) >= 2:
                for cand in (str(item[0]), str(item[1])):
                    if parse_magazine_length(cand) is not None:
                        names.append(cand)
            elif isinstance(item, Mapping):
                for key in ("old_weapon", "new_weapon"):
                    val = item.get(key)
                    if isinstance(val, str) and parse_magazine_length(val) is not None:
                        names.append(val)

    return names


def _harvest_magazine_variants_from_constants(
    variants: Dict[str, Dict[int, str]],
) -> None:
    """Ensure every authored ``*_salvolength{N}`` / ``*_infmagazine{N}`` is creatable."""
    unit_edits = load_unit_edits()
    for unit_name, edits in unit_edits.items():
        if unit_name.endswith("_reference"):
            continue
        for name in _iter_magazine_names_from_edits(edits):
            length = parse_magazine_length(name)
            if length is None:
                continue
            _register_variant(variants, strip_magazine_suffixes(name), length)

    for _neu_key, new_unit_data in NEW_UNITS.items():
        if not isinstance(new_unit_data, dict):
            continue
        for name in _iter_magazine_names_from_edits(new_unit_data):
            length = parse_magazine_length(name)
            if length is None:
                continue
            _register_variant(variants, strip_magazine_suffixes(name), length)


def _ensure_hagru_magazine_twins(variants: Dict[str, Dict[int, str]]) -> None:
    """Register ``Weapon_HAGRU`` magazine lengths whenever base MANPAD/ATGM has them.

    Runtime HAGRU attachment clones the donor mount's magazine suffix onto
    ``*_HAGRU_salvolength{N}`` / ``*_infmagazine{N}``, so those ammo descriptors
    must exist even when no unit mounts HAGRU during precompute.
    """
    missile_names = {name for (name, _, _, _), _ in missiles.items()}
    for weapon, length_map in list(variants.items()):
        bare, is_hagru = split_hagru_base(weapon)
        if is_hagru:
            continue
        hagru_name = f"{bare}_HAGRU"
        if hagru_name not in missile_names:
            continue
        for length, kind in length_map.items():
            variants.setdefault(hagru_name, {})[length] = kind


def build_infantry_at_aa_magazine_salvos(
    game_db: Dict[str, Any],
    countable: Optional[Set[str]] = None,
    insert_templates: Optional[Dict[str, str]] = None,
) -> Dict[str, Any]:
    """Build magazine-variant inventory and per-unit remount plan.

    Returns::

        {
            "variants_by_weapon": {
                "RocketInf_RPG7VL": [{"length": 6, "kind": "salvolength"}, ...],
            },
            "remounts": [
                {
                    "unit": "...",
                    "base_ammo": "RocketInf_RPG7VL",
                    "length": 6,
                    "kind": "salvolength",
                    "variant_ammo": "RocketInf_RPG7VL_salvolength6",
                    "hagru": False,
                    "source": "unit_edits",
                },
                ...
            ],
        }
    """
    if countable is None:
        countable = build_countable_small_arms_weapons(game_db)

    categories = _category_lookup()
    variants: Dict[str, Dict[int, str]] = {}
    remounts: List[Dict[str, Any]] = []
    remount_keys: Set[Tuple[str, str, int, bool]] = set()

    for unit_name, unit_info, edits, donor_name, source in _iter_infantry_squad_units(game_db):
        mounts_by_turret = resolve_infantry_mounts_by_turret(
            unit_name, edits, donor_name, game_db, insert_templates,
        )
        if not mounts_by_turret:
            continue
        if _is_weapon_team_by_loadout(mounts_by_turret, countable, game_db):
            continue

        # Collect magazine-category candidates, then unify lengths across any
        # mounts that share an AmmoBoxIndex / salvo_index.
        candidates: List[Dict[str, Any]] = []
        for _turret_idx, mounts in mounts_by_turret.items():
            for ammo_name, _qty in mounts:
                base_no_suffix = strip_magazine_suffixes(ammo_name)
                bare, is_hagru = split_hagru_base(base_no_suffix)
                category = categories.get(bare) or categories.get(base_no_suffix)
                if category not in INFANTRY_MAGAZINE_CATEGORIES:
                    continue
                companions = shared_salvo_index_companions(
                    unit_name, bare, game_db, donor_name,
                )
                length = resolve_magazine_length(
                    unit_name,
                    ammo_name if parse_magazine_length(ammo_name) else bare,
                    edits,
                    unit_info,
                    donor_name,
                    game_db,
                    category,
                    companions,
                )
                candidates.append({
                    "bare": bare,
                    "is_hagru": is_hagru,
                    "category": category,
                    "companions": frozenset(companions),
                    "length": length,
                })

        # Unify: every member of a shared pool gets max(resolved lengths)
        pool_length: Dict[frozenset[str], Optional[int]] = {}
        for cand in candidates:
            key = cand["companions"]
            lengths = [
                c["length"] for c in candidates
                if c["companions"] == key and c["length"] is not None
            ]
            pool_length[key] = unify_shared_pool_magazine_length(
                [int(n) for n in lengths if n is not None],
            )

        for cand in candidates:
            length = pool_length.get(cand["companions"])
            if length is None or length <= 1:
                continue
            bare = cand["bare"]
            is_hagru = cand["is_hagru"]
            category = cand["category"]
            kind = magazine_suffix_kind(bare, length)
            variant = magazine_ammo_name(bare, length, hagru=is_hagru)
            variants.setdefault(bare, {})[length] = kind
            if is_hagru:
                variants.setdefault(f"{bare}_HAGRU", {})[length] = kind
            # Ensure every shared-pool sibling gets a creatable magazine variant
            for companion in cand["companions"]:
                if companion == bare:
                    continue
                if categories.get(companion) not in INFANTRY_MAGAZINE_CATEGORIES:
                    continue
                variants.setdefault(companion, {})[length] = magazine_suffix_kind(
                    companion, length,
                )

            key = (unit_name, bare, length, is_hagru)
            if key in remount_keys:
                continue
            remount_keys.add(key)
            remounts.append({
                "unit": unit_name,
                "base_ammo": bare,
                "length": length,
                "kind": kind,
                "variant_ammo": variant,
                "hagru": is_hagru,
                "source": source,
                "category": category,
                "shared_pool": sorted(cand["companions"]),
            })

    _harvest_magazine_variants_from_constants(variants)
    _ensure_hagru_magazine_twins(variants)

    variants_by_weapon = {
        weapon: [
            {"length": length, "kind": kind}
            for length, kind in sorted(length_map.items())
        ]
        for weapon, length_map in sorted(variants.items())
    }

    # Ensure light_at weapons also get every LIGHT_AT_AMMO length used by squads
    for (weapon_name, category, _, _), _ in ammunitions.items():
        if category != "light_at":
            continue
        for length in sorted(set(LIGHT_AT_AMMO.values())):
            if length <= 1:
                continue
            kind = magazine_suffix_kind(weapon_name, length)
            variants_by_weapon.setdefault(weapon_name, [])
            existing_lengths = {entry["length"] for entry in variants_by_weapon[weapon_name]}
            if length not in existing_lengths:
                variants_by_weapon[weapon_name].append({"length": length, "kind": kind})
                variants_by_weapon[weapon_name].sort(key=lambda e: e["length"])

    logger.info(
        "Built infantry AT/AA magazine salvos: %s weapons, %s remounts",
        len(variants_by_weapon),
        len(remounts),
    )
    return {
        "variants_by_weapon": variants_by_weapon,
        "remounts": remounts,
    }


def save_infantry_at_aa_magazine_salvos(data: Dict[str, Any], config: Dict[str, Any]) -> None:
    db_path = Path(config["data_config"]["database_path"])
    constants_dir = db_path / "constants_precomputation"
    ensure_db_directory(str(constants_dir))
    out_file = constants_dir / "infantry_at_aa_magazine_salvos.json"
    try:
        with open(out_file, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2, sort_keys=True)
        logger.debug("Saved infantry_at_aa_magazine_salvos to %s", out_file)
    except Exception as e:
        logger.error("Failed to save infantry_at_aa_magazine_salvos: %s", e)
        raise
