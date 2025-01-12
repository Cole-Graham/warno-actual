"""Editors for GameData/Generated/Gameplay/DivisionRules.ndf"""

from typing import Any, Callable, Dict, List

from .mg_teams import edit_mg_teams
from .unit_edits import edit_units


def get_editors(unit_db: Dict[str, Any]) -> List[Callable]:
    """Get all editors for DivisionRules.ndf."""
    return [
        lambda source: edit_mg_teams(source, unit_db),
        lambda source: edit_units(source),
    ] 