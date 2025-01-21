"""Functions for modifying UI HUD time panel."""
from typing import Any

from src import ndf
from src.utils.logging_utils import setup_logger
from src.utils.ndf_utils import is_obj_type

logger = setup_logger(__name__)

def edit_uispecificingamehudtimepanelview(source_path) -> None:
    """Edit UISpecificInGameHUDTimePanelView.ndf."""
    logger.info("Editing UISpecificInGameHUDTimePanelView.ndf")
    
    # Update time and speed display
    affichagetempsetvitesseentexte = source_path.by_namespace("AffichageTempsEtVitesseEnTexte").v
    for element in affichagetempsetvitesseentexte.by_member("Elements").v:
        if not isinstance(element.v, ndf.model.Object):
            continue
        if is_obj_type(element.v, "BUCKListElementDescriptor"):
            component_descr = element.v.by_member("ComponentDescriptor").v
            if component_descr.type == "BUCKTextDescriptor":
                if component_descr.by_member("ElementName", False) is not None:
                    elementname = component_descr.by_member("ElementName").v
                    if elementname == '"NextActionTimeText"':
                        component_descr.by_member("TextColor").v = '"AppleIIc"'
                        component_descr.by_member("HorizontalFitStyle").v = "~/FitStyle/UserDefined"
                    if elementname == '"GameSpeedText"':
                        component_descr.by_member("TextColor").v = '"M81_P3AmberOrange"'
    
    # Update speed buttons
    timepanelspeedbuttons = source_path.by_namespace("TimePanelSpeedButtons").v
    timepanelspeedbuttons.insert(3, "FirstMargin = TRTTILength(Pixel = 10.0)")
    
    for element in timepanelspeedbuttons.by_member("Elements").v:
        if not isinstance(element.v, ndf.model.Object):
            continue
        if is_obj_type(element.v, "BUCKListElementDescriptor"):
            component_descr = element.v.by_member("ComponentDescriptor").v
            if component_descr.by_member("ElementName", False) is not None:
                elementname = component_descr.by_member("ElementName").v
                
                if elementname == '"SpeedPauseButton"':
                    component_descr.by_member("BackgroundColorToken").v = '"Transparent"'
                    component_descr.by_member("BorderLineColorToken").v = '"TimePanel/ButtonBorderM81Pause"'
                    component_descr.add('TextureColorToken = "BoutonTimePanelM81Pause"')
                
                elif elementname == '"SpeedSlowButton"':
                    componentframe = component_descr.by_member("ComponentFrame").v
                    componentframe.by_member("MagnifiableWidthHeight").v = "[GameSpeedPanelButtonWidth, 0.0]"
                    componentframe.add("RelativeWidthHeight = [0.0, 1.0]")
                    component_descr.add('BackgroundColorToken = "Transparent"')
                    component_descr.add('BorderLineColorToken = "TimePanel/ButtonBorderM81Slow"')
                    component_descr.add('BorderThickness = "1"')
                    component_descr.add('TextureColorToken = "BoutonTimePanelM81Slow"')
                    component_descr.by_member("BackgroundTexture").v = '"vitesse03"'
                
                elif elementname == '"SpeedPlayButton"':
                    componentframe = component_descr.by_member("ComponentFrame").v
                    componentframe.remove_by_member("RelativeWidthHeight")
                    componentframe.by_member("MagnifiableWidthHeight").v = "[25.0, 25.0]"
                    component_descr.add('BackgroundColorToken = "BoutonTimePanelM81Play"')
                    component_descr.add('DefaultToggleValue = true')
                    component_descr.add('BorderLineColorToken = "TimePanel/ButtonBorderM81Play"')
                    component_descr.add('BorderThickness = "1"')
                    component_descr.add('TextureColorToken = "BoutonTimePanelM81Play"')
                    component_descr.by_member("BackgroundTexture").v = '"vitesse02"'
                
                elif elementname == '"SpeedFastButton"':
                    component_descr.add('BackgroundColorToken = "BoutonTimePanelM81Fast"')
                    component_descr.add('BorderLineColorToken = "TimePanel/ButtonBorderM81Fast"')
                    component_descr.add('BorderThickness = "1"')
                    component_descr.add('TextureColorToken = "BoutonTimePanelM81Fast"')
                
                elif elementname == '"SpeedVeryFastButton"':
                    component_descr.add('BackgroundColorToken = "BoutonTimePanelM81Fast"')
                    component_descr.add('BorderLineColorToken = "TimePanel/ButtonBorderM81Fast"')
                    component_descr.add('BorderThickness = "1"')
                    component_descr.add('TextureColorToken = "BoutonTimePanelM81Fast"')
    
    logger.debug("Updated time panel properties") 