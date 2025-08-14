"""Functions for modifying Terrains.ndf"""

from src.utils.logging_utils import setup_logger
from src.utils.ndf_utils import strip_quotes, find_obj_by_type, is_obj_type
import ndf_parse as ndf

logger = setup_logger(__name__)


def edit_gameplay_terrains(source_path) -> None:
    """GameData/Gameplay/Terrains/Terrains.ndf"""
    logger.info("Editing terrain properties")

    # Add damage modifiers
    damage_modifications = {
        "DamageFamilies": ["sa_intermediate", "sa_full", "thermobarique"],
        "terrains": {
            "ForetDense": 0.5,
            "ForetLegere": 0.65,
            "PetitBatiment": 0.5,
            "Batiment": 0.5,
            "Ruin": 0.55,
        },
    }
    
    other_modifications = {
        "DefaultTerrain": {
            "SpeedModifierInfantry": 1.0,
        },
        "ForetLegere": {
            "DissimulationModifierGroundAir": 12,
            "DissimulationModifierGroundGround": 12,
            "SpeedModifierInfantry": 1.0,
            "ConcealmentBonus": 2.5,
        },
        "PetitBatiment": {
            "SpeedModifierInfantry": 1.0,
            "ConcealmentBonus": 3.25,
        },
        "Batiment": {
            "SpeedModifierInfantry": 1.0,
            "ConcealmentBonus": 3.25,
        },
        "Ruin": {
            "DissimulationModifierGroundAir": 48,
            "SpeedModifierInfantry": 0.7,
            "ConcealmentBonus": 2.5,
        },
    }

    tgameplayterrainsregistration_template = find_obj_by_type(
        source_path, "TGameplayTerrainsRegistration")
    
    terrains_list = tgameplayterrainsregistration_template.v.by_m("Terrains")

    for terrain_name, modifier in damage_modifications["terrains"].items():
        terrain_obj = terrains_list.v.find_by_cond(
            lambda o: is_obj_type(o.v, "TGameplayTerrain") and 
            strip_quotes(o.v.by_m("Name").v) == terrain_name, strict=False)
        
        if not terrain_obj:
            logger.warning(f"Terrain {terrain_name} not found")
            continue
        
        for damage_family in damage_modifications["DamageFamilies"]:
            damage_modifier_map = terrain_obj.v.by_m("DamageModifierPerFamilyAndResistance").v
            damage_modifier_map.add(
                f"(DamageFamily_{damage_family}, MAP [(ResistanceFamily_infanterie,{modifier})])"
            )
            logger.info(
                f"Added {damage_family} damage modifier {modifier} to {terrain_name}"
            )

    for terrain_name, modifier in other_modifications.items():
        terrain_obj = terrains_list.v.find_by_cond(
            lambda o: is_obj_type(o.v, "TGameplayTerrain") and 
            strip_quotes(o.v.by_m("Name").v) == terrain_name, strict=False)
        
        if not terrain_obj:
            logger.warning(f"Terrain {terrain_name} not found")
            continue

        for modifier_name, modifier_value in modifier.items():
            terrain_obj.v.by_m(modifier_name).v = str(modifier_value)
            logger.info(f"Updated {terrain_name} {modifier_name} to {modifier_value}")

    # Add infantry WA resistance to all terrains
    for terrain_obj in terrains_list.v:
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

                res_map.add(f"(ResistanceFamily_infanterieWA, {inf_resistance.v})")
                logger.info(f"Added ResistanceFamily_infanterieWA to {family_key} " f"with value {inf_resistance.v}")
