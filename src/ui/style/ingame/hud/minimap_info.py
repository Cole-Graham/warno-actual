"""Functions for modifying UI HUD minimap info view."""
from src import ndf
from src.utils.logging_utils import setup_logger
from src.utils.ndf_utils import is_obj_type

logger = setup_logger(__name__)


def edit_uispecificminimapinfoview(source_path) -> None:
    """Edit UISpecificMiniMapInfoView.ndf."""
    logger.info("Editing UISpecificMiniMapInfoView.ndf")
    
    # Update minimap size
    source_path.by_namespace("MinimapMagnifiableSize").v = "380.0"
    logger.debug("Updated minimap size") 
    
    main_component = source_path.by_namespace("BUCKSpecificMiniMapInfoMainComponentDescriptor").v
    components = main_component.by_member("Components")
    for component in components.v:
        if not isinstance(component.v, ndf.model.Object):
            continue
        if is_obj_type(component.v, "PanelRoundedCorner"):
            components.v.remove(component)
