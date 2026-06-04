"""Functions for editing in-game UI styles."""
from typing import Any

from src import ndf
from src.utils.logging_utils import setup_logger
from src.utils.ndf_utils import is_obj_type

logger = setup_logger(__name__)


def edit_uiingameresources(source_path: Any) -> None:
    """Edit GameData/UserInterface/Use/InGame/UIInGameResources.ndf to modify UI layout and styling."""
    logger.info("Editing in-game UI resources")

    uiingameresource = source_path.by_n("UIInGameResource").v
    viewdescriptors_map = uiingameresource.by_m("ViewDescriptors").v
    ingamechatviewdescriptor = viewdescriptors_map.by_k('"UISpecificIngameChatViewDescriptor"').v
    ingamechatviewdescriptor.by_m("PanelColorStyle").v = '"ChatPANELColorStyle_All_M81"'
    ingamechatviewdescriptor.by_m("ButtonColorStyle").v = '"ChatBUTTONColorStyle_All_M81"'

    source_path.by_n("IngameHUDRightFramesWidth").v = "385.0"

    ingamehudmaintcontainer = source_path.by_n("InGameMainContainerResource").v
    foreground_components = ingamehudmaintcontainer.by_m("ForegroundComponents").v
    components = foreground_components.by_m("Components")

    for component in components.v:
        if not isinstance(component.v, ndf.model.Object):
            continue

        if is_obj_type(component.v, "BUCKContainerDescriptor"):
            unique_name = component.v.by_m("UniqueName", False)
            if unique_name is not None and unique_name.v == '"SpecificLaunchBattleMainComponentDescriptor"':
                component_frame = component.v.by_m("ComponentFrame").v
                component_frame.by_m("MagnifiableOffset").v = "[0.0, 138.0]"
            elif unique_name is not None and unique_name.v == '"barre_du_haut"':
                components.v.remove(component)

        elif is_obj_type(component.v, "BUCKListDescriptor"):
            axis = component.v.by_m("Axis", False)
            if axis is not None and axis.v == "~/ListAxis/Vertical" and _is_right_hud_column(component.v):
                _replace_vertical_hud_elements(component.v)

    components.v.insert(1, _get_m81_top_bar_row())
    logger.debug("Applied M81 top bar and VIP-compliant right HUD column layout")


def _is_right_hud_column(vertical_list: Any) -> bool:
    """True only for the right HUD column list (the one holding the score/objectives views).

    ForegroundComponents now contains more than one top-level vertical list (VIP added a
    production/unit/tactic-cube column). We must only rebuild the right HUD column; rebuilding
    the other list drops containers like ``UISpecificTacticCubeActionViewMainContainer`` and
    crashes the engine. Detect by a signature container unique to the right column.
    """
    return '"SpecificInGameHUDScoreViewMainContainer"' in str(vertical_list)


def _replace_vertical_hud_elements(vertical_list: Any) -> None:
    """Replace right HUD list elements (no time row; nested containers for VIP axis rules)."""
    elements = vertical_list.by_m("Elements")
    while len(elements.v) > 0:
        elements.v.remove(elements.v[0])
    for element_ndf in _get_vertical_hud_element_blocks():
        elements.v.insert(len(elements.v), element_ndf)


def _get_m81_top_bar_row() -> str:
    """1020px bar with time panel starting immediately after the bar (not centered on it)."""
    return '''\
BUCKContainerDescriptor
(
    ElementName = "M81TopBarRow"
    ComponentFrame = TUIFramePropertyRTTI
    (
        RelativeWidthHeight = [1.0, 0.0]
        MagnifiableWidthHeight = [0.0, 40.0]
        AlignementToAnchor = [0.0, 0.0]
        AlignementToFather = [0.0, 0.0]
    )
    ClipContent = false
    Components =
    [
        BUCKContainerDescriptor
        (
            UniqueName = "barre_du_haut"
            ComponentFrame = TUIFramePropertyRTTI
            (
                MagnifiableWidthHeight = [1020.0, 40.0]
                AlignementToAnchor = [0.0, 0.0]
                AlignementToFather = [0.0, 0.0]
            )
            HasBackground = true
            BackgroundBlockColorToken = "M81_Ebony"
        ),
        BUCKContainerDescriptor
        (
            UniqueName = "SpecificInGameHUDTimePanelViewMainContainer"
            ComponentFrame = TUIFramePropertyRTTI
            (
                MagnifiableWidthHeight = [300.0, 40.0]
                MagnifiableOffset = [1020.0, 0.0]
                AlignementToAnchor = [0.0, 0.0]
                AlignementToFather = [0.0, 0.0]
            )
            Components =
            [
                PanelRoundedCorner
                (
                    ComponentFrame = TUIFramePropertyRTTI
                    (
                        RelativeWidthHeight = [1.0, 1.0]
                    )
                    FitStyle = ~/ContainerFitStyle/FitToContent
                    HasBackground = true
                    HasBorder = true
                    BackgroundBlockColorToken = "M81_MonochromeCRT"
                    BorderLineColorToken = "AppleIIc"
                    BorderThicknessToken = "1"
                    BackgroundLocalRenderLayer = 0
                    BorderLocalRenderLayer = 0
                    RoundedVertexes = [false, false, false, true]
                    Radius = 20
                ),
            ]
        ),
    ]
)'''


def _get_vertical_hud_element_blocks() -> tuple[str, ...]:
    """List element blocks: objectives, minimap, beacon, score (VIP-safe nested frames)."""
    return (
        '''\
BUCKListElementDescriptor
(
    ComponentDescriptor = BUCKContainerDescriptor
    (
        UniqueName = "InGameGlobalObjectivesContainer"
        ComponentFrame = TUIFramePropertyRTTI
        (
            RelativeWidthHeight = [1.0, 0.0]
        )
        FitStyle = ~/ContainerFitStyle/FitToContentVertically
    )
)''',
        '''\
BUCKListElementDescriptor
(
    ComponentDescriptor = BUCKContainerDescriptor
    (
        ComponentFrame = TUIFramePropertyRTTI
        (
            RelativeWidthHeight = [1.0, 0.0]
        )
        FitStyle = ~/ContainerFitStyle/FitToContentVertically
        Components =
        [
            BUCKContainerDescriptor
            (
                UniqueName = "UISpecificMiniMapInfoViewMainContainer"
                ComponentFrame = TUIFramePropertyRTTI
                (
                    RelativeWidthHeight = [1.0, 0.0]
                    MagnifiableOffset = [0.0, 10.0]
                )
                FitStyle = ~/ContainerFitStyle/FitToContentVertically
            ),
        ]
    )
)''',
        '''\
BUCKListElementDescriptor
(
    ComponentDescriptor = BUCKContainerDescriptor
    (
        ComponentFrame = TUIFramePropertyRTTI
        (
            RelativeWidthHeight = [1.0, 0.0]
        )
        FitStyle = ~/ContainerFitStyle/FitToContentVertically
        Components =
        [
            BUCKContainerDescriptor
            (
                UniqueName = "UICommonBeaconPanelViewMainContainer"
                ComponentFrame = TUIFramePropertyRTTI
                (
                    RelativeWidthHeight = [0.8312, 0.0]
                    AlignementToFather = [0.1688, 0.3]
                    AlignementToAnchor = [0.0, 0.0]
                )
                FitStyle = ~/ContainerFitStyle/FitToContentVertically
            ),
        ]
    )
)''',
        '''\
BUCKListElementDescriptor
(
    ComponentDescriptor = BUCKContainerDescriptor
    (
        ComponentFrame = TUIFramePropertyRTTI
        (
            RelativeWidthHeight = [1.0, 0.0]
        )
        FitStyle = ~/ContainerFitStyle/FitToContentVertically
        Components =
        [
            BUCKContainerDescriptor
            (
                UniqueName = "SpecificInGameHUDScoreViewMainContainer"
                ComponentFrame = TUIFramePropertyRTTI
                (
                    RelativeWidthHeight = [0.8312, 0.0]
                    AlignementToFather = [0.1688, 0.0]
                    AlignementToAnchor = [0.0, 0.0]
                    MagnifiableOffset = [0.0, 10.0]
                )
                FitStyle = ~/ContainerFitStyle/FitToContentVertically
            ),
        ]
    )
)''',
    )
