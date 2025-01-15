"""Functions for gathering weapon depiction data."""

from pathlib import Path
from typing import Any, Dict

from src import ndf
from src.utils.logging_utils import setup_logger

logger = setup_logger('depiction_data')

def gather_depiction_data(source_path: Path) -> Dict[str, Any]:
    """Gather weapon mesh and effect mappings."""
    logger.info("Gathering depiction data")
    
    file_path = "GameData/Generated/Gameplay/Gfx/Infanterie/GeneratedDepictionInfantry.ndf"
    logger.debug(f"Reading depiction data from: {source_path / file_path}")
    
    try:
        mod = ndf.Mod(source_path, source_path)
        source = mod.parse_src(file_path)
        
        depiction_data = {
            'weapon_meshes': _gather_mesh_data(source),
            'fire_effects': _gather_effect_data(source),
            'conditional_tags': _gather_tag_data(source)
        }
        
        logger.info(f"Gathered depiction data for {len(depiction_data['weapon_meshes'])} weapons")
        return depiction_data
        
    except Exception as e:
        logger.error(f"Failed to gather depiction data: {str(e)}")
        return {
            'weapon_meshes': {},
            'fire_effects': {},
            'conditional_tags': {}
        }

def _gather_mesh_data(source: Any) -> Dict[str, Dict[str, Any]]:
    """Gather weapon mesh mappings from depiction file."""
    mesh_data = {}
    
    try:
        for unit in source:
            unit_name = unit.n
            
            try:
                modules = unit.v.by_m("ModulesDescriptors").v
                for module in modules:
                    if not hasattr(module.v, 'type'):
                        continue
                        
                    if module.v.type == "TModuleSelector_WeaponManagerModuleDescriptor":
                        weapons = module.v.by_m("WeaponManagerModuleDescriptor").v
                        for weapon in weapons:
                            if not hasattr(weapon.v, 'type'):
                                continue
                                
                            if weapon.v.type == "TWeaponManagerModuleDescriptor":
                                mesh_list = weapon.v.by_m("ArmeIds").v
                                for mesh in mesh_list:
                                    mesh_name = mesh.v.replace("'", "")
                                    if mesh_name not in mesh_data:
                                        mesh_data[mesh_name] = {
                                            'mesh': mesh_name,
                                            'units': []
                                        }
                                    mesh_data[mesh_name]['units'].append(unit_name)
                                    
            except Exception as e:
                logger.debug(f"Error processing {unit_name}: {str(e)}")
                continue
                
        logger.debug(f"Found {len(mesh_data)} weapon mesh mappings")
        
    except Exception as e:
        logger.error(f"Error gathering mesh data: {str(e)}")
        
    return mesh_data

def _gather_effect_data(source: Any) -> Dict[str, Dict[str, Any]]:
    """Gather weapon fire effect mappings from depiction file."""
    effect_data = {}
    
    try:
        for unit in source:
            unit_name = unit.n
            
            try:
                modules = unit.v.by_m("ModulesDescriptors").v
                for module in modules:
                    if not hasattr(module.v, 'type'):
                        continue
                        
                    if module.v.type == "TModuleSelector_WeaponManagerModuleDescriptor":
                        weapons = module.v.by_m("WeaponManagerModuleDescriptor").v
                        for weapon in weapons:
                            if not hasattr(weapon.v, 'type'):
                                continue
                                
                            if weapon.v.type == "TWeaponManagerModuleDescriptor":
                                effect_list = weapon.v.by_m("FireEffectId").v
                                for effect in effect_list:
                                    effect_name = effect.v.replace("'", "")
                                    if effect_name not in effect_data:
                                        effect_data[effect_name] = {
                                            'effect': effect_name,
                                            'units': []
                                        }
                                    effect_data[effect_name]['units'].append(unit_name)
                                    
            except Exception as e:
                logger.debug(f"Error processing {unit_name}: {str(e)}")
                continue
                
        logger.debug(f"Found {len(effect_data)} weapon effect mappings")
        
    except Exception as e:
        logger.error(f"Error gathering effect data: {str(e)}")
        
    return effect_data

def _gather_tag_data(source: Any) -> Dict[str, Dict[str, Any]]:
    """Gather conditional animation tags from depiction file."""
    tag_data = {}
    
    try:
        for unit in source:
            unit_name = unit.n
            
            try:
                modules = unit.v.by_m("ModulesDescriptors").v
                for module in modules:
                    if not hasattr(module.v, 'type'):
                        continue
                        
                    if module.v.type == "TModuleSelector_WeaponManagerModuleDescriptor":
                        weapons = module.v.by_m("WeaponManagerModuleDescriptor").v
                        for weapon in weapons:
                            if not hasattr(weapon.v, 'type'):
                                continue
                                
                            if weapon.v.type == "TWeaponManagerModuleDescriptor":
                                tags = weapon.v.by_m("ConditionalTags").v
                                for tag_pair in tags.v:
                                    if not hasattr(tag_pair, 'v'):
                                        continue
                                        
                                    pair_str = str(tag_pair.v)
                                    if not pair_str.startswith('(') or not pair_str.endswith(')'):
                                        continue
                                        
                                    try:
                                        tag, mesh = pair_str[1:-1].split(',')
                                        tag = tag.strip().strip("'")
                                        weapon_name = tag.replace("ConditionalTag_", "")
                                        
                                        if weapon_name not in tag_data:
                                            tag_data[weapon_name] = {
                                                'tag': tag,
                                                'units': []
                                            }
                                        tag_data[weapon_name]['units'].append(unit_name)
                                    except ValueError:
                                        continue
                                    
            except Exception as e:
                logger.debug(f"Error processing {unit_name}: {str(e)}")
                continue
                
        logger.debug(f"Found {len(tag_data)} conditional tag mappings")
        
    except Exception as e:
        logger.error(f"Error gathering tag data: {str(e)}")
        
    return tag_data 