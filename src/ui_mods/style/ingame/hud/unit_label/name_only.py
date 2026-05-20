"""Functions for modifying UI HUD unit label view name only."""
from typing import Any

from src import ndf
from src.utils.logging_utils import setup_logger
from src.utils.ndf_utils import is_obj_type

logger = setup_logger(__name__)


def edit_uispecificunitlabelviewnameonly(source_path) -> None:
    """Edit UISpecificUnitLabelViewNameOnly.ndf.

    Args:
        source_path: NDF file containing HUD unit label view name only definitions
    """
    logger.info("Editing UISpecificUnitLabelViewNameOnly.ndf")

    _update_unit_name_and_right_list(source_path)
    _replace_upper_label_name_only(source_path)


def _update_unit_name_and_right_list(source_path) -> None:
    """Update unit name and right list properties."""
    unitnameandrightlistnameonly = source_path.by_namespace("UnitNameAndRightListNameOnly").v

    componentframe = unitnameandrightlistnameonly.by_member("ComponentFrame").v
    componentframe.add('MagnifiableOffset = [0.0, ~/ReticleMagnifiableSize * -5.5]')
    unitnameandrightlistnameonly.by_member("FitStyle").v = "~/ContainerFitStyle/MaxBetweenUserDefinedAndContent"

    unitnameandrightlistnameonly.insert(3, 'BorderLocalRenderLayer = 4')
    unitnameandrightlistnameonly.insert(4, 'BackgroundLocalRenderLayer = 4')

    _update_list_components(unitnameandrightlistnameonly.by_member("Components").v)

    logger.debug("Updated unit name and right list properties")


def _update_list_components(components: Any) -> None:
    """Update list component properties."""
    for component in components:
        if not isinstance(component.v, ndf.model.Object):
            continue

        if is_obj_type(component.v, "CurrentUnitLabelUpperList"):
            _update_current_unit_label(component.v)
        elif is_obj_type(component.v, "BUCKListDescriptor"):
            componentframe = component.v.by_member("ComponentFrame").v
            componentframe.add('MagnifiableOffset = [0.0, ~/ReticleMagnifiableSize * -5.5]')


def _update_current_unit_label(component: Any) -> None:
    """Update current unit label properties."""
    component_frame = '''\
ComponentFrame = TUIFramePropertyRTTI
(
    MagnifiableOffset = [0.0, ~/ReticleMagnifiableSize * -5.5]
    AlignementToFather = [0.5, 0.0]
    AlignementToAnchor = [0.5, 0.0]
)'''
    component.replace(0, component_frame)


def _replace_upper_label_name_only(source_path) -> None:
    """Replace vertical list UpperLabel with a container for VIP-compliant overlays."""
    index = source_path.by_namespace("UpperLabelNameOnly").index
    source_path.replace(index, _get_upper_label_name_only())
    logger.debug("Replaced UpperLabelNameOnly with BUCKContainerDescriptor layout")


def _get_upper_label_name_only() -> str:
    """Upper label: free-layout container (morale anchor, HP icon, carried units)."""
    return '''\
private UpperLabelNameOnly is BUCKContainerDescriptor
(
    ElementName = "UpperLabel"
    ComponentFrame = TUIFramePropertyRTTI
    (
        MagnifiableOffset = [0.0, ~/ReticleMagnifiableSize * -5.5]
        MagnifiableWidthHeight = [2000.0, 0.0]
        AlignementToFather = [0.5, 0.0]
        AlignementToAnchor = [0.5, 1.0]
    )
    ClipContent = false
    IsClippable = false
    Components =
    [
        ~/UnitNameAndRightListNameOnly,
        BUCKContainerDescriptor
        (
            ElementName = "MoraleGaugeAnchor"
            ComponentFrame = TUIFramePropertyRTTI
            (
                MagnifiableOffset = [0.0, 0.0]
                AlignementToFather = [0.5, 0.0]
                AlignementToAnchor = [0.5, 0.0]
            )
            FitStyle = ~/ContainerFitStyle/FitToContent
            Components =
            [
                TMoraleGaugeDescriptor
                (
                    ElementName = "MoraleGauge"
                    Description = ~/MoraleAndHPGaugesDescription
                    LocalRenderLayer = 1
                    UniformDrawer = $/UserInterface/UIUniformDrawer
                    AlignementToFather = [0.5, 0.0]
                    AlignementToAnchor = [0.5, 0.0]
                ),
            ]
        ),
        ~/UnitLabelUnitIconNameOnly,
        CarriedUnitNameList
        (
            ComponentFrame = TUIFramePropertyRTTI
            (
                MagnifiableOffset = [0.0, -18.5]
                AlignementToFather = [0.5, 0.0]
                AlignementToAnchor = [0.5, 0.0]
            )
        ),
    ]
)'''
