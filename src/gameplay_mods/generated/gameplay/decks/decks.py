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
    logger.info("Modifying deck packs using precomputed constants mappings")
    
    # Load precomputed deck pack mappings from constants_precomputation
    precomputed_mappings = game_db.get("deck_pack_mappings", {})
    deck_pack_modifications = precomputed_mappings.get("deck_pack_modifications", {})
    reference_mappings = precomputed_mappings.get("reference_mappings", {})
    new_command_unit_deck_packs_data = precomputed_mappings.get("new_command_unit_deck_packs", {})
    
    if not deck_pack_modifications:
        logger.warning("No precomputed deck pack modifications found in game_db")
    
    logger.info(
        f"Using {len(deck_pack_modifications)} precomputed deck pack modifications and "
        f"{len(new_command_unit_deck_packs_data)} precomputed new command unit deck packs"
    )

    # IMPORTANT: Create new command unit deck packs FIRST before modifying existing ones
    new_command_unit_mappings = _create_new_command_unit_deck_packs(source_path, new_command_unit_deck_packs_data)
    
    # Combine precomputed modifications with new command unit mappings
    # Structure expected by _edit_existing_deck_packs
    deck_pack_edits = {
        "existing_deck_pack_edits": deck_pack_modifications,
        "new_command_unit_deck_packs": new_command_unit_mappings,
    }

    # Apply ONLY deck pack modifications (never unit name changes)
    _edit_existing_deck_packs(source_path, deck_pack_edits)

    # Clean up any duplicate deck packs that may have been created
    _remove_duplicate_deck_packs(source_path)
    
    # TODO: Needs proper implementation
    _new_deck_packs(source_path)
    
    
def _create_new_command_unit_deck_packs(source_path: Any, precomputed_new_deck_packs: Dict[str, Dict[str, Any]]) -> Dict[str, str]:
    """Create new deck packs for new command units using precomputed data.
    
    Args:
        source_path: DeckPacks.ndf file (should only contain DeckPackDescriptor entries)
        precomputed_new_deck_packs: Precomputed data from constants_precomputation
            Format: {
                "new_namespace": {
                    "donor_template": "donor_namespace",
                    "new_unit_name": "unit_name",
                    "xp": xp_level,
                    "number": number
                }
            }
    
    Returns:
        Dictionary mapping donor namespaces to new namespaces (for reference updates)
    """
    new_command_unit_mappings = {}
    command_units_created = 0

    if not precomputed_new_deck_packs:
        logger.debug("No precomputed new command unit deck packs found")
        return new_command_unit_mappings

    # Build a map of donor template namespaces to actual deck pack objects
    donor_templates = {}  # namespace -> deck_pack
    
    # Iterate through source_path (DeckPacks.ndf) to find donor templates
    for deck_pack in source_path:
        # Only process DeckPackDescriptor entries
        if not hasattr(deck_pack, "namespace"):
            continue
        if not deck_pack.namespace.startswith("Descriptor_Deck_Pack_"):
            continue
        
        # Check if this is a donor template we need
        if deck_pack.namespace in [data["donor_template"] for data in precomputed_new_deck_packs.values()]:
            donor_templates[deck_pack.namespace] = deck_pack

    # Create new deck packs based on precomputed data
    for new_namespace, pack_data in precomputed_new_deck_packs.items():
        donor_template_namespace = pack_data["donor_template"]
        new_unit_name = pack_data["new_unit_name"]
        create_xp = pack_data["xp"]
        number = pack_data["number"]

        # Find the donor template
        if donor_template_namespace not in donor_templates:
            logger.warning(f"Donor template {donor_template_namespace} not found in DeckPacks.ndf")
            continue

        template_pack = donor_templates[donor_template_namespace]

        logger.info(f"Creating new deck pack {new_namespace} from template {donor_template_namespace}")

        # Clone the template pack
        new_deck_pack = template_pack.copy()
        new_deck_pack.namespace = new_namespace
        new_deck_pack.n = new_namespace

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

        # Add the new deck pack to source_path (DeckPacks.ndf)
        source_path.add(new_deck_pack)
        command_units_created += 1

        # Build mapping for reference updates (donor -> new unit)
        # Use the first new namespace created from this donor as the mapping target
        if donor_template_namespace not in new_command_unit_mappings:
            new_command_unit_mappings[donor_template_namespace] = new_namespace

    logger.info(f"Created {command_units_created} new command unit deck packs")
    return new_command_unit_mappings


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
                    target_number = int(parts[-1])

                    logger.info(f"Applying modification: {old_namespace} -> {new_namespace}")

                    # Update the deck pack namespace
                    deck_pack.namespace = new_namespace

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
                    
                    # Update Number member
                    number_member = deck_pack.v.by_m("Number", False)
                    if number_member:
                        number_member.v = str(target_number)
                    else:
                        logger.warning(f"Number member not found in {deck_pack.namespace}")
                    
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
    # Load precomputed deck pack mappings from constants_precomputation
    precomputed_mappings = game_db.get("deck_pack_mappings", {})
    deck_pack_modifications = precomputed_mappings.get("deck_pack_modifications", {})
    reference_mappings = precomputed_mappings.get("reference_mappings", {})

    # Combine for reference lookup (both XP changes and unit name changes apply to references)
    # Use precomputed modifications and reference mappings
    all_reference_mappings = {}
    all_reference_mappings.update(deck_pack_modifications)  # XP/number changes
    all_reference_mappings.update(reference_mappings)  # Donor -> new unit references (already includes new command units)

    logger.info(
        f"Updating deck pack references using {len(deck_pack_modifications)} modifications and "
        f"{len(reference_mappings)} reference mappings"
    )

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
        
        # Skip deck modifications for divsions that are removed from the game
        config = ModConfig.get_instance()
        hide_divs = config.config_data.get("hide_divs", [])
        write_dev = config.config_data["build_config"]["write_dev"]
        dev_show_divs = config.config_data.get("dev_show_divs") or []
        if not write_dev and f"{division}_multi" in hide_divs:
            continue
        if write_dev and division not in dev_show_divs and f"{division}_multi" in hide_divs:
            continue
        
        deck = source_path.by_n(f"Descriptor_Deck_{division}_multi")
        pack_list = deck.v.by_m("DeckPackList")
        if "remove" in edits:
            for pack in edits["remove"]:
                logger.info(f"Removing {pack} from {division}")
                pack_ref = pack_list.v.find_by_cond(lambda x: x.v == f"~/Descriptor_Deck_Pack_{pack}", False)
                if pack_ref:
                    pack_list.v.remove(pack_ref)
                else:
                    logger.warning(f"(edit_gen_gp_decks) Pack {pack} not found in {division}")
        if "add" in edits:
            for pack in edits["add"]:
                pack_list.v.add(f"~/Descriptor_Deck_Pack_{pack}")
        
    _hide_divisions_decks_ndf(source_path)


def _remove_deck_packs_from_multi_decks(source_path: Any) -> None:
    """Remove deck pack references from multi decks when units have 'remove' divisions or card limits."""
    logger.info("Processing deck pack removals and limits from multi decks")

    # Load unit edits
    unit_edits = load_unit_edits()
    # unit_edits.update(supply_unit_edits)

    removals_processed = 0
    limits_processed = 0

    # First pass: Handle "remove" divisions (complete removal)
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

    # Second pass: Handle card limits (limit number of deck packs per division)
    # Process all multi decks and limit deck packs based on card limits
    for deck_obj in source_path:
        if not hasattr(deck_obj, "namespace") or not deck_obj.namespace.endswith("_multi"):
            continue

        # Extract division name from multi deck namespace: Descriptor_Deck_{division}_multi
        division_name = deck_obj.namespace.replace("Descriptor_Deck_", "").replace("_multi", "")

        # Get the DeckPackList
        deck_pack_list = deck_obj.v.by_m("DeckPackList")
        if not deck_pack_list:
            continue

        # Helper function to get card limit from divisions config
        def get_card_limit(divisions_config: Dict[str, Any], div_name: str) -> int:
            """Get card limit for a division from divisions config."""
            if not isinstance(divisions_config, dict):
                return None
            
            # Check division-specific first
            if div_name in divisions_config:
                div_config = divisions_config[div_name]
                if isinstance(div_config, dict) and "cards" in div_config:
                    return div_config["cards"]
            
            # Fall back to default
            if "default" in divisions_config:
                default_config = divisions_config["default"]
                if isinstance(default_config, dict) and "cards" in default_config:
                    return default_config["cards"]
            
            return None

        # Check unit_edits for card limits
        for unit_name, edits in unit_edits.items():
            if "Divisions" not in edits:
                continue

            card_limit = get_card_limit(edits["Divisions"], division_name)
            if card_limit is None:
                continue

            # Find all deck pack references for this unit in this multi deck
            unit_pack_refs = []
            for pack_ref in deck_pack_list.v:
                ref_value = pack_ref.v.replace("~/", "")
                if ref_value.startswith(f"Descriptor_Deck_Pack_{unit_name}_"):
                    unit_pack_refs.append(pack_ref)

            # If we have more references than allowed, remove the excess
            if len(unit_pack_refs) > card_limit:
                pack_refs_to_remove = unit_pack_refs[card_limit:]  # Keep first N, remove the rest
                
                for pack_ref in pack_refs_to_remove:
                    logger.info(
                        f"Limiting {unit_name} in {division_name}: removing {pack_ref.v} "
                        f"(limit: {card_limit}, found: {len(unit_pack_refs)})"
                    )
                    deck_pack_list.v.remove(pack_ref)
                    limits_processed += 1

        # Check NEW_UNITS for card limits
        for donor, edits in NEW_UNITS.items():
            if "NewName" not in edits or "Divisions" not in edits:
                continue

            new_unit_name = edits["NewName"]
            card_limit = get_card_limit(edits["Divisions"], division_name)
            if card_limit is None:
                continue

            # Find all deck pack references for this new unit in this multi deck
            unit_pack_refs = []
            for pack_ref in deck_pack_list.v:
                ref_value = pack_ref.v.replace("~/", "")
                if ref_value.startswith(f"Descriptor_Deck_Pack_{new_unit_name}_"):
                    unit_pack_refs.append(pack_ref)

            # If we have more references than allowed, remove the excess
            if len(unit_pack_refs) > card_limit:
                pack_refs_to_remove = unit_pack_refs[card_limit:]  # Keep first N, remove the rest
                
                for pack_ref in pack_refs_to_remove:
                    logger.info(
                        f"Limiting {new_unit_name} in {division_name}: removing {pack_ref.v} "
                        f"(limit: {card_limit}, found: {len(unit_pack_refs)})"
                    )
                    deck_pack_list.v.remove(pack_ref)
                    limits_processed += 1

    # Third pass: Handle transport restrictions (remove packs with disallowed transports)
    transport_removals_processed = 0
    
    # Process all multi decks and remove deck packs with disallowed transports
    for deck_obj in source_path:
        if not hasattr(deck_obj, "namespace") or not deck_obj.namespace.endswith("_multi"):
            continue

        # Extract division name from multi deck namespace: Descriptor_Deck_{division}_multi
        division_name = deck_obj.namespace.replace("Descriptor_Deck_", "").replace("_multi", "")

        # Get the DeckPackList
        deck_pack_list = deck_obj.v.by_m("DeckPackList")
        if not deck_pack_list:
            continue

        # Helper function to get allowed transports from divisions config
        def get_allowed_transports(divisions_config: Dict[str, Any], div_name: str) -> list:
            """Get allowed transports for a division from divisions config."""
            if not isinstance(divisions_config, dict):
                return None
            
            # Check division-specific first
            if div_name in divisions_config:
                div_config = divisions_config[div_name]
                if isinstance(div_config, dict) and "Transports" in div_config:
                    transports = div_config["Transports"]
                    # Handle None (no transports allowed)
                    if transports is None:
                        return []
                    return transports
            
            # Fall back to default
            if "default" in divisions_config:
                default_config = divisions_config["default"]
                if isinstance(default_config, dict) and "Transports" in default_config:
                    transports = default_config["Transports"]
                    # Handle None (no transports allowed)
                    if transports is None:
                        return []
                    return transports
            
            return None

        # Helper function to process transport restrictions for a unit
        def process_transport_restrictions(unit_name: str, allowed_transports: list) -> None:
            """Process transport restrictions for a unit."""
            nonlocal transport_removals_processed
            
            if allowed_transports is None:
                return

            # Convert to set for easier lookup
            allowed_transports_set = set(allowed_transports)

            # Find all deck pack references for this unit in this multi deck
            pack_refs_to_remove = []
            for pack_ref in deck_pack_list.v:
                ref_value = pack_ref.v.replace("~/", "")
                
                # Check if this reference is for the unit we're checking
                if not ref_value.startswith(f"Descriptor_Deck_Pack_{unit_name}_"):
                    continue

                # Parse the namespace to extract transport name
                # Format: Descriptor_Deck_Pack_{unit_name}_{transport?}_{xp}_{number}
                parts = ref_value.split("_")
                if len(parts) < 4:
                    continue

                try:
                    # Extract unit_with_possible_transport (everything between prefix and XP)
                    unit_with_possible_transport = "_".join(parts[3:-2])
                    
                    # Check if this is a transport variant (starts with unit_name + "_")
                    if unit_with_possible_transport.startswith(unit_name + "_"):
                        # Extract transport name (everything after unit_name + "_")
                        transport_name = unit_with_possible_transport[len(unit_name) + 1:]
                        
                        # Check if transport is not in allowed list
                        if transport_name not in allowed_transports_set:
                            pack_refs_to_remove.append(pack_ref)
                            logger.info(
                                f"Removing {unit_name} pack with disallowed transport '{transport_name}' "
                                f"from {division_name}: {ref_value}"
                            )
                    # If it's a simple pack (no transport), it's allowed (simple packs don't have transports)
                    # So we don't add it to removal list
                except (ValueError, IndexError):
                    continue

            # Remove the identified references
            for pack_ref in pack_refs_to_remove:
                deck_pack_list.v.remove(pack_ref)
                transport_removals_processed += 1

        # Check unit_edits for transport restrictions
        for unit_name, edits in unit_edits.items():
            if "Divisions" not in edits:
                continue

            allowed_transports = get_allowed_transports(edits["Divisions"], division_name)
            process_transport_restrictions(unit_name, allowed_transports)

        # Check NEW_UNITS for transport restrictions
        for donor, edits in NEW_UNITS.items():
            if "NewName" not in edits or "Divisions" not in edits:
                continue

            new_unit_name = edits["NewName"]
            # TODO: New units dictionary has inconsistent formatting for division names (includes "multi" suffix)
            # This will get more complicated in the future when we specify edits for challenge and army general divs 
            allowed_transports = get_allowed_transports(edits["Divisions"], f"{division_name}_multi")
            process_transport_restrictions(new_unit_name, allowed_transports)

    logger.info(
        f"Processed {removals_processed} deck pack removals, {limits_processed} deck pack limits, "
        f"and {transport_removals_processed} transport restriction removals from multi decks"
    )


def _hide_divisions_decks_ndf(source_path) -> None:
    """GameData/Generated/Gameplay/Decks/Decks.ndf
    Remove decks for hidden divisions in Decks.ndf"""
    logger.info("Removing decks for hidden divisions in Decks.ndf")

    config = ModConfig.get_instance()

    # hide_divs = config.config_data.get("hide_divs", [])
    # if config.config_data["build_config"]["write_dev"]:
    #     # In dev mode, remove divisions that should be shown for testing
    #     dev_show_divs = config.config_data.get("dev_show_divs", [])
    #     divs_to_hide = [div for div in hide_divs if div not in dev_show_divs]
    # else:
    #     # In release mode, hide all divisions in hide_divs
    #     divs_to_hide = hide_divs

    # indices_to_remove = []
    # for division in divs_to_hide:
    #     deck_index = source_path.by_n(f"Descriptor_Deck_{division}").index
    #     indices_to_remove.append(deck_index)
    
    indices_to_remove = []
    for deck_descr in source_path:
        if deck_descr.n.endswith("_multi") or deck_descr.n.endswith("_Gruppierung"):
            indices_to_remove.append(deck_descr.index)

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
            
            
        