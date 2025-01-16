"""Infantry depiction and showroom editing."""

from typing import Any, Dict

from src.constants.unit_edits import load_unit_edits
from src.gameplay.depictions.infantry import edit_infantry_depictions
from src.gameplay.depictions.showroom import edit_showroom_units


def edit_depictions(source_files: Dict[str, Any], game_db: Dict[str, Any]) -> None:
    """Edit infantry depictions and showroom units.
    
    Args:
        source_files: Dictionary containing parsed NDF files:
            - 'infantry': GeneratedDepictionInfantry.ndf
            - 'showroom': ShowRoomUnits.ndf
        game_db: Game database containing unit and depiction data
    """
    # Load unit edits from constants
    unit_edits = load_unit_edits()
    
    # Edit infantry depictions
    edit_infantry_depictions(source_files['infantry'], unit_edits, game_db['depiction_data'])
    
    # Edit showroom units
    edit_showroom_units(source_files['showroom'], unit_edits) 