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

    _edit_veterancy_hints(source_path)
    _create_new_packs(source_path)

def _edit_veterancy_hints(source_path) -> None:
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
            
def _create_new_packs(source_path) -> None:
    """GameData/Generated/Gameplay/Gfx/ExperienceLevels.ndf"""
    logger.info("--------- creating new packs ---------")
    
    # create multiplicative simple_v3
    simplev3multi = source_path.by_n("ExperienceLevelsPackDescriptor_XP_pack_simple_v3").copy()
    simplev3multi.namespace = "ExperienceLevelsPackDescriptor_XP_pack_simple_v3_multiplicative"
    simplev3multi.v.by_m("DescriptorId").v = "GUID:{24897653-f7d5-47e2-983d-709d8c592547}"
    xp_levels_list = simplev3multi.v.by_m("ExperienceLevelsDescriptors")
    xp_levels_list.v[0].v.by_m("DescriptorId").v = f"GUID:{{769754fe-2e9d-4376-8eef-dc331d64e865}}"
    xp_levels_list.v[1].v.by_m("DescriptorId").v = f"GUID:{{de635e99-d3a6-4be6-967b-4422228a4421}}"
    xp_levels_list.v[2].v.by_m("DescriptorId").v = f"GUID:{{61ca26a4-a8b4-4186-8e9a-b72974d9ee12}}"
    xp_levels_list.v[3].v.by_m("DescriptorId").v = f"GUID:{{d7e83635-de97-4f90-a371-da4090c6064d}}"
    xp_levels_list.v[0].v.by_m("HintBodyToken").v = \
        "'" + VETERANCY_BONUSES["simple_v3_multiplicative"]["simple_v3_multiplicative_0"]["body_token"] + "'"
    xp_levels_list.v[1].v.by_m("HintBodyToken").v = \
        "'" + VETERANCY_BONUSES["simple_v3_multiplicative"]["simple_v3_multiplicative_1"]["body_token"] + "'"
    xp_levels_list.v[2].v.by_m("HintBodyToken").v = \
        "'" + VETERANCY_BONUSES["simple_v3_multiplicative"]["simple_v3_multiplicative_2"]["body_token"] + "'"
    xp_levels_list.v[3].v.by_m("HintBodyToken").v = \
        "'" + VETERANCY_BONUSES["simple_v3_multiplicative"]["simple_v3_multiplicative_3"]["body_token"] + "'"
    xp_levels_list.v[0].v.by_m("LevelEffectsPacks").v = "[$/GFX/EffectCapacity/UnitEffect_xp_rookie_multiplicative]"
    xp_levels_list.v[1].v.by_m("LevelEffectsPacks").v = "[$/GFX/EffectCapacity/UnitEffect_xp_trained_multiplicative]"
    xp_levels_list.v[2].v.by_m("LevelEffectsPacks").v = "[$/GFX/EffectCapacity/UnitEffect_xp_veteran_multiplicative]"
    xp_levels_list.v[3].v.by_m("LevelEffectsPacks").v = "[$/GFX/EffectCapacity/UnitEffect_xp_elite_multiplicative]"
    source_path.add(simplev3multi)
    
    # create multiplicative SF_v2
    sf2multi = source_path.by_n("ExperienceLevelsPackDescriptor_XP_pack_SF_v2").copy()
    sf2multi.namespace = "ExperienceLevelsPackDescriptor_XP_pack_SF_v2_multiplicative"
    sf2multi.v.by_m("DescriptorId").v = "GUID:{c730812a-7bde-4232-b02b-8e736ca1d046}"
    xp_levels_list = sf2multi.v.by_m("ExperienceLevelsDescriptors")
    xp_levels_list.v[0].v.by_m("DescriptorId").v = f"GUID:{{d076af3a-816d-4384-8ca2-1919afa4889f}}"
    xp_levels_list.v[1].v.by_m("DescriptorId").v = f"GUID:{{80ceee1c-ee03-4b30-9cc4-9027ab0f2b92}}"
    xp_levels_list.v[2].v.by_m("DescriptorId").v = f"GUID:{{5f535594-7f23-4b0d-9193-85f2b643533a}}"
    xp_levels_list.v[3].v.by_m("DescriptorId").v = f"GUID:{{d58d3286-9a02-4b04-b3e6-5236b2b473df}}"
    xp_levels_list.v[0].v.by_m("HintBodyToken").v = \
        "'" + VETERANCY_BONUSES["SF_v2_multiplicative"]["SF_v2_multiplicative_0"]["body_token"] + "'"
    xp_levels_list.v[1].v.by_m("HintBodyToken").v = \
        "'" + VETERANCY_BONUSES["SF_v2_multiplicative"]["SF_v2_multiplicative_1"]["body_token"] + "'"
    xp_levels_list.v[2].v.by_m("HintBodyToken").v = \
        "'" + VETERANCY_BONUSES["SF_v2_multiplicative"]["SF_v2_multiplicative_2"]["body_token"] + "'"
    xp_levels_list.v[3].v.by_m("HintBodyToken").v = \
        "'" + VETERANCY_BONUSES["SF_v2_multiplicative"]["SF_v2_multiplicative_3"]["body_token"] + "'"
    xp_levels_list.v[1].v.by_m("LevelEffectsPacks").v.remove(1)
    xp_levels_list.v[1].v.by_m("LevelEffectsPacks").v.add("$/GFX/EffectCapacity/UnitEffect_xp_trained_multiplicative")
    xp_levels_list.v[2].v.by_m("LevelEffectsPacks").v.remove(1)
    xp_levels_list.v[2].v.by_m("LevelEffectsPacks").v.add("$/GFX/EffectCapacity/UnitEffect_xp_veteran_multiplicative")
    xp_levels_list.v[3].v.by_m("LevelEffectsPacks").v.remove(1)
    xp_levels_list.v[3].v.by_m("LevelEffectsPacks").v.add("$/GFX/EffectCapacity/UnitEffect_xp_elite_multiplicative")
    source_path.add(sf2multi)