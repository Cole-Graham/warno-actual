"""Functions for modifying shared showroom component base."""

from src.utils.logging_utils import setup_logger

logger = setup_logger(__name__)


def edit_uispecificshowroomcomponentbase(source_path) -> None:
    """Edit GameData/UserInterface/Use/ShowRoom/UISpecificShowRoomComponentBase.ndf.

    Vanilla removed UnitInfosSheet; AnimationPanelUnitInfos now positions
    UnitInfosPanels at Y=208, matching the old mod offset (190 + 18).
    Filter bar spacing remains in armory.py (_edit_display_new_filter_bar_spacing).
    """
    logger.info("Editing UISpecificShowRoomComponentBase.ndf (no edits required)")
