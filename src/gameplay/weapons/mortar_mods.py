"""Functions for modifying mortar weapons."""

from src.utils.logging_utils import setup_logger
from src.utils.ndf_utils import ndf

logger = setup_logger(__name__)


def add_corrected_shot_dispersion(source, ammo_db: dict) -> None:
    """Add corrected shot dispersion multipliers to mortar ammunition.
    
    Args:
        source: Ammunition.ndf file
        ammo_db: Ammunition database containing mortar categories
    """
    logger.info("Adding corrected shot dispersion to mortars")
    mortar_cats = ammo_db["mortar_categories"]
    
    for ammo_descr in source:
        name = ammo_descr.n
        
        # Check if weapon is a mortar
        if name in mortar_cats["mortars"]:
            dispersion = 0.7
        elif name in mortar_cats["smoke_mortars"]:
            dispersion = 0.9
        else:
            continue
            
        # Add dispersion multiplier
        for i, member in enumerate(ammo_descr.v):
            if member.m == "DispersionWithoutSorting":
                ammo_descr.v.insert(i + 1, f"CorrectedShotDispersionMultiplier = {dispersion}")
                logger.info(f"Added {dispersion} dispersion multiplier for {name}")
                break


def add_radio_tag_to_mortars(source, game_db: dict) -> None:
    """Add 'Radio' tag to mortar units to enable corrected shot."""
    logger.info("Adding 'Radio' tag to mortar units")
    mortar_units = game_db["ammunition"]["unit_categories"]["mortar_units"]
    
    for unit in source:
        if unit.n not in mortar_units:
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
            
        # Check if Radio tag already exists
        tag_set = tags_module.v.by_m("TagSet").v
        if '"Radio"' in [tag.v for tag in tag_set]:
            logger.info(f"{unit.n} already has 'Radio' tag")
            continue
            
        # Add Radio tag after GroundUnits
        for i, tag in enumerate(tag_set):
            if tag.v == '"GroundUnits"':
                tag_set.insert(i + 1, '"Radio",')
                logger.info(f"Added 'Radio' tag to {unit.n}")
                break 


def edit_smoke_duration(source) -> None:
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

    for descr_row in source:
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