"""Functions for modifying veterancy effects."""

from src.utils.logging_utils import setup_logger

logger = setup_logger(__name__)


def edit_plane_veterancy(source) -> None:
    """Edit plane veterancy effects in EffetsSurUnite.ndf."""
    logger.info("Modifying plane veterancy effects")
    
    vet_changes = {
        "UnitEffect_xp_veteran": {
            "TUnitEffectAlterWeaponTempsEntreDeuxSalvesDescriptor": "0.83"
        },
        "UnitEffect_xp_elite": {
            "TUnitEffectAlterWeaponTempsEntreDeuxSalvesDescriptor": "0.76"
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
    
    for row in source:
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
            else:
                effect.v.by_m("ModifierValue").v = changes[effect_type]
                
            logger.info(f"Updated {effect_type} for {row.namespace}") 