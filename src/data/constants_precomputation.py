"""Constants-dependent precomputation data generation.

This module handles generation of JSON data files that depend on constants (unit_edits, NEW_UNITS)
rather than game files. These JSON files are regenerated on every patcher run, even when
build_database is false. The "database" is just the collection of JSON files on disk.
"""

import json
from pathlib import Path
from typing import Any, Dict, List

from src.constants.new_units import NEW_UNITS
from src.constants.unit_edits import load_unit_edits
from src.constants.weapons.vanilla_inst_modifications import (
    AMMUNITION_MISSILES_RENAMES,
    AMMUNITION_RENAMES,
)
from src.utils.config_utils import get_mod_src_path
from src.utils.database_utils import ensure_db_directory
from src.utils.logging_utils import setup_logger

from .deck_pack_mappings import build_deck_pack_mappings
from .small_arms_quantity_validation import (
    build_valid_small_arms_quantity_variants,
    save_valid_small_arms_variants,
    validate_small_arms_quantity_variants,
)
from .unit_data import gather_unit_data

logger = setup_logger(__name__)


def build_ammunition_renames(game_db: Dict[str, Any] = None) -> Dict[str, Dict[str, str]]:
    """Build ammunition renames from constants.
    
    Validates that old names exist in game_db before including them in renames.
    Logs warnings for old names that are not found in the game database.
    
    Args:
        game_db: Optional game database dict containing ammunition data
    
    Returns:
        Dict with renames_old_new and renames_new_old mappings based on constants
    """
    renames_old_new = {}
    
    # Build set of valid ammunition names from game_db if available
    valid_ammo_names = set()
    if game_db and "ammunition" in game_db:
        ammo_data = game_db["ammunition"]
        
        # Use the all_ammunition_and_missile list if available
        if "all_ammunition_and_missile" in ammo_data and isinstance(ammo_data["all_ammunition_and_missile"], list):
            valid_ammo_names = set(ammo_data["all_ammunition_and_missile"])
    
    # Add renames from constants, validating against game_db
    for old_name, new_name in AMMUNITION_RENAMES:
        if game_db and valid_ammo_names and old_name not in valid_ammo_names:
            logger.warning(f"Old ammunition name '{old_name}' not found in game_db, skipping rename")
        else:
            renames_old_new[old_name] = new_name
        
    for old_name, new_name in AMMUNITION_MISSILES_RENAMES:
        if game_db and valid_ammo_names and old_name not in valid_ammo_names:
            logger.warning(f"Old ammunition missile name '{old_name}' not found in game_db, skipping rename")
        else:
            renames_old_new[old_name] = new_name
    
    # Create reversed mapping
    renames_new_old = {v: k for k, v in renames_old_new.items()}
    
    return {
        "renames_old_new": renames_old_new,
        "renames_new_old": renames_new_old,
    }


def build_constants_precomputation_data(config: Dict[str, Any], game_db: Dict[str, Any] = None) -> Dict[str, Dict[str, str]]:
    """Build constants-dependent precomputation data and save as JSON files.
    
    This function always runs, regardless of build_database setting.
    It generates mappings based on current unit_edits and NEW_UNITS constants
    and saves them to constants_precomputation/deck_pack_mappings.json and
    constants_precomputation/ammunition_renames.json.
    
    Args:
        config: Configuration dict with database_path (path to JSON files) and mod_source_path
        game_db: Optional game_db dict used to validate ammunition renames
    
    Returns:
        Dict with deck_pack_mappings and ammunition_renames structure:
        {
            "deck_pack_modifications": {...},
            "reference_mappings": {...},
            "new_command_unit_deck_packs": {...},
            "ammunition_renames": {
                "renames_old_new": {...},
                "renames_new_old": {...}
            }
        }
    """
    logger.info("Building constants precomputation data")
    
    # Get mod_source_path to parse game files
    mod_source_path = get_mod_src_path(config)
    if not mod_source_path or not mod_source_path.exists():
        logger.error(f"Invalid mod_source_path: {mod_source_path}")
        return {
            "deck_pack_modifications": {},
            "reference_mappings": {},
            "new_command_unit_deck_packs": {},
            "ammunition_renames": {"renames_old_new": {}, "renames_new_old": {}},
        }
    
    try:
        # Build mappings by parsing game files
        # build_deck_pack_mappings filters at runtime using unit_edits and NEW_UNITS
        mappings = build_deck_pack_mappings(mod_source_path)
        
        # Build ammunition renames from constants
        ammunition_renames = build_ammunition_renames(game_db)
        
        # Build and save extended UpgradeFrom mapping (saves to disk internally)
        build_extended_upgrade_from_mapping(config)
        
        # Save deck_pack_mappings to separate JSON file
        save_constants_precomputation_data(mappings, config)
        
        # Save ammunition_renames to separate JSON file
        save_ammunition_renames(ammunition_renames, config)

        # Build and validate small arms quantity variants
        valid_small_arms_variants = build_valid_small_arms_quantity_variants(game_db)
        save_valid_small_arms_variants(valid_small_arms_variants, config)
        if game_db:
            validation_failed = validate_small_arms_quantity_variants(config, game_db)
            if validation_failed:
                logger.warning(
                    "Small arms quantity validation found errors - see above. "
                    "Fix unit edits or add quantities to NbWeapons in small_arms.py"
                )

        # Add ammunition_renames to return dict for convenience
        mappings["ammunition_renames"] = ammunition_renames

        logger.info(
            f"Constants precomputation data built and saved: "
            f"{len(mappings.get('deck_pack_modifications', {}))} modifications, "
            f"{len(mappings.get('reference_mappings', {}))} references, "
            f"{len(mappings.get('new_command_unit_deck_packs', {}))} new command unit deck packs, "
            f"{len(ammunition_renames.get('renames_old_new', {}))} ammunition renames"
        )
        return mappings
    except Exception as e:
        logger.error(f"Failed to build constants precomputation data: {e}", exc_info=True)
        return {
            "deck_pack_modifications": {},
            "reference_mappings": {},
            "new_command_unit_deck_packs": {},
            "ammunition_renames": {"renames_old_new": {}, "renames_new_old": {}},
        }


def load_constants_precomputation_data(config: Dict[str, Any]) -> Dict[str, Dict[str, str]]:
    """Load constants precomputation data from JSON files on disk.
    
    Args:
        config: Configuration dict with database_path (path to JSON files directory)
    
    Returns:
        Dict with deck_pack_mappings and ammunition_renames structure, or empty dict if files don't exist
    """
    db_path = Path(config["data_config"]["database_path"])
    mappings_file = db_path / "constants_precomputation" / "deck_pack_mappings.json"
    renames_file = db_path / "constants_precomputation" / "ammunition_renames.json"
    
    mappings = {
        "deck_pack_modifications": {},
        "reference_mappings": {},
        "new_command_unit_deck_packs": {},
    }
    
    # Load deck_pack_mappings
    if mappings_file.exists():
        try:
            with open(mappings_file) as f:
                mappings.update(json.load(f))
            logger.debug("Loaded deck_pack_mappings from disk")
            # Ensure all expected keys exist
            if "new_command_unit_deck_packs" not in mappings:
                mappings["new_command_unit_deck_packs"] = {}
        except Exception as e:
            logger.error(f"Failed to load deck_pack_mappings: {e}")
    else:
        logger.debug("Deck pack mappings file not found")
    
    # Load ammunition_renames
    if renames_file.exists():
        try:
            with open(renames_file) as f:
                mappings["ammunition_renames"] = json.load(f)
            logger.debug("Loaded ammunition_renames from disk")
        except Exception as e:
            logger.error(f"Failed to load ammunition_renames: {e}")
            mappings["ammunition_renames"] = {"renames_old_new": {}, "renames_new_old": {}}
    else:
        logger.debug("Ammunition renames file not found")
        mappings["ammunition_renames"] = {"renames_old_new": {}, "renames_new_old": {}}
    
    return mappings


def save_constants_precomputation_data(data: Dict[str, Dict[str, str]], config: Dict[str, Any]) -> None:
    """Save deck_pack_mappings data as JSON file to disk.
    
    Args:
        data: Dict with deck_pack_mappings structure (without ammunition_renames)
        config: Configuration dict with database_path (path to JSON files directory)
    """
    db_path = Path(config["data_config"]["database_path"])
    constants_dir = db_path / "constants_precomputation"
    
    # Create directory if needed
    ensure_db_directory(str(constants_dir))
    
    # Remove ammunition_renames if present (it's saved separately)
    save_data = {k: v for k, v in data.items() if k != "ammunition_renames"}
    
    # Save as JSON file: constants_precomputation/deck_pack_mappings.json
    mappings_file = constants_dir / "deck_pack_mappings.json"
    try:
        with open(mappings_file, "w") as f:
            json.dump(save_data, f, indent=2, sort_keys=True)
        logger.debug(f"Saved deck_pack_mappings to {mappings_file}")
    except Exception as e:
        logger.error(f"Failed to save deck_pack_mappings: {e}")
        raise


def save_ammunition_renames(renames: Dict[str, Dict[str, str]], config: Dict[str, Any]) -> None:
    """Save ammunition renames data as JSON file to disk.
    
    Args:
        renames: Dict with renames_old_new and renames_new_old structure
        config: Configuration dict with database_path (path to JSON files directory)
    """
    db_path = Path(config["data_config"]["database_path"])
    constants_dir = db_path / "constants_precomputation"
    
    # Create directory if needed
    ensure_db_directory(str(constants_dir))
    
    # Save as JSON file: constants_precomputation/ammunition_renames.json
    renames_file = constants_dir / "ammunition_renames.json"
    try:
        with open(renames_file, "w") as f:
            json.dump(renames, f, indent=2, sort_keys=True)
        logger.debug(f"Saved ammunition_renames to {renames_file}")
    except Exception as e:
        logger.error(f"Failed to save ammunition_renames: {e}")
        raise


def _detect_circular_chains(forward_mapping: Dict[str, str]) -> List[List[str]]:
    """Detect circular chains in the forward mapping.
    
    A circular chain occurs when following upgrade relationships leads back to a unit
    that was already visited in the chain.
    
    Example:
        If UnitA upgrades from UnitB, UnitB upgrades from UnitC, and UnitC upgrades from UnitA,
        this creates a circular chain: [UnitA, UnitB, UnitC, UnitA]
    
    Args:
        forward_mapping: Dictionary mapping unit names to their UpgradeFromUnit values
        
    Returns:
        List of circular chains, where each chain is a list of unit names forming the cycle
    """
    circular_chains = []
    visited = set()
    rec_stack = set()
    
    def find_cycle(unit: str, path: List[str]) -> None:
        """DFS to find cycles starting from a unit."""
        if unit in rec_stack:
            # Found a cycle - extract the cycle portion
            cycle_start = path.index(unit)
            cycle = path[cycle_start:] + [unit]
            # Only add if we haven't seen this exact cycle before
            if cycle not in circular_chains:
                circular_chains.append(cycle)
            return
        
        if unit in visited:
            return
        
        visited.add(unit)
        rec_stack.add(unit)
        path.append(unit)
        
        # Follow the upgrade relationship
        if unit in forward_mapping:
            upgrade_from = forward_mapping[unit]
            # Follow the chain - upgrade_from might not be in forward_mapping (could be base unit)
            # but we still want to detect if it creates a cycle back to something in our path
            if upgrade_from in rec_stack:
                # Found a cycle back to upgrade_from
                cycle_start = path.index(upgrade_from)
                cycle = path[cycle_start:] + [upgrade_from]
                if cycle not in circular_chains:
                    circular_chains.append(cycle)
            elif upgrade_from not in visited:
                # Continue DFS
                find_cycle(upgrade_from, path.copy())
        
        rec_stack.remove(unit)
    
    # Check all units in the forward mapping
    for unit in forward_mapping.keys():
        if unit not in visited:
            find_cycle(unit, [])
    
    return circular_chains


def _build_upgrade_chains(forward_mapping: Dict[str, str]) -> Dict[str, Any]:
    """Build upgrade chains from a forward mapping (unit -> upgrade_from).
    
    Groups units into chains where the base unit (lowest in chain) maps to
    a nested structure representing branches. Each direct child becomes a key,
    with its value being the chain continuing from that unit (or empty list if leaf).
    
    Example (linear chain):
        If UnitC upgrades from UnitB, and UnitB upgrades from UnitA,
        the result will be: {"UnitA": {"UnitB": ["UnitC"]}}
    
    Example (branching):
        If UnitB and UnitC both upgrade from UnitA, and UnitD upgrades from UnitB,
        the result will be: {"UnitA": {"UnitB": ["UnitD"], "UnitC": []}}
    
    Args:
        forward_mapping: Dictionary mapping unit names to their UpgradeFromUnit values
        
    Returns:
        Dictionary mapping base unit names to nested chain structures
    """
    # Build reverse mapping: upgrade_from -> [units that upgrade from it]
    reverse_mapping: Dict[str, List[str]] = {}
    
    for unit_name, upgrade_from in forward_mapping.items():
        if upgrade_from not in reverse_mapping:
            reverse_mapping[upgrade_from] = []
        reverse_mapping[upgrade_from].append(unit_name)
    
    # Find base units (units that are referenced as upgrade_from but don't upgrade from anything themselves)
    base_units = set()
    for upgrade_from in reverse_mapping.keys():
        if upgrade_from not in forward_mapping:
            base_units.add(upgrade_from)
    
    # Build chains starting from each base unit
    chain_mapping: Dict[str, Any] = {}
    
    def build_branch(unit: str, visited: set) -> Any:
        """Build a branch structure starting from a unit.
        
        Returns:
            - Empty list [] if unit has no children (leaf node)
            - Dict[str, Any] mapping each child to its branch if unit has children
        """
        if unit in visited:
            return []
        visited.add(unit)
        
        # Get all units that upgrade from this unit
        if unit not in reverse_mapping or not reverse_mapping[unit]:
            # Leaf node - no children
            return []
        
        # Branch node - create nested structure
        branch = {}
        for child_unit in reverse_mapping[unit]:
            child_branch = build_branch(child_unit, visited)
            branch[child_unit] = child_branch
        
        return branch
    
    for base_unit in base_units:
        branch = build_branch(base_unit, set())
        if branch:  # Only add if there are children
            chain_mapping[base_unit] = branch
            logger.debug(f"Built chain for {base_unit}: {branch}")
    
    return chain_mapping


def build_extended_upgrade_from_mapping(config: Dict[str, Any]) -> Dict[str, Any]:
    """Build extended UpgradeFrom mapping that includes unit_edits and new_units.
    
    This function:
    1. Loads vanilla unit_data from database to get original UpgradeFromUnit values
    2. Extends it with relationships from unit_edits
    3. Extends it with relationships from new_units
    4. Rebuilds chains from the combined forward mapping
    5. Saves the extended mapping to constants_precomputation/UpgradeFrom_mapping.json
    
    Args:
        config: Configuration dict with database_path and mod_source_path
        
    Returns:
        Dictionary mapping base unit names to nested chain structures
    """
    db_path = Path(config["data_config"]["database_path"])
    forward_mapping = {}
    
    # Load vanilla unit_data from database to get original UpgradeFromUnit values
    unit_data_file = db_path / "unit_data.json"
    if unit_data_file.exists():
        try:
            with open(unit_data_file) as f:
                unit_data = json.load(f)
            # Extract UpgradeFromUnit relationships from vanilla unit_data
            for unit_name, unit_info in unit_data.items():
                if isinstance(unit_info, dict) and "upgrade_from_unit" in unit_info:
                    upgrade_from = unit_info["upgrade_from_unit"]
                    if upgrade_from:  # Only add if not None/empty
                        forward_mapping[unit_name] = upgrade_from
            logger.debug(f"Loaded vanilla UpgradeFrom relationships from unit_data: {len(forward_mapping)} relationships")
        except Exception as e:
            logger.warning(f"Failed to load unit_data for UpgradeFrom mapping: {e}")
            # Fallback: try to re-extract from game files
            try:
                mod_source_path = get_mod_src_path(config)
                if mod_source_path and mod_source_path.exists():
                    logger.info("Re-extracting unit_data from game files as fallback")
                    unit_data = gather_unit_data(mod_source_path)
                    for unit_name, unit_info in unit_data.items():
                        if "upgrade_from_unit" in unit_info:
                            upgrade_from = unit_info["upgrade_from_unit"]
                            if upgrade_from:
                                forward_mapping[unit_name] = upgrade_from
                    logger.debug(f"Re-extracted {len(forward_mapping)} vanilla UpgradeFrom relationships")
            except Exception as e2:
                logger.error(f"Failed to re-extract unit_data: {e2}")
    else:
        logger.warning("unit_data.json not found, attempting to re-extract from game files")
        try:
            mod_source_path = get_mod_src_path(config)
            if mod_source_path and mod_source_path.exists():
                unit_data = gather_unit_data(mod_source_path)
                for unit_name, unit_info in unit_data.items():
                    if "upgrade_from_unit" in unit_info:
                        upgrade_from = unit_info["upgrade_from_unit"]
                        if upgrade_from:
                            forward_mapping[unit_name] = upgrade_from
                logger.debug(f"Extracted {len(forward_mapping)} vanilla UpgradeFrom relationships")
            else:
                logger.error("mod_source_path not available for re-extraction")
        except Exception as e:
            logger.error(f"Failed to extract unit_data: {e}")
    
    # Add/update/remove relationships from unit_edits
    try:
        unit_edits = load_unit_edits()
        edits_added = 0
        edits_removed = 0
        for unit_name, unit_edit in unit_edits.items():
            if "UpgradeFromUnit" in unit_edit:
                upgrade_from = unit_edit["UpgradeFromUnit"]
                if upgrade_from is not None:
                    # Add or update the relationship
                    forward_mapping[unit_name] = upgrade_from
                    edits_added += 1
                    logger.debug(f"Added/updated UpgradeFrom from unit_edits: {unit_name} -> {upgrade_from}")
                else:
                    # Explicitly remove the relationship if it exists
                    if unit_name in forward_mapping:
                        del forward_mapping[unit_name]
                        edits_removed += 1
                        logger.debug(f"Removed UpgradeFrom from unit_edits: {unit_name}")
            # If "UpgradeFromUnit" key is not present, leave the vanilla relationship unchanged
        logger.info(f"Processed unit_edits: {edits_added} added/updated, {edits_removed} removed")
    except Exception as e:
        logger.error(f"Failed to load unit_edits for UpgradeFrom mapping: {e}")
    
    # Add relationships from new_units
    try:
        new_units_added = 0
        skipped_no_newname = 0
        for unit_key, unit_data in NEW_UNITS.items():
            if not isinstance(unit_data, dict):
                continue
            
            # For donor units, NewName is required - this is the actual unit name
            if "NewName" not in unit_data:
                # Configuration error - log warning and skip
                unit_key_str = str(unit_key) if isinstance(unit_key, tuple) else unit_key
                logger.warning(
                    f"New unit entry {unit_key_str} is missing 'NewName' field - skipping UpgradeFromUnit processing. "
                    f"This is a configuration error."
                )
                skipped_no_newname += 1
                continue
            
            unit_name = unit_data["NewName"]
            
            # Skip reference entries
            if unit_name.endswith("_reference"):
                continue
            
            if "UpgradeFromUnit" in unit_data:
                upgrade_from = unit_data["UpgradeFromUnit"]
                if upgrade_from is not None:  # Only add if not None
                    forward_mapping[unit_name] = upgrade_from
                    new_units_added += 1
                    logger.debug(f"Added UpgradeFrom from new_units: {unit_name} -> {upgrade_from}")
        
        if skipped_no_newname > 0:
            logger.warning(f"Skipped {skipped_no_newname} new unit entries due to missing NewName field")
        logger.info(f"Added {new_units_added} UpgradeFrom relationships from new_units")
    except Exception as e:
        logger.error(f"Failed to process NEW_UNITS for UpgradeFrom mapping: {e}")
    
    # Validate for circular chains before building
    circular_chains = _detect_circular_chains(forward_mapping)
    if circular_chains:
        cycle_details = []
        for i, cycle in enumerate(circular_chains, 1):
            cycle_str = " -> ".join(cycle)
            cycle_details.append(f"  Circular chain {i}: {cycle_str}")
        error_msg = (
            f"Found {len(circular_chains)} circular chain(s) in upgrade relationships:\n"
            + "\n".join(cycle_details) +
            "\nCircular chains will be excluded from the mapping"
        )
        logger.error(error_msg)
    
    # Build chains from combined forward mapping
    chain_mapping = _build_upgrade_chains(forward_mapping)
    
    # Save extended mapping to constants_precomputation
    constants_dir = db_path / "constants_precomputation"
    ensure_db_directory(str(constants_dir))
    
    extended_mapping_file = constants_dir / "extendedUpgradeFrom_mapping.json"
    try:
        with open(extended_mapping_file, "w") as f:
            json.dump(chain_mapping, f, indent=2, sort_keys=False)
        logger.info(
            f"Saved extended UpgradeFrom mapping with {len(chain_mapping)} chains "
            f"containing {sum(len(chain) for chain in chain_mapping.values())} total units to {extended_mapping_file}"
        )
    except Exception as e:
        logger.error(f"Failed to save extended UpgradeFrom mapping: {e}")
        raise
    
    return chain_mapping

