from typing import Any
from src import ndf
from src.utils.logging_utils import setup_logger
from src.utils.ndf_utils import find_obj_by_namespace

logger = setup_logger(__name__)

def edit_gen_gp_gfx_smokedescriptor(source_path: Any):
    """GameData/Generated/Gameplay/Gfx/SmokeDescriptor.ndf"""
    
    _smoke_duration(source_path)
    

def _smoke_duration(source_path) -> None:
    """GameData/Generated/Gameplay/Gfx/SmokeDescriptor.ndf"""
    logger.info("------------- editing SmokeDescriptor.ndf -------------")
    logger.info("           Editing smoke duration for mortars          ")

    smokes = [  # (name, duration)
        ("Fumi105mm", 80),
        ("Fumi120mm", 80),
        ("Fumi120mm_mortier", 80),
        ("Fumi152mm", 80),
        ("Fumi203mm", 80),
        ("Fumi60mm", 80),
        ("Fumi81mm", 80),
    ]

    for smoke_name, duration in smokes:
        smoke_descr = find_obj_by_namespace(source_path, f"Descriptor_Smoke_{smoke_name}")
        if smoke_descr:
            modules_list = smoke_descr.v.by_m("ModulesDescriptors").v
            for module in modules_list:
                if not isinstance(module.v, ndf.model.Object):
                    continue
                if module.v.type != "TSmokeModuleDescriptor":
                    continue
                module.v.by_m("TimeToLive").v = str(duration)
                logger.info(f"Set {smoke_name} duration to {duration} seconds")
                break
        else:
            logger.warning(f"No smoke descriptor found for {smoke_name}")