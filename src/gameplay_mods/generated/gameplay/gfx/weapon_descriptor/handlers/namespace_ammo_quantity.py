from typing import Any, Dict

from src.constants.weapons import ammunitions
from src.constants.new_units import NEW_UNITS
from src.constants.unit_edits import load_unit_edits


def update_weapondescr_ammoname_quantity(source_path, logger, game_db):
    """Update the quantities in ammo names for WeaponDescriptor.ndf"""
    logger.info("Updating quantities in ammo namespaces in WeaponDescriptor.ndf")
    ammo_db = game_db["ammunition"]
    weapon_db = game_db["weapons"]
    unit_db = game_db["unit_data"]

    unit_edits = load_unit_edits()

    for weapon_descr_name, weapon_descr_data in weapon_db.items():
        # Get unit name and strength
        unit_name = weapon_descr_name.replace("WeaponDescriptor_", "")

        # Check for edited strength in unit_edits first
        unit_strength = None
        if unit_name in unit_edits and "strength" in unit_edits[unit_name]:
            unit_strength = unit_edits[unit_name]["strength"]
        # Fall back to unit_db if no edit exists
        if unit_strength is None and unit_name in unit_db:
            unit_strength = unit_db[unit_name].get("strength")

        if not unit_strength:
            if unit_name in NEW_UNITS:
                logger.debug(f"{unit_name} is a new unit, skipping")
                continue
            else:
                logger.warning(f"No strength found for unit {unit_name}")
                continue

        for (weapon_name, category, donor, is_new), data in ammunitions.items():
            if category != "small_arms":
                continue

            # Check if this weapon should use strength variants
            use_strength = False
            damage_family = data.get("Ammunition", {}).get("Arme", {}).get("Family")
            if damage_family in ["DamageFamily_sa_full", "DamageFamily_sa_intermediate"]:
                use_strength = True

            for turret_index, turret_data in weapon_descr_data["turrets"].items():
                old_name = ammo_db["renames_new_old"].get(weapon_name, None)

                if not old_name and weapon_name in turret_data["weapons"]:
                    quantity = turret_data["weapons"][weapon_name].get("quantity", None)
                    if quantity is None:
                        logger.debug(f"No quantity found for {weapon_name}")
                        continue

                elif old_name in turret_data["weapons"]:
                    quantity = turret_data["weapons"][old_name].get("quantity", None)
                    if quantity is None:
                        logger.debug(f"No quantity found for {weapon_name} or {old_name}")
                        continue

                else:
                    continue

                weapon_descr = source_path.by_n(weapon_descr_name)
                turret_list = weapon_descr.v.by_m("TurretDescriptorList")
                turret = turret_list.v[int(turret_index)]

                for mounted_wpn in turret.v.by_m("MountedWeaponDescriptorList").v:
                    ammo = mounted_wpn.v.by_m("Ammunition").v
                    ammo_n = ammo.split("_", 1)[1]
                    prefix = ammo.split("_", 1)[0]
                    nb_weapons = mounted_wpn.v.by_m("NbWeapons").v

                    if old_name and old_name == ammo_n:
                        if int(nb_weapons) == quantity:
                            if quantity > 1:
                                new_ammo = f"{prefix}_{weapon_name}_x{quantity}"
                                if use_strength:
                                    new_ammo = f"{prefix}_{weapon_name}_strength{unit_strength}_x{quantity}"
                            else:
                                new_ammo = f"{prefix}_{weapon_name}"
                                if use_strength:
                                    new_ammo = f"{prefix}_{weapon_name}_strength{unit_strength}"
                            mounted_wpn.v.by_m("Ammunition").v = new_ammo
                            logger.info(f"Updated ammo {ammo} to {new_ammo}")
                        else:
                            logger.debug(
                                f"database quantity ({quantity}) differs from "
                                f"NbWeapons ({nb_weapons}) for {weapon_name}"
                            )
                            if int(nb_weapons) > 1:
                                new_ammo = f"{prefix}_{weapon_name}_x{quantity}"
                                if use_strength:
                                    new_ammo = f"{prefix}_{weapon_name}_strength{unit_strength}_x{quantity}"
                            else:
                                new_ammo = f"{prefix}_{weapon_name}"
                                if use_strength:
                                    new_ammo = f"{prefix}_{weapon_name}_strength{unit_strength}"
                            mounted_wpn.v.by_m("Ammunition").v = new_ammo
                            logger.info(f"Updated ammo {ammo} to {new_ammo}")

                    elif ammo_n == weapon_name:
                        if int(nb_weapons) == quantity:
                            if quantity > 1:
                                new_ammo = f"{prefix}_{weapon_name}_x{quantity}"
                                if use_strength:
                                    new_ammo = f"{prefix}_{weapon_name}_strength{unit_strength}_x{quantity}"
                            else:
                                new_ammo = f"{prefix}_{weapon_name}"
                                if use_strength:
                                    new_ammo = f"{prefix}_{weapon_name}_strength{unit_strength}"
                            mounted_wpn.v.by_m("Ammunition").v = new_ammo
                            logger.info(f"Updated ammo {ammo} to {new_ammo}")