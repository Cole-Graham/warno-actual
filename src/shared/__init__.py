"""Shared modifications. (identical files)"""

from typing import Callable, Dict, List

from .buildings.fob import add_fob_minimap_texture
from src.ui import edit_uicommonflarelabelresources

# defunct (for now? I had to simplify config/build pipelines to get the patcher working)
def get_shared_editors() -> Dict[str, List[Callable]]:
    """Get shared file editors. (for identical files)"""
    return {
        "GameData/Generated/UserInterface/Textures/MinimapIcons.ndf": [
            add_fob_minimap_texture,  # Direct function reference instead of lambda
        ],
        "GameData/UserInterface/Use/Common/UICommonFlareLabelResources.ndf": [
            edit_uicommonflarelabelresources,  # Direct function reference instead of lambda
        ]
    }   