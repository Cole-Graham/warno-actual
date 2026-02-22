"""Validation for small arms quantity variants.

Validates that unit edits and new units only reference weapon quantity variants
that are configured to be created in the ammunition edits (small_arms NbWeapons).
"""

import json
from pathlib import Path
from typing import Any, Dict, Set, Tuple

from src.constants.new_units import NEW_UNITS
from src.constants.unit_edits import load_unit_edits
from src.constants.weapons import ammunitions
from src.utils.logging_utils import setup_logger

logger = setup_logger(__name__)

# Units that skip strength variant generation - use non-strength validation
UNITS_SKIP_STRENGTH_VARIANTS = {"KdA_DDR_TargetDummy"}


def _get_weapon_nb_weapons(weapon_name: str) -> list:
    """Get NbWeapons list for a weapon from ammunitions, resolving references."""
    for (w_name, category, _donor, _is_new), data in ammunitions.items():
        if w_name == weapon_name:
            nb_weapons = data.get("NbWeapons")
            if nb_weapons is None:
                return []
            if isinstance(nb_weapons, list):
                return nb_weapons
            # String reference - look up referenced weapon
            if isinstance(nb_weapons, str):
                return _get_weapon_nb_weapons(nb_weapons)
            return []
    return []


def _weapon_uses_strength_variants(weapon_name: str, game_db: Dict[str, Any]) -> bool:
    """Check if weapon uses strength variants (matches ammunition editor logic)."""
    for (w_name, category, _donor, _is_new), data in ammunitions.items():
        if w_name == weapon_name and category == "small_arms":
            ammo_properties = {}
            if game_db and "ammunition" in game_db:
                ammo_properties = game_db["ammunition"].get("ammo_properties", {}).get(
                    f"Ammo_{weapon_name}", {}
                )
            is_crew_or_vehicle = ammo_properties.get("MinMaxCategory") == "MinMax_MMG_HMG"
            if not is_crew_or_vehicle:
                damage_family = data.get("Ammunition", {}).get("Arme", {}).get("Family")
                return damage_family in ["DamageFamily_sa_full", "DamageFamily_sa_intermediate"]
            return False
    return False


def build_valid_small_arms_quantity_variants(
    game_db: Dict[str, Any] = None,
) -> Dict[str, Dict[str, Any]]:
    """Build dataset of valid small arms quantity variants from ammunition constants.

    Matches the logic in ammunition.py _create_quantity_variants:
    - For strength variants: creates Ammo_X_strength{s}_x{min(q,s)} for q in NbWeapons, s in 2..16
    - For non-strength: creates Ammo_X_x{q} for q in NbWeapons, Ammo_X for q=1

    Returns:
        Dict mapping weapon_name -> {
            "use_strength": bool,
            "valid_effective_per_strength": Dict[int, Set[int]],  # strength -> set of valid x values
            "valid_quantities": Set[int],  # for non-strength
        }
    """
    result: Dict[str, Dict[str, Any]] = {}

    for (weapon_name, category, _donor, _is_new), data in ammunitions.items():
        if category != "small_arms":
            continue

        nb_weapons = _get_weapon_nb_weapons(weapon_name)
        if not nb_weapons:
            continue

        use_strength = _weapon_uses_strength_variants(weapon_name, game_db)

        if use_strength:
            # For each strength 2..16, valid x values = {min(q, s) for q in NbWeapons}
            valid_effective_per_strength: Dict[int, Set[int]] = {}
            for strength in range(2, 17):
                valid_x = {min(q, strength) for q in nb_weapons}
                valid_effective_per_strength[strength] = valid_x
            result[weapon_name] = {
                "use_strength": True,
                "valid_effective_per_strength": valid_effective_per_strength,
            }
        else:
            result[weapon_name] = {
                "use_strength": False,
                "valid_quantities": set(nb_weapons),
            }

    return result


def _serialize_valid_variants_for_json(variants: Dict[str, Dict[str, Any]]) -> Dict:
    """Convert valid variants to JSON-serializable format (sets -> sorted lists)."""
    result = {}
    for weapon_name, data in variants.items():
        entry = {"use_strength": data["use_strength"]}
        if data["use_strength"]:
            entry["valid_effective_per_strength"] = {
                str(k): sorted(v) for k, v in data["valid_effective_per_strength"].items()
            }
        else:
            entry["valid_quantities"] = sorted(data["valid_quantities"])
        result[weapon_name] = entry
    return result


def save_valid_small_arms_variants(
    variants: Dict[str, Dict[str, Any]],
    config: Dict[str, Any],
) -> None:
    """Save valid small arms quantity variants to constants_precomputation JSON."""
    from src.utils.database_utils import ensure_db_directory

    db_path = Path(config["data_config"]["database_path"])
    constants_dir = db_path / "constants_precomputation"
    ensure_db_directory(str(constants_dir))

    serialized = _serialize_valid_variants_for_json(variants)
    out_file = constants_dir / "valid_small_arms_quantity_variants.json"
    with open(out_file, "w") as f:
        json.dump(serialized, f, indent=2, sort_keys=True)
    logger.debug(f"Saved valid small arms quantity variants to {out_file}")


def _is_valid_quantity(
    weapon_name: str,
    quantity: int,
    unit_strength: int,
    unit_name: str,
    valid_variants: Dict[str, Dict[str, Any]],
    game_db: Dict[str, Any],
) -> Tuple[bool, str]:
    """Check if (weapon, quantity, strength) is valid. Returns (is_valid, reason)."""
    if weapon_name not in valid_variants:
        return False, f"weapon '{weapon_name}' not in small_arms ammunition constants"

    weapon_data = valid_variants[weapon_name]
    use_strength = weapon_data["use_strength"] and unit_name not in UNITS_SKIP_STRENGTH_VARIANTS

    if use_strength:
        # Ammunition editor creates: Ammo_X_strength{s}_x{min(q,s)}
        # Unit edits request: Ammo_X_strength{s}_x{quantity}
        # So we need min(quantity, strength) in valid_effective_per_strength[strength]
        effective_q = min(quantity, unit_strength)
        valid_per_strength = weapon_data.get("valid_effective_per_strength", {})
        if unit_strength not in valid_per_strength:
            return False, f"strength {unit_strength} not in valid range (2-16)"
        if effective_q not in valid_per_strength[unit_strength]:
            valid_set = valid_per_strength[unit_strength]
            return False, (
                f"effective quantity {effective_q} (min({quantity},{unit_strength})) not in "
                f"valid set {sorted(valid_set)} for weapon '{weapon_name}'"
            )
        return True, ""
    else:
        valid_quantities = weapon_data.get("valid_quantities", set())
        if quantity not in valid_quantities:
            return False, (
                f"quantity {quantity} not in NbWeapons {sorted(valid_quantities)} "
                f"for weapon '{weapon_name}'"
            )
        return True, ""


def _collect_quantity_requests(unit_edits: Dict, new_units: Dict) -> list:
    """Collect all (unit_name, base_ammo, quantity) from unit_edits and NEW_UNITS."""
    requests = []

    for unit_name, unit_data in unit_edits.items():
        if unit_name.endswith("_reference"):
            continue
        wd = unit_data.get("WeaponDescriptor", {})
        eq_changes = wd.get("equipmentchanges", {})
        quantity_edits = eq_changes.get("quantity", {})
        for base_ammo, quantity in quantity_edits.items():
            requests.append((unit_name, base_ammo, quantity, "unit_edit"))

    for donor, edits in new_units.items():
        if not isinstance(edits, dict):
            continue
        unit_name = edits.get("NewName")
        if not unit_name or unit_name.endswith("_reference"):
            continue
        wd = edits.get("WeaponDescriptor", {})
        eq_changes = wd.get("equipmentchanges", {})
        quantity_edits = eq_changes.get("quantity", {})
        for base_ammo, quantity in quantity_edits.items():
            requests.append((unit_name, base_ammo, quantity, "new_unit"))

    return requests


def validate_small_arms_quantity_variants(
    config: Dict[str, Any],
    game_db: Dict[str, Any],
) -> bool:
    """Validate that all unit edits and new units reference valid small arms quantity variants.

    Runs during constants precomputation. Logs errors for invalid combinations.
    Returns True if any errors were found (validation failed).
    """
    valid_variants = build_valid_small_arms_quantity_variants(game_db)

    unit_edits = load_unit_edits()
    unit_data = game_db.get("unit_data", {})

    requests = _collect_quantity_requests(unit_edits, NEW_UNITS)

    errors: list = []
    for unit_name, base_ammo, quantity, source in requests:
        # Skip non-small-arms (weapons not in valid_variants)
        if base_ammo not in valid_variants:
            continue

        unit_strength = None
        if unit_name in unit_edits and "strength" in unit_edits[unit_name]:
            unit_strength = unit_edits[unit_name]["strength"]
        elif unit_name in unit_data:
            unit_strength = unit_data[unit_name].get("strength")
        else:
            for _donor, edits in NEW_UNITS.items():
                if isinstance(edits, dict) and edits.get("NewName") == unit_name:
                    unit_strength = edits.get("strength")
                    break

        if not unit_strength:
            # Cannot validate without strength - skip (unit might not be infantry)
            continue

        is_valid, reason = _is_valid_quantity(
            base_ammo,
            quantity,
            unit_strength,
            unit_name,
            valid_variants,
            game_db,
        )
        if not is_valid:
            errors.append(
                f"[{source}] {unit_name}: weapon '{base_ammo}' quantity {quantity} "
                f"(strength {unit_strength}) - {reason}"
            )

    if errors:
        for err in errors:
            logger.error(f"Invalid small arms quantity variant: {err}")
        logger.error(
            f"Found {len(errors)} invalid small arms quantity variant(s). "
            "Add the quantity to NbWeapons in small_arms.py or fix the unit edit."
        )
        return True
    return False
