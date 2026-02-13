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

    wa_entries_obj = source_path.by_n("wa_entries")
    if not wa_entries_obj:
        logger.error("Could not find wa_entries object")
        return

    wa_division_ids_map = wa_entries_obj.v.by_member("DivisionIds")
    added = 0

    # Collect divisions with valid cfg_name and division_id, then sort by division_id
    to_add = []
    for div_key, div_data in new_divisions.items():
        cfg_name = div_data.get("cfg_name")
        if not cfg_name:
            logger.warning(f"No cfg_name specified for {div_key}, skipping")
            continue
        division_id = div_data.get("division_id")
        if division_id is None:
            logger.warning(f"division_id missing for {div_key}, skipping")
            continue
        to_add.append((div_key, div_data))

    for div_key, div_data in sorted(to_add, key=lambda x: x[1]["division_id"]):
        cfg_name = div_data["cfg_name"]
        division_id = div_data["division_id"]
        # Division namespace format: Descriptor_Deck_Division_{cfg_name}_multi
        division_namespace = f"Descriptor_Deck_Division_{cfg_name}_multi"

        logger.info(f"Adding division to DivisionIds map: {division_namespace} with ID {division_id}")
        wa_division_ids_map.v.add((division_namespace, str(division_id)))
        added += 1

    logger.info(f"Added {added} new divisions to DivisionIds map")


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