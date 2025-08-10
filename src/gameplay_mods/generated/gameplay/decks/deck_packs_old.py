"""Functions for modifying deck packs and their references."""

from typing import Any, Dict

from src.constants.new_units import NEW_UNITS
from src.constants.unit_edits import load_unit_edits
from src.constants.unit_edits.SUPPLY_unit_edits import supply_unit_edits
from src.utils.logging_utils import setup_logger

logger = setup_logger(__name__)


def _remove_duplicate_deck_packs(source_path: Any) -> None:
    """Remove deck packs with duplicate namespaces, keeping only the first occurrence."""
    seen_namespaces = set()
    duplicates_to_remove = []

    for deck_pack in source_path:
        if not hasattr(deck_pack, "namespace"):
            continue

        if not deck_pack.namespace.startswith("Descriptor_Deck_Pack_"):
            continue

        if deck_pack.namespace in seen_namespaces:
            duplicates_to_remove.append(deck_pack)
        else:
            seen_namespaces.add(deck_pack.namespace)

    # Remove all duplicates
    for duplicate in duplicates_to_remove:
        logger.info(f"Removing duplicate deck pack: {duplicate.namespace}")
        source_path.remove(duplicate)

    if duplicates_to_remove:
        logger.info(f"Removed {len(duplicates_to_remove)} duplicate deck packs")


def modify_deck_packs(source_path: Any, game_db: Dict[str, Any]) -> None:
    """GameData\Generated\Gameplay\Decks\DeckPacks.ndf"""
    logger.info("Modifying deck packs using precomputed database mappings")

    # Get precomputed mappings from database
    deck_pack_mappings = game_db.get("deck_pack_mappings", {})

    if not deck_pack_mappings:
        logger.info("No deck pack mappings found in database")
        return

    # Extract only the deck pack modifications (XP/number changes only)
    deck_pack_modifications = deck_pack_mappings.get("deck_pack_modifications", {})

    if not deck_pack_modifications:
        logger.info("No deck pack modifications found in database")
        return

    # IMPORTANT: Create new command unit deck packs FIRST before modifying existing ones
    _create_new_command_unit_deck_packs_from_database(source_path, game_db)

    # Apply ONLY deck pack modifications (never unit name changes)
    _apply_deck_pack_modifications_from_database(source_path, deck_pack_modifications)

    # Clean up any duplicate deck packs that may have been created
    _remove_duplicate_deck_packs(source_path)


def _apply_deck_pack_modifications_from_database(source_path: Any, deck_pack_mappings: Dict[str, str]) -> None:
    """Apply precomputed deck pack modifications from database mappings."""
    modifications_applied = 0

    for deck_pack in source_path:
        if not hasattr(deck_pack, "namespace"):
            continue

        if not deck_pack.namespace.startswith("Descriptor_Deck_Pack_"):
            continue

        # Check if this deck pack has a precomputed modification
        if deck_pack.namespace in deck_pack_mappings:
            old_namespace = deck_pack.namespace
            new_namespace = deck_pack_mappings[old_namespace]

            # Parse new namespace to get target XP
            parts = new_namespace.split("_")
            if len(parts) >= 4:
                try:
                    target_xp = int(parts[-2])

                    logger.info(f"Applying modification: {old_namespace} -> {new_namespace}")

                    # Update the deck pack namespace
                    deck_pack.namespace = new_namespace
                    deck_pack.n = new_namespace

                    # Update XP value in the descriptor
                    if target_xp > 0:
                        # Add or update Xp parameter (ensure string value)
                        xp_member = deck_pack.v.by_m("Xp", False)
                        if xp_member:
                            xp_member.v = str(target_xp)
                        else:
                            deck_pack.v.insert(1, f"Xp = {target_xp}")
                    else:
                        # Remove Xp parameter for XP level 0
                        xp_member = deck_pack.v.by_m("Xp", False)
                        if xp_member:
                            deck_pack.v.remove_by_member("Xp")

                    modifications_applied += 1

                except (ValueError, IndexError) as e:
                    logger.warning(f"Failed to parse target XP from new namespace {new_namespace}: {e}")

    logger.info(f"Applied {modifications_applied} deck pack modifications")


def _create_new_command_unit_deck_packs_from_database(source_path: Any, game_db: Dict[str, Any]) -> None:
    """Create new deck packs for new command units using database data."""
    deck_pack_data = game_db.get("deck_pack_data")

    if not deck_pack_data:
        logger.warning("No deck pack data found in database")
        return

    command_units_created = 0

    for donor, edits in NEW_UNITS.items():
        donor_name = donor[0]

        # Verify required fields
        if "NewName" not in edits or "availability" not in edits:
            continue

        # Only process command units - identified by _CMD2_ in NewName
        new_unit_name = edits["NewName"]
        if "_CMD2_" not in new_unit_name:
            continue

        # Skip if donor has no deck pack data
        if donor_name not in deck_pack_data["base_units"]:
            logger.warning(f"No deck pack data found for donor {donor_name}")
            continue

        availability = edits["availability"]

        # Find all available XP levels (non-zero values in availability)
        available_xp_levels = []
        for i, avail in enumerate(availability):
            if avail > 0:
                available_xp_levels.append(i)

        if not available_xp_levels:
            logger.warning(f"No valid XP levels found for new unit {new_unit_name}")
            continue

        logger.info(f"Creating new command unit deck packs for {new_unit_name} at XP levels {available_xp_levels}")

        # Get donor deck pack info from database
        donor_data = deck_pack_data["base_units"][donor_name]

        # Find donor deck packs to use as templates (both simple and transport)
        all_donor_pack_namespaces = donor_data["simple_packs"] + donor_data["transport_packs"]
        donor_templates = {}  # namespace -> deck_pack
        for deck_pack in source_path:
            if deck_pack.namespace in all_donor_pack_namespaces:
                donor_templates[deck_pack.namespace] = deck_pack

        if not donor_templates:
            logger.warning(f"No donor template packs found for {donor_name}")
            continue

        # Create new deck packs for each donor template and each XP level
        for donor_namespace, template_pack in donor_templates.items():
            # Parse the donor namespace to understand its structure
            parts = donor_namespace.split("_")
            if len(parts) < 4:
                continue

            try:
                number = int(parts[-1])
                donor_xp = int(parts[-2])

                # Replace donor unit name with new unit name in the namespace structure
                donor_unit_part = "_".join(parts[3:-2])  # Everything between prefix and _XP_Number
                new_unit_part = donor_unit_part.replace(donor_name, new_unit_name, 1)

                for target_xp in available_xp_levels:
                    # Create new namespace preserving transport information
                    new_namespace = f"Descriptor_Deck_Pack_{new_unit_part}_{target_xp}_{number}"

                    logger.info(f"Creating new deck pack {new_namespace}")

                    # Clone the template pack
                    new_deck_pack = template_pack.copy()
                    new_deck_pack.namespace = new_namespace
                    new_deck_pack.n = new_namespace

                    # Update Unit reference
                    new_deck_pack.v.by_m("Unit").v = f"$/GFX/Unit/Descriptor_Unit_{new_unit_name}"

                    # Update XP value (ensure string value)
                    if target_xp > 0:
                        xp_member = new_deck_pack.v.by_m("Xp", False)
                        if xp_member:
                            xp_member.v = str(target_xp)
                        else:
                            new_deck_pack.v.insert(1, f"Xp = {target_xp}")
                    else:
                        # Remove Xp parameter for XP level 0
                        xp_member = new_deck_pack.v.by_m("Xp", False)
                        if xp_member:
                            new_deck_pack.v.remove_by_member("Xp")

                    # Add the new deck pack to source
                    source_path.add(new_deck_pack)
                    command_units_created += 1

            except (ValueError, IndexError):
                logger.warning(f"Failed to parse donor namespace {donor_namespace}")
                continue

    logger.info(f"Created {command_units_created} new command unit deck packs")


def update_deck_pack_references(source_path: Any, game_db: Dict[str, Any]) -> None:
    """GameData\Generated\Gameplay\Decks\Decks.ndf."""
    deck_pack_mappings = game_db.get("deck_pack_mappings", {})

    if not deck_pack_mappings:
        logger.info("No deck pack namespace mappings found in database")
        return

    # Get both types of mappings for reference updates
    deck_pack_modifications = deck_pack_mappings.get("deck_pack_modifications", {})
    reference_mappings = deck_pack_mappings.get("reference_mappings", {})

    # Combine for reference lookup (both XP changes and unit name changes apply to references)
    all_reference_mappings = {}
    all_reference_mappings.update(deck_pack_modifications)
    all_reference_mappings.update(reference_mappings)

    logger.info(f"Updating deck pack references using {len(all_reference_mappings)} precomputed mappings")

    for deck_obj in source_path:
        if not deck_obj.namespace.startswith("Descriptor_Deck_"):
            continue

        deck_pack_list = deck_obj.v.by_m("DeckPackList").v

        for pack_ref in deck_pack_list:
            old_ref = pack_ref.v.replace("~/", "")

            # Check both modification and reference mappings
            if old_ref in all_reference_mappings:
                new_ref = f"~/{all_reference_mappings[old_ref]}"
                logger.info(f"Updating deck reference {pack_ref.v} to {new_ref}")
                pack_ref.v = new_ref

    # Handle removal of deck packs from multi decks based on unit edits
    _remove_deck_packs_from_multi_decks(source_path)


def _remove_deck_packs_from_multi_decks(source_path: Any) -> None:
    """Remove deck pack references from multi decks when units have 'remove' divisions."""
    logger.info("Processing deck pack removals from multi decks")

    # Load unit edits
    unit_edits = load_unit_edits()
    unit_edits.update(supply_unit_edits)

    removals_processed = 0

    # Find units that have "remove" divisions
    for unit_name, edits in unit_edits.items():
        if "Divisions" not in edits:
            continue

        divisions_config = edits["Divisions"]
        if not isinstance(divisions_config, dict) or "remove" not in divisions_config:
            continue

        divisions_to_remove = divisions_config["remove"]
        if not isinstance(divisions_to_remove, list):
            continue

        logger.info(f"Processing removal of {unit_name} from divisions: {divisions_to_remove}")

        # For each division to remove from, find the corresponding multi deck
        for division_name in divisions_to_remove:
            multi_deck_name = f"Descriptor_Deck_{division_name}_multi"

            # Find the multi deck in source_path
            multi_deck = None
            for deck_obj in source_path:
                if hasattr(deck_obj, "namespace") and deck_obj.namespace == multi_deck_name:
                    multi_deck = deck_obj
                    break

            if not multi_deck:
                logger.warning(f"Multi deck {multi_deck_name} not found")
                continue

            # Get the DeckPackList
            deck_pack_list = multi_deck.v.by_m("DeckPackList")
            if not deck_pack_list:
                logger.warning(f"DeckPackList not found in {multi_deck_name}")
                continue

            # Remove all deck pack references for this unit
            pack_refs_to_remove = []
            for pack_ref in deck_pack_list.v:
                ref_value = pack_ref.v.replace("~/", "")

                # Check if this reference is for the unit we want to remove
                if ref_value.startswith(f"Descriptor_Deck_Pack_{unit_name}_"):
                    pack_refs_to_remove.append(pack_ref)

            # Remove the identified references
            for pack_ref in pack_refs_to_remove:
                logger.info(f"Removing {pack_ref.v} from {multi_deck_name}")
                deck_pack_list.v.remove(pack_ref)
                removals_processed += 1

    logger.info(f"Processed {removals_processed} deck pack removals from multi decks")


def new_deck_packs(source_path: Any) -> None:
    """Create new deck packs in DeckPacks.ndf."""
    logger.info("Creating new deck packs")

    # Create new deck pack for 8th Infantry Division (temp until we create constants for editing decks)
    new_deck_pack = (
        "Descriptor_Deck_Pack_8th_M1A1_Abrams_US_1_1 is DeckPackDescriptor"
        "("
        "    Xp = 1"
        "    Unit = $/GFX/Unit/Descriptor_Unit_8th_M1A1_Abrams_US\n"
        "    Number = 1"
        ")"
    )
    source_path.add(new_deck_pack)

    new_deck_pack = (
        "Descriptor_Deck_Pack_Scout_LRRP_POL_Mi_24D_POL_2_1 is DeckPackDescriptor"
        "("
        "    Xp = 2"
        "    Transport = $/GFX/Unit/Descriptor_Unit_Mi_24D_POL"
        "    Unit = $/GFX/Unit/Descriptor_Unit_Mi_24D_POL"
        "    Number = 1"
        ")"
    )
    source_path.add(new_deck_pack)
