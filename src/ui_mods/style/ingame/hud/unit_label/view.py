"""Functions for modifying UI HUD unit label view."""
# from typing import Any

from src import ndf
from src.utils.logging_utils import setup_logger
from src.utils.ndf_utils import is_obj_type

logger = setup_logger(__name__)


def edit_uispecificunitlabelview(source_path) -> None:
    """Edit UISpecificUnitLabelView.ndf.
    
    Args:
        source_path: NDF file containing HUD unit label view definitions
    """
    logger.info("Editing UISpecificUnitLabelView.ndf")
    
    # Add unit label icon name only
    source_path.insert(1, _get_unit_label_icon_name_only())
    logger.debug("Added unit label icon name only")
    
    # Update supply gauge
    _update_supply_gauge(source_path)
    
    # Update morale and HP gauges color tokens
    _update_morale_hp_gauges_color_tokens(source_path)
    
    # Add morale and HP gauges name only description
    _add_morale_hp_gauges_name_only(source_path)
    
    # Update bottom component
    _update_bottom_component(source_path)
    
    # Update icon and right label
    _update_icon_and_right_label(source_path)
    
    # Update upper label
    _update_upper_label(source_path)
    
    # Update game unit label view
    _update_game_unit_label_view(source_path)
    
    # Update reticle
    _update_reticle(source_path)


def _get_unit_label_icon_name_only() -> str:
    """Get unit label icon name only template."""
    return '''\
private UnitLabelUnitIconNameOnly is TBUCKSpecificLabelUnitIconDescriptor
(
    ElementName = "UnitIcon"
    ComponentFrame = TUIFramePropertyRTTI
    (
        MagnifiableOffset = [0.0, ~/ReticleMagnifiableSize * -11.0]
        MagnifiableWidthHeight = [ 0.0, 0.0]
        AlignementToFather = [0.50, 0.0]
        AlignementToAnchor = [1.0, 0.0]
    )
    ChildFitToContent = true
    LocalRenderLayer = 3
    TextureDrawer = "ColorMultiply"
    UniformDrawer = $/UserInterface/UIUniformDrawer
    HasBorder = false
    BorderThicknessToken = "2"
    BorderLineColorToken = "Blanc"
    HasBackground = true
    BackgroundLocalRenderLayer = 1
    MoraleAndHPGaugesDescription = ~/MoraleAndHPGaugesNameOnlyDescription
    SmartChipDescription = ~/SmartChipDescription
)'''


def _update_supply_gauge(source_path) -> None:
    """Update supply gauge properties."""
    unitlabelunitsupplygauge = source_path.by_namespace("UnitLabelUnitSupplyGauge").v
    description = unitlabelunitsupplygauge.by_member("Description").v
    description.by_member("MagnifiableExtraVOffset").v = "-4.0"
    logger.debug("Updated supply gauge offset")

def _update_morale_hp_gauges_color_tokens(source_path) -> None:
    """Update morale and HP gauges color tokens."""
    moraleandhpgaugesdescription = source_path.by_namespace("MoraleAndHPGaugesDescription")
    moraleandhpgaugesdescription.v.by_member("MoraleGaugeColorTokens").v = str(
        ["moral_color_bad_1_M81", "moral_color_bad_2", "moral_color_bad_3", "moral_color_bad_4_M81"])
    logger.debug("Updated morale and HP gauges color tokens")

def _add_morale_hp_gauges_name_only(source_path) -> None:
    """Add morale and HP gauges name only description."""
    index = source_path.by_namespace("MoraleAndHPGaugesDescription").index + 1
    source_path.insert(index, _get_morale_hp_gauges_name_only())
    logger.debug("Added morale and HP gauges name only description")


def _get_morale_hp_gauges_name_only() -> str:
    """Get morale and HP gauges name only template."""
    return '''\
MoraleAndHPGaugesNameOnlyDescription is TMoraleAndHPGaugesDescription
(
    MoraleGaugeColorTokens = ["moral_color_bad_1_M81", "moral_color_bad_2", "moral_color_bad_3", "moral_color_bad_4_M81"]
    HPElementHealthValue = 2
    MagnifiableWidthOneHPLabelBlock = 6.0
    MoraleMagnifiableWidthHeight = [32.0, 3.0]
    HPMagnifiableHeight = 4.0
    MagnifiableSpacing = 1.0
    HPGraduationThicknessToken = "1"
    HPGraduationColorToken = "Noir"
    HPFillColorToken = "White"
    HPBackgroundColorToken = "Noir"
)'''


def _update_bottom_component(source_path) -> None:
    """Update bottom component properties."""
    unitlabelbottomcomponent = source_path.by_namespace("UnitLabelBottomComponent").v
    unitlabelbottomcomponent.by_member("LeavingDistrictTextColor").v = '"M81_AppleIIc"'
    logger.debug("Updated bottom component text color")


def _update_icon_and_right_label(source_path) -> None:
    """Update icon and right label properties."""
    currentuniticonandrightlabel = source_path.by_namespace("CurrentUnitIconAndRightLabel").v
    
    for component in currentuniticonandrightlabel.by_member("Components").v:
        if not isinstance(component.v, ndf.model.Object) or not is_obj_type(component.v, "BUCKListDescriptor"):
            continue
            
        componentframe = component.v.by_member("ComponentFrame").v
        componentframe.add("MagnifiableOffset = [0.0, 0.0]")
    
    logger.debug("Updated icon and right label offset")


def _update_upper_label(source_path) -> None:
    """Update upper label properties."""
    upperlabel = source_path.by_namespace("UpperLabel").v
    
    componentframe = upperlabel.by_member("ComponentFrame").v
    componentframe.by_member("MagnifiableOffset").v = "[0.0, ~/ReticleMagnifiableSize * -7.5]"
    
    upperlabel.by_member("ClipContent").v = "true"
    logger.debug("Updated upper label properties")


def _update_game_unit_label_view(source_path) -> None:
    """Update game unit label view properties."""
    uispecificingameunitlabelviewdescriptor_template = source_path.by_namespace("UISpecificInGameUnitLabelViewDescriptor").v
    uispecificingameunitlabelviewdescriptor_template.by_member("SuppressAnimAlphaMinimum").v = "60"
    uispecificingameunitlabelviewdescriptor_template.by_member("ConcealedAnimAlphaMinimum").v = "60"
    logger.debug("Updated game unit label view animation properties")


def _update_reticle(source_path) -> None:
    """Update reticle properties."""
    # Update reticle descriptor
    unitreticledescriptor_template = source_path.by_namespace("UnitReticleDescriptor").v
    unitreticledescriptor_template.by_member("SuppressAnimAlphaMinimum").v = "60"
    unitreticledescriptor_template.by_member("ConcealedAnimAlphaMinimum").v = "60"
    
    # Update reticle main component
    _update_reticle_main_component(source_path)
    
    logger.debug("Updated reticle properties")


def _update_reticle_main_component(source_path) -> None:
    """Update reticle main component properties."""
    uispecificunitlabelreticledescriptor = source_path.by_namespace("UISpecificUnitLabelReticleDescriptor").v
    maincomponent_descr = uispecificunitlabelreticledescriptor.by_member("MainComponentDescriptor").v
    
    # Update frame
    componentframe = maincomponent_descr.by_member("ComponentFrame").v
    componentframe.by_member("MagnifiableWidthHeight").v = "[36.0, 36.0]"
    
    # Update components
    for component in maincomponent_descr.by_member("Components").v:
        if not isinstance(component.v, ndf.model.Object) or not is_obj_type(component.v, "BUCKTextureDescriptor"):
            continue
            
        elementname = component.v.by_member("ElementName").v
        if elementname == '"Surrounding"':
            componentframe = component.v.by_member("ComponentFrame").v
            componentframe.by_member("RelativeWidthHeight").v = "[0.0, 0.0]"  # noqa
