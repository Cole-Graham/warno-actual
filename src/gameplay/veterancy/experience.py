"""Functions for modifying experience levels."""

from src.dics.experience.level_data import EXPERIENCE_LEVELS
from src.utils.logging_utils import setup_logger

logger = setup_logger(__name__)


def _update_level_hint(xp_descr, level_type: str, level_name: str) -> None:
    """Update hint token for a specific experience level."""
    if level_name not in EXPERIENCE_LEVELS[level_type]:
        return
        
    body_token = EXPERIENCE_LEVELS[level_type][level_name]["body_token"]
    xp_descr.v.by_m("HintBodyToken").v = f"'{body_token}'"
    logger.info(f"Updated hint token for {level_name}")


def edit_experience_hints(source) -> None:
    """Edit experience level hints in ExperienceLevels.ndf."""
    logger.info("Modifying experience level hints")
    
    level_packs = {
        "ExperienceLevelsPackDescriptor_XP_pack_simple_v3": "simple_v3",
        "ExperienceLevelsPackDescriptor_XP_pack_SF_v2": "SF_v2",
        "ExperienceLevelsPackDescriptor_XP_pack_artillery": "artillery",
        "ExperienceLevelsPackDescriptor_XP_pack_helico": "helico",
        "ExperienceLevelsPackDescriptor_XP_pack_avion": "avion",
    }
    
    for row in source:
        if row.namespace not in level_packs:
            continue
            
        level_type = level_packs[row.namespace]
        xp_descr_list = row.v.by_m("ExperienceLevelsDescriptors").v
        
        for xp_descr in xp_descr_list:
            if not hasattr(xp_descr.v, 'type'):
                continue
                
            descr_namespace = xp_descr.namespace
            level_suffix = descr_namespace.split("_")[-2:]
            level_name = "_".join(level_suffix)
            
            _update_level_hint(xp_descr, level_type, level_name) 