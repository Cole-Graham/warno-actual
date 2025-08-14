"""Functions for modifying references to vanilla ammunition instances."""

from typing import Any, Dict



def vanilla_renames_weapondescriptor(source_path: Any, logger, game_db: Dict[str, Any]) -> None:
    """Apply vanilla renames to WeaponDescriptor.ndf
    
    Args:
        source_path: NDF file containing weapon descriptors
        ammo_db: Ammunition database containing salvo weapon mappings
        weapon_db: Weapon database containing weapon descriptor data
    """
    ammo_db = game_db["ammunition"]
    weapon_db = game_db["weapons"]
    # renames: List of (old_name, new_name) tuples
    try:
        for descr_namespace, weapon_descr_data in weapon_db.items():
            for weapon_name, entries in weapon_descr_data["weapon_locations"].items():
                # try:
                for entry in entries:
                    if weapon_name in ammo_db["renames_old_new"]:
                        new_name = ammo_db["renames_old_new"][weapon_name]
                        turret_index = entry["turret_index"]
                
                        weapon_descr = source_path.by_namespace(descr_namespace)
                        if weapon_descr:
                            turret = weapon_descr.v.by_m("TurretDescriptorList").v[turret_index]
                            weapon = turret.v.by_m("MountedWeaponDescriptorList").v[entry["mounted_index"]]
                            weapon.v.by_m("Ammunition").v = f"$/GFX/Weapon/Ammo_{new_name}"
                            logger.info(f"Renaming salvo weapon {weapon_name} to {new_name} on turret {turret_index}")
                    else:
                        logger.debug(f"No renaming needed for {weapon_name}")
                # except Exception as e:
                #     logger.error(f"Error renaming weapon {weapon_name}: {e}")
                #     logger.error(traceback.format_exc())
    except Exception as e:
        logger.error(f"Error applying vanilla renames: {e}")
        raise