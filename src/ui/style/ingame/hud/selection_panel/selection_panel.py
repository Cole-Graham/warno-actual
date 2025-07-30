"""Functions for modifying UI HUD unit selection panel view."""
from typing import Any

from src import ndf
from src.utils.logging_utils import setup_logger
from src.utils.ndf_utils import is_obj_type

logger = setup_logger(__name__)


def edit_uispecificunitselectionpanelview(source_path) -> None:
    """Edit UISpecificUnitSelectionPanelView.ndf.
    
    Args:
        source_path: NDF file containing HUD unit selection panel view definitions
    """
    logger.info("Editing UISpecificUnitSelectionPanelView.ndf")
    
    # Update deselection panel
    _update_deselection_panel(source_path)
    
    # Update selection panel name
    _update_selection_panel_name(source_path)
    
    # Update selection panel components
    _update_selection_panel_components(source_path)
    
    # Update fuel/supply display
    _update_fuel_supply_display(source_path)
    
    # Update unit name and type
    _update_unit_name_and_type(source_path)
    
    # Update shortcut button
    _update_shortcut_button(source_path)
    
    # Update ROE shortcuts panel
    _update_roe_shortcuts_panel(source_path)


def edit_uispecificsmartgroupselectionpanelview(source_path) -> None:
    """Edit UISpecificSmartGroupSelectionPanelView.ndf"""
    logger.info("Editing UISpecificSmartGroupSelectionPanelView.ndf")
    
    # Update smart group selection panel header
    _update_smartgrouppanelheadlist(source_path)
    
    # Update smart group selection main panel
    _update_smartgroupselectionpanelmainpanel(source_path)
    
    # Update smart group action button template
    _update_smartgroupactionbuttontemplate(source_path)
    
    # Update smart group label container
    _update_smartgrouplabelcontainer(source_path)
    
    logger.debug("Updated UISpecificSmartGroupSelectionPanelView.ndf")
    
def _update_smartgrouppanelheadlist(source_path) -> None:
    """SmartGroupPanelHeadList"""
    smartgrouppanelheadlist = source_path.by_namespace("SmartGroupPanelHeadList").v
    for element in smartgrouppanelheadlist.by_member("Elements").v:
        if isinstance(element.v, ndf.model.Object) and is_obj_type(element.v, "BUCKListElementDescriptor"):
            element_name = element.v.by_member("ElementName", False)
            if element_name is not None:
                if element_name.v == 'GroupName':
                    pass # placeholder for any future edits of GroupName element
                elif element_name.v == 'NbUnits':
                    element.v.by_member("TextColor").v = '"M81_AppleIIc"'

def _update_smartgroupselectionpanelmainpanel(source_path) -> None:
    """SmartGroupSelectionPanelMainPanel"""
    smartgroupselectionpanelmainpanel = source_path.by_namespace("SmartGroupSelectionPanelMainPanel").v
    backgroundcomponents = smartgroupselectionpanelmainpanel.by_member("BackgroundComponents").v
    for component in backgroundcomponents:
        if isinstance(component.v, ndf.model.Object) and is_obj_type(component.v, "PanelRoundedCorner"):
            component.v.by_member("BorderLineColorToken").v = '"M81_DarkCharcoalSelection"'
            component.v.by_member("BackgroundBlockColorToken").v = '"M81_DarkCharcoalTransparent"'
    
    logger.debug("Updated SmartGroupSelectionPanelMainPanel properties")
    
def _update_smartgroupactionbuttontemplate(source_path) -> None:
    """template SmartGroupActionButton"""
    smartgroupactionbuttontemplate = source_path.by_namespace("SmartGroupActionButton").v
    
    # edit template params
    template_params = smartgroupactionbuttontemplate.params
    template_params.by_param("ReinforceBackgroundBlockColorToken").v = '"BoutonTemps_Background_M81"'
    template_params.by_param("ReinforceBorderLineColorToken").v = '"BoutonTemps_Line_M81"'
    
    # edit template members
    components = smartgroupactionbuttontemplate.by_member("Components").v
    for component in components:
        if isinstance(component.v, ndf.model.Object):
            if is_obj_type(component.v, "BUCKContainerDescriptor"):
                pass # placeholder for any future edits of BUCKContainerDescriptor
            elif is_obj_type(component.v, "BUCKTextDescriptor"):
                component.v.by_member("TextColor").v = '"ButtonHUD/Text2_M81"'

def _update_smartgrouplabelcontainer(source_path) -> None:
    """SmartGroupLabelContainer"""
    smartgrouplabelcontainer = source_path.by_namespace("SmartGroupLabelContainer").v
    for component in smartgrouplabelcontainer.by_member("Components").v:
        if isinstance(component.v, ndf.model.Object):
            if is_obj_type(component.v, "SmartGroupActionButton"):
                component.v.by_member("ReinforceBackgroundBlockColorToken").v = '"BoutonTemps_Background_M81"'
                component.v.by_member("ReinforceBorderLineColorToken").v = '"BoutonTemps_Line_M81"'
            elif is_obj_type(component.v, "BUCKContainerDescriptor"):
                pass # placeholder for any future edits of BUCKContainerDescriptor
    
    logger.debug("Updated SmartGroupActionButton template properties")

def _update_deselection_panel(source_path) -> None:
    """Update deselection panel properties."""
    paneldeselectionunique = source_path.by_namespace("PanelDeSelectionUnique").v
    
    for component in paneldeselectionunique.by_member("BackgroundComponents").v:
        if not isinstance(component.v, ndf.model.Object) or not is_obj_type(component.v, "PanelRoundedCorner"):
            continue
            
        component.v.by_member("BackgroundBlockColorToken").v = '"M81_Artichoke"'
    
    logger.debug("Updated deselection panel colors")


def _update_selection_panel_name(source_path) -> None:
    """Update selection panel name properties."""
    panelselectionunique_nom = source_path.by_namespace("PanelSelectionUnique_Nom").v
    
    for component in panelselectionunique_nom.by_member("Components").v:
        if not isinstance(component.v, ndf.model.Object) or not is_obj_type(component.v, "PanelRoundedCorner"):
            continue
            
        _update_panel_properties(component.v)
    
    logger.debug("Updated selection panel name properties")


def _update_panel_properties(panel: Any) -> None:
    """Update panel properties."""
    panel.by_member("BorderLineColorToken").v = '"BoutonTemps_Line_M81"'
    panel.by_member("RoundedVertexes").v = "[false, false, false, true]"
    panel.add('HasBackground = true')
    panel.add('BackgroundBlockColorToken = "M81_DarkCharcoal"')
    panel.add('BorderThicknessToken = "1"')


def _update_selection_panel_components(source_path) -> None:
    """Update selection panel component properties."""
    # Update soldier name
    selectionpanel_nomsoldat = source_path.by_namespace("SelectionPanel_nomsoldat").v
    selectionpanel_nomsoldat.by_member("TextColor").v = '"M81_ArtichokeNearWhite"'
    
    # Update stress status
    _update_stress_status(source_path)
    
    logger.debug("Updated selection panel components")


def _update_stress_status(source_path) -> None:
    """Update stress status properties."""
    selectionpanelstressstatus = source_path.by_namespace("SelectionPanelStressStatus").v
    selectionpanelstressstatus.by_member("BackgroundBlockColorToken").v = '"M81_P3AmberOrange"'
    
    for component in selectionpanelstressstatus.by_member("Components").v:
        if not isinstance(component.v, ndf.model.Object) or not is_obj_type(component.v, "BUCKListDescriptor"):
            continue
            
        _update_stress_list(component.v)


def _update_stress_list(component: Any) -> None:
    """Update stress list properties."""
    component.by_member("HasBackground").v = "false"
    component.by_member("BackgroundBlockColorToken").v = '"M81_RedPhosphor"'
    component.insert(4, 'InterItemMargin = TRTTILength(Magnifiable = 2.0)')
    
    _update_stress_elements(component.by_member("Elements").v)


def _update_stress_elements(elements: Any) -> None:
    """Update stress elements properties."""
    for element in elements:
        if not isinstance(element.v, ndf.model.Object) or not is_obj_type(element.v, "BUCKListElementDescriptor"):
            continue
            
        component_descr = element.v.by_member("ComponentDescriptor").v
        if component_descr.type != "BUCKTextDescriptor":  # noqa
            continue
            
        _update_stress_text(component_descr)


def _update_stress_text(component: Any) -> None:
    """Update stress text properties."""
    if component.by_member("TextToken", False) is not None and component.by_member("TextToken").v == '"ST_MORAL"':
        for nested in component.by_member("Components").v:
            if not isinstance(nested.v, ndf.model.Object) or not is_obj_type(nested.v, "PanelRoundedCorner"):
                continue
                
            nested.v.by_member("RoundedVertexes").v = "[true, true, true, true]"
            nested.v.add('BackgroundBlockColorToken = "M81_Quincy"')
            nested.v.add('HasBackground = true')
    
    if component.by_member("ElementName", False) is not None and component.by_member("ElementName").v == "'StressStatus'":
        for nested in component.by_member("Components").v:
            if not isinstance(nested.v, ndf.model.Object) or not is_obj_type(nested.v, "PanelRoundedCorner"):
                continue
                
            nested.v.by_member("RoundedVertexes").v = "[true, true, true, true]"
            nested.v.add('BackgroundBlockColorToken = "PureBlack"')
            nested.v.add('HasBackground = true')
            nested.v.add('HasBorder = true')
            nested.v.add('BorderLineColorToken = "M81_P3AmberOrange"')


def _update_fuel_supply_display(source_path) -> None:
    """Update fuel/supply display properties."""
    affichagefuelorsupply = source_path.by_namespace("AffichageFuelOrSupply").v
    
    for component in affichagefuelorsupply.by_member("Components").v:
        if not isinstance(component.v, ndf.model.Object) or not is_obj_type(component.v, "BUCKListDescriptor"):
            continue
            
        _update_fuel_supply_list(component.v)
    
    logger.debug("Updated fuel/supply display properties")


def _update_fuel_supply_list(component: Any) -> None:
    """Update fuel/supply list properties."""
    component.by_member("InterItemMargin").v = "TRTTILength(Magnifiable = 2.0)"
    
    for element in component.by_member("Elements").v:
        if not isinstance(element.v, ndf.model.Object) or not is_obj_type(element.v, "BUCKListElementDescriptor"):
            continue
            
        component_descr = element.v.by_member("ComponentDescriptor").v
        if component_descr.type != "BUCKTextDescriptor":  # noqa
            continue
            
        if component_descr.by_member("ElementName", False) is not None:  # noqa
            if component_descr.by_member("ElementName").v == "'RemainingFuelOrSupply'":  # noqa
                component_descr.by_member("TextColor").v = '"M81_ArtichokeNearWhite"'  # noqa


def _update_unit_name_and_type(source_path) -> None:
    """Update unit name and type properties."""
    # Update unit name
    selectionpanelunitname = source_path.by_namespace("SelectionPanelUnitName").v
    selectionpanelunitname.by_member("TextColor").v = '"M81_ArtichokeVeryLight"'
    
    # Update HP display
    _update_hp_display(source_path)
    
    # Update unit type name
    selectionpanelunittypename = source_path.by_namespace("SelectionPanelUnitTypeName").v
    selectionpanelunittypename.by_member("TextColor").v = '"M81_ArtichokeNearWhite"'
    
    logger.debug("Updated unit name and type properties")


def _update_hp_display(source_path) -> None:
    """Update HP display properties."""
    affichagepv = source_path.by_namespace("AffichagePV").v
    affichagepv.by_member("BorderLineColorToken").v = '"AppleIIc"'
    affichagepv.by_member("BackgroundBlockColorToken").v = '"PureBlack"'
    affichagepv.by_member("GraduationColorToken").v = '"AppleIIc"'
    
    for component in affichagepv.by_member("Components").v:
        if not isinstance(component.v, ndf.model.Object) or not is_obj_type(component.v, "BUCKGaugeValueDescriptor"):
            continue
            
        component.v.by_member("BackgroundBlockColorToken").v = '"TypeG"'


def _update_shortcut_button(source_path) -> None:
    """Update shortcut button properties."""
    shortcutbuttondescriptor_template = source_path.by_namespace("ShortcutButtonDescriptor").v
    
    for component in shortcutbuttondescriptor_template.by_member("Components").v:
        if not isinstance(component.v, ndf.model.Object) or not is_obj_type(component.v, "BUCKContainerDescriptor"):
            continue
            
        _update_shortcut_container(component.v)
    
    logger.debug("Updated shortcut button properties")


def _update_shortcut_container(container: Any) -> None:
    """Update shortcut container properties."""
    for component in container.by_member("Components").v:
        if not isinstance(component.v, ndf.model.Object) or not is_obj_type(component.v, "PanelRoundedCorner"):
            continue
            
        component.v.by_member("BackgroundBlockColorToken").v = '"BoutonTemps_Background_M81"'
        component.v.by_member("BorderLineColorToken").v = '"BoutonTemps_Line_M81"'


def _update_roe_shortcuts_panel(source_path) -> None:
    """Update ROE shortcuts panel properties."""
    panelselectionunique_roeshortcuts = source_path.by_namespace("PanelSelectionUnique_RoeShortcuts").v
    panelselectionunique_roeshortcuts.by_member("BackgroundBlockColorToken").v = '"M81_Artichoke"'
    panelselectionunique_roeshortcuts.by_member("BorderLineColorToken").v = '"BoutonTemps_Line_M81"'
    
    for component in panelselectionunique_roeshortcuts.by_member("Components").v:
        if not isinstance(component.v, ndf.model.Object) or not is_obj_type(component.v, "BUCKTextDescriptor"):
            continue
            
        component.v.by_member("TextColor").v = '"M81_DarkCharcoal"'
    
    logger.debug("Updated ROE shortcuts panel properties")
