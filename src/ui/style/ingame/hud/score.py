"""Functions for modifying UI HUD score view."""
from typing import Any

from src import ndf
from src.utils.logging_utils import setup_logger
from src.utils.ndf_utils import is_obj_type

logger = setup_logger(__name__)


def edit_uispecifichudscoreview(source_path) -> None:
    """Edit UISpecificHUDScoreView.ndf."""
    logger.info("Editing UISpecificHUDScoreView.ndf")
    
    _update_alliance_score_line(source_path)
    _update_player_score_line(source_path)
    _update_player_score_panel_button(source_path)


def _update_alliance_score_line(source_path) -> None:
    """Update alliance score line properties."""
    alliancescoreline = source_path.by_namespace("AllianceScoreLine").v
    for component in alliancescoreline.by_member("Components").v:
        if not isinstance(component.v, ndf.model.Object) or not is_obj_type(component.v, "BUCKListDescriptor"):
            continue
            
        for element in component.v.by_member("Elements").v:
            if not isinstance(element.v, ndf.model.Object) or not is_obj_type(element.v, "BUCKListElementDescriptor"):
                continue
                
            container = element.v.by_member("ComponentDescriptor").v
            if container.type != "BUCKContainerDescriptor":  # noqa
                continue
                
            _update_score_container(container)


def _update_score_container(container: Any) -> None:
    """Update score container and its nested components."""
    if container.by_member("ElementName", False) is not None:
        elementname = container.by_member("ElementName").v
        if elementname == '<ElementName> + "PreGaugeContainer"':
            container.by_member("BackgroundBlockColorToken").v = '"PanelScore/ScoreBackgroundM81"'
            container.add("HasBorder = true")
            container.add('BorderLineColorToken = "M81_ArtichokeVeryLight"')
            
            for component in container.by_member("Components").v:
                if not isinstance(component.v, ndf.model.Object) or not is_obj_type(component.v, "BUCKTextureDescriptor"):
                    continue
                component.v.by_member("TextureColorToken").v = '"M81_WhiteText95"'
    else:
        for component in container.by_member("Components").v:
            if not isinstance(component.v, ndf.model.Object):
                continue
                
            if is_obj_type(component.v, "BUCKGaugeDescriptor"):
                elementname = component.v.by_member("ElementName").v
                if elementname == '<ElementName> + "Gauge"':
                    component.v.by_member("BackgroundBlockColorToken").v = '"PanelScore/ScoreBackgroundM81"'
                    component.v.add("HasBorder = true")
                    component.v.add('BorderLineColorToken = "M81_ArtichokeVeryLight"')
            
            elif is_obj_type(component.v, "BUCKListDescriptor"):
                _update_text_elements(component.v.by_member("Elements").v)


def _update_text_elements(elements: Any) -> None:
    """Update text element colors."""
    for element in elements:
        if not isinstance(element.v, ndf.model.Object) or not is_obj_type(element.v, "BUCKListElementDescriptor"):
            continue
            
        text_descr = element.v.by_member("ComponentDescriptor").v
        if text_descr.type != "BUCKTextDescriptor":  # noqa
            continue
            
        elementname = text_descr.by_member("ElementName").v  # noqa
        if elementname in ['<ElementName> + "Text"', '<ElementName> + "IncomeText"', '<ElementName> + "VictoryTimer"']:
            text_descr.by_member("TextColor").v = '"M81_WhiteText95"'  # noqa


def _update_player_score_line(source_path) -> None:
    """Update player score line properties."""
    playerscoreline = source_path.by_namespace("BUCKSpecificHUDScorePlayerOneLine").v
    for element in playerscoreline.by_member("Elements").v:
        if not isinstance(element.v, ndf.model.Object) or not is_obj_type(element.v, "BUCKListElementDescriptor"):
            continue
            
        component = element.v.by_member("ComponentDescriptor").v
        if component.type == "BUCKSpecificTextWithHint":  # noqa
            component.by_member("TextColor").v = '"BlancEquipe"'  # noqa
            component.by_member("TypefaceToken").v = '"Bombardier"'  # noqa
        elif component.type == "BUCKTextDescriptor" and component.by_member("ElementName", False) is not None:  # noqa
            if component.by_member("ElementName").v == '"Points"':  # noqa
                component.by_member("TextColor").v = '"M81_ArtichokeVeryLight"'  # noqa
        elif component.type == "BUCKButtonDescriptor":  # noqa
            for nested in component.by_member("Components").v:  # noqa
                if not isinstance(nested.v, ndf.model.Object) or not is_obj_type(nested.v, "BUCKTextureDescriptor"):
                    continue
                nested.v.by_member("TextureColorToken").v = '"CouleurTexture_boutonShortcutsTextM81"'


def _update_player_score_panel_button(source_path) -> None:
    """Update player score panel button properties."""
    panelbutton = source_path.by_namespace("PlayerScorePanelButton").v
    for component in panelbutton.by_member("Components").v:
        if not isinstance(component.v, ndf.model.Object) or not is_obj_type(component.v, "BUCKButtonDescriptor"):
            continue
            
        component.v.by_member("DefaultToggleValue").v = "true"
        for nested in component.v.by_member("Components").v:
            if not isinstance(nested.v, ndf.model.Object):
                continue
                
            if is_obj_type(nested.v, "BUCKContainerDescriptor"):
                for panel in nested.v.by_member("Components").v:
                    if not isinstance(panel.v, ndf.model.Object) or not is_obj_type(panel.v, "PanelRoundedCorner"):
                        continue
                    panel.v.by_member("BackgroundBlockColorToken").v = '"BoutonTemps_BackgroundM81"'
                    panel.v.by_member("BorderLineColorToken").v = '"CouleurBordure_boutonShortcutsTextM81"'
            elif is_obj_type(nested.v, "BUCKTextureDescriptor"):
                nested.v.by_member("TextureColorToken").v = '"CouleurTexture_boutonShortcutsTextM81"'
