from src.utils.logging_utils import setup_logger

logger = setup_logger(__name__)


def edit_gameplay_constantes_bombtrajectoryconfigs(source_path) -> None:
    """GameData/Gameplay/Constantes/BombTrajectoryConfigs.ndf"""
    logger.info("Editing BombTrajectoryConfigs.ndf")

    default_traj = source_path.by_n("DefaultBombTrajectory").v
    default_traj.by_m("FlyingTimeFromReferenceAltitudeAndSpeed").v = "3.0"
    logger.info("Set FlyingTimeFromReferenceAltitudeAndSpeed for DefaultBombTrajectory to 3.0")
