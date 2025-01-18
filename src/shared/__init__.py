"""Shared modifications. (identical files)"""

from typing import Callable, Dict, List

from .buildings.fob import add_fob_minimap_module, add_fob_minimap_texture


def get_shared_editors() -> Dict[str, List[Callable]]:
    """Get shared file editors. (for identical files)"""
    return {
        "GameData/Generated/Gameplay/Gfx/BuildingDescriptors.ndf": [
            lambda source: add_fob_minimap_module(source),
        ],
        "GameData/Generated/UserInterface/Textures/MinimapIcons.ndf": [
            lambda source: add_fob_minimap_texture(source),
        ]
    } 
