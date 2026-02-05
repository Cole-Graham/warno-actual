import re
from typing import Any, Dict
from src import ndf
from src.constants.weapons import missiles
from src.utils.logging_utils import setup_logger

logger = setup_logger(__name__)

def edit_gen_gp_gfx_missiledescriptors(source: Any, game_db: Dict[str, Any]) -> None:
    """GameData/Generated/Gameplay/Gfx/MissileDescriptors.ndf"""
    logger.info("Adjusting missile speed and acceleration")

    ammo_db = game_db["ammunition"]
    missile_inst_renames_new_old = ammo_db.get("renames_new_old", {})
    missile_inst_renames_old_new = ammo_db.get("renames_old_new", {})

    for missile_decr in source:
        # Strip Descriptor_Missile_ prefix for comparison
        stripped_namespace = missile_decr.namespace.replace("Descriptor_Missile_", "")

        # Check for renames first
        if stripped_namespace in missile_inst_renames_new_old:
            stripped_namespace = missile_inst_renames_new_old[stripped_namespace]
        elif stripped_namespace in missile_inst_renames_old_new:
            stripped_namespace = missile_inst_renames_old_new[stripped_namespace]
        
        # Strip _salvolengthN suffix if present (new format)
        salvo_length_match = re.search(r"_salvolength(\d+)$", stripped_namespace)
        if salvo_length_match:
            stripped_namespace = stripped_namespace.replace(salvo_length_match.group(0), "")
        
        # Extract _xN suffix if present (old format)
        x_suffix_match = re.search(r"_x(\d+)$", stripped_namespace)
        x_suffix_value = None
        if x_suffix_match:
            x_suffix_value = int(x_suffix_match.group(1))
            # Don't strip yet - we'll check if it matches a valid salvo length

        # Try to match to a missile definition
        matched_missile = None
        matched_data = None
        
        for (missile, category, donor, is_new), data in missiles.items():
            if data is None or "MissileDescriptor" not in data:
                continue
            
            # If we have an _xN suffix, check if it's a valid salvo length for this missile
            if x_suffix_value is not None:
                # Check if this missile has SalvoLengths defined
                salvo_lengths = None
                if "WeaponDescriptor" in data and "SalvoLengths" in data["WeaponDescriptor"]:
                    salvo_lengths = data["WeaponDescriptor"]["SalvoLengths"]
                
                # If salvo lengths are defined, verify the _xN value matches one of them
                if salvo_lengths is not None:
                    if x_suffix_value not in salvo_lengths:
                        # This _xN suffix doesn't match any salvo length for this missile
                        continue
                    # It matches, so strip the _xN suffix for comparison
                    base_name = stripped_namespace.replace(x_suffix_match.group(0), "")
                else:
                    # No SalvoLengths defined, strip _xN anyway (fallback behavior)
                    base_name = stripped_namespace.replace(x_suffix_match.group(0), "")
            else:
                # No _xN suffix, use as-is
                base_name = stripped_namespace
            
            # Match the base name to the missile name
            if missile == base_name:
                matched_missile = missile
                matched_data = data
                break
        
        # If no match found, skip this descriptor
        if matched_missile is None or matched_data is None:
            continue

        # Apply speed/acceleration changes to the matched descriptor
        modules_list = missile_decr.v.by_m("ModulesDescriptors")
        for module in modules_list.v:
            if not isinstance(module.v, ndf.model.Object):
                continue

            if module.v.type != "TGuidedMissileMovementModuleDescriptor":
                continue

            default_cfg = module.v.by_m("DefaultConfig")
            uncontrollable_cfg = module.v.by_m("UncontrollableConfig")
            if "MaxSpeedGRU" in matched_data["MissileDescriptor"]:
                max_speed = matched_data["MissileDescriptor"]["MaxSpeedGRU"]
                default_cfg.v.by_m("MaxSpeedGRU").v = str(max_speed)  # noqa
                logger.debug(f"Changed {missile_decr.namespace} max speed to {max_speed}")

                uncontrollable_cfg.v.by_m("MaxSpeedGRU").v = str(max_speed)  # noqa
                logger.debug(f"Changed {missile_decr.namespace} uncontrollable speed to {max_speed}")

            if "MaxAccelerationGRU" in matched_data["MissileDescriptor"]:
                max_accel = matched_data["MissileDescriptor"]["MaxAccelerationGRU"]
                default_cfg.v.by_m("MaxAccelerationGRU").v = str(max_accel)  # noqa
                logger.debug(f"Changed {missile_decr.namespace} max acceleration to {max_accel}")
                
                uncontrollable_cfg.v.by_m("MaxAccelerationGRU").v = str(max_accel)  # noqa
                logger.debug(f"Changed {missile_decr.namespace} uncontrollable acceleration to {max_accel}")

            if "AutoGyr" in matched_data["MissileDescriptor"]:
                auto_gyr = matched_data["MissileDescriptor"]["AutoGyr"]
                default_cfg.v.by_m("AutoGyr").v = str(auto_gyr)  # noqa
                logger.debug(f"Changed {missile_decr.namespace} auto gyr to {auto_gyr} (90 degrees)")
            break