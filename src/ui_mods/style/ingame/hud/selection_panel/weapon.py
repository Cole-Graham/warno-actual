"""Functions for modifying UI HUD unit selection weapon panel view."""
from typing import Any

from src import ndf
from src.utils.logging_utils import setup_logger
from src.utils.ndf_utils import is_obj_type

logger = setup_logger(__name__)


def edit_uispecificunitselectionweaponpanelview(source_path) -> None:
    """Edit UISpecificUnitSelectionWeaponPanelView.ndf.
    
    Args:
        source_path: NDF file containing HUD unit selection weapon panel view definitions
    """
    logger.info("Editing UISpecificUnitSelectionWeaponPanelView.ndf")
    
    # Update weapon information
    _update_weapon_information(source_path)
    
    # Update weapon button overblock
    _update_weapon_button_overblock(source_path)
    
    # Update weapon status
    _update_weapon_status(source_path)


def _update_weapon_information(source_path) -> None:
    """Update weapon information properties."""
    weaponinformation_template = source_path.by_namespace("WeaponInformation").v
    weaponinformation_template.by_member("BorderThicknessToken").v = '"1"'
    logger.debug("Updated weapon information border")


def _update_weapon_button_overblock(source_path) -> None:
    """Update weapon button overblock properties."""
    weaponpanelweaponbuttonoverblock = source_path.by_namespace("WeaponPanelWeaponButtonOverblock").v
    weaponpanelweaponbuttonoverblock.by_member("BackgroundBlockColorToken").v = '"WeaponButton/Overblock_M81"'
    logger.debug("Updated weapon button overblock color")


def _update_weapon_status(source_path) -> None:
    """Update weapon status properties."""
    weaponpanelweaponstatus = source_path.by_namespace("WeaponPanelWeaponStatus").v
    weaponpanelweaponstatus.by_member("BackgroundBlockColorToken").v = '"M81_ArtichokeTransparent"'
    
    for component in weaponpanelweaponstatus.by_member("Components").v:
        if not isinstance(component.v, ndf.model.Object) or not is_obj_type(component.v, "BUCKListDescriptor"):
            continue
            
        _update_weapon_status_elements(component.v.by_member("Elements").v)
    
    logger.debug("Updated weapon status properties")


def _update_weapon_status_elements(elements: Any) -> None:
    """Update weapon status element properties."""
    for element in elements:
        if not isinstance(element.v, ndf.model.Object) or not is_obj_type(element.v, "BUCKListElementDescriptor"):
            continue
            
        component_descr = element.v.by_member("ComponentDescriptor").v
        if component_descr.type == "BUCKChronoAnimatedTextureDescriptor":  # noqa
            component_descr.by_member("ChronoForegroundColor").v = '"M81_AppleIIc"'  # noqa
