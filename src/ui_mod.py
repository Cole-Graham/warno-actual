from typing import Callable, Dict


def get_file_editor(file_path: str, config: Dict) -> Callable:
    """Get the appropriate edit function based on file path and build target"""
    
    # Example of a file that needs different handling for UI vs gameplay
    if file_path == "GameData/Generated/Gameplay/GFX/OrderAvailability_Tactic.ndf":
        if config['build_config']['target'] == 'ui_only':
            return edit_orderavailability_ui
        else:
            return edit_orderavailability_gameplay
            
    # Return None if no special handling needed
    return None

def edit_orderavailability_ui(source):
    """Edit OrderAvailability_Tactic.ndf for UI-only mod"""
    # UI-specific edits here
    pass

def edit_orderavailability_gameplay(source):
    """Edit OrderAvailability_Tactic.ndf for gameplay mod"""
    # Gameplay-specific edits here
    pass 