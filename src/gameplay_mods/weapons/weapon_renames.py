from typing import Any, Dict

from src.utils.logging_utils import setup_logger
from src.utils.ndf_utils import is_obj_type, is_valid_turret, strip_quotes

logger = setup_logger(__name__)

def apply_weapon_renames(source_path: Any, game_db: Dict[str, Any]) -> None:
    """Apply weapon and ammunition renames to WeaponDescriptor.ndf file.
    
    Args:
        source_path: The NDF file being edited
        game_db: Game database containing ammunition and weapon data
    """
    ammo_db = game_db["ammunition"]
    weapon_db = game_db["weapons"]
    
    # Process each weapon descriptor
    for weapon_descr in source_path:
        if not weapon_descr.namespace.startswith("WeaponDescriptor_"):
            continue
            
        if weapon_descr.namespace not in weapon_db:
            continue
            
        # Process each turret
        for turret in weapon_descr.v.by_m("TurretDescriptorList").v:
            if not is_valid_turret(turret.v):
                continue
                
            mounted_wpns = turret.v.by_m("MountedWeaponDescriptorList")
            
            # Check each weapon in the turret
            for weapon in mounted_wpns.v:
                if not is_obj_type(weapon.v, "TMountedWeaponDescriptor"):
                    continue
                    
                ammo_path = weapon.v.by_m("Ammunition").v
                if not ammo_path.startswith("$/GFX/Weapon/Ammo_"):
                    continue
                    
                # Extract ammo name from path
                ammo_name = ammo_path.split("$/GFX/Weapon/Ammo_")[1]
                base_ammo_name = ammo_name.split("_x")[0]  # Remove any _x{number} suffix
                
                # Check if this ammo has a new name
                if base_ammo_name in ammo_db["renames_old_new"]:
                    new_name = ammo_db["renames_old_new"][base_ammo_name]
                    
                    # Preserve quantity suffix if it exists
                    if "_x" in ammo_name:
                        quantity = ammo_name.split("_x")[1]
                        new_ammo_path = f"$/GFX/Weapon/Ammo_{new_name}_x{quantity}"
                    else:
                        new_ammo_path = f"$/GFX/Weapon/Ammo_{new_name}"
                        
                    weapon.v.by_m("Ammunition").v = new_ammo_path
                    logger.debug(f"Renamed ammo from {base_ammo_name} to {new_name}")

def rename_missile_variants(source_path: Any, game_db: Dict[str, Any]) -> None:
    """Add HAGRU missile variants to MANPAD turrets.
    
    Args:
        source_path: The NDF file being edited
        game_db: Game database containing ammunition and weapon data
    """
    ammo_db = game_db["ammunition"]
    weapon_db = game_db["weapons"]
    
    for weapon_descr in source_path:
        if not weapon_descr.namespace.startswith("WeaponDescriptor_"):
            continue
            
        if weapon_descr.namespace not in weapon_db:
            continue
            
        weapon_data = weapon_db[weapon_descr.namespace]
        
        # Process each turret
        for turret_idx, turret_data in weapon_data["turrets"].items():
            turret = weapon_descr.v.by_m("TurretDescriptorList").v[int(turret_idx)]
            if not is_valid_turret(turret.v):
                continue
                
            mounted_wpns = turret.v.by_m("MountedWeaponDescriptorList")
            wpns_to_add = []
            
            # Check each weapon in the turret
            for ammo_name, weapon_info in turret_data["weapons"].items():
                # Strip _x{number} suffix for dictionary lookup
                base_ammo_name = ammo_name.split("_x")[0]
                
                # Get salvo length from weapon info
                salvo_length = weapon_info.get('regex_quantity', 1)
                
                # Check if this is a MANPAD missile that needs HAGRU variant
                if _is_manpad_missile(base_ammo_name, game_db):
                    # Find and copy the weapon
                    for weapon in mounted_wpns.v:
                        if not is_obj_type(weapon.v, "TMountedWeaponDescriptor"):
                            continue
                        
                        ammo_path = f"$/GFX/Weapon/Ammo_{ammo_name}"
                        if weapon.v.by_m("Ammunition").v == ammo_path:
                            new_wpn = weapon.copy()
                            # Add HAGRU variant with appropriate salvo length
                            if salvo_length == 1:
                                new_ammo = f"$/GFX/Weapon/Ammo_{base_ammo_name}_HAGRU"
                            else:
                                new_ammo = (f"$/GFX/Weapon/Ammo_{base_ammo_name}_HAGRU"
                                          f"_salvolength{salvo_length}")
                            new_wpn.v.by_m("Ammunition").v = new_ammo
                            wpns_to_add.append(new_wpn)
                            logger.debug(
                                f"Adding HAGRU missile {base_ammo_name}_HAGRU to "
                                f"{weapon_descr.namespace}"
                            )
                            break
            
            # Add all new weapons after iteration
            for new_wpn in wpns_to_add:
                mounted_wpns.v.add(new_wpn)

def _is_manpad_missile(ammo_name: str, game_db: Dict[str, Any]) -> bool:
    """Check if an ammunition is a MANPAD missile that should get HAGRU variant.
    
    Args:
        ammo_name: Name of the ammunition to check
        game_db: Game database containing ammunition data
        
    Returns:
        bool: True if this is a MANPAD missile that should get HAGRU variant
    """
    missiles = game_db.get("missiles", {})
    for (missile_name, _, _, _), missile_data in missiles.items():
        if (missile_name == ammo_name and
            "Ammunition" in missile_data and
            "arme" in missile_data["Ammunition"] and
            missile_data["Ammunition"]["arme"].get(
                "DamageFamily") == "DamageFamily_manpad_tbagru"):
            return True
    return False 