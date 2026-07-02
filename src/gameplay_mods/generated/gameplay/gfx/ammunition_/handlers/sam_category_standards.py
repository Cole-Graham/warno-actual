"""Apply SAM missile category standards (``TimeBetweenTwoSalvos`` from salvo length)."""

from typing import Any

from src.constants.weapons.standards import sam_time_between_salvos_seconds


def _read_shots_count_per_salvo(descr: Any) -> int | None:
    membr = descr.v.by_m("ShotsCountPerSalvo", False)
    if membr is None:
        return None
    try:
        return int(str(membr.v))
    except (TypeError, ValueError):
        return None


def apply_sam_time_between_salvos_standard(
    descr: Any,
    category: str,
    *,
    shots_count: int | None = None,
) -> None:
    """Set ``TimeBetweenTwoSalvos`` for SAM missiles from salvo length.

    Pass ``shots_count`` when salvo length is known from ``WeaponDescriptor``
    ``SalvoLengths`` (including newly created ``_salvolength{N}`` variants).
    Otherwise reads ``ShotsCountPerSalvo`` from the descriptor.
    """
    if category != "SAM":
        return

    resolved = shots_count if shots_count is not None else _read_shots_count_per_salvo(descr)
    if resolved is None:
        return

    membr = descr.v.by_m("TimeBetweenTwoSalvos", False)
    if membr is None:
        return

    value = sam_time_between_salvos_seconds(resolved)
    membr.v = str(value)
