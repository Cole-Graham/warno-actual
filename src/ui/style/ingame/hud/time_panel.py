"""Functions for modifying UI HUD time panel."""
from typing import Any

from src import ndf
from src.utils.logging_utils import setup_logger
from src.utils.ndf_utils import is_obj_type

logger = setup_logger(__name__)

def edit_uispecificingamehudtimepanelview(source_path) -> None:
    """Edit UISpecificInGameHUDTimePanelView.ndf.
    
    Args:
        source: NDF file containing HUD time panel definitions
    """
    logger.info("Editing UISpecificInGameHUDTimePanelView.ndf")
    
    # Update time and speed display
    _update_time_speed_display(source_path)
    
    # Update speed buttons
    _update_speed_buttons(source_path)

def _update_time_speed_display(source_path) -> None:
    """Update time and speed display properties."""
    affichagetempsetvitesseentexte = source_path.by_namespace("AffichageTempsEtVitesseEnTexte").v
    
    for element in affichagetempsetvitesseentexte.by_member("Elements").v:
        if not isinstance(element.v, ndf.model.Object) or not is_obj_type(element.v, "BUCKListElementDescriptor"):
            continue
            
        component_descr = element.v.by_member("ComponentDescriptor").v
        if component_descr.type != "BUCKTextDescriptor" or component_descr.by_member("ElementName", False) is None:
            continue
            
        elementname = component_descr.by_member("ElementName").v
        if elementname == '"NextActionTimeText"':
            component_descr.by_member("TextColor").v = '"AppleIIc"'
            component_descr.by_member("HorizontalFitStyle").v = "~/FitStyle/UserDefined"
        elif elementname == '"GameSpeedText"':
            component_descr.by_member("TextColor").v = '"M81_P3AmberOrange"'
    
    logger.debug("Updated time and speed display properties")

def _update_speed_buttons(source_path) -> None:
    """Update speed button properties."""
    timepanelspeedbuttons = source_path.by_namespace("TimePanelSpeedButtons").v
    timepanelspeedbuttons.insert(3, "FirstMargin = TRTTILength(Pixel = 10.0)")
    
    button_updates = {
        '"SpeedPauseButton"': {
            'BackgroundColorToken': '"Transparent"',
            'BorderLineColorToken': '"TimePanel/ButtonBorderM81Pause"',
            'TextureColorToken': '"BoutonTimePanelM81Pause"'
        },
        '"SpeedSlowButton"': {
            'BackgroundColorToken': '"Transparent"',
            'BorderLineColorToken': '"TimePanel/ButtonBorderM81Slow"',
            'BorderThickness': '"1"',
            'TextureColorToken': '"BoutonTimePanelM81Slow"',
            'BackgroundTexture': '"vitesse03"'
        },
        '"SpeedPlayButton"': {
            'BackgroundColorToken': '"BoutonTimePanelM81Play"',
            'BorderLineColorToken': '"TimePanel/ButtonBorderM81Play"',
            'BorderThickness': '"1"',
            'TextureColorToken': '"BoutonTimePanelM81Play"',
            'BackgroundTexture': '"vitesse02"',
            'DefaultToggleValue': 'true'
        },
        '"SpeedFastButton"': {
            'BackgroundColorToken': '"BoutonTimePanelM81Fast"',
            'BorderLineColorToken': '"TimePanel/ButtonBorderM81Fast"',
            'BorderThickness': '"1"',
            'TextureColorToken': '"BoutonTimePanelM81Fast"'
        },
        '"SpeedVeryFastButton"': {
            'BackgroundColorToken': '"BoutonTimePanelM81Fast"',
            'BorderLineColorToken': '"TimePanel/ButtonBorderM81Fast"',
            'BorderThickness': '"1"',
            'TextureColorToken': '"BoutonTimePanelM81Fast"'
        }
    }
    
    for element in timepanelspeedbuttons.by_member("Elements").v:
        if not isinstance(element.v, ndf.model.Object) or not is_obj_type(element.v, "BUCKListElementDescriptor"):
            continue
            
        component_descr = element.v.by_member("ComponentDescriptor").v
        if component_descr.by_member("ElementName", False) is None:
            continue
            
        elementname = component_descr.by_member("ElementName").v
        if elementname not in button_updates:
            continue
            
        _apply_button_updates(component_descr, elementname, button_updates[elementname])
    
    logger.debug("Updated speed button properties")

def _apply_button_updates(component: Any, elementname: str, updates: dict) -> None:
    """Apply updates to button component."""
    for key, value in updates.items():
        if key == 'BackgroundTexture':
            component.by_member(key).v = value
        else:
            component.add(f'{key} = {value}')
    
    if elementname == '"SpeedSlowButton"':
        componentframe = component.by_member("ComponentFrame").v
        componentframe.by_member("MagnifiableWidthHeight").v = "[GameSpeedPanelButtonWidth, 0.0]"
        componentframe.add("RelativeWidthHeight = [0.0, 1.0]")
    elif elementname == '"SpeedPlayButton"':
        componentframe = component.by_member("ComponentFrame").v
        componentframe.remove_by_member("RelativeWidthHeight")
        componentframe.by_member("MagnifiableWidthHeight").v = "[25.0, 25.0]" 