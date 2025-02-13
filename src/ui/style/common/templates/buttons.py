"""Functions for modifying UI button templates."""
from src import ndf
from src.utils.logging_utils import setup_logger
from src.utils.ndf_utils import is_obj_type

logger = setup_logger(__name__)


def edit_buckspecificbuttons(source_path) -> None:
    """Edit BuckSpecificButtons.ndf.
    
    Args:
        source_path: NDF file containing button template definitions
    """
    logger.info("Editing BuckSpecificButtons.ndf")
    
    # Update BoutonFulda colors
    boutonfulda = source_path.by_namespace("BoutonFulda").v
    boutonfulda.params.by_param("BackgroundColor").v = '"BoutonTemps_BackgroundM81"'
    boutonfulda.params.by_param("LineBorderColor").v = '"BoutonTemps"'
    logger.debug("Updated BoutonFulda colors")
    
    # Update BoutonFulda_AvecIcone colors
    boutonfulda_avecicone = source_path.by_namespace("BoutonFulda_AvecIcone").v
    for component in boutonfulda_avecicone.by_member("Components").v:
        if not isinstance(component.v, ndf.model.Object):
            continue
            
        if is_obj_type(component.v, "BUCKContainerDescriptor"):
            nested_components = component.v.by_member("Components").v
            for row in nested_components:
                if is_obj_type(row.v, "PanelRoundedCorner"):
                    roundedpanel = row.v
                    
                    # Set background color based on strategic mode
                    bg_colortoken = '(<IsFromStrategic> == true ? "SM_RifleGreen_75" : "BoutonFlaresBlockM81")'
                    roundedpanel.by_member("BackgroundBlockColorToken").v = bg_colortoken
                    
                    # Set border color based on strategic mode
                    border_colortoken = '(<IsFromStrategic> == true ? "SM_Grullo" : "BoutonTemps")'
                    roundedpanel.by_member("BorderLineColorToken").v = border_colortoken
                    
                    logger.debug("Updated BoutonFulda_AvecIcone panel colors")
    
    # Update BUCKSpecificButton colors
    buckspecificbutton = source_path.by_namespace("BUCKSpecificButton").v
    buckspecificbutton.params.by_param("PanelRoundedCorner_BorderLineColorToken").v = '"BoutonTemps"'
    buckspecificbutton.params.by_param("PanelRoundedCorner_BackgroundBlockColorToken").v = '"BoutonTemps_BackgroundM81"'
    logger.debug("Updated BUCKSpecificButton colors")
    
    # Update HUDButton properties
    hudbutton = source_path.by_namespace("HUDButton").v
    
    # Add default toggle value parameter
    new_param = "DefaultToggleValue : bool = false"
    index = hudbutton.params.by_param("IsTogglable").index + 1
    hudbutton.params.insert(index, new_param)
    
    # Update visual properties
    hudbutton.params.by_param("HasBorder").v = "false"
    hudbutton.params.by_param("BorderLineColorToken").v = '""'
    hudbutton.params.by_param("HasBackground").v = "false" 
    hudbutton.params.by_param("BackgroundColorToken").v = '""'
    hudbutton.params.by_param("ForegroundTexture").v = '""'
    hudbutton.params.by_param("BackgroundTexture").v = '""'
    logger.debug("Updated HUDButton properties")
