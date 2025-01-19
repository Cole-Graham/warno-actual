"""Functions for modifying UI hint views."""
from src import ndf
from src.utils.logging_utils import setup_logger
from src.utils.ndf_utils import is_obj_type

logger = setup_logger(__name__)

def edit_buckspecifichint(source_path) -> None:
    """Edit BuckSpecificHint.ndf.
    
    Args:
        source: NDF file containing hint view definitions
    """
    logger.info("Editing BuckSpecificHint.ndf")
    
    # Update hint component colors and properties
    hintingamebuckcomponent = source_path.by_namespace("HintInGameBUCKComponent").v
    hintingamebuckcomponent.params.by_param("BackgroundBlockColorToken").v = '"M81_Ebony"'
    hintingamebuckcomponent.params.by_param("BorderLineColorToken").v = '"M81_Artichoke"'
    logger.debug("Updated hint component colors")
    
    # Update background panel properties
    bg_components = hintingamebuckcomponent.by_member("ListBackgroundComponents").v
    for component in bg_components:
        if not isinstance(component.v, ndf.model.Object):
            continue
            
        if is_obj_type(component.v, "PanelRoundedCorner"):
            roundedpanel = component.v
            roundedpanel.by_member("RoundedVertexes").v = "[false, false, false, false]"
            logger.debug("Updated hint panel rounded vertices") 