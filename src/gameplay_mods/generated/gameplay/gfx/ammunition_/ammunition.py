"""Editor for Ammunition.ndf."""

from typing import Any, Dict, List, Tuple
from uuid import uuid4

from src import ndf
from src.constants.weapons import ammunitions
from src.constants.weapons.vanilla_inst_modifications import AMMUNITION_REMOVALS
from src.utils.dictionary_utils import write_dictionary_entries
from src.utils.logging_utils import setup_logger

from .handlers import (
    add_corrected_shot_dispersion,
    apply_aim_time_standards,
    apply_bomb_damage_standards,
    apply_damage_families,
    apply_fire_descriptors,
    apply_he_damage_standards,
    apply_weapon_range_standards,
    remove_vanilla_instances,
    vanilla_renames_ammunition,
)

logger = setup_logger(__name__)


def edit_gen_gp_gfx_ammunition(source_path, game_db: Dict[str, Any]) -> None:
    """GameData/Generated/Gameplay/Gfx/Ammunition.ndf"""
    try:
        ammo_db = game_db["ammunition"]

        # Handle vanilla modifications first
        try:
            vanilla_renames_ammunition(source_path, logger, ammo_db)
            remove_vanilla_instances(source_path, logger, AMMUNITION_REMOVALS)
            logger.debug("Applied vanilla modifications")
        except Exception as e:
            logger.error(f"Failed applying vanilla modifications: {str(e)}")
            raise

        # Apply global modifications
        try:
            add_corrected_shot_dispersion(source_path, logger, game_db)
            # edit_mg_team_weapons(source_path, game_db)
            apply_damage_families(source_path, logger, game_db)
            apply_aim_time_standards(source_path, logger)
            apply_weapon_range_standards(source_path, logger)
            apply_bomb_damage_standards(source_path, logger)
            apply_he_damage_standards(source_path, logger)
            apply_fire_descriptors(source_path, logger)
            logger.debug("Applied global modifications")
        except Exception as e:
            logger.error(f"Failed applying global modifications: {str(e)}")
            raise

        # Track dictionary entries
        ingame_names = []
        calibers = []

        # Process each weapon
        for (weapon_name, category, donor, is_new), data in ammunitions.items():
            if "Ammunition" not in data:
                continue

            logger.info(f"Processing weapon {weapon_name} (is_new={is_new})")
            try:
                ammo_data = data["Ammunition"]

                # Determine if weapon should use strength variants
                use_strength = False
                if category == "small_arms":
                    damage_family = ammo_data.get("Arme", {}).get("Family")
                    use_strength = damage_family in ["DamageFamily_sa_full", "DamageFamily_sa_intermediate"]

                # Get or create base descriptor
                try:
                    if is_new:
                        base_descr = _create_new_descriptor(source_path, data, weapon_name, donor)
                    else:
                        base_descr = _get_existing_descriptor(source_path, weapon_name)

                    if not base_descr:
                        logger.error(f"Could not get descriptor for {weapon_name}")
                        continue

                    logger.debug(f"Got base descriptor for {weapon_name}")
                except Exception as e:
                    logger.error(f"Failed getting descriptor for {weapon_name}: {str(e)}")
                    continue

                # Apply edits
                try:
                    _apply_weapon_edits(base_descr, category, data, ammo_data)
                    logger.debug(f"Applied edits to {weapon_name}")
                except Exception as e:
                    logger.error(f"Failed applying edits to {weapon_name}: {str(e)}")
                    continue

                # Handle new weapons and quantities
                try:
                    if is_new:
                        if "NbWeapons" not in data or len(data["NbWeapons"]) == 1:
                            # Add strength to base namespace if needed
                            if use_strength:
                                base_descr.namespace = f"Ammo_{weapon_name}_strength2"  # Start at strength2
                                base_descr.v.by_m("Arme").v.by_m("Index").v = "1"  # Index starts at 1
                            source_path.add(base_descr)
                            logger.debug(
                                f"Added new base descriptor for {weapon_name} "
                                f"(is_new={is_new}, {base_descr.namespace})"
                            )

                    if "NbWeapons" in data:
                        base_cost = _get_base_supply_cost(weapon_name)
                        if len(data["NbWeapons"]) > 1:
                            _create_quantity_variants(
                                source_path, base_descr, weapon_name, data["NbWeapons"], base_cost,
                                is_new, use_strength, category
                            )
                        elif category == "small_arms" and data["NbWeapons"][0] > 1:
                            # Set base namespace first with strength if needed
                            if use_strength:
                                for strength in range(2, 17):
                                    strength_descr = base_descr.copy()
                                    strength_descr.namespace = (
                                        f"Ammo_{weapon_name}_strength{strength}_x{data['NbWeapons'][0]}"
                                    )
                                    arme_index = min(strength - 1, 13)
                                    strength_descr.v.by_m("Arme").v.by_m("Index").v = str(arme_index)

                                    # Generate unique GUIDs for descriptor IDs
                                    strength_descr.v.by_m("DescriptorId").v = f"GUID:{{{uuid4()}}}"
                                    hitroll_obj = strength_descr.v.by_m("HitRollRuleDescriptor")
                                    hitroll_obj.v.by_m("DescriptorId").v = f"GUID:{{{uuid4()}}}"

                                    source_path.add(strength_descr)
                                    logger.debug(f"Added strength {strength} variant for {weapon_name}")
                            else:
                                base_descr.namespace = f"Ammo_{weapon_name}_x{data['NbWeapons'][0]}"

                        elif category == "small_arms" and data["NbWeapons"][0] == 1:
                            if use_strength and not is_new:
                                for strength in range(2, 17):
                                    strength_descr = base_descr.copy()
                                    strength_descr.namespace = f"Ammo_{weapon_name}_strength{strength}"
                                    arme_index = min(strength - 1, 13)
                                    strength_descr.v.by_m("Arme").v.by_m("Index").v = str(arme_index)

                                    # Generate unique GUIDs for descriptor IDs
                                    strength_descr.v.by_m("DescriptorId").v = f"GUID:{{{uuid4()}}}"
                                    hitroll_obj = strength_descr.v.by_m("HitRollRuleDescriptor")
                                    hitroll_obj.v.by_m("DescriptorId").v = f"GUID:{{{uuid4()}}}"

                                    source_path.add(strength_descr)
                                    logger.debug(f"Added strength {strength} variant for {weapon_name}")
                            # else:
                            #     base_descr.namespace = f"Ammo_{weapon_name}"

                except Exception as e:
                    logger.error(f"Failed handling quantities for {weapon_name}: {str(e)}")
                    continue

                # Track dictionary entries
                try:
                    _track_dictionary_entries(weapon_name, ammo_data, ingame_names, calibers)
                except Exception as e:
                    logger.error(f"Failed tracking dictionary entries for {weapon_name}: {str(e)}")
                    continue

                logger.info(f"Successfully processed weapon {weapon_name}")

            except Exception as e:
                logger.error(f"Failed processing weapon {weapon_name}: {str(e)}")
                continue

        # Write dictionary entries
        if ingame_names or calibers:
            try:
                write_ammo_dictionary_entries(ingame_names, calibers)
            except Exception as e:
                logger.error(f"Failed writing dictionary entries: {str(e)}")
                raise

    except Exception as e:
        logger.error(f"Fatal error in edit_ammunition: {str(e)}")
        raise


def _should_use_strength_variant(weapon_name: str) -> bool:
    """Check if a weapon should use strength variants based on its damage family.

    Args:
        weapon_name: Name of the weapon to check

    Returns:
        bool: True if weapon should use strength variants
    """
    for (ammo_name, category, _, _), data in ammunitions.items():
        if ammo_name == weapon_name and category == "small_arms":
            damage_family = data.get("Ammunition", {}).get("Arme", {}).get("Family")
            return damage_family in ["DamageFamily_sa_full", "DamageFamily_sa_intermediate"]
    return False


def _create_quantity_variants(
    source_path,
    base_descr,
    weapon_name,
    quantities,
    base_cost,
    is_new,
    use_strength,
    category,
):
    """Create quantity and strength variants from base ammunition descriptor."""
    logger.info(f"Creating quantity and strength variants for {weapon_name} (is_new={is_new})")
    logger.info(f"Quantities: {quantities}")

    # Track created variants to avoid duplicates
    created_variants = set()

    # Create variants for each quantity
    for i, quantity in enumerate(quantities):
        if use_strength:
            # Create strength variants for each quantity
            for strength in range(2, 17):  # 2 to 16 inclusive
                # Only create quantity variants up to the strength value
                effective_quantity = min(quantity, strength)

                if effective_quantity == 1 and i == len(quantities) - 1:
                    namespace = f"Ammo_{weapon_name}_strength{strength}"
                else:
                    namespace = f"Ammo_{weapon_name}_strength{strength}_x{effective_quantity}"

                # Skip if we've already created this variant
                if namespace in created_variants:
                    logger.debug(f"Skipping duplicate variant {namespace}")
                    continue

                existing = source_path.by_n(namespace, strict=False)
                logger.debug(f"Checking {namespace} - exists: {existing is not None}")

                if is_new or (existing is None):
                    # Create new variant
                    variant = base_descr.copy()
                    variant.v.by_m("DescriptorId").v = f"GUID:{{{uuid4()}}}"
                    variant.v.by_m("HitRollRuleDescriptor").v.by_m("DescriptorId").v = f"GUID:{{{uuid4()}}}"
                    variant.namespace = namespace

                    # Set Arme Index based on strength
                    arme_obj = variant.v.by_m("Arme").v
                    arme_index = min(strength - 1, 13)
                    arme_obj.by_m("Index").v = str(arme_index)

                    if base_cost is not None:
                        # Scale supply cost by effective quantity
                        variant_supply_cost = base_cost * effective_quantity
                        if category == "small_arms":
                            # 66% modifier to limit the supply costs of small arms
                            # None digits will round to the nearest integer, then convert back to float
                            small_arms_variant_cost = float(round((variant_supply_cost * 0.66), None))
                            variant.v.by_m("SupplyCost").v = str(small_arms_variant_cost)
                        else:
                            variant.v.by_m("SupplyCost").v = str(variant_supply_cost)

                    source_path.add(variant)
                    created_variants.add(namespace)
                    logger.info(f"Created new variant {namespace}")
                else:
                    # Update both supply cost and Arme Index
                    if base_cost is not None:
                        # Scale supply cost by effective quantity
                        existing_supply_cost = base_cost * effective_quantity
                        if category == "small_arms":
                            # 66% modifier to limit the supply costs of small arms
                            # None digits will round to the nearest integer, then convert back to float
                            small_arms_existing_cost = float(round((existing_supply_cost * 0.66), None))
                            existing.v.by_m("SupplyCost").v = str(small_arms_existing_cost)
                        else:
                            existing.v.by_m("SupplyCost").v = str(existing_supply_cost)

                    arme_index = min(strength - 1, 13)
                    existing.v.by_m("Arme").v.by_m("Index").v = str(arme_index)
                    created_variants.add(namespace)
                    logger.debug(f"Updated existing variant {namespace}")
        else:
            # Create regular quantity variant without strength
            if quantity == 1 and i == len(quantities) - 1:
                namespace = f"Ammo_{weapon_name}"
            else:
                namespace = f"Ammo_{weapon_name}_x{quantity}"

            existing = source_path.by_n(namespace, strict=False)
            if is_new or (existing is None):
                variant = base_descr.copy()
                variant.v.by_m("DescriptorId").v = f"GUID:{{{uuid4()}}}"
                variant.v.by_m("HitRollRuleDescriptor").v.by_m("DescriptorId").v = f"GUID:{{{uuid4()}}}"
                variant.namespace = namespace

                if base_cost is not None:
                    # Scale supply cost by quantity
                    variant_supply_cost = base_cost * quantity
                    if category == "small_arms":
                        # 66% modifier to limit the supply costs of small arms
                        # None digits will round to the nearest integer, then convert back to float
                        small_arms_variant_cost = float(round((variant_supply_cost * 0.66), None))
                        variant.v.by_m("SupplyCost").v = str(small_arms_variant_cost)
                    else:
                        variant.v.by_m("SupplyCost").v = str(variant_supply_cost)

                source_path.add(variant)
                logger.info(f"Created new variant {namespace}")
            else:
                if base_cost is not None:
                    # Scale supply cost by quantity
                    existing_supply_cost = base_cost * quantity
                    if category == "small_arms":
                        # 66% modifier to limit the supply costs of small arms
                        # None digits will round to the nearest integer, then convert back to float
                        small_arms_existing_cost = float(round((existing_supply_cost * 0.66), None))
                        existing.v.by_m("SupplyCost").v = str(small_arms_existing_cost)
                    else:
                        existing.v.by_m("SupplyCost").v = str(existing_supply_cost)
                    logger.debug(f"Updated existing variant {namespace}")


def _apply_weapon_edits(descr: Any, category: str, data: Dict, ammo_data: Dict) -> None:
    """Apply edits from ammunition data to descriptor."""
    membr = descr.v.by_m

    logger.debug(f"Applying edits to {descr.n}")

    if "token" in ammo_data:
        descr.v.by_m("Name").v = "'" + ammo_data["token"] + "'"

    # Apply Arme edits
    if "Arme" in ammo_data:
        arme_data = ammo_data["Arme"]
        arme_obj = descr.v.by_m("Arme").v

        for arme_membr, arme_v in arme_data.items():
            if isinstance(arme_v, (float, int, bool)):
                arme_obj.by_m(arme_membr).v = str(arme_v)
            else:
                arme_obj.by_m(arme_membr).v = arme_v

    # Apply parent member edits
    if "parent_membr" in ammo_data:
        for key, value in ammo_data["parent_membr"].items():
            logger.debug(f"Setting {key} = {value}")
            if key == "add":  # adding new member, e.g. [16, "MaximumRangeHelicopterGRU = 875"]
                for index, new_member in value:
                    descr.v.insert(index, new_member)
            elif isinstance(value, (float, int, bool)):
                membr(key).v = str(value)
            elif isinstance(value, tuple) and key == "Caliber":
                membr(key).v = f"'{value[1]}'"
            elif isinstance(value, list):
                # Convert list to NDF format
                list_str = "[" + ", ".join(f"'{item}'" for item in value) + "]"
                logger.debug(f"Converting list {list_str} to NDF")
                membr(key).v = ndf.convert(list_str.encode("utf-8"))[0].v
            elif isinstance(value, str):
                membr(key).v = str(value)
            else:
                logger.error(f"Unknown type for {key}: {type(value)}")

    # Apply hit roll edits
    if "hit_roll" in ammo_data:
        _apply_hit_roll_edits(descr, ammo_data["hit_roll"])

    # Apply texture
    if "NewTexture" in data:
        texture_file = '"' + f"Texture_Interface_Weapon_{data['NewTexture']}" + '"'
        membr("InterfaceWeaponTexture").v = texture_file
        logger.debug(f"Applied texture {texture_file}")

    if "Texture" in data:
        texture_file = '"' + f"Texture_Interface_Weapon_{data['Texture']}" + '"'
        membr("InterfaceWeaponTexture").v = texture_file
        logger.debug(f"Applied texture {texture_file}")


def _apply_hit_roll_edits(descr: Any, hit_roll_data: Dict) -> None:
    """Apply hit roll edits to ammunition descriptor."""

    hitroll_obj = descr.v.by_m("HitRollRuleDescriptor").v

    if "BaseCriticModifier" in hit_roll_data:
        hitroll_obj.by_m("BaseCriticModifier").v = str(hit_roll_data["BaseCriticModifier"])

    modifiers = hitroll_obj.by_m("BaseHitValueModifiers").v
    if "Idling" in hit_roll_data:
        modifiers[1].v = (modifiers[1].v[0], str(hit_roll_data["Idling"]))
    if "Moving" in hit_roll_data:
        modifiers[2].v = (modifiers[2].v[0], str(hit_roll_data["Moving"]))


def _track_dictionary_entries(weapon_name, ammo_data, ingame_names, calibers):
    """Track dictionary entries for ammunition."""
    if "display" in ammo_data and "token" in ammo_data:
        ingame_names.append((weapon_name, ammo_data["token"], ammo_data["display"]))

    if "parent_membr" in ammo_data and "Caliber" in ammo_data["parent_membr"]:
        caliber_data = ammo_data["parent_membr"]["Caliber"]
        if caliber_data[0] != "existing":
            calibers.append((weapon_name, caliber_data[1], caliber_data[0]))

def get_supply_costs(weapons_dict: Dict) -> List[Tuple[str, int]]:
    """Get base supply costs for weapons."""
    weapon_costs = []
    for (weapon, _, _, _), data in weapons_dict.items():
        if data is None:
            continue
        if supply_cost := data.get("Ammunition", {}).get("parent_membr", {}).get("SupplyCost", None):
            weapon_costs.append((weapon, supply_cost))
        elif base_supply_cost := data.get("SupplyCost", None):
            weapon_costs.append((weapon, base_supply_cost))
    return weapon_costs

def _get_base_supply_cost(weapon_name):
    """Get the base supply cost for ammunition."""
    supply_costs = get_supply_costs(ammunitions)
    for weapon, cost in supply_costs:
        if weapon == weapon_name:
            return cost
    return None


def _create_new_descriptor(source_path, data, weapon_name, donor):
    """Create a new descriptor for ammunition."""
    donor_descr = source_path.by_n(f"Ammo_{donor}")
    if not donor_descr:
        # Try without Ammo_ prefix
        donor_descr = source_path.by_n(donor)
        if not donor_descr:
            logger.error(f"Could not find donor {donor} for {weapon_name}")
            return None

    # Create base descriptor
    base_descr = donor_descr.copy()

    # Generate new GUIDs
    base_descr.v.by_m("DescriptorId").v = f"GUID:{{{uuid4()}}}"
    hitroll_obj = base_descr.v.by_m("HitRollRuleDescriptor").v
    hitroll_obj.by_m("DescriptorId").v = f"GUID:{{{uuid4()}}}"

    # Set namespace
    if "NbWeapons" in data and len(data["NbWeapons"]) == 1:
        if data["NbWeapons"][0] > 1:
            if _should_use_strength_variant(weapon_name):
                base_descr.namespace = f"Ammo_{weapon_name}_strength2_x{data['NbWeapons'][0]}"
            else:
                base_descr.namespace = f"Ammo_{weapon_name}_x{data['NbWeapons'][0]}"
        else:
            if _should_use_strength_variant(weapon_name):
                base_descr.namespace = f"Ammo_{weapon_name}_strength2"
            else:
                base_descr.namespace = f"Ammo_{weapon_name}"
    else:
        if _should_use_strength_variant(weapon_name):
            base_descr.namespace = f"Ammo_{weapon_name}_strength2"
        else:
            base_descr.namespace = f"Ammo_{weapon_name}"

    logger.debug(f"Created new base descriptor for {weapon_name} from {donor}")
    return base_descr


def _get_existing_descriptor(source_path, weapon_name):
    """Get an existing descriptor for ammunition."""
    # TODO: Somehow this broke? Its defining
    base_descr = source_path.by_n(f"Ammo_{weapon_name}")
    if not base_descr:
        # Try without Ammo_ prefix
        base_descr = source_path.by_n(weapon_name)
        if not base_descr:
            logger.error(f"Could not find weapon {weapon_name}")
            return None
    return base_descr

def write_ammo_dictionary_entries(ingame_names: List[Tuple[str, str, str]], 
                                calibers: List[Tuple[str, str, str]]) -> None:
    """Write ammunition dictionary entries."""
    entries = []
    
    # Add weapon names
    for weapon, token, display in ingame_names:
        entries.append((token, display))
        
    # Add caliber entries
    for weapon, token, display in calibers:
        entries.append((token, display))
        
    if entries:
        write_dictionary_entries(entries, dictionary_type="units")