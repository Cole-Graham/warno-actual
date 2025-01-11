from typing import Callable, Dict

from src.unit_edits import process_unitdescriptor


def get_file_editor(file_path: str, config: Dict) -> Callable:
    """Get the appropriate edit function for gameplay files"""
    
    # Map gameplay files to their editor functions
    editors = {
        "GameData/Generated/Gameplay/Gfx/UniteDescriptor.ndf": process_unitdescriptor,
        # Add more gameplay file editors here
    }
    
    return editors.get(file_path) 