from src.utils.logging_utils import setup_logger

logger = setup_logger(__name__)


def edit_ui_ingame_uimousepolicyresources(source_path) -> None:
    """GameData/UserInterface/Use/InGame/UIMousePolicyResources.ndf"""
    logger.info("Editing UIMousePolicyResources.ndf")

    mouse_widget = source_path.by_n("MouseWidgetSelector_Attack").v
    text_for_damage_type = mouse_widget.by_m("TextForDamageType").v
    text_for_damage_type.add(
        '(DamageFamily_sead_missile_wa, "TC_HEAT")',
    )
