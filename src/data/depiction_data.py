"""Functions for gathering weapon depiction data."""

from pathlib import Path
from typing import Any, Dict

from src import ndf
from src.data.ammo_data import get_vanilla_renames
from src.utils.logging_utils import setup_logger
from src.utils.ndf_utils import is_obj_type, strip_quotes

logger = setup_logger(__name__)

def gather_depiction_data(mod_src_path: Path) -> Dict[str, Any]:
    """Gather depiction data from source files."""
    logger.info("Gathering depiction data")
    
    depiction_data = {
        "modele": {},        # Maps weapon names to model paths
        "fire_effect": {},   # Maps weapon names to fire effects
        "conditionaltag": {} # Maps weapon names to animation tags
    }
    
    try:
        # Just parsing input, no output needed
        mod = ndf.Mod(mod_src_path, "None")
        
        # Get weapon renames mapping
        ammo_ndf_path = "GameData/Generated/Gameplay/Gfx/Ammunition.ndf"
        missiles_ndf_path = "GameData/Generated/Gameplay/Gfx/AmmunitionMissiles.ndf"
        
        # Get renames from both ammunition files
        weapon_renames = {
            **get_vanilla_renames(mod, ammo_ndf_path),
            **get_vanilla_renames(mod, missiles_ndf_path)
        }
        logger.debug(f"Loaded {len(weapon_renames)} weapon renames")
        
        # Process infantry depictions
        infantry_ndf_path = "GameData/Generated/Gameplay/Gfx/Infanterie/GeneratedDepictionInfantry.ndf"
        logger.debug(f"Reading infantry depictions from: {infantry_ndf_path}")
        infantry_parse_source = mod.parse_src(infantry_ndf_path)
        
        # Process each weapon's depiction data
        for entry in infantry_parse_source:
            if not hasattr(entry, 'namespace') or not entry.namespace:
                continue
                
            # Look for weapon alternatives (mesh data)
            if entry.namespace.startswith("AllWeaponAlternatives_"):
                for alt in entry.v:
                    if not is_obj_type(alt.v, "TDepictionDescriptor"):
                        continue
                    try:
                        mesh = alt.v.by_m("MeshDescriptor").v
                        if mesh and mesh.startswith("$/GFX/DepictionResources/Modele_"):
                            weapon_name = mesh.split("Modele_")[-1]
                            data = {"mesh": mesh}
                            if weapon_name in weapon_renames:
                                data["rename"] = weapon_renames[weapon_name]
                            depiction_data["modele"][weapon_name] = data
                            logger.debug(f"Found model for weapon: {weapon_name}")
                    except Exception as e:
                        logger.debug(f"Error processing mesh: {str(e)}")
                        
            # Look for weapon subdepictions (fire effects)
            elif entry.namespace.startswith("AllWeaponSubDepiction_"):
                operators = entry.v.by_m("Operators", None)
                if operators and operators.v:  # Check if operators exists and has values
                    for op in operators.v:
                        if not is_obj_type(op.v, "DepictionOperator_WeaponInstantFireInfantry"):
                            continue
                        try:
                            fire_tag_list = op.v.by_m("FireEffectTag").v
                            if not fire_tag_list:  # Check if list is empty
                                continue
                            fire_tag = strip_quotes(fire_tag_list[0].v if hasattr(fire_tag_list[0], 'v') else fire_tag_list[0])
                            weapon_name = fire_tag.split("FireEffect_")[-1]
                            
                            shoot_data = strip_quotes(op.v.by_m("WeaponShootDataPropertyName").v)
                            turret_index = int(shoot_data.split("_")[-1]) - 1
                            
                            if weapon_name not in depiction_data["fire_effect"]:
                                depiction_data["fire_effect"][weapon_name] = {
                                    "effects": {}
                                }
                            
                            depiction_data["fire_effect"][weapon_name]["effects"][turret_index] = fire_tag
                            
                            if weapon_name in weapon_renames:
                                depiction_data["fire_effect"][weapon_name]["rename"] = weapon_renames[weapon_name]
                            logger.debug(f"Found fire effect for weapon: {weapon_name}")
                        except Exception as e:
                            logger.debug(f"Error processing fire effect: {str(e)}")
                            
            # Look for soldier depictions (animation tags)
            elif entry.namespace.startswith("TacticDepiction_") and entry.namespace.endswith("_Soldier"):
                operators = entry.v.by_m("Operators", None)
                if operators and operators.v:  # Check if operators exists and has values
                    for op in operators.v:
                        if not is_obj_type(op.v, "DepictionOperator_SkeletalAnimation2_Default"):
                            continue
                        try:
                            tags = op.v.by_m("ConditionalTags", None)
                            if not tags or not tags.v:  # Check if tags exist and have values
                                logger.debug("No conditional tags found")
                                continue
                                
                            for tag in tags.v:
                                tag_name = strip_quotes(tag.v[0].v if hasattr(tag.v[0], 'v') else tag.v[0])
                                mesh_alt = strip_quotes(tag.v[1].v if hasattr(tag.v[1], 'v') else tag.v[1])
                                depiction_data["conditionaltag"][tag_name] = mesh_alt
                                logger.debug(f"Found animation tag: {tag_name} -> {mesh_alt}")
                        except Exception as e:
                            logger.debug(f"Error processing animation tag: {str(e)}")
        
        logger.info(f"Gathered {len(depiction_data['modele'])} weapon models")
        logger.info(f"Gathered {len(depiction_data['fire_effect'])} fire effects")
        logger.info(f"Gathered {len(depiction_data['conditionaltag'])} animation tags")
        
        return depiction_data
        
    except Exception as e:
        logger.error(f"Error gathering depiction data: {str(e)}")
        return depiction_data 