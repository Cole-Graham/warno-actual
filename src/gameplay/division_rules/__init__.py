"""Editors for GameData/Generated/Gameplay/DivisionRules.ndf"""

from typing import Any, Callable, Dict, List

from .mg_teams import edit_mg_teams
from .unit_edits import unit_edits_divisionrules, supply_divisionrules

__all__ = [
    'edit_mg_teams',
    'unit_edits_divisionrules',
    'supply_divisionrules',
]