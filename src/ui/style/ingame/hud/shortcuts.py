"""Functions for modifying UI HUD shortcuts for selection view."""
# from src import ndf
from src.utils.logging_utils import setup_logger

logger = setup_logger(__name__)


def edit_uispecificshortcutsforselectionview(source_path) -> None:
    """Edit UISpecificShortcutsForSelectionView.ndf.
    
    Args:
        source_path: NDF file containing HUD shortcuts view definitions
    """
    logger.info("Editing UISpecificShortcutsForSelectionView.ndf")
    
    # Update shortcut button templates
    _update_shortcut_button_templates(source_path)
    
    # Update main component
    _update_main_component(source_path)


def _update_shortcut_button_templates(source_path) -> None:
    """Update shortcut button template properties."""
    # Basic shortcut button
    shortcutbutton_template = source_path.by_namespace("ShortcutButton").v
    shortcutbutton_template.params.by_param("BackgroundBlockColorToken").v = '"Transparent"'
    shortcutbutton_template.params.by_param("BorderLineColorToken").v = '"CouleurBordure_boutonShortcuts_M81"'
    
    # Base hint button
    shortcutbuttonwithbasehint_template = source_path.by_namespace("ShortcutButtonWithBaseHint").v
    index = source_path.by_namespace("ShortcutButtonWithBaseHint").index
    shortcutbuttonwithbasehint_template.by_member("TextureColorToken").v = '"CouleurTexture_boutonShortcuts_M81"'
    
    shortcuttogglebuttonwithbasehint_template = (
        f'template ShortcutToggleButtonWithBaseHint'
        f'['
        f'    ElementName: string = "",'
        f'    TextureToken: string = "",'
        f'    HintTitleToken: string = "",'
        f'    HintBodyToken: string = "",'
        f'    HintExtendedToken: string = "",'
        f'    MagnifiableWidthHeightTexture: float2 = [30.0, 30.0]'
        f'] is ShortcutButton'
        f'('
        f'    ElementName = <ElementName>'
        f'    MagnifiableWidthHeightTexture = <MagnifiableWidthHeightTexture>'
        f'    TextureToken = <TextureToken>'
        f'    TextureColorToken = "CouleurTexture_boutonShortcuts_toggle_M81"'
        f'    BorderLineColorToken = "CouleurBordure_boutonShortcuts_toggle_M81"'
        f'    HintableAreaComponent = BUCKSpecificHintableArea'
        f'    ('
        f'        HintTitleToken = <HintTitleToken>'
        f'        HintBodyToken = <HintBodyToken>'
        f'        HintExtendedToken = <HintExtendedToken>'
        f'        DicoToken = ~/LocalisationConstantes/dico_interface_ingame'
        f'    )'
        f')'
    )
    source_path.insert(index, shortcuttogglebuttonwithbasehint_template)
    
    # Strategic hint button
    shortcutbuttonwithstrategichint_template = source_path.by_namespace("ShortcutButtonWithStrategicHint").v
    shortcutbuttonwithstrategichint_template.params.by_param("BorderLineColorToken").v = '"CouleurBordure_boutonShortcuts_M81"'
    
    # OrderPanelButton
    orderpanelpaneltogglebutton = (
        f'OrderPanelPanelButton is ShortcutToggleButtonWithBaseHint'
        f'('
        f'    ElementName = "OrdersFeedBackButton"'
        f'    TextureToken = "textureOrders"'
        f'    HintTitleToken = "HSL_ORDERT"'
        f'    HintBodyToken = "HSL_ORDERB"'
        f')'
    )
    orderpanelbutton_index = source_path.by_namespace("OrderPanelPanelButton").index
    source_path.replace(orderpanelbutton_index, orderpanelpaneltogglebutton)
    
    # LoSPanelButton
    lospaneltogglebutton = (
        f'LoSPanelButton is ShortcutToggleButtonWithBaseHint'
        f'('
        f'    ElementName = "LoSFeedBackButton"'
        f'    TextureToken = "icone_los"'
        f'    HintTitleToken = "HSL_ULOSBT"'
        f'    HintBodyToken = "HSL_ULOSBB"'
        f'    HintExtendedToken = "HSL_ULOSBE"'
        f'    MagnifiableWidthHeightTexture = [52.0, 32.0]'
        f')'
    )
    lospanelbutton_index = source_path.by_namespace("LoSPanelButton").index
    source_path.replace(lospanelbutton_index, lospaneltogglebutton)
    
    logger.debug("Updated shortcut button templates")


def _update_main_component(source_path) -> None:
    """Update main component properties."""
    maincomponent = source_path.by_namespace("BUCKSpecificShortcutsForSelectionMainComponentDescriptor").v
    
    # Update background and border
    maincomponent.by_member("BackgroundBlockColorToken").v = '"M81_MonochromeCRT"'
    maincomponent.by_member("HasBorder").v = "true"
    maincomponent.insert(5, 'BorderThicknessToken = "2"')
    maincomponent.insert(6, 'BorderLineColorToken = "M81_TypeG"')
    
    # Update corner properties
    maincomponent.insert(7, 'RoundedVertexes = [false, true, false, false]')
    maincomponent.insert(8, 'Radius = 20')
    
    logger.debug("Updated main component properties")
