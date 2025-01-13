"""Editors for depiction-related files."""

from typing import Any, Callable, Dict, List

from .infantry import edit_infantry_depictions
from .showroom import edit_showroom_units


def get_editors(unit_db: Dict[str, Any]) -> Dict[str, List[Callable]]:
    """Get editors for depiction files."""
    return {
        "GameData/Generated/Gameplay/GFX/ShowRoomUnits.ndf": [
            lambda source: edit_showroom_units(source, unit_db),
        ],
        "GameData/Generated/Gameplay/Gfx/Infanterie/GeneratedDepictionInfantry.ndf": [
            lambda source: edit_infantry_depictions(source, unit_db),
        ]
    } 