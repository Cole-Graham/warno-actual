"""Functions for modifying UI HUD offmap airplane view."""
# from typing import Any

from src import ndf
from src.utils.logging_utils import setup_logger
from src.utils.ndf_utils import is_obj_type

logger = setup_logger(__name__)


def edit_uispecificoffmapairplaneview(source_path) -> None:
    """Edit UISpecificOffMapAirplaneView.ndf."""
    logger.info("Editing UISpecificOffMapAirplaneView.ndf")
    
    # Update main component
    maincomponent = source_path.by_namespace("BUCKSpecificOffMapAirplaneMainComponentDescriptor").v
    maincomponent.by_member("BorderLineColorToken").v = '"BoutonTempsLineAirwingM81"'
    
    for component in maincomponent.by_member("Components").v:
        if not isinstance(component.v, ndf.model.Object):
            continue
        if is_obj_type(component.v, "BUCKSpecificButton"):
            if component.v.by_member("ElementName", False) is not None:
                elementname = component.v.by_member("ElementName").v
                if elementname == "'SelectionButton'":
                    component.v.by_member("BorderLineColorToken").v = '"BoutonTempsLineAirwingM81"'
                    component.v.by_member("BigBorderBackgroundColorToken").v = '"BoutonTempsLineAirwingM81"'
                    component.v.by_member("TextColorToken").v = '"ButtonHUD/Text2AirwingM81"'
                    component.v.insert(10, 'BorderThicknessToken = "2"')
    
    # Update airplane XP display
    airplanexp = source_path.by_namespace("AirplaneXP").v
    componentframe = airplanexp.by_member("ComponentFrame").v
    componentframe.by_member("AlignementToFather").v = "[0.0, 0.0]"
    componentframe.by_member("AlignementToAnchor").v = "[0.0, -3.83]"
    componentframe.by_member("MagnifiableOffset").v = "[0.0, 0.0]"
    airplanexp.by_member("BackgroundBlockColorToken").v = '"M81_DarkCharcoal"'
    
    # Update status block
    blocnom_status_jauge = source_path.by_namespace("BlocNom_status_jauge").v
    componentframe = blocnom_status_jauge.by_member("ComponentFrame").v
    componentframe.by_member("AlignementToFather").v = "[0.0, 0.2]"
    
    statusunite = source_path.by_namespace("StatusUnite").v
    statusunite.by_member("TypefaceToken").v = '"Bombardier"'
    statusunite.by_member("TextColor").v = '"M81_AppleIIc"'
    
    # Update unit name
    nomunite = source_path.by_namespace("NomUnite").v
    nomunite.insert(3, 'HasBorder = true')
    nomunite.by_member("BackgroundBlockColorToken").v = '"OffMapUnitButtonNameM81"'
    nomunite.insert(5, 'BorderLineColorToken = "OffMapUnitButtonNameM81"')
    
    # Update state gauge
    stategauge = source_path.by_namespace("StateGauge").v
    stategauge.by_member("BackgroundBlockColorToken").v = '"M81_DarkCharcoalTransparent"'
    for component in stategauge.by_member("Components").v:
        if not isinstance(component.v, ndf.model.Object):
            continue
        if is_obj_type(component.v, "BUCKGaugeValueDescriptor"):
            component.v.by_member("BackgroundBlockColorToken").v = '"M81_AppleIIcTransparent"'
    
    logger.debug("Updated offmap airplane view properties")
