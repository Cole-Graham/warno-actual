"""Functions for modifying unit deployment."""

from src.utils.logging_utils import setup_logger

# logger = setup_logger(__name__)


def edit_forward_deploy(source_path) -> None:
    """Edit forward deployment ranges in UniteDescriptor.ndf."""
    # logger.info("Modifying forward deployment ranges")
    
    for unit_descr in source_path:
        is_cmd = False
        modules_list = unit_descr.v.by_m("ModulesDescriptors").v
        
        for i, module in enumerate(modules_list, start=0):
            if not hasattr(module.v, 'type'):
                continue
                
            module_type = module.v.type
            if module_type == "TZoneInfluenceMapModuleDescriptor":
                is_cmd = True
                
            if module_type != "TDeploymentShiftModuleDescriptor":
                continue
            
            if is_cmd:
                modules_list.remove(i)
                # logger.info(f"Removed deployment shift from {unit_descr.namespace}")
                break
            
            shift = module.v.by_m("DeploymentShiftGRU").v
            if shift == "2473.49823322":
                module.v.by_m("DeploymentShiftGRU").v = "750.0"
                # logger.info(f"Set {unit_descr.namespace} deployment to 750m")
                break
            
            elif shift == "3533.56890459":
                module.v.by_m("DeploymentShiftGRU").v = "1750.0"
                # logger.info(f"Set {unit_descr.namespace} deployment to 1750m")
            
            else:
                # logger.warning(f"Unknown deployment shift for {unit_descr.namespace}: {shift}")
                pass
