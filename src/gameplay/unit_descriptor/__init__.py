"""Unit descriptor modification modules."""

from .cover import edit_auto_cover
from .deployment import edit_forward_deploy
from .infantry import edit_infantry_armor_wa
from .mg_teams import edit_mg_teams
from .optics import edit_antirad_optics
from .team import edit_team_supply
from .unit_edits import edit_units

__all__ = [
    'edit_auto_cover',
    'edit_forward_deploy',
    'edit_infantry_armor_wa',
    'edit_mg_teams',
    'edit_antirad_optics',
    'edit_team_supply',
    'edit_units',
] 