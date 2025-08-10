"""Functions for modifying terrain properties."""

from src.utils.logging_utils import setup_logger
from src.utils.ndf_utils import strip_quotes
import ndf_parse as ndf

logger = setup_logger(__name__)


def is_obj_type(item, item_type: str) -> bool:
    """Check if an item is an object of a specific type."""
    return hasattr(item, "type") and item.type == item_type


def edit_terrains(source_path) -> None:
    """GameData/Gameplay/Terrains/Terrains.ndf"""
    logger.info("Editing terrain properties")

    # Add damage modifiers
    terrain_modifiers_dict = {
        "ForetDense": "0.5",
        "ForetLegere": "0.65",
        "PetitBatiment": "0.5",
        "Batiment": "0.5",
        "Ruin": "0.55",
    }

    for row in source_path:
        if not isinstance(row.v, ndf.model.Object):
            continue

        if row.v.type == "TGameplayTerrainsRegistration":
            tgameplayterrainsregistration_template = row.v
            terrains = tgameplayterrainsregistration_template.by_m("Terrains").v
            break

    for terrain_obj in terrains:
        if not is_obj_type(terrain_obj.v, "TGameplayTerrain"):
            continue

        terrain_name = strip_quotes(terrain_obj.v.by_m("Name").v)
        if terrain_name in terrain_modifiers_dict:

            damage_modifier_map = terrain_obj.v.by_m("DamageModifierPerFamilyAndResistance").v
            damage_modifier_map.add(
                f"(DamageFamily_sa_intermediate, MAP [(ResistanceFamily_infanterie,{terrain_modifiers_dict[terrain_name]})])"
            )
            logger.info(
                f"Added sa_intermediate damage modifier {terrain_modifiers_dict[terrain_name]} to {terrain_name}"
            )

            damage_modifier_map.add(
                f"(DamageFamily_sa_full, MAP [(ResistanceFamily_infanterie,{terrain_modifiers_dict[terrain_name]})])"
            )
            logger.info(f"Added sa_full damage modifier {terrain_modifiers_dict[terrain_name]} to {terrain_name}")

            damage_modifier_map.add(
                f"(DamageFamily_thermobarique, MAP [(ResistanceFamily_infanterie,{terrain_modifiers_dict[terrain_name]})])"
            )
            logger.info(f"Added thermobarique damage modifier {terrain_modifiers_dict[terrain_name]} to {terrain_name}")

        if terrain_name == "DefaultTerrain":
            terrain_obj.v.by_m("SpeedModifierInfantry").v = "1.0"
            logger.info("Updated DefaultTerrain speed modifier")

        elif terrain_name == "ForetLegere":
            terrain_obj.v.by_m("DissimulationModifierGroundAir").v = "12"
            terrain_obj.v.by_m("DissimulationModifierGroundGround").v = "12"
            logger.info("Updated ForetLegere dissimulation modifiers")
            terrain_obj.v.by_m("SpeedModifierInfantry").v = "1.0"
            logger.info("Updated ForetLegere speed modifier")
            terrain_obj.v.by_m("ConcealmentBonus").v = "2.5"
            logger.info("Updated ForetLegere concealment bonus")

        elif terrain_name == "PetitBatiment":
            terrain_obj.v.by_m("SpeedModifierInfantry").v = "1.0"
            logger.info("Updated PetitBatiment speed modifier")
            terrain_obj.v.by_m("ConcealmentBonus").v = "3.25"
            logger.info("Updated PetitBatiment concealment bonus")

        elif terrain_name == "Batiment":
            terrain_obj.v.by_m("SpeedModifierInfantry").v = "1.0"
            logger.info("Updated Batiment speed modifier")
            terrain_obj.v.by_m("ConcealmentBonus").v = "3.25"
            logger.info("Updated Batiment concealment bonus")

        elif terrain_name == "Ruin":
            terrain_obj.v.by_m("DissimulationModifierGroundAir").v = "48"
            logger.info("Updated Ruin dissimulation modifier")
            terrain_obj.v.by_m("SpeedModifierInfantry").v = "0.7"
            logger.info("Updated Ruin speed modifier")
            terrain_obj.v.by_m("ConcealmentBonus").v = "2.5"
            logger.info("Updated Ruin concealment bonus")

    # Add infantry WA resistance to all terrains
    for terrain_obj in terrains:
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
