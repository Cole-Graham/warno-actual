from src.utils.logging_utils import setup_logger

logger = setup_logger(__name__)


def edit_gameplay_constantes_weapontypepriorities(source_path) -> None:
    """GameData/Gameplay/Constantes/WeaponTypePriorities.ndf"""
    logger.info("Editing WeaponTypePriorities.ndf")

    weapon_types = source_path.by_n("WeaponTypePriorities").v.by_m("WeaponTypes").v
    ap_missile_row = weapon_types.find_by_cond(
        lambda row: isinstance(row.v, tuple)
        and len(row.v) >= 1
        and row.v[0] == "DamageFamily_ap_missile",
        strict=False,
    )
    new_row = "(DamageFamily_sead_missile_wa, EWeaponRangeDependant/NotDefined)"
    if ap_missile_row is None:
        raise RuntimeError(
            "WeaponTypes: no tuple row with first element DamageFamily_ap_missile",
        )
    weapon_types.insert(ap_missile_row.index + 1, new_row)
