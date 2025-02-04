"""Functions for modifying mortar weapons."""

from typing import Any, Dict

from src.utils.logging_utils import setup_logger
from src.utils.ndf_utils import ndf

logger = setup_logger(__name__)


def add_corrected_shot_dispersion(source_path: Any, game_db: Dict[str, Any]) -> None:
    """Add corrected shot dispersion to mortar weapons."""
    ammo_db = game_db["ammunition"]
    
    logger.info("Adding corrected shot dispersion to mortars")
    mortar_categories = ammo_db["mortar_weapons"]
    
    for weapon_descr in source_path:
        name = weapon_descr.n.replace("Ammo_", "")
        
        # Check if weapon is a mortar
        if name in mortar_categories["mortars"]:
            dispersion = 0.7
        elif name in mortar_categories["smoke_mortars"]:
            dispersion = 0.9
        else:
            continue
            
        # Add dispersion multiplier
        has_multiplier = False
        for i, member in enumerate(weapon_descr.v):
            if member.m == "DispersionWithoutSorting":
                insert_index = i + 1

            elif member.m == "CorrectedShotDispersionMultiplier":
                existing_multiplier = member.v
                has_multiplier = True
        
        if has_multiplier:
            logger.info(f"Corrected shot dispersion multiplier already exists for {name}, "
                        f"with value {existing_multiplier}")
        else:
            weapon_descr.v.insert(insert_index, f"CorrectedShotDispersionMultiplier = {dispersion}")
            logger.info(f"Added {dispersion} dispersion multiplier for {name}")



def add_radio_tag_to_mortars(source_path, game_db: dict) -> None:
    """Add 'Radio' tag to mortar units to enable corrected shot."""
    logger.info("Adding 'Radio' tag to mortar units")
    
    for unit in source_path:
        # Check if unit exists in database and has mortar texture
        unit_name = unit.namespace.replace("Descriptor_Unit_", "")
        if (unit_name not in game_db["unit_data"] or 
            game_db["unit_data"][unit_name].get("menu_icon") != "Texture_RTS_H_mortar"):
            continue
        
        if "Radio" in game_db["unit_data"][unit_name].get("tags", []):
            logger.info(f"{unit_name} already has 'Radio' tag")
            continue

        modules = unit.v.by_m("ModulesDescriptors").v
        tags_module = None
        
        # Find tags module
        for module in modules:
            if hasattr(module.v, 'type') and module.v.type == "TTagsModuleDescriptor":
                tags_module = module
                break
        
        if not tags_module:
            continue
            
        # Add Radio tag after GroundUnits
        tag_set = tags_module.v.by_m("TagSet").v
        for i, tag in enumerate(tag_set):
            if tag.v == '"GroundUnits"':
                tag_set.insert(i + 1, '"Radio",')
                logger.info(f"Added 'Radio' tag to {unit_name}")
                break 


def edit_smoke_duration(source_path) -> None:
    """Edit smoke duration for mortars in SmokeDescriptor.ndf."""
    logger.info("------------- editing SmokeDescriptor.ndf -------------")
    logger.info("           Editing smoke duration for mortars          ")
    
    smokes = [  # (name, duration)
        ("Fumi105mm", 80),
        ("Fumi107mm", 80),
        ("Fumi120mm", 80),
        ("Fumi120mm_mortier", 80),
        ("Fumi122mm", 80),
        ("Fumi152mm", 80),
        ("Fumi155mm", 80),
        ("Fumi203mm", 80),
        ("Fumi60mm", 80),
        ("Fumi81mm", 80),
    ]

    for descr_row in source_path:
        for smoke_name, duration in smokes:
            if descr_row.namespace == f"Descriptor_Smoke_{smoke_name}":
                modules_list = descr_row.v.by_m("ModulesDescriptors").v
                for module in modules_list:
                    if not isinstance(module.v, ndf.model.Object):
                        continue
                    if module.v.type != "TSmokeModuleDescriptor":
                        continue
                    module.v.by_m("TimeToLive").v = str(duration)
                    logger.info(f"Set {smoke_name} duration to {duration} seconds")
                    break
                break 