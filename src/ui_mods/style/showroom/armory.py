"""Functions for modifying showroom armory component."""
# from src import ndf
from src.utils.logging_utils import setup_logger
from src.utils.ndf_utils import find_obj_by_type

logger = setup_logger(__name__)


def edit_uispecificshowroomarmorycomponent(source_path) -> None:
    """Edit UISpecificShowroomArmoryComponent.ndf.
    
    Args:
        source_path: NDF file containing showroom armory component definitions
    """
    logger.info("Editing UISpecificShowroomArmoryComponent.ndf")
    
    # Update max units
    source_path.by_namespace("MaxUnitsInDeckPerCategory").v = "11"
    logger.debug("Updated max units in deck per category")
    
    _edit_armory_component(source_path)
    _edit_category_button_descr(source_path)
    _edit_togglable_filter_button(source_path)
    _edit_division_filter_button(source_path)
    _edit_showroom_top_filters_bar(source_path)
    _edit_allnationsfilter(source_path)
    _edit_allegiancedivisionfilter(source_path)
    _edit_unitgridnamefilter(source_path)

def _edit_armory_component(source_path) -> None:
    """edit ArmoryComponentDescriptor"""
    
    # armory_component = source_path.by_namespace("ArmoryComponentDescriptor")
    # unit_pack_descriptor = armory_component.v.by_member("UnitPackDescriptor")
    pass

def _edit_category_button_descr(source_path) -> None:
    """edit ArmoryCategoryButtonDescriptor"""
    
    category_button_descr = source_path.by_namespace("ArmoryCategoryButtonDescriptor")
    components = category_button_descr.v.by_m("Components")
    bucktextdescriptor = find_obj_by_type(components.v, "BUCKTextDescriptor")
    bucktextdescriptor.v.by_m("TextSize").v = '"18"'

def _edit_togglable_filter_button(source_path) -> None:
    """edit ShowroomTogglableFilterButton"""

    togglable_filter_button = source_path.by_namespace("ShowroomTogglableFilterButton")
    togglable_filter_button.v.params.by_param("MagnifiableWidthHeight").v = "[40.0, 24.0]"
    
def _edit_division_filter_button(source_path) -> None:
    """edit ArmoryDivisionFilterButtonDescriptor"""

    division_filter_button = source_path.by_namespace("ArmoryDivisionFilterButtonDescriptor")
    division_filter_button.v.by_m("ComponentFrame").v.by_m("MagnifiableWidthHeight").v = "[52.0, 52.0]"

def _edit_showroom_top_filters_bar(source_path) -> None:
    """edit ShowroomTopFiltersBarContainer"""
    
    showroom_top_filters_bar = source_path.by_namespace("ShowroomTopFiltersBarContainer")
    elements = showroom_top_filters_bar.v.by_m("Elements")
    
    new_value = """[
    BUCKListElementDescriptor
    (
        ComponentDescriptor = ~/AllNationsFilter
    ),
    BUCKListElementDescriptor
    (   
        ComponentDescriptor = BUCKSpecificScrollingContainerDescriptor
        (
            ElementName = "UnitDivisionScrollingContainer222"
            ComponentFrame = TUIFramePropertyRTTI
            (
                MagnifiableWidthHeight = [1500.0, 60.0]
                AlignementToFather = [0.5, 0.0]
                AlignementToAnchor = [0.5, 0.0]
            )

            ExternalScrollbar = true
            ScrollStepSize = [0.0, 60.0]
            HasHorizontalScrollbar = true
            ScrollBarBackgroundToken = "AmroryButtonTxt"
            ScrollBarElevatorBackgroundToken = "AmroryButtonBkg"
            HorizontalScrollbarComponentFrame = TUIFramePropertyRTTI
            (
                MagnifiableWidthHeight = [0.0, 2.0]
                MagnifiableOffset = [0.0, 55.0]
            )

            Components = [AllegianceDivisionFilter(ElementName = "NATODivisionFilterRack")]
        )
    ),
    BUCKListElementDescriptor
    (   
        ComponentDescriptor = BUCKSpecificScrollingContainerDescriptor
        (
            ElementName = "UnitDivisionScrollingContainer223"
            ComponentFrame = TUIFramePropertyRTTI
            (
                MagnifiableWidthHeight = [1500.0, 60.0]
                AlignementToFather = [0.5, 0.0]
                AlignementToAnchor = [0.5, 0.0]
            )

            ExternalScrollbar = true
            ScrollStepSize = [0.0, 60.0]
            HasHorizontalScrollbar = true
            ScrollBarBackgroundToken = "AmroryButtonTxt"
            ScrollBarElevatorBackgroundToken = "AmroryButtonBkg"
            HorizontalScrollbarComponentFrame = TUIFramePropertyRTTI
            (
                MagnifiableWidthHeight = [0.0, 2.0]
                MagnifiableOffset = [0.0, -1.0]
            )

            Components = [AllegianceDivisionFilter(ElementName = "PACTDivisionFilterRack")]
        )
    ),
    BUCKListElementDescriptor
    (
        ComponentDescriptor = ~/DisplayNewFilterBar
    ),
]"""
    elements.v = new_value
    
def _edit_allnationsfilter(source_path) -> None:
    """edit AllNationsFilter"""
    
    allnationsfilter = source_path.by_namespace("AllNationsFilter")
    allnationsfilter.v.by_m("ComponentFrame").v.by_m("MagnifiableWidthHeight").v = "[0,24]"
    
def _edit_allegiancedivisionfilter(source_path) -> None:
    """edit AllegianceDivisionFilter"""
    
    allegiance_division_filter = source_path.by_namespace("AllegianceDivisionFilter")
    allegiance_division_filter.v.by_m("ComponentFrame").v.by_m("MagnifiableWidthHeight").v = "[0.0, 0.0]"

def _edit_unitgridnamefilter(source_path) -> None:
    """edit UnitGridNameFilter"""
    
    # unitgridnamefilter = source_path.by_namespace("UnitGridNameFilter")
    pass
    