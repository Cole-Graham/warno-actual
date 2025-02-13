"""Editors for GameData/Generated/Gameplay/DivisionRules.ndf"""

from typing import Any, Callable, Dict, List

from .deck_packs import modify_deck_packs, update_deck_pack_references, new_deck_packs
from .decks import modify_decks
from .mg_teams import mg_team_division_rules
from .unit_edits import unit_edits_divisionrules, supply_divisionrules


__all__ = [
    'modify_deck_packs',
    'update_deck_pack_references',
    'new_deck_packs',
    'modify_decks',
    'mg_team_division_rules',
    'unit_edits_divisionrules',
    'supply_divisionrules',
]
