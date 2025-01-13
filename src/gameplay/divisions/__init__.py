"""Editors for GameData/Generated/Gameplay/Divisions.ndf"""

from typing import Any, Callable, Dict, List

from .matrices import edit_division_matrices
from .unit_edits import edit_units


def get_editors(game_db: Dict[str, Any]) -> Dict[str, List[Callable]]:
    """Get editors for division files."""
    return {
        "GameData/Generated/Gameplay/Divisions.ndf": [
            lambda source: edit_units(source),
        ],
        "GameData/Generated/Gameplay/DivisionCostMatrix.ndf": [
            lambda source: edit_division_matrices(source),
        ],
    } 