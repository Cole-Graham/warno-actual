import json
from pathlib import Path
from typing import Any, Dict

from src import ndf
from src.data.unit_data import gather_unit_data, gather_weapon_data
from src.utils.config_utils import get_destination_path, get_source_paths
from src.utils.logging_utils import setup_logger

logger = setup_logger('database')

def build_database(config: Dict[str, Any]) -> None:
    """Build or update the database with game data."""
    logger.info("Starting database build process")
    
    try:
        if not config.get("data_config", {}).get("build_database", True):
            logger.info("Database build skipped as per configuration")
            return
            
        # Create database directory relative to this file
        db_dir = Path(__file__).parent / "database"
        logger.info(f"Using database directory: {db_dir}")
        db_dir.mkdir(parents=True, exist_ok=True)
        
        # Get full source and destination paths from config
        source_paths = get_source_paths(config)
        dest_path = get_destination_path(config)
        
        # Use base game path for gathering data
        base_game_path = source_paths[-1]  # Base game is always last in the list
        unit_data = gather_unit_data(base_game_path, dest_path)
        logger.info("Gathering weapon data...")
        weapon_data = gather_weapon_data(base_game_path)
        depiction_data = gather_depiction_data(base_game_path)
        
        # Save unit data
        unit_db_path = db_dir / "units.json"
        weapon_db_path = db_dir / "weapons.json"
        
        logger.info(f"Saving unit data ({len(unit_data)} entries)")
        with open(unit_db_path, 'w') as f:
            json.dump(unit_data, f, indent=2)
            
        logger.info(f"Saving weapon data ({len(weapon_data)} entries)")
        with open(weapon_db_path, 'w') as f:
            json.dump(weapon_data, f, indent=2)
            
        logger.debug(f"Unit data size: {unit_db_path.stat().st_size} bytes")
        logger.debug(f"Weapon data size: {weapon_db_path.stat().st_size} bytes")
        
        # Save depiction data
        depiction_db_path = db_dir / "depictions.json"
        with open(depiction_db_path, 'w') as f:
            json.dump(depiction_data, f, indent=2)
        
        logger.info("Database build completed successfully")
        
    except Exception as e:
        logger.error(f"Database build failed: {str(e)}")
        raise

def load_data(config: Dict[str, Any], data_type: str) -> Dict[str, Any]:
    """Load specific data from the database."""
    try:
        # Use same path as build_database
        db_dir = Path(__file__).parent / "database"
        data_path = db_dir / f"{data_type}.json"
        
        if not data_path.exists():
            logger.warning(f"No {data_type} data found in database")
            return {}
            
        with open(data_path) as f:
            return json.load(f)
            
    except Exception as e:
        logger.error(f"Error loading {data_type} data: {str(e)}")
        return {}
    
def gather_depiction_data(base_path: Path) -> Dict[str, Any]:
    """Gather weapon mesh and effect mappings."""
    logger.info("Gathering depiction data")
    
    file_path = "GameData/Generated/Gameplay/Gfx/Infanterie/GeneratedDepictionInfantry.ndf"
    logger.debug(f"Reading depiction data from: {base_path / file_path}")
    
    try:
        mod = ndf.Mod(base_path, base_path)
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
        for row in source:
            if not hasattr(row, 'namespace') or not hasattr(row, 'v'):
                continue
                
            if isinstance(row.namespace, str) and row.namespace.startswith('AllWeaponAlternatives_'):
                unit_name = row.namespace.replace('AllWeaponAlternatives_', '')
                
                for obj in row.v:
                    if not hasattr(obj.v, 'type') or not hasattr(obj.v, 'by_m'):
                        continue
                        
                    if obj.v.type == "TDepictionDescriptor":
                        mesh_descriptor = obj.v.by_m("MeshDescriptor")
                        if not mesh_descriptor or not hasattr(mesh_descriptor, 'v'):
                            continue
                            
                        mesh_name = mesh_descriptor.v
                        if isinstance(mesh_name, str) and mesh_name.startswith("$/GFX/DepictionResources/Modele_"):
                            weapon_name = mesh_name.split("Modele_")[1]
                            if weapon_name not in mesh_data:
                                mesh_data[weapon_name] = {
                                    'mesh': mesh_name,
                                    'units': []
                                }
                            mesh_data[weapon_name]['units'].append(unit_name)
                            
        logger.debug(f"Found {len(mesh_data)} weapon mesh mappings")
        
    except Exception as e:
        logger.error(f"Error gathering mesh data: {str(e)}")
        
    return mesh_data

def _gather_effect_data(source: Any) -> Dict[str, Dict[str, Any]]:
    """Gather weapon fire effect mappings from depiction file."""
    effect_data = {}
    
    try:
        for row in source:
            if not hasattr(row, 'namespace') or not hasattr(row, 'v'):
                continue
                
            if isinstance(row.namespace, str) and row.namespace.startswith('AllWeaponSubDepiction_'):
                unit_name = row.namespace.replace('AllWeaponSubDepiction_', '')
                operators = row.v.by_m("Operators")
                if not operators or not hasattr(operators, 'v'):
                    continue
                    
                for operator in operators.v:
                    if not hasattr(operator.v, 'type'):
                        continue
                        
                    if operator.v.type == "DepictionOperator_WeaponInstantFireInfantry":
                        fire_tags = operator.v.by_m("FireEffectTag")
                        if not fire_tags or not hasattr(fire_tags, 'v') or not fire_tags.v:
                            continue
                            
                        fire_tag = str(fire_tags.v[0])
                        weapon_name = fire_tag.replace("FireEffect_", "")
                        if weapon_name not in effect_data:
                            effect_data[weapon_name] = {
                                'effect': fire_tag,
                                'units': []
                            }
                        effect_data[weapon_name]['units'].append(unit_name)
                        
        logger.debug(f"Found {len(effect_data)} fire effect mappings")
        
    except Exception as e:
        logger.error(f"Error gathering effect data: {str(e)}")
        
    return effect_data

def _gather_tag_data(source: Any) -> Dict[str, Dict[str, Any]]:
    """Gather conditional animation tags from depiction file."""
    tag_data = {}
    
    try:
        soldier_entries = [row for row in source if hasattr(row, 'namespace') 
                         and isinstance(row.namespace, str) 
                         and row.namespace.endswith('_Soldier')]
        
        if not soldier_entries:
            logger.warning("No soldier entries found in depiction file")
            return tag_data
            
        for row in soldier_entries:
            unit_name = row.namespace.replace('TacticDepiction_', '').replace('_Soldier', '')
            logger.debug(f"Processing soldier entry for {unit_name}")
            
            try:
                operators = row.v.by_m("Operators")
                if not operators or not hasattr(operators, 'v'):
                    logger.debug(f"No valid operators found for {unit_name}")
                    continue
                
                for operator in operators.v:
                    if not hasattr(operator.v, 'type'):
                        continue
                        
                    if operator.v.type == "DepictionOperator_SkeletalAnimation2_Default":
                        try:
                            tags = operator.v.by_m("ConditionalTags")
                            logger.debug(f"Found tags for {unit_name}: {tags.v if tags else 'None'}")
                        except Exception as e:
                            logger.debug(f"Failed to get tags for {unit_name}: {str(e)}")
                            continue
                            
                        if not tags or not hasattr(tags, 'v'):
                            continue
                            
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
    

