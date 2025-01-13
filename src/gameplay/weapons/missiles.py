"""Editor for AmmunitionMissiles.ndf."""

from typing import Any, Dict

from src.dics.weapon_edits.vanilla_inst_modifications import (
    ammunition_missiles_removals,
    ammunition_missiles_renames,
)

from .vanilla_modifications import apply_vanilla_renames, remove_vanilla_instances


def edit_missiles(source, unit_db: Dict[str, Any]) -> None:
    """Edit AmmunitionMissiles.ndf file."""
    # First handle vanilla modifications
    apply_vanilla_renames(source, ammunition_missiles_renames)
    remove_vanilla_instances(source, ammunition_missiles_removals)
    
    # Then apply other edits... 