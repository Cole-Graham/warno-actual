"""Functions for modifying unit effects."""

import ast
from typing import List, Tuple

from src.dics.effects.capacities import (
    CHOC_MOVE_CAPACITY,
    CHOC_MOVE_GSR_CAPACITY,
    NO_CHOC_MOVE_CAPACITY,
)
from src.utils.logging_utils import setup_logger

logger = setup_logger(__name__)

# Effect definitions
NO_CHOC_MOVE = (
    'export UnitEffect_Ajoute_Tag_no_Choc_move is TEffectsPackDescriptor'
    '('
    '    DescriptorId       = GUID:{bf1daa2b-1708-4702-80ff-4c7dfd76c2d7}'
    "    NameForDebug       = 'Ajoute_Tag_no_Choc_move'"
    '    EffectsDescriptors = ['
    '        TUnitEffectRaiseTagDescriptor'
    '        ('
    '            TagListToRaise = ["RadioJammed"]'
    '        )'
    '    ]'
    ')'
)

CHOC_MOVE = (
    'export UnitEffect_Choc_move is TEffectsPackDescriptor'
    '('
    '    DescriptorId       = GUID:{c3dbf0eb-c573-47b6-ba19-2d17ad3f9f24}'
    "    NameForDebug       = 'Choc_move'"
    '    EffectsDescriptors = ['
    '        TUnitEffectIncreaseDamageTakenDescriptor'
    '        ('
    '            ModifierType        = ~/ModifierType_Pourcentage'
    '            BonusDamage         = -50'
    '            DamageType          = EDamageType/Suppress'
    '        ),'
    '        TUnitEffectIncreaseDamageTakenDescriptor'
    '        ('
    '            ModifierType = ~/ModifierType_Pourcentage'
    '            BonusDamage = -20'
    '            DamageType  = EDamageType/Physical'
    '        ),'
    '        TUnitEffectIncreaseSpeedDescriptor'
    '        ('
    '            ModifierType = ~/ModifierType_Multiplicatif'
    '            BonusSpeedBaseInPercent   = 1.33'
    '        ),'
    '        TUnitEffectShowLabelIconDescriptor'
    '        ('
    '            TextureToken = "icone_shock_move"'
    '        )'
    '    ]'
    ')'
)

CHOC_MOVE_GSR = (
    'export UnitEffect_Choc_move_GSR is TEffectsPackDescriptor'
    '('
    '    DescriptorId       = GUID:{177c48af-2b7d-4d09-bae7-4d2d2628f946}'
    "    NameForDebug       = 'Choc_move_GSR'"
    '    EffectsDescriptors = ['
    '        TUnitEffectIncreaseSpeedDescriptor'
    '        ('
    '            ModifierType = ~/ModifierType_Multiplicatif'
    '            BonusSpeedBaseInPercent   = 1.33'
    '        ),'
    '        TUnitEffectShowLabelIconDescriptor'
    '        ('
    '            TextureToken = "icone_shock_move"'
    '        )'
    '    ]'
    ')'
)


def edit_shock_effects(source) -> None:
    """Edit shock effects in EffetsSurUnite.ndf."""
    logger.info("Modifying Shock Trait effects")
    
    # Add new shock effects
    for i, row in enumerate(source, start=1):
        if row.namespace == "UnitEffect_Choc":
            source.insert(i, CHOC_MOVE)
            source.insert(i, CHOC_MOVE_GSR)
            source.insert(i, NO_CHOC_MOVE)
            logger.info("Added shock movement effects")
            break
    
    # Modify sniper effects
    sniper_obj = source.by_n("UnitEffect_sniper").v
    effects_list = sniper_obj.by_m("EffectsDescriptors").v
    
    for effect in effects_list:
        if not hasattr(effect.v, 'type'):
            continue
            
        if effect.v.type == "TUnitEffectIncreaseWeaponPhysicalDamagesDescriptor":
            effects_list.remove(effect.index)
            logger.info(f"Removed sniper damage bonus from {sniper_obj.parent_row.namespace}") 


def edit_shock_effects_packs_list(source) -> None:
    """Edit shock effects in EffectsPacksList.ndf."""
    logger.info("Modifying Shock Trait effects in packs list")
    
    choc_move = "~/UnitEffect_Choc_move"
    choc_move_GSR = "~/UnitEffect_Choc_move_GSR"
    choc_tag_no_move = "~/UnitEffect_Ajoute_Tag_no_Choc_move"
    
    effectspacks_list = source.by_n("EffectsPacksList").v.by_m("EffectsPacks").v
    
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


def edit_capacite_list(source) -> None:
    """Edit capacities in CapaciteList.ndf."""
    logger.info("Modifying Shock Trait effects in capacite list")
    
    # Edit shock range
    for capacite_descr in source:
        if capacite_descr.n == "Capacite_Choc":
            capacite_descr.v.by_m("RangeGRU").v = "100"
            logger.info("Updated Capacite_Choc range to 100")
            break
    
    # Add new capacities
    for i, row in enumerate(source, start=1):
        if row.namespace == "Capacite_Choc":
            source.insert(i, CHOC_MOVE_CAPACITY)
            source.insert(i, CHOC_MOVE_GSR_CAPACITY)
            source.insert(i, NO_CHOC_MOVE_CAPACITY)
            logger.info("Added shock movement capacities")
            break 


def _get_unit_tags(tags) -> List[str]:
    """Extract tags from either string or List format."""
    if isinstance(tags, str):
        return [tag.strip("'\"") for tag in ast.literal_eval(tags)]
    return [tag.v.strip("'\"") for tag in tags]


def _check_unit_properties(modules_list) -> Tuple[bool, bool, bool]:
    """Check if unit is GSR, infantry, and/or infantry AT."""
    is_gsr = False
    infantry = False
    infantry_at = False
    
    for descr_row in modules_list:
        if not hasattr(descr_row.v, 'type'):
            continue
            
        descr_type = descr_row.v.type
        
        # Check for GSR specialty
        if descr_type == "TUnitUIModuleDescriptor":
            specialties_list = descr_row.v.by_m("SpecialtiesList").v
            if isinstance(specialties_list, str):
                tags = _get_unit_tags(specialties_list)
                is_gsr = '_gsr' in tags
            else:
                is_gsr = any(tag.v == "'_gsr'" for tag in specialties_list)
                
        # Check infantry tags
        elif descr_type == "TTagsModuleDescriptor":
            tags = descr_row.v.by_m("TagSet").v
            tags = _get_unit_tags(tags)
            infantry = 'Infanterie' in tags
            infantry_at = 'Infanterie_AT' in tags
            
            if not infantry or infantry_at:
                break
                
    return is_gsr, infantry, infantry_at


def edit_shock_units(source) -> None:
    """Add shock movement capabilities to shock units."""
    logger.info("Adding shock movement capabilities to units")
    
    for unit_row in source:
        modules_list = unit_row.v.by_m("ModulesDescriptors").v
        
        # Check unit properties
        is_gsr, infantry, infantry_at = _check_unit_properties(modules_list)
        
        if not infantry or infantry_at:
            continue
            
        # Add shock movement capabilities
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
            for skill in skill_list:
                if skill.v != "$/GFX/EffectCapacity/Capacite_Choc":
                    continue
                    
                if not is_gsr:
                    skill_list.add("$/GFX/EffectCapacity/Capacite_Choc_move")
                    skill_list.add("$/GFX/EffectCapacity/Capacite_no_Choc_move")
                    logger.info(f"Added shock movement capacities to {unit_row.namespace}")
                else:
                    skill_list.add("$/GFX/EffectCapacity/Capacite_Choc_move_GSR")
                    logger.info(f"Added GSR shock movement capacity to {unit_row.namespace}")
                break 