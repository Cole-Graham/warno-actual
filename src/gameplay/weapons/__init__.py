"""Editors for GameData/Generated/Gameplay/WeaponDescriptor.ndf"""

from typing import Any, Callable, Dict, List

from .unit_edits import edit_units


def get_editors(unit_db: Dict[str, Any]) -> List[Callable]:
    """Get all editors for WeaponDescriptor.ndf."""
    return [
        lambda source: edit_units(source),
    ] 