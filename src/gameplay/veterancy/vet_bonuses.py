"""Functions for modifying experience levels."""

# from typing import List, Tuple

# from src import ModConfig
from src.dics.veterancy.vet_bonuses import VETERANCY_BONUSES
from src.utils.dictionary_utils import write_dictionary_entries
from src.utils.logging_utils import setup_logger
from src.utils.ndf_utils import ndf

logger = setup_logger(__name__)


def write_veterancy_tokens() -> None:
    """Write experience hint texts to dictionary file."""
    
    # Gather entries to write
    entries = dict()
    for xp_type, data in VETERANCY_BONUSES.items():
        for xp_level, xp_data in data.items():
            body_token = xp_data["body_token"]
            body = xp_data["body"]
            if body_token:
                entries.update({body_token: body})
    
    # Write entries
    write_dictionary_entries(entries, dictionary_type="ingame")


def edit_veterancy_effects(source_path) -> None:
    """Edit veterancy effects in EffetsSurUnite.ndf."""
    logger.info("Modifying veterancy effects")
    
    vet_changes = {
        # Default
        "UnitEffect_xp_rookie": {
            "TUnitEffectHealOverTimeDescriptor": "1.4"
        },
        "UnitEffect_xp_trained": {
            "TUnitEffectHealOverTimeDescriptor": "4"
        },
        "UnitEffect_xp_veteran": {
            "TUnitEffectHealOverTimeDescriptor": "4.8",
            "TUnitEffectAlterWeaponTempsEntreDeuxSalvesDescriptor": "0.83"
        },
        "UnitEffect_xp_elite": {
            "TUnitEffectHealOverTimeDescriptor": "5.6",
            "TUnitEffectAlterWeaponTempsEntreDeuxSalvesDescriptor": "0.76"
        },
        # SF
        "UnitEffect_xp_trained_SF": {
            "TUnitEffectHealOverTimeDescriptor": "4.8"
        },
        "UnitEffect_xp_veteran_SF": {
            "TUnitEffectHealOverTimeDescriptor": "6.0"
        },
        "UnitEffect_xp_elite_SF": {
            "TUnitEffectHealOverTimeDescriptor": "6.8"
        },
        # Arty
        "UnitEffect_xp_rookie_arty": {
            "TUnitEffectHealOverTimeDescriptor": "1.4"
        },
        "UnitEffect_xp_trained_arty": {
            "TUnitEffectHealOverTimeDescriptor": "3.0"
        },
        "UnitEffect_xp_veteran_arty": {
            "TUnitEffectHealOverTimeDescriptor": "3.8"
        },
        "UnitEffect_xp_elite_arty": {
            "TUnitEffectHealOverTimeDescriptor": "4.6"
        },
        # Helo
        "UnitEffect_xp_rookie_helo": {
            "TUnitEffectHealOverTimeDescriptor": "1.4"
        },
        "UnitEffect_xp_trained_helo": {
            "TUnitEffectHealOverTimeDescriptor": "4.2"
        },
        "UnitEffect_xp_veteran_helo": {
            "TUnitEffectHealOverTimeDescriptor": "6.2"
        },
        "UnitEffect_xp_elite_helo": {
            "TUnitEffectHealOverTimeDescriptor": "8.2"
        },
        # Avion
        "UnitEffect_xp_trained_avion": {
            "TUnitEffectHealOverTimeDescriptor": "2"
        },
        "UnitEffect_xp_veteran_avion": {
            "TUnitEffectBonusPrecisionWhenTargetedDescriptor": "-4",
            "TUnitEffectIncreaseWeaponPrecisionMouvementDescriptor": "4"
        },
        "UnitEffect_xp_elite_avion": {
            "TUnitEffectBonusPrecisionWhenTargetedDescriptor": "-8",
            "TUnitEffectIncreaseWeaponPrecisionMouvementDescriptor": "8"
        }
    }
    
    for row in source_path:
        if row.namespace not in vet_changes:
            continue
            
        effects_list = row.v.by_m("EffectsDescriptors").v
        changes = vet_changes[row.namespace]
        
        for effect in effects_list:
            if not hasattr(effect.v, 'type'):
                continue
                
            effect_type = effect.v.type
            if effect_type not in changes:
                continue
                
            if effect_type == "TUnitEffectBonusPrecisionWhenTargetedDescriptor":
                effect.v.by_m("BonusPrecisionWhenTargeted").v = changes[effect_type]
            elif effect_type == "TUnitEffectIncreaseWeaponPrecisionMouvementDescriptor":
                effect.v.by_m("ModifierValue").v = changes[effect_type]
            elif effect_type == "TUnitEffectHealOverTimeDescriptor":
                effect.v.by_m("HealUnitsPerSecond").v = changes[effect_type]
            else:
                effect.v.by_m("ModifierValue").v = changes[effect_type]
                
            logger.info(f"Updated {effect_type} for {row.namespace}")

     
def edit_veterancy_hints(source_path) -> None:
    """Edit veterancy hint texts in ExperienceLevels.ndf."""
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
            "level_format": "avion{level}",  # Note: no underscore for avion
        }
    }

    for row in source_path:
        if row.namespace not in xp_packs:
            continue
            
        pack_info = xp_packs[row.namespace]
        pack_type = pack_info["pack_type"]
        
        try:
            xp_descr_list = row.v.by_m("ExperienceLevelsDescriptors").v
            
            for xp_descr in xp_descr_list:
                if not isinstance(xp_descr.v, ndf.model.Object):
                    continue
                    
                # Extract level number from namespace
                descr_namespace = xp_descr.namespace
                if not (level_match := descr_namespace.split("_")[-1]).isdigit():
                    continue
                    
                level = level_match
                level_key = pack_info["level_format"].format(level=level)
                
                if level_key not in VETERANCY_BONUSES[pack_type]:
                    logger.warning(
                        f"Missing veterancy data for {level_key} in {pack_type}"
                    )
                    continue
                    
                body_token = VETERANCY_BONUSES[pack_type][level_key]["body_token"]
                xp_descr.v.by_m("HintBodyToken").v = f"'{body_token}'"
                logger.info(f"Modified {descr_namespace} for {row.namespace}")
                
        except Exception as e:
            logger.error(
                f"Failed to process {row.namespace}: {str(e)}"
            )