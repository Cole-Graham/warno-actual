"""Constants-dependent precomputation data generation.

This module handles generation of JSON data files that depend on constants (unit_edits, NEW_UNITS)
rather than game files. These JSON files are regenerated on every patcher run, even when
build_database is false. The "database" is just the collection of JSON files on disk.
"""

import json
import re
from pathlib import Path
from typing import Any, Dict, List, Tuple

from src.constants.new_units import NEW_UNITS
from src.constants.unit_edits import load_unit_edits
from src.constants.unit_edits.replace_schema import normalize_replace
from src.constants.weapons import ammunitions, missiles
from src.constants.weapons.standards.by_category import (
    AA_CATEGORIES,
    AA_SUPPRESS_BY_PHYSICAL_DAMAGE,
)
from src.constants.weapons.vanilla_inst_modifications import (
    AMMUNITION_MISSILES_RENAMES,
    AMMUNITION_RENAMES,
)
from src.utils.config_utils import get_mod_src_path
from src.utils.database_utils import ensure_db_directory
from src.utils.logging_utils import setup_logger

from .aircraft_vision_validation import validate_aircraft_vision_vs_weapon_range
from .deck_pack_mappings import build_deck_pack_mappings
from .insert_turret_templates import (
    build_insert_turret_templates,
    save_insert_turret_templates,
)
from .small_arms_quantity_validation import (
    build_valid_small_arms_quantity_variants,
    save_valid_small_arms_variants,
    validate_small_arms_quantity_variants,
)
from .ui_texture_validation import validate_ui_texture_constants
from .unit_data import (
    _build_upgrade_chains,
    _detect_circular_chains,
    gather_unit_data,
    validate_no_multiple_ancestors,
    validate_upgrade_forward_mapping_chain_lengths,
)

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

        if game_db and "ammunition" in game_db:
            clu_targets = game_db["ammunition"].get("clu_sol_trait_targets")
            if clu_targets:
                save_clu_sol_trait_targets(clu_targets, config)

        # Build and save insert turret templates (vanilla turrets for equipment insert)
        insert_templates = build_insert_turret_templates(
            config, game_db, ammunition_renames=ammunition_renames,
        )
        save_insert_turret_templates(insert_templates, config)

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

            ui_texture_failed = validate_ui_texture_constants(game_db)
            if ui_texture_failed:
                logger.warning(
                    "UI texture validation found errors - see above. "
                    "Fix textures in unit_edits / NEW_UNITS or rebuild ui_texture_reference from vanilla.",
                )

            aircraft_vision_failed = validate_aircraft_vision_vs_weapon_range(game_db)
            if aircraft_vision_failed:
                logger.warning(
                    "Aircraft vision validation found errors - see above. "
                    "Raise EVisionRange/Standard or reduce weapon MaximumRangeGRU.",
                )

        # Build protected ammo set for blanket deployment-time disable
        deployment_time_units = build_deployment_time_units(game_db) if game_db else {
            "protected_ammo": [],
        }
        save_deployment_time_units(deployment_time_units, config)

        # Build AA suppress damages mapping (PhysicalDamages -> SuppressDamages)
        aa_suppress_damages = build_aa_suppress_damages(game_db) if game_db else {}
        save_aa_suppress_damages(aa_suppress_damages, config)

        # Build he_dca weapons map (weapon_name -> final damage family)
        he_dca_weapons = build_he_dca_weapons(game_db) if game_db else {}
        save_he_dca_weapons(he_dca_weapons, config)

        # Build canon HE accuracy inheritance (AP hit_roll -> paired HE on same turret)
        canon_he_acc = build_canon_he_accuracy_inheritance(game_db) if game_db else {}
        save_canon_he_accuracy_inheritance(canon_he_acc, config)

        # Add ammunition_renames and insert_turret_templates to return dict for convenience
        mappings["ammunition_renames"] = ammunition_renames
        mappings["insert_turret_templates"] = insert_templates
        mappings["deployment_time_units"] = deployment_time_units
        mappings["aa_suppress_damages"] = aa_suppress_damages
        mappings["he_dca_weapons"] = he_dca_weapons
        mappings["canon_he_accuracy_inheritance"] = canon_he_acc

        logger.info(
            f"Constants precomputation data built and saved: "
            f"{len(mappings.get('deck_pack_modifications', {}))} modifications, "
            f"{len(mappings.get('reference_mappings', {}))} references, "
            f"{len(mappings.get('new_command_unit_deck_packs', {}))} new command unit deck packs, "
            f"{len(ammunition_renames.get('renames_old_new', {}))} ammunition renames, "
            f"{len(insert_templates)} insert turret templates, "
            f"{len(deployment_time_units.get('protected_ammo', []))} protected ammo, "
            f"{len(aa_suppress_damages)} AA suppress damages, "
            f"{len(he_dca_weapons)} he_dca weapons, "
            f"{len(canon_he_acc)} canon HE accuracy inheritances"
        )
        return mappings
    except Exception as e:
        logger.error(f"Failed to build constants precomputation data: {e}", exc_info=True)
        return {
            "deck_pack_modifications": {},
            "reference_mappings": {},
            "new_command_unit_deck_packs": {},
            "ammunition_renames": {"renames_old_new": {}, "renames_new_old": {}},
            "canon_he_accuracy_inheritance": {},
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


def save_clu_sol_trait_targets(targets: Dict[str, str], config: Dict[str, Any]) -> None:
    """Save precomputed CLU SOL TraitsToken patch map (Ammo_* namespace -> trait key)."""
    db_path = Path(config["data_config"]["database_path"])
    constants_dir = db_path / "constants_precomputation"
    ensure_db_directory(str(constants_dir))
    out_file = constants_dir / "clu_sol_trait_targets.json"
    try:
        with open(out_file, "w") as f:
            json.dump(targets, f, indent=2, sort_keys=True)
        logger.debug(f"Saved clu_sol_trait_targets to {out_file}")
    except Exception as e:
        logger.error(f"Failed to save clu_sol_trait_targets: {e}")
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


def build_deployment_time_units(game_db: Dict[str, Any]) -> Dict[str, List[str]]:
    """Build protected unit/ammo sets for blanket deployment-time disable.

    The engine requires that if ANY ammo on a unit has ``HasDeploymentTime =
    True``, the unit MUST have ``TWeaponDeploymentModuleDescriptor``, and vice
    versa.  So the module and the ammo flag must stay in sync.

    **Protected ammo** = ammo whose ``HasDeploymentTime`` will remain ``True``
    after patching:
      - ammo used by units with ``"WeaponDeployment"`` in unit_edits/NEW_UNITS
      - ammo whose constants explicitly set ``HasDeploymentTime = True``

    **Protected units** = units that must keep (or gain)
    ``TWeaponDeploymentModuleDescriptor``:
      - units with ``"WeaponDeployment"`` in unit_edits/NEW_UNITS
      - any unit carrying at least one protected ammo

    Returns:
        Dict with ``protected_units`` and ``protected_ammo`` lists.
    """
    weapons_db = game_db.get("weapons", {})
    ammo_props = game_db.get("ammunition", {}).get("ammo_properties", {})
    _salvo_suffix_re = re.compile(r'(_x\d+|_salvolength\d+)$')

    # --- 1. Seed protected units from unit_edits / NEW_UNITS ---
    unit_edits = load_unit_edits()
    protected_units: set = set()
    for unit_name_key, edits in unit_edits.items():
        if "WeaponDeployment" in edits:
            protected_units.add(unit_name_key)
    for _key, new_unit_data in NEW_UNITS.items():
        if isinstance(new_unit_data, dict) and "WeaponDeployment" in new_unit_data:
            protected_units.add(new_unit_data.get("NewName", ""))

    # --- 1b. Build per-unit ammo replacement map from unit_edits equipmentchanges ---
    unit_replace_map: Dict[str, Dict[str, str]] = {}
    for unit_name, edits in unit_edits.items():
        replacements: Dict[str, str] = {}
        replace_block = (
            edits.get("WeaponDescriptor", {})
            .get("equipmentchanges", {})
            .get("replace")
        )
        for spec in normalize_replace(replace_block):
            old_base = _salvo_suffix_re.sub("", spec.old_weapon)
            new_base = _salvo_suffix_re.sub("", spec.new_weapon)
            replacements[old_base] = new_base
        if replacements:
            unit_replace_map[unit_name] = replacements

    # --- 2. Build protected ammo set ---
    protected_ammo: set = set()

    # 2a. All ammo on explicitly protected units keeps its vanilla value
    for weapon_descr_name, weapon_info in weapons_db.items():
        if not weapon_descr_name.startswith("WeaponDescriptor_"):
            continue
        unit_name = weapon_descr_name.replace("WeaponDescriptor_", "", 1)
        if unit_name not in protected_units:
            continue
        for turret in weapon_info.get("turrets", {}).values():
            for ammo_name in turret.get("weapons", {}).keys():
                base = _salvo_suffix_re.sub('', ammo_name)
                # Only protect if the vanilla ammo actually has the flag
                if ammo_props.get(f"Ammo_{base}", {}).get("HasDeploymentTime"):
                    protected_ammo.add(base)

    # 2b. Ammo whose constants explicitly set HasDeploymentTime = True
    for (weapon_name, _cat, _donor, _is_new), data in {**ammunitions, **missiles}.items():
        ammo_data = data.get("Ammunition", {})
        parent_membr = ammo_data.get("parent_membr", {})
        if not parent_membr:
            continue
        if parent_membr.get("HasDeploymentTime") is True:
            protected_ammo.add(weapon_name)
            continue
        add_entry = parent_membr.get("add")
        if isinstance(add_entry, list) and len(add_entry) == 2 and isinstance(add_entry[1], str):
            if "HasDeploymentTime" in add_entry[1]:
                if add_entry[1].split("=", 1)[1].strip() == "True":
                    protected_ammo.add(weapon_name)

    # --- 3. Reverse-map: any unit carrying protected ammo must keep the module ---
    for weapon_descr_name, weapon_info in weapons_db.items():
        if not weapon_descr_name.startswith("WeaponDescriptor_"):
            continue
        unit_name = weapon_descr_name.replace("WeaponDescriptor_", "", 1)
        if unit_name in protected_units:
            continue
        for turret in weapon_info.get("turrets", {}).values():
            for ammo_name in turret.get("weapons", {}).keys():
                base_name = _salvo_suffix_re.sub('', ammo_name)
                effective_name = unit_replace_map.get(unit_name, {}).get(base_name, base_name)
                if effective_name in protected_ammo:
                    protected_units.add(unit_name)
                    break

    logger.info(
        f"Deployment time: {len(protected_units)} protected units, "
        f"{len(protected_ammo)} protected ammo base names"
    )
    return {
        "protected_units": sorted(protected_units),
        "protected_ammo": sorted(protected_ammo),
    }


def save_deployment_time_units(data: Dict[str, List[str]], config: Dict[str, Any]) -> None:
    """Save deployment time units data as JSON file to disk."""
    db_path = Path(config["data_config"]["database_path"])
    constants_dir = db_path / "constants_precomputation"
    ensure_db_directory(str(constants_dir))

    out_file = constants_dir / "deployment_time_units.json"
    try:
        with open(out_file, "w") as f:
            json.dump(data, f, indent=2, sort_keys=True)
        logger.debug(f"Saved deployment_time_units to {out_file}")
    except Exception as e:
        logger.error(f"Failed to save deployment_time_units: {e}")
        raise


def _lookup_vanilla_physical_damages(
    weapon_name: str,
    ammo_props: Dict[str, Any],
) -> Any:
    """Look up vanilla PhysicalDamages from ammo_properties.

    Tries exact ``Ammo_{weapon_name}`` first, then falls back to any
    ``Ammo_{weapon_name}_*`` entry (vanilla salvo variants use ``_x{N}``
    suffixes and may not have a bare base namespace).
    """
    exact = ammo_props.get(f"Ammo_{weapon_name}", {})
    pd = exact.get("PhysicalDamages")
    if pd is not None:
        return pd

    prefix = f"Ammo_{weapon_name}_"
    for key, props in ammo_props.items():
        if key.startswith(prefix):
            pd = props.get("PhysicalDamages")
            if pd is not None:
                return pd

    return None


def build_aa_suppress_damages(game_db: Dict[str, Any]) -> Dict[str, Dict[str, int]]:
    """Build weapon_name -> {physical_damage, suppress_damage} for AA missiles.

    For each AA missile (A2A / SAM / MANPAD) in the ``missiles`` dict,
    determine the final PhysicalDamages (constants override > vanilla game_db)
    and look up the corresponding *intended* total suppress damage via
    ``AA_SUPPRESS_BY_PHYSICAL_DAMAGE``.

    Both values are persisted so the handler can derive the final
    ``SuppressDamages`` to write to NDF, subtracting
    ``AA_ADDITIONAL_SUPPRESS_PER_LOST_PHYSICAL * physical_damage`` from the
    intended total (the engine adds that product back at runtime).

    Fallback order for PhysicalDamages:
      1. Constants ``parent_membr`` on this weapon
      2. Vanilla ``ammo_properties`` for this weapon (exact or ``_x{N}`` match)
      3. Donor weapon's constants ``parent_membr`` (for ``is_new`` missiles)
      4. Donor weapon's vanilla ``ammo_properties`` (exact or ``_x{N}`` match)
    """
    ammo_props = game_db.get("ammunition", {}).get("ammo_properties", {})

    # Pre-build donor lookup: weapon_name -> (donor, data)
    missile_index: Dict[str, Dict] = {}
    for (wn, cat, _d, _n), d in missiles.items():
        if cat in AA_CATEGORIES:
            missile_index[wn] = d

    result: Dict[str, Dict[str, int]] = {}

    for (weapon_name, category, donor, is_new), data in missiles.items():
        if category not in AA_CATEGORIES:
            continue

        # 1. Constants override on this weapon
        phys_dmg = (
            data.get("Ammunition", {})
            .get("parent_membr", {})
            .get("PhysicalDamages")
        )

        # 2. Vanilla ammo_properties (exact or _x{N} salvo variant match)
        if phys_dmg is None:
            phys_dmg = _lookup_vanilla_physical_damages(weapon_name, ammo_props)

        # 3-4. Donor fallback for new missiles (e.g. HAGRU variants)
        if phys_dmg is None and is_new and donor:
            donor_data = missile_index.get(donor, {})
            phys_dmg = (
                donor_data.get("Ammunition", {})
                .get("parent_membr", {})
                .get("PhysicalDamages")
            )
            if phys_dmg is None:
                phys_dmg = _lookup_vanilla_physical_damages(donor, ammo_props)

        if phys_dmg is None:
            logger.warning(
                f"(aa_suppress) {weapon_name}: no PhysicalDamages found "
                f"in constants, game_db, or donor, skipping",
            )
            continue

        phys_key = int(phys_dmg)
        suppress = AA_SUPPRESS_BY_PHYSICAL_DAMAGE.get(phys_key)
        if suppress is None:
            logger.warning(
                f"(aa_suppress) {weapon_name}: PhysicalDamages={phys_key} "
                f"has no entry in AA_SUPPRESS_BY_PHYSICAL_DAMAGE, skipping",
            )
            continue

        result[weapon_name] = {
            "physical_damage": phys_key,
            "suppress_damage": suppress,
        }

    logger.info(
        f"Built AA suppress damages mapping: {len(result)} missiles",
    )
    return result


def save_aa_suppress_damages(data: Dict[str, Dict[str, int]], config: Dict[str, Any]) -> None:
    """Save AA suppress damages mapping as JSON file to disk."""
    db_path = Path(config["data_config"]["database_path"])
    constants_dir = db_path / "constants_precomputation"
    ensure_db_directory(str(constants_dir))

    out_file = constants_dir / "aa_suppress_damages.json"
    try:
        with open(out_file, "w") as f:
            json.dump(data, f, indent=2, sort_keys=True)
        logger.debug(f"Saved aa_suppress_damages to {out_file}")
    except Exception as e:
        logger.error(f"Failed to save aa_suppress_damages: {e}")
        raise


_HE_DCA_FAMILY = "DamageFamily_he_dca"
_SALVO_SUFFIX_RE = re.compile(r"(_x\d+|_salvolength\d+)$")


def _constants_arme_family(data: Dict[str, Any]) -> Any:
    """Return constants override for ``Arme.Family`` (None if not set)."""
    if not isinstance(data, dict):
        return None
    arme = data.get("Ammunition", {}).get("Arme", {})
    if not isinstance(arme, dict):
        return None
    return arme.get("Family")


def build_he_dca_weapons(game_db: Dict[str, Any]) -> Dict[str, str]:
    """Build ``weapon_name -> final_damage_family`` for ``DamageFamily_he_dca`` weapons.

    Walks ``ammunitions``/``missiles`` constants (constants overrides on
    ``Arme.Family`` win) and the vanilla ``ammo_properties`` map (for weapons
    with no constants entry). Returns only weapons whose **final** family is
    ``DamageFamily_he_dca``, keyed by base ``weapon_name`` (no ``Ammo_``
    prefix, no salvo suffix). Downstream consumers (B3/B4) use this map to
    auto-clone ``_AIR`` ammo and auto-wire air mounts.
    """
    ammo_props = game_db.get("ammunition", {}).get("ammo_properties", {})

    constants_override: Dict[str, Any] = {}
    for (weapon_name, _cat, _donor, _is_new), data in {**ammunitions, **missiles}.items():
        family_override = _constants_arme_family(data)
        if family_override is not None:
            constants_override[weapon_name] = family_override

    final_family: Dict[str, str] = {}

    # Vanilla pass: derive base name from Ammo_<weapon>(_x{N}) keys.
    for ammo_ns, props in ammo_props.items():
        if not ammo_ns.startswith("Ammo_"):
            continue
        family = props.get("Family")
        if not family:
            continue
        base = _SALVO_SUFFIX_RE.sub("", ammo_ns[len("Ammo_"):])
        if base in constants_override:
            family = constants_override[base]
        if family == _HE_DCA_FAMILY:
            final_family[base] = family

    # Constants-only pass: weapons that may not exist in vanilla yet
    # (is_new) or whose constants override sets the family directly.
    for (weapon_name, _cat, donor, is_new), data in {**ammunitions, **missiles}.items():
        family_override = _constants_arme_family(data)
        if family_override is None:
            if not is_new:
                continue
            donor_family: Any = None
            if donor:
                exact = ammo_props.get(f"Ammo_{donor}", {})
                donor_family = exact.get("Family")
                if donor_family is None:
                    prefix = f"Ammo_{donor}_"
                    for key, p in ammo_props.items():
                        if key.startswith(prefix) and p.get("Family"):
                            donor_family = p["Family"]
                            break
            if donor_family is None:
                continue
            family_override = donor_family

        if family_override == _HE_DCA_FAMILY:
            final_family[weapon_name] = family_override

    logger.info(
        f"Built he_dca weapons mapping: {len(final_family)} ammo descriptors"
    )
    return final_family


def save_he_dca_weapons(data: Dict[str, str], config: Dict[str, Any]) -> None:
    """Save he_dca weapons mapping as JSON file to disk."""
    db_path = Path(config["data_config"]["database_path"])
    constants_dir = db_path / "constants_precomputation"
    ensure_db_directory(str(constants_dir))

    out_file = constants_dir / "he_dca_weapons.json"
    try:
        with open(out_file, "w") as f:
            json.dump(data, f, indent=2, sort_keys=True)
        logger.debug(f"Saved he_dca_weapons to {out_file}")
    except Exception as e:
        logger.error(f"Failed to save he_dca_weapons: {e}")
        raise


def build_canon_he_accuracy_inheritance(game_db: Dict[str, Any]) -> Dict[str, Dict[str, Any]]:
    """Build HE canon/autocannon weapon_name -> inherited hit_roll dict from its AP pair on the same turret.

    Uses game_db["weapons"] turret/mounted-weapon data to discover co-located AP/HE pairs
    (names starting with Canon_ or AutoCanon_ and containing _AP_ / _HE_).
    Pairs are formed by name substitution (_AP_ -> _HE_) or, as fallback, when a turret
    has exactly one AP and one HE entry.

    For each pair the ammunitions constants are consulted:
    - both define hit_roll but accuracy values (Idling/Moving/DistanceToTarget) differ -> warning
      (BaseCriticModifier may legitimately differ between AP and HE and is ignored for this check)
    - HE defines hit_roll but AP does not -> warning
    - only AP defines hit_roll -> record for later application to the HE descriptor

    The resulting map is consumed by the ammunition handler during NDF patching.
    """
    weapons_db = game_db.get("weapons", {})
    canon_autocanon_by_name: Dict[str, Dict] = {}
    for (weapon_name, category, _donor, _is_new), data in ammunitions.items():
        if category in ("canon", "autocannon"):
            canon_autocanon_by_name[weapon_name] = data

    result: Dict[str, Dict[str, Any]] = {}
    warned_pairs: set[Tuple[str, str]] = set()

    for _wdescr_name, weapon_info in weapons_db.items():
        turrets = weapon_info.get("turrets", {})
        for _turret_idx, turret_data in turrets.items():
            turret_weapons = turret_data.get("weapons", {})
            ap_names = [w for w in turret_weapons if (w.startswith("Canon_") or w.startswith("AutoCanon_")) and "_AP_" in w]
            he_names = [w for w in turret_weapons if (w.startswith("Canon_") or w.startswith("AutoCanon_")) and "_HE_" in w]

            if not ap_names or not he_names:
                continue

            pairs: List[Tuple[str, str]] = []
            for ap in ap_names:
                he_cand = ap.replace("_AP_", "_HE_")
                if he_cand in he_names:
                    pairs.append((ap, he_cand))

            if not pairs and len(ap_names) == 1 and len(he_names) == 1:
                pairs.append((ap_names[0], he_names[0]))

            for ap_name, he_name in pairs:
                ap_data = canon_autocanon_by_name.get(ap_name, {})
                he_data = canon_autocanon_by_name.get(he_name, {})
                ap_hit = ap_data.get("Ammunition", {}).get("hit_roll") if ap_data else None
                he_hit = he_data.get("Ammunition", {}).get("hit_roll") if he_data else None

                if ap_hit and he_hit:
                    # Compare only accuracy values; BaseCriticModifier is allowed to differ
                    acc_keys = ("Idling", "Moving", "DistanceToTarget")
                    ap_acc = {k: ap_hit[k] for k in acc_keys if k in ap_hit}
                    he_acc = {k: he_hit[k] for k in acc_keys if k in he_hit}
                    if ap_acc != he_acc:
                        pair_key = (ap_name, he_name)
                        if pair_key not in warned_pairs:
                            warned_pairs.add(pair_key)
                            logger.warning(
                                f"Both AP ({ap_name}) and HE ({he_name}) define hit_roll but accuracy values differ: AP={ap_acc} HE={he_acc}"
                            )
                elif he_hit and not ap_hit:
                    pair_key = (ap_name, he_name)
                    if pair_key not in warned_pairs:
                        warned_pairs.add(pair_key)
                        logger.warning(
                            f"HE canon {he_name} has manual hit_roll but corresponding AP canon {ap_name} does not"
                        )
                elif ap_hit and not he_hit:
                    if he_name not in result:
                        result[he_name] = ap_hit
                    elif result[he_name] != ap_hit:
                        logger.warning(f"Conflicting inherited hit_roll for {he_name} from multiple AP pairs")

    logger.info(f"Built canon HE accuracy inheritance mapping: {len(result)} HE weapons")
    return result


def save_canon_he_accuracy_inheritance(data: Dict[str, Dict[str, Any]], config: Dict[str, Any]) -> None:
    """Save canon HE accuracy inheritance mapping as JSON file to disk."""
    db_path = Path(config["data_config"]["database_path"])
    constants_dir = db_path / "constants_precomputation"
    ensure_db_directory(str(constants_dir))

    out_file = constants_dir / "canon_he_accuracy_inheritance.json"
    try:
        with open(out_file, "w") as f:
            json.dump(data, f, indent=2, sort_keys=True)
        logger.debug(f"Saved canon_he_accuracy_inheritance to {out_file}")
    except Exception as e:
        logger.error(f"Failed to save canon_he_accuracy_inheritance: {e}")
        raise


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

    validate_upgrade_forward_mapping_chain_lengths(forward_mapping)

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

    # Validate for multi-ancestor units (runs on every patcher execution)
    validate_no_multiple_ancestors(chain_mapping)

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

