"""Functions for modifying shared showroom component base."""

from src.utils.logging_utils import setup_logger

logger = setup_logger(__name__)


def edit_uispecificshowroomcomponentbase(source_path) -> None:
    """Edit GameData/UserInterface/Use/ShowRoom/UISpecificShowRoomComponentBase.ndf."""
    
    animationpanelunitinfos = source_path.by_namespace("AnimationPanelUnitInfos")
    frameproperty_beforeanimation = animationpanelunitinfos.v.by_m("FramePropertyBeforeAnimation")
    frameproperty_beforeanimation.v.by_m("MagnifiableOffset").v = "[-120.0, 228.0]"
    frameproperty_afteranimation = animationpanelunitinfos.v.by_m("FramePropertyAfterAnimation")
    frameproperty_afteranimation.v.by_m("MagnifiableOffset").v = "[0.0, 228.0]"
