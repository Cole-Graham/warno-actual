"""Functions for modifying EffetsSurUnite.ndf"""
from typing import Any, List, Tuple
from src import ndf
from src.constants.effects.veterancy import (
    ELITE_HELO_SF_GUID,
    HELO_ATTACK_EFFECT_GUIDS,
    MULTIPLICATIVE_INFANTRY_GUIDS,
    PACK_TYPES_VANILLA_LOCALIZATION,
    POST_PATCH_OVERRIDES,
    VETERANCY_BONUSES,
    VETERANCY_EFFECT_CHANGES,
    VETERANCY_HELO_ATTACK_EFFECT_CHANGES,
    VETERANCY_RUNTIME_EFFECT_CHANGES,
    VETERANCY_SF_MULTIPLICATIVE_EFFECT_CHANGES,
)
from src.utils.dictionary_utils import write_dictionary_entries
from src.utils.ndf_utils import find_obj_by_type, strip_quotes
from src.constants.effects import (
    CHOC_CQC_BONUSES,
    CHOC_INRANGE_FEEDBACK_EFFECT,
    CHOC_INRANGE_TAG_EFFECT,
    SPRINT_EFFECT,
    DEPLOY_EFFECT,
    DEPLOY_OK_EFFECT,
    MEDIUM_EQUIP_PENALTY_EFFECT,
    MEDIUM_EQUIP_PENALTY_FLOOR_TAG_EFFECT,
    MEDIUM_EQUIP_PENALTY_SF_EFFECT,
    NO_SPRINT_MORALE_EFFECT,
    NO_SWIFT_EFFECT,
    SWIFT_EFFECT,
    SWIFT_OK_EFFECT,
)
from src.utils.logging_utils import setup_logger

logger = setup_logger(__name__)


def _normalize_effect_damage_type(value: str) -> str:
    damage_type = str(value).strip()
    if damage_type.startswith("~/"):
        damage_type = damage_type[2:]
    return damage_type


def _find_vet_effect(effects_list, effect_type: str, damage_type: str | None = None):
    for effect in effects_list.v:
        if not hasattr(effect.v, "type") or effect.v.type != effect_type:
            continue
        if damage_type is not None:
            damage_type_membr = effect.v.by_m("DamageType", False)
            if damage_type_membr is None:
                continue
            if (
                _normalize_effect_damage_type(damage_type_membr.v)
                != _normalize_effect_damage_type(damage_type)
            ):
                continue
        return effect
    return None


# TODO: Break this down into specific functions
def edit_gen_gp_effects_effetssurunite(source_path) -> None:
    """GameData/Generated/Gameplay/Effects/EffetsSurUnite.ndf"""
    logger.info("Modifying unit effects")

    # Add new effects
    for i, row in enumerate(source_path, start=1):
        if row.namespace == "UnitEffect_Choc":
            source_path.insert(i, CHOC_INRANGE_FEEDBACK_EFFECT)
            source_path.insert(i, CHOC_INRANGE_TAG_EFFECT)
            source_path.insert(i, SPRINT_EFFECT)
            source_path.insert(i, NO_SPRINT_MORALE_EFFECT)
            source_path.insert(i, SWIFT_EFFECT)
            source_path.insert(i, NO_SWIFT_EFFECT)
            source_path.insert(i, SWIFT_OK_EFFECT)
            source_path.insert(i, DEPLOY_OK_EFFECT)
            source_path.insert(i, DEPLOY_EFFECT)
            source_path.insert(i, MEDIUM_EQUIP_PENALTY_EFFECT)
            source_path.insert(i, MEDIUM_EQUIP_PENALTY_SF_EFFECT)
            source_path.insert(i, MEDIUM_EQUIP_PENALTY_FLOOR_TAG_EFFECT)
            break
        
    # Edit Choc effect
    choc_obj = source_path.by_n("UnitEffect_Choc")
    effects_list = choc_obj.v.by_m("EffectsDescriptors")
    for effect in effects_list.v:
        if not hasattr(effect.v, "type"):
            continue
        # Remove Physical Damage Bonus
        if effect.v.type == "TUnitEffectIncreaseWeaponPhysicalDamagesDescriptor":
            effect.v.by_m("ModifierValue").v = str(CHOC_CQC_BONUSES["physical_damage_bonus"])
            # effects_list.v.remove(effect.index)
            # logger.info(f"Removed Choc physical damage bonus from {choc_obj.v.parent_row.namespace}")
        elif effect.v.type == "TBonusWeaponAimtimeEffectDescriptor":
            effect.v.by_m("ModifierValue").v = str(CHOC_CQC_BONUSES["aim_time_multiplier"])
        elif effect.v.type == "TUnitEffectAlterWeaponTempsEntreDeuxSalvesDescriptor":
            effect.v.by_m("ModifierValue").v = str(CHOC_CQC_BONUSES["salvo_reload_multiplier"])
        elif effect.v.type == "TUnitEffectAlterWeaponTempsEntreDeuxTirsDescriptor":
            effect.v.by_m("ModifierValue").v = str(CHOC_CQC_BONUSES["shot_reload_percentage"])

    # Modify sniper effects
    sniper_obj = source_path.by_n("UnitEffect_sniper")
    effects_list = sniper_obj.v.by_m("EffectsDescriptors")

    for effect in effects_list.v:
        if not hasattr(effect.v, "type"):
            continue

        if effect.v.type == "TUnitEffectIncreaseWeaponPhysicalDamagesDescriptor":
            effects_list.v.remove(effect.index)
            logger.info(f"Removed sniper damage bonus from {sniper_obj.v.parent_row.namespace}")
            break

    # Modify stress on miss
    stress_on_miss_objects = [
        ("UnitEffect_stressOnMiss_high", 140),
        ("UnitEffect_stressOnMiss_low", 80),
        ("UnitEffect_stressOnMiss_mid", 110),
    ]

    # Edit stress on miss effects
    for effect_name, suppress_damage in stress_on_miss_objects:
        stress_on_miss_obj = source_path.by_n(effect_name)
        effects_list = stress_on_miss_obj.v.by_m("EffectsDescriptors")
        for effect in effects_list.v:
            if not hasattr(effect.v, "type"):
                continue

            if effect.v.type != "TEffectInflictDamageDescriptor":
                continue
            if effect.v.by_m("DamageType").v == "~/EDamageType/Suppress":
                effect.v.by_m("DamageValue").v = str(suppress_damage)
                logger.info(f"Updated {effect_name.replace('UnitEffect_', '')} effect to "
                            f"{suppress_damage}")
                break
            
    _edit_veterancy_effects(source_path)
    _edit_airunit_effects(source_path)
    
    # Write experience hint texts to dictionary file.
    entries: List[Tuple[str, str]] = []
    for xp_type, data in VETERANCY_BONUSES.items():
        if xp_type in PACK_TYPES_VANILLA_LOCALIZATION:
            continue
        for xp_level, xp_data in data.items():
            body_token = xp_data["body_token"]
            body = xp_data["body"]
            if body_token:
                entries.append((body_token, body))

    # Write entries
    write_dictionary_entries(entries, dictionary_type="ingame")
            

def _evasion_descriptor_template(value: int) -> str:
    return (
        f"TUnitEffectBonusPrecisionWhenTargetedDescriptor"
        f"("
        f"    ModifierType = ~/ModifierType_Additionnel"
        f"    BonusPrecisionWhenTargeted = {value}"
        f")"
    )


def _vet_missing_descriptor_template(
    effect_type: str,
    value: Any,
    damage_type: str | None = None,
) -> str | None:
    if effect_type == "TUnitEffectIncreaseDamageTakenDescriptor" and damage_type is not None:
        return (
            f"TUnitEffectIncreaseDamageTakenDescriptor"
            f"("
            f"    ModifierType = ~/ModifierType_Pourcentage"
            f"    BonusDamage = {value}"
            f"    DamageType = {damage_type}"
            f")"
        )
    if effect_type == "TUnitEffectAlterWeaponTempsEntreDeuxSalvesDescriptor":
        return (
            f"TUnitEffectAlterWeaponTempsEntreDeuxSalvesDescriptor"
            f"("
            f"    ModifierType = ~/ModifierType_Multiplicatif"
            f"    ModifierValue = {value}"
            f")"
        )
    if effect_type == "TUnitEffectIncreaseSpeedDescriptor":
        return (
            f"TUnitEffectIncreaseSpeedDescriptor"
            f"("
            f"    ModifierType = ~/ModifierType_Pourcentage"
            f"    BonusSpeedBaseInPercent = {value}"
            f")"
        )
    return None


def _apply_vet_member_value(effect, effect_type: str, new_value: Any) -> None:
    if effect_type == "TUnitEffectIncreaseDamageTakenDescriptor":
        effect.v.by_m("BonusDamage").v = str(new_value)
    elif effect_type == "TUnitEffectBonusPrecisionWhenTargetedDescriptor":
        effect.v.by_m("BonusPrecisionWhenTargeted").v = str(new_value)
    elif effect_type == "TUnitEffectHealOverTimeDescriptor":
        effect.v.by_m("HealUnitsPerSecond").v = str(new_value)
    elif effect_type == "TUnitEffectIncreaseSpeedDescriptor":
        effect.v.by_m("BonusSpeedBaseInPercent").v = str(new_value)
    elif effect.v.by_m("ModifierValue", False):
        effect.v.by_m("ModifierValue").v = str(new_value)


def _apply_vet_effect_changes(
    source_path,
    vet_changes: dict[str, dict[Any, Any]],
) -> None:
    for effect_pack_ns, changes in vet_changes.items():
        row = source_path.find_by_cond(
            lambda r, ns=effect_pack_ns: r.namespace == ns,
            strict=False,
        )
        if not row:
            logger.warning(
                f"Effect pack {effect_pack_ns!r} not found in EffetsSurUnite.ndf; "
                f"skipping veterancy changes for this pack",
            )
            continue

        effects_list = row.v.by_m("EffectsDescriptors")

        for change_key, new_value in changes.items():
            if change_key == "add":
                continue

            if isinstance(change_key, tuple):
                effect_type, damage_type = change_key
            else:
                effect_type, damage_type = change_key, None

            effect = _find_vet_effect(effects_list, effect_type, damage_type)
            if effect:
                _apply_vet_member_value(effect, effect_type, new_value)
                change_label = (
                    f"{effect_type} ({damage_type})"
                    if damage_type is not None
                    else effect_type
                )
                logger.info(f"Updated {change_label} for {effect_pack_ns}")
            else:
                change_label = (
                    f"{effect_type} ({damage_type})"
                    if damage_type is not None
                    else effect_type
                )
                missing_template = _vet_missing_descriptor_template(
                    effect_type,
                    new_value,
                    damage_type,
                )
                if missing_template is not None:
                    effects_list.v.add(missing_template)
                    logger.info(f"Added {change_label} for {effect_pack_ns}")
                else:
                    logger.warning(
                        f"{change_label} not found in EffectsDescriptors for {effect_pack_ns}; "
                        f"expected to apply veterancy change {new_value!r}",
                    )

        if "add" in changes:
            for add_entry, args in changes["add"]:
                if add_entry == "evasion":
                    existing_evasion = find_obj_by_type(
                        effects_list.v,
                        "TUnitEffectBonusPrecisionWhenTargetedDescriptor",
                    )
                    if existing_evasion:
                        existing_evasion.v.by_m("BonusPrecisionWhenTargeted").v = str(args)
                        logger.info(
                            f"Updated TUnitEffectBonusPrecisionWhenTargetedDescriptor "
                            f"for {effect_pack_ns}",
                        )
                        continue
                    effect_str = _evasion_descriptor_template(args)
                else:
                    effect_fn, fn_args = add_entry, args
                    effect_str = effect_fn(*fn_args)
                effects_list.v.add(effect_str)


def _edit_veterancy_effects(source_path) -> None:
    """GameData/Generated/Gameplay/Effects/EffetsSurUnite.ndf"""
    logger.info("Modifying veterancy effects")

    _apply_vet_effect_changes(source_path, VETERANCY_EFFECT_CHANGES)
    _add_helo_attack_xp_effects(source_path)
    _apply_vet_effect_changes(source_path, VETERANCY_HELO_ATTACK_EFFECT_CHANGES)
    _clone_multiplicative_infantry_xp(source_path)
    _apply_vet_effect_changes(source_path, VETERANCY_SF_MULTIPLICATIVE_EFFECT_CHANGES)
    _convert_multiplicative_infantry_precision(source_path)
    _apply_post_patch_overrides(source_path)
    _mirror_avion_suppress_resist_as_stun_resist(source_path)


def _apply_post_patch_overrides(source_path) -> None:
    logger.info("Applying post-patch veterancy overrides")

    precision_types = (
        "TUnitEffectIncreaseWeaponPrecisionArretDescriptor",
        "TUnitEffectIncreaseWeaponPrecisionMouvementDescriptor",
    )
    for override in POST_PATCH_OVERRIDES:
        row = source_path.find_by_cond(
            lambda r, ns=override.effect_pack: r.namespace == ns,
            strict=False,
        )
        if not row:
            logger.warning(f"{override.effect_pack} not found; skipping post-patch override")
            continue
        effects_list = row.v.by_m("EffectsDescriptors")
        if override.precision_stationary is not None:
            for effect_type in precision_types:
                precision = find_obj_by_type(effects_list.v, effect_type)
                if not precision:
                    logger.warning(f"No {effect_type} on {override.effect_pack}")
                    continue
                mod_type = str(precision.v.by_m("ModifierType").v)
                if mod_type != "~/ModifierType_Additionnel":
                    logger.warning(
                        f"Unexpected ModifierType {mod_type!r} on "
                        f"{override.effect_pack} {effect_type}",
                    )
                    continue
                value = (
                    override.precision_moving
                    if effect_type == "TUnitEffectIncreaseWeaponPrecisionMouvementDescriptor"
                    and override.precision_moving is not None
                    else override.precision_stationary
                )
                precision.v.by_m("ModifierValue").v = str(value)
                logger.info(f"Set {effect_type} to {value} for {override.effect_pack}")
        elif override.precision_moving is not None:
            precision = find_obj_by_type(
                effects_list.v,
                "TUnitEffectIncreaseWeaponPrecisionMouvementDescriptor",
            )
            if precision:
                precision.v.by_m("ModifierValue").v = str(override.precision_moving)
        if override.suppress_resist_bonus_damage is not None:
            damage_taken = _find_vet_effect(
                effects_list,
                "TUnitEffectIncreaseDamageTakenDescriptor",
                "EDamageType/Suppress",
            )
            if damage_taken:
                damage_taken.v.by_m("BonusDamage").v = str(
                    override.suppress_resist_bonus_damage,
                )
                logger.info(
                    f"Set suppress resist to {override.suppress_resist_bonus_damage} "
                    f"for {override.effect_pack}",
                )
        if override.remove_evasion_descriptor:
            evasion = find_obj_by_type(
                effects_list.v,
                "TUnitEffectBonusPrecisionWhenTargetedDescriptor",
            )
            if evasion:
                effects_list.v.remove(evasion)
                logger.info(
                    f"Removed TUnitEffectBonusPrecisionWhenTargetedDescriptor "
                    f"from {override.effect_pack}",
                )
            else:
                logger.debug(
                    f"No TUnitEffectBonusPrecisionWhenTargetedDescriptor on "
                    f"{override.effect_pack}; nothing to remove",
                )
        elif override.evasion_bonus_precision_when_targeted is not None:
            evasion = find_obj_by_type(
                effects_list.v,
                "TUnitEffectBonusPrecisionWhenTargetedDescriptor",
            )
            if evasion:
                evasion.v.by_m("BonusPrecisionWhenTargeted").v = str(
                    override.evasion_bonus_precision_when_targeted,
                )
            else:
                effects_list.v.add(
                    _evasion_descriptor_template(
                        override.evasion_bonus_precision_when_targeted,
                    ),
                )


def _add_helo_attack_xp_effects(source_path) -> None:
    """Clone helo XP effect packs for attack helicopters (before base precision nerf)."""
    logger.info("Adding attack helicopter XP effect packs")

    for base_ns, guid in (
        ("UnitEffect_xp_rookie_helo", HELO_ATTACK_EFFECT_GUIDS["UnitEffect_xp_rookie_helo_attack"]),
        ("UnitEffect_xp_trained_helo", HELO_ATTACK_EFFECT_GUIDS["UnitEffect_xp_trained_helo_attack"]),
        ("UnitEffect_xp_veteran_helo", HELO_ATTACK_EFFECT_GUIDS["UnitEffect_xp_veteran_helo_attack"]),
        ("UnitEffect_xp_elite_helo", HELO_ATTACK_EFFECT_GUIDS["UnitEffect_xp_elite_helo_attack"]),
    ):
        attack_ns = f"{base_ns}_attack"
        new_effect = source_path.by_n(base_ns).copy()
        new_effect.namespace = attack_ns
        new_effect.v.by_m("DescriptorId").v = f"GUID:{{{guid}}}"
        new_effect.v.by_m("NameForDebug").v = f"'{attack_ns}'"
        source_path.add(new_effect)
        logger.info(f"Added new effect: {attack_ns}")


_AVION_VET_PACKS: tuple = (
    "UnitEffect_xp_rookie_avion",
    "UnitEffect_xp_trained_avion",
    "UnitEffect_xp_veteran_avion",
    "UnitEffect_xp_elite_avion",
)


def _mirror_avion_suppress_resist_as_stun_resist(source_path) -> None:
    """Mirror EDamageType/Suppress damage-taken bonuses with EDamageType/Stun on
    each ``UnitEffect_xp_*_avion`` pack so vet protection scales the stun pack
    threshold equivalently to the suppress pack threshold (see Mt=250 alignment
    in DamageModules.ndf editor).
    """
    logger.info("Mirroring avion vet suppress resistance as stun resistance")

    for pack_ns in _AVION_VET_PACKS:
        row = source_path.find_by_cond(
            lambda r, ns=pack_ns: r.namespace == ns,
            strict=False,
        )
        if not row:
            logger.debug(f"{pack_ns} not present; skipping stun-resist mirror")
            continue

        effects_list = row.v.by_m("EffectsDescriptors")
        suppress_effects = []
        has_stun_effect = False
        for effect in effects_list.v:
            if not hasattr(effect.v, "type"):
                continue
            if effect.v.type != "TUnitEffectIncreaseDamageTakenDescriptor":
                continue
            damage_type_membr = effect.v.by_m("DamageType", False)
            if damage_type_membr is None:
                continue
            # Strip any leading "~/" so we accept both qualified and bare forms
            # (vanilla EffetsSurUnite.ndf writes "EDamageType/Suppress" without
            # the "~/" prefix).
            damage_type = str(damage_type_membr.v).strip()
            if damage_type.startswith("~/"):
                damage_type = damage_type[2:]
            if damage_type == "EDamageType/Suppress":
                suppress_effects.append(effect)
            elif damage_type == "EDamageType/Stun":
                has_stun_effect = True

        if has_stun_effect:
            logger.debug(f"{pack_ns} already has Stun damage-taken descriptor; skipping")
            continue
        if not suppress_effects:
            logger.debug(f"{pack_ns} has no Suppress damage-taken descriptor; nothing to mirror")
            continue

        for effect in suppress_effects:
            modifier_type = str(effect.v.by_m("ModifierType").v)
            bonus_damage = str(effect.v.by_m("BonusDamage").v)
            # Match the vanilla format used by the existing Suppress entry
            # (no "~/" prefix on DamageType in EffetsSurUnite.ndf).
            mirror = (
                f"TUnitEffectIncreaseDamageTakenDescriptor"
                f"("
                f"    ModifierType = {modifier_type}"
                f"    BonusDamage = {bonus_damage}"
                f"    DamageType = EDamageType/Stun"
                f")"
            )
            effects_list.v.add(mirror)
            logger.info(
                f"Added Stun damage-taken descriptor to {pack_ns} "
                f"(ModifierType={modifier_type}, BonusDamage={bonus_damage})"
            )

def _clone_multiplicative_infantry_xp(source_path) -> None:
    """GameData/Generated/Gameplay/Effects/EffetsSurUnite.ndf"""
    logger.info("Cloning multiplicative infantry XP effects")

    for namespace, guid in MULTIPLICATIVE_INFANTRY_GUIDS.items():
        new_effect = source_path.by_n(f"UnitEffect_{namespace}").copy()
        new_effect.namespace = f"UnitEffect_{namespace}_multiplicative"
        current_debug_name = strip_quotes(new_effect.v.by_m("NameForDebug").v)
        new_effect.v.by_m("NameForDebug").v = f"'{current_debug_name}_multiplicative'"
        new_effect.v.by_m("DescriptorId").v = f"GUID:{{{guid}}}"
        source_path.add(new_effect)
        logger.info(f"Added new effect: {new_effect.namespace}")

    xp_elite_helo_sf = source_path.by_n("UnitEffect_xp_elite_helo").copy()
    xp_elite_helo_sf.namespace = "UnitEffect_xp_elite_helo_SF"
    xp_elite_helo_sf.v.by_m("DescriptorId").v = f"GUID:{{{ELITE_HELO_SF_GUID}}}"
    xp_elite_helo_sf.v.by_m("NameForDebug").v = "'UnitEffect_xp_elite_helo_SF'"
    source_path.add(xp_elite_helo_sf)
    _apply_vet_effect_changes(source_path, VETERANCY_RUNTIME_EFFECT_CHANGES)


def _convert_multiplicative_infantry_precision(source_path) -> None:
    """Convert additive weapon precision on multiplicative infantry XP packs."""
    logger.info("Converting multiplicative infantry XP precision modifiers")

    for namespace in MULTIPLICATIVE_INFANTRY_GUIDS:
        row = source_path.by_n(f"UnitEffect_{namespace}_multiplicative")
        effects_list = row.v.by_m("EffectsDescriptors")
        weapon_precision = find_obj_by_type(
            effects_list.v,
            "TUnitEffectIncreaseWeaponPrecisionArretDescriptor",
        )
        if weapon_precision:
            weapon_precision.v.by_m("ModifierType").v = "~/ModifierType_Multiplicatif"
            weapon_precision.v.by_m("ModifierValue").v = str(
                float(weapon_precision.v.by_m("ModifierValue").v) / 100.0 + 1.0,
            )
        weapon_precision = find_obj_by_type(
            effects_list.v,
            "TUnitEffectIncreaseWeaponPrecisionMouvementDescriptor",
        )
        if weapon_precision:
            weapon_precision.v.by_m("ModifierType").v = "~/ModifierType_Multiplicatif"
            weapon_precision.v.by_m("ModifierValue").v = str(
                float(weapon_precision.v.by_m("ModifierValue").v) / 100.0 + 1.0,
            )

def _edit_airunit_effects(source_path) -> None:
    """GameData/Generated/Gameplay/Effects/EffetsSurUnite.ndf"""
    logger.info("Modifying air unit effects")
    
    # Edit air unit cohesion effects
    cohesion_namespaces = [
        "AirUnit_Cohesion_Low",
        "AirUnit_Cohesion_Mediocre",
        "AirUnit_Cohesion_Normal",
    ]
    
    for namespace in cohesion_namespaces:
        effect_descr = source_path.by_n(f"UnitEffect_{namespace}")
        effects_list = effect_descr.v.by_m("EffectsDescriptors")
        
        # IncreaseWeaponPrecision
        precision_modifier_type = "TUnitEffectIncreaseWeaponPrecisionArretDescriptor"
        precision_modifier = find_obj_by_type(
            effects_list.v,
            precision_modifier_type,
        )
        if precision_modifier:
            effects_list.v.remove(precision_modifier)
            logger.info(f"Removed {precision_modifier_type} effect for {namespace}")
        else:
            logger.warning(f"No {precision_modifier_type} effect found for {namespace}")
        
        # IncreaseWeaponPrecisionMouvement
        precision_movement_modifier_type = "TUnitEffectIncreaseWeaponPrecisionMouvementDescriptor"
        precision_movement_modifier = find_obj_by_type(
            effects_list.v,
            precision_movement_modifier_type,
        )
        if precision_movement_modifier:
            effects_list.v.remove(precision_movement_modifier)
            logger.info(f"Removed {precision_movement_modifier_type} effect for {namespace}")
        else:
            logger.warning(f"No {precision_movement_modifier_type} effect found for {namespace}")