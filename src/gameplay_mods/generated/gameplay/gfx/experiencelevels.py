"""Functions for modifying ExperienceLevels.ndf"""

from typing import Any
from src.dics.veterancy.vet_bonuses import VETERANCY_BONUSES
from src import ndf
from src.utils.logging_utils import setup_logger

logger = setup_logger(__name__)


def edit_gen_gp_gfx_experiencelevels(source_path) -> None:
    """GameData/Generated/Gameplay/Gfx/ExperienceLevels.ndf"""
    logger.info("--------- editing ExperienceLevels.ndf ---------")
    logger.info("          Modifying plane veterancy hints       ")

    # Define experience pack mappings
    xp_packs = {
        "ExperienceLevelsPackDescriptor_XP_pack_simple_v3": {
            "pack_type": "simple_v3",
            "level_format": "simple_v3_{level}",
        },
        "ExperienceLevelsPackDescriptor_XP_pack_SF_v2": {
            "pack_type": "SF_v2",
            "level_format": "SF_v2_{level}",
        },
        "ExperienceLevelsPackDescriptor_XP_pack_artillery": {
            "pack_type": "artillery",
            "level_format": "artillery_{level}",
        },
        "ExperienceLevelsPackDescriptor_XP_pack_helico": {
            "pack_type": "helico",
            "level_format": "helico_{level}",
        },
        "ExperienceLevelsPackDescriptor_XP_pack_avion": {
            "pack_type": "avion",
            "level_format": "avion_{level}",
        },
    }

    for row in source_path:
        if row.namespace not in xp_packs:
            continue

        pack_info = xp_packs[row.namespace]
        pack_type = pack_info["pack_type"]

        try:
            xp_descr_list = row.v.by_m("ExperienceLevelsDescriptors").v

            for level, xp_descr in enumerate(xp_descr_list):
                if not isinstance(xp_descr.v, ndf.model.Object):
                    continue

                # Use index as level number (0-based)
                level_key = pack_info["level_format"].format(level=level)

                if level_key not in VETERANCY_BONUSES[pack_type]:
                    logger.warning(f"Missing veterancy data for {level_key} in {pack_type}")
                    continue

                body_token = VETERANCY_BONUSES[pack_type][level_key]["body_token"]
                xp_descr.v.by_m("HintBodyToken").v = f"'{body_token}'"
                logger.info(f"Modified dictionary token for level {level} of {row.namespace}")

        except Exception as e:
            logger.error(f"Failed to process {row.namespace}: {str(e)}")