"""Functions for modifying mortar weapon instances."""

from src.utils.logging_utils import setup_logger

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