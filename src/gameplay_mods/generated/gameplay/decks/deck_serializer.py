import re
from typing import Any

from src.constants.generated.gameplay.decks import load_new_divisions
from src.constants.new_units import NEW_UNITS
from src.utils.logging_utils import setup_logger
from src import ModConfig, ndf

logger = setup_logger(__name__)


def edit_gen_gp_decks_deckserializer(source_path: Any) -> None:
    """GameData/Generated/Gameplay/Decks/DeckSerializer.ndf"""
    _update_deck_serializer(source_path)
    _add_new_divisions_to_serializer(source_path)
    _hide_divisions_deckserializer_ndf(source_path)

def _update_deck_serializer(source_path: Any) -> None:
    """Update DeckSerializer.ndf for new units."""
    logger.info("Updating DeckSerializer.ndf for new units")

    # create Warno Actual TDeckSerializerEntries object
    serializer_entries = "wa_entries is TDeckSerializerEntries" "(" "    DivisionIds = MAP[]" "    UnitIds = MAP[]" ")"
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


def _add_new_divisions_to_serializer(source_path: Any) -> None:
    """Add new national divisions to DivisionIds map in wa_entries."""
    new_divisions = load_new_divisions()
    
    if not new_divisions:
        logger.info("No new divisions to add to DivisionIds map")
        return
    
    logger.info("Adding new divisions to DivisionIds map")
    
    # Get vanilla serializer to find the last division ID
    vanilla_serializer = source_path.find_by_cond(lambda serializer_obj: serializer_obj.index == 0)
    if not vanilla_serializer:
        logger.error("Could not find vanilla serializer object")
        return
    
    division_ids_map = vanilla_serializer.v.by_member("DivisionIds")
    if not division_ids_map or not division_ids_map.v:
        logger.error("Could not find DivisionIds map in vanilla serializer")
        return
    
    # Get the last division ID from vanilla serializer
    last_row = division_ids_map.v[-1]
    last_row_str = str(last_row)
    # Extract the ID value from the last row
    # Format is typically something like: ListRow[0](value='Descriptor_Deck_Division_...', ...) ListRow[1](value='123', ...)
    # The ID is the second element (value) in the tuple
    try:
        # Try to extract ID using the same method as UnitIds
        # Get the last occurrence of value='...' which should be the ID
        last_row_int = int(last_row_str.split("value='")[-1].split("'")[0])
    except (ValueError, IndexError):
        # Try alternative parsing if the format uses double quotes or different structure
        try:
            # Look for numeric value in the string (handle both single and double quotes)
            matches = re.findall(r"value=['\"](\d+)['\"]", last_row_str)
            if matches:
                last_row_int = int(matches[-1])  # Get the last match (should be the ID)
            else:
                logger.error(f"Could not parse last division ID from: {last_row_str}")
                return
        except Exception as e:
            logger.error(f"Failed to parse last division ID: {e}")
            return
    
    # Start new division IDs from last_id + 1
    new_division_id = last_row_int + 1
    
    # Get wa_entries object
    wa_entries_obj = source_path.by_n("wa_entries")
    if not wa_entries_obj:
        logger.error("Could not find wa_entries object")
        return
    
    wa_division_ids_map = wa_entries_obj.v.by_member("DivisionIds")
    
    # Add each new division to the DivisionIds map
    for div_key, div_data in new_divisions.items():
        cfg_name = div_data.get("cfg_name")
        if not cfg_name:
            logger.warning(f"No cfg_name specified for {div_key}, skipping")
            continue
        
        # Division namespace format: Descriptor_Deck_Division_{cfg_name}_multi
        division_namespace = f"Descriptor_Deck_Division_{cfg_name}_multi"
        
        logger.info(f"Adding division to DivisionIds map: {division_namespace} with ID {new_division_id}")
        wa_division_ids_map.v.add((division_namespace, str(new_division_id)))
        new_division_id += 1
    
    logger.info(f"Added {len(new_divisions)} new divisions to DivisionIds map")


def _hide_divisions_deckserializer_ndf(source_path) -> None:
    """GameData/Generated/Gameplay/Decks/DecksSerializer.ndf
    Remove division map rows in DecksSerializer.ndf for hidden divisions."""
    logger.info("Removing division map rows for hidden divisions in DecksSerializer.ndf")

    config = ModConfig.get_instance()

    hide_divs = config.config_data.get("hide_divs", [])
    if config.config_data["build_config"]["write_dev"]:
        # In dev mode, remove divisions that should be shown for testing
        dev_show_divs = config.config_data.get("dev_show_divs", [])
        divs_to_hide = [div for div in hide_divs if div not in dev_show_divs]
    else:
        # In release mode, hide all divisions in hide_divs
        divs_to_hide = hide_divs

    vanilla_serializer = source_path.find_by_cond(lambda serializer_obj: serializer_obj.index == 0)
    division_ids_map = vanilla_serializer.v.by_member("DivisionIds")
    for division in divs_to_hide:
        division_ids_map.v.remove_by_key(f"Descriptor_Deck_Division_{division}")