"""Functions for modifying UI HUD offmap airplane view."""
from typing import Any

from src import ndf
from src.utils.logging_utils import setup_logger
from src.utils.ndf_utils import is_obj_type

logger = setup_logger(__name__)

def edit_uispecificoffmapairplaneview(source_path) -> None:
    """Edit UISpecificOffMapAirplaneView.ndf."""
    logger.info("Editing UISpecificOffMapAirplaneView.ndf")
    
    # Update offmap airplane properties
    offmapairplaneviewdescriptor = source_path.by_namespace("OffMapAirplaneViewDescriptor").v
    
    # Update main component
    _update_main_component(source_path)
    
    # Update airplane XP display
    _update_airplane_xp(source_path)
    
    # Update status block
    _update_status_block(source_path)
    
    # Update unit name
    _update_unit_name(source_path)
    
    # Update state gauge
    _update_state_gauge(source_path)

def _update_main_component(source_path) -> None:
    """Update main component properties."""
    maincomponent = source_path.by_namespace("BUCKSpecificOffMapAirplaneMainComponentDescriptor").v
    maincomponent.by_member("BorderLineColorToken").v = '"BoutonTempsLineAirwingM81"'
    
    for component in maincomponent.by_member("Components").v:
        if not isinstance(component.v, ndf.model.Object) or not is_obj_type(component.v, "BUCKSpecificButton"):
            continue
            
        if component.v.by_member("ElementName", False) is None:
            continue
            
        if component.v.by_member("ElementName").v == "'SelectionButton'":
            _update_selection_button(component.v)
    
    logger.debug("Updated main component properties")

def _update_selection_button(button: Any) -> None:
    """Update selection button properties."""
    button.by_member("BorderLineColorToken").v = '"BoutonTempsLineAirwingM81"'
    button.by_member("BigBorderBackgroundColorToken").v = '"BoutonTempsLineAirwingM81"'
    button.by_member("TextColorToken").v = '"ButtonHUD/Text2AirwingM81"'
    button.insert(10, 'BorderThicknessToken = "2"')

def _update_airplane_xp(source_path) -> None:
    """Update airplane XP display properties."""
    airplanexp = source_path.by_namespace("AirplaneXP").v
    
    componentframe = airplanexp.by_member("ComponentFrame").v
    componentframe.by_member("AlignementToFather").v = "[0.0, 0.0]"
    componentframe.by_member("AlignementToAnchor").v = "[0.0, -3.83]"
    componentframe.by_member("MagnifiableOffset").v = "[0.0, 0.0]"
    
    airplanexp.by_member("BackgroundBlockColorToken").v = '"M81_DarkCharcoal"'
    logger.debug("Updated airplane XP display properties")

def _update_status_block(source_path) -> None:
    """Update status block properties."""
    blocnom_status_jauge = source_path.by_namespace("BlocNom_status_jauge").v
    blocnom_status_jauge.by_member("ComponentFrame").v.by_member("AlignementToFather").v = "[0.0, 0.2]"
    
    statusunite = source_path.by_namespace("StatusUnite").v
    statusunite.by_member("TypefaceToken").v = '"Bombardier"'
    statusunite.by_member("TextColor").v = '"M81_AppleIIc"'
    logger.debug("Updated status block properties")

def _update_unit_name(source_path) -> None:
    """Update unit name properties."""
    nomunite = source_path.by_namespace("NomUnite").v
    nomunite.insert(3, 'HasBorder = true')
    nomunite.by_member("BackgroundBlockColorToken").v = '"OffMapUnitButtonNameM81"'
    nomunite.insert(5, 'BorderLineColorToken = "OffMapUnitButtonNameM81"')
    logger.debug("Updated unit name properties")

def _update_state_gauge(source_path) -> None:
    """Update state gauge properties."""
    stategauge = source_path.by_namespace("StateGauge").v
    stategauge.by_member("BackgroundBlockColorToken").v = '"M81_DarkCharcoalTransparent"'
    
    for component in stategauge.by_member("Components").v:
        if not isinstance(component.v, ndf.model.Object) or not is_obj_type(component.v, "BUCKGaugeValueDescriptor"):
            continue
            
        component.v.by_member("BackgroundBlockColorToken").v = '"M81_AppleIIcTransparent"'
    
    logger.debug("Updated state gauge properties") 