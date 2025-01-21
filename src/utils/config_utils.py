from pathlib import Path
from typing import Any, Dict, List

from src.utils.logging_utils import setup_logger

logger = setup_logger(__name__)

def get_mod_src_path(config: Dict) -> Path:
    """Get mod source directory path based on config."""
    warno_mods = Path(config['directories']['warno_mods'])
    build_config = config['build_config']
    
    # If building gameplay mod and using UI as base
    if (build_config['target'] == 'gameplay' and 
        build_config.get('use_ui_as_base', False)):
        # Use UI mod as source
        mod_name = (config['directories']['ui_dev'] 
                   if build_config['write_dev'] 
                   else config['directories']['ui_release'])
    else:
        # Use base game as source
        mod_name = config['directories']['base_game']
        
    return warno_mods / mod_name

def get_mod_dst_path(config_data: Dict) -> Path:
    """Determine the correct destination path based on build configuration"""
    build_config = config_data['build_config']
    dirs = config_data['directories']
    warno_mods = Path(dirs['warno_mods'])
    
    if build_config['target'] == 'gameplay':
        dest = dirs['gameplay_dev'] if build_config['write_dev'] else dirs['gameplay_release']
    else:  # ui_only
        dest = dirs['ui_only_dev'] if build_config['write_dev'] else dirs['ui_only_release']
        
    return warno_mods / dest

def get_files_to_process(config_data):
    """Get list of files to process based on build target"""
    build_config = config_data['build_config']
    files = config_data['files']
    
    logger.info(f"Getting files to process for target: {build_config['target']}")
    to_process = []
    
    # Add shared files first
    shared_files = files.get('shared', {}).keys()
    logger.debug(f"Adding shared files: {list(shared_files)}")
    to_process.extend(shared_files)
    
    if build_config['target'] == 'ui_only':
        logger.debug(f"Adding UI-only files: {files['ui_only']}")
        to_process.extend(files['ui_only'])
        return to_process
    
    # For gameplay mod, include both gameplay files and variant files
    logger.debug(f"Adding gameplay files: {files['gameplay_only']}")
    to_process.extend(files['gameplay_only'])
    
    # Handle variants
    variant_files = list(files['variants'].keys())
    logger.debug(f"Adding variant files: {variant_files}")
    to_process.extend(variant_files)
    
    # If not using UI as base, include UI files AFTER gameplay files
    if not build_config['use_ui_as_base']:
        logger.debug(f"Adding UI files: {files['ui_only']}")
        to_process.extend(files['ui_only'])
    
    logger.info(f"Total files to process: {len(to_process)}")
    return to_process 