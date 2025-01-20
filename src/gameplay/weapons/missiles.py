"""Functions for editing missile weapons."""
from typing import Any, Dict, List, Tuple
from uuid import uuid4

from src import ndf
from src.constants.weapons.missiles import missiles
from src.constants.weapons.vanilla_inst_modifications import (
    AMMUNITION_MISSILES_REMOVALS,
    AMMUNITION_MISSILES_RENAMES,
)
from src.gameplay.weapons.vanilla_modifications import (
    apply_vanilla_renames,
    remove_vanilla_instances,
)
from src.utils.dictionary_utils import write_dictionary_entries
from src.utils.logging_utils import setup_logger

from ..dics import write_missile_dictionary_entries
from .utils import get_supply_costs

logger = setup_logger(__name__)

def edit_missiles(source_path: Any, game_db: Dict[str, Any]) -> None:
    """Edit AmmunitionMissiles.ndf file."""
    try:
        ammo_db = game_db["ammunition"]
        
        # Handle vanilla modifications
        try:
            apply_vanilla_renames(source_path, AMMUNITION_MISSILES_RENAMES, ammo_db)
            remove_vanilla_instances(source_path, AMMUNITION_MISSILES_REMOVALS)
            logger.debug("Applied vanilla modifications")
        except Exception as e:
            logger.error(f"Failed applying vanilla modifications: {str(e)}")
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
                # Get or create base descriptor
                try:
                    if is_new:
                        base_descr = _create_new_descriptor(source_path, weapon_name, donor)
                    else:
                        base_descr = _get_existing_descriptor(source_path, weapon_name)
                        
                    if not base_descr:
                        logger.error(f"Could not get descriptor for {weapon_name}")
                        continue
                        
                    logger.debug(f"Got base descriptor for {weapon_name}")
                except Exception as e:
                    logger.error(f"Failed getting descriptor for {weapon_name}: {str(e)}")
                    continue
                
                # Apply edits
                try:
                    if "Ammunition" in data:
                        _apply_missile_edits(base_descr, data["Ammunition"], is_new)
                        logger.debug(f"Applied edits to {weapon_name}")
                except Exception as e:
                    logger.error(f"Failed applying edits to {weapon_name}: {str(e)}")
                    continue
                
                # Handle salvo variants
                try:
                    if "WeaponDescriptor" in data and "SalvoLengths" in data["WeaponDescriptor"]:
                        _handle_salvo_variants(source_path, base_descr, weapon_name, data, is_new)
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

def _create_new_descriptor(source_path, weapon_name, donor):
    """Create a new descriptor for a missile."""
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
    try:
        existing = source_path.by_n(f"Ammo_{weapon_name}")
        exists = True
    except:
        exists = False
        existing = None
        
    if not exists:
        logger.error(f"Could not find missile {weapon_name}")
        return None
    return existing

def _handle_salvo_variants(source_path: Any, base_descr: Any, weapon_name: str, 
                         data: Dict, is_new: bool) -> None:
    """Handle salvo variants for missile."""
    logger.info(f"Creating salvo variants for {weapon_name} (is_new={is_new})")
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
        else:
            namespace = f"Ammo_{weapon_name}_x{length}"
            
        try:
            existing = source_path.by_n(namespace)
            exists = True
        except:
            exists = False
            existing = None
            
        logger.debug(f"Checking {namespace} - exists: {exists}")
        
        if is_new or not exists:
            # Create new variant
            variant = base_descr.copy()
            variant.v.by_m("DescriptorId").v = f"GUID:{{{uuid4()}}}"
            variant.v.by_m("HitRollRuleDescriptor").v.by_m("DescriptorId").v = f"GUID:{{{uuid4()}}}"
            variant.namespace = namespace
            
            if base_cost is not None:
                variant.v.by_m("SupplyCost").v = str(int(base_cost) * length)
                
            # Set salvo-specific values
            variant.v.by_m("NbTirParSalves").v = str(length)
            variant.v.by_m("AffichageMunitionParSalve").v = str(length)
            
            source_path.add(variant)
            logger.info(f"Created new variant {namespace}")
        else:
            # Update existing variant
            if base_cost is not None:
                existing.v.by_m("SupplyCost").v = str(int(base_cost) * length)
            existing.v.by_m("NbTirParSalves").v = str(length)
            existing.v.by_m("AffichageMunitionParSalve").v = str(length)
            logger.debug(f"Updated existing variant {namespace}")

def _apply_missile_edits(descr: Any, data: Dict, is_new: bool) -> None:
    """Apply edits to missile descriptor."""
    membr = descr.v.by_m
    
    # Apply Arme edits
    if "Arme" in data:
        arme_data = data["Arme"]
        arme_obj = descr.v.by_m("Arme").v
        
        for arme_membr, arme_v in arme_data.items():
            if isinstance(arme_v, (float, int, bool)):
                arme_obj.by_m(arme_membr).v = str(arme_v)
            else:
                arme_obj.by_m(arme_membr).v = arme_v
    
    # Apply member edits
    if "parent_membr" in data:
        for key, value in data["parent_membr"].items():
            if key == "add":
                index = value[0]
                value = value[1]
                descr.v.insert(index, value)
            elif isinstance(value, (float, int, bool)):
                membr(key).v = str(value)
            elif isinstance(value, tuple) and key == "Caliber":
                membr(key).v = f"'{value[1]}'"
            elif isinstance(value, list):
                # Convert list to NDF format
                list_str = "[" + ", ".join(f"'{item}'" for item in value) + "]"
                logger.debug(f"Converting list {list_str} to NDF")
                membr(key).v = ndf.convert(list_str.encode('utf-8'))[0].v
            else:
                membr(key).v = value
                
    # Apply hit roll edits
    if "hit_roll" in data:
        _apply_hit_roll_edits(descr, data["hit_roll"])
        
    # Apply texture
    if "Texture" in data:
        texture_file = f'"Texture_Interface_Weapon_{data["Texture"]}"'
        membr("InterfaceWeaponTexture").v = texture_file

def _apply_hit_roll_edits(descr: Any, hit_roll_data: Dict) -> None:
    """Apply hit roll edits to descriptor."""
    hitroll_obj = descr.v.by_m("HitRollRuleDescriptor").v
    roll_membrs = hitroll_obj.by_m("BaseHitValueModifiers").v
    
    for roll_type, hit_chance in hit_roll_data.items():
        if roll_type == "Idling":
            roll_membr_list = list(roll_membrs[1].v)
            roll_membr_list[1] = str(hit_chance)
            roll_membrs[1].v = tuple(roll_membr_list)
        elif roll_type == "Moving":
            roll_membr_list = list(roll_membrs[2].v)
            roll_membr_list[1] = str(hit_chance)
            roll_membrs[2].v = tuple(roll_membr_list)

def _track_dictionary_entries(weapon_name, data, ingame_names, calibers):
    """Track dictionary entries for a missile."""
    if "Ammunition" in data:
        ammo_data = data["Ammunition"]
        if "displayname" in ammo_data and "nametoken" in ammo_data:
            ingame_names.append((
                weapon_name,
                ammo_data["nametoken"],
                ammo_data["displayname"]
            ))
        
        if "parent_membr" in ammo_data and "Caliber" in ammo_data["parent_membr"]:
            caliber_data = ammo_data["parent_membr"]["Caliber"]
            if caliber_data[0] != "existing":
                calibers.append((weapon_name, caliber_data[1], caliber_data[0])) 