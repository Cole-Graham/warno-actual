"""Functions for modifying unit effects."""

import ast
from typing import List, Tuple

from src import ModConfig
from src.constants.effects.capacities import (
    CHOC_MOVE_CAPACITY,
    CHOC_MOVE_EFFECT,
    CHOC_MOVE_GSR_CAPACITY,
    CHOC_MOVE_GSR_EFFECT,
    NO_CHOC_MOVE_CAPACITY,
    NO_CHOC_MOVE_EFFECT,
)
from src.utils.logging_utils import setup_logger

logger = setup_logger(__name__)


def edit_shock_effects(source_path) -> None:
    """Edit shock effects in EffetsSurUnite.ndf."""
    logger.info("Modifying Shock Trait effects")
    
    # Add new shock effects
    for i, row in enumerate(source_path, start=1):
        if row.namespace == "UnitEffect_Choc":
            source_path.insert(i, CHOC_MOVE_EFFECT)
            source_path.insert(i, CHOC_MOVE_GSR_EFFECT)
            source_path.insert(i, NO_CHOC_MOVE_EFFECT)
            logger.info("Added shock movement effects")
            break
    
    # Modify sniper effects
    sniper_obj = source_path.by_n("UnitEffect_sniper").v
    effects_list = sniper_obj.by_m("EffectsDescriptors").v
    
    for effect in effects_list:
        if not hasattr(effect.v, 'type'):
            continue
            
        if effect.v.type == "TUnitEffectIncreaseWeaponPhysicalDamagesDescriptor":
            effects_list.remove(effect.index)
            logger.info(f"Removed sniper damage bonus from {sniper_obj.parent_row.namespace}") 


def edit_shock_effects_packs_list(source_path) -> None:
    """Edit shock effects in EffectsPacksList.ndf."""
    logger.info("Modifying Shock Trait effects in packs list")
    
    choc_move = "~/UnitEffect_Choc_move"
    choc_move_GSR = "~/UnitEffect_Choc_move_GSR"
    choc_tag_no_move = "~/UnitEffect_Ajoute_Tag_no_Choc_move"
    
    effectspacks_list = source_path.by_n("EffectsPacksList").v.by_m("EffectsPacks").v
    
    for i, row in enumerate(effectspacks_list):
        if row.v == "~/UnitEffect_Ajoute_Tag_snipe_ok":
            gsr_ok_index = i
        if row.v == "~/UnitEffect_Choc":
            effectspacks_list.insert(gsr_ok_index, choc_tag_no_move)
            logger.info("Added no_Choc_move effect to packs list")
            
            effectspacks_list.insert(i + 1, choc_move)
            effectspacks_list.insert(i + 1, choc_move_GSR)
            logger.info("Added Choc_move and Choc_move_GSR effects to packs list")
            break


def edit_capacite_list(source_path) -> None:
    """Edit capacities in CapaciteList.ndf."""
    logger.info("Modifying Shock Trait effects in capacite list")
    
    # Edit shock range
    for capacite_descr in source_path:
        if capacite_descr.n == "Capacite_Choc":
            capacite_descr.v.by_m("RangeGRU").v = "100"
            logger.info("Updated Capacite_Choc range to 100")
            break
    
    # Add new capacities
    for i, row in enumerate(source_path, start=1):
        if row.namespace == "Capacite_Choc":
            source_path.insert(i, CHOC_MOVE_CAPACITY)
            source_path.insert(i, CHOC_MOVE_GSR_CAPACITY)
            source_path.insert(i, NO_CHOC_MOVE_CAPACITY)
            logger.info("Added shock movement capacities")
            break 



def edit_shock_units(source_path, game_db) -> None:
    """Add shock movement capabilities to shock units."""
    logger.info("Adding shock movement capabilities to units")
    
    units_modified = 0
    
    for unit_name, unit_data in game_db['unit_data'].items():
        if 'skills' not in unit_data:
            continue
        
        shock_attributes = [
            'Choc' in unit_data['skills'],
            '_gsr' not in unit_data['tags'],
        ]
        
        shock_gsr_attributes = [
            'Choc' in unit_data['skills'],
            '_gsr' in unit_data['tags'],
        ]
        
        if not any(shock_attributes) and not any(shock_gsr_attributes):
            continue
        
        unit_descr = source_path.by_n(f"Descriptor_Unit_{unit_name}")
        modules_list = unit_descr.v.by_m("ModulesDescriptors").v
        for descr_row in modules_list:
            if not hasattr(descr_row.v, 'type'):
                continue
                
            if descr_row.v.type != "TModuleSelector":
                continue
            
            default_membr = descr_row.v.by_m("Default").v
            if not hasattr(default_membr, 'type'):
                continue
                
            if default_membr.type != "TCapaciteModuleDescriptor":
                continue
            
            skill_list = default_membr.by_m("DefaultSkillList").v
            
            if all(shock_attributes):
                skill_list.add("$/GFX/EffectCapacity/Capacite_Choc_move")
                skill_list.add("$/GFX/EffectCapacity/Capacite_no_Choc_move")
                logger.info(f"Added shock movement capacities to {unit_name}")
                units_modified += 1
                
            elif all(shock_gsr_attributes):
                skill_list.add("$/GFX/EffectCapacity/Capacite_Choc_move_GSR")
                logger.info(f"Added GSR shock movement capacity to {unit_name}")
                units_modified += 1
                break
            
    logger.info(f"Total units modified: {units_modified}")