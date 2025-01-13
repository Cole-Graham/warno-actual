"""Gameplay modification modules.

Module Structure:
    depictions/     - Editors for unit depictions and showroom
    division_rules/ - Editors for division rules
    divisions/      - Editors for divisions
    effects/        - Editors for unit effects and capacities
    terrains/       - Editors for terrain properties
    ui/            - Editors for UI elements
    unit_descriptor/ - Editors for unit descriptors
    veterancy/      - Editors for veterancy and experience
    weapons/        - Editors for weapons and ammunition
"""

from .editors import get_editors

__all__ = [
    'get_editors',
] 