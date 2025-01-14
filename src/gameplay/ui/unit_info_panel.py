"""Functions for modifying UI info panels."""

from typing import List, Tuple

from src import ModConfig
from src.dics.ui.unit_info_panel import UNIT_INFO_PANEL_DATA
from src.utils.dictionary_utils import write_dictionary_entries
from src.utils.logging_utils import setup_logger
from src.utils.ndf_utils import is_obj_type

logger = setup_logger(__name__)


def write_info_panel_hints() -> None:
    """Write info panel hint texts to dictionary file."""
    config = ModConfig.get_instance().config_data
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
    
    write_dictionary_entries(entries, config)


def edit_unit_info_panel(source) -> None:
    """Edit unit info panel in UISpecificUnitInfoPanelView.ndf."""
    logger.info("Modifying unit info panel")
    
    for descr_row in source:
        if not is_obj_type(descr_row.v, "TUISpecificUnitInfoPanelViewDescriptor"):
            continue
            
        for root_obj, data in UNIT_INFO_PANEL_DATA.items():
            if root_obj == "AttributeDescriptorsPool" and "AttributeStrength" in data:
                attribute_descrs_map = descr_row.v.by_m("AttributeDescriptorsPool").v
                strength_elements_obj = attribute_descrs_map.by_k('"AttributeStrength"').v
                
                if "hint" in data["AttributeStrength"]:
                    new_token = f"{data['AttributeStrength']['token']}B"
                    strength_elements_obj.by_m("HintToken").v = f'"{new_token}"'
                    logger.info(f"Updated Strength hint token to {new_token}") 