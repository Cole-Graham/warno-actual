from pathlib import Path
from typing import Dict, List


def get_source_paths(config: Dict) -> List[Path]:
    """Get ordered list of source paths based on configuration.
    
    Returns:
        List of paths in priority order:
        - For UI mods: [base_game]
        - For gameplay with UI base: [ui_mod, base_game]
        - For gameplay without UI: [base_game]
    """
    warno_mods = Path(config['directories']['warno_mods'])
    base_game = config['directories']['base_game']
    base_path = warno_mods / base_game
    
    if config['build_config']['target'] == 'ui_only':
        # UI-only mod always uses base game as source
        return [base_path]
    
    # For gameplay mod, check if we should use UI as base
    if config['build_config']['use_ui_as_base']:
        # Use appropriate UI mod version as primary source
        ui_source = config['directories']['ui_dev'] if config['build_config']['write_dev'] else config['directories']['ui_release']
        ui_path = warno_mods / ui_source
        return [ui_path, base_path]  # UI mod first, base game as fallback
    
    # Default to using base game as source
    return [base_path]

def get_destination_path(config_data: Dict) -> Path:
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
    
    if build_config['target'] == 'ui_only':
        return files['ui_only']
    
    # For gameplay mod, include both gameplay files and variant files
    to_process = files['gameplay_only'].copy()
    to_process.extend(files['variants'])  # variants are now just strings
    
    # If not using UI as base, also include UI files
    if not build_config['use_ui_as_base']:
        to_process.extend(files['ui_only'])
    
    return to_process 