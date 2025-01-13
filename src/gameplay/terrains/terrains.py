"""Functions for modifying terrain properties."""

from src.utils.logging_utils import setup_logger

logger = setup_logger(__name__)


def is_obj_type(item, item_type: str) -> bool:
    """Check if an item is an object of a specific type."""
    return hasattr(item, 'type') and item.type == item_type


def edit_terrains(source) -> None:
    """Edit terrain properties in Terrains.ndf."""
    logger.info("Editing terrain properties")
    
    # Add full_balle damage modifiers
    terrain_modifiers = [
        ("ForetDense", "0.5"),
        ("ForetLegere", "0.65"),
        ("PetitBatiment", "0.5"),
        ("Batiment", "0.5"),
        ("Ruin", "0.55")
    ]
    
    for terrain, value in terrain_modifiers:
        terrain_obj = source.by_n(terrain).v
        damage_modifier_map = terrain_obj.by_m("DamageModifierPerFamilyAndResistance").v
        damage_modifier_map.add(
            f"(DamageFamily_full_balle, MAP [(ResistanceFamily_infanterie,{value})])")
        logger.info(f"Added full_balle damage modifier {value} to {terrain}")
    
    # Edit ForetLegere properties
    forest_light = source.by_n("ForetLegere").v
    forest_light.by_m("DissimulationModifierGroundAir").v = "20"
    forest_light.by_m("DissimulationModifierGroundGround").v = "23"
    logger.info("Updated ForetLegere dissimulation modifiers")
    
    # Edit Ruin properties
    ruin = source.by_n("Ruin").v
    ruin.by_m("DissimulationModifierGroundAir").v = "48"
    ruin.by_m("SpeedModifierInfantry").v = "0.7"
    logger.info("Updated Ruin modifiers")
    
    # Add infantry WA resistance to all terrains
    for terrain_obj in source:
        if not is_obj_type(terrain_obj.v, "TGameplayTerrain"):
            continue
            
        damage_modifier_map = terrain_obj.v.by_m("DamageModifierPerFamilyAndResistance", False)
        if damage_modifier_map is None:
            continue
            
        logger.info(f"Editing {terrain_obj.namespace}")
        
        for damage_family in damage_modifier_map.v:
            family_key = damage_family.k
            res_map = damage_family.v
            
            inf_resistance = res_map.by_k("ResistanceFamily_infanterie", False)
            if inf_resistance is not None:
                res_map.add(
                    f"(ResistanceFamily_infanterieWA, {inf_resistance.v})")
                logger.info(
                    f"Added ResistanceFamily_infanterieWA to {family_key} "
                    f"with value {inf_resistance.v}") 