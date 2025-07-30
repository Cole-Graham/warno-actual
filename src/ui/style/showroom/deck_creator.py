"""Functions for modifying showroom deck creator components."""
from typing import Any

from src import ndf
from src.utils.logging_utils import setup_logger
from src.utils.ndf_utils import is_obj_type

logger = setup_logger(__name__)

def edit_uispecificshowroomdeckcreatorscreencomponent(source_path) -> None:
    """Edit UISpecificShowroomDeckCreatorScreenComponent.ndf."""
    logger.info("Editing UISpecificShowroomDeckCreatorScreenComponent.ndf")
    
    # Update max units
    source_path.by_namespace("DeckCreatorMaxUnitsInDeckPerCategory").v = "11"
    
    # Update XP button
    _update_xp_button(source_path)
    
    # Update deck list
    _update_deck_list(source_path)
    
    # Update deck name display
    _update_deck_name_display(source_path)
    
    # Update save buttons
    _update_save_buttons(source_path)
    
    # Update navigation button
    _update_navigation_button(source_path)
    
    # Update top bar
    _update_top_bar(source_path)
    
    # Update transport button
    _update_transport_button(source_path)
    
    # Update factory name descriptor
    _update_factorynamedescriptor(source_path)
    
    # Update FreeCaseDescriptor
    _update_freecasedescriptor(source_path)

def edit_uispecificshowroomgroupsdeckcreatorscreenview(source_path) -> None:
    """Edit UISpecificShowRoomGroupsDeckCreatorScreenView.ndf."""
    logger.info("Editing UISpecificShowRoomGroupsDeckCreatorScreenView.ndf")
    
    # Update smart group container
    _update_smart_group_container(source_path)
    
    # Update unit amount button
    _update_unitamountbutton(source_path)
    
    # Update activation points component
    _update_activationpointscomponent(source_path)

def _update_activationpointscomponent(source_path) -> None:
    """Update ActivationPointsComponent"""
    activationpointscomponent = source_path.by_namespace("ActivationPointsComponent")
    elements = activationpointscomponent.v.by_member("Elements")
    for element in elements.v:
        if isinstance(element.v, ndf.model.Object):
            if is_obj_type(element.v, "BUCKListElementDescriptor"):
                
                if element.v.by_member("ElementName").v == '"ActivationPointsCurrent"':
                    pass # for future edits of current activation points
                
                elif element.v.by_member("ElementName").v == '"ActivationPointsTemp"':
                    element.v.by_member("TextStyle").v = '"ActivationPointTemp_M81"'
                
                elif element.v.by_member("ElementName").v == '"ActivationPointsMax"':
                    pass # for future edits of max activation points
                
                elif element.v.by_member("ElementName").v == '"ActivationPointsTitre"':
                    pass # for future edits of title
                
                    
    activationpointscomponent.by_member("BackgroundBlockColorToken").v = '"M81_Ebony128"'
    logger.debug("Updated ActivationPointsComponent template")

def _update_factorynamedescriptor(source_path) -> None:
    """Update FactoryNameDescriptor template.
    UISpe"""
    factorynamedescriptor_template = source_path.by_namespace("FactoryNameDescriptor").v
    factorynamedescriptor_template.by_member("BackgroundBlockColorToken").v = '"M81_Ebony128"'
    logger.debug("Updated FactoryNameDescriptor template")

def _update_xp_button(source_path) -> None:
    """Update XP button properties."""
    boutonxp_template = source_path.by_namespace("BoutonXp").v
    component_descr = boutonxp_template.by_member("ComponentDescriptor").v
    
    component_descr.by_member("BorderLineColorToken").v = '"BoutonXP_deck_border_M81"'
    component_descr.by_member("BackgroundBlockColorToken").v = '"BoutonXP_deck_M81"'
    
    for component in component_descr.by_member("Components").v:
        if not isinstance(component.v, ndf.model.Object) or not is_obj_type(component.v, "BUCKTextureDescriptor"):
            continue
            
        if component.v.by_member("TextureColorToken", False) is not None:
            if component.v.by_member("TextureColorToken").v == '"BoutonXP_deck_chevron"':
                component.v.by_member("TextureColorToken").v = '"BoutonXP_deck_chevron_M81"'
    
    logger.debug("Updated XP button colors")

def _update_smart_group_container(source_path) -> None:
    """Update smart group container properties."""
    smartgroupinfoscontainer_template = source_path.by_namespace("SmartGroupInfosContainer").v
    
    # Update elements
    elements = smartgroupinfoscontainer_template.by_member("Elements").v
    for element in elements:
        if not isinstance(element.v, ndf.model.Object) or not is_obj_type(element.v, "BUCKListElementDescriptor"):
            continue
        
        if element.v.by_member("ElementName", False) is not None:
            if element.v.by_member("ElementName").v == '"SmartGroupNameEditableText"':
                element.v.by_member("TextColorToken").v = '"ButtonHUD/Text2_M81"'
                
        else:
            continue
    
    # Update foreground components
    new_foreground_value = '''\
(<IsEditable> ?
    []
    : [
        BUCKButtonDescriptor
        (
            ElementName = "SmartGroupProductionButton"
            ComponentFrame = TUIFramePropertyRTTI
            (
                RelativeWidthHeight = [1.0, 1.0]
            )
            IsTogglable = true
            CannotDeselect = true
            ForceEvents = true
            MaskEvents = false
            HidePointerEvents = true
            PointerEventsToAllow = ~/EAllowablePointerEventType/Move
            HasBorder = true
            BorderLineColorToken = "ButtonHUD/Text2_ALL_M81"
            BorderThicknessToken = "1"
        ),
    ]
)
'''
    smartgroupinfoscontainer_template.by_member("ForegroundComponents").v = new_foreground_value
    logger.debug("Updated smart group container components")
    
def _update_unitamountbutton(source_path) -> None:
    """Update UnitAmountButton"""
    unitamountbutton = source_path.by_namespace("UnitAmountButton").v
    unitamountbutton.by_member("BorderLineColorToken").v = '"BoutonTemps_Line_M81"'
    unitamountbutton.by_member("BackgroundBlockColorToken").v = '"BoutonTemps_Background_M81"'
    components = unitamountbutton.by_member("Components").v
    for component in components:
        if not isinstance(component.v, ndf.model.Object) or not is_obj_type(component.v, "BUCKTextDescriptor"):
            continue
        component.v.by_member("TextColor").v = '"UnitAmountButton_M81"'
    logger.debug("Updated UnitAmountButton")

def _update_deck_list(source_path) -> None:
    """Update deck list properties."""
    listedesunitesdudeck = source_path.by_namespace("ListeDesUnitesDuDeck").v
    componentframe = listedesunitesdudeck.by_member("ComponentFrame").v
    componentframe.by_member("MagnifiableOffset").v = "[25.0, 8.0]"
    logger.debug("Updated deck list offset")


def _update_deck_name_display(source_path) -> None:
    """Update deck name display properties."""
    affichagenomdudeck = source_path.by_namespace("AffichageNomDuDeck").v
    
    # Update frame alignment
    componentframe = affichagenomdudeck.by_member("ComponentFrame").v
    componentframe.by_member("AlignementToFather").v = "[-0.10, 0.5]"
    
    # Update elements
    for element in affichagenomdudeck.by_member("Elements").v:
        if not isinstance(element.v, ndf.model.Object) or not is_obj_type(element.v, "BUCKListElementDescriptor"):
            continue
            
        component_descr = element.v.by_member("ComponentDescriptor").v
        if component_descr.type == "BUCKTextDescriptor":  # noqa
            _update_text_alignment(component_descr)
        elif component_descr.type == "BUCKEditableTextDescriptor":  # noqa
            _update_editable_text(component_descr)
    
    logger.debug("Updated deck name display properties")


def _update_text_alignment(component: Any) -> None:
    """Update text component alignment."""
    componentframe = component.by_member("ComponentFrame").v
    componentframe.add("AlignementToAnchor = [0.0, 0.0]")
    componentframe.add("AlignementToFather = [0.0, 0.0]")


def _update_editable_text(component: Any) -> None:
    """Update editable text properties."""
    clippingcontainerframeproperty = component.by_member("ClippingContainerFrameProperty").v
    clippingcontainerframeproperty.by_member("AlignementToFather").v = "[0.0, 0.5]"
    clippingcontainerframeproperty.by_member("AlignementToAnchor").v = "[0.0, 0.5]"
    component.by_member("BackgroundBlockColorToken").v = '"M81_EbonyVeryDark"'


def _update_save_buttons(source_path) -> None:
    """Update save buttons properties."""
    deckeditorsaveandcobuttons = source_path.by_namespace("DeckEditorSaveAndCoButtons").v
    componentframe = deckeditorsaveandcobuttons.by_member("ComponentFrame").v
    componentframe.by_member("AlignementToAnchor").v = "[0.90, 0.5]"
    componentframe.by_member("AlignementToFather").v = "[0.90, 0.5]"
    logger.debug("Updated save buttons alignment")


def _update_navigation_button(source_path) -> None:
    """Update navigation button properties."""
    deckeditornavigationbutton_template = source_path.by_namespace("DeckEditorNavigationButton").v
    deckeditornavigationbutton_template.by_member("BackgroundBlockColorToken").v = '"M81_Ebony"'
    
    for component in deckeditornavigationbutton_template.by_member("Components").v:
        if not isinstance(component.v, ndf.model.Object) or not is_obj_type(component.v, "BUCKTextDescriptor"):
            continue
            
        component.v.by_member("TextColor").v = '<IsToggled> ? "BoutonXP_deck_chevron_M81" : "BoutonXP_deck_chevron_M81"'
    
    logger.debug("Updated navigation button colors")


def _update_top_bar(source_path) -> None:
    """Update top bar properties."""
    deckeditortopbargreenbackground = source_path.by_namespace("DeckEditorTopBarGreenBackground").v
    deckeditortopbargreenbackground.by_member("BackgroundBlockColorToken").v = '"M81_EbonyVeryDark"'
    deckeditortopbargreenbackground.by_member("BorderLineColorToken").v = '"M81_DarkCharcoal"'
    logger.debug("Updated top bar colors")


def _update_transport_button(source_path) -> None:
    """Update transport button properties."""
    notransportbuttondescriptor = source_path.by_namespace("NoTransportButtonDescriptor").v
    notransportbuttondescriptor.by_member("BorderLineColorToken").v = '"BoutonVignetteAchatArmory_M81"'
    logger.debug("Updated transport button border color")

def _update_freecasedescriptor(source_path) -> None:
    """Update FreeCaseDescriptor"""
    freecasedescriptor = source_path.by_namespace("FreeCaseDescriptor").v
    components = freecasedescriptor.by_member("Components").v
    for component in components:
        if not isinstance(component.v, ndf.model.Object) or not is_obj_type(component.v, "BUCKTextureDescriptor"):
            continue
        component.v.by_member("TextureColorToken").v = '"DeckCreator/SlotLibre_M81"'
    logger.debug("Updated FreeCaseDescriptor")
