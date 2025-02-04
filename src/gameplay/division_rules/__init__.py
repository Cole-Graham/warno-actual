"""Editors for GameData/Generated/Gameplay/DivisionRules.ndf"""

from typing import Any, Callable, Dict, List

from .mg_teams import mg_team_division_rules
from .unit_edits import unit_edits_divisionrules, supply_divisionrules


__all__ = [
    'mg_team_division_rules',
    'unit_edits_divisionrules',
    'supply_divisionrules',
]