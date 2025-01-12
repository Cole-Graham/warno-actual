import re
from typing import Any, Dict, List, Tuple

from src import ndf
from src.data.data_builder import load_data
from src.dics import load_unit_edits
from src.utils.logging_utils import setup_logger
from src.utils.ndf_utils import get_module_list, is_obj_type, is_valid_turret

logger = setup_logger('weapons_unit_edits')

def _gather_turret_templates(source: Any, weapon_db: Dict[str, Any]) -> List[Tuple[str, Any]]:
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
            
        weapon_name = f"WeaponDescriptor_{unit}"
        if weapon_name not in weapon_db:
            continue
            
        weapon_data = weapon_db[weapon_name]
        for weapon_descr in source:
            turret_objects.extend(
                _find_turret_templates(weapon_descr, equipment_changes["add"], weapons_to_add, weapon_data)
            )
    
    logger.debug(f"Found templates for weapons: {weapons_to_add}")
    return turret_objects

def _find_turret_templates(weapon_descr: Any, add_list: List, weapons_to_add: List, weapon_data: Dict) -> List[Tuple[str, Any]]:
    """Find turret templates matching the add list using database data."""
    templates = []
    weapon_locations = weapon_data['weapon_locations']
    
    for turret in weapon_descr.v.by_member("TurretDescriptorList").v:
        if not is_valid_turret(turret.v):
            continue
            
        yul_bone = int(turret.v.by_m("YulBoneOrdinal").v)
        
        for weapon_name, _ in add_list:
            if weapon_name in weapons_to_add:
                continue
                
            if weapon_name in weapon_locations:
                for location in weapon_locations[weapon_name]:
                    if location['turret_index'] == yul_bone:
                        new_turret = _prepare_turret_template(turret, weapon_name)
                        weapons_to_add.append(weapon_name)
                        templates.append((weapon_name, new_turret))
                        break
    
    return templates

def _is_valid_turret(turret: Any) -> bool:
    """Check if turret is a valid type."""
    return any([
        is_obj_type(turret, "TTurretInfanterieDescriptor"),
        is_obj_type(turret, "TTurretTwoAxisDescriptor"),
        is_obj_type(turret, "TTurretUnitDescriptor")
    ])

def _prepare_turret_template(turret: Any, index: int) -> Any:
    """Prepare a turret template with updated indices."""
    new_turret = turret.copy()
    
    # Update weapon indices
    mounted_wpns = new_turret.v.by_m("MountedWeaponDescriptorList").v
    for weapon in mounted_wpns:
        weapon.v.by_m("SalvoStockIndex").v = str(index)
    
    # Update turret bone index
    new_turret.v.by_m("YulBoneOrdinal").v = str(index + 1)
    return new_turret

def _update_turret_weapons(turret: Any, edits: Dict, weapon_data: Dict) -> None:
    """Update weapons in a turret based on edits using database data."""
    if "MountedWeapons" not in edits:
        return
        
    weapon_edits = edits["MountedWeapons"]
    mounted_wpns = turret.v.by_m("MountedWeaponDescriptorList").v
    weapon_locations = weapon_data['weapon_locations']
    yul_bone = int(turret.v.by_m("YulBoneOrdinal").v)
    
    # Add new weapons
    if "add" in weapon_edits:
        for donor, donor_edits in weapon_edits["add"].items():
            if donor not in weapon_locations:
                continue
                
            for location in weapon_locations[donor]:
                if location['turret_index'] != yul_bone:
                    continue
                    
                for weapon in mounted_wpns:
                    if not is_obj_type(weapon.v, "TMountedWeaponDescriptor"):
                        continue
                        
                    if int(weapon.v.by_m("SalvoStockIndex").v) == location['salvo_index']:
                        new_weapon = weapon.copy()
                        for membr, value in donor_edits.items():
                            new_weapon.v.by_m(membr).v = str(value)
                        mounted_wpns.add(new_weapon)
                        break
    
    # Update existing weapons
    for weapon_name, weapon_edits in weapon_edits.items():
        if weapon_name == "add":
            continue
            
        if weapon_name not in weapon_locations:
            continue
            
        for location in weapon_locations[weapon_name]:
            if location['turret_index'] != yul_bone:
                continue
                
            for weapon in mounted_wpns:
                if not is_obj_type(weapon.v, "TMountedWeaponDescriptor"):
                    continue
                    
                if int(weapon.v.by_m("SalvoStockIndex").v) == location['salvo_index']:
                    for membr, value in weapon_edits.items():
                        weapon.v.by_m(membr).v = str(value)

def _handle_turret_changes(weapon_descr: Any, edits: Dict) -> None:
    """Handle turret additions, removals, and updates."""
    if "turrets" not in edits:
        return
        
    turret_list = weapon_descr.v.by_member("TurretDescriptorList").v
    turrets_to_remove = []
    
    # Handle removals
    if "remove" in edits["turrets"]:
        salves_list = weapon_descr.v.by_m("Salves").v
        for turret in turret_list:
            if not _is_valid_turret(turret.v):
                continue
                
            yul_bone = int(turret.v.by_m("YulBoneOrdinal").v)
            if yul_bone in edits["turrets"]["remove"]:
                turrets_to_remove.append(turret.index)
                salves_list.remove(yul_bone - 1)
    
    # Handle updates
    for turret in turret_list:
        if not _is_valid_turret(turret.v):
            continue
            
        yul_bone = int(turret.v.by_m("YulBoneOrdinal").v)
        if yul_bone not in edits["turrets"]:
            continue
            
        turret_edits = edits["turrets"][yul_bone]
        _update_turret_weapons(turret, turret_edits)
        
        # Update other turret properties
        for membr, value in turret_edits.items():
            if membr != "MountedWeapons":
                turret.v.by_m(membr).v = str(value)
    
    # Remove marked turrets
    for index in reversed(turrets_to_remove):
        turret_list.remove(index)
        logger.debug(f"Removed turret {index}")

def _handle_salvo_changes(weapon_descr: Any, edits: Dict) -> None:
    """Handle salvo list changes."""
    if "Salves" not in edits:
        return
        
    salvo_edits = edits["Salves"]
    salves_list = weapon_descr.v.by_m("Salves").v
    
    # Add new salvos
    if "add" in salvo_edits:
        for index, salvo in salvo_edits["add"]:
            logger.debug(f"Adding salvo {salvo} at index {index}")
            salves_list.insert(index, str(salvo))
    
    # Remove salvos for specific weapons
    if "remove" in salvo_edits:
        weapon_indices = _get_weapon_salvo_indices(weapon_descr, salvo_edits["remove"])
        for index in sorted(weapon_indices, reverse=True):
            logger.debug(f"Removing salvo at index {index}")
            salves_list.remove(index)
    
    # Update existing salvos
    if isinstance(salves_list, ndf.model.List):
        weapon_indices = _get_weapon_salvo_mapping(weapon_descr)
        for weapon, salvo in salvo_edits.items():
            if weapon in ("add", "remove"):
                continue
                
            for ammo_name, index in weapon_indices:
                if _match_weapon_name(ammo_name, weapon):
                    logger.debug(f"Updating salvo for {weapon} at index {index}")
                    salves_list.replace(int(index), str(salvo))

def _get_weapon_salvo_indices(weapon_descr: Any, weapons: List[str]) -> List[int]:
    """Get salvo indices for specified weapons."""
    indices = []
    
    for turret in weapon_descr.v.by_member("TurretDescriptorList").v:
        if not _is_valid_turret(turret.v):
            continue
            
        for weapon in turret.v.by_m("MountedWeaponDescriptorList").v:
            if not is_obj_type(weapon.v, "TMountedWeaponDescriptor"):
                continue
                
            ammo = weapon.v.by_m("Ammunition").v.split("$/GFX/Weapon/Ammo_", 1)[1]
            if any(ammo.startswith(w) for w in weapons):
                indices.append(int(weapon.v.by_m("SalvoStockIndex").v))
                
    return indices

def _get_weapon_salvo_mapping(weapon_descr: Any) -> List[Tuple[str, str]]:
    """Get mapping of weapon names to salvo indices."""
    mapping = []
    
    for turret in weapon_descr.v.by_member("TurretDescriptorList").v:
        if not _is_valid_turret(turret.v):
            continue
            
        for weapon in turret.v.by_m("MountedWeaponDescriptorList").v:
            if not is_obj_type(weapon.v, "TMountedWeaponDescriptor"):
                continue
                
            ammo = weapon.v.by_m("Ammunition").v.split("$/GFX/Weapon/Ammo_", 1)[1]
            index = weapon.v.by_m("SalvoStockIndex").v
            mapping.append((ammo, index))
                
    return mapping

def _match_weapon_name(ammo_name: str, weapon: str) -> bool:
    """Match weapon name accounting for quantity suffix."""
    pattern = r"^(.*?)(?:_x\d+)?$"
    match = re.match(pattern, ammo_name)
    return match and match.group(1) == weapon

def _handle_equipment_changes(weapon_descr: Any, edits: Dict, turret_templates: List[Tuple[str, Any]]) -> None:
    """Handle equipment changes."""
    if "equipmentchanges" not in edits:
        return
        
    equipment_changes = edits["equipmentchanges"]
    
    # Handle weapon replacements
    if any(key in equipment_changes for key in ["replace", "replace_fixedsalvo"]):
        _handle_weapon_replacements(weapon_descr, equipment_changes)
    
    # Add new weapons
    if "add" in equipment_changes:
        _add_new_weapons(weapon_descr, equipment_changes["add"], turret_templates)
    
    # Update weapon quantities
    if "quantity" in equipment_changes:
        _update_weapon_quantities(weapon_descr, equipment_changes["quantity"])

def _handle_weapon_replacements(weapon_descr: Any, edits: Dict, weapon_data: Dict) -> None:
    """Handle weapon replacements using database data."""
    weapon_locations = weapon_data['weapon_locations']
    turret_list = weapon_descr.v.by_member("TurretDescriptorList").v
    
    # Handle fixed salvo replacements
    if "replace_fixedsalvo" in edits:
        for current, replacement in edits["replace_fixedsalvo"]:
            if current not in weapon_locations:
                continue
                
            for location in weapon_locations[current]:
                for turret in turret_list:
                    if int(turret.v.by_m("YulBoneOrdinal").v) != location['turret_index']:
                        continue
                        
                    mounted_wpns = turret.v.by_m("MountedWeaponDescriptorList").v
                    for weapon in mounted_wpns:
                        if not is_obj_type(weapon.v, "TMountedWeaponDescriptor"):
                            continue
                            
                        if int(weapon.v.by_m("SalvoStockIndex").v) == location['salvo_index']:
                            new_ammo = f"$/GFX/Weapon/Ammo_{replacement}"
                            logger.debug(f"Replacing {current} with {replacement}")
                            weapon.v.by_m("Ammunition").v = new_ammo
    
    # Handle pattern-based replacements
    if "replace" in edits:
        for current, replacement in edits["replace"]:
            if current not in weapon_locations:
                continue
                
            for location in weapon_locations[current]:
                for turret in turret_list:
                    if int(turret.v.by_m("YulBoneOrdinal").v) != location['turret_index']:
                        continue
                        
                    mounted_wpns = turret.v.by_m("MountedWeaponDescriptorList").v
                    for weapon in mounted_wpns:
                        if not is_obj_type(weapon.v, "TMountedWeaponDescriptor"):
                            continue
                            
                        if int(weapon.v.by_m("SalvoStockIndex").v) == location['salvo_index']:
                            new_ammo = f"$/GFX/Weapon/Ammo_{replacement}"
                            logger.debug(f"Replacing {current} with {replacement}")
                            weapon.v.by_m("Ammunition").v = new_ammo

def _add_new_weapons(weapon_descr: Any, add_list: List, turret_templates: List[Tuple[str, Any]]) -> None:
    """Add new weapons to the descriptor."""
    turret_list = weapon_descr.v.by_member("TurretDescriptorList").v
    
    for ammo_name, turret_template in turret_templates:
        for turret_index, weapon_name in add_list:
            if weapon_name == ammo_name:
                logger.debug(f"Adding {ammo_name} at index {turret_index}")
                turret_list.insert(turret_index, turret_template)

def _update_weapon_quantities(weapon_descr: Any, quantity_changes: Dict, weapon_data: Dict) -> None:
    """Update weapon quantities using database data."""
    weapon_locations = weapon_data['weapon_locations']
    turret_list = weapon_descr.v.by_member("TurretDescriptorList").v
    
    for weapon_name, quants in quantity_changes.items():
        if weapon_name not in weapon_locations:
            continue
            
        quantity = quants[2]  # Using index 2 for quantity
        for location in weapon_locations[weapon_name]:
            for turret in turret_list:
                if int(turret.v.by_m("YulBoneOrdinal").v) != location['turret_index']:
                    continue
                    
                mounted_wpns = turret.v.by_m("MountedWeaponDescriptorList").v
                for weapon in mounted_wpns:
                    if not is_obj_type(weapon.v, "TMountedWeaponDescriptor"):
                        continue
                        
                    if int(weapon.v.by_m("SalvoStockIndex").v) == location['salvo_index']:
                        new_ammo = f"$/GFX/Weapon/Ammo_{weapon_name}_x{quantity}"
                        logger.debug(f"Setting {weapon_name} quantity to {quantity}")
                        weapon.v.by_m("Ammunition").v = new_ammo
                        weapon.v.by_m("NbWeapons").v = str(quantity)

def edit_units(source: Any) -> None:
    """Edit weapon descriptors for units."""
    logger.info("Editing weapon descriptors")
    
    # Get edits and weapon data
    unit_edits = load_unit_edits()
    weapon_db = load_data({}, "weapons")  # Empty config is fine since we fixed the path
    
    # Gather templates first for equipment changes
    turret_templates = _gather_turret_templates(source, weapon_db)
    
    for unit, edits in unit_edits.items():
        if "WeaponDescriptor" not in edits:
            continue
            
        weapon_name = f"WeaponDescriptor_{unit}"
        if weapon_name not in weapon_db:
            logger.warning(f"No weapon data found for {unit}")
            continue
            
        weapon_data = weapon_db[weapon_name]
        
        for weapon_descr in source:
            if weapon_descr.namespace != weapon_name:
                continue
                
            logger.debug(f"Processing {unit}")
            _apply_weapon_edits(weapon_descr, edits["WeaponDescriptor"], weapon_data)

def _apply_weapon_edits(weapon_descr: Any, edits: Dict, weapon_data: Dict) -> None:
    """Apply weapon edits using database data."""
    # Handle turret changes
    if "turrets" in edits:
        _apply_turret_changes(weapon_descr, edits["turrets"], weapon_data["turrets"])
    
    # Handle salvo changes
    if "Salves" in edits:
        _apply_salvo_changes(weapon_descr, edits["Salves"], weapon_data)
    
    # Handle equipment changes
    if "equipmentchanges" in edits:
        _apply_equipment_changes(weapon_descr, edits["equipmentchanges"], weapon_data)

def _apply_turret_changes(weapon_descr: Any, edits: Dict, weapon_data: Dict) -> None:
    """Apply turret changes using database data."""
    turret_list = weapon_descr.v.by_member("TurretDescriptorList").v
    turret_data = weapon_data['turrets']
    
    # Handle removals
    if "remove" in edits:
        for yul_bone in edits["remove"]:
            if str(yul_bone) in turret_data:
                for turret in turret_list:
                    if int(turret.v.by_m("YulBoneOrdinal").v) == yul_bone:
                        logger.debug(f"Removing turret {yul_bone}")
                        turret_list.remove(turret.index)
                        break
    
    # Handle updates
    for yul_bone, turret_edits in edits.items():
        if yul_bone == "remove":
            continue
            
        if str(yul_bone) not in turret_data:
            logger.warning(f"Turret {yul_bone} not found in database")
            continue
            
        for turret in turret_list:
            if int(turret.v.by_m("YulBoneOrdinal").v) != int(yul_bone):
                continue
                
            _update_turret_weapons(turret, turret_edits, weapon_data)
            
            # Update other properties
            for membr, value in turret_edits.items():
                if membr != "MountedWeapons":
                    turret.v.by_m(membr).v = str(value)

def _apply_salvo_changes(weapon_descr: Any, edits: Dict, weapon_data: Dict) -> None:
    """Apply salvo changes using database data."""
    salves_list = weapon_descr.v.by_m("Salves").v
    weapon_indices = weapon_data['weapon_indices']
    
    # Add new salvos
    if "add" in edits:
        for index, salvo in edits["add"]:
            logger.debug(f"Adding salvo {salvo} at index {index}")
            salves_list.insert(index, str(salvo))
    
    # Remove salvos for specific weapons
    if "remove" in edits:
        for weapon in edits["remove"]:
            if weapon in weapon_indices:
                for index in sorted(weapon_indices[weapon], reverse=True):
                    logger.debug(f"Removing salvo at index {index}")
                    salves_list.remove(index)
    
    # Update existing salvos
    if isinstance(salves_list, ndf.model.List):
        salvo_mapping = weapon_data['salvo_mapping']
        for weapon, salvo in edits.items():
            if weapon in ("add", "remove"):
                continue
                
            if weapon in salvo_mapping:
                index = salvo_mapping[weapon]
                logger.debug(f"Updating salvo for {weapon} at index {index}")
                salves_list.replace(int(index), str(salvo))

def _apply_equipment_changes(weapon_descr: Any, edits: Dict, weapon_data: Dict) -> None:
    """Apply equipment changes using database data."""
    # Handle replacements
    if any(key in edits for key in ["replace", "replace_fixedsalvo"]):
        _handle_weapon_replacements(weapon_descr, edits, weapon_data)
    
    # Handle quantity changes
    if "quantity" in edits:
        _update_weapon_quantities(weapon_descr, edits["quantity"], weapon_data)

# ... more helper functions ... 