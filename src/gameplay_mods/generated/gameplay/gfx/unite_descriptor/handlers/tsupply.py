"""Edit TTagsModuleDescriptor for existing and new units"""

from src import ndf

def handle_supply_module(
    logger,
    game_db,
    unit_data,
    edit_type,
    unit_name   ,
    edits,
    module,
    *args,
) -> None:
    """Edit TSupplyModuleDescriptor for existing and new units"""

    if edit_type == "new_units":
        pass

    if edit_type == "unit_edits":
        if not unit_data["is_supply_unit"]:
            return

        is_helo = unit_data["is_helo_unit"]

        membr = module.v.by_m
        supply_descr = membr("SupplyDescriptor")
        supply_capacity = membr("SupplyCapacity")

        if not supply_descr or not supply_capacity:
            logger.warning(f"Missing supply descriptors for {unit_name}")
            return

        old_capacity = supply_capacity.v

        if "SupplyDescriptor" in edits:
            supply_descr.v = f"$/GFX/Weapon/{edits['SupplyDescriptor']}"
            logger.info(f"Set {unit_name} supply descriptor to {edits['SupplyDescriptor']}")

        # Update capacity if specified
        if "SupplyCapacity" in edits:
            new_capacity = str(edits["SupplyCapacity"])
            if old_capacity != new_capacity:
                supply_capacity.v = new_capacity
                logger.info(f"Updated {unit_name} supply capacity: {old_capacity} -> {new_capacity}")