"""Adjusting standard stats for weapons."""

from typing import Any, Dict, List, Union

from src import ndf
from src.constants.weapons.standards import (
    AIM_TIME_STANDARDS,
    CANON_HE_DAMAGE_BY_CALIBER,
    CANON_HE_DAMAGE_EXCEPTIONS,
    HE_BOMB_DAMAGE_BY_WEIGHT,
    HE_BOMB_NAME_MATCH,
    HE_BOMB_TRAIT_TOKENS,
    WEAPON_RANGE_MEMBERS_TO_CHECK,
)
from src.constants.weapons.standards.pattern.clu_sol_traits import (
    CLU_SOL_TRAIT_TOKEN_CLUSTER,
    CLU_SOL_TRAIT_TOKEN_HEAT,
)


def apply_aim_time_standards(source_path, logger):
    """Edit aim times for weapons."""
    for ammo_descr in source_path:
        has_category = ammo_descr.v.by_m("TypeCategoryName", False) is not None
        has_aim_time = ammo_descr.v.by_m("AimingTime", False) is not None

        if not (has_aim_time and has_category):
            continue

        ammo_type = ammo_descr.v.by_m("TypeCategoryName").v
        aim_time = ammo_descr.v.by_m("AimingTime").v

        for rule in AIM_TIME_STANDARDS:
            if ammo_type != rule["type_category"]:
                continue
            if aim_time in rule["current"]:
                target = rule["target"]
                ammo_descr.v.by_m("AimingTime").v = target
                label = rule["label"]
                extra = f" ({label})" if label else ""
                logger.info(f"(Ammunition.ndf) Changed {ammo_descr.namespace} aim time to {target}{extra}")
            else:
                logger.debug(
                    f"""(Ammunition.ndf) {ammo_descr.namespace} aim time is not in {rule["current"]}, likely
                                   an ammo edit changed this (in which case ignore this) or it was
                                   changed by Eugen""",
                )
            break


def apply_weapon_range_standards(source_path, logger):
    """Edit weapon ranges."""

    for weapon_descr in source_path:
        member = weapon_descr.v.by_m
        for range_type, data in WEAPON_RANGE_MEMBERS_TO_CHECK.items():
            if member(range_type, False) is None:
                continue

            for old_range, new_range in data.items():
                if member(range_type).v == str(old_range):
                    member(range_type).v = str(new_range)
                    logger.info(
                        f"(Ammunition.ndf) Changed {weapon_descr.namespace} "
                        f"{range_type} from {old_range} to {new_range}",
                    )
                    continue


def apply_bomb_damage_standards(source_path, logger):
    """Edit bomb damage standards in Ammunition.ndf and AmmunitionMissiles.ndf"""

    bombs = HE_BOMB_DAMAGE_BY_WEIGHT
    he_bomb_matching = HE_BOMB_NAME_MATCH

    # TODO: String matching is not reliable long term, we should set this in ammo edits instead
    for ammo_descr in source_path:
        ammo_name = ammo_descr.namespace
        traits_list = ammo_descr.v.by_m("TraitsToken")
        if not any(
            any(token in trait.v for token in HE_BOMB_TRAIT_TOKENS)
            for trait in traits_list.v
        ):
            continue

        if any(bomb in ammo_name for bomb in he_bomb_matching["100"]):
            for key, value in bombs["he_100kg"].items():
                ammo_descr.v.by_m(key).v = str(value)
                logger.info(f"(Ammunition.ndf) Changed {ammo_descr.namespace} {key} to {value}")
        if any(bomb in ammo_name for bomb in he_bomb_matching["250"]):
            for key, value in bombs["he_250kg"].items():
                ammo_descr.v.by_m(key).v = str(value)
                logger.info(f"(Ammunition.ndf) Changed {ammo_descr.namespace} {key} to {value}")
        elif any(bomb in ammo_name for bomb in he_bomb_matching["500"]):
            for key, value in bombs["he_500kg"].items():
                ammo_descr.v.by_m(key).v = str(value)
                logger.info(f"(Ammunition.ndf) Changed {ammo_descr.namespace} {key} to {value}")
        elif any(bomb in ammo_name for bomb in he_bomb_matching["1000"]):
            for key, value in bombs["he_1000kg"].items():
                ammo_descr.v.by_m(key).v = str(value)
                logger.info(f"(Ammunition.ndf) Changed {ammo_descr.namespace} {key} to {value}")
        elif any(bomb in ammo_name for bomb in he_bomb_matching["1250"]):
            for key, value in bombs["he_1250kg"].items():
                ammo_descr.v.by_m(key).v = str(value)
                logger.info(f"(Ammunition.ndf) Changed {ammo_descr.namespace} {key} to {value}")


def apply_he_damage_standards(source_path, logger):
    """Apply HE (PhysicalDamages) standards in Ammunition.ndf"""

    damage_map = CANON_HE_DAMAGE_BY_CALIBER
    exceptions = CANON_HE_DAMAGE_EXCEPTIONS

    for ammo_descr in source_path:
        namespace = ammo_descr.namespace
        if namespace in exceptions:
            continue

        if ammo_descr.v.by_m("Name", False) is None:
            logger.debug(f"No name found for {namespace}")
            continue

        name_membr = ammo_descr.v.by_m("Name").v
        if name_membr == "'None'":
            continue

        minmax_category = ammo_descr.v.by_m("MinMaxCategory", False)
        if minmax_category is None or minmax_category.v != "MinMax_CanonAP":
            continue

        piercing_bool = ammo_descr.v.by_m("PiercingWeapon").v
        if piercing_bool == "True":
            continue

        caliber_membr = ammo_descr.v.by_m("Caliber").v
        if caliber_membr in damage_map:
            ammo_descr.v.by_m("PhysicalDamages").v = str(damage_map[caliber_membr])
            logger.info(f"Changed {namespace} HE damage to {damage_map[caliber_membr]}")


def _parse_numeric_value(value: Union[int, float, str]) -> Union[int, float, None]:
    try:
        if isinstance(value, (int, float)):
            return value
        if isinstance(value, str):
            if "." in value:
                return float(value)
            return int(value)
    except (TypeError, ValueError):
        return None
    return None


def _trait_for_ammo_namespace(
    namespace: str,
    targets: Dict[str, str],
    renames_new_old: Dict[str, str],
) -> Union[str, None]:
    """Resolve precomputed target after salvo renames (namespace may be new name)."""
    if namespace in targets:
        return targets[namespace]
    base = namespace.removeprefix("Ammo_")
    old_base = renames_new_old.get(base)
    if old_base is not None:
        return targets.get(f"Ammo_{old_base}")
    return None


def apply_clu_sol_trait_standards(source_path, logger, game_db: Dict[str, Any]) -> None:
    """TraitsToken: swap ``cluster`` for CLU SOL trait from game_db; remove ``HEAT`` (precomputed map)."""
    ammo_db = game_db.get("ammunition", {})
    targets = ammo_db.get("clu_sol_trait_targets") or {}
    if not targets:
        return
    renames_new_old = ammo_db.get("renames_new_old", {})

    for ammo_descr in source_path:
        if not hasattr(ammo_descr, "namespace") or not ammo_descr.namespace:
            continue
        target_trait = _trait_for_ammo_namespace(ammo_descr.namespace, targets, renames_new_old)
        if target_trait is None:
            continue

        traits_list = ammo_descr.v.by_m("TraitsToken", False)
        if traits_list is None:
            logger.debug("(Ammo) No TraitsToken for %s", ammo_descr.namespace)
            continue

        old_tokens = [trait.v for trait in traits_list.v]
        new_trait_ndf = f"'{target_trait}'"
        out: List[str] = [
            t for t in old_tokens
            if t not in (CLU_SOL_TRAIT_TOKEN_CLUSTER, CLU_SOL_TRAIT_TOKEN_HEAT)
        ]
        if new_trait_ndf not in out:
            out.append(new_trait_ndf)

        if out == old_tokens:
            continue

        list_str = "[" + ", ".join(out) + "]"
        ammo_descr.v.by_m("TraitsToken").v = ndf.convert(list_str.encode("utf-8"))[0].v
        logger.info("(Ammo) CLU SOL TraitsToken %s -> %s", ammo_descr.namespace, target_trait)


def apply_infantry_mmg_cac_trait(source_path, logger) -> None:
    """Add CAC trait to infantry MMGs with MinimumRangeGRU = 0."""
    for ammo_descr in source_path:
        minmax_category = ammo_descr.v.by_m("MinMaxCategory", False)
        if minmax_category is None or minmax_category.v != "MinMax_inf_MMG":
            continue

        min_range_membr = ammo_descr.v.by_m("MinimumRangeGRU", False)
        if min_range_membr is None:
            continue

        min_range_value = _parse_numeric_value(min_range_membr.v)
        if min_range_value != 0:
            continue

        traits_list = ammo_descr.v.by_m("TraitsToken", False)
        if traits_list is None:
            logger.debug(f"No TraitsToken list found for {ammo_descr.namespace}")
            continue

        existing_traits = [trait.v for trait in traits_list.v]
        if "'CAC'" in existing_traits:
            continue

        traits_list.v.add("'CAC'")
        logger.info(f"Added CAC trait to {ammo_descr.namespace} (MinimumRangeGRU = 0)")
