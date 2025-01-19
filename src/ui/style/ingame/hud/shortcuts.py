"""Functions for modifying UI HUD shortcuts for selection view."""
from src import ndf
from src.utils.logging_utils import setup_logger

logger = setup_logger(__name__)

def edit_uispecificshortcutsforselectionview(source_path) -> None:
    """Edit UISpecificShortcutsForSelectionView.ndf.
    
    Args:
        source: NDF file containing HUD shortcuts view definitions
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
    shortcutbutton_template.params.by_param("BorderLineColorToken").v = '"CouleurBordure_boutonShortcutsTextM81"'
    
    # Base hint button
    shortcutbuttonwithbasehint_template = source_path.by_namespace("ShortcutButtonWithBaseHint").v
    shortcutbuttonwithbasehint_template.by_member("TextureColorToken").v = '"CouleurTexture_boutonShortcutsTextM81"'
    
    # Strategic hint button
    shortcutbuttonwithstrategichint_template = source_path.by_namespace("ShortcutButtonWithStrategicHint").v
    shortcutbuttonwithstrategichint_template.params.by_param("BorderLineColorToken").v = '"CouleurBordure_boutonShortcutsTextM81"'
    
    logger.debug("Updated shortcut button templates")

def _update_main_component(source_path) -> None:
    """Update main component properties."""
    maincomponent = source_path.by_namespace("BUCKSpecificShortcutsForSelectionMainComponentDescriptor").v
    
    # Update background and border
    maincomponent.by_member("BackgroundBlockColorToken").v = '"M81_MonochromeCRT"'
    maincomponent.by_member("HasBorder").v = "true"
    maincomponent.insert(5, 'BorderThicknessToken = "2"')
    maincomponent.insert(6, 'BorderLineColorToken = "TypeG"')
    
    # Update corner properties
    maincomponent.insert(7, 'RoundedVertexes = [false, false, false, true]')
    maincomponent.insert(8, 'Radius = 20')
    
    logger.debug("Updated main component properties") 