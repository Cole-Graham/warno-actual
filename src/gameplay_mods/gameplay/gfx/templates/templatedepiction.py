"""Functions for modifying TemplateDepiction.ndf"""

import re
from typing import Any

from src.constants.unit_edits.depiction_edits.selector_tactic import (
    NEW_SELECTOR_TACTIC_OBJECTS,
)
from src.utils.logging_utils import setup_logger

logger = setup_logger(__name__)

_SURROGATES_NAMESPACE_RE = re.compile(r"^TacticDepiction_(\d+)_Surrogates$")


def edit_gameplay_gfx_templates_templatedepiction(source_path: Any) -> None:
    """GameData/Gameplay/Gfx/Templates/TemplateDepiction.ndf.

    Ensures every ``surrogates_count`` referenced by
    :data:`NEW_SELECTOR_TACTIC_OBJECTS` has a matching
    ``TacticDepiction_NN_Surrogates`` row. Missing counts are inserted in
    numeric order, each right after the previous numbered row, so the chained
    ``TacticDepiction_{prev:02}_Surrogates + [[LOD_High, 'NN']]`` references
    resolve. Any count already present in the parsed source is left untouched,
    including rows the game devs may ship in future patches.
    """
    if not NEW_SELECTOR_TACTIC_OBJECTS:
        logger.debug("NEW_SELECTOR_TACTIC_OBJECTS is empty; no surrogate rows to add")
        return

    existing: dict[int, int] = {}
    for row_index, row in enumerate(source_path):
        namespace = getattr(row, "namespace", None)
        if not namespace:
            continue
        match = _SURROGATES_NAMESPACE_RE.match(namespace)
        if match:
            existing[int(match.group(1))] = row_index

    required = sorted({ss for _, ss in NEW_SELECTOR_TACTIC_OBJECTS})
    for n in required:
        if n in existing:
            logger.debug(
                f"TacticDepiction_{n:02}_Surrogates already present; skipping"
            )

    missing = [n for n in required if n not in existing]
    if not missing:
        logger.info("No new TacticDepiction_NN_Surrogates rows needed")
        return

    for n in missing:
        prev_candidates = [k for k in existing if k < n]
        if not prev_candidates:
            logger.error(
                f"Cannot insert TacticDepiction_{n:02}_Surrogates: no lower-numbered "
                f"row exists to chain from. Skipping."
            )
            continue
        prev = max(prev_candidates)
        prev_row_index = existing[prev]
        insert_idx = prev_row_index + 1

        new_row = (
            f"TacticDepiction_{n:02}_Surrogates is "
            f"TacticDepiction_{prev:02}_Surrogates + [[LOD_High, '{n:02}']]"
        )
        source_path.insert(insert_idx, new_row)
        logger.info(
            f"Inserted TacticDepiction_{n:02}_Surrogates after "
            f"TacticDepiction_{prev:02}_Surrogates (row {insert_idx})"
        )

        existing[n] = insert_idx
        for k, idx in list(existing.items()):
            if k != n and idx >= insert_idx:
                existing[k] = idx + 1
