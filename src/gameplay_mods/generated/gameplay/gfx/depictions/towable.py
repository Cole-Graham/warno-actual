"""Functions for modifying Towable.ndf"""

from typing import Any

from src.constants.new_units import NEW_UNITS
from src.utils.logging_utils import setup_logger
from src.utils.ndf_utils import is_obj_type

logger = setup_logger(__name__)

_TOWED_ENTRY_TYPE = "TTowedUnitCatalogEntry"


def _identifier_value_as_str(value: Any) -> str:
    return str(value).strip("'").strip('"')


def edit_gen_gp_gfx_towable(source_path: Any) -> None:
    """GameData/Generated/Gameplay/Gfx/Depictions/Towable.ndf

    Appends a ``TTowedUnitCatalogEntry`` for each new unit whose vanilla donor
    has a matching ``Identifier`` row. The clone keeps donor mesh paths; only
    ``Identifier`` is set to the new unit name.
    """
    existing_ids: set[str] = set()
    donor_row_by_id: dict[str, Any] = {}

    for row in source_path:
        try:
            if not is_obj_type(row.v, _TOWED_ENTRY_TYPE):
                continue
            id_m = row.v.by_m("Identifier", False)
            if id_m is None:
                continue
            raw = _identifier_value_as_str(id_m.v)
            existing_ids.add(raw)
            if raw not in donor_row_by_id:
                donor_row_by_id[raw] = row
        except Exception as exc:
            logger.debug("Skipping row in Towable index pass: %s", exc)
            continue

    for donor, edits in NEW_UNITS.items():
        donor_name = donor[0]
        unit_name = edits["NewName"]
        if unit_name in existing_ids:
            continue
        donor_row = donor_row_by_id.get(donor_name)
        if donor_row is None:
            continue

        # Same pattern as DepictionVehicles: copy the list row, assign only
        # Identifier. Mesh/InitialPose are left as on the donor; we do not
        # mutate them, so a shallow-shared nested InitialPose on the clone
        # cannot desync the donor row.
        new_row = donor_row.copy()
        id_member = new_row.v.by_m("Identifier", False)
        if id_member is None:
            logger.error(
                "TTowedUnitCatalogEntry clone for %s has no Identifier; skipping",
                unit_name,
            )
            continue
        id_member.v = f'"{unit_name}"'
        source_path.add(new_row)
        existing_ids.add(unit_name)
        logger.info(
            "Added towed catalog entry for %s (donor %s)",
            unit_name,
            donor_name,
        )
