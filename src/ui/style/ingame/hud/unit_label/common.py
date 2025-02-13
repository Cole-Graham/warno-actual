"""Functions for modifying UI HUD unit label common components."""
# from src import ndf
from src.utils.logging_utils import setup_logger

logger = setup_logger(__name__)


def edit_uispecificunitlabelcommon(source_path) -> None:
    """Edit UISpecificUnitLabelCommon.ndf.
    
    Args:
        source_path: NDF file containing HUD unit label common definitions
    """
    logger.info("Editing UISpecificUnitLabelCommon.ndf")
    
    # Update reticle size
    source_path.by_namespace("ReticleMagnifiableSize").v = "4.0"
    logger.debug("Updated reticle size")
    
    # Update upper name and unit count
    _update_upper_name_and_unit_count(source_path)
    
    # Update carried name and unit count
    _update_carried_name_and_unit_count(source_path)
    
    # Update leaving district chrono
    _update_leaving_district_chrono(source_path)
    
    # Update carried unit name list
    _update_carried_unit_name_list(source_path)
    
    # Update current unit label upper list
    _update_current_unit_label_upper_list(source_path)


def _update_upper_name_and_unit_count(source_path) -> None:
    """Update upper name and unit count properties."""
    uppernameandunitcountdescription = source_path.by_namespace("UpperNameAndUnitCountDescription").v
    uppernameandunitcountdescription.by_member("TypefaceToken").v = '"Bombardier"'
    uppernameandunitcountdescription.by_member("UnitInfoVPadding").v = "TRTTILength2(Magnifiable = [6.0, 6.0])"
    uppernameandunitcountdescription.by_member("UnitNameHPadding").v = "TRTTILength2(Magnifiable = [6.0, 6.0])"
    uppernameandunitcountdescription.by_member("UnitNumberHPadding").v = "TRTTILength2(Magnifiable = [4.0, 4.0])"
    logger.debug("Updated upper name and unit count properties")


def _update_carried_name_and_unit_count(source_path) -> None:
    """Update carried name and unit count properties."""
    carriednameandunitcountdescription = source_path.by_namespace("CarriedNameAndUnitCountDescription").v
    carriednameandunitcountdescription.by_member("TypefaceToken").v = '"Bombardier"'
    carriednameandunitcountdescription.by_member("UnitInfoVPadding").v = "TRTTILength2(Magnifiable = [4.0, 4.0])"
    carriednameandunitcountdescription.by_member("UnitNameHPadding").v = "TRTTILength2(Magnifiable = [6.0, 6.0])"
    carriednameandunitcountdescription.by_member("UnitNumberHPadding").v = "TRTTILength2(Magnifiable = [4.0, 4.0])"
    logger.debug("Updated carried name and unit count properties")


def _update_leaving_district_chrono(source_path) -> None:
    """Update leaving district chrono properties."""
    leavingdistrictchronodescription = source_path.by_namespace("LeavingDistrictChronoDescription").v
    leavingdistrictchronodescription.by_member("ChronoForegroundColor").v = '"M81_AppleIIc"'
    logger.debug("Updated leaving district chrono color")


def _update_carried_unit_name_list(source_path) -> None:
    """Update carried unit name list properties."""
    carriedunitnamelist_template = source_path.by_namespace("CarriedUnitNameList").v
    componentframe_param = carriedunitnamelist_template.params.by_param("ComponentFrame").v
    componentframe_param.add("MagnifiableOffset = [0.0, 0.0]")
    logger.debug("Updated carried unit name list offset")


def _update_current_unit_label_upper_list(source_path) -> None:
    """Update current unit label upper list properties."""
    currentunitlabelupperlist_template = source_path.by_namespace("CurrentUnitLabelUpperList").v
    
    # Update frame
    componentframe_param = currentunitlabelupperlist_template.params.by_param("ComponentFrame").v
    componentframe_param.add("MagnifiableOffset = [0.0, 0.0]")
    
    # Add border properties
    currentunitlabelupperlist_template.insert(5, 'HasBorder = true')
    currentunitlabelupperlist_template.insert(6, 'BorderThicknessToken = "2"')
    currentunitlabelupperlist_template.insert(7, 'BordersToDraw = ~/TBorderSide/Bottom')
    currentunitlabelupperlist_template.insert(8, 'BorderLineColorToken = "UnitLabelBorder_M81_Otan"')
    currentunitlabelupperlist_template.insert(9, 'BorderLocalRenderLayer = 5')
    
    # Update fit style
    currentunitlabelupperlist_template.insert(13, 'FitStyle = ~/ContainerFitStyle/FitToContent')
    
    logger.debug("Updated current unit label upper list properties")
