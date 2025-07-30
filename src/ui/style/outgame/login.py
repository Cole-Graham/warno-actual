"""Out-game login UI."""

from typing import Any, Dict

from src import ndf
from src.utils.logging_utils import setup_logger
from src.utils.ndf_utils import is_obj_type

logger = setup_logger(__name__)

def edit_uispecificloginview(source_path) -> None:
    """Edit UISpecificLoginView.ndf."""
    logger.info("Editing UISpecificLoginView.ndf")
    
    loginpanelline_template = source_path.by_namespace("LoginPanelLine").v
    
    elements = loginpanelline_template.by_member("Elements").v
    
    for element in elements:
        if not isinstance(element.v, ndf.model.Object) or not is_obj_type(element.v, "BUCKListElementDescriptor"):
            continue
            
        component_descr = element.v.by_member("ComponentDescriptor").v
        if component_descr.type != "BUCKContainerDescriptor":  # noqa
            continue
        
        components = component_descr.by_member("Components").v
        for component in components:
            if not isinstance(component.v, ndf.model.Object):
                continue
            
            if is_obj_type(component.v, "BUCKEditableTextDescriptor"):
                component.v.by_member("SelectionColorToken").v = '"DeckOverview/CaseGrisee/EditableText/Selected_M81"'
                
def edit_uispecificoutgamerecoverloginview(source_path) -> None:
    """Edit UISpecificOutGameRecoverLoginView.ndf."""
    logger.info("Editing UISpecificOutGameRecoverLoginView.ndf")
    
    ecrangauchetexteditable_template = source_path.by_namespace("EcranGaucheTextEditable").v
    components = ecrangauchetexteditable_template.by_member("Components").v
    
    for component in components:
        if not isinstance(component.v, ndf.model.Object):
            continue
            
        if is_obj_type(component.v, "BUCKListDescriptor"):
            elements = component.v.by_member("Elements").v
            for element in elements:
                if not isinstance(element.v, ndf.model.Object):
                    continue
                    
                if is_obj_type(element.v, "BUCKListElementDescriptor"):
                    component_descr = element.v.by_member("ComponentDescriptor").v
                    if component_descr.type == "BUCKEditableTextDescriptor":  # noqa
                        component.v.by_member("SelectionColorToken").v = '"DeckOverview/CaseGrisee/EditableText/Selected_M81"'
                        
def edit_uispecificoutgamerecoverpasswordview(source_path) -> None:
    """Edit UISpecificOutGameRecoverPasswordView.ndf."""
    logger.info("Editing UISpecificOutGameRecoverPasswordView.ndf")
    
    recoverpasswordline_template = source_path.by_namespace("RecoverPasswordLine").v
    elements = recoverpasswordline_template.by_member("Elements").v
    
    for element in elements:
        if not isinstance(element.v, ndf.model.Object) or not is_obj_type(element.v, "BUCKListElementDescriptor"):
            continue
            
        component_descr = element.v.by_member("ComponentDescriptor").v
        if component_descr.type == "BUCKEditableTextDescriptor":  # noqa
            component_descr.v.by_member("SelectionColorToken").v = '"DeckOverview/CaseGrisee/EditableText/Selected_M81"'
            