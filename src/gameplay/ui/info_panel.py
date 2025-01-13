"""Functions for modifying UI info panels."""

from src.utils.logging_utils import setup_logger

logger = setup_logger(__name__)

# UI panel modification data
UNIT_INFO_PANEL_DATA = {
    "AttributeDescriptorsPool": {
        "AttributeStrength": {
            "token": "STRENGTH_HINT_TOKEN",  # Replace with actual token
            "hint": True
        }
    }
}


def edit_unit_info_panel(source) -> None:
    """Edit unit info panel in UISpecificUnitInfoPanelView.ndf."""
    logger.info("Modifying unit info panel")
    
    for descr_row in source:
        if not hasattr(descr_row.v, 'type'):
            continue
            
        if descr_row.v.type != "TUISpecificUnitInfoPanelViewDescriptor":
            continue
            
        for root_obj, data in UNIT_INFO_PANEL_DATA.items():
            if root_obj == "AttributeDescriptorsPool" and "AttributeStrength" in data:
                attribute_descrs_map = descr_row.v.by_m("AttributeDescriptorsPool").v
                strength_elements_obj = attribute_descrs_map.by_k('"AttributeStrength"').v
                
                if "hint" in data["AttributeStrength"]:
                    new_token = data["AttributeStrength"]["token"]
                    strength_elements_obj.by_m("HintToken").v = f'"{new_token}"'
                    logger.info(f"Updated Strength hint token to {new_token}") 