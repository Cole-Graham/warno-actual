"""Functions for modifying mortar weapons."""

from typing import Any, Dict

import logging


def add_corrected_shot_dispersion(source_path: Any, logger: logging.Logger, game_db: Dict[str, Any]) -> None:
    """Add corrected shot dispersion to mortar weapons."""
    ammo_db = game_db["ammunition"]

    logger.info("Adding corrected shot dispersion to mortars")
    mortar_categories = ammo_db["mortar_weapons"]
    renames_new_old = ammo_db.get("renames_new_old", {})

    insert_index = 0

    for weapon_descr in source_path:
        name = weapon_descr.n.replace("Ammo_", "")

        # Resolve vanilla renames: mortar_categories uses original names, but descriptors
        # may have been renamed (e.g. Mortier_M40_107mm -> Mortier_M30_107mm)
        lookup_name = renames_new_old.get(name, name)

        # Check if weapon is a mortar
        if lookup_name in mortar_categories["mortars"]:
            dispersion = 0.7
        elif lookup_name in mortar_categories["smoke_mortars"]:
            dispersion = 0.9
        else:
            continue

        # Add dispersion multiplier
        existing_multiplier = None
        for i, member in enumerate(weapon_descr.v):
            if member.m == "SalvoShotsSorted":
                insert_index = i + 1
            elif member.m == "CorrectedShotDispersionMultiplier":
                existing_multiplier = member.v

        if existing_multiplier is not None:
            logger.info(
                f"Corrected shot dispersion multiplier already exists for {name}, with value {existing_multiplier}"
            )
        else:
            weapon_descr.v.insert(insert_index, f"CorrectedShotDispersionMultiplier = {dispersion}")
            logger.info(f"Added {dispersion} dispersion multiplier for {name}")