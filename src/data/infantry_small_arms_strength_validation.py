"""Validate infantry squad small-arms quantity totals vs effective strength.

Ensures edited/new infantry squads have countable small-arms (SMGs, rifles,
shotguns, snipers, squad MGs) summing to strength. Excludes AT, smoke, satchel,
flamethrowers, MANPADs, and weapon teams detected by resolved loadout (zero
countable small arms, all mounts specialist / occupied / team_mg).

See ``docs/validation/infantry_small_arms_vs_strength.md``.

``WeaponDescriptor.turrets.MountedWeapons`` ``remove`` and ``Ammunition`` member
patches are applied (same order as the weapon-descriptor handler: before
``equipmentchanges.replace``). ``MountedWeapons.insert`` that adds ammo absent
from vanilla ``game_db["weapons"]`` may still be missed.

A rifle squad stripped of all small arms but retaining only AT mounts (all
``specialist``, zero ``countable``) is skipped as a weapon-team-shaped loadout.
Use ``INFANTRY_SMALL_ARMS_STRENGTH_SKIP_UNITS`` or fix the edit when intentional.
"""

from __future__ import annotations

import json
import re
from pathlib import Path
from typing import Any, Dict, List, Optional, Set, Tuple

from src.constants.new_units import NEW_UNITS
from src.constants.unit_edits import load_unit_edits
from src.constants.unit_edits.replace_schema import normalize_replace
from src.constants.weapons import ammunitions, missiles
from src.constants.weapons.standards.by_category import AA_CATEGORIES
from src.constants.weapons.vanilla_inst_modifications import (
    AMMUNITION_MISSILES_RENAMES,
    AMMUNITION_RENAMES,
)
from src.data.small_arms_quantity_validation import UNITS_SKIP_STRENGTH_VARIANTS
from src.utils.database_utils import ensure_db_directory
from src.utils.logging_utils import setup_logger

logger = setup_logger(__name__)

_SALVO_SUFFIX_RE = re.compile(r"(_x\d+|_salvolength\d+|_infmagazine\d+)$")
_NB_WEAPONS_RE = re.compile(r"NbWeapons\s*=\s*(\d+)")

MountRole = str

SMALL_ARMS_DAMAGE_FAMILIES: frozenset[str] = frozenset({
    "DamageFamily_sniper",
    "DamageFamily_sniper_double",
    "DamageFamily_sniper_triple",
    "DamageFamily_sa_intermediate",
    "DamageFamily_sa_full",
    "DamageFamily_12_7",
    "DamageFamily_14_5",
    "DamageFamily_fmballe",
})

EXCLUDED_AMMO_CATEGORIES: frozenset[str] = frozenset({
    "light_at",
    "medium_at",
    "heavy_at",
    "recoilless",
    "napalm",
    "fire",
    "AGL",
    "ATGM",
    *AA_CATEGORIES,
})

INFANTRY_SMALL_ARMS_STRENGTH_SKIP_UNITS: frozenset[str] = frozenset()

_EXCLUDED_MINMAX_CATEGORIES: frozenset[str] = frozenset({
    "MinMax_MMG_HMG",
    "MinMax_FLAME",
})

# Soldiers carrying these weapons do not also count a separate rifle toward strength.
_OCCUPIED_SLOT_MINMAX_CATEGORIES: frozenset[str] = frozenset({
    "MinMax_CanonAP",
    "MinMax_FLAME",
})

_WEAPON_TEAM_ROLES: frozenset[str] = frozenset({
    "team_mg",
    "occupied",
    "specialist",
})


def _strip_ammo_suffixes(ammo_name: str) -> str:
    base = re.sub(r"_strength\d+", "", ammo_name)
    base = _SALVO_SUFFIX_RE.sub("", base)
    return base


def _build_vanilla_ammo_rename_map() -> Dict[str, str]:
    return {
        old_name: new_name
        for old_name, new_name in (*AMMUNITION_RENAMES, *AMMUNITION_MISSILES_RENAMES)
    }


def _constants_weapon_category(weapon_name: str) -> Optional[str]:
    for (name, category, _, _), _data in {**ammunitions, **missiles}.items():
        if name == weapon_name:
            return category
    return None


def _is_excluded_weapon_name(weapon_name: str) -> bool:
    if weapon_name.startswith(("MMG_team_", "HMG_team_")):
        return True
    category = _constants_weapon_category(weapon_name)
    if category in EXCLUDED_AMMO_CATEGORIES:
        return True
    return False


def _vanilla_ammo_props(
    base_weapon: str,
    ammo_props: Dict[str, Any],
) -> Optional[Dict[str, Any]]:
    candidates = [base_weapon]
    if "_salvolength" in base_weapon:
        prefix, suffix = base_weapon.rsplit("_salvolength", 1)
        if suffix.isdigit():
            candidates.extend([f"{prefix}_x{suffix}", prefix])
    x_match = re.match(r"^(.+)_x(\d+)$", base_weapon)
    if x_match:
        candidates.append(f"{x_match.group(1)}_salvolength{x_match.group(2)}")
        candidates.append(x_match.group(1))

    seen: Set[str] = set()
    for name in candidates:
        if not name or name in seen:
            continue
        seen.add(name)
        entry = ammo_props.get(f"Ammo_{name}")
        if entry:
            return entry
    return None


def _classify_mount_role(
    base: str,
    countable: Set[str],
    game_db: Dict[str, Any],
) -> MountRole:
    if base in countable:
        return "countable"
    ammo_props = game_db.get("ammunition", {}).get("ammo_properties", {})
    props = _vanilla_ammo_props(base, ammo_props)
    if base.startswith(("MMG_team_", "HMG_team_")):
        return "team_mg"
    if props:
        minmax = props.get("MinMaxCategory")
        if minmax == "MinMax_MMG_HMG":
            return "team_mg"
        if minmax == "MinMax_CanonAP":
            return "occupied"
        if minmax == "MinMax_FLAME":
            return "occupied"
    if _is_excluded_weapon_name(base):
        return "specialist"
    return "unknown"


def _is_weapon_team_by_loadout(
    mounts_by_turret: Dict[int, List[Tuple[str, int]]],
    countable: Set[str],
    game_db: Dict[str, Any],
) -> bool:
    mounts = [m for turret_mounts in mounts_by_turret.values() for m in turret_mounts]
    if not mounts:
        return False
    roles = {_classify_mount_role(base, countable, game_db) for base, _ in mounts}
    if "countable" in roles:
        return False
    if "unknown" in roles:
        return False
    return roles <= _WEAPON_TEAM_ROLES


def _occupied_weapon_slots(
    mounts_by_turret: Dict[int, List[Tuple[str, int]]],
    game_db: Dict[str, Any],
) -> int:
    """Count soldiers whose primary weapon prevents also carrying a rifle."""
    ammo_props = game_db.get("ammunition", {}).get("ammo_properties", {})
    occupied = 0
    for turret_mounts in mounts_by_turret.values():
        canon_qty = 0
        flame_qty = 0
        for base, qty in turret_mounts:
            props = _vanilla_ammo_props(base, ammo_props)
            if not props:
                continue
            minmax = props.get("MinMaxCategory")
            if minmax == "MinMax_CanonAP":
                canon_qty = max(canon_qty, qty)
            elif minmax == "MinMax_FLAME":
                flame_qty += qty
        occupied += canon_qty + flame_qty
    return occupied


def build_countable_small_arms_weapons(game_db: Dict[str, Any]) -> Set[str]:
    """Build set of base weapon names that count toward infantry small-arms totals."""
    countable: Set[str] = set()
    ammo_props = game_db.get("ammunition", {}).get("ammo_properties", {})

    for (weapon_name, category, _donor, _is_new), _data in ammunitions.items():
        if category != "small_arms":
            continue
        if _is_excluded_weapon_name(weapon_name):
            continue
        props = _vanilla_ammo_props(weapon_name, ammo_props)
        if props and props.get("MinMaxCategory") in _EXCLUDED_MINMAX_CATEGORIES:
            continue
        countable.add(weapon_name)

    for ammo_key, props in ammo_props.items():
        if not ammo_key.startswith("Ammo_"):
            continue
        base = _strip_ammo_suffixes(ammo_key[5:])
        if base in countable or _is_excluded_weapon_name(base):
            continue
        if props.get("MinMaxCategory") in _EXCLUDED_MINMAX_CATEGORIES:
            continue
        if props.get("MinMaxCategory") == "MinMax_inf_sniper":
            countable.add(base)
            continue
        if props.get("Family") in SMALL_ARMS_DAMAGE_FAMILIES:
            countable.add(base)

    return countable


def save_countable_small_arms_weapons(
    weapons: Set[str],
    config: Dict[str, Any],
) -> None:
    db_path = Path(config["data_config"]["database_path"])
    constants_dir = db_path / "constants_precomputation"
    ensure_db_directory(str(constants_dir))
    out_file = constants_dir / "countable_small_arms_weapons.json"
    with open(out_file, "w") as f:
        json.dump({"countable_weapons": sorted(weapons)}, f, indent=2, sort_keys=True)
    logger.debug("Saved countable small arms weapons to %s", out_file)


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


def _default_quantity_for_weapon(
    weapon_name: str,
    game_db: Dict[str, Any],
    vanilla_renames: Dict[str, str],
    insert_templates: Optional[Dict[str, str]] = None,
) -> int:
    weapons_db = game_db.get("weapons", {})
    lookup_bases = {_strip_ammo_suffixes(weapon_name)}
    renamed = vanilla_renames.get(weapon_name)
    if renamed:
        lookup_bases.add(_strip_ammo_suffixes(renamed))

    for descr_data in weapons_db.values():
        for turret in descr_data.get("turrets", {}).values():
            for ammo_name, wdata in turret.get("weapons", {}).items():
                base = _strip_ammo_suffixes(ammo_name)
                effective = vanilla_renames.get(base, base)
                if effective in lookup_bases or base in lookup_bases:
                    return int(wdata.get("quantity", 1))

    if insert_templates and weapon_name in insert_templates:
        match = _NB_WEAPONS_RE.search(insert_templates[weapon_name])
        if match:
            return int(match.group(1))

    return 1


def _apply_vanilla_rename(base: str, vanilla_renames: Dict[str, str]) -> str:
    return vanilla_renames.get(base, base)


def resolve_infantry_mounts_by_turret(
    unit_name: str,
    edits: Optional[Dict[str, Any]],
    donor_name: Optional[str],
    game_db: Dict[str, Any],
    insert_templates: Optional[Dict[str, str]] = None,
) -> Dict[int, List[Tuple[str, int]]]:
    """Resolve post-edit (base_weapon, quantity) mounts grouped by turret index."""
    weapons_db = game_db.get("weapons", {})
    descriptor_name = _resolve_weapon_descriptor_name(unit_name, donor_name, weapons_db)
    if not descriptor_name:
        return {}

    vanilla_renames = _build_vanilla_ammo_rename_map()
    ammo_db = game_db.get("ammunition", {})
    renames_old_new = ammo_db.get("renames_old_new", {})

    mounts_by_turret: Dict[int, List[List[Any]]] = {}
    weapon_info = weapons_db.get(descriptor_name, {})
    for turret_key in sorted(weapon_info.get("turrets", {}).keys(), key=int):
        turret_idx = int(turret_key)
        turret = weapon_info["turrets"][turret_key]
        mounts_by_turret[turret_idx] = []
        for ammo_name, wdata in turret.get("weapons", {}).items():
            base = _strip_ammo_suffixes(ammo_name)
            base = _apply_vanilla_rename(base, vanilla_renames)
            mounts_by_turret[turret_idx].append([base, int(wdata.get("quantity", 1))])

    equipment_changes: Dict[str, Any] = {}
    turrets_edits: Dict[str, Any] = {}
    if edits:
        wd = edits.get("WeaponDescriptor", {})
        equipment_changes = wd.get("equipmentchanges", {})
        turrets_edits = wd.get("turrets", {})

    if isinstance(turrets_edits, dict):
        # Per-turret MountedWeapons edits run before whole-turret remove and
        # equipmentchanges.replace (matches unit_edits_weapondescriptor order).
        for turret_key, turret_edits in turrets_edits.items():
            if turret_key == "remove" or not isinstance(turret_edits, dict):
                continue
            try:
                turret_idx = int(turret_key)
            except (TypeError, ValueError):
                continue
            turret_mounts = mounts_by_turret.get(turret_idx)
            if turret_mounts is None:
                continue
            mw_edits = turret_edits.get("MountedWeapons")
            if not isinstance(mw_edits, dict):
                continue
            if "remove" in mw_edits:
                for weapon_index in sorted(
                    (int(i) for i in mw_edits["remove"]),
                    reverse=True,
                ):
                    if 0 <= weapon_index < len(turret_mounts):
                        turret_mounts.pop(weapon_index)
            for ammo_name, ammo_edits in mw_edits.items():
                if ammo_name in ("insert", "remove") or not isinstance(ammo_edits, dict):
                    continue
                new_ammo_raw = ammo_edits.get("Ammunition")
                if not isinstance(new_ammo_raw, str):
                    continue
                new_ammo = new_ammo_raw
                if new_ammo.startswith("$/GFX/Weapon/Ammo_"):
                    new_ammo = new_ammo[len("$/GFX/Weapon/Ammo_"):]
                new_ammo = _strip_ammo_suffixes(new_ammo)
                target = _strip_ammo_suffixes(str(ammo_name))
                for i, (base, qty) in enumerate(turret_mounts):
                    if base == target or renames_old_new.get(base, base) == target:
                        turret_mounts[i] = [new_ammo, qty]
                        break
        if "remove" in turrets_edits:
            for raw_idx in turrets_edits["remove"]:
                mounts_by_turret.pop(int(raw_idx), None)

    replace_specs = normalize_replace(equipment_changes.get("replace"))
    for spec in replace_specs:
        current = _strip_ammo_suffixes(spec.old_weapon)
        new_weapon = _strip_ammo_suffixes(spec.new_weapon)
        renamed_current = renames_old_new.get(current, current)
        for turret_idx in sorted(mounts_by_turret.keys()):
            turret_mounts = mounts_by_turret[turret_idx]
            replaced = False
            for i, (base, qty) in enumerate(turret_mounts):
                if base == current or base == renamed_current:
                    turret_mounts[i] = [new_weapon, qty]
                    replaced = True
                    break
            if replaced:
                break

    quantity_edits = equipment_changes.get("quantity", {})
    if quantity_edits:
        for turret_mounts in mounts_by_turret.values():
            for i, (base, _qty) in enumerate(turret_mounts):
                if base in quantity_edits:
                    turret_mounts[i][1] = int(quantity_edits[base])

    insert_list = equipment_changes.get("insert", [])
    insert_edits = equipment_changes.get("insert_edits", {})
    for item in insert_list:
        if not isinstance(item, (list, tuple)) or len(item) < 2:
            continue
        turret_idx = int(item[0])
        weapon_name = item[1]
        if not isinstance(weapon_name, str):
            continue

        qty = int(quantity_edits.get(weapon_name, _default_quantity_for_weapon(
            weapon_name, game_db, vanilla_renames, insert_templates,
        )))
        turret_edits = insert_edits.get(turret_idx) or insert_edits.get(str(turret_idx))
        if isinstance(turret_edits, dict) and "NbWeapons" in turret_edits:
            qty = int(turret_edits["NbWeapons"])

        mounts_by_turret.setdefault(turret_idx, []).append([
            _strip_ammo_suffixes(weapon_name),
            qty,
        ])

    return {
        turret_idx: [(base, qty) for base, qty in turret_mounts]
        for turret_idx, turret_mounts in sorted(mounts_by_turret.items())
    }


def resolve_infantry_mounts(
    unit_name: str,
    edits: Optional[Dict[str, Any]],
    donor_name: Optional[str],
    game_db: Dict[str, Any],
    insert_templates: Optional[Dict[str, str]] = None,
) -> List[Tuple[str, int]]:
    """Resolve post-edit (base_weapon, quantity) mounts for a unit (flat list)."""
    mounts_by_turret = resolve_infantry_mounts_by_turret(
        unit_name, edits, donor_name, game_db, insert_templates,
    )
    mounts: List[Tuple[str, int]] = []
    for turret_idx in sorted(mounts_by_turret.keys()):
        mounts.extend(mounts_by_turret[turret_idx])
    return mounts


def _is_infantry_squad(
    edits: Optional[Dict[str, Any]],
    unit_info: Dict[str, Any],
) -> bool:
    if edits:
        if edits.get("is_heavy_equipment"):
            return False
        if edits.get("is_ground_vehicle") and not edits.get("is_infantry", False):
            return False
        role = edits.get("UnitRole")
        if role in ("infantry", "hq_inf"):
            return True
        tagset = edits.get("TagSet", {})
        if isinstance(tagset, dict):
            tags = tagset.get("overwrite_all", [])
            if "Infanterie" in tags:
                return True
        if edits.get("is_infantry"):
            return True

    if unit_info:
        if unit_info.get("unit_role") in ("infantry", "hq_inf"):
            return True
        if "Infanterie" in unit_info.get("tags", []):
            return True
    return False


def _should_validate_unit(
    unit_name: str,
    unit_info: Dict[str, Any],
    edits: Optional[Dict[str, Any]],
) -> bool:
    if unit_name in UNITS_SKIP_STRENGTH_VARIANTS:
        return False
    if unit_name in INFANTRY_SMALL_ARMS_STRENGTH_SKIP_UNITS:
        return False
    return _is_infantry_squad(edits, unit_info)


def _resolve_strength(
    edits: Optional[Dict[str, Any]],
    unit_info: Dict[str, Any],
) -> Optional[int]:
    if edits and "strength" in edits:
        strength = edits["strength"]
        if isinstance(strength, (int, float)):
            return int(strength)
    if unit_info and unit_info.get("strength") is not None:
        try:
            return int(unit_info["strength"])
        except (TypeError, ValueError):
            pass
    return None


def _sum_countable_small_arms(
    mounts: List[Tuple[str, int]],
    countable: Set[str],
) -> Tuple[int, Dict[str, int]]:
    breakdown: Dict[str, int] = {}
    total = 0
    for base, qty in mounts:
        if base not in countable:
            continue
        breakdown[base] = breakdown.get(base, 0) + qty
        total += qty
    return total, breakdown


def _iter_validated_infantry_units(
    game_db: Dict[str, Any],
) -> List[Tuple[str, Dict[str, Any], Optional[Dict[str, Any]], Optional[str], str]]:
    unit_edits = load_unit_edits()
    unit_data = game_db.get("unit_data", {})
    results: List[Tuple[str, Dict[str, Any], Optional[Dict[str, Any]], Optional[str], str]] = []
    seen: Set[str] = set()

    for unit_name, edits in unit_edits.items():
        if unit_name.endswith("_reference"):
            continue
        unit_info = unit_data.get(unit_name, {})
        if not _should_validate_unit(unit_name, unit_info, edits):
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
        if not _should_validate_unit(new_name, unit_info, new_unit_data):
            continue
        results.append((new_name, unit_info, new_unit_data, donor_name, "NEW_UNITS"))
        seen.add(new_name)

    return results


def build_infantry_small_arms_balance(
    game_db: Dict[str, Any],
    countable: Optional[Set[str]] = None,
    insert_templates: Optional[Dict[str, str]] = None,
) -> Dict[str, Dict[str, Any]]:
    """Build per-unit small-arms totals vs strength for validated infantry."""
    if countable is None:
        countable = build_countable_small_arms_weapons(game_db)

    balance: Dict[str, Dict[str, Any]] = {}
    for unit_name, unit_info, edits, donor_name, source in _iter_validated_infantry_units(game_db):
        strength = _resolve_strength(edits, unit_info)
        if strength is None:
            logger.warning(
                "Infantry small arms validation: skipping %s (%s) — no strength",
                unit_name,
                source,
            )
            continue

        mounts_by_turret = resolve_infantry_mounts_by_turret(
            unit_name, edits, donor_name, game_db, insert_templates,
        )
        if not mounts_by_turret:
            logger.debug(
                "Infantry small arms validation: no mounts resolved for %s (%s)",
                unit_name,
                source,
            )
            continue

        if _is_weapon_team_by_loadout(mounts_by_turret, countable, game_db):
            mounts_flat = [
                m for turret_mounts in mounts_by_turret.values() for m in turret_mounts
            ]
            roles = sorted({
                _classify_mount_role(base, countable, game_db)
                for base, _ in mounts_flat
            })
            logger.debug(
                "Infantry small arms validation: skipping weapon team %s (%s) — roles %s",
                unit_name,
                source,
                roles,
            )
            continue

        mounts = [
            m for turret_idx in sorted(mounts_by_turret.keys())
            for m in mounts_by_turret[turret_idx]
        ]
        small_arms_total, breakdown = _sum_countable_small_arms(mounts, countable)
        occupied_slots = _occupied_weapon_slots(mounts_by_turret, game_db)
        expected_small_arms = strength - occupied_slots
        balance[unit_name] = {
            "strength": strength,
            "expected_small_arms": expected_small_arms,
            "occupied_slots": occupied_slots,
            "small_arms_total": small_arms_total,
            "breakdown": breakdown,
            "source": source,
        }

    return balance


def save_infantry_small_arms_balance(
    balance: Dict[str, Dict[str, Any]],
    config: Dict[str, Any],
) -> None:
    db_path = Path(config["data_config"]["database_path"])
    constants_dir = db_path / "constants_precomputation"
    ensure_db_directory(str(constants_dir))
    out_file = constants_dir / "infantry_small_arms_balance.json"
    with open(out_file, "w") as f:
        json.dump(balance, f, indent=2, sort_keys=True)
    logger.debug("Saved infantry small arms balance to %s", out_file)


def validate_infantry_small_arms_vs_strength(
    game_db: Dict[str, Any],
    balance: Optional[Dict[str, Dict[str, Any]]] = None,
) -> bool:
    """Validate small-arms totals match strength. Returns True if any errors found."""
    if balance is None:
        balance = build_infantry_small_arms_balance(game_db)

    errors: List[str] = []
    for unit_name, entry in balance.items():
        strength = entry.get("strength")
        total = entry.get("small_arms_total")
        expected = entry.get("expected_small_arms")
        if strength is None or total is None or expected is None:
            continue
        if total != expected:
            breakdown = entry.get("breakdown", {})
            breakdown_str = ", ".join(f"{k}:{v}" for k, v in sorted(breakdown.items()))
            source = entry.get("source", "unknown")
            occupied = entry.get("occupied_slots", 0)
            occupied_note = f", occupied_slots={occupied}" if occupied else ""
            errors.append(
                f"[{source}] {unit_name}: small arms total {total} != "
                f"expected {expected} (strength {strength}{occupied_note}) "
                f"({breakdown_str})",
            )

    if errors:
        for err in errors:
            logger.error("Infantry small arms vs strength: %s", err)
        logger.error(
            "Found %s infantry small arms vs strength mismatch(es). "
            "Fix unit edits / NEW_UNITS quantities or add to "
            "INFANTRY_SMALL_ARMS_STRENGTH_SKIP_UNITS if intentional.",
            len(errors),
        )
        return True
    return False
