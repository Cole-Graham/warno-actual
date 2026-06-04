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
    
    # if target == "gameplay":
        # _edit_armory_component(source_path)
        # _edit_category_button_descr(source_path)
        # _edit_togglable_filter_button(source_path)
        # _edit_division_filter_button(source_path)
        # _edit_division_scroll_containers(source_path)
        # _edit_allegiancedivisionfilter(source_path)
        # _edit_unitgridnamefilter(source_path)
    
    _edit_armory_component(source_path)
    _edit_category_button_descr(source_path)
    _edit_togglable_filter_button(source_path)
    _edit_division_filter_button(source_path)
    _edit_division_scroll_containers(source_path)
    _edit_flag_division_filter_row_spacing(source_path)
    _edit_display_new_filter_bar_spacing(source_path)
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

    Shrinks the national flag buttons back to the mod's smaller size. The flag
    texture's TextureFrame now uses RelativeWidthHeight = [1.0, 1.0], so it scales
    with the button automatically and needs no fixed-height override.
    """

    togglable_filter_button = source_path.by_namespace("ShowroomTogglableFilterButton")
    togglable_filter_button.v.params.by_param("MagnifiableWidthHeight").v = "[40.0, 24.0]"
    
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


def _edit_flag_division_filter_row_spacing(source_path) -> None:
    """Add 2px vertical gaps between the four flag/division filter rows."""

    flag_and_division_filter = source_path.by_namespace("TopFilterDisplay_AllFlagAndDivisionFilter").v
    margin = flag_and_division_filter.by_m("InterItemMargin", False)
    if margin is None:
        flag_and_division_filter.add("InterItemMargin = TRTTILength(Magnifiable = 2.0)")
    else:
        margin.v = "TRTTILength(Magnifiable = 2.0)"
    logger.debug("Set TopFilterDisplay_AllFlagAndDivisionFilter InterItemMargin to 2.0")


def _edit_display_new_filter_bar_spacing(source_path) -> None:
    """Push DisplayNewFilterBar down 4px via FiltersPanelList InterItemMargin."""

    filters_panel_list = source_path.by_namespace("FiltersPanelList").v
    margin = filters_panel_list.by_m("InterItemMargin", False)
    if margin is None:
        filters_panel_list.add("InterItemMargin = TRTTILength(Magnifiable = 4.0)")
        new_value = 4.0
    else:
        magnifiable = margin.v.by_m("Magnifiable", False)
        if magnifiable is not None:
            current = float(magnifiable.v)
            new_value = current + 4.0
            magnifiable.v = str(new_value)
        else:
            margin.v = "TRTTILength(Magnifiable = 4.0)"
            new_value = 4.0
    logger.debug("Set FiltersPanelList InterItemMargin to %s", new_value)


def _edit_allegiancedivisionfilter(source_path) -> None:
    """edit AllegianceDivisionFilter"""
    
    allegiance_division_filter = source_path.by_namespace("AllegianceDivisionFilter")
    allegiance_division_filter.v.by_m("ComponentFrame").v.by_m("MagnifiableWidthHeight").v = "[0.0, 0.0]"

def _edit_unitgridnamefilter(source_path) -> None:
    """edit UnitGridNameFilter"""
    
    # unitgridnamefilter = source_path.by_namespace("UnitGridNameFilter")
    pass
