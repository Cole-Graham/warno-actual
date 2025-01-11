import os


def get_source_paths(config_data):
    """Get the appropriate source path based on build configuration."""
    build_config = config_data['build_config']
    dirs = config_data['directories']
    warno_mods = dirs['warno_mods']
    
    if build_config['target'] == 'ui_only':
        # UI-only mod always uses base game as source
        return [os.path.join(warno_mods, dirs['base_game'])]
    
    # For gameplay mod, check if we should use UI as base
    if build_config['use_ui_as_base']:
        # Use appropriate UI mod version as source
        ui_source = dirs['ui_dev'] if build_config['write_dev'] else dirs['ui_release']
        return [os.path.join(warno_mods, ui_source)]
    
    # Default to using base game as source
    return [os.path.join(warno_mods, dirs['base_game'])]

def get_destination_path(config_data):
    """Determine the correct destination path based on build configuration"""
    build_config = config_data['build_config']
    dirs = config_data['directories']
    warno_mods = dirs['warno_mods']
    
    if build_config['target'] == 'gameplay':
        dest = dirs['gameplay_dev'] if build_config['write_dev'] else dirs['gameplay_release']
    else:  # ui_only
        dest = dirs['ui_only_dev'] if build_config['write_dev'] else dirs['ui_only_release']
        
    return os.path.join(warno_mods, dest)

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