"""Functions for modifying UI cube action components."""
from typing import Any

from src import ndf
from src.utils.logging_utils import setup_logger
from src.utils.ndf_utils import is_obj_type

logger = setup_logger(__name__)

def edit_uiingamebuckcubeaction(source_path) -> None:
    """Edit UIInGameBUCKCubeAction.ndf."""
    logger.info("Editing UIInGameBUCKCubeAction.ndf")
    
    # Update cube action buttons
    _update_cube_action_button(source_path)
    _update_cube_action_toggle_button(source_path)
    
    # Update cube action panels
    _update_panel_cube_action_orders(source_path)
    _update_panel_cube_action_smart_orders(source_path)

def _update_cube_action_button(source_path) -> None:
    """Update cube action button properties."""
    cubeactionbutton_template = source_path.by_namespace("CubeActionButton").v
    
    # Update text and colors
    cubeactionbutton_template.params.by_param("TextColor").v = '"ButtonHUD/Text2_M81CubeAction"'
    cubeactionbutton_template.params.by_param("BackgroundBlockColorToken").v = '"BoutonTemps"'
    cubeactionbutton_template.params.by_param("BorderLineColorToken").v = '"BoutonTempsM81CubeActionLine"'
    
    # Add new color parameters
    index = cubeactionbutton_template.params.by_param("BigLineAction").index + 1
    cubeactionbutton_template.params.insert(index, 'BackgroundColor : string = "Fulda2_BoutonCubeAction"')
    cubeactionbutton_template.params.insert(index + 1, 'BorderColor : string = "ButtonHUD/BigBorder_M81CubeAction"')
    
    # Update components
    cubeactionbutton_template.by_member("Components").v = _get_cube_action_button_components()
    logger.debug("Updated cube action button properties")

def _update_cube_action_toggle_button(source_path) -> None:
    """Update cube action toggle button properties."""
    cubeactiontogglebutton_template = source_path.by_namespace("CubeActionToggleButton").v
    cubeactiontogglebutton_template.by_member("BackgroundBlockColorToken").v = '"BoutonTemps"'
    cubeactiontogglebutton_template.by_member("BorderLineColorToken").v = '"BoutonTemps"'
    
    for component in cubeactiontogglebutton_template.by_member("Components").v:
        if not isinstance(component.v, ndf.model.Object):
            continue
            
        if is_obj_type(component.v, "PanelRoundedCorner"):
            component.v.by_member("BackgroundBlockColorToken").v = '"BoutonTemps"'
            component.v.by_member("BorderLineColorToken").v = '"BoutonTemps"'
        elif is_obj_type(component.v, "BUCKTextDescriptor"):
            component.v.by_member("TextColor").v = '"ButtonHUD/Text2_toggle"'
    
    logger.debug("Updated cube action toggle button properties")

def _update_panel_cube_action_orders(source_path) -> None:
    """Update panel cube action orders properties."""
    panelcubeactionorders = source_path.by_namespace("PanelCubeAction_Orders").v
    
    for component in panelcubeactionorders.by_member("BackgroundComponents").v:
        if not isinstance(component.v, ndf.model.Object) or not is_obj_type(component.v, "PanelRoundedCorner"):
            continue
            
        _process_panel_components(component.v.by_member("Components").v)
    
    logger.debug("Updated panel cube action orders properties")

def _update_panel_cube_action_smart_orders(source_path) -> None:
    """Update panel cube action smart orders properties."""
    panelcubeactionsmartorders = source_path.by_namespace("PanelCubeAction_SmartOrders").v
    
    # Update grid margins
    elements = panelcubeactionsmartorders.by_member("Elements").v
    for element in elements:
        if not isinstance(element.v, ndf.model.Object) or not is_obj_type(element.v, "BUCKListElementDescriptor"):
            continue
            
        component_descr = element.v.by_member("ComponentDescriptor").v
        if component_descr.type != "BUCKGridDescriptor":
            continue
            
        component_descr.by_member("LastElementMargin").v = "TRTTILength2( Magnifiable = [5.0, 0.0] )"
    
    # Update background components
    for component in panelcubeactionsmartorders.by_member("BackgroundComponents").v:
        if not isinstance(component.v, ndf.model.Object) or not is_obj_type(component.v, "PanelRoundedCorner"):
            continue
            
        component.v.add("HasBackground = true")
        component.v.add('BackgroundBlockColorToken = "M81_Ebony"')
    
    logger.debug("Updated panel cube action smart orders properties")

def _process_panel_components(components: Any) -> None:
    """Process panel components to update nested elements."""
    for component in components:
        if not isinstance(component.v, ndf.model.Object) or not is_obj_type(component.v, "BUCKListDescriptor"):
            continue
            
        for element in component.v.by_member("Elements").v:
            if not isinstance(element.v, ndf.model.Object) or not is_obj_type(element.v, "BUCKListElementDescriptor"):
                continue
                
            component_descr = element.v.by_member("ComponentDescriptor").v
            if component_descr.type != "PanelRoundedCorner":
                continue
                
            component_descr.add("HasBackground = true")
            component_descr.add('BackgroundBlockColorToken = "M81_Ebony"')

def _get_cube_action_button_components() -> str:
    """Get cube action button component template."""
    return '''\n
    [
        PanelRoundedCorner
        (
            ComponentFrame = TUIFramePropertyRTTI
            (
                RelativeWidthHeight = [1.0, 1.0]
                MagnifiableWidthHeight = [-4.0, -4.0]
                AlignementToFather = [0.5, 0.5]
                AlignementToAnchor = [0.5, 0.5]
            )

            Radius = 3
            BackgroundBlockColorToken = <BackgroundBlockColorToken>
            BorderLineColorToken = <BorderLineColorToken>
            RoundedVertexes = <RoundedVertexes>
        ),
        BUCKTextDescriptor
        (
            ElementName = "CubeActionButtonText"

            ComponentFrame = TUIFramePropertyRTTI
            (
                RelativeWidthHeight = [0.9, 0.9]
                MagnifiableWidthHeight = [-6.0, -6.0]
                AlignementToFather = [0.5, 0.5]
                AlignementToAnchor = [0.5, 0.5]
            )

            ParagraphStyle = TParagraphStyle
            (
                Alignment = UIText_Center
                VerticalAlignment = UIText_VerticalCenter
                InterLine = -0.2
            )

            HasBorder = <HasBorder>
            BorderLineColorToken = 'ButtonHUD/Text2'
            BorderThicknessToken = '1'
            HasBackground = false
            BackgroundBlockColorToken = 'bouton_cubeAction'

            TextStyle = "Default"
            HorizontalFitStyle = ~/FitStyle/UserDefined
            VerticalFitStyle = ~/FitStyle/UserDefined

            BigLineAction   = <BigLineAction>
            TextColor       = <TextColor>
            TextSize        = <TextSize>
            TextDico        = ~/LocalisationConstantes/dico_interface_outgame
            TypefaceToken   = "Liberator"
        ),
    ] +

    (<HintableAreaComponent> != nil ? [<HintableAreaComponent>] : [])''' 