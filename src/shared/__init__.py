"""Shared modifications. (identical files)"""

from typing import Callable, Dict, List

from . import add_fob_minimap_module


def get_shared_editors() -> Dict[str, List[Callable]]:
    """Get shared file editors. (for identical files)"""
    return {
        "GameData/Generated/Gameplay/Gfx/BuildingDescriptors.ndf": [
            lambda source: add_fob_minimap_module(source),
        ],
    } 
