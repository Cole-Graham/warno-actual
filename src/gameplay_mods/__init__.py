"""Gameplay modification modules."""


from typing import Any, Callable, Dict, List

# New import structure
from .gameplay import (
    edit_constantes_gdconstants,
    edit_constantes_ravitaillement,
    edit_constantes_weaponconstantes,
    edit_unit_team,
    edit_unit_airplane_critical,
    edit_unit_groundunit_critical,
    edit_unit_helico_critical,
    edit_unit_infanterie_critical,
    edit_unit_template_critical,
    edit_unit_testunits_critical,
)
from .generated import (
    edit_decks,
    edit_decks_deckserializer,
    edit_decks_divisioncostmatrix,
    edit_decks_divisionrules,
    edit_decks_divisions,
    edit_decks_deckpacks,
    edit_gfx_ammunition,
    edit_gfx_ammunitionmissiles,
    edit_gfx_capacitelist,
    edit_gfx_conditionsdescriptor,
    edit_gfx_damagelevels,
    edit_gfx_effetssurunite,
    edit_gfx_orderavailabilitytactic,
    edit_gfx_smokedescriptor,
    edit_gfx_unitedescriptor,
    edit_gfx_weapondescriptor,
    edit_userinterface_divisiontextures,
)

__all__ = [
    # .gameplay
    'edit_constantes_gdconstants',
    'edit_constantes_ravitaillement',
    'edit_constantes_weaponconstantes',
    'edit_unit_team',
    'edit_unit_airplane_critical',
    'edit_unit_groundunit_critical',
    'edit_unit_helico_critical',
    'edit_unit_infanterie_critical',
    'edit_unit_template_critical',
    'edit_unit_testunits_critical',
    # .generated
    'edit_decks',
    'edit_decks_deckserializer',
    'edit_decks_divisioncostmatrix',
    'edit_decks_divisionrules',
    'edit_decks_divisions',
    'edit_decks_deckpacks',
    'edit_gfx_ammunition',
    'edit_gfx_ammunitionmissiles',
    'edit_gfx_capacitelist',
    'edit_gfx_conditionsdescriptor',
    'edit_gfx_damagelevels',
    'edit_gfx_effetssurunite',
    'edit_gfx_orderavailabilitytactic',
    'edit_gfx_smokedescriptor',
    'edit_gfx_unitedescriptor',
    'edit_gfx_weapondescriptor',
    'edit_userinterface_divisiontextures',
]