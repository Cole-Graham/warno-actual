import re
from typing import Any, Dict, List, Tuple

from src import ndf
from src.constants.unit_edits import load_unit_edits
from src.constants.weapons import LIGHT_AT_AMMO
from src.constants.weapons import ammunitions as ammos
from src.utils.logging_utils import setup_logger
from src.utils.ndf_utils import find_namespace, is_obj_type, is_valid_turret

from .vanilla_modifications import vanilla_renames_weapondescriptor

logger = setup_logger(__name__)

def unit_edits_weapondescriptor(source_path: Any, game_db: Dict[str, Any]) -> None:
    """Unit Edits for WeaponDescriptor.ndf file.
    
    Args:
        source_path: The NDF file being edited
        game_db: Game database containing ammunition and weapon data
    """

    ammo_db = game_db["ammunition"]
    unit_db = game_db["unit_data"]
    weapon_db = game_db["weapons"]
    
    vanilla_renames_weapondescriptor(source_path, ammo_db, weapon_db)
    
    # Get edits and weapon data
    unit_edits = load_unit_edits()
    weapon_db = game_db.get("weapons", {})
    
    # Gather templates first for equipment changes
    turret_templates = _gather_turret_templates(source_path, ammo_db, weapon_db)
    
    for unit, edits in unit_edits.items():
        if "WeaponDescriptor" not in edits:
            continue
            
        weapon_descr_name = f"WeaponDescriptor_{unit}"
        if weapon_descr_name not in weapon_db:
            logger.warning(f"No weapon data found for {unit}")
            continue
            
        weapon_descr_data = weapon_db[weapon_descr_name]
        
        for weapon_descr in source_path:
            if weapon_descr.namespace != weapon_descr_name:
                continue
                
            logger.debug(f"Processing {unit}")
            _apply_weapon_edits(weapon_descr, edits["WeaponDescriptor"],
                                weapon_descr_data, turret_templates, game_db)
            
            # Adjust light AT weapon salvos based on squad size
            _adjust_light_at_salvos(weapon_descr, unit, ammos,
                                    ammo_db, unit_db, weapon_db)

def _gather_turret_templates(
    source_path: Any,
    ammo_db: Dict[str, Any],
    weapon_db: Dict[str, Any],
) -> List[Tuple[str, Any]]:
    """Gather turret templates for equipment changes using database data."""
    turret_objects = []
    weapons_to_add = []
    
    unit_edits = load_unit_edits()
    for unit, edits in unit_edits.items():
        if not "WeaponDescriptor" in edits:
            continue
            
        equipment_changes = edits["WeaponDescriptor"].get("equipmentchanges", {})
        if not equipment_changes.get("add"):
            continue
            
        weapon_descr_name = f"WeaponDescriptor_{unit}"
        if not weapon_db or weapon_descr_name not in weapon_db:
            logger.warning(f"Weapon {weapon_descr_name} not found in database")
            continue
            
        weapon_descr_data = weapon_db[weapon_descr_name]
        for weapon_descr in source_path:
            try:
                turret_objects.extend(
                    _find_turret_templates(
                        weapon_descr,
                        equipment_changes["add"],
                        weapons_to_add,
                        weapon_descr_data,
                        ammo_db,))
            except Exception as e:
                logger.error(f"Failed to find turret templates for {weapon_descr_name}: {str(e)}")
    
    logger.debug(f"Found templates for weapons: {weapons_to_add}")
    return turret_objects

def _find_turret_templates(
    weapon_descr: Any,
    add_list: List,
    weapons_to_add: List,
    weapon_descr_data: Dict,
    ammo_db: Dict,
) -> List[Tuple[str, Any]]:
    """Find turret templates matching the add list using database data."""
    templates = []
    weapon_locations = weapon_descr_data['weapon_locations']
    
    def add_turret_template(turret, name: str):
        for location in weapon_locations[name]:
            if location['turret_index'] == turret.index:
                new_turret = _prepare_turret_template(turret, name)
                weapons_to_add.append(name)
                templates.append((name, new_turret))
                break
    
    for turret in weapon_descr.v.by_member("TurretDescriptorList").v:
        if not is_valid_turret(turret.v):
            continue
        
        for index_to_insert, ammo_name in add_list:
            ammo_renames = ammo_db["renames_old_new"]
            new_name = ammo_renames.get(ammo_name, None)
            # check if we already have this turret
            names_to_check = [ammo_name, new_name]
            if any(name in weapon_locations for name in names_to_check):
                continue
            
            if new_name and new_name in weapon_locations:
                add_turret_template(turret, new_name)
            
            elif ammo_name in weapon_locations:
                add_turret_template(turret, ammo_name)
    
    return templates

def _prepare_turret_template(turret: Any, index: int) -> Any:
    """Prepare a turret template with updated indices."""
    new_turret = turret.copy()
    
    # Update weapon indices
    mounted_wpns = new_turret.v.by_m("MountedWeaponDescriptorList")
    for weapon in mounted_wpns.v:
        weapon.v.by_m("SalvoStockIndex").v = str(index)
    
    # Update turret bone index
    new_turret.v.by_m("YulBoneOrdinal").v = str(index + 1)
    return new_turret

def _add_new_weapons(weapon_descr: Any, add_list: List, turret_templates: List[Tuple[str, Any]]) -> None:
    """Add new weapons to the descriptor."""
    turret_list = weapon_descr.v.by_member("TurretDescriptorList").v
    
    for ammo_name, turret_template in turret_templates:
        for turret_index, weapon_name in add_list:
            if weapon_name == ammo_name:
                logger.debug(f"Adding {ammo_name} at index {turret_index}")
                turret_list.insert(turret_index, turret_template)

def _update_weapon_quantities(weapon_descr: Any, quantity_changes: Dict, weapon_descr_data: Dict) -> None:
    """Update weapon quantities using database data."""
    weapon_locations = weapon_descr_data['weapon_locations']
    turret_list = weapon_descr.v.by_member("TurretDescriptorList").v
    
    for weapon_name, quants in quantity_changes.items():
        if weapon_name not in weapon_locations:
            continue
            
        quantity = quants[2]  # Using index 2 for quantity
        for location in weapon_locations[weapon_name]:
            for turret in turret_list:
                if int(turret.v.by_m("YulBoneOrdinal").v) != location['turret_index']:
                    continue
                    
                mounted_wpns = turret.v.by_m("MountedWeaponDescriptorList")
                for weapon in mounted_wpns.v:
                    if not is_obj_type(weapon.v, "TMountedWeaponDescriptor"):
                        continue
                        
                    if int(weapon.v.by_m("SalvoStockIndex").v) == location['salvo_index']:
                        new_ammo = f"$/GFX/Weapon/Ammo_{weapon_name}_x{quantity}"
                        logger.debug(f"Setting {weapon_name} quantity to {quantity}")
                        weapon.v.by_m("Ammunition").v = new_ammo
                        weapon.v.by_m("NbWeapons").v = str(quantity)

def _apply_weapon_edits(
    weapon_descr: Any,
    edits: Dict,
    weapon_descr_data: Dict,
    turret_templates: List[Tuple[str, Any]],
    game_db: Dict,
) -> None:
    """Apply weapon edits using database data."""

    # Handle salvo changes first to prevent index errors when editing salves
    if "Salves" in edits:
        _apply_salvo_changes(weapon_descr, edits["Salves"], weapon_descr_data)
    
    # Handle turret changes
    if "turrets" in edits:
        _apply_turret_changes(
            weapon_descr, 
            edits["turrets"], 
            weapon_descr_data)
    
    # Handle equipment changes
    if "equipmentchanges" in edits:
        _apply_equipment_changes(weapon_descr, edits["equipmentchanges"], weapon_descr_data, turret_templates, game_db)

def _apply_turret_changes(weapon_descr: Any, turrets_edits: Dict, weapon_descr_data: Dict) -> None:
    """Apply turret changes using database data."""
    turret_list = weapon_descr.v.by_member("TurretDescriptorList").v
    turret_data = weapon_descr_data["turrets"]
    
    for turret_number, turret_edits in turrets_edits.items():
        if not isinstance(turret_number, int):
            continue
        turret_index = turret_number - 1
        if str(turret_index) not in turret_data: # json keys are always strings
            logger.warning(f"Turret {turret_number} not found in database")
            continue
        turret_list = weapon_descr.v.by_m("TurretDescriptorList")
        weapon_descr_namespace = weapon_descr.namespace
        # weapon/ammo edits
        if "MountedWeapons" in turret_edits:
            for turret_descr in turret_list.v:
                if not is_valid_turret(turret_descr.v):
                    logger.debug(f"Turret {turret_number} is not valid")
                    continue
                
                prefix = "$/GFX/Weapon/Ammo_"
                mounted_wpns = turret_descr.v.by_m("MountedWeaponDescriptorList")
                if "add" in turret_edits["MountedWeapons"]:
                    for weapon in mounted_wpns.v:
                        wpn_index = weapon.index
                        if not is_obj_type(weapon.v, "TMountedWeaponDescriptor"):
                            logger.debug(f"Mounted weapon {wpn_index} is not valid")
                            continue
                        
                        ammunition = weapon.v.by_m("Ammunition").v.split(prefix)[1]
                        for donor, donor_edits in turret_edits["MountedWeapons"]["add"].items():
                            if ammunition != donor:
                                continue
                            new_wpn = weapon.copy()
                            for membr, value in donor_edits.items():
                                if isinstance(value, list):
                                    new_list = ndf.model.List()
                                    for item in value:
                                        new_list.add(f"'{item}'")
                                    new_wpn.v.by_m(membr).v = new_list
                                else:
                                    new_wpn.v.by_m(membr).v = str(value)
                            
                            mounted_wpns.v.add(new_wpn)
                            
                for weapon in mounted_wpns.v:
                    if not is_obj_type(weapon.v, "TMountedWeaponDescriptor"):
                        logger.debug(f"Mounted weapon {weapon.index} is not valid")
                        continue
                    
                    ammunition = weapon.v.by_m("Ammunition").v.split(prefix)[1]
                    for ammo_name, ammo_edits in turret_edits["MountedWeapons"].items():
                        if ammunition != ammo_name:
                            continue
                        for ammo_membr, ammo_value in ammo_edits.items():
                            if isinstance(ammo_value, list):
                                new_list = ndf.model.List()
                                for item in ammo_value:
                                    new_list.add(f"'{item}'")
                                weapon.v.by_m(ammo_membr).v = new_list
                            else:
                                weapon.v.by_m(ammo_membr).v = str(ammo_value)
            
        # turret property edits                        
        for membr, value in turret_edits.items():
            if membr == "MountedWeapons":
                continue
            else:
                turret_list.v[turret_index].v.by_m(membr).v = str(value)
                

    if "remove" in turrets_edits:
        turret_list = weapon_descr.v.by_member("TurretDescriptorList")
        for turret_number in turrets_edits["remove"]:
            turret_index = int(turret_number) - 1
            turret_list.v.remove(turret_index)
                

def _apply_salvo_changes(weapon_descr: Any, salve_edits: Dict, weapon_db: Dict) -> None:
    """Apply salvo changes using database data."""
    salves_list = weapon_descr.v.by_m("Salves")
    weapon_indices = weapon_db['weapon_indices']

    
    # Update salvos first to prevent index errors
    if isinstance(salves_list.v, ndf.model.List):
        salvo_mapping = weapon_db['salvo_mapping']
        for weapon, salvo in salve_edits.items():
            if weapon in ("add", "remove"):
                continue
                
            if weapon in salvo_mapping:
                index = salvo_mapping[weapon]
                logger.debug(f"Updating salvo for {weapon} at index {index}")
                salves_list.v.replace(index, str(salvo))
                
    # Add new salvos
    if "add" in salve_edits:
        for index, salvo in salve_edits["add"]:
            logger.debug(f"Adding salvo {salvo} at index {index}")
            salves_list.v.insert(index, str(salvo))
    
    # Remove salvos for specific weapons
    if "remove" in salve_edits:
        for weapon in salve_edits["remove"]:
            if weapon in weapon_indices:
                for index in sorted(weapon_indices[weapon], reverse=True):
                    logger.debug(f"Removing salvo at index {index}")
                    salves_list.v.remove(index)

def _apply_equipment_changes(
    weapon_descr: Any,
    equipment_changes: Dict,
    weapon_descr_data: Dict,
    turret_templates: List[Tuple[str, Any]],
    game_db: Dict,
) -> None:
    """Apply equipment changes to weapon descriptor."""
    # Handle replacements
    if any(key in equipment_changes for key in ["replace", "replace_fixedsalvo"]):
        _apply_weapon_replacements(weapon_descr, equipment_changes, game_db)
    
    # Handle additions
    if "add" in equipment_changes:
        _add_new_weapons(weapon_descr, equipment_changes["add"], turret_templates)
    
    # Handle quantity changes
    if "quantity" in equipment_changes:
        _update_weapon_quantities(weapon_descr, equipment_changes["quantity"], weapon_descr_data)

def _apply_weapon_replacements(weapon_descr: Any, equipment_changes: Dict, game_db: Dict) -> None:
    """Replace weapons with their replacements."""
    ammo_pattern = re.compile(r'\$/GFX/Weapon/Ammo_(.*?)(?:_x\d+)?$')
    turret_list = weapon_descr.v.by_member("TurretDescriptorList").v
    ammo_db = game_db["ammunition"]
    weapon_db = game_db["weapons"]
    
    def __get_weapon_quantity(
        weapon_descr: Any,
        turret_index: str,
        ammo_name: str,
        ammo_db: Dict,
        weapon_db: Dict,
    ) -> int:
        """Get the quantity of a weapon from the weapons.json"""
        weapon_descr_name = weapon_descr.namespace
        current_turret = weapon_db[weapon_descr_name]['turrets'][turret_index]
        
        if ammo_name in ammo_db['renames_new_old']:
            old_name = ammo_db['renames_new_old'].get(ammo_name, None)
            if old_name:
                current_weapon = current_turret['weapons'][old_name]
            else:
                current_weapon = current_turret['weapons'][ammo_name]
        
        else:
            current_weapon = current_turret['weapons'][ammo_name]
        
        return current_weapon['quantity']
    
    for turret in turret_list:
        if not is_valid_turret(turret.v):
            continue
        
        turret_index = str(turret.index)
        mounted_wpns = turret.v.by_m("MountedWeaponDescriptorList")
        for weapon in mounted_wpns.v:
            if not is_obj_type(weapon.v, "TMountedWeaponDescriptor"):
                continue
                
            ammo_val = weapon.v.by_m("Ammunition").v
            stripped_ammo = ammo_val.split("$/GFX/Weapon/Ammo_", 1)[1]
            
            # Handle fixed salvo replacements (todo: not use lazy eval of "replace_fixedsalvo")
            if "replace_fixedsalvo" in equipment_changes:
                for current, replacement in equipment_changes["replace_fixedsalvo"]:
                    if ammo_val == f"$/GFX/Weapon/Ammo_{current}":
                        weapon.v.by_m("Ammunition").v = f"$/GFX/Weapon/Ammo_{replacement}"
                        logger.debug(f"Replaced {current} with {replacement}")
            
            # Handle regular replacements
            if "replace" in equipment_changes:
                match = ammo_pattern.match(ammo_val)
                if match:
                    ammo_name = match.group(1)
                    for current, replacement in equipment_changes["replace"]:
                        if ammo_name == current:
                            quantity = __get_weapon_quantity(weapon_descr, turret_index,
                                                             ammo_name, ammo_db, weapon_db)
                            if quantity > 1:
                                new_ammo = f"$/GFX/Weapon/Ammo_{replacement}_x{quantity}"
                            else:
                                new_ammo = f"$/GFX/Weapon/Ammo_{replacement}"
                            weapon.v.by_m("Ammunition").v = new_ammo
                            logger.debug(f"Replaced {current} with {replacement}")

def _adjust_light_at_salvos(
    weapon_descr: Any,
    unit_name: str,
    ammos: Dict,
    ammo_db: Dict, 
    unit_db: Dict,
    weapon_db: Dict,
) -> None:
    """Adjust salvo counts for light AT weapons based on squad size."""
    # Get squad size from unit data 
    squad_size = unit_db.get(unit_name, {}).get("strength")
    if not squad_size:
        logger.warning(f"No strength data found for {unit_name}")
        return
    if squad_size not in LIGHT_AT_AMMO:
        logger.info(f"Invalid squad size {squad_size} for {unit_name}")
        return

    # Get this unit's weapon data
    weapon_descr_name = f"WeaponDescriptor_{unit_name}"
    unit_weapon_data = weapon_db.get(weapon_descr_name)
    if not unit_weapon_data:
        logger.warning(f"No weapon data found for {weapon_descr_name}")
        return

    # Get weapon renames mapping
    renames = ammo_db.get("renames_old_new", {})

    # Look through turrets for light AT weapons
    turrets = unit_weapon_data.get("turrets", {})
    for turret in turrets.values():
        for ammo_name, weapon_data in turret.get("weapons", {}).items():
            # Check original name for possible rename, and return the original name if none found
            ammo_to_check = renames.get(ammo_name, ammo_name)
            # todo: weapons.keys() is a dictionary that should probably be called ammunitions or ammos, for clarity
            if any(key[0] == ammo_to_check and key[1] == "light_at" for key in ammos.keys()):
                salvo_index = weapon_data["salvo_index"]
                new_ammo_count = LIGHT_AT_AMMO[squad_size]
                
                # Update the salvo count
                salves_list = weapon_descr.v.by_m("Salves").v
                logger.debug(
                    f"Updating {ammo_name} salvo count to {new_ammo_count} "
                    f"for {squad_size}-man squad")
                salves_list.replace(int(salvo_index), str(new_ammo_count))

