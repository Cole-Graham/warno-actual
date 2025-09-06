"""Functions for gathering weapon depiction data."""

# import re
from copy import deepcopy
from pathlib import Path
from typing import Any, Dict

from src import ndf
from src.constants.weapons.vanilla_inst_modifications import MERGED_RENAMES
from src.data.ammo_data import get_vanilla_renames
from src.utils.logging_utils import setup_logger
from src.utils.ndf_utils import is_obj_type, strip_quotes

logger = setup_logger(__name__)


def gather_depiction_data(mod_src_path: Path) -> Dict[str, Any]:
    """Gather depiction data from DepictionInfantry.ndf."""
    logger.info("Gathering depiction data from DepictionInfantry.ndf")

    # Initialize the depiction_data dictionary
    depiction_data = {}

    # Template for each unit's depiction data
    template_data_entry = {
        "weapon_alternatives": {"alts": {}, "reference": {}},  # Changed to dict to store by selector_id
        "weapon_subdepictions": {},
        "tactic_alternatives": {},
        "tactic_soldier": {"selector_tactic": "", "animation_tags": {}},
    }

    # Store complete list of fire effects
    all_fire_effects = {}

    try:
        mod = ndf.Mod(str(mod_src_path), "None")
        logger.debug(f"Created NDF mod for path: {mod_src_path}")

        ammo_ndf_path = "GameData/Generated/Gameplay/Gfx/Ammunition.ndf"
        missiles_ndf_path = "GameData/Generated/Gameplay/Gfx/AmmunitionMissiles.ndf"
        all_renames = _build_all_renames(mod, ammo_ndf_path, missiles_ndf_path)

        infantry_ndf_path = "GameData/Generated/Gameplay/Gfx/Infanterie/DepictionInfantry.ndf"
        logger.debug(f"Attempting to parse: {infantry_ndf_path}")

        try:
            infantry_parse_source = mod.parse_src(infantry_ndf_path)
            logger.debug("Successfully parsed infantry NDF file")
        except Exception as e:
            logger.error(f"Failed to parse infantry NDF file: {str(e)}")
            return depiction_data

        current_unit = None
        logger.debug("Starting to process entries...")

        for entry in infantry_parse_source:
            try:
                if not hasattr(entry, "namespace"):
                    continue

                # Get unit name from TacticDepiction_ entries
                if entry.namespace.startswith("TacticDepiction_"):
                    current_unit = entry.namespace.replace("TacticDepiction_", "")
                    logger.debug(f"Found new unit: {current_unit}")
                    depiction_data[current_unit] = deepcopy(template_data_entry)
                    continue

                if not current_unit:
                    continue

                # Process weapon alternatives
                if entry.namespace == f"AllWeaponAlternatives_{current_unit}":
                    logger.debug(f"Processing weapon alternatives for {current_unit}")
                    try:
                        for alt in entry.v:
                            if is_obj_type(alt.v, "TDepictionVisual"):
                                selector_id = strip_quotes(alt.v.by_m("SelectorId").v[0].v)
                                mesh = alt.v.by_m("MeshDescriptor").v
                                depiction_data[current_unit]["weapon_alternatives"]["alts"][selector_id] = mesh
                                logger.debug(f"Added weapon alternative: {selector_id} -> {mesh}")
                            elif is_obj_type(alt.v, "TMeshlessDepictionDescriptor"):
                                selector_id = strip_quotes(alt.v.by_m("SelectorId").v[0].v)
                                mesh = alt.v.by_m("ReferenceMeshForSkeleton").v
                                depiction_data[current_unit]["weapon_alternatives"]["reference"][selector_id] = mesh
                                logger.debug(f"Added reference mesh: {selector_id} -> {mesh}")
                    except Exception as e:
                        logger.error(f"Error processing weapon alternative for {current_unit}: {str(e)}")

                # Process weapon subdepictions
                elif entry.namespace == f"AllWeaponSubDepiction_{current_unit}":
                    logger.debug(f"Processing weapon subdepictions for {current_unit}")
                    try:
                        operators = entry.v.by_m("Operators").v  # noqa
                        for op in operators:
                            if not is_obj_type(op.v, "DepictionOperator_WeaponInstantFireInfantry"):
                                continue
                            fire_tag = strip_quotes(op.v.by_m("FireEffectTag").v)
                            weapon_shoot_data = strip_quotes(op.v.by_m("WeaponShootDataPropertyName").v)
                            weapon_name = fire_tag.replace("FireEffect_", "")
                            if weapon_name in all_renames:
                                depiction_data[current_unit]["weapon_subdepictions"][weapon_name] = {
                                    "fire_tag": fire_tag,
                                    "rename": all_renames[weapon_name],
                                    "weapon_shoot_data": weapon_shoot_data,
                                }
                            else:
                                depiction_data[current_unit]["weapon_subdepictions"][weapon_name] = {
                                    "fire_tag": fire_tag,
                                    "weapon_shoot_data": weapon_shoot_data,
                                }
                            all_fire_effects[weapon_name] = fire_tag
                            logger.debug(f"Added weapon subdepiction: {weapon_name} -> {fire_tag}")
                    except Exception as e:
                        logger.error(f"Error processing weapon subdepiction for {current_unit}: {str(e)}")

                # Process tactic alternatives
                elif entry.namespace == f"TacticDepiction_{current_unit}_Alternatives":
                    logger.debug(f"Processing tactic alternatives for {current_unit}")
                    try:
                        for alt in entry.v:
                            if is_obj_type(alt.v, "TDepictionVisual"):
                                selector_id_lod = alt.v.by_m("SelectorId").v[0].v
                                if selector_id_lod == "LOD_High":
                                    selector_id_number = strip_quotes(alt.v.by_m("SelectorId").v[1].v)
                                    selector_id = [selector_id_lod, selector_id_number]
                                else:
                                    selector_id = [selector_id_lod]
                                mesh = alt.v.by_m("MeshDescriptor").v.split("Modele_")[-1]
                                depiction_data[current_unit]["tactic_alternatives"] = {
                                    "selector_id": selector_id,
                                    "mesh": mesh,
                                }
                                logger.debug(f"Added tactic alternative: {selector_id} -> {mesh}")
                    except Exception as e:
                        logger.error(f"Error processing tactic alternative for {current_unit}: {str(e)}")

                # Process tactic soldier
                elif entry.namespace == f"TacticDepiction_{current_unit}_Soldier":
                    logger.debug(f"Processing SelectorTactic and animation tags for {current_unit}")
                    try:
                        selector_tactic = entry.v.by_m("Selector").v.split("InfantrySelectorTactic_")[-1]  # noqa
                        depiction_data[current_unit]["tactic_soldier"]["selector_tactic"] = selector_tactic
                        operators = entry.v.by_m("Operators").v  # noqa
                        for op in operators:
                            if op.namespace != "DepictionOperator_SkeletalAnimation2_Default":
                                continue
                            conditional_tags = op.v.by_m("ConditionalTags").v
                            for tag_tuple in conditional_tags:
                                # Each tag_tuple is ('weapon_type', 'mesh_alternative')
                                weapon_type = strip_quotes(tag_tuple.v[0].v)
                                mesh_alt = strip_quotes(tag_tuple.v[1].v)
                                depiction_data[current_unit]["tactic_soldier"]["animation_tags"][weapon_type] = mesh_alt
                                logger.debug(f"Added animation tag: {weapon_type} -> {mesh_alt}")
                    except Exception as e:
                        logger.error(f"Error processing animation tag for {current_unit}: {str(e)}")

            except Exception as e:
                logger.error(f"Error processing entry: {str(e)}")
                continue

        # Add complete fire effects list to output
        depiction_data["all_fire_effects"] = all_fire_effects

        logger.info(f"Gathered depiction data for {len(depiction_data)-1} units")  # -1 for all_fire_effects
        logger.info(f"Gathered {len(all_fire_effects)} total fire effects")
        logger.debug(f"Final depiction data: {depiction_data}")
        return depiction_data

    except Exception as e:
        logger.error(f"Error gathering depiction data: {str(e)}")
        return depiction_data


def _build_all_renames(mod, ammo_ndf_path, missiles_ndf_path):
    try:
        all_merged_renames = {}
        all_merged_renames.update(MERGED_RENAMES)
        all_merged_renames.update(get_vanilla_renames(mod, ammo_ndf_path))
        all_merged_renames.update(get_vanilla_renames(mod, missiles_ndf_path))
        return all_merged_renames
    except Exception as e:
        logger.error(f"(depiction_data.py) Error building all renames: {str(e)}")
        return {}
