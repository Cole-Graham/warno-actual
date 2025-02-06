"""Functions for modifying UI launch battle button resources."""
from typing import Any

from src import ndf
from src.utils.dictionary_utils import write_dictionary_entries
from src.utils.logging_utils import setup_logger
from src.utils.ndf_utils import is_obj_type

logger = setup_logger(__name__)


def edit_uiingamelaunchbattlebuttonresources(source_path) -> None:
    """Edit UIInGameLaunchBattleButtonResources.ndf."""
    logger.info("Editing UIInGameLaunchBattleButtonResources.ndf")
    
    # Update deployment phase panel
    _update_deployment_phase_panel(source_path)
    
    # Add FOB reminder text
    _add_fob_reminder_text(source_path)
    
    # Update launch button cancel
    _update_launch_button_cancel(source_path)


def _update_deployment_phase_panel(source_path) -> None:
    """Update deployment phase panel properties."""
    deploymentphasepanel = source_path.by_namespace("DeploymentPhasePanel").v
    
    for component in deploymentphasepanel.by_member("Components").v:
        if not isinstance(component.v, ndf.model.Object):
            continue
            
        if is_obj_type(component.v, "PanelRoundedCorner"):
            component.v.by_member("BackgroundBlockColorToken").v = '"M81_Ebony128"'
            component.v.by_member("BorderLineColorToken").v = '"M81_EbonyLight"'
        elif is_obj_type(component.v, "BUCKContainerDescriptor"):
            component.v.by_member("BorderLineColorToken").v = '"M81_Artichoke191"'
        elif is_obj_type(component.v, "BUCKTextDescriptor"):
            _update_text_properties(component.v)
        elif is_obj_type(component.v, "BUCKListDescriptor"):
            componentframe = component.v.by_member("ComponentFrame").v
            componentframe.by_member("MagnifiableOffset").v = "[0.0, 35.0]"  # noqa
    
    logger.debug("Updated deployment phase panel properties")


def _update_text_properties(component: Any) -> None:
    """Update text component properties."""
    component.by_member("TextColor").v = '"M81_DarkCharcoal"'
    component.by_member("BackgroundBlockColorToken").v = '"M81_Artichoke191"'
    component.by_member("BorderLineColorToken").v = '"M81_Artichoke"'


def _add_fob_reminder_text(source_path) -> None:
    """Add FOB reminder text component and localization."""
    deploymentphasepanel = source_path.by_namespace("DeploymentPhasePanel").v
    components = deploymentphasepanel.by_member("Components").v
    
    # Add new text component
    components.insert(2, _get_fob_reminder_template())
    logger.debug("Added FOB reminder text component")
    
    # Add localization entry
    write_dictionary_entries({"BUYFOB": "Buy your FOB(s) first, so you don't forget!!!"}, "ingame")
    logger.debug("Added FOB reminder text to dictionary")


def _update_launch_button_cancel(source_path) -> None:
    """Update launch button cancel properties."""
    launchbuttoncanceldescriptor = source_path.by_namespace("LaunchButtonCancelDescriptor").v
    launchbuttoncanceldescriptor.by_member("TextColor").v = '"DeploymentPhase/CancelTimerM81"'
    logger.debug("Updated launch button cancel color")


def _get_fob_reminder_template() -> str:
    """Get FOB reminder text component template."""
    return '''\
BUCKTextDescriptor
(
    ComponentFrame = TUIFramePropertyRTTI
    (
        MagnifiableWidthHeight = [DeploymentPhasePanelWidth - 13.0, 14.0]
        MagnifiableOffset = [0.0, 116.0]
        AlignementToFather = [0.5, 0.0]
        AlignementToAnchor = [0.5, 0.0]
    )
    HorizontalFitStyle = ~/FitStyle/UserDefined
    VerticalFitStyle = ~/FitStyle/UserDefined
    TextStyle = 'Default'
    TextToken = 'BUYFOB'
    TypefaceToken = "UIMainFont"
    TextDico = ~/LocalisationConstantes/dico_interface_ingame
    TextColor = 'M81_DarkCharcoal'
    TextSize = "11"
    HasBackground = true
    BackgroundBlockColorToken = 'M81_Artichoke191'
    ParagraphStyle = TParagraphStyle
    (
        Alignment = UIText_Center
        VerticalAlignment = UIText_VerticalCenter
    )
    HasBorder = true
    BorderLineColorToken = 'M81_Artichoke'
    BorderThicknessToken = '3'
    BordersToDraw = ~/TBorderSide/Top
)'''
