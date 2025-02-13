"""Functions for editing in-game UI styles."""
from typing import Any

from src import ndf
from src.utils.logging_utils import setup_logger

logger = setup_logger(__name__)


def edit_uiingameresources(source_path: Any) -> None:
    """Edit UIInGameResources.ndf to modify UI layout and styling."""
    logger.info("Editing in-game UI resources")
    
    # Update chat view style
    uiingameresource = source_path.by_n("UIInGameResource").v
    viewdescriptors_map = uiingameresource.by_m("ViewDescriptors").v
    ingamechatviewdescriptor = viewdescriptors_map.by_k('"UISpecificIngameChatViewDescriptor"').v
    ingamechatviewdescriptor.by_m("PanelColorStyle").v = '"ChatPANELColorStyleM81"'
    ingamechatviewdescriptor.by_m("ButtonColorStyle").v = '"ChatBUTTONColorStyleM81"'
    
    # Update frame width
    source_path.by_n("IngameHUDRightFramesWidth").v = "385.0"
    
    # Modify main container layout
    ingamehudmaintcontainer = source_path.by_n("InGameMainContainerResource").v
    foreground_components = ingamehudmaintcontainer.by_m("ForegroundComponents").v
    components = foreground_components.by_m("Components").v
    
    # Remove/update existing components
    for component in components:
        if not isinstance(component.v, ndf.model.Object):
            continue
        
        if component.v.type == "BUCKContainerDescriptor":
            unique_name = component.v.by_m("UniqueName", False)
            if unique_name is not None and unique_name.v == '"SpecificLaunchBattleMainComponentDescriptor"':
                component_frame = component.v.by_m("ComponentFrame").v
                component_frame.by_m("MagnifiableOffset").v = "[0.0, 138.0]"  # noqa
            
        elif component.v.by_m("UniqueName", False) is not None:
            if component.v.by_m("UniqueName").v == '"barre_du_haut"':
                components.remove(component)

        else:
            elements = component.v.by_m("Elements").v
            for element in elements:

                if not isinstance(element.v, ndf.model.Object):
                    continue
                    
                component_descriptor = element.v.by_m("ComponentDescriptor").v
                if component_descriptor.type == "BUCKContainerDescriptor":  # noqa
                    unique_name = component_descriptor.by_m("UniqueName").v  # noqa
                    
                    if unique_name == '"SpecificInGameHUDTimePanelViewMainContainer"':
                        elements.remove(element)
                    elif unique_name == '"UISpecificMiniMapInfoViewMainContainer"':
                        component_descriptor.by_m("ComponentFrame").v.add("MagnifiableOffset = [0.0, 10.0]")  # noqa
                    elif unique_name == '"UICommonFlarePanelViewMainContainer"':
                        component_descriptor.by_m("ComponentFrame").v.by_m("RelativeWidthHeight").v = "[0.8312, 0.0]"  # noqa
                        component_descriptor.by_m("ComponentFrame").v.add("AlignementToFather = [0.1688, 0.3]")  # noqa
                    elif unique_name == '"SpecificInGameHUDScoreViewMainContainer"':
                        frame = component_descriptor.by_m("ComponentFrame").v  # noqa
                        frame.by_m("RelativeWidthHeight").v = "[0.8312, 0.0]"
                        frame.add("AlignementToFather = [0.1688, 0.0]")
                        frame.add("MagnifiableOffset = [0.0, 10.0]")
    
    # Add new top bar component
    new_entry = (
        f'BUCKListDescriptor'
        f'('
        f'    ComponentFrame = TUIFramePropertyRTTI'
        f'    ('
        f'        RelativeWidthHeight = [1.0, 1.0]'
        f'        AlignementToAnchor = [0.0, 0.0]'
        f'        AlignementToFather = [0.0, 0.0]'
        f'    )'
        f'    InterItemMargin = TRTTILength( Magnifiable = 0.0 )'
        f'    Axis = ~/ListAxis/Horizontal'
        f'    Elements = ['
        f'        BUCKListElementDescriptor'
        f'        ('
        f'            ComponentDescriptor = BUCKContainerDescriptor'
        f'            ('
        f'                UniqueName = "barre_du_haut"'
        f'                ComponentFrame = TUIFramePropertyRTTI'
        f'                ('
        f'                    MagnifiableWidthHeight  = [1020.0, 40.0]'
        f'                    AlignementToAnchor = [0, 0.0]'
        f'                    AlignementToFather = [0, 0.0]'
        f'                )'
        f'                HasBackground = true'
        f'                BackgroundBlockColorToken = "M81_Ebony"'
        f'            )'
        f'        ),'
        f'        BUCKListElementDescriptor'
        f'        ('
        f'            ComponentDescriptor = BUCKContainerDescriptor'
        f'            ('
        f'                UniqueName = "SpecificInGameHUDTimePanelViewMainContainer"'
        f'                ComponentFrame = TUIFramePropertyRTTI'
        f'                ('
        f'                    MagnifiableWidthHeight = [300.0, 40.0]'
        f'                    AlignementToAnchor = [0.5, 0.0]'
        f'                    AlignementToFather = [0.5, 0.0]'
        f'                )'
        f'                Components ='
        f'                ['
        f'                    PanelRoundedCorner'
        f'                    ('
        f'                        ComponentFrame = TUIFramePropertyRTTI ( RelativeWidthHeight = [1.0, 1.0] )'
        f'                        FitStyle = ~/ContainerFitStyle/FitToContent'
        f'                        HasBackground = true'
        f'                        HasBorder = true'
        f'                        BackgroundBlockColorToken = "M81_MonochromeCRT"'
        f'                        BorderLineColorToken = "AppleIIc"'
        f'                        BorderThicknessToken = "1"'
        f'                        BackgroundLocalRenderLayer = 0'
        f'                        BorderLocalRenderLayer = 0'
        f'                        RoundedVertexes = [false, false, false, true]'
        f'                        Radius = 20'
        f'                    )'
        f'                ]'
        f'            )'
        f'        )'
        f'    ]'
        f')'
    )
    components.insert(1, new_entry)
