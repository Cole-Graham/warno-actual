from typing import Any

from src.constants.generated.gameplay.decks import divs_not_released
from src.constants.new_units import NEW_UNITS
from src.utils.logging_utils import setup_logger
from src import ModConfig, ndf

logger = setup_logger(__name__)


def edit_gen_gp_decks_deckserializer(source_path: Any) -> None:
    """GameData/Generated/Gameplay/Decks/DeckSerializer.ndf"""
    _update_deck_serializer(source_path)
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


def _hide_divisions_deckserializer_ndf(source_path) -> None:
    """GameData/Generated/Gameplay/Decks/DecksSerializer.ndf
    Remove division map rows in DecksSerializer.ndf for hidden divisions."""
    logger.info("Removing division map rows for hidden divisions in DecksSerializer.ndf")

    config = ModConfig.get_instance()

    divs_to_hide = (
        divs_not_released if not config.config_data["build_config"]["write_dev"] else config.config_data["hide_divs"]
    )

    vanilla_serializer = source_path.find_by_cond(lambda serializer_obj: serializer_obj.index == 0)
    division_ids_map = vanilla_serializer.v.by_member("DivisionIds")
    for division in divs_to_hide:
        division_ids_map.v.remove_by_key(f"Descriptor_Deck_Division_{division}")