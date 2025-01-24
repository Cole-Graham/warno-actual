"""Editor for Ammunition.ndf."""

from typing import Any, Dict, List, Optional
from uuid import uuid4

from src import ndf
from src.constants.weapons.ammunition import ammunitions
from src.constants.weapons.vanilla_inst_modifications import AMMUNITION_REMOVALS
from src.utils.dictionary_utils import write_dictionary_entries
from src.utils.logging_utils import setup_logger
from src.utils.ndf_utils import is_valid_turret

from ..dics import write_ammo_dictionary_entries
from .damage_families import apply_damage_families
from .mg_teams import edit_mg_team_weapons
from .mortar_mods import add_corrected_shot_dispersion
from .utils import get_supply_costs
from .vanilla_modifications import remove_vanilla_instances, vanilla_renames_ammunition

logger = setup_logger(__name__)

def _generate_guid():
    """Generate a new GUID."""
    return str(uuid4())

def edit_ammunition(source_path, game_db: Dict[str, Any]) -> None:
    """Edit Ammunition.ndf file."""
    try:
        ammo_db = game_db["ammunition"]
        
        # Handle vanilla modifications first
        try:
            vanilla_renames_ammunition(source_path, ammo_db)
            remove_vanilla_instances(source_path, AMMUNITION_REMOVALS)
            logger.debug("Applied vanilla modifications")
        except Exception as e:
            logger.error(f"Failed applying vanilla modifications: {str(e)}")
            raise
        
        # Apply global modifications
        try:
            add_corrected_shot_dispersion(source_path, game_db)
            edit_mg_team_weapons(source_path, game_db)
            apply_damage_families(source_path, game_db)
            logger.debug("Applied global modifications")
        except Exception as e:
            logger.error(f"Failed applying global modifications: {str(e)}")
            raise
        
        # Track dictionary entries
        ingame_names = []
        calibers = []
        
        # Process each weapon
        for (weapon_name, category, donor, is_new), data in ammunitions.items():
            if "Ammunition" not in data:
                continue
                
            logger.info(f"Processing weapon {weapon_name} (is_new={is_new})")
            try:
                ammo_data = data["Ammunition"]
                
                # Get or create base descriptor
                try:
                    if is_new:
                        base_descr = _create_new_descriptor(source_path, data,
                                                            weapon_name, donor)
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
                    _apply_weapon_edits(base_descr, data, ammo_data)
                    logger.debug(f"Applied edits to {weapon_name}")
                except Exception as e:
                    logger.error(f"Failed applying edits to {weapon_name}: {str(e)}")
                    continue
                
                # Handle new weapons and quantities
                try:
                    if is_new:
                        # For new weapons, only add base descriptor if there are no quantities
                        if "NbWeapons" not in data or len(data["NbWeapons"]) == 1:
                            source_path.add(base_descr)
                            logger.debug(f"Added new base descriptor for {weapon_name}")
                    
                    if "NbWeapons" in data:
                        base_cost = _get_base_supply_cost(weapon_name)
                        if len(data["NbWeapons"]) > 1:
                            _create_quantity_variants(source_path, base_descr, weapon_name, 
                                                data["NbWeapons"], base_cost, is_new)
                        elif category == "small_arms" and data["NbWeapons"][0] > 1:
                            base_descr.namespace = f"Ammo_{weapon_name}_x{data['NbWeapons'][0]}"
                            logger.debug(f"Updated namespace for {weapon_name} to {base_descr.namespace}")
                            
                except Exception as e:
                    logger.error(f"Failed handling quantities for {weapon_name}: {str(e)}")
                    continue
                
                # Track dictionary entries
                try:
                    _track_dictionary_entries(weapon_name, ammo_data, ingame_names, calibers)
                except Exception as e:
                    logger.error(f"Failed tracking dictionary entries for {weapon_name}: {str(e)}")
                    continue
                
                logger.info(f"Successfully processed weapon {weapon_name}")
                
            except Exception as e:
                logger.error(f"Failed processing weapon {weapon_name}: {str(e)}")
                continue
        
        # Write dictionary entries
        if ingame_names or calibers:
            try:
                write_ammo_dictionary_entries(ingame_names, calibers)
            except Exception as e:
                logger.error(f"Failed writing dictionary entries: {str(e)}")
                raise
                
    except Exception as e:
        logger.error(f"Fatal error in edit_ammunition: {str(e)}")
        raise

def _create_quantity_variants(source_path, base_descr, weapon_name, quantities, base_cost, is_new):
    """Create quantity variants from base ammunition descriptor."""
    logger.info(f"Creating quantity variants for {weapon_name} (is_new={is_new})")
    logger.info(f"Quantities: {quantities}")
    
    for i, quantity in enumerate(quantities):
        if quantity == 1 and i == len(quantities) - 1:
            namespace = f"Ammo_{weapon_name}"
        else:
            namespace = f"Ammo_{weapon_name}_x{quantity}"
            
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
                variant.v.by_m("SupplyCost").v = str(int(base_cost) * quantity)
                
            source_path.add(variant)
            logger.info(f"Created new variant {namespace}")
        else:
            # Just update supply cost
            if base_cost is not None:
                existing.v.by_m("SupplyCost").v = str(int(base_cost) * quantity)
            logger.debug(f"Updated existing variant {namespace}")

def update_weapondescr_ammoname_quantity(source_path, game_db):
    """Update the quantities in ammo names for WeaponDescriptor.ndf"""
    logger.info("Updating quantities in ammo namespaces in WeaponDescriptor.ndf")
    ammo_db = game_db["ammunition"]
    weapon_db = game_db["weapons"]
    
    for weapon_descr_name, weapon_descr_data in weapon_db.items():
        for (weapon_name, category, donor, is_new), data in ammunitions.items():
            if category != "small_arms": 
                continue
            
            for turret_index, turret_data in weapon_descr_data["turrets"].items():
        
                old_name = ammo_db["renames_new_old"].get(weapon_name, None)
                    
                if not old_name and weapon_name in turret_data["weapons"]:
                    quantity = turret_data["weapons"][weapon_name].get("quantity", None)
                    if quantity is None:
                        logger.debug(f"No quantity found for {weapon_name}")
                        continue
                
                elif old_name in turret_data["weapons"]:
                    quantity = turret_data["weapons"][old_name].get("quantity", None)
                    if quantity is None:
                        logger.debug(f"No quantity found for {weapon_name} or {old_name}")
                        continue
                
                else:
                    continue
                
                if quantity and quantity > 1:
                    weapon_descr = source_path.by_n(weapon_descr_name)
                    turret_list = weapon_descr.v.by_m("TurretDescriptorList")
                    turret = turret_list.v[int(turret_index)]
                    
                    for mounted_wpn in turret.v.by_m("MountedWeaponDescriptorList").v:
                        ammo = mounted_wpn.v.by_m("Ammunition").v
                        ammo_n = ammo.split("_", 1)[1]
                        prefix = ammo.split("_", 1)[0]
                        nb_weapons = mounted_wpn.v.by_m("NbWeapons").v
                        
                        if old_name and old_name == ammo_n:
                            if int(nb_weapons) == quantity:
                                new_ammo = f"{prefix}_{weapon_name}_x{quantity}"
                                mounted_wpn.v.by_m("Ammunition").v = new_ammo
                                logger.info(f"Updated ammo {ammo} to {new_ammo}\n")
                            else:
                                logger.debug(f"database quantity ({quantity}) differs from "
                                             f"NbWeapons ({nb_weapons}) for {weapon_name}")
                                if int(nb_weapons) > 1:
                                    new_ammo = f"{prefix}_{weapon_name}_x{quantity}"
                                    mounted_wpn.v.by_m("Ammunition").v = new_ammo
                                    logger.info(f"Updated ammo {ammo} to {new_ammo}\n")
                                else:
                                    logger.debug(f"Quantity is {quantity}, no changes "
                                                 f"applied for {weapon_name}\n")
                        
                        elif ammo_n == weapon_name:
                            if int(nb_weapons) == quantity:
                                new_ammo = f"{prefix}_{weapon_name}_x{quantity}"
                                mounted_wpn.v.by_m("Ammunition").v = new_ammo
                                logger.info(f"Updated ammo {ammo} to {new_ammo}\n")
                                
                        else:
                            logger.debug(f"No changes applied for {weapon_name}\n")
        
        

def _apply_weapon_edits(descr: Any, data: Dict, ammo_data: Dict) -> None:
    """Apply edits from ammunition data to descriptor."""
    membr = descr.v.by_m
    
    logger.debug(f"Applying edits to {descr.n}")
    
    # Apply Arme edits
    if "Arme" in ammo_data:
        arme_data = ammo_data["Arme"]
        arme_obj = descr.v.by_m("Arme").v
        
        for arme_membr, arme_v in arme_data.items():
            if isinstance(arme_v, (float, int, bool)):
                arme_obj.by_m(arme_membr).v = str(arme_v)
            else:
                arme_obj.by_m(arme_membr).v = arme_v
    
    # Apply parent member edits
    if "parent_membr" in ammo_data:
        for key, value in ammo_data["parent_membr"].items():
            logger.debug(f"Setting {key} = {value}")
            if key == "add": # adding new member, e.g. [16, "PorteeMaximaleTBAGRU = 875"]
                index = value[0]
                value = value[1]
                descr.v.insert(index, value)
                continue
            elif isinstance(value, (float, int, bool)):
                membr(key).v = str(value)
            elif isinstance(value, tuple) and key == "Caliber":
                membr(key).v = f"'{value[1]}'"
            elif isinstance(value, list):
                # Convert list to NDF format
                list_str = "[" + ", ".join(f"'{item}'" for item in value) + "]"
                logger.debug(f"Converting list {list_str} to NDF")
                membr(key).v = ndf.convert(list_str.encode('utf-8'))[0].v
    
    # Apply hit roll edits
    if "hit_roll" in ammo_data:
        _apply_hit_roll_edits(descr, ammo_data["hit_roll"])
        
    # Apply texture
    if "Texture" in data:
        texture_file = f'"Texture_Interface_Weapon_{data["Texture"]}"'
        membr("InterfaceWeaponTexture").v = texture_file
        logger.debug(f"Applied texture {texture_file}")

def _apply_hit_roll_edits(descr: Any, hit_roll_data: Dict) -> None:
    """Apply hit roll edits to ammunition descriptor."""
    hitroll_obj = descr.v.by_m("HitRollRuleDescriptor").v
    
    if "BaseCriticModifier" in hit_roll_data:
        hitroll_obj.by_m("BaseCriticModifier").v = str(hit_roll_data["BaseCriticModifier"])
        
    modifiers = hitroll_obj.by_m("BaseHitValueModifiers").v
    if "Idling" in hit_roll_data:
        modifiers[1].v = (modifiers[1].v[0], str(hit_roll_data["Idling"]))
    if "Moving" in hit_roll_data:
        modifiers[2].v = (modifiers[2].v[0], str(hit_roll_data["Moving"]))

def _track_dictionary_entries(weapon_name, ammo_data, ingame_names, calibers):
    """Track dictionary entries for ammunition."""
    if "display" in ammo_data and "token" in ammo_data:
        ingame_names.append((
            weapon_name, 
            ammo_data["token"],
            ammo_data["display"]
        ))
    
    if "parent_membr" in ammo_data and "Caliber" in ammo_data["parent_membr"]:
        caliber_data = ammo_data["parent_membr"]["Caliber"]
        if caliber_data[0] != "existing":
            calibers.append((weapon_name, caliber_data[1], caliber_data[0]))

def _get_base_supply_cost(weapon_name):
    """Get the base supply cost for ammunition."""
    supply_costs = get_supply_costs(ammunitions)
    for weapon, cost in supply_costs:
        if weapon == weapon_name:
            return cost
    return None

def _create_new_descriptor(source_path, data, weapon_name, donor):
    """Create a new descriptor for ammunition."""
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
    if "NbWeapons" in data and len(data["NbWeapons"]) == 1:
        if data["NbWeapons"][0] > 1:
            base_descr.namespace = f"Ammo_{weapon_name}_x{data['NbWeapons'][0]}"
        else:
            base_descr.namespace = f"Ammo_{weapon_name}"
    else:
        base_descr.namespace = f"Ammo_{weapon_name}"
    
    logger.debug(f"Created new base descriptor for {weapon_name} from {donor}")
    return base_descr

def _get_existing_descriptor(source_path, weapon_name):
    """Get an existing descriptor for ammunition."""
    base_descr = source_path.by_n(f"Ammo_{weapon_name}")
    if not base_descr:
        # Try without Ammo_ prefix
        base_descr = source_path.by_n(weapon_name)
        if not base_descr:
            logger.error(f"Could not find weapon {weapon_name}")
            return None
    return base_descr 

def apply_default_salves(
    source_path: Any,
    game_db: Dict[str, Any],
) -> None:
    """Apply default salves to WeaponDescriptor.ndf"""
    
    def __edit_salves(
        source_path: Any,
        weapon_descr_name: str,
        ammo_name: str,
        salvo_stock_index: int,
        default_salves: List[int]
    ) -> None:
        weapon_descr = source_path.by_n(weapon_descr_name)
        salves = weapon_descr.v.by_m("Salves")
        salves.v[salvo_stock_index].v = str(default_salves)
        logger.info(f"Applied default salves for {ammo_name} to {weapon_descr_name}")
    
    ammo_db = game_db["ammunition"]
    for (ammo_name, category, donor, is_new), data in ammunitions.items():
        if not (data.get("WeaponDescriptor") and "Salves" in data["WeaponDescriptor"]):
            continue
        
        old_name = ammo_db["renames_new_old"].get(ammo_name, None)
        
        default_salves = data["WeaponDescriptor"]["Salves"]
        for weapon_descr_name, weapon_descr_data in ammo_db["salves_map"].items():
            
            if old_name and old_name in weapon_descr_data["salves"]:
                salvo_stock_index = weapon_descr_data["salves"][old_name][0]
                __edit_salves(source_path, weapon_descr_name, old_name,
                            salvo_stock_index, default_salves)
           
            elif ammo_name in weapon_descr_data["salves"]:
                salvo_stock_index = weapon_descr_data["salves"][ammo_name][0]
                __edit_salves(source_path, weapon_descr_name, ammo_name,
                            salvo_stock_index, default_salves)
