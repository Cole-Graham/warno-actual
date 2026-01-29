"""Functions for modifying EffetsSurUnite.ndf"""
from typing import List, Tuple
from src import ndf
from src.dics.veterancy.vet_bonuses import VETERANCY_BONUSES
from src.utils.dictionary_utils import write_dictionary_entries
from src.utils.ndf_utils import find_obj_by_type, strip_quotes
from src.constants.effects.capacities import (
    CHOC_MOVE_EFFECT,
    CHOC_MOVE_OK_EFFECT,
    NO_CHOC_MOVE_EFFECT,
    NO_CHOC_MOVE_MORALE_EFFECT,
    NO_SWIFT_EFFECT,
    SWIFT_EFFECT,
    SWIFT_OK_EFFECT,
    DEPLOY_EFFECT,
    DEPLOY_OK_EFFECT,
    MEDIUM_COHESION_LOSS_EFFECT,
    COHESION_LOSS_OK_EFFECT,
)
from src.utils.logging_utils import setup_logger

logger = setup_logger(__name__)

# TODO: Break this down into specific functions
def edit_gen_gp_gfx_effetssurunite(source_path) -> None:
    """GameData/Generated/Gameplay/Gfx/EffetsSurUnite.ndf"""
    logger.info("Modifying unit effects")

    # Add new effects
    for i, row in enumerate(source_path, start=1):
        if row.namespace == "UnitEffect_Choc":
            source_path.insert(i, CHOC_MOVE_EFFECT)
            source_path.insert(i, NO_CHOC_MOVE_EFFECT)
            source_path.insert(i, NO_CHOC_MOVE_MORALE_EFFECT)
            source_path.insert(i, SWIFT_EFFECT)
            source_path.insert(i, NO_SWIFT_EFFECT)
            source_path.insert(i, CHOC_MOVE_OK_EFFECT)
            source_path.insert(i, SWIFT_OK_EFFECT)
            source_path.insert(i, DEPLOY_OK_EFFECT)
            source_path.insert(i, DEPLOY_EFFECT)
            source_path.insert(i, MEDIUM_COHESION_LOSS_EFFECT)
            source_path.insert(i, COHESION_LOSS_OK_EFFECT)
            break

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

            if effect.v.type == "TEffectInflictSuppressDamageDescriptor":
                effect.v.by_m("SuppressDamageValue").v = str(suppress_damage)
                logger.info(f"Updated {effect_name.replace('UnitEffect_', '')} effect to "
                            f"{suppress_damage}")
                break
            
    _edit_veterancy_effects(source_path)
            
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
    """GameData/Generated/Gameplay/Gfx/EffetsSurUnite.ndf"""
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
        "UnitEffect_xp_veteran_helo": {"TUnitEffectHealOverTimeDescriptor": 6.2},
        "UnitEffect_xp_elite_helo": {"TUnitEffectHealOverTimeDescriptor": 8.4, "add": [(_add_evasion, (-5,))]},
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
    for row in source_path:
        if row.namespace not in vet_changes:
            continue

        effects_list = row.v.by_m("EffectsDescriptors")
        changes = vet_changes[row.namespace]

        for effect in effects_list.v:
            if not hasattr(effect.v, "type"):
                continue

            effect_type = effect.v.type
            if effect_type not in changes:
                continue

            if effect_type == "TUnitEffectBonusPrecisionWhenTargetedDescriptor":
                effect.v.by_m("BonusPrecisionWhenTargeted").v = str(changes[effect_type])

            elif effect_type == "TUnitEffectHealOverTimeDescriptor":
                effect.v.by_m("HealUnitsPerSecond").v = str(changes[effect_type])

            else:
                effect.v.by_m("ModifierValue").v = str(changes[effect_type])

            logger.info(f"Updated {effect_type} for {row.namespace}")

        if "add" in changes:
            for effect_fn, args in changes["add"]:  # noqa
                effect_str = effect_fn(*args)
                effects_list.v.add(effect_str)
    
    _add_multiplicative_infantry_xp(source_path)

def _add_multiplicative_infantry_xp(source_path) -> None:
    """GameData/Generated/Gameplay/Gfx/EffetsSurUnite.ndf"""
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
        
    xp_elite_helo = source_path.by_n("UnitEffect_xp_elite_helo").copy()
    xp_elite_helo.namespace = "UnitEffect_xp_elite_helo_SF"
    xp_elite_helo.v.by_m("DescriptorId").v = f"GUID:{{2967b45d-5b50-48ab-87f7-7ddeeb17f5f4}}"
    xp_elite_helo.v.by_m("NameForDebug").v = f"'UnitEffect_xp_elite_helo_SF'"
    new_effect = (
        f"TUnitEffectBonusPrecisionWhenTargetedDescriptor"
        f"("
        f"    ModifierType = ~/ModifierType_Additionnel"
        f"    BonusPrecisionWhenTargeted = -5"
        f")"
    )
    xp_elite_helo.v.by_m("EffectsDescriptors").v.add(new_effect)
    source_path.add(xp_elite_helo)
    
        