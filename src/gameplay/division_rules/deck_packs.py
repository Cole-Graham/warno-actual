"""Functions for modifying deck packs and their references."""

from typing import Any, Dict, List, Tuple

from src import ndf
from src.constants.unit_edits import load_unit_edits
from src.constants.unit_edits.SUPPLY_unit_edits import supply_unit_edits
from src.data import decks
from src.utils.logging_utils import setup_logger
from src.utils.ndf_utils import is_obj_type

logger = setup_logger(__name__)

def modify_deck_packs(source_path: Any, game_db: Dict[str, Any]) -> None:
    """Modify deck packs in DeckPacks.ndf"""
    logger.info("Modifying deck packs")

    unit_edits = load_unit_edits()
    unit_edits.update(supply_unit_edits)
    deck_data = game_db["decks"]["multi"]  # Get multi deck data

    for unit, edits in unit_edits.items():
        if "Divisions" in edits or "XPMultiplier" in edits:
            _handle_deck_packs(source_path, unit, edits, deck_data)

def _remove_duplicate_deck_packs(source_path: Any) -> None:
    """Remove duplicate deck packs from source_path."""
    seen_namespaces = {}
    for deck_pack in source_path:
        if deck_pack.namespace in seen_namespaces:
            source_path.remove(deck_pack)
        else:
            seen_namespaces[deck_pack.namespace] = deck_pack

def _handle_deck_packs(
    source_path: Any,
    unit: str,
    edits: Dict[str, Any],
    deck_data: Dict[str, Any]
) -> None:
    """Handle modifying deck packs."""
    # First find all deck packs for this unit that exist in deck_data
    deck_packs_in_use = set()
    for div_data in deck_data.values():
        for pack in div_data["packs"]:
            if pack.startswith(f"Descriptor_Deck_Pack_{unit}"):
                deck_packs_in_use.add(pack)

    # Group deck packs by base name (without XP/cards suffix), but only those in use
    deck_pack_groups = {}
    for deck_pack in source_path:
        if deck_pack.namespace in deck_packs_in_use:
            base_name = "_".join(deck_pack.n.split("_")[:-2])
            if base_name not in deck_pack_groups:
                deck_pack_groups[base_name] = []
            deck_pack_groups[base_name].append(deck_pack)

    # Process each group of deck packs
    for base_name, deck_packs in deck_pack_groups.items():
        # Get XP value from first pack
        current_xp = int(deck_packs[0].n.split("_")[-2])
        
        # Get new XP value if specified
        xp_list = edits.get("XPMultiplier", None)
        new_xp = None
        if xp_list and current_xp < len(xp_list) and xp_list[current_xp] in (0, None):
            # Only update XP if current_xp matches index of 0/None in xp_list
            new_xp = next((i for i, x in enumerate(xp_list) if x not in (0, None)), None)
        else:
            if xp_list and not xp_list[current_xp] in (0, None):
                logger.info(f"No XP multiplier specified for {unit} {current_xp}")
        updated_xp = new_xp if new_xp is not None else current_xp

        # Track namespaces we've already seen to detect duplicates
        seen_namespaces = {}

        # Update each deck pack in the group
        for deck_pack in deck_packs:
            current_cards = int(deck_pack.n.split("_")[-1])
            has_xp = deck_pack.v.by_m("Xp", False) is not None

            # Find divisions containing this specific deck pack
            division_names = []
            for div_name, div_data in deck_data.items():
                if deck_pack.namespace in div_data["packs"]:
                    division_names.append(div_name)

            # Get card count - use first non-None value from:
            # 1. Division-specific values (checking all divisions that have the pack)
            # 2. Default value
            new_cards = None
            for div_name in division_names:
                new_cards = edits.get("Divisions", {}).get(div_name, {}).get("cards", None)
                if new_cards is not None:
                    break

            if new_cards is None:
                new_cards = edits.get("Divisions", {}).get("default", {}).get("cards", None)

            # Only update cards if new_cards is lower than current
            updated_cards = min(current_cards, new_cards) if new_cards is not None else current_cards

            # Only update namespace and values if either XP or cards changed
            if updated_xp != current_xp or updated_cards != current_cards:
                new_namespace = f"{base_name}_{updated_xp}_{updated_cards}"
                logger.info(f"Updating {deck_pack.namespace} to {new_namespace}")
                deck_pack.n = new_namespace
                
                # Update XP value if it changed
                if updated_xp != current_xp:
                    if updated_xp > 0:
                        if has_xp:
                            deck_pack.v.by_m("Xp").v = updated_xp
                        else:
                            deck_pack.v.insert(1, f"Xp = {updated_xp}")
                    elif has_xp:
                        # Remove Xp member if it exists and new value is 0
                        deck_pack.v.remove_by_member("Xp")

                # Update card count if it changed
                if updated_cards != current_cards:
                    deck_pack.v.by_m("Number").v = updated_cards
                    
    _remove_duplicate_deck_packs(source_path)

def update_deck_pack_references(source_path: Any, game_db: Dict[str, Any]) -> None:
    """Update deck pack references in Decks.ndf."""
    logger.info("Updating deck pack references")
    
    unit_edits = load_unit_edits()
    unit_edits.update(supply_unit_edits)
    deck_data = game_db["decks"]["multi"]  # Get multi deck data
    
    # Track namespace changes for non-multi decks
    namespace_changes = {}  # old_namespace -> new_namespace
    
    # Process each unit in unit_edits
    for unit, edits in unit_edits.items():
        # Get list of divisions to remove this unit from
        divisions_to_remove = set(edits.get("Divisions", {}).get("remove", []))
        if divisions_to_remove:
            logger.info(f"Will remove {unit} from divisions: {divisions_to_remove}")
        
        # Pre-process divisions that contain this unit's deck packs
        unit_divisions = {}
        for div_name, div_data in deck_data.items():
            for pack in div_data["packs"]:
                if pack.startswith(f"Descriptor_Deck_Pack_{unit}"):
                    if pack not in unit_divisions:
                        unit_divisions[pack] = []
                    unit_divisions[pack].append(div_name)
                    
        # Skip if no divisions contain this unit
        if not unit_divisions and not divisions_to_remove:
            continue
            
        # Get new XP value if specified
        xp_list = edits.get("XPMultiplier", None)
        new_xp = None
        if xp_list:
            new_xp = next((i for i, x in enumerate(xp_list) if x not in (0, None)), None)
        
        # Cache division card counts
        div_cards = {}
        default_cards = edits.get("Divisions", {}).get("default", {}).get("cards", None)
        for div_name in {div for divs in unit_divisions.values() for div in divs}:
            div_cards[div_name] = edits.get("Divisions", {}).get(div_name, {}).get("cards", default_cards)
        
        # Update references in each division's deck
        for deck_obj in source_path:
            if not (deck_obj.namespace.startswith("Descriptor_Deck_") and
                   deck_obj.namespace.endswith("_multi")):
                continue
                
            div_name = deck_obj.namespace.split("Descriptor_Deck_")[1].split("_multi")[0]
            deck_pack_list = deck_obj.v.by_m("DeckPackList").v
            
            # Handle removals first
            if div_name in divisions_to_remove:
                # Remove all deck packs for this unit
                packs_to_remove = []
                for i, pack_ref in enumerate(deck_pack_list):
                    if pack_ref.v.startswith(f"~/Descriptor_Deck_Pack_{unit}"):
                        packs_to_remove.append(i)
                        logger.info(f"Removing {pack_ref.v} from {div_name}")
                
                # Remove packs in reverse order to maintain correct indices
                for i in reversed(packs_to_remove):
                    deck_pack_list.remove(i)
                continue
            
            # Skip if division doesn't have any packs to update
            if div_name not in div_cards:
                continue
                
            # Update remaining references
            for pack_ref in deck_pack_list:
                if not pack_ref.v.startswith(f"~/Descriptor_Deck_Pack_{unit}"):
                    continue
                    
                # Parse current values
                base_name = "_".join(pack_ref.v.split("_")[:-2])
                current_xp = int(pack_ref.v.split("_")[-2])
                current_cards = int(pack_ref.v.split("_")[-1])
                
                # Get updated values
                updated_xp = current_xp
                if xp_list and current_xp < len(xp_list) and xp_list[current_xp] in (0, None):
                    updated_xp = new_xp if new_xp is not None else current_xp
                else:
                    if xp_list and not xp_list[current_xp] in (0, None):
                        logger.info(f"No XP multiplier specified for {unit} {current_xp}")
                
                # Only update cards if new value is lower
                updated_cards = current_cards
                if div_cards[div_name] is not None:
                    updated_cards = min(current_cards, div_cards[div_name])
                
                # Update reference with new values if either XP or cards changed
                if updated_xp != current_xp or updated_cards != current_cards:
                    old_ref = pack_ref.v
                    new_ref = f"{base_name}_{updated_xp}_{updated_cards}"
                    logger.info(f"Updating {old_ref} to {new_ref}")
                    pack_ref.v = new_ref
                    
                    # Track namespace change
                    namespace_changes[old_ref.replace("~/", "")] = new_ref.replace("~/", "")
    
    def _update_non_multi_decks(source_path: Any, namespace_changes: Dict[str, str]) -> None:
        """Update deck pack references in non-multi decks."""
        for deck_obj in source_path:
            if not (deck_obj.namespace.startswith("Descriptor_Deck_") and 
                   not deck_obj.namespace.endswith("_multi")):
                continue
                
            deck_pack_list = deck_obj.v.by_m("DeckPackList").v
            
            for pack_ref in deck_pack_list:
                old_ref = pack_ref.v.replace("~/", "")
                if old_ref in namespace_changes:
                    new_ref = f"~/{namespace_changes[old_ref]}"
                    logger.info(f"Updating non-multi deck reference {pack_ref.v} to {new_ref}")
                    pack_ref.v = new_ref
    
    # Update non-multi decks
    _update_non_multi_decks(source_path, namespace_changes)
        
def new_deck_packs(source_path: Any) -> None:
    """Create new deck packs in DeckPacks.ndf."""
    logger.info("Creating new deck packs")

    # Create new deck pack for 8th Infantry Division (temp until we create constants for editing decks)
    new_deck_pack = (
        'Descriptor_Deck_Pack_8th_M1A1_Abrams_US_1_1 is DeckPackDescriptor'
        '('
        '    Xp = 1'
        '    Unit = $/GFX/Unit/Descriptor_Unit_8th_M1A1_Abrams_US\n'
        '    Number = 1'
        ')'
    )
    source_path.add(new_deck_pack)
    
