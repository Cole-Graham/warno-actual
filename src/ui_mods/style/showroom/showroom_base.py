"""Functions for modifying shared showroom component base."""

from src import ndf
from src.utils.logging_utils import setup_logger

logger = setup_logger(__name__)

_UNIT_INFOS_SHEET_Y_DELTA = 18.0


def edit_uispecificshowroomcomponentbase(source_path) -> None:
    """Edit GameData/UserInterface/Use/ShowRoom/UISpecificShowRoomComponentBase.ndf."""
    logger.info("Editing UISpecificShowRoomComponentBase.ndf")
    _edit_unit_infos_sheet_offset(source_path)


def _edit_unit_infos_sheet_offset(source_path) -> None:
    """Move UnitInfosSheet down to clear DisplayNewFilterBar with margin."""

    sheet = source_path.by_namespace("UnitInfosSheet").v
    frame = sheet.by_m("ComponentFrame").v
    offset_member = frame.by_m("MagnifiableOffset")
    offset_value = offset_member.v

    if isinstance(offset_value, ndf.model.List) and len(offset_value) >= 2:
        x = float(offset_value[0].v)
        y = float(offset_value[1].v) + _UNIT_INFOS_SHEET_Y_DELTA
        offset_value[1].v = str(y)
    else:
        offset_member.v = f"[20.0, {190.0 + _UNIT_INFOS_SHEET_Y_DELTA}]"
        x, y = 20.0, 190.0 + _UNIT_INFOS_SHEET_Y_DELTA

    logger.debug("Updated UnitInfosSheet MagnifiableOffset to [%s, %s]", x, y)
