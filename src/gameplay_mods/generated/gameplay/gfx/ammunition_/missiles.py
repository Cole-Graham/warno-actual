"""Functions for editing missile weapons."""

import re
from typing import Any, Dict, List, Tuple
from uuid import uuid4

from src import ndf
from src.constants.weapons import missiles
from src.constants.weapons.vanilla_inst_modifications import (
    AMMUNITION_MISSILES_REMOVALS,
)
from src.utils.dictionary_utils import write_dictionary_entries
from src.utils.logging_utils import setup_logger

from .ammunition import get_supply_costs
from .handlers import (
    apply_bomb_damage_standards,
    remove_vanilla_instances,
    vanilla_renames_ammunition,
)

logger = setup_logger(__name__)


def edit_gen_gp_gfx_ammunitionmissiles(source_path: Any, game_db: Dict[str, Any]) -> None:
    """Edit AmmunitionMissiles.ndf file."""
    try:
        ammo_db = game_db["ammunition"]

        # Handle vanilla modifications first
        try:
            vanilla_renames_ammunition(source_path, logger, ammo_db)
            remove_vanilla_instances(source_path, logger, AMMUNITION_MISSILES_REMOVALS)
            logger.debug("Applied vanilla modifications")
        except Exception as e:
            logger.error(f"Failed applying vanilla modifications: {str(e)}")
            raise
        
        # Apply global modifications
        try:
            apply_bomb_damage_standards(source_path, logger)
            edit_missile_speed(source_path, game_db)
            logger.debug("Applied global modifications")
        except Exception as e:
            logger.error(f"Failed applying global modifications: {str(e)}")
            raise

        # Track dictionary entries
        ingame_names = []
        calibers = []

        # Process each missile
        for (weapon_name, category, donor, is_new), data in missiles.items():
            if data is None:
                continue

            logger.info(f"Processing missile {weapon_name} (is_new={is_new})")
            try:
                ammo_data = data.get("Ammunition", None)

                # Get or create base descriptor
                try:
                    if is_new:
                        base_descr = _create_new_descriptor(source_path, weapon_name, donor, data)
                    else:
                        base_descr = _get_existing_descriptor(source_path, weapon_name)

                    if not base_descr:
                        logger.error(f"Could not get descriptor for {weapon_name}")
                        continue

                    logger.debug(f"Got base descriptor for {weapon_name}")
                except Exception as e:
                    logger.error(f"Failed getting descriptor for {weapon_name}: {str(e)}")
                    continue

                # Apply edits to base descriptor
                try:
                    if ammo_data:
                        _apply_missile_edits(base_descr, data, ammo_data, is_new)
                        logger.debug(f"Applied edits to {weapon_name}")
                except Exception as e:
                    logger.error(f"Failed applying edits to {weapon_name}: {str(e)}")
                    continue

                # Handle salvo variants - pass the fully edited base descriptor
                try:
                    if "WeaponDescriptor" in data and "SalvoLengths" in data["WeaponDescriptor"]:
                        _handle_salvo_variants(source_path, base_descr, weapon_name, data, is_new)
                    elif is_new:
                        # Only add base descriptor if no salvo variants
                        source_path.add(base_descr)
                except Exception as e:
                    logger.error(f"Failed handling salvo variants for {weapon_name}: {str(e)}")
                    continue

                # Track dictionary entries
                try:
                    _track_dictionary_entries(weapon_name, data, ingame_names, calibers)
                except Exception as e:
                    logger.error(f"Failed tracking dictionary entries for {weapon_name}: {str(e)}")
                    continue

                logger.info(f"Successfully processed missile {weapon_name}")

            except Exception as e:
                logger.error(f"Failed processing missile {weapon_name}: {str(e)}")
                continue

        # Write dictionary entries
        if ingame_names or calibers:
            try:
                write_missile_dictionary_entries(ingame_names, calibers)
            except Exception as e:
                logger.error(f"Failed writing dictionary entries: {str(e)}")
                raise

    except Exception as e:
        logger.error(f"Fatal error in edit_missiles: {str(e)}")
        raise


def _create_new_descriptor(source_path, weapon_name, donor, data):
    """Create a new descriptor for a missile."""
    # For missiles with salvo variants, find any salvo length variant of donor
    donor_descr = None
    if "WeaponDescriptor" in data and "SalvoLengths" in data["WeaponDescriptor"]:
        # Look up donor's salvo lengths from missiles dictionary
        for (name, _, _, _), missile_data in missiles.items():
            if name == donor and "WeaponDescriptor" in missile_data:
                if "SalvoLengths" in missile_data["WeaponDescriptor"]:
                    # Try each salvo length variant of donor
                    for salvo_length in missile_data["WeaponDescriptor"]["SalvoLengths"]:
                        if salvo_length == 1:
                            donor_descr = source_path.by_n(f"Ammo_{donor}")
                        else:
                            donor_descr = source_path.by_n(f"Ammo_{donor}_salvolength{salvo_length}")
                        if donor_descr:
                            break
                break

    if not donor_descr:
        # Try without salvo length suffix
        donor_descr = source_path.by_n(f"Ammo_{donor}")
        if not donor_descr:
            # Try without Ammo_ prefix
            donor_descr = source_path.by_n(donor)
            if not donor_descr:
                logger.error(f"Could not find donor {donor} for {weapon_name}")
                return None

    # Create base descriptor
    base_descr = donor_descr.copy()

    # Generate new GUIDs
    base_descr.v.by_m("DescriptorId").v = f"GUID:{{{uuid4()}}}"
    hitroll_obj = base_descr.v.by_m("HitRollRuleDescriptor").v
    hitroll_obj.by_m("DescriptorId").v = f"GUID:{{{uuid4()}}}"

    # Set namespace
    base_descr.namespace = f"Ammo_{weapon_name}"

    logger.debug(f"Created new base descriptor for {weapon_name} from {donor}")
    return base_descr


def _get_existing_descriptor(source_path, weapon_name):
    """Get an existing descriptor for a missile."""
    # Find the missile data from the tuples
    missile_data = None
    for (name, category, donor, is_new), data in missiles.items():
        if name == weapon_name:
            missile_data = data
            break

    if not missile_data:
        logger.error(f"No missile data found for {weapon_name}")
        return None

    # First try to find any salvo length variant
    if "WeaponDescriptor" in missile_data and "SalvoLengths" in missile_data["WeaponDescriptor"]:
        # Get the lowest salvo length
        salvo_lengths = sorted(missile_data["WeaponDescriptor"]["SalvoLengths"])
        lowest_salvo = salvo_lengths[0]

        try:
            # Try with salvo length suffix first
            if lowest_salvo > 1:
                existing = source_path.by_n(f"Ammo_{weapon_name}_salvolength{lowest_salvo}")
            else:
                existing = source_path.by_n(f"Ammo_{weapon_name}")
            if existing:
                return existing
        except Exception:  # noqa
            pass

    # Fall back to base name if no salvo variants found
    try:
        existing = source_path.by_n(f"Ammo_{weapon_name}")
        if existing:
            return existing
    except Exception:  # noqa
        logger.error(f"Could not find missile {weapon_name}")
        return None

    return None


def _handle_salvo_variants(source_path: Any, base_descr: Any, weapon_name: str, data: Dict, is_new: bool) -> None:
    """Handle salvo variants for missile."""
    logger.info(f"{'Creating' if is_new else 'Editing'} salvo variants for {weapon_name}")
    salvo_lengths = data["WeaponDescriptor"]["SalvoLengths"]
    logger.info(f"Salvo lengths: {salvo_lengths}")

    # Get base supply cost
    supply_costs = get_supply_costs(missiles)
    base_cost = None
    for weapon, cost in supply_costs:
        if weapon == weapon_name:
            base_cost = cost
            break

    for i, length in enumerate(salvo_lengths):
        if length == 1 and i == len(salvo_lengths) - 1:
            namespace = f"Ammo_{weapon_name}"
        elif "salvolength" in weapon_name:
            namespace = f"Ammo_{weapon_name}"
        else:
            namespace = f"Ammo_{weapon_name}_salvolength{length}"

        try:
            if is_new:
                # For new missiles, copy the already-edited base descriptor
                variant = base_descr.copy()
                variant.v.by_m("DescriptorId").v = f"GUID:{{{uuid4()}}}"
                variant.v.by_m("HitRollRuleDescriptor").v.by_m("DescriptorId").v = f"GUID:{{{uuid4()}}}"
                variant.namespace = namespace

                # Only apply salvo-specific values
                if base_cost is not None:
                    variant.v.by_m("SupplyCost").v = str(base_cost * length)
                variant.v.by_m("ShotsCountPerSalvo").v = str(length)
                variant.v.by_m("AffichageMunitionParSalve").v = str(length)

                source_path.add(variant)
                logger.info(f"Created new variant {namespace}")

            else:
                # For existing missiles, update the variant or create it if missing
                existing = source_path.by_n(namespace, strict=False)
                if existing:
                    logger.debug(f"Found existing variant {namespace}")

                    # Apply all base missile edits first
                    if "Ammunition" in data:
                        _apply_missile_edits(existing, data, data["Ammunition"], is_new)

                    # Then update salvo-specific values
                    if base_cost is not None:
                        existing.v.by_m("SupplyCost").v = str(base_cost * length)
                    existing.v.by_m("ShotsCountPerSalvo").v = str(length)
                    existing.v.by_m("AffichageMunitionParSalve").v = str(length)
                    logger.info(f"Updated existing variant {namespace}")
                else:
                    # Variant doesn't exist, create it from the base descriptor
                    logger.info(f"Creating missing salvo variant {namespace}")
                    variant = base_descr.copy()
                    variant.v.by_m("DescriptorId").v = f"GUID:{{{uuid4()}}}"
                    variant.v.by_m("HitRollRuleDescriptor").v.by_m("DescriptorId").v = f"GUID:{{{uuid4()}}}"
                    variant.namespace = namespace

                    # Apply all base missile edits first
                    if "Ammunition" in data:
                        _apply_missile_edits(variant, data, data["Ammunition"], is_new)

                    # Then apply salvo-specific values
                    if base_cost is not None:
                        variant.v.by_m("SupplyCost").v = str(base_cost * length)
                    variant.v.by_m("ShotsCountPerSalvo").v = str(length)
                    variant.v.by_m("AffichageMunitionParSalve").v = str(length)

                    source_path.add(variant)
                    logger.info(f"Created missing variant {namespace}")

        except Exception as e:
            logger.error(f"Error handling salvo variant {namespace}: {str(e)}")
            continue


def _apply_missile_edits(descr: Any, data: Dict, ammo_data: Dict, is_new: bool) -> None:  # noqa
    """Apply edits to missile descriptor."""
    membr = descr.v.by_m

    # Apply Arme edits
    if "Ammunition" in data:

        if "arme" in data["Ammunition"] and "DamageFamily" in data["Ammunition"]["arme"]:
            descr.v.by_m("Arme").v.by_m("Family").v = data["Ammunition"]["arme"]["DamageFamily"]

        if "token" in data["Ammunition"]:
            descr.v.by_m("Name").v = "'" + data["Ammunition"]["token"] + "'"

        arme_data = data["Ammunition"].get("Arme", None)
        if arme_data:
            arme_obj = descr.v.by_m("Arme").v

            for arme_membr, arme_v in arme_data.items():
                if isinstance(arme_v, (float, int, bool)):
                    arme_obj.by_m(arme_membr).v = str(arme_v)
                else:
                    arme_obj.by_m(arme_membr).v = arme_v

        # Apply member edits
        parent_data = data["Ammunition"].get("parent_membr", None)
        if parent_data:
            for key, value in parent_data.items():
                if key == "add":
                    index = value[0]
                    value = value[1]
                    # Extract member name from "MemberName = Value" format
                    member_name = value.split("=")[0].strip()
                    # Check if member already exists before inserting
                    if descr.v.by_m(member_name, False) is None:
                        descr.v.insert(index, value)
                    else:
                        logger.debug(f"Member {member_name} already exists in {descr.n}, skipping insert")
                elif isinstance(value, (float, int, bool)):
                    membr(key).v = str(value)
                elif isinstance(value, tuple) and key == "Caliber":
                    membr(key).v = f"'{value[1]}'"
                elif isinstance(value, list):
                    # Convert list to NDF format
                    list_str = "[" + ", ".join(f"'{item}'" for item in value) + "]"
                    logger.debug(f"Converting list {list_str} to NDF")
                    membr(key).v = ndf.convert(list_str.encode("utf-8"))[0].v
                else:
                    membr(key).v = value

        # Apply hit roll edits
        hit_roll_data = data["Ammunition"].get("hit_roll", None)
        if hit_roll_data:
            _apply_hit_roll_edits(descr, hit_roll_data)

    # Apply texture
    if "NewTexture" in data:
        texture_file = '"' + f"Texture_Interface_Weapon_{data['NewTexture']}" + '"'
        membr("InterfaceWeaponTexture").v = texture_file
        logger.debug(f"Applied texture {texture_file}")

    if "Texture" in data:
        texture_file = '"' + f"Texture_Interface_Weapon_{data['Texture']}" + '"'
        membr("InterfaceWeaponTexture").v = texture_file
        logger.debug(f"Applied texture {texture_file}")


def _apply_hit_roll_edits(descr: Any, hit_roll_data: Dict) -> None:
    """Apply hit roll edits to descriptor."""
    logger.debug(f"Applying hit roll edits to {descr.n}")
    hitroll_obj = descr.v.by_m("HitRollRuleDescriptor")
    roll_membrs = hitroll_obj.v.by_m("BaseHitValueModifiers").v

    for roll_type, hit_chance in hit_roll_data.items():
        if roll_type == "Idling":
            roll_membr_list = list(roll_membrs[1].v)
            roll_membr_list[1] = str(hit_chance)
            roll_membrs[1].v = tuple(roll_membr_list)
        elif roll_type == "Moving":
            roll_membr_list = list(roll_membrs[2].v)
            roll_membr_list[1] = str(hit_chance)
            roll_membrs[2].v = tuple(roll_membr_list)
        elif roll_type == "DistanceToTarget":
            dis_to_target_membr = hitroll_obj.v.by_m("DistanceToTarget", None)
            if dis_to_target_membr:
                dis_to_target_membr.v = str(hit_chance)
            else:
                hitroll_obj.v.add(f"DistanceToTarget = {str(hit_chance)}")


def _track_dictionary_entries(weapon_name, data, ingame_names, calibers):
    """Track dictionary entries for a missile."""
    if "Ammunition" in data:
        ammo_data = data["Ammunition"]
        if "display" in ammo_data and "token" in ammo_data:
            ingame_names.append((weapon_name, ammo_data["token"], ammo_data["display"]))

        if "parent_membr" in ammo_data and "Caliber" in ammo_data["parent_membr"]:
            caliber_data = ammo_data["parent_membr"]["Caliber"]
            if caliber_data[0] != "existing":
                calibers.append((weapon_name, caliber_data[1], caliber_data[0]))


def edit_missile_speed(source: Any, game_db: Dict[str, Any]) -> None:
    """Adjust missile speed and acceleration."""
    logger.info("Adjusting missile speed and acceleration")

    ammo_db = game_db["ammunition"]
    missile_inst_renames = ammo_db.get("renames_new_old", {})

    for missile_decr in source:
        # Strip Ammo_ prefix for comparison
        stripped_namespace = missile_decr.namespace.replace("Descriptor_Missile_", "")

        for (missile, category, donor, is_new), data in missiles.items():
            if data is None or "MissileDescriptor" not in data:
                continue

            # Check for renames
            if stripped_namespace in missile_inst_renames:
                stripped_namespace = missile_inst_renames[stripped_namespace]

            if missile != stripped_namespace:
                continue

            modules_list = missile_decr.v.by_m("ModulesDescriptors")
            for module in modules_list.v:
                if not isinstance(module.v, ndf.model.Object):
                    continue

                if module.v.type != "TGuidedMissileMovementModuleDescriptor":
                    continue

                default_cfg = module.v.by_m("DefaultConfig")
                uncontrollable_cfg = module.v.by_m("UncontrollableConfig")
                if "MaxSpeedGRU" in data["MissileDescriptor"]:
                    max_speed = data["MissileDescriptor"]["MaxSpeedGRU"]
                    default_cfg.v.by_m("MaxSpeedGRU").v = str(max_speed)  # noqa
                    logger.debug(f"Changed {missile_decr.namespace} max speed to {max_speed}")

                    uncontrollable_cfg.v.by_m("MaxSpeedGRU").v = str(max_speed)  # noqa
                    logger.debug(f"Changed {missile_decr.namespace} uncontrollable speed to {max_speed}")

                if "MaxAccelerationGRU" in data["MissileDescriptor"]:
                    max_accel = data["MissileDescriptor"]["MaxAccelerationGRU"]
                    default_cfg.v.by_m("MaxAccelerationGRU").v = str(max_accel)  # noqa
                    logger.debug(f"Changed {missile_decr.namespace} max acceleration to {max_accel}")

                if "AutoGyr" in data["MissileDescriptor"]:
                    auto_gyr = data["MissileDescriptor"]["AutoGyr"]
                    default_cfg.v.by_m("AutoGyr").v = str(auto_gyr)  # noqa
                    logger.debug(f"Changed {missile_decr.namespace} auto gyr to {auto_gyr} (90 degrees)")
            break

def write_missile_dictionary_entries(ingame_names: List[Tuple[str, str, str]], 
                                  calibers: List[Tuple[str, str, str]]) -> None:
    """Write missile dictionary entries."""
    entries = []
    
    # Add weapon names
    for weapon, token, display in ingame_names:
        entries.append((token, display))
        
    # Add caliber entries
    for weapon, token, display in calibers:
        entries.append((token, display))
        
    if entries:
        write_dictionary_entries(entries, dictionary_type="units")