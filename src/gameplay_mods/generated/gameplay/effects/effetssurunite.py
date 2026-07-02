"""Functions for modifying EffetsSurUnite.ndf"""
from typing import List, Tuple
from src import ndf
from src.dics.veterancy.vet_bonuses import VETERANCY_BONUSES
from src.utils.dictionary_utils import write_dictionary_entries
from src.utils.ndf_utils import find_obj_by_type, strip_quotes
from src.constants.effects import (
    CHOC_CQC_BONUSES,
    SPRINT_EFFECT,
    DEPLOY_EFFECT,
    DEPLOY_OK_EFFECT,
    MEDIUM_EQUIP_PENALTY_EFFECT,
    NO_SPRINT_MORALE_EFFECT,
    NO_SWIFT_EFFECT,
    SWIFT_EFFECT,
    SWIFT_OK_EFFECT,
)
from src.utils.logging_utils import setup_logger

logger = setup_logger(__name__)

# TODO: Break this down into specific functions
def edit_gen_gp_effects_effetssurunite(source_path) -> None:
    """GameData/Generated/Gameplay/Effects/EffetsSurUnite.ndf"""
    logger.info("Modifying unit effects")

    # Add new effects
    for i, row in enumerate(source_path, start=1):
        if row.namespace == "UnitEffect_Choc":
            source_path.insert(i, SPRINT_EFFECT)
            source_path.insert(i, NO_SPRINT_MORALE_EFFECT)
            source_path.insert(i, SWIFT_EFFECT)
            source_path.insert(i, NO_SWIFT_EFFECT)
            source_path.insert(i, SWIFT_OK_EFFECT)
            source_path.insert(i, DEPLOY_OK_EFFECT)
            source_path.insert(i, DEPLOY_EFFECT)
            source_path.insert(i, MEDIUM_EQUIP_PENALTY_EFFECT)
            break
        
    # Edit Choc effect
    choc_obj = source_path.by_n("UnitEffect_Choc")
    effects_list = choc_obj.v.by_m("EffectsDescriptors")
    for effect in effects_list.v:
        if not hasattr(effect.v, "type"):
            continue
        # Remove Physical Damage Bonus
        if effect.v.type == "TUnitEffectIncreaseWeaponPhysicalDamagesDescriptor":
            effects_list.v.remove(effect.index)
            logger.info(f"Removed Choc physical damage bonus from {choc_obj.v.parent_row.namespace}")
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
        for xp_level, xp_data in data.items():
            body_token = xp_data["body_token"]
            body = xp_data["body"]
            if body_token:
                entries.append((body_token, body))

    # Write entries
    write_dictionary_entries(entries, dictionary_type="ingame")
            

def _edit_veterancy_effects(source_path) -> None:
    """GameData/Generated/Gameplay/Effects/EffetsSurUnite.ndf"""
    logger.info("Modifying veterancy effects")

    def _add_evasion(value: int) -> str:
        effect_template = (
            f"TUnitEffectBonusPrecisionWhenTargetedDescriptor"
            f"("
            f"    ModifierType = ~/ModifierType_Additionnel"
            f"    BonusPrecisionWhenTargeted = {value}"
            f")"
        )
        return effect_template

    vet_changes = {
        # Default
        "UnitEffect_xp_rookie": {"TUnitEffectHealOverTimeDescriptor": 3.0},
        "UnitEffect_xp_trained": {"TUnitEffectHealOverTimeDescriptor": 4},
        "UnitEffect_xp_veteran": {
            "TUnitEffectHealOverTimeDescriptor": 4.8,
            "TUnitEffectAlterWeaponTempsEntreDeuxSalvesDescriptor": 0.83,
        },
        "UnitEffect_xp_elite": {
            "TUnitEffectHealOverTimeDescriptor": 5.6,
            "TUnitEffectAlterWeaponTempsEntreDeuxSalvesDescriptor": 0.76,
        },
        # SF
        "UnitEffect_xp_trained_SF": {"TUnitEffectHealOverTimeDescriptor": 4.8},
        "UnitEffect_xp_veteran_SF": {"TUnitEffectHealOverTimeDescriptor": 6.0},
        "UnitEffect_xp_elite_SF": {"TUnitEffectHealOverTimeDescriptor": 6.8},
        # Arty
        "UnitEffect_xp_rookie_arty": {"TUnitEffectHealOverTimeDescriptor": 3.0},
        "UnitEffect_xp_trained_arty": {"TUnitEffectHealOverTimeDescriptor": 3.0},
        "UnitEffect_xp_veteran_arty": {"TUnitEffectHealOverTimeDescriptor": 3.8},
        "UnitEffect_xp_elite_arty": {"TUnitEffectHealOverTimeDescriptor": 4.6},
        # Helo
        "UnitEffect_xp_rookie_helo": {"TUnitEffectHealOverTimeDescriptor": 3.0},
        "UnitEffect_xp_trained_helo": {"TUnitEffectHealOverTimeDescriptor": 4.2},
        "UnitEffect_xp_veteran_helo": {
            "TUnitEffectIncreaseDamageTakenDescriptor": -20,
            "TUnitEffectHealOverTimeDescriptor": 6.2
        },
        "UnitEffect_xp_elite_helo": {
            "TUnitEffectIncreaseDamageTakenDescriptor": -20,
            "TUnitEffectHealOverTimeDescriptor": 8.4, "add": [(_add_evasion, (-5,))]
        },
        # Avion
        "UnitEffect_xp_trained_avion": {"TUnitEffectHealOverTimeDescriptor": 2},
        "UnitEffect_xp_veteran_avion": {
            "TUnitEffectBonusPrecisionWhenTargetedDescriptor": -4,
            "TUnitEffectIncreaseWeaponPrecisionMouvementDescriptor": 4,
        },
        "UnitEffect_xp_elite_avion": {
            "TUnitEffectBonusPrecisionWhenTargetedDescriptor": -8,
            "TUnitEffectIncreaseWeaponPrecisionMouvementDescriptor": 8,
        },
    }

    # Apply specifically defined veterancy changes
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

        for effect_type, new_value in changes.items():
            if effect_type == "add":
                continue

            effect = effects_list.v.find_by_cond(
                lambda o, et=effect_type: hasattr(o.v, "type") and o.v.type == et,
                strict=False,
            )
            if effect:
                if effect_type == "TUnitEffectIncreaseDamageTakenDescriptor":
                    effect.v.by_m("BonusDamage").v = str(new_value)
                elif effect_type == "TUnitEffectBonusPrecisionWhenTargetedDescriptor":
                    effect.v.by_m("BonusPrecisionWhenTargeted").v = str(new_value)
                elif effect_type == "TUnitEffectHealOverTimeDescriptor":
                    effect.v.by_m("HealUnitsPerSecond").v = str(new_value)
                elif effect.v.by_m("ModifierValue", False):
                    effect.v.by_m("ModifierValue").v = str(new_value)
                logger.info(f"Updated {effect_type} for {effect_pack_ns}")
            else:
                logger.warning(
                    f"{effect_type} not found in EffectsDescriptors for {effect_pack_ns}; "
                    f"expected to apply veterancy change {new_value!r}",
                )

        if "add" in changes:
            for effect_fn, args in changes["add"]:  # noqa
                effect_str = effect_fn(*args)
                effects_list.v.add(effect_str)
    
    _add_helo_attack_xp_effects(source_path)
    _add_multiplicative_infantry_xp(source_path)
    _nerf_base_helo_xp_precision(source_path)
    _mirror_avion_suppress_resist_as_stun_resist(source_path)


_HELO_ATTACK_EFFECT_GUIDS: dict[str, str] = {
    "UnitEffect_xp_rookie_helo_attack": "30d8a0dd-0f87-429b-98e2-098aeb1a0b1e",
    "UnitEffect_xp_trained_helo_attack": "0c48af36-5a1d-401c-9952-ae4351b5f2ac",
    "UnitEffect_xp_veteran_helo_attack": "96e82bfe-107a-44fc-a76d-94a293e4a769",
    "UnitEffect_xp_elite_helo_attack": "fac2b968-dcf7-4e8d-baa1-ac3b79d13976",
}


def _add_helo_attack_xp_effects(source_path) -> None:
    """Clone helo XP effect packs for attack helicopters (before base precision nerf)."""
    logger.info("Adding attack helicopter XP effect packs")

    for base_ns, guid in (
        ("UnitEffect_xp_rookie_helo", _HELO_ATTACK_EFFECT_GUIDS["UnitEffect_xp_rookie_helo_attack"]),
        ("UnitEffect_xp_trained_helo", _HELO_ATTACK_EFFECT_GUIDS["UnitEffect_xp_trained_helo_attack"]),
        ("UnitEffect_xp_veteran_helo", _HELO_ATTACK_EFFECT_GUIDS["UnitEffect_xp_veteran_helo_attack"]),
        ("UnitEffect_xp_elite_helo", _HELO_ATTACK_EFFECT_GUIDS["UnitEffect_xp_elite_helo_attack"]),
    ):
        attack_ns = f"{base_ns}_attack"
        new_effect = source_path.by_n(base_ns).copy()
        new_effect.namespace = attack_ns
        new_effect.v.by_m("DescriptorId").v = f"GUID:{{{guid}}}"
        new_effect.v.by_m("NameForDebug").v = f"'{attack_ns}'"
        source_path.add(new_effect)
        logger.info(f"Added new effect: {attack_ns}")


def _nerf_base_helo_xp_precision(source_path) -> None:
    """Reduce base transport helo vet precision; run after any elite_helo copies (e.g. SF)."""
    logger.info("Nerfing base helicopter XP precision bonuses")

    precision_types = (
        "TUnitEffectIncreaseWeaponPrecisionArretDescriptor",
        "TUnitEffectIncreaseWeaponPrecisionMouvementDescriptor",
    )
    for pack_ns, modifier_value in (
        ("UnitEffect_xp_veteran_helo", 5),
        ("UnitEffect_xp_elite_helo", 10),
    ):
        row = source_path.find_by_cond(
            lambda r, ns=pack_ns: r.namespace == ns,
            strict=False,
        )
        if not row:
            logger.warning(f"{pack_ns} not found; skipping precision change")
            continue
        effects_list = row.v.by_m("EffectsDescriptors")
        for effect_type in precision_types:
            precision = find_obj_by_type(effects_list.v, effect_type)
            if not precision:
                logger.warning(f"No {effect_type} on {pack_ns}")
                continue
            mod_type = str(precision.v.by_m("ModifierType").v)
            if mod_type != "~/ModifierType_Additionnel":
                logger.warning(
                    f"Unexpected ModifierType {mod_type!r} on {pack_ns} {effect_type}; "
                    f"expected ~/ModifierType_Additionnel",
                )
                continue
            precision.v.by_m("ModifierValue").v = str(modifier_value)
            logger.info(f"Set {effect_type} to {modifier_value} for {pack_ns}")


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

def _add_multiplicative_infantry_xp(source_path) -> None:
    """GameData/Generated/Gameplay/Effects/EffetsSurUnite.ndf"""
    logger.info("Adding multiplicative infantry XP effects")

    infantry_xp_objects = {
        "xp_rookie": "93c3832b-179f-4f71-9c3e-0aaa51ad6563",
        "xp_trained": "38b2a348-2385-463c-8edb-722a5d9b37f3",
        "xp_trained_SF": "2b3b11d5-f08d-4428-82a2-7307ab6055d9",
        "xp_veteran": "d1b6e97c-24f3-4aec-a457-79c3262cc830",
        "xp_veteran_SF": "f125886e-e9d2-4f30-92d9-700303ccd8c6",
        "xp_elite": "b80fe588-b3b5-4f63-9587-75b254a2361e",
        "xp_elite_SF": "7b707579-3230-4884-a91f-b10dc4df0ddb",
    }
    
    for namespace, guid in infantry_xp_objects.items():
        new_effect = source_path.by_n(f"UnitEffect_{namespace}").copy()
        new_effect.namespace = f"UnitEffect_{namespace}_multiplicative"
        current_debug_name = strip_quotes(new_effect.v.by_m("NameForDebug").v)
        new_effect.v.by_m("NameForDebug").v = f"'{current_debug_name}_multiplicative'"
        new_effect.v.by_m("DescriptorId").v = f"GUID:{{{guid}}}"
        effects_list = new_effect.v.by_m("EffectsDescriptors")
        weapon_precision = find_obj_by_type(effects_list.v, "TUnitEffectIncreaseWeaponPrecisionArretDescriptor")
        if weapon_precision:
            weapon_precision.v.by_m("ModifierType").v = "~/ModifierType_Multiplicatif"
            weapon_precision.v.by_m("ModifierValue").v = str(
                float(weapon_precision.v.by_m("ModifierValue").v) / 100.0 + 1.0)
        weapon_precision = find_obj_by_type(effects_list.v, "TUnitEffectIncreaseWeaponPrecisionMouvementDescriptor")
        if weapon_precision:
            weapon_precision.v.by_m("ModifierType").v = "~/ModifierType_Multiplicatif"
            weapon_precision.v.by_m("ModifierValue").v = str(
                float(weapon_precision.v.by_m("ModifierValue").v) / 100.0 + 1.0)
        source_path.add(new_effect)
        logger.info(f"Added new effect: {new_effect.namespace}")
        
    xp_elite_helo_sf = source_path.by_n("UnitEffect_xp_elite_helo").copy()
    xp_elite_helo_sf.namespace = "UnitEffect_xp_elite_helo_SF"
    # modify stress resistance from 45% to 40%
    effects_list = xp_elite_helo_sf.v.by_m("EffectsDescriptors")
    damage_taken = find_obj_by_type(effects_list.v, "TUnitEffectIncreaseDamageTakenDescriptor")
    if damage_taken:
        damage_taken.v.by_m("BonusDamage").v = str(-40)
        logger.info(f"Updated stress resistance from 45% to 40% for {xp_elite_helo_sf.namespace}")
    else:
        logger.warning(f"No TUnitEffectIncreaseDamageTakenDescriptor effect found for {xp_elite_helo_sf.namespace}")
    xp_elite_helo_sf.v.by_m("DescriptorId").v = f"GUID:{{2967b45d-5b50-48ab-87f7-7ddeeb17f5f4}}"
    xp_elite_helo_sf.v.by_m("NameForDebug").v = f"'UnitEffect_xp_elite_helo_SF'"
    if not find_obj_by_type(
        effects_list.v,
        "TUnitEffectBonusPrecisionWhenTargetedDescriptor",
    ):
        effects_list.v.add(
            f"TUnitEffectBonusPrecisionWhenTargetedDescriptor"
            f"("
            f"    ModifierType = ~/ModifierType_Additionnel"
            f"    BonusPrecisionWhenTargeted = -5"
            f")"
        )
        logger.warning(f"Something changed, this effect should already be added to UnitEffect_xp_elite_helo block")
    source_path.add(xp_elite_helo_sf)
    
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