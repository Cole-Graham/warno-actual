from src.utils.logging_utils import setup_logger

logger = setup_logger(__name__)


def edit_ui_ingame_uiingameunitlabelresource(source_path) -> None:
    """GameData/UserInterface/Use/InGame/UIInGameUnitLabelResources.ndf"""
    logger.info("Editing UIInGameUnitLabelResources.ndf")

    specific = source_path.by_n("SpecificInGameUnitLabelResources").v
    damage_map = specific.by_m("DamageTypeNameToFeedbackType").v
    damage_map.add(
        f"(DamageFamily_sead_missile_wa, ~/InGameUnitLabelUpdateFeedbackType/Missile)",
    )
