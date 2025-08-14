"""Functions for modifying UI flare labels."""
# import csv
from typing import Any, List  # noqa

from src import ndf
from src.utils.dictionary_utils import write_dictionary_entries
from src.utils.logging_utils import setup_logger
from src.utils.ndf_utils import is_obj_type

logger = setup_logger(__name__)


def edit_uicommonflarelabelresources(source_path: Any) -> None:
    """Edit UICommonFlareLabelResources.ndf."""
    logger.info("Editing UICommonFlareLabelResources.ndf")
    
    # Update flare text tokens
    _update_flare_text_tokens(source_path)
    
    # Add new text entries
    _add_flare_text_entries()
    
    # Update flare label template
    _update_flare_label_template(source_path)
    
    # Update flare text template
    flaretext_template = source_path.by_namespace("FlareLabelText").v
    flaretext_template.params.by_param("TypefaceToken").v = '"Eurostyle"'
    logger.debug("Updated flare text typeface")


def _update_flare_text_tokens(source_path) -> None:
    """Update flare text tokens."""
    # Map of texture tokens to new text tokens
    token_map = {
        '"textureFlareAttack"': '"ATKFLARE"',
        'textureFlareDefense"': '"DEFNDFLARE"',
        '"textureFlareHelp"': '"HALPMEEE"',
        '"textureFlareFireSupport"': '"FIREFLARE"'
    }
    
    for row in source_path.by_namespace("CommonFlareLabelResources").v:
        if not isinstance(row.v, ndf.model.Object):
            continue
            
        if not is_obj_type(row.v, "FlareLabelDescriptor"):
            continue
            
        icon_texture_token = row.v.by_member("IconTextureToken").v
        if icon_texture_token in token_map:
            row.v.by_member("TextToken").v = token_map[icon_texture_token]
            logger.debug(f"Updated text token for {icon_texture_token}")


def _add_flare_text_entries() -> None:
    """Add new text entries to dictionary."""
    new_entries = [
        ("ATKFLARE", "ATTACK!"),
        ("DEFNDFLARE", "DEFEND"),
        ("HALPMEEE", "HELP!"),
        ("FIREFLARE", "FIRE SUPPORT")
    ]
    
    write_dictionary_entries(new_entries, dictionary_type="ingame")


def _update_flare_label_template(source_path) -> None:
    """Update flare label template properties."""
    flare_label_template = source_path.by_namespace("FlareLabelDescriptor").v
    
    # Add margin parameter
    index = flare_label_template.params.by_param("IconSize").index + 1
    flare_label_template.params.insert(index, "Margin : float = 3.0")
    logger.debug("Added margin parameter to flare label template")
    
    # Update element colors
    _update_element_colors(flare_label_template)
    
    # Update foreground components
    _update_foreground_components(flare_label_template)
    
    # Update background components
    _update_background_components(flare_label_template)


def _update_element_colors(template: Any) -> None:
    """Update flare label element colors."""
    for element in template.by_member("Elements").v:
        if not isinstance(element.v, ndf.model.Object):
            continue
            
        if not is_obj_type(element.v, "BUCKListElementDescriptor"):
            continue
            
        component_descr = element.v.by_member("ComponentDescriptor").v
        
        if component_descr.type == "BUCKTextureDescriptor":  # noqa
            component_descr.by_member("TextureColorToken").v = '"M81_VeryDarkCharcoal"'  # noqa
        elif component_descr.type == "FlareLabelText":  # noqa
            component_descr.by_member("TextColor").v = '"M81_DarkCharcoal"'  # noqa
    
    logger.debug("Updated flare label element colors")


def _update_foreground_components(template: Any) -> None:
    """Update flare label foreground components."""
    for component in template.by_member("ForegroundComponents").v:
        if not isinstance(component.v, ndf.model.Object):
            continue
            
        if not is_obj_type(component.v, "FlareLabelText"):
            continue
            
        component.v.by_member("BackgroundBlockColorToken").v = '"M81_DarkCharcoalTransparent"'
    
    logger.debug("Updated flare label foreground colors")


def _update_background_components(template: Any) -> None:
    """Update flare label background components."""
    for component in template.by_member("BackgroundComponents").v:
        if not isinstance(component.v, ndf.model.Object):
            continue
            
        if not is_obj_type(component.v, "PanelRoundedCorner"):
            continue
            
        component.v.add("HasBorder = true")
        component.v.add('BackgroundBlockColorToken = "M81_ArtichokeVeryLight62"')
        component.v.add('BorderLineColorToken = "M81_VeryDarkCharcoal"')
    
    logger.debug("Updated flare label background properties")
