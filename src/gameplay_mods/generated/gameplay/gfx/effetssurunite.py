"""Functions for modifying EffetsSurUnite.ndf"""
from typing import List, Tuple
from src import ndf
from src.dics.veterancy.vet_bonuses import VETERANCY_BONUSES
from src.utils.dictionary_utils import write_dictionary_entries
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
    _edit_veterancy_hints(source_path)
            
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

    def add_evasion(value: int) -> str:
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
        "UnitEffect_xp_rookie": {"TUnitEffectHealOverTimeDescriptor": 1.6},
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
        "UnitEffect_xp_rookie_arty": {"TUnitEffectHealOverTimeDescriptor": 1.6},
        "UnitEffect_xp_trained_arty": {"TUnitEffectHealOverTimeDescriptor": 3.0},
        "UnitEffect_xp_veteran_arty": {"TUnitEffectHealOverTimeDescriptor": 3.8},
        "UnitEffect_xp_elite_arty": {"TUnitEffectHealOverTimeDescriptor": 4.6},
        # Helo
        "UnitEffect_xp_rookie_helo": {"TUnitEffectHealOverTimeDescriptor": 1.6},
        "UnitEffect_xp_trained_helo": {"TUnitEffectHealOverTimeDescriptor": 4.2},
        "UnitEffect_xp_veteran_helo": {"TUnitEffectHealOverTimeDescriptor": 6.2},
        "UnitEffect_xp_elite_helo": {"TUnitEffectHealOverTimeDescriptor": 8.4, "add": [(add_evasion, (-5,))]},
        # Avion
        "UnitEffect_xp_trained_avion": {"TUnitEffectHealOverTimeDescriptor": 2},
        "UnitEffect_xp_veteran_avion": {
            "TUnitEffectBonusPrecisionWhenTargetedDescriptor": -4,
            "TUnitEffectIncreaseWeaponPrecisionMouvementDescriptor": 1.04,
        },
        "UnitEffect_xp_elite_avion": {
            "TUnitEffectBonusPrecisionWhenTargetedDescriptor": -8,
            "TUnitEffectIncreaseWeaponPrecisionMouvementDescriptor": 1.08,
        },
    }
    
    # Switch to multiplicative modifier for all veterancy accuracy bonuses
    infantry_xp_objects = [
        "xp_trained",
        "xp_trained_SF",
        "xp_veteran",
        "xp_veteran_SF",
        "xp_elite",
        "xp_elite_SF",
    ]
    for row in source_path:
        if not any(row.namespace.endswith(string) for string in infantry_xp_objects):
            continue
        
        effects_list = row.v.by_m("EffectsDescriptors")
        for effect in effects_list.v:
            if not hasattr(effect.v, "type"):
                continue
            effect_type = effect.v.type
            if effect_type == "TUnitEffectIncreaseWeaponPrecisionArretDescriptor":
                effect.v.by_m("ModifierType").v = "~/ModifierType_Multiplicatif"
                modifier_value = effect.v.by_m("ModifierValue").v
                effect.v.by_m("ModifierValue").v = str(float(modifier_value) / 100.0 + 1.0)
            elif effect_type == "TUnitEffectIncreaseWeaponPrecisionMouvementDescriptor":
                effect.v.by_m("ModifierType").v = "~/ModifierType_Multiplicatif"
                modifier_value = effect.v.by_m("ModifierValue").v
                effect.v.by_m("ModifierValue").v = str(float(modifier_value) / 100.0 + 1.0)

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
                
                
def _edit_veterancy_hints(source_path) -> None:
    """GameData/Generated/Gameplay/Gfx/ExperienceLevels.ndf"""
    logger.info("--------- editing ExperienceLevels.ndf ---------")
    logger.info("          Modifying plane veterancy hints       ")

    # Define experience pack mappings
    xp_packs = {
        "ExperienceLevelsPackDescriptor_XP_pack_simple_v3": {
            "pack_type": "simple_v3",
            "level_format": "simple_v3_{level}",
        },
        "ExperienceLevelsPackDescriptor_XP_pack_SF_v2": {
            "pack_type": "SF_v2",
            "level_format": "SF_v2_{level}",
        },
        "ExperienceLevelsPackDescriptor_XP_pack_artillery": {
            "pack_type": "artillery",
            "level_format": "artillery_{level}",
        },
        "ExperienceLevelsPackDescriptor_XP_pack_helico": {
            "pack_type": "helico",
            "level_format": "helico_{level}",
        },
        "ExperienceLevelsPackDescriptor_XP_pack_avion": {
            "pack_type": "avion",
            "level_format": "avion_{level}",
        },
    }

    for row in source_path:
        if row.namespace not in xp_packs:
            continue

        pack_info = xp_packs[row.namespace]
        pack_type = pack_info["pack_type"]

        try:
            xp_descr_list = row.v.by_m("ExperienceLevelsDescriptors").v

            for level, xp_descr in enumerate(xp_descr_list):
                if not isinstance(xp_descr.v, ndf.model.Object):
                    continue

                # Use index as level number (0-based)
                level_key = pack_info["level_format"].format(level=level)

                if level_key not in VETERANCY_BONUSES[pack_type]:
                    logger.warning(f"Missing veterancy data for {level_key} in {pack_type}")
                    continue

                body_token = VETERANCY_BONUSES[pack_type][level_key]["body_token"]
                xp_descr.v.by_m("HintBodyToken").v = f"'{body_token}'"
                logger.info(f"Modified dictionary token for level {level} of {row.namespace}")

        except Exception as e:
            logger.error(f"Failed to process {row.namespace}: {str(e)}")