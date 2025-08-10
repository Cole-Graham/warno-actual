"""Functions for modifying UI unit button view."""
from typing import Any

from src import ndf
from src.utils.logging_utils import setup_logger
from src.utils.ndf_utils import is_obj_type

logger = setup_logger(__name__)


def edit_uispecificunitbuttonview(source_path) -> None:
    """Edit UISpecificUnitButtonView.ndf.
    
    Args:
        source_path: NDF file containing unit button view definitions
    """
    logger.info("Editing UISpecificUnitButtonView.ndf")
    
    # Update basic button properties
    source_path.by_namespace("AddRemoveButtonSize").v = "20.0"
    logger.debug("Updated add/remove button size")
    
    # Update main unit button
    _update_main_unit_button(source_path)
    
    # Update corner button
    _update_corner_button(source_path)
    
    # Update add unit button
    _update_add_unit_button(source_path)
    
    # Update unit info display
    _update_unit_info_display(source_path)

    # Update unit availability display
    _update_nb_unit_in_the_pack(source_path)
    
    # Update text components
    _update_text_components(source_path)


def _update_main_unit_button(source_path) -> None:
    """Update main unit button properties."""
    mainunitbutton_template = source_path.by_namespace("MainUnitButton").v
    mainunitbutton_template.by_member("BorderLineColorToken").v = '"BoutonVignetteAchatArmory_M81"'
    logger.debug("Updated main unit button border color")


def _update_corner_button(source_path) -> None:
    """Update corner button properties."""
    unitcornerbutton_template = source_path.by_namespace("UnitCornerButton").v
    unitcornerbutton_template.by_member("ButtonAlignementToAnchor").v = "[-3.35, 0.0]"
    logger.debug("Updated corner button alignment")


def _update_add_unit_button(source_path) -> None:
    """Update add unit button properties."""
    addunitbutton = source_path.by_namespace("AddUnitButton").v
    addunitbutton.by_member("BackgroundBlockColorToken").v = '"DeckCreator/AddUnitToDeck_M81"'
    addunitbutton.by_member("TextSizeToken").v = '"20"'
    addunitbutton.by_member("TextColorToken").v = "'BoutonUnit_deck_M81'"
    addunitbutton.by_member("TextTypefaceToken").v = "'Bombardier'"
    logger.debug("Updated add unit button text properties")


def _update_unit_info_display(source_path) -> None:
    """Update unit info display properties."""
    affichageinfosunit = source_path.by_namespace("AffichageInfosUnit").v
    
    for component in affichageinfosunit.by_member("Components").v:
        if not isinstance(component.v, ndf.model.Object) or not is_obj_type(component.v, "BUCKListDescriptor"):
            continue
            
        _process_info_elements(component.v.by_member("Elements").v)
    logger.debug("Updated unit info display properties")


def _update_nb_unit_in_the_pack(source_path) -> None:
    """Update unit info display properties."""
    nbunitinthepack = source_path.by_namespace("NbUnitInThePack").v

    for component in nbunitinthepack.by_member("Components").v:
        if not isinstance(component.v, ndf.model.Object) or not is_obj_type(component.v, "BUCKListDescriptor"):
            continue

        _process_info_elements(component.v.by_member("Elements").v, True)
    logger.debug("Updated unit info display properties")


def _process_info_elements(elements_list: Any, nbunitinthepack=False) -> None:
    """Process unit info display elements."""
    for element in elements_list:
        if not isinstance(element.v, ndf.model.Object) or not is_obj_type(element.v, "BUCKListElementDescriptor"):
            continue
            
        component_descr = element.v.by_member("ComponentDescriptor").v
        if component_descr.type != "BUCKListDescriptor":  # noqa
            continue
            
        _update_nested_elements(component_descr.by_member("Elements").v, nbunitinthepack)  # noqa


def _update_nested_elements(nested_elements_list: Any, nbunitinthepack) -> None:
    """Update nested element properties."""
    for nested_element in nested_elements_list:
        if not isinstance(nested_element.v, ndf.model.Object) or not is_obj_type(nested_element.v, "BUCKListElementDescriptor"):
            continue
            
        nested_component_descr = nested_element.v.by_member("ComponentDescriptor").v
        if nested_component_descr.type != "BUCKTextureDescriptor":  # noqa
            continue

        if nbunitinthepack:
            nested_component_descr.by_member("TypefaceToken").v = '"Bombardier"'  # noqa
        else:
            _update_component_frames(nested_component_descr)
            _update_texture_properties(nested_component_descr)
        break


def _update_component_frames(component_descr: Any) -> None:
    """Update component frame properties."""
    component_frame = component_descr.by_member("ComponentFrame").v
    component_frame.by_member("MagnifiableWidthHeight").v = "[20.0, 20.0]"
    component_frame.by_member("AlignementToFather").v = "[0.0, 0.0]"
    component_frame.by_member("AlignementToAnchor").v = "[0.0, 0.0]"


def _update_texture_properties(component_descr: Any) -> None:
    """Update texture properties."""
    texture_frame = component_descr.by_member("TextureFrame").v
    texture_frame.by_member("MagnifiableWidthHeight").v = "[25.0, 25.0]"
    texture_frame.add("AlignementToFather = [0.50, 0.50]")
    texture_frame.add("AlignementToAnchor = [0.50, 0.50]")
    
    component_descr.by_member("BackgroundBlockColorToken").v = '"ArmoryUnitButtonName_M81_Artichoke"'
    component_descr.add('TextureColorToken = "M81_VeryDarkCharcoal"')


def _update_text_components(source_path) -> None:
    """Update text component properties."""
    # Update unit name text
    _update_unit_name_text(source_path)
    
    # Update pack and unit name list
    packandunitnamelist = source_path.by_namespace("PackAndUnitNameList").v
    packandunitnamelist.by_member("BackgroundBlockColorToken").v = '"ArmoryUnitButtonName_M81_Artichoke"'
    
    # Update additional unit name text
    _update_additional_name_text(source_path)
    
    # Update unit alone name text
    unitbuttonunitalonenametext = source_path.by_namespace("UnitButtonUnitAloneNameText").v
    unitbuttonunitalonenametext.by_member("TextColor").v = '"SD2_BlancPur"'
    
    # Update XP unit
    xpunit = source_path.by_namespace("XPUnit").v
    xpunit.by_member("BackgroundBlockColorToken").v = '"M81_DarkCharcoal"'
    
    # Update pack number
    nombredepack = source_path.by_namespace("NombreDePack").v
    nombredepack.by_member("BackgroundBlockColorToken").v = '"M81_Quincy"'
    nombredepack.by_member("TextColor").v = '"SD2_BlancPur"'
    
    logger.debug("Updated text component properties")


def _update_unit_name_text(source_path) -> None:
    """Update unit name text properties."""
    unitbuttonunitnametext = source_path.by_namespace("UnitButtonUnitNameText").v
    
    # Update component frame
    componentframe = unitbuttonunitnametext.by_member("ComponentFrame").v
    componentframe.by_member("RelativeWidthHeight").v = "[1.0, 8.5]"
    componentframe.by_member("MagnifiableWidthHeight").v = "[0.0, 1.0]"
    
    # Update paragraph style
    paragraphstyle = unitbuttonunitnametext.by_member("ParagraphStyle").v
    paragraphstyle.by_member("VerticalAlignment").v = "UIText_Up"

    unitbuttonunitnametext.by_member("TypefaceToken").v = '"Bombardier"'
    
    # Add text padding
    unitbuttonunitnametext.insert(9, 'TextPadding = TRTTILength4 ( Magnifiable = [0.0, 2.0, 0.0, 0.0] )')
    unitbuttonunitnametext.by_member("TextColor").v = '"BoutonUnit_deck_M81"'


def _update_additional_name_text(source_path) -> None:
    """Update additional unit name text properties."""
    unitbuttonadditionalunitnametext = source_path.by_namespace("UnitButtonAdditionalUnitNameText").v
    unitbuttonadditionalunitnametext.by_member("BackgroundBlockColorToken").v = '"ArmoryUnitButtonName_M81"'
    unitbuttonadditionalunitnametext.by_member("TextColor").v = '"TransportedText_M81"'

    prixunit = source_path.by_namespace("PrixUnit").v
    prixunit.by_member("TypefaceToken").v = '"Bombardier"'
