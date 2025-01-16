"""UI modification module."""

from typing import Callable, Dict, List

from .buildings import edit_fob_minimap


def get_editors() -> Dict[str, List[Callable]]:
    """Get UI file editors."""
    return {
        "GameData/Generated/Gameplay/Gfx/BuildingDescriptors.ndf": [
            lambda source: edit_fob_minimap(source),
        ]
    } 