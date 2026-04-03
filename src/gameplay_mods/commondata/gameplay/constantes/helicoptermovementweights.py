"""Functions for modifying HelicopterMovementWeights.ndf (CommonData)."""

from typing import Union

from src import ndf
from src.utils.logging_utils import setup_logger

logger = setup_logger(__name__)


def _set_member(obj, name: str, value: Union[float, int]) -> None:
    obj.v.by_m(name).v = str(value)


def edit_cd_gameplay_constantes_helicoptermovementweights(source_path) -> None:
    """CommonData/Gameplay/Constantes/HelicopterMovementWeights.ndf"""
    logger.info("Editing HelicopterMovementWeights.ndf")

    _set_member(source_path.by_n("DefaultHelicopterWeights"), "Speed", 2.2)
    _set_member(source_path.by_n("DefaultHelicopterWeights"), "AnglesXY", 3.0)
    _set_member(source_path.by_n("DefaultHelicopterWeights"), "AngularSpeedXY", 1.0)

    _set_member(source_path.by_n("StoppingHelicopterWeights"), "Position", 1.5)
    _set_member(source_path.by_n("StoppingHelicopterWeights"), "Speed", 1.2)
    _set_member(source_path.by_n("StoppingHelicopterWeights"), "AnglesXY", 6.0)
    _set_member(source_path.by_n("StoppingHelicopterWeights"), "AngleZ", 4.0)
    _set_member(source_path.by_n("StoppingHelicopterWeights"), "AngularSpeedXY", 3.0)
    _set_member(source_path.by_n("StoppingHelicopterWeights"), "AnglularZSpeed", 5.0)

    _set_member(source_path.by_n("StoppingBeforeLandingHelicopterWeights"), "Position", 2.5)
    _set_member(source_path.by_n("StoppingBeforeLandingHelicopterWeights"), "Speed", 1.0)
    _set_member(source_path.by_n("StoppingBeforeLandingHelicopterWeights"), "AnglesXY", 7.0)
    _set_member(source_path.by_n("StoppingBeforeLandingHelicopterWeights"), "AngleZ", 2.0)
    _set_member(source_path.by_n("StoppingBeforeLandingHelicopterWeights"), "AngularSpeedXY", 3.0)
    _set_member(source_path.by_n("StoppingBeforeLandingHelicopterWeights"), "AnglularZSpeed", 3.0)

    _set_member(source_path.by_n("LandingHelicopterWeights"), "Position", 5.0)
    _set_member(source_path.by_n("LandingHelicopterWeights"), "AnglesXY", 13.0)
    _set_member(source_path.by_n("LandingHelicopterWeights"), "AngleZ", 1.0)
    _set_member(source_path.by_n("LandingHelicopterWeights"), "AngularSpeedXY", 4.0)
    _set_member(source_path.by_n("LandingHelicopterWeights"), "AnglularZSpeed", 3.5)

    _set_member(source_path.by_n("TargetHelicopterWeights"), "Speed", 2.2)
    _set_member(source_path.by_n("TargetHelicopterWeights"), "AnglesXY", 3.0)
    _set_member(source_path.by_n("TargetHelicopterWeights"), "AngularSpeedXY", 1.0)

    _set_member(source_path.by_n("LandingIntermediateHelicopterWeights"), "Position", 3.5)
    _set_member(source_path.by_n("LandingIntermediateHelicopterWeights"), "Speed", 0.5)
    _set_member(source_path.by_n("LandingIntermediateHelicopterWeights"), "AnglesXY", 10.0)
    _set_member(source_path.by_n("LandingIntermediateHelicopterWeights"), "AngleZ", 1.5)
    _set_member(source_path.by_n("LandingIntermediateHelicopterWeights"), "AngularSpeedXY", 3.5)
    _set_member(source_path.by_n("LandingIntermediateHelicopterWeights"), "AnglularZSpeed", 3.0)

    mgr = source_path.by_n("HelicopterWeightsManager").v
    new_hw = ndf.convert(
        b"_hw is MAP ["
        b"(~/StoppedFlying, ~/StillHelicopterWeights), "
        b"(~/MoveTowardTarget, ~/TargetHelicopterWeights), "
        b"(~/Landing, ~/LandingHelicopterWeights), "
        b"(~/StoppingBeforeLanding, ~/StoppingBeforeLandingHelicopterWeights), "
        b"(~/Stopping, ~/StoppingHelicopterWeights)"
        b"]",
    )[0].v
    mgr.by_m("HelicopterWeights").v = new_hw

    wst = mgr.by_m("WaypointScoreThresholds").v
    wst.by_k("~/StoppingBeforeLanding").v = ("6.0", "5.0")
    wst.by_k("~/Stopping").v = ("5.2", "4.4")
    wst.by_k("~/Landing").v = ("4.4", "4.0")
