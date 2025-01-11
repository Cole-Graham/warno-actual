from src import ModConfig, ndf
from src.gameplay_mod import get_file_editor as get_gameplay_editor
from src.ui_mod import get_file_editor as get_ui_editor
from src.utils.config_utils import (
    get_destination_path,
    get_files_to_process,
    get_source_paths,
)
from src.utils.logging_utils import setup_logger

logger = setup_logger('main')

def main():
    config = ModConfig.get_instance()
    build_config = config.config_data['build_config']
    
    # Get paths - but only use the first source path for ndf.Mod
    source_paths = get_source_paths(config.config_data)
    source_path = source_paths[0]  # Use primary source path
    dest_path = get_destination_path(config.config_data)
    
    logger.info("Starting mod build")
    logger.info(f"Build target: {build_config['target']}")
    logger.info(f"Development build: {build_config['write_dev']}")
    logger.info(f"Using UI as base: {build_config.get('use_ui_as_base', False)}")
    logger.info(f"Source path: {source_path}")
    
    # Initialize mod with single source path
    try:
        mod = ndf.Mod(source_path, dest_path)
        
        # Get list of files to process
        files_to_process = get_files_to_process(config.config_data)
        logger.info(f"Found {len(files_to_process)} files to process")
        
        # Process each file
        for file_path in files_to_process:
            logger.info(f"Processing {file_path}")
            with mod.edit(file_path) as source:
                # Get appropriate editor based on build target
                editor = (get_gameplay_editor(file_path, config.config_data) 
                         if build_config['target'] == 'gameplay'
                         else get_ui_editor(file_path, config.config_data))
                if editor:
                    editor(source)
                    
        logger.info("Build completed successfully")
        
    except Exception as e:
        logger.error(f"Build failed: {str(e)}")
        raise


if __name__ == "__main__":
    main()
