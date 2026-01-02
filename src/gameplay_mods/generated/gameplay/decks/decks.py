"""Functions for modifying deck packs and their references."""

from typing import Any, Dict
import re

from src.constants.generated.gameplay.decks import load_deck_edits
from src.constants.new_units import NEW_UNITS
from src.constants.unit_edits import load_unit_edits
from src.constants.unit_edits.SUPPLY_unit_edits import supply_unit_edits
from src.utils.logging_utils import setup_logger
from src import ModConfig

logger = setup_logger(__name__)

# Edit deck packs ------------------------------------------------------------------------
def edit_gen_gp_decks_deckpacks(source_path: Any, game_db: Dict[str, Any]) -> None:
    """GameData/Generated/Gameplay/Decks/DeckPacks.ndf"""
    logger.info("Modifying deck packs using precomputed database mappings")
    
    unit_edits = load_unit_edits()
    # unit_edits.update(supply_unit_edits)
    deck_pack_data = game_db.get("deck_pack_data", {})
    
    deck_pack_edits = _determine_deck_pack_edits(source_path, game_db, unit_edits)

    # IMPORTANT: Create new command unit deck packs FIRST before modifying existing ones
    new_command_unit_mappings = _create_new_command_unit_deck_packs(source_path, NEW_UNITS, deck_pack_data)
    
    # Add the new command unit mappings to deck_pack_edits for reference updates
    deck_pack_edits["new_command_unit_deck_packs"].update(new_command_unit_mappings)

    # Apply ONLY deck pack modifications (never unit name changes)
    _edit_existing_deck_packs(source_path, deck_pack_edits)

    # Clean up any duplicate deck packs that may have been created
    _remove_duplicate_deck_packs(source_path)
    
    # TODO: Needs proper implementation
    _new_deck_packs(source_path)
    
    
def _determine_deck_pack_edits(source_path: Any, game_db: Dict[str, Any], unit_edits: Dict[str, Any]) -> Dict[str, str]:
    """Determine deck pack edits from database."""
    deck_pack_data = game_db.get("deck_pack_data", {})
    deck_pack_edit_mappings = {
        "existing_deck_pack_edits": {},
        "new_command_unit_deck_packs": {},
    }

    # Process existing deck packs
    for base_unit, unit_data in deck_pack_data["base_units"].items():
        if base_unit not in unit_edits or "availability" not in unit_edits[base_unit]:
            continue

        availability = unit_edits[base_unit]["availability"]
        available_xp_levels = [i for i, avail in enumerate(availability) if avail > 0]

        if not available_xp_levels:
            continue
        
        # Group all packs (simple + transport) by their Number value
        number_groups = {}  # number -> [namespaces]
        all_unit_packs = unit_data["simple_packs"] + unit_data["transport_packs"]
        
        for namespace in all_unit_packs:
            parts = namespace.split("_")
            if len(parts) >= 4:
                try:
                    number = int(parts[-1])
                    if number not in number_groups:
                        number_groups[number] = []
                    number_groups[number].append(namespace)
                except (ValueError, IndexError):
                    continue
        
        # Process each Number group separately
        for number, namespaces in number_groups.items():
            # Get existing XP levels for this number group
            existing_xp_levels = []
            namespace_by_xp = {}  # xp -> [namespaces]
            
            for namespace in namespaces:
                parts = namespace.split("_")
                if len(parts) >= 4:
                    try:
                        current_xp = int(parts[-2])
                        existing_xp_levels.append(current_xp)
                        if current_xp not in namespace_by_xp:
                            namespace_by_xp[current_xp] = []
                        namespace_by_xp[current_xp].append(namespace)
                    except (ValueError, IndexError):
                        continue
                    
            available_xp_set = set(available_xp_levels)
            existing_xp_set = set(existing_xp_levels)
            
            packs_to_keep = available_xp_set.intersection(existing_xp_set)
            packs_to_update = existing_xp_set - available_xp_set
            missing_xp_levels = sorted(available_xp_set - existing_xp_set)
        
            missing_xp_list = missing_xp_levels.copy()
            for current_xp in sorted(packs_to_update):
                if current_xp not in namespace_by_xp:
                    continue
                
                namespaces_for_xp = namespace_by_xp[current_xp]
                target_xp = _find_best_target_xp(current_xp, available_xp_levels, missing_xp_list)
                
                if target_xp is not None and target_xp != current_xp:
                    for namespace in namespaces_for_xp:
                        parts = namespace.split("_")
                        unit_with_possible_transport = "_".join(parts[3:-2])
                        
                        old_namespace = namespace
                        new_namespace = f"Descriptor_Deck_Pack_{unit_with_possible_transport}_{target_xp}_{number}"
                        deck_pack_edit_mappings["existing_deck_pack_edits"][old_namespace] = new_namespace
                        
                        logger.debug(f"Created mapping: {old_namespace} -> {new_namespace}")
                        
                        if target_xp in missing_xp_list:
                            missing_xp_list.remove(target_xp)
                            
            logger.debug(f"Processed mappings for {base_unit}: {len(all_unit_packs)} packs")
    
    # Process transport modifications
    for base_unit, unit_data in deck_pack_data["base_units"].items():
        if base_unit not in unit_edits:
            continue
        
        # Check if unit has transport modifications
        unit_edit = unit_edits[base_unit]
        new_transports = None
        if "Divisions" in unit_edit:
            divisions_config = unit_edit["Divisions"]
            if isinstance(divisions_config, dict) and "default" in divisions_config:
                default_config = divisions_config["default"]
                if isinstance(default_config, dict) and "Transports" in default_config:
                    new_transports = default_config["Transports"]
        
        if new_transports is None:
            continue
        
        # Convert to set for easier comparison
        new_transports_set = set(new_transports)
        
        # Extract existing transports from transport pack namespaces
        existing_transports = set()
        for transport_pack_namespace in unit_data["transport_packs"]:
            parts = transport_pack_namespace.split("_")
            if len(parts) >= 4:
                # Format: Descriptor_Deck_Pack_{unit_name}_{transport_name}_{xp}_{number}
                # Extract transport name: everything between unit_name and xp
                unit_with_possible_transport = "_".join(parts[3:-2])
                if unit_with_possible_transport.startswith(base_unit + "_"):
                    transport_name = unit_with_possible_transport[len(base_unit) + 1:]  # +1 for underscore
                    existing_transports.add(transport_name)
        
        # Check if transports have changed
        if existing_transports != new_transports_set:
            logger.info(f"Transport modification detected for {base_unit}: {existing_transports} -> {new_transports_set}")
            
            # Process each transport pack
            for transport_pack_namespace in unit_data["transport_packs"]:
                parts = transport_pack_namespace.split("_")
                if len(parts) < 4:
                    continue
                
                try:
                    number = int(parts[-1])
                    xp = int(parts[-2])
                    unit_with_possible_transport = "_".join(parts[3:-2])
                    
                    # Extract existing transport name
                    if not unit_with_possible_transport.startswith(base_unit + "_"):
                        continue
                    
                    old_transport_name = unit_with_possible_transport[len(base_unit) + 1:]
                    
                    # Skip if this transport is still valid
                    if old_transport_name in new_transports_set:
                        continue
                    
                    # Map to first available new transport (or handle multiple transports)
                    # For now, map to the first new transport
                    if new_transports_set:
                        new_transport_name = sorted(new_transports_set)[0]  # Use sorted for consistency
                        
                        # Check if there's already an XP mapping for this pack
                        if transport_pack_namespace in deck_pack_edit_mappings["existing_deck_pack_edits"]:
                            # There's already an XP mapping - we need to update it to also change transport
                            existing_mapping = deck_pack_edit_mappings["existing_deck_pack_edits"][transport_pack_namespace]
                            # Parse existing mapping to extract XP and number (it may already have a transport)
                            existing_parts = existing_mapping.split("_")
                            if len(existing_parts) >= 4:
                                try:
                                    existing_xp = int(existing_parts[-2])
                                    existing_number = int(existing_parts[-1])
                                    # Create new mapping with new transport and existing (possibly updated) XP
                                    updated_namespace = f"Descriptor_Deck_Pack_{base_unit}_{new_transport_name}_{existing_xp}_{existing_number}"
                                    deck_pack_edit_mappings["existing_deck_pack_edits"][transport_pack_namespace] = updated_namespace
                                    logger.info(f"Updated transport+XP mapping: {transport_pack_namespace} -> {updated_namespace}")
                                except (ValueError, IndexError):
                                    logger.warning(f"Failed to parse existing mapping {existing_mapping} for transport update")
                        else:
                            # No existing mapping - create new transport mapping with original XP
                            new_namespace = f"Descriptor_Deck_Pack_{base_unit}_{new_transport_name}_{xp}_{number}"
                            deck_pack_edit_mappings["existing_deck_pack_edits"][transport_pack_namespace] = new_namespace
                            logger.info(f"Transport mapping: {transport_pack_namespace} -> {new_namespace}")
                    
                except (ValueError, IndexError) as e:
                    logger.warning(f"Failed to parse transport pack namespace {transport_pack_namespace}: {e}")
                    continue
            
    return deck_pack_edit_mappings


def _create_new_command_unit_deck_packs(source_path: Any, new_units: Dict[str, Any], deck_pack_data: Dict[str, Any]) -> Dict[str, str]:
    """Create new deck packs for new command units using database data."""
    new_command_unit_deck_packs = {}

    command_units_created = 0

    for donor, edits in new_units.items():
        donor_name = donor[0]

        # Verify required fields
        if "NewName" not in edits or "availability" not in edits:
            continue

        # Only process command units - identified by _CMD2_ in NewName
        new_unit_name = edits["NewName"]
        logger.debug(f"New command unit name name: {new_unit_name}")
        if "_CMD2_" not in new_unit_name:
            continue

        # Skip if donor has no deck pack data
        if donor_name not in deck_pack_data["base_units"]:
            logger.debug(f"No deck pack data found for donor {donor_name}")
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
            logger.debug(f"Donor namespace: {donor_namespace}")
            logger.debug(f"Parts: {parts}")
            if len(parts) < 4:
                logger.warning(f"Donor namespace {donor_namespace} has less than 4 parts")
                continue

            try:
                number = int(parts[-1])
                donor_xp = int(parts[-2])

                # Replace donor unit name with new unit name in the namespace structure
                donor_unit_part = "_".join(parts[3:-2])  # Everything between Descriptor_Deck_Pack_ and _{XP}_{Number}
                new_unit_part = donor_unit_part.replace(donor_name, new_unit_name, 1)

                # Determine target XP for this donor namespace
                if donor_xp in available_xp_levels:
                    target_xp = donor_xp
                elif available_xp_levels:
                    target_xp = min(available_xp_levels, key=lambda x: abs(x - donor_xp))
                else:
                    continue

                # Create the mapping from donor namespace to new namespace
                new_namespace = f"Descriptor_Deck_Pack_{new_unit_part}_{target_xp}_{number}"
                new_command_unit_deck_packs[donor_namespace] = new_namespace

                # Create deck packs for all available XP levels
                for create_xp in available_xp_levels:
                    # Create new namespace preserving transport information
                    create_namespace = f"Descriptor_Deck_Pack_{new_unit_part}_{create_xp}_{number}"

                    logger.info(f"Creating new deck pack {create_namespace}")

                    # Clone the template pack
                    new_deck_pack = template_pack.copy()
                    new_deck_pack.namespace = create_namespace
                    new_deck_pack.n = create_namespace

                    # Update Unit reference
                    new_deck_pack.v.by_m("Unit").v = f"$/GFX/Unit/Descriptor_Unit_{new_unit_name}"

                    # Update XP value (ensure string value)
                    if create_xp > 0:
                        xp_member = new_deck_pack.v.by_m("Xp", False)
                        if xp_member:
                            xp_member.v = str(create_xp)
                        else:
                            new_deck_pack.v.insert(1, f"Xp = {create_xp}")
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
    return new_command_unit_deck_packs


def _edit_existing_deck_packs(source_path: Any, deck_pack_edits: Dict[str, str]) -> None:
    """Apply precomputed deck pack modifications from database mappings."""
    
    existing_deck_pack_edits = deck_pack_edits["existing_deck_pack_edits"]
    modifications_applied = 0

    for deck_pack in source_path:
        if not hasattr(deck_pack, "namespace"):
            continue

        if not deck_pack.namespace.startswith("Descriptor_Deck_Pack_"):
            continue

        # Check if this deck pack has a precomputed modification
        if deck_pack.namespace in existing_deck_pack_edits:
            old_namespace = deck_pack.namespace
            new_namespace = existing_deck_pack_edits[old_namespace]

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
                    
                    # Check if transport changed by comparing old and new namespace parts
                    old_parts = old_namespace.split("_")
                    new_parts = new_namespace.split("_")
                    if len(old_parts) >= 4 and len(new_parts) >= 4:
                        # Extract unit_with_possible_transport from both namespaces
                        old_unit_with_transport = "_".join(old_parts[3:-2])
                        new_unit_with_transport = "_".join(new_parts[3:-2])
                        
                        # If they differ, the transport likely changed
                        if old_unit_with_transport != new_unit_with_transport:
                            # Get base unit name from Unit member to extract transport name
                            unit_member = deck_pack.v.by_m("Unit", False)
                            transport_member = deck_pack.v.by_m("Transport", False)
                            
                            if unit_member and transport_member:
                                # Extract unit name from Unit member: $/GFX/Unit/Descriptor_Unit_{unit_name}
                                unit_ref = unit_member.v
                                if "Descriptor_Unit_" in unit_ref:
                                    base_unit_name = unit_ref.split("Descriptor_Unit_")[-1]
                                    
                                    # Extract transport from new namespace
                                    if new_unit_with_transport.startswith(base_unit_name + "_"):
                                        new_transport_name = new_unit_with_transport[len(base_unit_name) + 1:]
                                        # Update Transport member
                                        new_transport_ref = f"$/GFX/Unit/Descriptor_Unit_{new_transport_name}"
                                        transport_member.v = new_transport_ref
                                        logger.info(f"Updated Transport member: {transport_member.v} -> {new_transport_ref}")
                                    elif old_unit_with_transport.startswith(base_unit_name + "_") and not new_unit_with_transport.startswith(base_unit_name + "_"):
                                        # Old had transport, new doesn't - remove transport
                                        old_transport_name = old_unit_with_transport[len(base_unit_name) + 1:]
                                        logger.info(f"Removing Transport member (transport removed: {old_transport_name})")
                                        deck_pack.v.remove_by_member("Transport")

                    modifications_applied += 1

                except (ValueError, IndexError) as e:
                    logger.warning(f"Failed to parse target XP from new namespace {new_namespace}: {e}")

    logger.info(f"Applied {modifications_applied} deck pack modifications")


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
        
        
def _find_best_target_xp(current_xp: int, available_xp_levels: list, missing_xp_levels: list) -> int:
    """Find the best target XP level for an existing pack that needs updating.

    Strategy:
    1. Prefer missing XP levels (levels that need new packs)
    2. Among missing levels, prefer the one closest to current_xp
    3. If current_xp > all available, use highest available
    4. If current_xp < all available, use lowest available
    """
    if not available_xp_levels:
        return None

    # If there are missing XP levels, prioritize them
    if missing_xp_levels:
        # Find the missing XP level closest to current_xp
        closest_missing = min(missing_xp_levels, key=lambda x: abs(x - current_xp))
        return closest_missing

    # No missing levels - this shouldn't happen in normal mapping, but handle gracefully
    # Find the available XP level closest to current_xp
    closest_available = min(available_xp_levels, key=lambda x: abs(x - current_xp))
    return closest_available
        
# Update deck pack references ------------------------------------------------------------
def edit_gen_gp_decks(source_path: Any, game_db: Dict[str, Any]) -> None:
    """GameData/Generated/Gameplay/Decks/Decks.ndf."""
    unit_edits = load_unit_edits()
    # unit_edits.update(supply_unit_edits)
    
    deck_pack_edits = _determine_deck_pack_edits(source_path, game_db, unit_edits)
    existing_deck_pack_edits = deck_pack_edits["existing_deck_pack_edits"]
    new_command_unit_deck_packs = deck_pack_edits["new_command_unit_deck_packs"]

    # Combine for reference lookup (both XP changes and unit name changes apply to references)
    all_reference_mappings = {}
    all_reference_mappings.update(existing_deck_pack_edits)
    all_reference_mappings.update(new_command_unit_deck_packs)

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
    
    # Add and remove deck pack references
    multi_deck_edits = load_deck_edits()
    for division, edits in multi_deck_edits.items():
        deck = source_path.by_n(f"Descriptor_Deck_{division}_multi")
        pack_list = deck.v.by_m("DeckPackList")
        if "remove" in edits:
            for pack in edits["remove"]:
                logger.info(f"Removing {pack} from {division}")
                pack_ref = pack_list.v.find_by_cond(lambda x: x.v == f"~/Descriptor_Deck_Pack_{pack}")
                pack_list.v.remove(pack_ref)
        if "add" in edits:
            for pack in edits["add"]:
                pack_list.v.add(f"~/Descriptor_Deck_Pack_{pack}")
        
    _hide_divisions_decks_ndf(source_path)


def _remove_deck_packs_from_multi_decks(source_path: Any) -> None:
    """Remove deck pack references from multi decks when units have 'remove' divisions."""
    logger.info("Processing deck pack removals from multi decks")

    # Load unit edits
    unit_edits = load_unit_edits()
    # unit_edits.update(supply_unit_edits)

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


def _hide_divisions_decks_ndf(source_path) -> None:
    """GameData/Generated/Gameplay/Decks/Decks.ndf
    Remove decks for hidden divisions in Decks.ndf"""
    logger.info("Removing decks for hidden divisions in Decks.ndf")

    config = ModConfig.get_instance()

    hide_divs = config.config_data.get("hide_divs", [])
    if config.config_data["build_config"]["write_dev"]:
        # In dev mode, remove divisions that should be shown for testing
        dev_show_divs = config.config_data.get("dev_show_divs", [])
        divs_to_hide = [div for div in hide_divs if div not in dev_show_divs]
    else:
        # In release mode, hide all divisions in hide_divs
        divs_to_hide = hide_divs

    indices_to_remove = []
    for division in divs_to_hide:
        deck_index = source_path.by_n(f"Descriptor_Deck_{division}").index
        indices_to_remove.append(deck_index)

    for index in sorted(indices_to_remove, reverse=True):
        source_path.remove(index)


def _new_deck_packs(source_path: Any) -> None:
    """Create new deck packs in DeckPacks.ndf"""
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


def edit_deck_pack_lists(source_path: Any) -> None:
    """GameData/Generated/Gameplay/Decks/Decks.ndf (POSSIBLY DEPRECATED)"""
    logger.info("Editing deck packs for new units")

    for donor, edits in NEW_UNITS.items():
        donor_name = donor[0]

        # Get base_vet from availability (index of first non-zero value)
        availability = edits.get("availability", None)
        base_vet = None
        if availability:
            for i, availability_ in enumerate(availability):
                if availability_ != 0:
                    base_vet = str(i)
                    break

        rename_donor_packs = edits.get("Decks", {}).get("packs", {}).get("rename", False)
        if rename_donor_packs:
            for deck_descr in source_path:
                deck_pack_list = deck_descr.v.by_m("DeckPackList")
                for deck_pack in deck_pack_list.v:
                    # Use regex to match deck pack descriptor pattern
                    # Pattern 1: ~/Descriptor_Deck_Pack_{donor_name}_{transport}_{base_vet}_{card_count}
                    # Pattern 2: ~/Descriptor_Deck_Pack_{donor_name}_{base_vet}_{card_count}
                    # Transport names can contain underscores, so we need to be careful about the pattern

                    # Try pattern with transport first
                    pattern_with_transport = rf"^~/Descriptor_Deck_Pack_{re.escape(donor_name)}_(.+?)_(\d+)_(\d+)$"
                    match = re.match(pattern_with_transport, deck_pack.v)

                    if match:
                        transport = match.group(1)
                        old_base_vet = match.group(2)
                        card_count = match.group(3)

                        logger.info(
                            f"Matched deck pack with transport: donor={donor_name}, transport={transport}, "
                            f"old_base_vet={old_base_vet}, card_count={card_count}"
                        )

                        # Use new base_vet if available, otherwise keep old one
                        new_base_vet = base_vet if base_vet else old_base_vet

                        # Construct new descriptor name with transport
                        new_descriptor = (
                            f"~/Descriptor_Deck_Pack_{edits['NewName']}_{transport}_{new_base_vet}_{card_count}"
                        )

                        logger.info(f"Renaming deck pack: {deck_pack.v} -> {new_descriptor}")
                        deck_pack.v = new_descriptor
                    else:
                        # Try pattern without transport
                        pattern_without_transport = rf"^~/Descriptor_Deck_Pack_{re.escape(donor_name)}_(\d+)_(\d+)$"
                        match = re.match(pattern_without_transport, deck_pack.v)

                        if match:
                            old_base_vet = match.group(1)
                            card_count = match.group(2)

                            logger.info(
                                f"Matched deck pack without transport: donor={donor_name}, "
                                f"old_base_vet={old_base_vet}, card_count={card_count}"
                            )

                            # Use new base_vet if available, otherwise keep old one
                            new_base_vet = base_vet if base_vet else old_base_vet

                            # Construct new descriptor name without transport
                            new_descriptor = f"~/Descriptor_Deck_Pack_{edits['NewName']}_{new_base_vet}_{card_count}"

                            logger.info(f"Renaming deck pack: {deck_pack.v} -> {new_descriptor}")
                            deck_pack.v = new_descriptor
            
            
        