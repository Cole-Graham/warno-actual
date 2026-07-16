"""Set strength on dedicated ATGM infantry teams from equip specialty."""

from __future__ import annotations

import re
from typing import Any, Dict, Optional, Set

from src.constants.new_units import NEW_UNITS
from src.constants.unit_edits import load_unit_edits
from src.constants.unit_edits.replace_schema import normalize_replace
from src.constants.unit_edits.standards import (
    ATGM_INFANTRY_TEAM_STRENGTH_PATTERN_STANDARD,
)
from src.constants.weapons.vanilla_inst_modifications import (
    AMMUNITION_MISSILES_RENAMES,
    AMMUNITION_RENAMES,
)
from src.utils.ndf_utils import find_obj_by_type, strip_quotes

_SALVO_SUFFIX_RE = re.compile(r"(_x\d+|_salvolength\d+|_infmagazine\d+)$")
_SKIP_SOLDIER_COUNT = frozenset({"KdA_DDR_TargetDummy"})

_ARMOR_PARTS = (
    "ResistanceFront",
    "ResistanceSides",
    "ResistanceRear",
    "ResistanceTop",
)


def _build_vanilla_ammo_rename_maps() -> tuple[Dict[str, str], Dict[str, str]]:
    forward = {
        old_name: new_name
        for old_name, new_name in (*AMMUNITION_RENAMES, *AMMUNITION_MISSILES_RENAMES)
    }
    reverse = {new_name: old_name for old_name, new_name in forward.items()}
    return forward, reverse


def _build_unit_replace_map(edits: Optional[Dict[str, Any]]) -> Dict[str, str]:
    if not edits:
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


def _new_unit_edits_by_name() -> Dict[str, Dict[str, Any]]:
    by_name: Dict[str, Dict[str, Any]] = {}
    for donor_key, edits in NEW_UNITS.items():
        if not isinstance(edits, dict):
            continue
        new_name = edits.get("NewName")
        if not new_name:
            continue
        by_name[new_name] = {
            "edits": edits,
            "donor": donor_key[0] if isinstance(donor_key, tuple) else None,
        }
    return by_name


def _units_with_explicit_strength(
    unit_edits: Dict[str, Any],
    new_units_by_name: Dict[str, Dict[str, Any]],
) -> Set[str]:
    explicit: Set[str] = set()
    for unit_name, edits in unit_edits.items():
        if isinstance(edits, dict) and "strength" in edits:
            explicit.add(unit_name)
    for unit_name, meta in new_units_by_name.items():
        if "strength" in meta["edits"]:
            explicit.add(unit_name)
    return explicit


def is_at_team_unit(unit_name: str, unit_data: Optional[Dict[str, Any]]) -> bool:
    """Dedicated AT team by DB flag or ATteam_/Atteam_ name prefix."""
    if unit_data and unit_data.get("is_at_team"):
        return True
    return "atteam" in unit_name.lower()


def resolve_strength_for_specialties(
    specialties: Any,
    std: Optional[Dict[str, Any]] = None,
) -> int:
    """Return 4 if infantry_equip_veryheavy is present, else 3."""
    rule = std or ATGM_INFANTRY_TEAM_STRENGTH_PATTERN_STANDARD
    veryheavy = rule["veryheavy_specialty"]
    for tag in specialties.v:
        if strip_quotes(tag.v) == veryheavy:
            return rule["veryheavy_strength"]
    return rule["default_strength"]


def _type_category_token(
    ammo_props: Dict[str, Any],
    weapon_name: str,
    reverse_renames: Dict[str, str],
) -> Optional[str]:
    candidates = [weapon_name]
    prior = reverse_renames.get(weapon_name)
    if prior and prior not in candidates:
        candidates.append(prior)
    for name in candidates:
        for key in (f"Ammo_{name}", name):
            props = ammo_props.get(key)
            if not props:
                continue
            tcn = props.get("TypeCategoryName")
            if isinstance(tcn, dict):
                token = tcn.get("Token")
                if token:
                    return strip_quotes(str(token))
            elif isinstance(tcn, str) and tcn:
                return strip_quotes(tcn)
    return None


def unit_has_anti_tank_missile_mount(
    unit_name: str,
    game_db: Dict[str, Any],
    edits: Optional[Dict[str, Any]] = None,
    donor_name: Optional[str] = None,
    type_category_token: Optional[str] = None,
) -> bool:
    """True when a resolved mount has TypeCategoryName ANTI-TANK MISSILE."""
    token = type_category_token or ATGM_INFANTRY_TEAM_STRENGTH_PATTERN_STANDARD[
        "type_category_token"
    ]
    weapons_db = game_db.get("weapons", {})
    ammo_props = game_db.get("ammunition", {}).get("ammo_properties", {})
    forward_renames, reverse_renames = _build_vanilla_ammo_rename_maps()

    descr_self = f"WeaponDescriptor_{unit_name}"
    weapon_info = weapons_db.get(descr_self)
    if weapon_info is None and donor_name:
        weapon_info = weapons_db.get(f"WeaponDescriptor_{donor_name}")
    if not weapon_info:
        return False

    replace_map = _build_unit_replace_map(edits)
    for turret in weapon_info.get("turrets", {}).values():
        for ammo_name in turret.get("weapons", {}).keys():
            base = _SALVO_SUFFIX_RE.sub("", ammo_name)
            effective = replace_map.get(base, base)
            effective = forward_renames.get(effective, effective)
            if _type_category_token(ammo_props, effective, reverse_renames) == token:
                return True
            # Also accept the pre-replace mount (vanilla ATGM before equipment swap).
            if _type_category_token(ammo_props, base, reverse_renames) == token:
                return True
    return False


def _resolve_unit_edits_and_donor(
    unit_name: str,
    unit_edits: Dict[str, Any],
    new_units_by_name: Dict[str, Dict[str, Any]],
) -> tuple[Optional[Dict[str, Any]], Optional[str]]:
    if unit_name in unit_edits:
        return unit_edits[unit_name], None
    meta = new_units_by_name.get(unit_name)
    if meta:
        return meta["edits"], meta.get("donor")
    return None, None


def _set_infantry_wa_armor_for_strength(damage_module: Any, strength: int) -> None:
    blindage = damage_module.v.by_m("BlindageProperties", False)
    if blindage is None:
        return
    armor_index = str(max(15 - strength, 1))
    for part in _ARMOR_PARTS:
        resistance = blindage.v.by_m(part, False)
        if resistance is None:
            continue
        family_row = resistance.v.by_m("Family", False)
        if family_row is None:
            continue
        if strip_quotes(str(family_row.v)) != "ResistanceFamily_infanterieWA":
            continue
        index_row = resistance.v.by_m("Index", False)
        if index_row is not None:
            index_row.v = armor_index


def apply_strength_to_atgm_team_unit(
    logger: Any,
    unit_name: str,
    modules_list: Any,
    strength: int,
) -> bool:
    """Write MaxPhysicalDamages (and SoldierCount when present) for one unit.

    Dedicated AT / HMG weapon teams often have no ``TInfantrySquadModuleDescriptor``;
    HP is owned by ``TBaseDamageModuleDescriptor`` only (same as unit_edits strength).
    """
    base_damage = find_obj_by_type(modules_list.v, "TBaseDamageModuleDescriptor")
    if base_damage is None:
        logger.warning(
            f"ATGM team strength: missing TBaseDamageModuleDescriptor on {unit_name}",
        )
        return False

    squad = find_obj_by_type(modules_list.v, "TInfantrySquadModuleDescriptor")
    if squad is not None and unit_name not in _SKIP_SOLDIER_COUNT:
        squad.v.by_m("SoldierCount").v = str(strength)

    base_damage.v.by_m("MaxPhysicalDamages").v = str(strength)

    damage = find_obj_by_type(modules_list.v, "TDamageModuleDescriptor")
    if damage is not None:
        _set_infantry_wa_armor_for_strength(damage, strength)

    logger.info(f"ATGM infantry team strength: set {unit_name} to {strength}")
    return True


def apply_atgm_infantry_team_strength_pattern_standard(
    logger: Any,
    source_path: Any,
    game_db: Dict[str, Any],
) -> None:
    """Set ATGM team strength after unit_edits / new_units (specialty-aware)."""
    std = ATGM_INFANTRY_TEAM_STRENGTH_PATTERN_STANDARD
    unit_db = game_db.get("unit_data", {})
    unit_edits = load_unit_edits()
    new_units_by_name = _new_unit_edits_by_name()
    explicit_strength = _units_with_explicit_strength(unit_edits, new_units_by_name)
    updated = 0

    for unit_descr in source_path:
        unit_name = unit_descr.namespace.replace("Descriptor_Unit_", "")
        if unit_name in explicit_strength:
            continue

        unit_data = unit_db.get(unit_name, {})
        if not is_at_team_unit(unit_name, unit_data):
            continue

        edits, donor = _resolve_unit_edits_and_donor(
            unit_name, unit_edits, new_units_by_name,
        )
        if not unit_has_anti_tank_missile_mount(
            unit_name,
            game_db,
            edits=edits,
            donor_name=donor,
            type_category_token=std["type_category_token"],
        ):
            continue

        modules_list = unit_descr.v.by_m("ModulesDescriptors")
        ui_module = find_obj_by_type(modules_list.v, "TUnitUIModuleDescriptor")
        if ui_module is None:
            continue
        specialties_list = ui_module.v.by_m("SpecialtiesList", False)
        if specialties_list is None:
            continue

        strength = resolve_strength_for_specialties(specialties_list, std)
        if apply_strength_to_atgm_team_unit(
            logger, unit_name, modules_list, strength,
        ):
            updated += 1

    if updated:
        logger.info(
            f"ATGM infantry team strength: updated {updated} dedicated ATGM team(s)",
        )
