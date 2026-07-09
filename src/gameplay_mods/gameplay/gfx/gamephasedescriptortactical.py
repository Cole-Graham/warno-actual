"""Functions for modifying GamePhaseDescriptorTactical.ndf."""

from __future__ import annotations

from typing import Any, Sequence, Tuple

from src.constants.gameplay.deployment_grace_period import DEPLOYMENT_GRACE_PERIOD_NOT_SPECIFIED
from src.utils.logging_utils import setup_logger

logger = setup_logger(__name__)

_DEPLOYMENT_MODE_KEYS = (
    "EDeploymentMode/NotSpecified",
    "~/EDeploymentMode/NotSpecified",
)


def _validate_steps(steps: Sequence[Tuple[int, int]]) -> None:
    if not steps:
        raise ValueError("Deployment grace StepList must not be empty")
    if steps[-1][0] != -1:
        raise ValueError("Deployment grace StepList must end with TempsMaxEnSecondes = -1")
    for i in range(len(steps) - 2):
        if steps[i][0] >= steps[i + 1][0]:
            raise ValueError(
                "Deployment grace StepList TempsMaxEnSecondes must strictly increase "
                f"(step {i}: {steps[i][0]} >= step {i + 1}: {steps[i + 1][0]})",
            )


def _lookup_grace_entry(grace_map: Any) -> Any:
    for key in _DEPLOYMENT_MODE_KEYS:
        entry = grace_map.by_k(key, strict=False)
        if entry is not None:
            return entry
    return None


def edit_gameplay_gfx_gamephasedescriptortactical(source_path) -> None:
    """GameData/Gameplay/Gfx/GamePhaseDescriptorTactical.ndf"""
    logger.info("Editing GamePhaseDescriptorTactical.ndf (deployment grace period)")

    descr = source_path.by_n("deploiementGamePhaseDescriptor", strict=False)
    if descr is None:
        raise ValueError("deploiementGamePhaseDescriptor not found in GamePhaseDescriptorTactical.ndf")

    grace_map = descr.v.by_m("ListeProprietesTempsGrace").v
    entry = _lookup_grace_entry(grace_map)
    if entry is None:
        raise ValueError(
            "EDeploymentMode/NotSpecified not found in ListeProprietesTempsGrace",
        )

    config = DEPLOYMENT_GRACE_PERIOD_NOT_SPECIFIED
    steps = config["steps"]
    _validate_steps(steps)

    timer_seconds = config["timer_seconds"]
    entry.v.by_m("TempsGracePourTimerEnSecond").v = str(timer_seconds)
    logger.info("NotSpecified TempsGracePourTimerEnSecond set to %s", timer_seconds)

    step_list = entry.v.by_m("StepList").v
    if len(step_list) != len(steps):
        raise ValueError(
            f"NotSpecified StepList length {len(step_list)} != expected {len(steps)}",
        )

    for index, (max_seconds, multiplier) in enumerate(steps):
        step = step_list[index].v
        step.by_m("TempsMaxEnSecondes").v = str(max_seconds)
        step.by_m("MultiplicateurTempsGrace").v = str(multiplier)
        logger.info(
            "NotSpecified StepList[%s]: TempsMaxEnSecondes=%s, MultiplicateurTempsGrace=%s",
            index,
            max_seconds,
            multiplier,
        )
