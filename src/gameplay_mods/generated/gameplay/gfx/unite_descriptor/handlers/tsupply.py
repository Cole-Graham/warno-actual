"""Edit TSupplyModuleDescriptor for existing and new units"""


def handle_supply_module(
    logger,
    game_db,
    unit_data,
    edit_type,
    unit_name,
    edits,
    module,
    *args,
) -> None:
    """Edit TSupplyModuleDescriptor for existing and new units"""

    supply_edits = edits.get("Supply", {})
    if not supply_edits:
        return

    if edit_type == "unit_edits" and not unit_data["is_supply_unit"]:
        return

    membr = module.v.by_m
    supply_descr = membr("SupplyDescriptor", False)
    supply_capacity = membr("SupplyCapacity", False)

    if not supply_descr or not supply_capacity:
        logger.warning(f"Missing supply descriptors for {unit_name}")
        return

    old_capacity = supply_capacity.v

    if "SupplyDescriptor" in supply_edits:
        supply_descr.v = f"$/GFX/Weapon/{supply_edits['SupplyDescriptor']}"
        logger.info(f"Set {unit_name} supply descriptor to {supply_edits['SupplyDescriptor']}")

    if "SupplyCapacity" in supply_edits:
        new_capacity = str(supply_edits["SupplyCapacity"])
        if old_capacity != new_capacity:
            supply_capacity.v = new_capacity
            logger.info(f"Updated {unit_name} supply capacity: {old_capacity} -> {new_capacity}")

    if "SupplyPriority" in supply_edits:
        supply_priority = membr("SupplyPriority", False)
        if supply_priority:
            new_priority = str(supply_edits["SupplyPriority"])
            if supply_priority.v != new_priority:
                supply_priority.v = new_priority
                logger.info(f"Updated {unit_name} supply priority to {new_priority}")
