"""Functions for modifying UI engagement rules."""
from typing import Any, List, Tuple

from src import ndf
from src.utils.logging_utils import setup_logger
from src.utils.ndf_utils import is_obj_type

logger = setup_logger(__name__)


def edit_uiingamebuckengagementrules(source_path) -> None:
    """Edit UIInGameBUCKEngagementRules.ndf.
    
    Args:
        source_path: NDF file containing engagement rules definitions
    """
    logger.info("Editing UIInGameBUCKEngagementRules.ndf")
    
    # Update engagement button properties
    _update_engagement_button(source_path)
    
    # Update engagement rules view
    _update_engagement_rules_view(source_path)


def _update_engagement_button(source_path) -> None:
    """Update engagement button properties."""
    engagementbuttondescriptor_template = source_path.by_namespace("EngagementButtonDescriptor").v
    
    for component in engagementbuttondescriptor_template.by_member("Components").v:
        if not isinstance(component.v, ndf.model.Object) or not is_obj_type(component.v, "PanelRoundedCorner"):
            continue
            
        component.v.by_member("BackgroundBlockColorToken").v = '"BoutonTempsBlockM81"'
        component.v.by_member("BorderLineColorToken").v = '"BoutonTempsTextM81"'
    
    logger.debug("Updated engagement button colors")


def _update_engagement_rules_view(source_path) -> None:
    """Update engagement rules view properties."""
    tacticengagementrulesview_descr = source_path.by_namespace("UISpecificTacticEngagementRulesViewDescriptor").v
    
    # Update category component
    categorycomponent = tacticengagementrulesview_descr.by_member("CategoryComponent").v
    categorycomponent.by_member("BackgroundBlockColorToken").v = '"M81_Artichoke"'
    
    # Update button colors
    _update_engagement_buttons(tacticengagementrulesview_descr.by_member("CategoryToButtons").v)
    
    logger.debug("Updated engagement rules view properties")


def _update_engagement_buttons(categorytobuttons_map: Any) -> None:
    """Update engagement button colors."""
    buttonstype_elementname: List[Tuple[str, str]] = [
        ("EngagementAdvance", "EngagementAdvance_Hunt"),
        ("EngagementUseRoad", "EngagementUseRoad_True"),
        ("EngagementSmartMove", "EngagementSmartMove_False"),
        ("EngagementIdleBehavior", "EngagementIdleBehavior_AutoCover"),
        ("EngagementAutoResale", "EngagementAutoResale_True"),
        ("EngagementUnarmedVehiculeBehavior", "EngagementUnarmedVehiculeBehavior_FireAtWill"),
        ("EngagementOutrangedShotReaction", "OutrangedShotReaction_Defensive"),
        ("EngagementMissilesBehavior", "EngagementMissilesBehavior_LookAtNonEmptyTransport"),
    ]
    
    for buttonstype, elementname in buttonstype_elementname:
        buttons = categorytobuttons_map.by_key(f'"{buttonstype}"').v
        engagementbuttons = buttons.by_member("EngagementButtons").v
        
        for row in engagementbuttons:
            if not isinstance(row.v, ndf.model.Object) or not is_obj_type(row.v, "EngagementButtonDescriptor"):
                continue
                
            if row.v.by_member("ElementName").v == f'"{elementname}"':
                row.v.by_member("TextColor").v = '"M81_RoE_Default"'
                logger.debug(f"Updated text color for {elementname}")
