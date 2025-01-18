"""UI modification module."""

from typing import Callable, Dict, List

from .buildings import add_fob_minimap_module, edit_minimapicons


def get_ui_editors() -> Dict[str, List[Callable]]:
    """Get UI file editors."""
    return {
        "GameData/Generated/Gameplay/Gfx/BuildingDescriptors.ndf": [
            lambda source: add_fob_minimap_module(source),
        ],
        
        # UI files
        "GameData/Generated/UserInterface/Textures/MinimapIcons.ndf": [
            lambda source: edit_minimapicons(source),
        ]
    }   