"""Functions for adding new units to divisions."""

from typing import Any

from src import ndf
from src.constants.new_units import NEW_UNITS
from src.utils.logging_utils import setup_logger
# from src.utils.ndf_utils import generate_guid

logger = setup_logger(__name__)


def add_division_rules(source_path: Any) -> None:
    """Add unit rules to DivisionRules.ndf."""
    logger.info("Adding unit rules to divisions")
    
    for donor, edits in NEW_UNITS.items():
        if "NewName" not in edits or "Divisions" not in edits:
            continue
            
        unit_name = edits["NewName"]

        for division, div_data in edits["Divisions"].items():
            if division == "default":
                continue
            
            division_obj_namespace = f"Descriptor_Deck_Division_{division}_Rule"
            transports = div_data.get("Transports")
            
            # Create transport list if available
            if transports:
                transport_list = [f"$/GFX/Unit/Descriptor_Unit_{t}" for t in transports]
                transport_str = f"[{', '.join(transport_list)}]"

            base_avail = max(edits["availability"])
            xp_multi = str([i / base_avail for i in edits["availability"]])

            default_cards = edits["Divisions"]["default"]["cards"]
            cards = div_data.get("cards", default_cards)

            # Different entries for vehicles vs infantry/towed
            if edits.get("is_ground_vehicle", False) and not edits.get("is_infantry", False):
                new_entry = (
                    f'TDeckUniteRule\n'
                    f'(\n'
                    f'    UnitDescriptor = $/GFX/Unit/Descriptor_Unit_{unit_name}\n'
                    f'    AvailableWithoutTransport = True\n'
                    f'    MaxPackNumber = {cards}\n'
                    f'    NumberOfUnitInPack = {base_avail}\n'
                    f'    NumberOfUnitInPackXPMultiplier = {xp_multi}\n'
                    f'),'
                )
            else:
                new_entry = (
                    f'TDeckUniteRule\n'
                    f'(\n'
                    f'    UnitDescriptor = $/GFX/Unit/Descriptor_Unit_{unit_name}\n'
                    f'    AvailableWithoutTransport = False\n'
                    f'    AvailableTransportList = {transport_str}\n'  # noqa
                    f'    MaxPackNumber = {cards}\n'
                    f'    NumberOfUnitInPack = {base_avail}\n'
                    f'    NumberOfUnitInPackXPMultiplier = {xp_multi}\n'
                    f'),'
                )
            
            # Add to division rules
            div_rules = source_path.by_n(division_obj_namespace).v.by_m("UnitRuleList")
            div_rules.v.add(new_entry)
            logger.info(f"Added rules for {unit_name} to {division}")

            # Handle unit replacements
            if edits.get("is_replacement", False):
                for i, unit_rule in enumerate(div_rules.v, start=0):
                    if unit_rule.v.by_m("UnitDescriptor").v == f"$/GFX/Unit/Descriptor_Unit_{donor}":
                        div_rules.v.remove(i)
                        logger.info(f"Removed old entry for {donor} from {division}")


def add_to_divisions(source_path: Any) -> None:  # don't need anymore
    """Add units to Divisions.ndf."""
    logger.info("Adding units to division packs")
    
    for donor, edits in NEW_UNITS.items():
        if "NewName" not in edits or "Divisions" not in edits:
            continue
            
        unit_name = edits["NewName"]
        
        for division in edits["Divisions"]:
            if division == "default":
                continue
            namespace = f"Descriptor_Deck_Division_{division}"
            pack_list = source_path.by_n(namespace).v.by_member("PackList").v
            
            # Get card count for this division
            cards = edits["Divisions"][division].get("cards",
                                           edits["Divisions"]["default"]["cards"])
            
            new_entry = f"(~/Descriptor_Deck_Pack_{unit_name}, {cards}),"
            pack_list.add(new_entry)
            logger.info(f"Added {unit_name} to division {division}")


def create_deck_pack_descriptors(source_path: Any) -> None:  # not used currently
    """Create deck pack descriptors in DeckPacks.ndf."""
    logger.info("Creating deck pack descriptors")
    
    for donor, edits in NEW_UNITS.items():
        if "NewName" not in edits:
            continue
            
        unit_name = edits["NewName"]
        
        # Handle XP multipliers - unused
        # xp_values = edits.get("XPMultiplier", [1.0, 1.0, 1.0, 1.0])
        # xp_str = f"[{', '.join(str(x) for x in xp_values)}]"
        
        # Different descriptor type for vehicles
        if edits.get("is_ground_vehicle", False):
            descriptor_line = f"    VehicleDescriptor = ~/Descriptor_Unit_{unit_name}"  # noqa
        else:
            descriptor_line = f"    UnitDescriptor = ~/Descriptor_Unit_{unit_name}"  # noqa
        
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
    
    # create Warno Actual TDeckSerializerEntries object
    serializer_entries = (
        'wa_entries is TDeckSerializerEntries'
        '('
        '    DivisionIds = MAP[]'
        '    UnitIds = MAP[]'
        ')'
    )
    ndf_serializer_entries = ndf.convert(serializer_entries)
    source_path.add(ndf_serializer_entries)
    logger.info("Created Warno Actual TDeckSerializerEntries object")

    vanilla_serializer = source_path.find_by_cond(lambda serializer_obj: serializer_obj.index == 0)
    unit_ids_map = vanilla_serializer.v.by_member("UnitIds")
    last_row = unit_ids_map.v[-1]
    last_row_str = str(last_row)
    last_row_int = int(last_row_str.split("value='")[-1].split("'")[0])
    
    new_unit_id = last_row_int + 1        
    for donor, edits in NEW_UNITS.items():
        if "NewName" not in edits:
            continue
        
        unit_name = edits["NewName"]
        deckserializer_obj = source_path.by_n("wa_entries")
        unit_ids_map = deckserializer_obj.v.by_member("UnitIds")
        logger.info(f"DeckSerializer.ndf) Adding new entry: $/GFX/Unit/Descriptor_Unit_{unit_name}")
        unit_ids_map.v.add(("$/GFX/Unit/Descriptor_Unit_" + unit_name, str(new_unit_id)))
        new_unit_id += 1


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
