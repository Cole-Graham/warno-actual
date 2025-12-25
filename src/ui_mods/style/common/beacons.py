"""Functions for modifying UI flare labels."""
# import csv
from typing import Any, List  # noqa

from src import ndf
from src.utils.dictionary_utils import write_dictionary_entries
from src.utils.logging_utils import setup_logger
from src.utils.ndf_utils import is_obj_type

logger = setup_logger(__name__)


def edit_uicommonbeaconlabelresources(source_path: Any) -> None:
    """Edit UICommonBeaconLabelResources.ndf."""
    logger.info("Editing UICommonBeaconLabelResources.ndf")
    
    # Update beacon text tokens
    _update_beacon_text_tokens(source_path)
    
    # Add new text entries
    _add_beacon_text_entries()
    
    # Update beacon label template
    _update_beacon_label_template(source_path)
    
    # Update beacon text template
    beacontext_template = source_path.by_namespace("BeaconLabelText").v
    beacontext_template.params.by_param("TypefaceToken").v = '"Eurostyle"'
    logger.debug("Updated beacon text typeface")


def _update_beacon_text_tokens(source_path) -> None:
    """Update beacon text tokens."""
    # Map of texture tokens to new text tokens
    token_map = {
        '"textureBeaconAttack"': '"ATKBEACON"',
        'textureBeaconDefense"': '"DEFBEACON"',
        '"textureBeaconHelp"': '"HELPBEACON"',
        '"textureBeaconFireSupport"': '"FIREBEACON"'
    }
    
    for row in source_path.by_namespace("CommonBeaconLabelResources").v:
        if not isinstance(row.v, ndf.model.Object):
            continue
            
        if not is_obj_type(row.v, "BeaconLabelDescriptor"):
            continue
            
        icon_texture_token = row.v.by_member("IconTextureToken").v
        if icon_texture_token in token_map:
            row.v.by_member("TextToken").v = token_map[icon_texture_token]
            logger.debug(f"Updated text token for {icon_texture_token}")


def _add_beacon_text_entries() -> None:
    """Add new text entries to dictionary."""
    new_entries = [
        ("ATKBEACON", "ATTACK!"),
        ("DEFBEACON", "DEFEND"),
        ("HELPBEACON", "HELP!"),
        ("FIREBEACON", "FIRE SUPPORT")
    ]
    
    write_dictionary_entries(new_entries, dictionary_type="ingame")


def _update_beacon_label_template(source_path) -> None:
    """Update beacon label template properties."""
    beacon_label_template = source_path.by_namespace("BeaconLabelDescriptor").v
    
    # Add margin parameter
    index = beacon_label_template.params.by_param("IconSize").index + 1
    beacon_label_template.params.insert(index, "Margin : float = 3.0")
    logger.debug("Added margin parameter to beacon label template")
    
    # Update element colors
    _update_element_colors(beacon_label_template)
    
    # Update foreground components
    _update_foreground_components(beacon_label_template)
    
    # Update background components
    _update_background_components(beacon_label_template)


def _update_element_colors(template: Any) -> None:
    """Update beacon label element colors."""
    for element in template.by_member("Elements").v:
        if not isinstance(element.v, ndf.model.Object):
            continue
            
        if not is_obj_type(element.v, "BUCKListElementDescriptor"):
            continue
            
        component_descr = element.v.by_member("ComponentDescriptor").v
        
        if component_descr.type == "BUCKTextureDescriptor":  # noqa
            component_descr.by_member("TextureColorToken").v = '"M81_VeryDarkCharcoal"'  # noqa
        elif component_descr.type == "BeaconLabelText":  # noqa
            component_descr.by_member("TextColor").v = '"M81_DarkCharcoal"'  # noqa
    
    logger.debug("Updated beacon label element colors")


def _update_foreground_components(template: Any) -> None:
    """Update beacon label foreground components."""
    for component in template.by_member("ForegroundComponents").v:
        if not isinstance(component.v, ndf.model.Object):
            continue
            
        if not is_obj_type(component.v, "BeaconLabelText"):
            continue
            
        component.v.by_member("BackgroundBlockColorToken").v = '"M81_DarkCharcoalTransparent"'
    
    logger.debug("Updated beacon label foreground colors")


def _update_background_components(template: Any) -> None:
    """Update beacon label background components."""
    for component in template.by_member("BackgroundComponents").v:
        if not isinstance(component.v, ndf.model.Object):
            continue
            
        if not is_obj_type(component.v, "PanelRoundedCorner"):
            continue
            
        component.v.add("HasBorder = true")
        component.v.add('BackgroundBlockColorToken = "M81_ArtichokeVeryLight62"')
        component.v.add('BorderLineColorToken = "M81_VeryDarkCharcoal"')
    
    logger.debug("Updated beacon label background properties")
