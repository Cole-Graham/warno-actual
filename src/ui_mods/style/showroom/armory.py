"""Functions for modifying showroom armory component."""
# from src import ndf
from src.utils.logging_utils import setup_logger
from src.utils.ndf_utils import find_obj_by_type
from src import ModConfig

logger = setup_logger(__name__)

config = ModConfig.get_instance()
target = config.config_data['build_config']['target']

def edit_uispecificshowroomarmorycomponent(source_path) -> None:
    """Edit GameData/UserInterface/Use/ShowRoom/Views/UISpecificShowRoomArmoryComponent.ndf.
    
    Args:
        source_path: NDF file containing showroom armory component definitions
    """
    logger.info("Editing UISpecificShowRoomArmoryComponent.ndf")
    
    # Update max units
    source_path.by_namespace("MaxUnitsInDeckPerCategory").v = "11"
    logger.debug("Updated max units in deck per category")
    
    if target == "gameplay":
        _edit_armory_component(source_path)
        _edit_category_button_descr(source_path)
        _edit_togglable_filter_button(source_path)
        _edit_division_filter_button(source_path)
        _edit_division_scroll_containers(source_path)
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
    """edit ShowroomTogglableFilterButton

    Shrinks the national flag buttons back to the mod's smaller size and shrinks
    the flag texture frame (added in the VIP layout) to match the smaller button
    height so the clipped flag fills the button cleanly.
    """

    togglable_filter_button = source_path.by_namespace("ShowroomTogglableFilterButton")
    togglable_filter_button.v.params.by_param("MagnifiableWidthHeight").v = "[40.0, 24.0]"

    # The VIP template clips the flag texture to a [0, 40] frame; match it to the
    # smaller [40, 24] button so the flag isn't cut off vertically.
    components = togglable_filter_button.v.by_m("Components")
    flag_texture = find_obj_by_type(components.v, "BUCKTextureDescriptor")
    flag_texture.v.by_m("TextureFrame").v.by_m("MagnifiableWidthHeight").v = "[0, 24]"
    
def _edit_division_filter_button(source_path) -> None:
    """edit ArmoryDivisionFilterButtonDescriptor"""

    division_filter_button = source_path.by_namespace("ArmoryDivisionFilterButtonDescriptor")
    division_filter_button.v.by_m("ComponentFrame").v.by_m("MagnifiableWidthHeight").v = "[52.0, 52.0]"

def _edit_division_scroll_containers(source_path) -> None:
    """edit TopFilterDisplay_AllFlagAndDivisionFilter

    Wraps the NATO/PACT division racks in horizontal scrolling containers while
    leaving the country flag racks untouched, preserving the VIP layout
    (NATO flags, NATO divisions, PACT flags, PACT divisions).
    """

    flag_and_division_filter = source_path.by_namespace("TopFilterDisplay_AllFlagAndDivisionFilter")
    elements = flag_and_division_filter.v.by_m("Elements")

    new_value = """[
    // NATO national flags
    BUCKListElementDescriptor
    (
        ComponentDescriptor = BUCKListElementDescriptor
        (
            ComponentDescriptor = BUCKRackDescriptor
            (
                ElementName = "NATOCountryFilterRack"
                ComponentFrame = TUIFramePropertyRTTI ()

                BreadthComputationMode = ~/BreadthComputationMode/ComputeBreadthFromLargestChild

                FirstMargin = TRTTILength( Magnifiable = 0.0 )
                InterItemMargin = TRTTILength( Magnifiable = 8.0 )
                Axis = ~/ListAxis/Horizontal

                BladeDescriptor = ArmoryCountryFilterButtonDescriptor
            )
        )
    ),
    // NATO divisions (scrollable)
    BUCKListElementDescriptor
    (
        ComponentDescriptor = BUCKSpecificScrollingContainerDescriptor
        (
            ElementName = "NATODivisionScrollingContainer"
            ComponentFrame = TUIFramePropertyRTTI
            (
                MagnifiableWidthHeight = [1700.0, 62.0]
            )

            ExternalScrollbar = true
            ScrollStepSize = [18.34, 0.0]
            HasHorizontalScrollbar = true
            ScrollBarBackgroundToken = "AmroryButtonTxt"
            ScrollBarElevatorBackgroundToken = "AmroryButtonBkg"
            HorizontalScrollbarComponentFrame = TUIFramePropertyRTTI
            (
                MagnifiableWidthHeight = [0.0, 3.5]
                MagnifiableOffset = [0.0, 56.0]
            )
            Components = [AllegianceDivisionFilter(ElementName = "NATODivisionFilterRack")]
        )
    ),
    // PACT national flags
    BUCKListElementDescriptor
    (
        ComponentDescriptor = BUCKListElementDescriptor
        (
            ComponentDescriptor = BUCKRackDescriptor
            (
                ElementName = "PACTCountryFilterRack"
                ComponentFrame = TUIFramePropertyRTTI()

                BreadthComputationMode = ~/BreadthComputationMode/ComputeBreadthFromLargestChild

                FirstMargin = TRTTILength( Magnifiable = 0.0 )
                InterItemMargin = TRTTILength( Magnifiable = 8.0 )
                Axis = ~/ListAxis/Horizontal

                BladeDescriptor = ArmoryCountryFilterButtonDescriptor
            )
        )
    ),
    // PACT divisions (scrollable)
    BUCKListElementDescriptor
    (
        ComponentDescriptor = BUCKSpecificScrollingContainerDescriptor
        (
            ElementName = "PACTDivisionScrollingContainer"
            ComponentFrame = TUIFramePropertyRTTI
            (
                MagnifiableWidthHeight = [1700.0, 62.0]
            )

            ExternalScrollbar = true
            ScrollStepSize = [18.34, 0.0]
            HasHorizontalScrollbar = true
            ScrollBarBackgroundToken = "AmroryButtonTxt"
            ScrollBarElevatorBackgroundToken = "AmroryButtonBkg"
            HorizontalScrollbarComponentFrame = TUIFramePropertyRTTI
            (
                MagnifiableWidthHeight = [0.0, 3.5]
                MagnifiableOffset = [0.0, 56.0]
            )
            Components = [AllegianceDivisionFilter(ElementName = "PACTDivisionFilterRack")]
        )
    ),
]"""
    elements.v = new_value

def _edit_allegiancedivisionfilter(source_path) -> None:
    """edit AllegianceDivisionFilter"""
    
    allegiance_division_filter = source_path.by_namespace("AllegianceDivisionFilter")
    allegiance_division_filter.v.by_m("ComponentFrame").v.by_m("MagnifiableWidthHeight").v = "[0.0, 0.0]"

def _edit_unitgridnamefilter(source_path) -> None:
    """edit UnitGridNameFilter"""
    
    # unitgridnamefilter = source_path.by_namespace("UnitGridNameFilter")
    pass
