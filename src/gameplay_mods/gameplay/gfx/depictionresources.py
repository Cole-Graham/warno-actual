"""Functions for modifying various depiction resources"""

import textwrap
from typing import Dict

from src.constants.new_units import NEW_DEPICTIONS
from src.utils.logging_utils import setup_logger
from src.utils.config_utils import get_mod_dst_path

logger = setup_logger(__name__)

def add_unit_meshes(config: Dict) -> None:
    """Add specific unit meshes by creating new .ndf files in the correct directory structure.
    
    Args:
        config: Configuration dictionary containing mod paths and settings
    """
    # Get the destination mod path
    mod_dst_path = get_mod_dst_path(config)
    
    for unit_descr_name, unit_data in NEW_DEPICTIONS.items():
        unit_name = unit_data["unit_name"]
        target_dir_name = unit_data.get(f"{unit_name}_ndf", {}).get("directory", None)
        meshes_ndf_code = unit_data.get(f"{unit_name}_ndf", {}).get("ndf_code", None)
        
        if target_dir_name is None or meshes_ndf_code is None:
            logger.debug(f"Skipping {unit_name}: missing directory or ndf_code")
            continue
            
        # Build the target path: GameData/Gameplay/Gfx/DepictionResources/{target_dir_name}/
        target_path = mod_dst_path / "GameData" / "Gameplay" / "Gfx" / "DepictionResources" / target_dir_name
        
        # Check if target directory exists
        if not target_path.exists():
            raise FileNotFoundError(f"Target directory does not exist: {target_path}")
            
        # Create the .ndf file path
        ndf_file_path = target_path / f"{unit_name}.ndf"
        
        # Write the .ndf file (overwrite if exists)
        try:
            # Use textwrap.dedent to remove common leading whitespace from dictionary formatting
            cleaned_code = textwrap.dedent(meshes_ndf_code)
            
            with open(ndf_file_path, 'w', encoding='utf-8') as f:
                f.write(cleaned_code)
            logger.info(f"Created/overwritten {ndf_file_path}")
        except Exception as e:
            logger.error(f"Failed to write {ndf_file_path}: {e}")
            raise