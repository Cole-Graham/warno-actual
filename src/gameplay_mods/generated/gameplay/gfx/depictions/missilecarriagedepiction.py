"""Functions for modifying MissileCarriageDepiction.ndf"""

from typing import Any

from src.constants.unit_edits import load_depiction_edits
from src.constants.new_units import NEW_DEPICTIONS
from src.gameplay_mods.generated.gameplay.gfx.depictions._apply import apply_indexed_list_ops
from src.utils.logging_utils import setup_logger
from src.utils.ndf_utils import ndf

logger = setup_logger(__name__)

_NDF_FILE = "MissileCarriageDepiction.ndf"


def edit_gen_gp_gfx_missilecarriagedepiction(source_path: Any) -> None:
    """GameData/Generated/Gameplay/Gfx/Depictions/MissileCarriageDepiction.ndf"""
    _edit_depictions(source_path)
    _create_new_depictions(source_path)


def _edit_depictions(source_path: Any) -> None:
    """Edit missile carriage depictions for existing units"""
    depiction_edits = load_depiction_edits()

    for unit_name, unit_data in depiction_edits.items():
        if _NDF_FILE not in unit_data["valid_files"]:
            continue

        if "MissileCarriageDepiction_ndf" not in unit_data:
            logger.error(f"{_NDF_FILE} is valid for {unit_name} but no edits found")
            continue

        unit_edits = unit_data["MissileCarriageDepiction_ndf"]
        for key, edits in unit_edits.items():
            if not isinstance(key, tuple):
                logger.error(f"Key is not a tuple: {key}")
                continue

            namespace, _obj_type = key
            if not namespace:
                continue

            missile_carriage = source_path.by_n(namespace)
            if not missile_carriage:
                logger.error(f"Could not find missile carriage depiction {namespace} for {unit_name}")
                continue

            for row_name_or_type, value in edits.items():
                if row_name_or_type == "Missiles":
                    apply_indexed_list_ops(
                        missile_carriage.v.by_m(row_name_or_type),
                        value,
                        label=f"{namespace}.Missiles ({unit_name})",
                        op_handlers={"edit": _edit_missile},
                    )
                else:
                    missile_carriage.v.by_m(row_name_or_type).v = value
                    logger.info(f"Edited {row_name_or_type} for {unit_name}")


def _edit_missile(list_member: Any, row_index: int, payload: Any) -> None:
    """Apply per-member edits to a single Missiles row."""
    if not isinstance(payload, dict):
        logger.error(f"Missiles[{row_index}] edit payload is not a dict")
        return
    for member, new_value in payload.items():
        list_member.v[row_index].v.by_m(member).v = str(new_value)
        logger.info(f"Edited Missiles[{row_index}].{member}")


def _create_new_depictions(source_path: Any) -> None:
    """Create missile carriage depictions for new units"""
    for unit_name, unit_data in NEW_DEPICTIONS.items():
        if _NDF_FILE not in unit_data["valid_files"]:
            continue
        unit_depictions = unit_data["MissileCarriageDepiction_ndf"]
        logger.debug(f"Processing missile carriage depictions for {unit_name}")

        for descr_type, descr_obj in unit_depictions.items():
            new_descr_obj = ndf.convert(descr_obj)
            source_path.add(new_descr_obj)
            logger.info(f"Added {descr_type} for {unit_name}")
