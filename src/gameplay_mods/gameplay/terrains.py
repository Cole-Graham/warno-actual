"""Functions for modifying Terrains.ndf"""

from src.utils.logging_utils import setup_logger
from src.utils.ndf_utils import strip_quotes, find_obj_by_type, is_obj_type

logger = setup_logger(__name__)


def edit_gameplay_terrains(source_path) -> None:
    """GameData/Gameplay/Terrains/Terrains.ndf"""
    logger.info("Editing terrain properties")

    # Add damage modifiers
    damage_modifications = {
        "DamageFamilies": [
            "12_7",
            "14_5",
            "sa_intermediate",
            "sa_full",
            "thermobarique",
            "pgb_bomb",
        ],
        "terrains": {
            "ForetDense": 0.5,
            "ForetLegere": 0.65,
            "PetitBatiment": 0.5,
            "Batiment": 0.5,
            "Ruin": 0.55,
        },
    }

    # SpeedModifierInfantry moved to GameData/Gameplay/Constantes/TerrainSpeedFactors.ndf
    # (InfantryTerrainSpeedFactors); see constantes/terrainspeedfactors.py
    other_modifications = {
        "ForetLegere": {
            "DissimulationModifierGroundAir": 12,
            "DissimulationModifierGroundGround": 12,
            "ConcealmentBonus": 2.5,
        },
        "PetitBatiment": {
            "ConcealmentBonus": 3.25,
        },
        "Batiment": {
            "ConcealmentBonus": 3.25,
        },
        "Ruin": {
            "DissimulationModifierGroundAir": 48,
            "ConcealmentBonus": 2.5,
        },
    }

    tgameplayterrainsregistration_template = find_obj_by_type(
        source_path, "TGameplayTerrainsRegistration")

    terrains_list = tgameplayterrainsregistration_template.v.by_m("Terrains")

    # First: for every terrain, each (DamageFamily, inner MAP) row — if there is
    # ResistanceFamily_infanterie, ensure ResistanceFamily_infanterieWA exists with the same value.
    for terrain_obj in terrains_list.v:
        if not is_obj_type(terrain_obj.v, "TGameplayTerrain"):
            continue

        damage_modifier_map = terrain_obj.v.by_m("DamageModifierPerFamilyAndResistance", False)
        if damage_modifier_map is None:
            continue

        logger.info("Ensuring infanterieWA mirrors for %s", terrain_obj.namespace)

        for damage_entry in damage_modifier_map.v:
            res_map = damage_entry.v
            inf_resistance = res_map.by_k("ResistanceFamily_infanterie", False)
            if inf_resistance is None:
                continue
            if res_map.by_k("ResistanceFamily_infanterieWA", False) is not None:
                continue

            res_map.add(f"(ResistanceFamily_infanterieWA, {inf_resistance.v})")
            logger.info(
                "Added ResistanceFamily_infanterieWA to %s on %s with value %s",
                damage_entry.k,
                terrain_obj.namespace,
                inf_resistance.v,
            )

    for terrain_name, modifier in damage_modifications["terrains"].items():
        terrain_obj = terrains_list.v.find_by_cond(
            lambda o: is_obj_type(o.v, "TGameplayTerrain") and
            strip_quotes(o.v.by_m("Name").v) == terrain_name, strict=False)

        if not terrain_obj:
            logger.warning(f"Terrain {terrain_name} not found")
            continue

        damage_modifier_map = terrain_obj.v.by_m("DamageModifierPerFamilyAndResistance")

        for damage_family in damage_modifications["DamageFamilies"]:
            damage_modifier_map.v.add(
                f"(DamageFamily_{damage_family}, MAP ["
                f"(ResistanceFamily_infanterie,{modifier}),"
                f"(ResistanceFamily_infanterieWA,{modifier})])",
            )
            logger.info(
                f"Added {damage_family} damage modifier {modifier} to {terrain_name} "
                "(infanterie + infanterieWA)",
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
