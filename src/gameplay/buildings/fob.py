"""Gameplay FOB building modifications."""

from src import ndf
from src.utils.logging_utils import setup_logger

logger = setup_logger(__name__)

def edit_fob_attributes(source_path) -> None:
    """GameData/Generated/Gameplay/Gfx/BuildingDescriptors.ndf
    Edit FOB supply, health and command point cost."""
    logger.info("Editing FOB attributes")
    
    try:
        for fob_descr in source_path:
            if not hasattr(fob_descr, 'v') or not hasattr(fob_descr.v, 'by_m'):
                logger.error("Invalid FOB descriptor structure")
                continue
                
            try:
                modules_list = fob_descr.v.by_m("ModulesDescriptors").v
            except AttributeError:
                logger.error("Failed to get modules list")
                continue
            
            for module in modules_list:
                if not isinstance(module.v, ndf.model.Object):
                    continue
                
                if module.v.type == "TSupplyModuleDescriptor":
                    module.v.by_m("SupplyDescriptor").v = "$/GFX/Weapon/FOBSupply"
                    module.v.by_m("SupplyCapacity").v = "6500"
                    logger.info("Updated FOB supply capacity to 6500")
                
                elif module.v.type == "TBaseDamageModuleDescriptor":
                    module.v.by_m("MaxPhysicalDamages").v = "20"
                    logger.info("Updated FOB health to 20")
                
                elif module.v.type == "TProductionModuleDescriptor":
                    module.v.by_m("ProductionRessourcesNeeded").v.by_k(
                        "$/GFX/Resources/Resource_CommandPoints").v = "75"
                    logger.info("Updated FOB command point cost to 75")
    except Exception as e:
        logger.error(f"Failed to edit FOB attributes: {e}") 