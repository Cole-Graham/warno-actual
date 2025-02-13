"""Functions for gathering weapon depiction data."""
import json
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
    """Gather depiction data from GeneratedDepictionInfantry.ndf."""
    logger.info("Gathering depiction data from GeneratedDepictionInfantry.ndf")
    
    # Initialize the depiction_data dictionary
    depiction_data = {}

    # Template for each unit's depiction data
    template_data_entry = {
        "weapon_alternatives": {
            "alts": {},
            "reference": {}  # Changed to dict to store by selector_id
        },
        "weapon_subdepictions": {},
        "tactic_alternatives": {},
        "tactic_soldier": {
            "selector_tactic": "",
            "animation_tags": {}
        },
    }
    
    # Store complete list of fire effects
    all_fire_effects = {}
    # Store weapon to mesh mappings 
    all_weapon_meshes = {}
    # Store all weapon type to mesh alternative mappings
    all_animation_tags = {}
    # Store mapping of weapons to their animation tags
    animation_weapon_map = {}

    try:
        mod = ndf.Mod(str(mod_src_path), "None")
        logger.debug(f"Created NDF mod for path: {mod_src_path}")
        
        ammo_ndf_path = "GameData/Generated/Gameplay/Gfx/Ammunition.ndf"
        missiles_ndf_path = "GameData/Generated/Gameplay/Gfx/AmmunitionMissiles.ndf"
        all_renames = _build_all_renames(mod, ammo_ndf_path, missiles_ndf_path)
        
        infantry_ndf_path = "GameData/Generated/Gameplay/Gfx/Infanterie/GeneratedDepictionInfantry.ndf"
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
                # Check if we've reached InfantrySelectorTactic_00_01
                if entry.namespace == "InfantrySelectorTactic_00_01":
                    break

                # Get unit name from Gfx_ entries
                if entry.namespace.startswith("Gfx_"):
                    current_unit = entry.namespace.replace("Gfx_", "")
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
                            if is_obj_type(alt.v, "TDepictionDescriptor"):
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
                            fire_tag = strip_quotes(op.v.by_m("FireEffectTag").v[0].v)
                            weapon_shoot_data = strip_quotes(op.v.by_m("WeaponShootDataPropertyName").v)
                            weapon_name = fire_tag.replace("FireEffect_", "")
                            if weapon_name in all_renames:
                                depiction_data[current_unit]["weapon_subdepictions"][weapon_name] = {
                                    "fire_tag": fire_tag,
                                    "rename": all_renames[weapon_name],
                                    "weapon_shoot_data": weapon_shoot_data
                                }
                            else:
                                depiction_data[current_unit]["weapon_subdepictions"][weapon_name] = {
                                    "fire_tag": fire_tag,
                                    "weapon_shoot_data": weapon_shoot_data
                                }
                            all_fire_effects[weapon_name] = fire_tag
                            logger.debug(f"Added weapon subdepiction: {weapon_name} -> {fire_tag}")
                            
                            # Map weapon to mesh based on weapon_shoot_data index
                            mesh_index = int(weapon_shoot_data.split("_")[-1])
                            mesh_key = f"MeshAlternative_{mesh_index}"
                            if mesh_key in depiction_data[current_unit]["weapon_alternatives"]["alts"]:
                                mesh = depiction_data[current_unit]["weapon_alternatives"]["alts"][mesh_key]  # noqa
                                all_weapon_meshes[weapon_name] = mesh.split("Modele_")[-1]
                                logger.debug(f"Mapped weapon '{weapon_name}' to mesh '{all_weapon_meshes[weapon_name]}'")
                            
                    except Exception as e:
                        logger.error(f"Error processing weapon subdepiction for {current_unit}: {str(e)}")

                # Process tactic alternatives
                elif entry.namespace == f"TacticDepiction_{current_unit}_Alternatives":
                    logger.debug(f"Processing tactic alternatives for {current_unit}")
                    try:
                        for alt in entry.v:
                            if is_obj_type(alt.v, "TDepictionDescriptor"):
                                selector_id_lod = alt.v.by_m("SelectorId").v[0].v
                                if selector_id_lod == "LOD_High":
                                    selector_id_number = strip_quotes(alt.v.by_m("SelectorId").v[1].v)
                                    selector_id = [selector_id_lod, selector_id_number]
                                else:
                                    selector_id = [selector_id_lod]
                                mesh = alt.v.by_m("MeshDescriptor").v.split("Modele_")[-1]
                                depiction_data[current_unit]["tactic_alternatives"] = {  # noqa
                                    "selector_id": selector_id,
                                    "mesh": mesh
                                }
                                logger.debug(f"Added tactic alternative: {selector_id} -> {mesh}")
                    except Exception as e:
                        logger.error(f"Error processing tactic alternative for {current_unit}: {str(e)}")
                
                # Process tactic soldier
                elif entry.namespace == f"TacticDepiction_{current_unit}_Soldier":
                    logger.debug(f"Processing SelectorTactic and animation tags for {current_unit}")
                    try:
                        selector_tactic = entry.v.by_m("Selector").v.split("InfantrySelectorTactic_")[-1]  # noqa
                        depiction_data[current_unit]["tactic_soldier"]["selector_tactic"] = selector_tactic  # noqa
                        operators = entry.v.by_m("Operators").v  # noqa
                        for op in operators:
                            if op.v.type != "DepictionOperator_SkeletalAnimation2_Default":
                                logger.debug(f"Skipping non-animation operator: {op.namespace}")
                                continue
                            if op.v.by_m("ConditionalTags", False) is not None:
                                conditional_tags = op.v.by_m("ConditionalTags").v
                                for tag_tuple in conditional_tags:
                                    if isinstance(tag_tuple.v, tuple):
                                        weapon_type = strip_quotes(tag_tuple.v[0])
                                        mesh_alt = strip_quotes(tag_tuple.v[1])
                                        depiction_data[current_unit]["tactic_soldier"]["animation_tags"][weapon_type] = mesh_alt
                                        # Add to global animation tags dictionary
                                        if weapon_type not in all_animation_tags:
                                            all_animation_tags[weapon_type] = set()
                                        all_animation_tags[weapon_type].add(mesh_alt)
                                        
                                        # Map weapons to animation tags based on mesh alternative number
                                        mesh_alt_num = mesh_alt.split("_")[-1]
                                        for weapon_name, weapon_data in depiction_data[current_unit]["weapon_subdepictions"].items():  # noqa
                                            weapon_mesh_num = weapon_data["weapon_shoot_data"].split("_")[-1]
                                            if weapon_mesh_num == mesh_alt_num:
                                                animation_weapon_map[weapon_name] = weapon_type
                                                logger.debug(f"Mapped weapon '{weapon_name}' to animation type '{weapon_type}'")
                                        
                                        logger.debug(f"Added animation tag: {weapon_type} -> {mesh_alt}")
                                    else:
                                        logger.warning(f"Unexpected format for conditional tag: {tag_tuple}")
                            else:
                                logger.debug(f"No conditional tags found for operator: {op.namespace}")
                    except Exception as e:
                        logger.error(f"Error processing animation tag for {current_unit}: {str(e)}")

            except Exception as e:
                logger.error(f"Error processing entry: {str(e)}")
                continue

        # Convert sets to sorted lists for consistent JSON serialization
        all_animation_tags = {k: sorted(list(v)) for k, v in all_animation_tags.items()}

        # Add complete lists to output
        depiction_data["all_fire_effects"] = all_fire_effects
        depiction_data["all_weapon_meshes"] = all_weapon_meshes
        depiction_data["all_animation_tags"] = all_animation_tags
        depiction_data["animation_weapon_map"] = animation_weapon_map

        logger.info(f"Gathered depiction data for {len(depiction_data)-4} units")  # -4 for all_fire_effects, all_weapon_meshes, all_animation_tags, animation_weapon_map
        logger.info(f"Gathered {len(all_fire_effects)} total fire effects")
        logger.info(f"Gathered {len(all_animation_tags)} unique weapon types")
        logger.debug(f"Final depiction data: {json.dumps(depiction_data, indent=4)}")
        
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
