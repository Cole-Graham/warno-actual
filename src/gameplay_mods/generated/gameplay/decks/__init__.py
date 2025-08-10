"""Editors for GameData/Generated/Gameplay/Decks.ndf"""

from .deck_serializer import hide_divisions_deckserializer_ndf, update_deck_serializer
from .decks import (
    edit_deck_packs,
    edit_deck_pack_lists,
    hide_divisions_decks_ndf,
    new_deck_packs,
    update_deck_pack_references,
)
from .division_rules import (
    new_unit_division_rules,
    supply_divisionrules,
    unit_edits_divisionrules,
)
from .divisions import edit_divisions
from .divisioncostmatrix import edit_divisioncostmatrix
from .mg_teams import mg_team_division_rules

__all__ = [
    # .deck_serializer
    'hide_divisions_deckserializer_ndf',
    'update_deck_serializer',
    # .decks
    'edit_deck_packs',
    'edit_deck_pack_lists',
    'hide_divisions_decks_ndf',
    'new_deck_packs',
    'update_deck_pack_references',
    # .division_rules
    'new_unit_division_rules',
    'supply_divisionrules',
    'unit_edits_divisionrules',
    # .divisions
    'edit_divisions',
    # .divisioncostmatrix
    'edit_divisioncostmatrix',
    # .mg_teams
    'mg_team_division_rules',
]
