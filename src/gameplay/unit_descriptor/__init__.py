"""Editors for GameData/Generated/Gameplay/Gfx/UniteDescriptor.ndf"""

from typing import Any, Callable, List

from src.gameplay.unit_descriptor.mg_teams import edit_mg_teams
from src.gameplay.unit_descriptor.unit_edits import edit_units


def get_editors(unit_db: dict) -> List[Callable[[Any], None]]:
    """Get all unit descriptor editors."""
    return [
        lambda source: edit_mg_teams(source, unit_db),
        lambda source: edit_units(source, unit_db),
    ] 