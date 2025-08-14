"""Functions for modifying UI info panels."""

from typing import List, Tuple

from src.dics.ui.unit_info_panel import UNIT_INFO_PANEL_DATA
from src.utils.dictionary_utils import write_dictionary_entries
from src.utils.logging_utils import setup_logger
from src.utils.ndf_utils import find_obj_by_type

logger = setup_logger(__name__)


def edit_ui_ingame_uispecificunitinfopanelview(source_path) -> None:
    """GameData/UserInterface/Use/InGame/UISpecificUnitInfoPanelView.ndf"""
    logger.info("Modifying unit info panel")

    unit_infopanel = find_obj_by_type(source_path, "TUISpecificUnitInfoPanelViewDescriptor")

    for root_obj, data in UNIT_INFO_PANEL_DATA.items():
        if root_obj == "AttributeDescriptorsPool" and "AttributeStrength" in data:
            attribute_descrs_map = unit_infopanel.v.by_m("AttributeDescriptorsPool").v
            strength_elements_obj = attribute_descrs_map.by_k('"AttributeStrength"').v

            if "hint" in data["AttributeStrength"]:
                new_token = f"{data['AttributeStrength']['token']}"
                strength_elements_obj.by_m("HintToken").v = f'"{new_token}"'
                logger.info(f"Updated Strength hint token to {new_token}")

    _write_info_panel_hints()


def _write_info_panel_hints() -> None:
    """Write info panel hint texts to dictionary file."""
    # config = ModConfig.get_instance().config_data
    entries: List[Tuple[str, str]] = []

    for root_obj, data in UNIT_INFO_PANEL_DATA.items():
        for attr, attr_data in data.items():
            if "token" not in attr_data:
                continue

            base_token = attr_data["token"]

            # Add body hint
            if "hint" in attr_data:
                entries.append((f"{base_token}B", attr_data["hint"]))

            # Add extended hint
            if "extended" in attr_data:
                entries.append((f"{base_token}E", attr_data["extended"]))

    write_dictionary_entries(entries, dictionary_type="ingame")
