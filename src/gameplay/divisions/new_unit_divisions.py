"""Functions for adding new units to divisions."""

from typing import Any, Dict

from src import ndf
from src.constants.new_units import NEW_UNITS
from src.utils.logging_utils import setup_logger
from src.utils.ndf_utils import _generate_guid

logger = setup_logger(__name__)

def add_division_rules(source_path: Any) -> None:
    """Add unit rules to DivisionRules.ndf."""
    logger.info("Adding unit rules to divisions")
    
    for donor, edits in NEW_UNITS.items():
        if "NewName" not in edits or "Divisions" not in edits:
            continue
            
        unit_name = edits["NewName"]
        division_rules_map = source_path.by_n("DivisionRules").v.by_member("DivisionRules").v
        
        for division, div_data in edits["Divisions"].items():
            key = f"~/Descriptor_Deck_Division_{division}"
            transports = div_data.get("Transports")
            
            # Create transport list if available
            if transports:
                transport_list = [f"$/GFX/Unit/Descriptor_Unit_{t}" for t in transports]
                transport_str = f"[{', '.join(transport_list)}]"
            
            xp_multi_str = str(edits["XPMultiplier"])
            
            # Different entries for vehicles vs infantry/towed
            if edits["is_ground_vehicle"] and not edits["is_infantry"]:
                new_entry = (
                    f'TDeckUniteRule\n'
                    f'(\n'
                    f'    UnitDescriptor = $/GFX/Unit/Descriptor_Unit_{unit_name}\n'
                    f'    AvailableWithoutTransport = True\n'
                    f'    NumberOfUnitInPack = {edits["Availability"]}\n'
                    f'    NumberOfUnitInPackXPMultiplier = {xp_multi_str}\n'
                    f'),'
                )
            else:
                new_entry = (
                    f'TDeckUniteRule\n'
                    f'(\n'
                    f'    UnitDescriptor = $/GFX/Unit/Descriptor_Unit_{unit_name}\n'
                    f'    AvailableWithoutTransport = False\n'
                    f'    AvailableTransportList = {transport_str}\n'
                    f'    NumberOfUnitInPack = {edits["Availability"]}\n'
                    f'    NumberOfUnitInPackXPMultiplier = {xp_multi_str}\n'
                    f'),'
                )
            
            # Add to division rules
            deck_content = division_rules_map.by_key(key).v
            deck_content.by_m("UnitRuleList").v.add(new_entry)
            logger.info(f"Added rules for {unit_name} to {division}")
            
            # Handle unit replacements
            if edits.get("is_replacement", False):
                for i, unit_rule in enumerate(deck_content.by_m("UnitRuleList").v, start=0):
                    if unit_rule.v.by_m("UnitDescriptor").v == f"$/GFX/Unit/Descriptor_Unit_{donor}":
                        deck_content.by_m("UnitRuleList").v.remove(i)
                        logger.info(f"Removed old entry for {donor} from {division}")

def add_to_divisions(source_path: Any) -> None:
    """Add units to Divisions.ndf."""
    logger.info("Adding units to division packs")
    
    for donor, edits in NEW_UNITS.items():
        if "NewName" not in edits or "Divisions" not in edits:
            continue
            
        unit_name = edits["NewName"]
        
        for division in edits["Divisions"]:
            namespace = f"Descriptor_Deck_Division_{division}"
            pack_list = source_path.by_n(namespace).v.by_member("PackList").v
            
            # Get card count for this division
            cards = edits["Cards"].get(division, edits["Cards"]["default"])
            
            new_entry = f"(~/Descriptor_Deck_Pack_{unit_name}, {cards}),"
            pack_list.add(new_entry)
            logger.info(f"Added {unit_name} to division {division}")

def create_deck_pack_descriptors(source_path: Any) -> None:
    """Create deck pack descriptors in DeckPacks.ndf."""
    logger.info("Creating deck pack descriptors")
    
    for donor, edits in NEW_UNITS.items():
        if "NewName" not in edits:
            continue
            
        unit_name = edits["NewName"]
        
        # Handle XP multipliers
        xp_values = edits.get("XPMultiplier", [1.0, 1.0, 1.0, 1.0])
        xp_str = f"[{', '.join(str(x) for x in xp_values)}]"
        
        # Different descriptor type for vehicles
        if edits.get("is_ground_vehicle", False):
            descriptor_line = f"    VehicleDescriptor = ~/Descriptor_Unit_{unit_name}"
        else:
            descriptor_line = f"    UnitDescriptor = ~/Descriptor_Unit_{unit_name}"
        
        deck_pack = (
            f'Descriptor_Deck_Pack_{unit_name} is DeckPackDescriptor\n'
            f'(\n'
            f'    Unit = $/GFX/Unit/Descriptor_Unit_{unit_name}\n'
            f')\n'
        )
        source_path.add(deck_pack)
        logger.info(f"Created deck pack descriptor for {unit_name}")

def update_deck_serializer(source_path: Any) -> None:
    """Update DeckSerializer.ndf for new units."""
    logger.info("Updating DeckSerializer.ndf for new units")
    
    for donor, edits in NEW_UNITS.items():
        if "NewName" not in edits:
            continue
        
        unit_name = edits["NewName"]
        deckserializer_obj = source_path.by_n("DeckSerializer")
        unit_ids_map = deckserializer_obj.v.by_member("UnitIds").v
        last_row = unit_ids_map[-1]
        last_row_str = str(last_row)
        last_row_int = int(last_row_str.split("value='")[-1].split("'")[0])
        last_row_integer = str(last_row_int + 1)
        logger.info(f"DeckSerializer.ndf) Adding new entry: $/GFX/Unit/Descriptor_Unit_{unit_name}")
        unit_ids_map.add(("$/GFX/Unit/Descriptor_Unit_" + unit_name, last_row_integer))
        
def create_division_packs(source_path: Any) -> None:
    """Create division packs in DivisionPacks.ndf."""
    logger.info("Creating division packs")
    
    for donor, edits in NEW_UNITS.items():
        if "NewName" not in edits:
            continue
        
        unit_name = edits["NewName"]
        new_entry = (
            f'Descriptor_Deck_Pack_{unit_name} is DeckPackDescriptor\n'
            f'(\n'
            f'    Unit = $/GFX/Unit/Descriptor_Unit_{unit_name}\n'
            f')\n'
        )
        source_path.add(new_entry)
        logger.info(f"Created division pack for {unit_name}")
