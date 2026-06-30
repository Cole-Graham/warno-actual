import re
from typing import Any, Dict
from src import ndf
from src.constants.weapons import missiles
from src.utils.logging_utils import setup_logger
from src.utils.ndf_utils import find_obj_by_type

from .handlers.missile_movement_config import apply_missile_descriptor_movement_configs

logger = setup_logger(__name__)

def edit_gen_gp_gfx_missiledescriptors(source: Any, game_db: Dict[str, Any]) -> None:
    """GameData/Generated/Gameplay/Gfx/MissileDescriptors.ndf"""
    logger.info("Adjusting missile speed and acceleration")

    ammo_db = game_db["ammunition"]
    missile_inst_renames_new_old = ammo_db.get("renames_new_old", {})
    missile_inst_renames_old_new = ammo_db.get("renames_old_new", {})

    for missile_decr in source:
        
        missile_namespace = missile_decr.namespace
        
        # remove stress on miss
        modules_list = missile_decr.v.by_m("ModulesDescriptors")
        capacite_module = find_obj_by_type(modules_list.v, "TCapaciteModuleDescriptor")
        if capacite_module:
            default_skill_list = capacite_module.v.by_m("DefaultSkillList")
            skill_list_length = len(default_skill_list.v)
            stress_on_miss_skills = [
                "$/GFX/EffectCapacity/Capacite_StressOnMiss_high",
                "$/GFX/EffectCapacity/Capacite_StressOnMiss_mid",
                "$/GFX/EffectCapacity/Capacite_StressOnMiss_low",
            ]
            stress_on_miss_skill = default_skill_list.v.find_by_cond(
                lambda x: x.v in stress_on_miss_skills, strict=False
            )
            if stress_on_miss_skill and skill_list_length == 1:
                modules_list.v.remove(capacite_module)
            elif stress_on_miss_skill:
                default_skill_list.v.remove(stress_on_miss_skill)
            elif missile_namespace.startswith(
                "Descriptor_Missile_SAM") or missile_namespace.startswith("Descriptor_Missile_MANPAD"):
                logger.warning(f"No stress on miss skill found for {missile_decr.namespace}")
        
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
        for module in modules_list.v:
            if not isinstance(module.v, ndf.model.Object):
                continue

            if module.v.type != "TGuidedMissileMovementModuleDescriptor":
                continue

            apply_missile_descriptor_movement_configs(
                module,
                matched_data["MissileDescriptor"],
                missile_decr.namespace,
                logger,
            )
            break